# QUALITY_SOURCE_SPRINT_08_RESULT

Updated: 2026-06-09

## Scope

- Goal: select 30 high-quality Skill / Agent / tool candidates for SMB six-department scenarios.
- Department coverage: creative design, operations, sales, ecommerce, support, management / HR / finance.
- Selection rule: candidates can enter the candidate registry if they fit the platform base, can use the OpenAI-compatible relay/model gateway where model inference is needed, and can serve six-department SMB workflows.
- This file is source research only. It does not mean L1 passed, L2 passed, draft L3 packaged, stable promoted, or customer-callable.
- No dependencies installed, no real account access, no API/provider calls, no generated images/videos/audio/files, no customer data access, no key read/write/print, no business-system writes.

## Current Registry Baseline

- Stable registry current count: 71 `SKILL.md` / 71 `skill.yaml`.
- Candidate repository current remote count before this Sprint08 source write: 744 files.
- Deduplication baseline: avoid directly repeating stable 71 systems such as Intercom Article Decay, Shopify Return Product Quality, Metabase Executive Digest, DocuSign Missing Signature, Mailchimp Deliverability QC, Help Scout Saved Reply Gap, Front Account Handoff, Amplitude Activation Dropoff, and earlier P0/P1/P2 stable packages.

## Selection Summary

| Category | Count |
| --- | ---: |
| Total selected candidates | 30 |
| Creative design | 5 |
| Operations | 5 |
| Sales | 5 |
| Ecommerce | 5 |
| Support | 5 |
| Management / HR / finance | 5 |
| Open-source repo / tool candidates | 23 |
| SaaS/API adapter candidates | 3 |
| Media provider / generation-route candidates | 4 |
| Default L1 state | 30 needs_license_review |

## Top 30 Candidate Table

| # | candidate_id | department | source / URL | source_type | license_signal | proposed_skill | trial_mode | score | why selected | hard boundary |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | `quality_sprint08_diffusers_product_scene_payload_candidate` | Creative design | Hugging Face Diffusers, https://github.com/huggingface/diffusers | open-source media framework | Apache-2.0, active | product scene / packshot prompt and payload planner | route_config_mock | 88 | recognized image/video generation stack; useful for product scenes and ecommerce visuals | no real model run, no GPU job, no image output, no upload |
| 2 | `quality_sprint08_remotion_campaign_video_template_candidate` | Creative design | Remotion, https://github.com/remotion-dev/remotion | open-source video framework | GitHub API returned NOASSERTION; license needs review | campaign video template spec generator | metadata_mock | 84 | strong programmatic video ecosystem; can generate video specs before real rendering | no render, no screenshot, no media output, no npm install |
| 3 | `quality_sprint08_manim_training_explainer_candidate` | Creative design | Manim Community, https://github.com/ManimCommunity/manim | open-source animation framework | MIT, active | training explainer storyboard and scene plan | metadata_mock | 82 | useful for HR training, product explainers, finance education | no render, no Python execution, no video output |
| 4 | `quality_sprint08_replicate_brand_asset_route_candidate` | Creative design | Replicate, https://replicate.com/docs | media provider route | provider terms required | brand asset model route planner | route_check | 80 | recognized multi-model media route; useful when relay supports model switching | no provider call, no upload, no generated image/video |
| 5 | `quality_sprint08_openai_images_packshot_variant_candidate` | Creative design | OpenAI Images docs, https://platform.openai.com/docs/guides/images | media provider route | OpenAI terms required | packshot variation payload planner | dry_run_payload_only | 83 | directly fits current OpenAI-compatible relay path for image generation planning | no image endpoint call, no cost, no asset upload |
| 6 | `quality_sprint08_dagster_ops_metric_pipeline_candidate` | Operations | Dagster, https://github.com/dagster-io/dagster | open-source data orchestration | Apache-2.0, active | operations metric pipeline brief | metadata_mock | 83 | strong data-asset orchestration; useful for operations reporting workflows | no pipeline execution, no DB connection, no scheduler write |
| 7 | `quality_sprint08_prefect_daily_ops_flow_monitor_candidate` | Operations | Prefect, https://github.com/PrefectHQ/prefect | open-source workflow orchestration | Apache-2.0, active | daily operations flow risk monitor | metadata_mock | 82 | useful for recurring task/flow health summaries | no flow run, no cloud login, no automation write |
| 8 | `quality_sprint08_superset_dashboard_digest_candidate` | Operations | Apache Superset, https://github.com/apache/superset | open-source BI dashboard | Apache-2.0, active | dashboard narrative and anomaly digest | read_only_mock | 84 | strong BI platform; complements but does not duplicate Metabase stable Skill | no real dashboard connection, no SQL/query execution |
| 9 | `quality_sprint08_redash_query_anomaly_digest_candidate` | Operations | Redash, https://github.com/getredash/redash | open-source BI/query platform | BSD-2-Clause, active | query result anomaly digest | read_only_mock | 80 | common internal dashboard/query tool for SMB analytics | no DB/API connection, no query execution |
| 10 | `quality_sprint08_baserow_ops_board_health_candidate` | Operations | Baserow, https://github.com/baserow/baserow | open-source no-code database | GitHub API returned NOASSERTION; license needs review | operations board health read-only brief | read_only_mock | 78 | useful Airtable-like operations tracker candidate | no workspace login, no row write, no automation trigger |
| 11 | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | Sales | Cal.com, https://github.com/calcom/cal.com | open-source scheduling | MIT signal via GitHub API, active | sales meeting prep from mock bookings | read_only_mock | 83 | strong scheduling infrastructure for sales assistants | no booking create/update/cancel, no email/calendar send |
| 12 | `quality_sprint08_twenty_crm_lead_source_qc_candidate` | Sales | Twenty CRM, https://github.com/twentyhq/twenty | open-source CRM | GitHub API returned NOASSERTION; license needs review | lead source quality read-only report | read_only_mock | 82 | recognized AI-oriented CRM alternative; complements existing HubSpot/Pipedrive stable adapters | no CRM write, no task create, no email send |
| 13 | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | Sales | PandaDoc API, https://developers.pandadoc.com | SaaS/API adapter | provider terms required | proposal status and follow-up brief | read_only_mock | 80 | useful sales proposal follow-up adapter not yet stable | no document send, no signature request, no status modification |
| 14 | `quality_sprint08_apify_partner_research_brief_candidate` | Sales | Apify/Crawlee lead, https://github.com/apify/crawlee | open-source scraping/browser framework | license needs review; crawling risk | partner research brief from user-provided snippets | mock_text_only | 76 | useful for BD research if real crawling is disabled or separately approved | no real crawling, no browser automation, no proxy/API call |
| 15 | `quality_sprint08_bruno_sales_api_demo_collection_candidate` | Sales | Bruno API client, https://github.com/usebruno/bruno | open-source API client | GitHub API access blocked; license needs review | sales demo API collection brief | metadata_mock | 74 | useful for sales engineers preparing API demos | no API call, no secrets, no collection execution |
| 16 | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | Ecommerce | Medusa, https://github.com/medusajs/medusa | open-source commerce platform | MIT, active | product catalog QC read-only report | read_only_mock | 84 | strong ecommerce backend; complements Shopify/BigCommerce/Woo stable adapters | no store login, no product/order/inventory write |
| 17 | `quality_sprint08_saleor_order_margin_readonly_candidate` | Ecommerce | Saleor, https://github.com/saleor/saleor | open-source commerce API | BSD-3-Clause, active | order and margin risk read-only brief | read_only_mock | 82 | headless commerce API with strong SMB/ecommerce relevance | no checkout/order/product write |
| 18 | `quality_sprint08_vendure_inventory_exception_candidate` | Ecommerce | Vendure, https://github.com/vendurehq/vendure | open-source commerce framework | GitHub API returned NOASSERTION; license needs review | inventory exception and replenishment brief | read_only_mock | 79 | useful TypeScript commerce backend candidate | no stock adjustment, no product update |
| 19 | `quality_sprint08_sylius_promo_margin_readonly_candidate` | Ecommerce | Sylius, https://github.com/Sylius/Sylius | open-source ecommerce platform | MIT, active | promo margin and coupon risk read-only brief | read_only_mock | 79 | mature PHP ecommerce platform; adds non-Shopify coverage | no promotion/order/catalog write |
| 20 | `quality_sprint08_crawlee_competitor_listing_snapshot_candidate` | Ecommerce | Crawlee, https://github.com/apify/crawlee | open-source crawling framework | license needs review | competitor listing snapshot from mock HTML | mock_html_only | 76 | ecommerce competitive listing analysis is high-value | no live scraping, no robots/ToS bypass, no browser run |
| 21 | `quality_sprint08_chatwoot_support_macro_gap_candidate` | Support | Chatwoot, https://github.com/chatwoot/chatwoot | open-source support platform | GitHub API returned NOASSERTION; license needs review | support macro gap read-only report | read_only_mock | 82 | recognized open-source support desk; complements Zendesk/Freshdesk/Intercom stable packages | no inbox write, no reply send, no assignment/tag write |
| 22 | `quality_sprint08_rasa_intent_policy_gap_candidate` | Support | Rasa, https://github.com/RasaHQ/rasa | open-source conversational AI | Apache-2.0 historically; recheck required | intent and policy gap mock analyzer | mock_only | 78 | useful support intent routing and policy coverage checks | no bot deployment, no training run, no live conversation |
| 23 | `quality_sprint08_docling_product_manual_kb_parser_candidate` | Support | Docling, https://github.com/docling-project/docling | open-source document parsing | MIT, active | product manual to KB outline parser | mock_text_only | 82 | strong document-to-GenAI tool; useful for support manuals | no real file read, no OCR/PDF processing, no local artifact |
| 24 | `quality_sprint08_unstructured_support_sop_parser_candidate` | Support | Unstructured, https://github.com/Unstructured-IO/unstructured | open-source document ETL | Apache-2.0, active | support SOP sectioning and FAQ seed brief | mock_text_only | 80 | widely used document ingestion stack; useful for support knowledge ops | no real file read, no PDF/OCR run, no upload |
| 25 | `quality_sprint08_promptfoo_support_reply_regression_candidate` | Support | promptfoo, https://github.com/promptfoo/promptfoo | open-source eval framework | MIT, active | support reply regression eval component | component_mock | 78 | mature agent/prompt evaluation tool; useful as QA component | no production eval, no customer logs, no provider call |
| 26 | `quality_sprint08_airflow_admin_approval_workflow_candidate` | Management / HR / finance | Apache Airflow, https://github.com/apache/airflow | open-source workflow scheduler | Apache-2.0, active | admin approval workflow state brief | metadata_mock | 80 | common workflow engine; useful for admin/finance approval modeling | no DAG run, no scheduler write, no DB connection |
| 27 | `quality_sprint08_openrefine_expense_cleaning_plan_candidate` | Management / HR / finance | OpenRefine, https://github.com/OpenRefine/OpenRefine | open-source data cleaning | license needs review | expense data cleaning rules brief | mock_rows_only | 78 | useful finance/admin data cleanup pattern | no local app launch, no CSV/XLSX read/write |
| 28 | `quality_sprint08_tabula_invoice_table_extract_plan_candidate` | Management / HR / finance | Tabula, https://github.com/tabulapdf/tabula-java | open-source PDF table extraction | license needs review | invoice table extraction plan | metadata_mock | 76 | common invoice/table extraction utility, but file boundary must be strict | no PDF read, no Java run, no output file |
| 29 | `quality_sprint08_invoiceplane_receivable_aging_candidate` | Management / HR / finance | InvoicePlane, https://github.com/InvoicePlane/InvoicePlane | open-source invoicing | GitHub API returned NOASSERTION; license needs review | receivable aging read-only brief | read_only_mock | 76 | SMB-friendly invoicing system candidate | no invoice/payment write, no reminder send |
| 30 | `quality_sprint08_actualbudget_cashflow_warning_candidate` | Management / HR / finance | Actual Budget, https://github.com/actualbudget/actual | open-source finance app | MIT, active | cashflow warning from mock ledger rows | mock_rows_only | 78 | local-first finance tool; useful for simple cashflow patterning | no real ledger read, no bank sync, no transaction write |

## P0 Priority Subset

These 12 should be prioritized for L1 review because their source quality, business value, and testability are strongest:

1. `quality_sprint08_diffusers_product_scene_payload_candidate`
2. `quality_sprint08_dagster_ops_metric_pipeline_candidate`
3. `quality_sprint08_superset_dashboard_digest_candidate`
4. `quality_sprint08_calcom_meeting_prep_readonly_candidate`
5. `quality_sprint08_medusa_catalog_qc_readonly_candidate`
6. `quality_sprint08_saleor_order_margin_readonly_candidate`
7. `quality_sprint08_chatwoot_support_macro_gap_candidate`
8. `quality_sprint08_docling_product_manual_kb_parser_candidate`
9. `quality_sprint08_unstructured_support_sop_parser_candidate`
10. `quality_sprint08_airflow_admin_approval_workflow_candidate`
11. `quality_sprint08_actualbudget_cashflow_warning_candidate`
12. `quality_sprint08_openai_images_packshot_variant_candidate`

## L1 Review Guidance

- Open-source tools with permissive licenses can move to `allow_smoke` if the license and dependency chain are clean.
- `NOASSERTION`, AGPL/GPL/custom license, unclear provider terms, or missing source package evidence should be marked `needs_more_license_info` or blocked.
- SaaS/API adapters must stay `read_only_mock` until a later real Harness is explicitly approved.
- Media/provider candidates must stay `route_check` or `dry_run_payload_only`; no real generation before a separate provider-smoke approval.
- Browser/crawler candidates must use user-provided snippets or mock HTML only; no real crawling in L1/L2.
- Document/PDF/table candidates must use mock text/rows only; no customer files or generated files.

## Recommended Next Step

- Send `queues/LICENSE_REVIEW_QUALITY_SPRINT_08_QUEUE.md` to the license window.
- If L1 passes, testbench should generate `DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_RESULT.md` and a Top10 or Top12 L2 queue.
- Stable registry remains at 71 until explicit platform acceptance and promotion.
