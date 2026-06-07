# DeepAgents Local Runner

This runner connects the AI.Skills stable library and SMB candidate draft library to `langchain-ai/deepagents` for local smoke testing.

It is a local trial harness only. A successful run here does not promote any candidate to customer-callable stable delivery.

## What It Loads

- Stable baseline: 13 Skills from `skills/p0-first-13-platform-callable-skills/skills`
- Draft L3 candidates: 4 Skills from:
  - `skills/p0-six-department-draft-l3-skills/skills`
  - `skills/smb-candidate-draft-l3-skills/skills`
- Candidate cards from `skills/smb-callable-candidate-skills/candidates`:
  - `mock_callable`
  - `dry_run_callable`
  - `deepagents_smoke_passed`
  - `component_only`
  - `draft_l3` when no formal draft L3 Skill package already exists

## Runtime

Use `uv` and an isolated virtual environment:

```powershell
uv sync
```

Copy `.env.example` to `.env` and fill:

```text
OPENAI_API_KEY=your-relay-key
OPENAI_BASE_URL=https://your-openai-compatible-relay/v1
DEEPAGENTS_MODEL=openai:gpt-5.5
```

The key is never stored in this repo.

## Commands

Discovery only:

```powershell
uv run python -m deepagents_local_runner.run_discovery
```

Preflight and optional model smoke:

```powershell
uv run python -m deepagents_local_runner.run_smoke --write-report
```

If `.env` is missing or has no API key, the smoke command writes a preflight report and skips model calls.

Controlled image relay minimal sample smoke:

```powershell
uv run python -m deepagents_local_runner.run_image_relay_sample --write-report
```

Windows PowerShell fallback, for environments without `uv` or `python` on PATH:

```powershell
.\scripts\run_image_relay_sample.ps1 -WriteReport
```

If local PowerShell script execution is disabled, use a process-scoped bypass without changing machine policy:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_image_relay_sample.ps1 -WriteReport
```

Write the audit report to a sandbox path first:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_image_relay_sample.ps1 -WriteReport -ReportPath .\media-smoke\reports\REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md
```

The image relay command defaults to preflight/blocked mode. It only calls an image relay when all of these are true:

- `--execute` is passed.
- For PowerShell, `-Execute` is passed.
- `REAL_MEDIA_SMOKE_APPROVED=1` is present in the process environment.
- `IMAGE_RELAY_BASE_URL` or `OPENAI_BASE_URL` is configured.
- `IMAGE_RELAY_API_KEY` or `OPENAI_API_KEY` is configured.

Example with platform-managed environment variables:

```powershell
uv run python -m deepagents_local_runner.run_image_relay_sample --execute --write-report
```

PowerShell:

```powershell
.\scripts\run_image_relay_sample.ps1 -Execute -WriteReport
```

PowerShell with process-scoped execution-policy bypass:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\run_image_relay_sample.ps1 -Execute -WriteReport
```

If the default report path is not writable, the runner falls back to `media-smoke/reports/`. You can also pass `-ReportPath` on PowerShell or `--report-path` on Python to write the report to a sandbox location first.

The command never writes or prints API keys. Outputs are written only to gitignored sandbox directories such as `media-smoke/`, `generated-media/`, or `real-smoke-output/`. A successful run writes the audit report to:

```text
skills/smb-callable-candidate-skills/REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md
```

## Safety Boundary

The runner exposes no business action tools. It does not send email or SMS, write CRM/calendar/tasks, crawl pages, upload products, issue refunds, modify inventory, call SEO APIs, or generate images.

DeepAgents receives Skill files through an ephemeral state backend and is configured with filesystem write-deny permissions. Only mock prompts and local Skill metadata are used.

The separate image relay minimal sample command is not part of normal DeepAgents smoke. It is gated by explicit command-center approval, environment-managed routing, one-image-per-candidate limits, and sandbox-only output. Passing that smoke does not promote any candidate to stable delivery or customer-callable status.
