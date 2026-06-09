# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_08

Generated: 2026-06-09

Source:
- `../L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_08_RESULT.md`
- `L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_08_QUEUE.md`

## Queue Scope

- Package exactly the 10 Sprint08 L2-passed simulated candidates below.
- These are draft L3 candidates only, not stable promotions and not customer-callable.
- Stable formal Skill baseline remains 71.
- All SaaS/API/read-only/mock candidates require real Harness acceptance before production use.

## Draft L3 Queue

| rank | source_candidate_id | draft_skill_id | packaging_mode | required_boundary |
| ---: | --- | --- | --- | --- |
| 1 | `quality_sprint08_superset_dashboard_digest_candidate` | `superset_dashboard_digest_readonly_agent` | draft_l3_readonly_agent | `read_only=true`; no SQL/query execution; no DB/API connection; no dashboard write |
| 2 | `quality_sprint08_redash_query_anomaly_digest_candidate` | `redash_query_anomaly_digest_readonly_agent` | draft_l3_readonly_agent | `read_only=true`; no query execution; no DB/API connection; no dashboard write |
| 3 | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | `calcom_meeting_prep_readonly_agent` | draft_l3_readonly_agent | `read_only=true`; no booking create/update/cancel; no email/calendar send |
| 4 | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | `pandadoc_proposal_status_readonly_agent` | draft_l3_readonly_agent | `read_only=true`; no document send; no signature request; no document/status write |
| 5 | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | `medusa_catalog_qc_readonly_agent` | draft_l3_readonly_agent | `read_only=true`; no product/order/inventory write |
| 6 | `quality_sprint08_saleor_order_margin_readonly_candidate` | `saleor_order_margin_readonly_agent` | draft_l3_readonly_agent | `read_only=true`; no checkout/order/product write |
| 7 | `quality_sprint08_sylius_promo_margin_readonly_candidate` | `sylius_promo_margin_readonly_agent` | draft_l3_readonly_agent | `read_only=true`; no promotion/order/catalog write |
| 8 | `quality_sprint08_rasa_intent_policy_gap_candidate` | `rasa_intent_policy_gap_mock_agent` | draft_l3_mock_agent | no training, deployment, model update, or live chat connection |
| 9 | `quality_sprint08_unstructured_support_sop_parser_candidate` | `unstructured_support_sop_parser_mock_agent` | draft_l3_mock_agent | no real file read; no OCR/upload; no artifact output |
| 10 | `quality_sprint08_actualbudget_cashflow_warning_candidate` | `actualbudget_cashflow_warning_mock_agent` | draft_l3_mock_agent | no real ledger read; no bank sync; no transaction write |

## Packaging Requirements

- Include `SKILL.md` draft and `skill.yaml` draft for each candidate.
- Include fixed input schema and output schema.
- Include at least 3 Chinese SMB test cases per skill.
- Include adapter targets: `generic_agent`; add `mcp` or SaaS adapter target only when platform harness exists.
- Include source project and license evidence from Sprint08 L1.
- Include real Harness smoke required fields for SaaS/API/read-only candidates.
- Include `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true`.
- Include human review triggers and failure criteria.
- State clearly that this is draft L3 and not a stable/customer-callable skill.

## Not In Packaging Queue

- Media/provider route-check items: `quality_sprint08_diffusers_product_scene_payload_candidate`, `quality_sprint08_replicate_brand_asset_route_candidate`, `quality_sprint08_openai_images_packshot_variant_candidate`.
- L1 excluded items: 9 `needs_more_license_info` candidates and 1 `component_only` candidate.
