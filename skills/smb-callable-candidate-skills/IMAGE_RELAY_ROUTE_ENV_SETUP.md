# IMAGE_RELAY_ROUTE_ENV_SETUP

Date: 2026-06-05

## Purpose

This handoff defines the platform-side environment needed to rerun the approved minimal real image sample smoke for 3 OpenAI-compatible image relay candidates.

The runner has been added, but the current testbench environment does not expose a platform-managed image relay route or key. The current block is therefore `route_env_not_configured`, not candidate failure.

## Approved Scope

Only these 3 candidates are approved for minimal real image sample smoke:

| candidate_id | max sample |
| --- | --- |
| `marketing_real_poster_banner_agent_candidate` | 1 mock event poster image |
| `ecommerce_product_main_image_agent_candidate` | 1 mock product hero image |
| `store_menu_poster_generation_candidate` | 1 mock menu poster image |

No other media candidate is approved for real generation by this handoff.

## Required Environment Variables

Set these in the platform runner environment or secrets manager. Do not write them to repo files.

| variable | required | note |
| --- | --- | --- |
| `REAL_MEDIA_SMOKE_APPROVED` | yes | Must be `1` for the runner to execute. |
| `IMAGE_RELAY_BASE_URL` or `OPENAI_BASE_URL` | yes | OpenAI-compatible relay base URL, for example a `/v1` base. |
| `IMAGE_RELAY_API_KEY` or `OPENAI_API_KEY` | yes | Secret value from platform/secrets manager only. |
| `IMAGE_RELAY_ENDPOINT` | optional | Defaults to `/images/generations`. |
| `IMAGE_RELAY_MODEL` | optional | Defaults to `gpt-image-1`; override if relay uses another image-capable model id. |
| `IMAGE_RELAY_SIZE` | optional | Defaults to `1024x1024`. |
| `IMAGE_RELAY_RESPONSE_FORMAT` | optional | Defaults to `b64_json`; may be changed if the relay returns URLs. |

## Prohibited Handling

- Do not commit `.env` or secret files.
- Do not write the relay key into markdown, YAML, JSON, scripts, test reports, or command history captures.
- Do not print the key in logs.
- Do not pass the key as a literal command-line argument.
- Do not upload real customer, employee, candidate, brand, trademark, copyrighted, or third-party assets.
- Do not publish generated outputs or write them to customer/business systems.
- Do not copy generated media into the stable delivery repository.

## Runner Entrypoints

Python entrypoint:

```powershell
uv run python -m deepagents_local_runner.run_image_relay_sample --execute --write-report
```

PowerShell fallback:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File X:\codexwork\ai-agent-skills-candidate-registry\platform-runners\deepagents-local-runner\scripts\run_image_relay_sample.ps1 -Execute -WriteReport
```

If the formal result path is not writable from the runner process, write to a gitignored sandbox report first:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File X:\codexwork\ai-agent-skills-candidate-registry\platform-runners\deepagents-local-runner\scripts\run_image_relay_sample.ps1 -Execute -WriteReport -ReportPath X:\codexwork\ai-agent-skills-candidate-registry\platform-runners\deepagents-local-runner\media-smoke\reports\REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md
```

The testbench may then summarize that sandbox report into the formal result file without exposing keys.

The runner will block unless `REAL_MEDIA_SMOKE_APPROVED=1`, a relay base URL, and a relay key are present in the environment.

## Output Location

Generated files must remain in a gitignored sandbox path, such as:

- `platform-runners/deepagents-local-runner/media-smoke/`
- `platform-runners/deepagents-local-runner/generated-media/`
- `platform-runners/deepagents-local-runner/real-smoke-output/`

The audit report is written to:

```text
skills/smb-callable-candidate-skills/REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md
```

## Required Report Fields

The report must record, without secrets:

- `candidate_id`
- `provider_route`
- request summary
- usage or cost note
- output sandbox path
- content safety status
- manual review status
- result status: `passed`, `needs_fix`, `blocked`, or `failed`

## Hard Limits

- `max_images_per_candidate=1`
- `total_max_images=3`
- `max_auto_retries=0`
- `sandbox_output_only=true`
- `no_publish=true`
- `no_customer_callable=true`
- `manual_review_required=true`
- `key_visible_to_testbench=false`
- `write_stable_registry=false`
- `write_business_system=false`
- `upload_customer_assets=false`

## Current Status

- Runner entrypoint exists.
- Safety preflight was verified locally: without approval/route/key, the runner returns `blocked` and does not call any provider.
- Current environment does not expose the required route/key variables.
- Next action: platform runner environment must inject the variables above, then testbench can rerun the same approved smoke.
