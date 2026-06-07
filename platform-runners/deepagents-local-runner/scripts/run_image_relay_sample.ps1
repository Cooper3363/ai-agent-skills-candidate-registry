param(
    [switch]$Execute,
    [switch]$WriteReport,
    [string]$OutputRoot = "",
    [string]$ReportPath = "",
    [string]$FallbackReportRoot = ""
)

$ErrorActionPreference = "Stop"

$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$RunnerRoot = Split-Path -Parent $ScriptRoot
$RepoRoot = Split-Path -Parent (Split-Path -Parent $RunnerRoot)
if (-not $ReportPath) {
    $ReportPath = Join-Path $RepoRoot "skills\smb-callable-candidate-skills\REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md"
}
if (-not $OutputRoot) {
    $OutputRoot = Join-Path $RunnerRoot "media-smoke\real-media-minimal-samples"
}
if (-not $FallbackReportRoot) {
    $FallbackReportRoot = Join-Path $RunnerRoot "media-smoke\reports"
}

$Cases = @(
    @{
        candidate_id = "marketing_real_poster_banner_agent_candidate"
        title = "Mock event poster"
        prompt = "Create a clean square poster for a fictional small stationery shop. Text: Weekend Stationery Sale, Friday to Sunday, notebooks and pens. Use a friendly modern retail style. Do not include real brand names, logos, people, trademarks, copyrighted characters, or absolute claims."
        triggers = @("brand_or_trademark", "people_or_portrait", "pricing_or_promotion_claim", "copyright_or_policy_sensitive_content")
    },
    @{
        candidate_id = "ecommerce_product_main_image_agent_candidate"
        title = "Mock product hero image"
        prompt = "Create a clean ecommerce hero image for a fictional 500ml stainless steel thermos in matte white on a neutral background. Use mock product attributes only. Do not include real brand names, logos, certifications, packaging replicas, people, or misleading performance claims."
        triggers = @("product_misrepresentation", "trademark_or_packaging_risk", "fake_certification", "unclear_specs")
    },
    @{
        candidate_id = "store_menu_poster_generation_candidate"
        title = "Mock menu poster"
        prompt = "Create a simple square menu poster for a fictional noodle shop. Menu: Tomato Noodles 18, Mushroom Noodles 20, Iced Tea 8. Use a warm casual style. Do not include real logos, real restaurant names, health claims, copyrighted artwork, or misleading promotion claims."
        triggers = @("price_or_menu_uncertainty", "food_health_claim", "trademark_or_font_risk", "promotion_promise")
    }
)

function Get-EnvValue {
    param([string]$Name, [string]$Fallback = "")
    $value = [Environment]::GetEnvironmentVariable($Name, "Process")
    if ([string]::IsNullOrWhiteSpace($value)) {
        $value = [Environment]::GetEnvironmentVariable($Name, "User")
    }
    if ([string]::IsNullOrWhiteSpace($value)) {
        $value = [Environment]::GetEnvironmentVariable($Name, "Machine")
    }
    if ([string]::IsNullOrWhiteSpace($value)) {
        return $Fallback
    }
    return $value.Trim()
}

function Get-RouteConfig {
    $baseUrl = Get-EnvValue "IMAGE_RELAY_BASE_URL"
    if (-not $baseUrl) { $baseUrl = Get-EnvValue "OPENAI_BASE_URL" }
    $apiKey = Get-EnvValue "IMAGE_RELAY_API_KEY"
    if (-not $apiKey) { $apiKey = Get-EnvValue "OPENAI_API_KEY" }
    $endpoint = Get-EnvValue "IMAGE_RELAY_ENDPOINT" "/images/generations"
    if (-not $endpoint.StartsWith("/")) { $endpoint = "/" + $endpoint }
    return @{
        approved = ((Get-EnvValue "REAL_MEDIA_SMOKE_APPROVED") -eq "1")
        has_base_url = -not [string]::IsNullOrWhiteSpace($baseUrl)
        has_api_key = -not [string]::IsNullOrWhiteSpace($apiKey)
        base_url = $baseUrl
        api_key = $apiKey
        endpoint = $endpoint
        model = Get-EnvValue "IMAGE_RELAY_MODEL" "gpt-image-1"
        size = Get-EnvValue "IMAGE_RELAY_SIZE" "1024x1024"
        response_format = Get-EnvValue "IMAGE_RELAY_RESPONSE_FORMAT" "b64_json"
    }
}

function Get-RouteLabel {
    param($Config)
    if (-not $Config.has_base_url) { return "missing" }
    return ($Config.base_url.TrimEnd("/") + $Config.endpoint)
}

function Get-SafeSlug {
    param([string]$Text)
    return (($Text -replace "[^a-zA-Z0-9_.-]+", "-").Trim("-"))
}

function New-BlockedRows {
    param($Config, [bool]$ExecuteMode)
    $findings = New-Object System.Collections.Generic.List[string]
    if (-not $ExecuteMode) { $findings.Add("execute flag not set; preflight only") }
    if (-not $Config.approved) { $findings.Add("REAL_MEDIA_SMOKE_APPROVED=1 is required") }
    if (-not $Config.has_base_url) { $findings.Add("IMAGE_RELAY_BASE_URL or OPENAI_BASE_URL is required") }
    if (-not $Config.has_api_key) { $findings.Add("IMAGE_RELAY_API_KEY or OPENAI_API_KEY is required") }
    if ($findings.Count -eq 0) { return @() }

    $route = Get-RouteLabel $Config
    return @($Cases | ForEach-Object {
        @{
            candidate_id = $_.candidate_id
            status = "blocked"
            provider_route = $route
            output_path = "-"
            usage_or_cost_note = "not_run"
            findings = @($findings)
        }
    })
}

function Invoke-ImageRelay {
    param($Config, [string]$Prompt)
    $uri = Get-RouteLabel $Config
    $payload = @{
        model = $Config.model
        prompt = $Prompt
        size = $Config.size
        n = 1
    }
    if ($Config.response_format) {
        $payload.response_format = $Config.response_format
    }
    $headers = @{
        Authorization = "Bearer $($Config.api_key)"
        "Content-Type" = "application/json"
    }
    $body = $payload | ConvertTo-Json -Depth 8
    return Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -Body $body -TimeoutSec 120
}

function Save-ImageResponse {
    param($Response, [string]$OutputPath)
    if (-not $Response.data -or $Response.data.Count -lt 1) {
        throw "image response did not include data[0]"
    }
    $first = $Response.data[0]
    if ($first.b64_json) {
        [IO.File]::WriteAllBytes($OutputPath, [Convert]::FromBase64String($first.b64_json))
        return $OutputPath
    }
    if ($first.url) {
        Invoke-WebRequest -Uri $first.url -OutFile $OutputPath -TimeoutSec 120 | Out-Null
        return $OutputPath
    }
    throw "image response did not include b64_json or url"
}

function Invoke-Samples {
    param($Config, [string]$Root)
    $runDir = Join-Path $Root (Get-Date -Format "yyyyMMdd-HHmmss")
    New-Item -ItemType Directory -Force -Path $runDir | Out-Null
    $route = Get-RouteLabel $Config
    $rows = New-Object System.Collections.Generic.List[hashtable]

    foreach ($case in $Cases) {
        $outputPath = Join-Path $runDir ((Get-SafeSlug $case.candidate_id) + ".png")
        try {
            $started = Get-Date
            $response = Invoke-ImageRelay -Config $Config -Prompt $case.prompt
            $saved = Save-ImageResponse -Response $response -OutputPath $outputPath
            $elapsed = [Math]::Round(((Get-Date) - $started).TotalSeconds, 2)
            $usageNote = "elapsed_seconds=$elapsed"
            if ($response.usage) {
                $usageNote += "; usage=" + (($response.usage | ConvertTo-Json -Compress -Depth 8) -replace "\|", "/")
            }
            $rows.Add(@{
                candidate_id = $case.candidate_id
                status = "passed"
                provider_route = $route
                output_path = $saved
                usage_or_cost_note = $usageNote
                findings = @(
                    "manual_review_required",
                    "content_safety_status=provider_and_platform_review_required",
                    ("triggers=" + ($case.triggers -join ","))
                )
            })
        } catch {
            $rows.Add(@{
                candidate_id = $case.candidate_id
                status = "failed"
                provider_route = $route
                output_path = "-"
                usage_or_cost_note = "not_available"
                findings = @($_.Exception.GetType().Name, ($_.Exception.Message -replace "\|", "/"))
            })
        }
    }
    return @($rows)
}

function ConvertTo-Report {
    param($Config, [array]$Rows, [string]$Root, [bool]$ExecuteMode)
    $counts = @{
        passed = 0
        needs_fix = 0
        blocked = 0
        failed = 0
    }
    foreach ($row in $Rows) {
        if ($counts.ContainsKey($row.status)) { $counts[$row.status]++ }
    }

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add("# REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT")
    $lines.Add("")
    $lines.Add("Generated: " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss"))
    $lines.Add("")
    $lines.Add("## Summary")
    $lines.Add("")
    $lines.Add("- Execute mode: " + ($ExecuteMode.ToString().ToLowerInvariant()))
    $lines.Add("- Approval env present: " + ($Config.approved.ToString().ToLowerInvariant()))
    $lines.Add("- Relay base URL configured: " + ($Config.has_base_url.ToString().ToLowerInvariant()))
    $lines.Add("- Relay API key configured: " + ($Config.has_api_key.ToString().ToLowerInvariant()))
    $lines.Add("- Model: ``$($Config.model)``")
    $lines.Add("- Output root: ``$Root``")
    $lines.Add("- API keys and secrets are not printed or written by this report.")
    $lines.Add("")
    $lines.Add("## Result Counts")
    $lines.Add("")
    $lines.Add("- passed: " + $counts.passed)
    $lines.Add("- needs_fix: " + $counts.needs_fix)
    $lines.Add("- blocked: " + $counts.blocked)
    $lines.Add("- failed: " + $counts.failed)
    $lines.Add("")
    $lines.Add("## Results")
    $lines.Add("")
    $lines.Add("| candidate_id | status | provider_route | output_path | usage_or_cost_note | findings |")
    $lines.Add("| --- | --- | --- | --- | --- | --- |")
    foreach ($row in $Rows) {
        $findings = if ($row.findings) { ($row.findings -join "; ") } else { "none" }
        $lines.Add("| ``$($row.candidate_id)`` | $($row.status) | $($row.provider_route) | $($row.output_path) | $($row.usage_or_cost_note) | $findings |")
    }
    $lines.Add("")
    $lines.Add("## Hard Boundaries")
    $lines.Add("")
    @(
        "max_images_per_candidate=1",
        "total_max_images=3",
        "max_auto_retries=0",
        "sandbox_output_only=true",
        "no_publish=true",
        "no_customer_callable=true",
        "manual_review_required=true",
        "key_visible_to_testbench=false",
        "write_stable_registry=false",
        "write_business_system=false",
        "upload_customer_assets=false"
    ) | ForEach-Object { $lines.Add("- ``$_``") }
    $lines.Add("")
    $lines.Add("## Notes")
    $lines.Add("")
    $lines.Add("- A passed result only means a controlled minimal mock image sample succeeded.")
    $lines.Add("- It does not make the candidate customer-callable or stable-delivery ready.")
    $lines.Add("- Generated files must remain in a gitignored sandbox output directory.")
    return ($lines -join "`n") + "`n"
}

$Config = Get-RouteConfig
$Rows = New-BlockedRows -Config $Config -ExecuteMode ([bool]$Execute)
if ($Rows.Count -eq 0) {
    $Rows = Invoke-Samples -Config $Config -Root $OutputRoot
}
$Report = ConvertTo-Report -Config $Config -Rows $Rows -Root $OutputRoot -ExecuteMode ([bool]$Execute)
if ($WriteReport) {
    try {
        $reportDir = Split-Path -Parent $ReportPath
        if ($reportDir) {
            New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
        }
        Set-Content -LiteralPath $ReportPath -Value $Report -Encoding UTF8
    } catch {
        New-Item -ItemType Directory -Force -Path $FallbackReportRoot | Out-Null
        $fallbackPath = Join-Path $FallbackReportRoot "REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md"
        Set-Content -LiteralPath $fallbackPath -Value $Report -Encoding UTF8
        Write-Output "report_write_fallback=$fallbackPath"
    }
}
Write-Output $Report

if (($Rows | Where-Object { $_.status -eq "blocked" }).Count -gt 0) { exit 3 }
if (($Rows | Where-Object { $_.status -eq "failed" }).Count -gt 0) { exit 2 }
if (($Rows | Where-Object { $_.status -eq "needs_fix" }).Count -gt 0) { exit 1 }
exit 0
