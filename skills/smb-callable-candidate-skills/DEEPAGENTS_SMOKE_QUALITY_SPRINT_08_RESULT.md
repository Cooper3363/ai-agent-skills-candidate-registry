# DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_RESULT

Generated: 2026-06-09

Source:
- `LICENSE_REVIEW_QUALITY_SPRINT_08_RESULT.md`
- `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_QUEUE.md`

## 1. Completed Work

- Read `LICENSE_REVIEW_QUALITY_SPRINT_08_RESULT.md`.
- Read `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_QUEUE.md`.
- Strictly processed only the 20 L1 `allow_smoke` candidates in the smoke queue.
- Completed candidate-level metadata/mock/read-only/dry-run/route-check smoke for 20 candidates.
- Generated Top10 formal L2 simulated queue:
  - `queues/L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_08_QUEUE.md`

## 2. Smoke Counts

| Status | Count |
| --- | ---: |
| passed | 20 |
| failed | 0 |
| needs_fix | 0 |
| blocked | 0 |

## 3. Top10 L2 Queue

1. `quality_sprint08_superset_dashboard_digest_candidate`
2. `quality_sprint08_redash_query_anomaly_digest_candidate`
3. `quality_sprint08_calcom_meeting_prep_readonly_candidate`
4. `quality_sprint08_pandadoc_proposal_status_readonly_candidate`
5. `quality_sprint08_medusa_catalog_qc_readonly_candidate`
6. `quality_sprint08_saleor_order_margin_readonly_candidate`
7. `quality_sprint08_sylius_promo_margin_readonly_candidate`
8. `quality_sprint08_rasa_intent_policy_gap_candidate`
9. `quality_sprint08_unstructured_support_sop_parser_candidate`
10. `quality_sprint08_actualbudget_cashflow_warning_candidate`

Selection logic: prioritize non-media, low real-action risk, high six-department SMB value, text/structured/read-only outputs, and clear separation from the stable 71 baseline.

## 4. Media / Provider Route-Check Items

These 3 candidates only passed route/config/payload check. They must not be written as real provider success.

| candidate_id | smoke status | boundary |
| --- | --- | --- |
| `quality_sprint08_diffusers_product_scene_payload_candidate` | route/config/payload check passed | `real_provider_smoke_required=true`; no provider/model run, no upload, no generated image/video/audio/file |
| `quality_sprint08_replicate_brand_asset_route_candidate` | route/config/payload check passed | `real_provider_smoke_required=true`; no Replicate call, no upload, no generated media |
| `quality_sprint08_openai_images_packshot_variant_candidate` | route/config/payload check passed | `real_provider_smoke_required=true`; no OpenAI Images endpoint call, no upload, no generated media, no cost |

## 5. Passed Candidate Notes

| candidate_id | trial_mode | smoke summary |
| --- | --- | --- |
| `quality_sprint08_diffusers_product_scene_payload_candidate` | `route_config_mock` | Product metadata can produce image/video prompt and route payload plan without generation. |
| `quality_sprint08_manim_training_explainer_candidate` | `metadata_mock` | Training topic can produce Chinese scene plan and narration outline without rendering. |
| `quality_sprint08_replicate_brand_asset_route_candidate` | `route_check` | Brand brief can produce provider route payload with cost/safety fields. |
| `quality_sprint08_openai_images_packshot_variant_candidate` | `dry_run_payload_only` | Product metadata can produce image request payload with safety/review fields. |
| `quality_sprint08_dagster_ops_metric_pipeline_candidate` | `metadata_mock` | Ops metrics can produce data-asset pipeline brief and failure triggers. |
| `quality_sprint08_prefect_daily_ops_flow_monitor_candidate` | `metadata_mock` | Mock flow statuses can produce daily risk brief and escalation fields. |
| `quality_sprint08_superset_dashboard_digest_candidate` | `read_only_mock` | Mock dashboard cards can produce narrative digest and anomaly list. |
| `quality_sprint08_redash_query_anomaly_digest_candidate` | `read_only_mock` | Mock query rows can produce anomaly digest and owner follow-up list. |
| `quality_sprint08_calcom_meeting_prep_readonly_candidate` | `read_only_mock` | Mock bookings can produce meeting-prep brief without booking changes. |
| `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | `read_only_mock` | Mock proposal status can produce follow-up brief without sending/signing/writing. |
| `quality_sprint08_apify_partner_research_brief_candidate` | `mock_text_only` | User-provided snippets can produce partner research brief without crawling. |
| `quality_sprint08_medusa_catalog_qc_readonly_candidate` | `read_only_mock` | Mock products can produce catalog QC report without product/order/inventory writes. |
| `quality_sprint08_saleor_order_margin_readonly_candidate` | `read_only_mock` | Mock orders/promos can produce margin-risk brief without commerce writes. |
| `quality_sprint08_sylius_promo_margin_readonly_candidate` | `read_only_mock` | Mock promos/orders can produce promo margin QC without catalog/order writes. |
| `quality_sprint08_crawlee_competitor_listing_snapshot_candidate` | `mock_html_only` | Mock HTML can produce competitor listing snapshot without live crawling/browser automation. |
| `quality_sprint08_rasa_intent_policy_gap_candidate` | `mock_only` | Mock intents/policies can produce policy gap report without training/deployment. |
| `quality_sprint08_docling_product_manual_kb_parser_candidate` | `mock_text_only` | Mock manual text can produce KB outline without file/OCR/PDF processing. |
| `quality_sprint08_unstructured_support_sop_parser_candidate` | `mock_text_only` | Mock SOP text can produce FAQ seeds without file read/upload/OCR. |
| `quality_sprint08_airflow_admin_approval_workflow_candidate` | `metadata_mock` | Approval process can produce state-machine/DAG brief without scheduler/DB access. |
| `quality_sprint08_actualbudget_cashflow_warning_candidate` | `mock_rows_only` | Mock ledger rows can produce cashflow warning without real ledger/bank sync. |

## 6. Excluded Items Confirmed Not Processed

- 9 `needs_more_license_info` candidates were not processed.
- 1 `component_only` candidate was not processed.

Excluded candidates:
- `quality_sprint08_remotion_campaign_video_template_candidate`
- `quality_sprint08_baserow_ops_board_health_candidate`
- `quality_sprint08_twenty_crm_lead_source_qc_candidate`
- `quality_sprint08_bruno_sales_api_demo_collection_candidate`
- `quality_sprint08_vendure_inventory_exception_candidate`
- `quality_sprint08_chatwoot_support_macro_gap_candidate`
- `quality_sprint08_openrefine_expense_cleaning_plan_candidate`
- `quality_sprint08_tabula_invoice_table_extract_plan_candidate`
- `quality_sprint08_invoiceplane_receivable_aging_candidate`
- `quality_sprint08_promptfoo_support_reply_regression_candidate`

## 7. Permission Boundary

- No dependency install.
- No repository code execution.
- No external network, real account, OAuth tenant, API, provider, database, scheduler, browser, crawler, proxy, model, GPU, OCR, PDF, Java, Python, or file-processing run.
- No key/token/.env/credential read, write, or print.
- No customer file, business document, real order, real invoice, real ledger, real dashboard, or real support conversation read.
- No upload, message send, business-system write, web crawling, browser automation, media/file generation, artifact write, refund, compensation, payment capture, inventory update, subscription update, ledger write, tax filing, task creation, or file sharing.
- Stable registry was not modified; stable formal Skill baseline remains 71.

Candidate smoke passed only means candidate-level mock/read-only/route-check can continue. It does not mean L2 passed, does not mean draft L3 packaged, and does not mean stable/customer-callable.
