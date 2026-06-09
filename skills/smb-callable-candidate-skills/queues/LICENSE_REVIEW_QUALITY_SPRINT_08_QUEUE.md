# LICENSE_REVIEW_QUALITY_SPRINT_08_QUEUE

Generated: 2026-06-09
Source: `../QUALITY_SOURCE_SPRINT_08_RESULT.md`

## Queue Scope

- Review exactly 30 selected candidates for six-department SMB coverage.
- This is L1 / trial-mode review only.
- Do not run code, install dependencies, call APIs/providers, generate media, read customer files, read `.env`, print/write keys, or modify stable.
- Output requested from license window:
  - `../LICENSE_REVIEW_QUALITY_SPRINT_08_RESULT.md`
  - `DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_QUEUE.md` for L1/trial-mode allow items only.

## Summary

| Department | Count |
| --- | ---: |
| Creative design | 5 |
| Operations | 5 |
| Sales | 5 |
| Ecommerce | 5 |
| Support | 5 |
| Management / HR / finance | 5 |
| Total | 30 |

## Review Queue

| # | priority | candidate_id | department | source_url | source_type | license_review_focus | proposed_trial_mode | smoke_focus_if_allowed | exclusion_condition |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint08_diffusers_product_scene_payload_candidate` | Creative design | https://github.com/huggingface/diffusers | open-source media framework | Confirm Apache-2.0, dependency/model license boundaries, local/GPU/provider execution risks | `route_config_mock` | product metadata -> image/video payload plan only | block real model run, generated media, upload |
| 2 | P1 | `quality_sprint08_remotion_campaign_video_template_candidate` | Creative design | https://github.com/remotion-dev/remotion | open-source video framework | GitHub API returned NOASSERTION; confirm repo license, renderer/output terms, npm dependency boundaries | `metadata_mock` | campaign brief -> video template spec only | block render, screenshot, generated video |
| 3 | P1 | `quality_sprint08_manim_training_explainer_candidate` | Creative design | https://github.com/ManimCommunity/manim | open-source animation framework | Confirm MIT and Python dependency/output file boundaries | `metadata_mock` | training topic -> scene plan only | block Python run and video output |
| 4 | P1 | `quality_sprint08_replicate_brand_asset_route_candidate` | Creative design | https://replicate.com/docs | media provider route | Provider terms, model-specific licenses, BYOK/cost/content safety | `route_check` | brand brief -> route payload only | block provider call and media generation |
| 5 | P0 | `quality_sprint08_openai_images_packshot_variant_candidate` | Creative design | https://platform.openai.com/docs/guides/images | media provider route | OpenAI Images terms, content safety, product/brand asset rights, cost cap | `dry_run_payload_only` | product metadata -> image request payload | block real image endpoint and upload |
| 6 | P0 | `quality_sprint08_dagster_ops_metric_pipeline_candidate` | Operations | https://github.com/dagster-io/dagster | open-source orchestration | Confirm Apache-2.0, cloud/service terms, no pipeline execution | `metadata_mock` | ops metrics -> pipeline brief | block scheduler run, DB connection |
| 7 | P1 | `quality_sprint08_prefect_daily_ops_flow_monitor_candidate` | Operations | https://github.com/PrefectHQ/prefect | open-source orchestration | Confirm Apache-2.0, cloud/API terms, no automation writes | `metadata_mock` | mock flow statuses -> risk brief | block cloud login and flow run |
| 8 | P0 | `quality_sprint08_superset_dashboard_digest_candidate` | Operations | https://github.com/apache/superset | open-source BI | Confirm Apache-2.0, dashboard data privacy, API/read-only boundary | `read_only_mock` | mock dashboard cards -> digest | block SQL/query execution and DB connection |
| 9 | P1 | `quality_sprint08_redash_query_anomaly_digest_candidate` | Operations | https://github.com/getredash/redash | open-source BI | Confirm BSD-2-Clause, query/data privacy, read-only scope | `read_only_mock` | mock query result rows -> anomaly digest | block real query and dashboard write |
| 10 | P1 | `quality_sprint08_baserow_ops_board_health_candidate` | Operations | https://github.com/baserow/baserow | no-code database | GitHub API returned NOASSERTION; confirm license/commercial terms/API terms | `read_only_mock` | mock board rows -> board health report | block row write, automation trigger |
| 11 | P0 | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | Sales | https://github.com/calcom/cal.com | open-source scheduling | Confirm MIT signal and Cal.com API/OAuth/read-only booking scope | `read_only_mock` | mock bookings -> meeting prep brief | block booking create/update/cancel/send |
| 12 | P1 | `quality_sprint08_twenty_crm_lead_source_qc_candidate` | Sales | https://github.com/twentyhq/twenty | open-source CRM | GitHub API returned NOASSERTION; confirm license, CRM data privacy, read-only boundary | `read_only_mock` | mock leads/opps -> source QC | block CRM write/task/email |
| 13 | P1 | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | Sales | https://developers.pandadoc.com | SaaS/API adapter | Provider API terms, document privacy, signature/send restrictions | `read_only_mock` | mock proposal status -> follow-up brief | block send/signature/document write |
| 14 | P1 | `quality_sprint08_apify_partner_research_brief_candidate` | Sales | https://github.com/apify/crawlee | crawler/browser framework | Confirm license and crawling/ToS/proxy risks; only user snippets allowed | `mock_text_only` | user-provided snippets -> partner brief | block real crawl/browser/proxy/API |
| 15 | P2 | `quality_sprint08_bruno_sales_api_demo_collection_candidate` | Sales | https://github.com/usebruno/bruno | API client | GitHub API blocked; confirm license and secret storage risks | `metadata_mock` | API description -> demo collection brief | block API call, secret read/write |
| 16 | P0 | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | Ecommerce | https://github.com/medusajs/medusa | open-source commerce | Confirm MIT, API terms, catalog/order privacy | `read_only_mock` | mock products -> catalog QC | block product/order/inventory write |
| 17 | P0 | `quality_sprint08_saleor_order_margin_readonly_candidate` | Ecommerce | https://github.com/saleor/saleor | open-source commerce | Confirm BSD-3-Clause, API/read-only boundary | `read_only_mock` | mock orders/promos -> margin risk brief | block checkout/order/product write |
| 18 | P1 | `quality_sprint08_vendure_inventory_exception_candidate` | Ecommerce | https://github.com/vendurehq/vendure | open-source commerce | GitHub API returned NOASSERTION; confirm license and inventory write boundary | `read_only_mock` | mock inventory rows -> exception brief | block stock/product update |
| 19 | P1 | `quality_sprint08_sylius_promo_margin_readonly_candidate` | Ecommerce | https://github.com/Sylius/Sylius | open-source commerce | Confirm MIT and commerce API boundary | `read_only_mock` | mock promos/orders -> margin QC | block promotion/order/catalog write |
| 20 | P1 | `quality_sprint08_crawlee_competitor_listing_snapshot_candidate` | Ecommerce | https://github.com/apify/crawlee | crawler/browser framework | Confirm license and crawling/ToS risks; mock HTML only | `mock_html_only` | mock HTML -> competitor listing snapshot | block live scraping/browser/proxy |
| 21 | P0 | `quality_sprint08_chatwoot_support_macro_gap_candidate` | Support | https://github.com/chatwoot/chatwoot | support desk | GitHub API returned NOASSERTION; confirm license/support data privacy | `read_only_mock` | mock conversations/macros -> macro gap | block reply, assignment, tag write |
| 22 | P1 | `quality_sprint08_rasa_intent_policy_gap_candidate` | Support | https://github.com/RasaHQ/rasa | conversational AI | Recheck license/commercial terms and model/training data boundaries | `mock_only` | mock intents/policies -> gap report | block model training/deployment/live chat |
| 23 | P0 | `quality_sprint08_docling_product_manual_kb_parser_candidate` | Support | https://github.com/docling-project/docling | document parsing | Confirm MIT, document privacy, file/OCR boundaries | `mock_text_only` | mock manual text -> KB outline | block PDF/OCR/file read/output |
| 24 | P0 | `quality_sprint08_unstructured_support_sop_parser_candidate` | Support | https://github.com/Unstructured-IO/unstructured | document ETL | Confirm Apache-2.0, enterprise terms, file/OCR boundaries | `mock_text_only` | mock SOP text -> FAQ seed | block PDF/OCR/file read/upload |
| 25 | P1 | `quality_sprint08_promptfoo_support_reply_regression_candidate` | Support | https://github.com/promptfoo/promptfoo | eval component | Confirm MIT, eval data privacy, provider-call boundary | `component_mock` | mock support replies -> regression eval config | component_only unless wrapped as callable Skill |
| 26 | P1 | `quality_sprint08_airflow_admin_approval_workflow_candidate` | Management / HR / finance | https://github.com/apache/airflow | workflow scheduler | Confirm Apache-2.0, DAG execution and scheduler write risks | `metadata_mock` | approval process -> DAG/state-machine brief | block DAG run/scheduler/DB connection |
| 27 | P1 | `quality_sprint08_openrefine_expense_cleaning_plan_candidate` | Management / HR / finance | https://github.com/OpenRefine/OpenRefine | data cleaning | Confirm license and local file processing boundaries | `mock_rows_only` | mock expense rows -> cleaning rules | block CSV/XLSX read/write and app launch |
| 28 | P2 | `quality_sprint08_tabula_invoice_table_extract_plan_candidate` | Management / HR / finance | https://github.com/tabulapdf/tabula-java | PDF table extraction | Confirm license, Java dependency, PDF privacy and output boundaries | `metadata_mock` | invoice table schema -> extraction plan | block PDF read/Java run/output file |
| 29 | P2 | `quality_sprint08_invoiceplane_receivable_aging_candidate` | Management / HR / finance | https://github.com/InvoicePlane/InvoicePlane | invoicing app | GitHub API returned NOASSERTION; confirm license and payment/invoice boundaries | `read_only_mock` | mock invoices -> receivable aging brief | block invoice/payment write/reminder send |
| 30 | P0 | `quality_sprint08_actualbudget_cashflow_warning_candidate` | Management / HR / finance | https://github.com/actualbudget/actual | finance app | Confirm MIT and local-first data/privacy boundary | `mock_rows_only` | mock ledger rows -> cashflow warning | block real ledger/bank sync/transaction write |

## Hard Boundary For All Items

- No dependency install.
- No real account/OAuth/API/provider access.
- No key, token, `.env`, credential, customer file, or real business document read/write/print.
- No message send, file upload, business-system write, refund, compensation, payment capture, inventory update, subscription update, ledger write, tax filing, task creation, file sharing, browser automation, real crawl, or real media generation.
- No stable registry modification during L1.
