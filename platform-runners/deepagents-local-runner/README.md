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

## Safety Boundary

The runner exposes no business action tools. It does not send email or SMS, write CRM/calendar/tasks, crawl pages, upload products, issue refunds, modify inventory, call SEO APIs, or generate images.

DeepAgents receives Skill files through an ephemeral state backend and is configured with filesystem write-deny permissions. Only mock prompts and local Skill metadata are used.
