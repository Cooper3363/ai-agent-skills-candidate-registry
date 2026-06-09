# L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_08_QUEUE

Generated: 2026-06-09

Source:
- `../DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_RESULT.md`
- `DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_QUEUE.md`

## Scope

- Queue exactly 10 candidates for formal L2 simulated.
- Each candidate should receive at least 3 Chinese SMB mock/read-only use cases, for at least 30 total use cases.
- This is simulated L2 only. It must not connect real accounts, APIs, providers, databases, files, crawlers, browsers, schedulers, or business systems.
- Stable formal Skill baseline remains 71.

## Queue

| rank | candidate_id | recommended_l2_mode | why selected | hard boundary |
| ---: | --- | --- | --- | --- |
| 1 | `quality_sprint08_superset_dashboard_digest_candidate` | read_only_mock_l2 | Operations/management dashboard digest, clear structured input/output | no Superset login, no SQL, no DB/API connection |
| 2 | `quality_sprint08_redash_query_anomaly_digest_candidate` | read_only_mock_l2 | Operations query anomaly digest, useful dashboard/query coverage | no query execution, no DB/API connection, no dashboard write |
| 3 | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | read_only_mock_l2 | Sales meeting prep adapter, clear read-only boundary | no booking create/update/cancel, no email/calendar send |
| 4 | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | read_only_mock_l2 | Sales proposal follow-up, high business fit, low mock risk | no document send, no signature request, no document/status write |
| 5 | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | read_only_mock_l2 | Ecommerce catalog QC, good complement to existing commerce coverage | no store login, no product/order/inventory write |
| 6 | `quality_sprint08_saleor_order_margin_readonly_candidate` | read_only_mock_l2 | Ecommerce margin-risk brief, structured order/promo input | no checkout/order/product write |
| 7 | `quality_sprint08_sylius_promo_margin_readonly_candidate` | read_only_mock_l2 | Ecommerce promo margin QC, useful non-Shopify commerce coverage | no promotion/order/catalog write |
| 8 | `quality_sprint08_rasa_intent_policy_gap_candidate` | mock_l2 | Support intent/policy gap checker, useful for service routing | no training, no deployment, no live chat |
| 9 | `quality_sprint08_unstructured_support_sop_parser_candidate` | mock_text_l2 | Support SOP parsing and FAQ seed generation, clear mock-text boundary | no real file read, no OCR/upload, no artifact output |
| 10 | `quality_sprint08_actualbudget_cashflow_warning_candidate` | mock_rows_l2 | Finance cashflow warning from mock ledger rows, strong SMB value | no real ledger read, no bank sync, no transaction write |

## Explicitly Not In This L2 Queue

Media/provider route-check items are not in ordinary L2 packaging flow and require separate real provider smoke approval before any real output claim:

- `quality_sprint08_diffusers_product_scene_payload_candidate`
- `quality_sprint08_replicate_brand_asset_route_candidate`
- `quality_sprint08_openai_images_packshot_variant_candidate`

Excluded by L1 and not eligible for this L2 queue:

- 9 `needs_more_license_info` candidates.
- 1 `component_only` candidate.

## L2 Checks Required

- Fixed input schema and output schema.
- Chinese usability across at least 3 SMB use cases per candidate.
- DeepAgents / generic Agent Skill callable expression.
- OpenAI-compatible relay/model gateway compatibility where model inference is needed.
- Permission boundary and forbidden action enforcement.
- Human review triggers.
- Failure criteria.
- Duplicate relationship with stable 71 and existing candidates.
- Whether the candidate should remain component-only.
