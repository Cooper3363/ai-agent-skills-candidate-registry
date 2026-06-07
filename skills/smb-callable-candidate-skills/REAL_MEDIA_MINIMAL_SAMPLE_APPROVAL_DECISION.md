# REAL_MEDIA_MINIMAL_SAMPLE_APPROVAL_DECISION

Decision date: 2026-06-05

## Decision

AI.Skills command center approves a minimal real image sample smoke for the 3 OpenAI-compatible image relay candidates that already passed route/config check.

This approval is limited to controlled testbench smoke only. It does not mean provider acceptance, customer callable status, stable delivery status, or draft L3 approval.

## Approved Candidates

| candidate_id | approved_sample | provider_route | output_scope |
| --- | --- | --- | --- |
| `marketing_real_poster_banner_agent_candidate` | 1 mock event poster image | OpenAI-compatible image relay | runner sandbox only |
| `ecommerce_product_main_image_agent_candidate` | 1 mock product hero image | OpenAI-compatible image relay | runner sandbox only |
| `store_menu_poster_generation_candidate` | 1 mock menu poster image | OpenAI-compatible image relay | runner sandbox only |

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

## Required Runtime Controls

- Use only platform-managed or environment-managed key routing.
- Do not write API keys, relay keys, request secrets, or provider credentials to the repository.
- Do not print keys in logs.
- Output files must stay under a sandbox path excluded by git, such as `media-smoke/`, `generated-media/`, or `real-smoke-output/`.
- Use mock prompts and mock business data only.
- Do not use real customer, employee, candidate, brand, trademark, copyrighted, or third-party assets.
- Record candidate_id, provider_route, request summary, cost estimate or usage note, output path, content safety status, and manual review status.

## Fixed Mock Scenarios

| candidate_id | mock scenario | manual review triggers |
| --- | --- | --- |
| `marketing_real_poster_banner_agent_candidate` | Generate a neutral small-business weekend sale poster for a fictional stationery shop. | Brand/trademark, people, pricing claims, copyright, policy-sensitive content |
| `ecommerce_product_main_image_agent_candidate` | Generate a clean hero image for a fictional stainless steel thermos product with mock attributes only. | Product misrepresentation, trademarks, packaging claims, fake certification, unclear specs |
| `store_menu_poster_generation_candidate` | Generate a simple menu poster for a fictional noodle shop using mock menu items and mock prices. | Price/menu uncertainty, food health claims, trademark/font risk, promotion promises |

## Explicit Non-Approval

The following are not approved by this decision:

- Batch generation.
- Real customer asset upload.
- Real brand or trademark use.
- Real product package replication.
- Real human portrait, avatar, or voice use.
- Publishing or sending outputs.
- Writing outputs to the stable delivery repository.
- Treating the generated sample as customer deliverable evidence.

## Next Required Output

The testbench should write:

- `REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT.md`

The result must classify each sample as `passed`, `needs_fix`, `blocked`, or `failed`, and must include output sandbox paths without embedding secrets.
