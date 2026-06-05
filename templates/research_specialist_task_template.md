# AI.Skills Research Specialist Task Template

Use this template when the command window assigns discovery and validation work to the
AI.Skills research specialist. The goal is to find, verify, test, and package
commercially usable open-source Agent/Skills so the platform team can call them.

## 1. Task Brief

**Task owner:** AI.Skills research specialist

**Command window:** Boss / direction-setting window

**Research goal:**

- Find open-source Agent/Skills candidates that can become callable business Skills.
- Verify commercial usability, repository health, and business fit.
- Run practical tests where needed and produce clear platform-call recommendations.

**Platform boundary:**

- This work supplies Skills to the platform.
- Do not design or implement the platform runtime, UI, billing, model key management,
  or Harness internals.
- Treat Harness as the Agent framework adapter layer for OpenClow, Hermes, MCP, and
  generic Agent runtimes.

## 2. Business Scenarios

Cover all three scenario groups. Prioritize customer support / sales / marketing first,
then finance / admin / contracts, while collecting ecommerce / local operations
candidates in parallel.

| Scenario group | Priority | What to look for | Extra caution |
| --- | --- | --- | --- |
| Customer support / sales / marketing | P0 | FAQ with citations, lead research, follow-up copy, campaign copy, sales summaries, customer feedback clustering | Hallucination control, brand consistency, CRM/email permissions |
| Finance / admin / contracts | P1 | Invoice and receipt extraction, expense checks, meeting minutes, contract review, quote comparison, HR/admin checklists | Accuracy, compliance, human review boundary, document privacy |
| Ecommerce / local operations | P1 | Product listing optimization, competitor snapshots, order exception handling, inventory alerts, funnel reports, browser automation | Account permissions, anti-bot risk, audit logs, failed automation handling |

## 3. Candidate Sources

Search and record candidates from these source types:

- GitHub repositories with clear open-source licenses.
- Official project documentation, release notes, and package metadata.
- Existing catalog entries in this repository.
- Open-source Agent, tool, MCP, prompt, parser, OCR, RAG, workflow, and automation
  projects that can be wrapped into lightweight callable Skills.

Do not treat a full product, large WebUI, or heavy framework as a direct Skill unless it
can be reduced to a specific stable callable task.

## 4. Entry Criteria

Only recommend a candidate for L1 when all of these are true:

- License is MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, or another approved
  permissive license.
- Repository is not archived and has reasonable maintenance activity.
- The candidate maps to a clear business task for small and micro businesses.
- The candidate can be expressed as a lightweight Skill with stable inputs, stable
  outputs, permission needs, and source references.
- Commercial-risk notes are recorded, including dependencies, model weights, datasets,
  cloud services, and third-party APIs when relevant.

## 5. Exclusion And Deferral Rules

Default to deferral or rejection when any of these apply:

- License is GPL, AGPL, SSPL, BUSL, custom commercial-restricted, unclear, or GitHub
  reports `NOASSERTION`.
- Repository is archived, abandoned, or missing a clear `LICENSE` file.
- README claims open source but the license file or dependency terms are unclear.
- The project is primarily a full product, large WebUI, or heavy base framework rather
  than a callable task.
- The project depends on restricted model weights, datasets, brand assets, or cloud
  terms that may limit commercial redistribution or hosted service use.
- The candidate cannot produce a predictable business output after reasonable testing.

## 6. Validation Steps

For each candidate:

1. Open the official repository and confirm it is the primary source.
2. Record repository URL, license, archive status, last meaningful maintenance signal,
   and validation date.
3. Check `LICENSE`, README, package metadata, and obvious dependency risks.
4. Identify the business scenario, callable Skill idea, target users, inputs, outputs,
   permissions, and adapter target.
5. Decide whether the candidate is a direct Skill, a supporting dependency, or a deferred
   research lead.
6. If moving toward L2, install or run the candidate in a controlled test environment.
7. Run at least three Chinese business test cases and keep inputs, outputs, failure
   points, screenshots, logs, or notes.
8. Score the candidate and recommend one action: reject, defer, enter L1, run L2 test,
   or package as L3.

## 7. Scoring

Use the existing 100-point scorecard:

| Dimension | Points |
| --- | ---: |
| Commercial license | 20 |
| Business fit | 20 |
| Deployment difficulty | 15 |
| Output quality | 15 |
| Runtime stability | 10 |
| Chinese-language fit | 10 |
| Maintenance activity | 10 |

Rules:

- License failure overrides the score and blocks first-batch recommendation.
- Candidates under 70 points do not enter first-batch recommendation.
- Output quality must come from actual tests, not repository popularity.
- Record why points were deducted.

## 8. L1 / L2 / L3 Decision Rules

| Status | Meaning | Minimum evidence |
| --- | --- | --- |
| L1 license_metadata_verified | License, repository status, maintenance, and business fit pass | Source links, license evidence, scenario mapping, risk notes |
| L2 runtime_tested | Candidate was installed or run and passed practical tests | At least 3 Chinese business cases, outputs, logs/screenshots/notes, failure notes |
| L3 packaged_skill | Candidate is wrapped as a platform-neutral callable Skill package | `SKILL.md`, `skill.yaml`, prompts/tools/tests, adapter target, test records |

## 9. Required Output Format

Start with a short conclusion:

- Recommended next action.
- Best candidates and why.
- Main risks and blockers.

Then provide this table:

| Project | Repo | License | Commercial usable | Maintenance | Scenario | Callable Skill | Inputs / Outputs | Permissions | Risks | Score | Suggested action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| Example | https://github.com/example/example | MIT | Yes | Active | Customer support | FAQ answer with citations | Input: question + docs; Output: answer + citations | Read docs, call LLM | Needs RAG quality test | 82 | Enter L1 |

End with:

- Rejected or deferred candidates and reasons.
- L2 test plan for the next batch.
- L3 packaging notes for candidates ready for platform call.
- Open questions for the command window.

## 10. Platform-Call Packaging Notes

For candidates recommended for L3, prepare enough information for the platform team to
call the Skill without guessing:

- Stable Skill ID.
- One-sentence intent.
- JSON-like input fields.
- JSON-like output fields.
- Required permissions.
- Source references and license.
- Adapter targets: `openclow`, `openclaw`, `hermes`, `mcp`, or `generic_agent`.
- Test cases and expected output shape.
- Known failure modes and human-review triggers.

## 11. Copyable Assignment Prompt

```text
You are the AI.Skills research specialist.

Task:
Find, verify, and test open-source Agent/Skills candidates that can become commercially
usable callable Skills for a small-business intelligent application service platform.

Platform context:
The platform team is building the runtime separately. Your responsibility is discovery,
license and metadata validation, practical testing, scoring, and platform-call readiness.
Do not design the platform itself.

Scenario focus:
[Fill in: customer support / sales / marketing, finance / admin / contracts, ecommerce /
local operations, or all three]

Requirements:
- Prefer MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause licenses.
- Defer GPL, AGPL, SSPL, BUSL, unclear licenses, GitHub NOASSERTION, archived projects,
  full products, large WebUIs, and heavy frameworks that are not direct callable tasks.
- For each candidate, record repository URL, license evidence, maintenance status,
  business scenario, callable Skill idea, inputs, outputs, permissions, risks, score, and
  suggested action.
- If testing toward L2, run at least 3 Chinese business test cases and keep notes.
- Recommend exactly one action per candidate: reject, defer, enter L1, run L2 test, or
  package as L3.

Output:
Start with a short conclusion, then provide the required candidate table, then list
deferred/rejected items, L2 test plan, L3 packaging notes, and open questions.
```
