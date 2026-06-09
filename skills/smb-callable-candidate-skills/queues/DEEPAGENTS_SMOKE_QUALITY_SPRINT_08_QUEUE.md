# DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_QUEUE

生成日期：2026-06-09

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_08_RESULT.md`

本队列只包含 L1 放行项：`allow_smoke`。

硬边界：

- 不安装依赖。
- 不运行仓库代码。
- 不调用真实 API/provider。
- 不生成图片、视频、音频、PPT、PDF、HTML 或真实文件。
- 不读取、打印或写入 key、token、`.env`、凭据或客户文件。
- 不访问真实账号，不上传素材。
- 不发送邮件/短信/微信/Slack/Teams/平台消息。
- 不写 CRM/POS/财务/HR/协作/广告/电商/业务系统。
- 不抓取真实网页，不运行 browser automation，不使用代理/API 抓取。
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。
- 本轮不送正式 L2，不封装，不客户调用，不修改 stable；stable 正式 Skill 基线仍为 71。

## Summary

| 类型 | 数量 |
| --- | ---: |
| metadata/mock open-source tools | 5 |
| SaaS/API/read-only mock | 7 |
| media/provider route or payload check | 3 |
| browser/crawler mock snippets/HTML | 2 |
| document/text mock | 2 |
| finance mock rows | 1 |
| smoke queue total | 20 |

## Queue

| # | priority | department | candidate_id | smoke_type | trial_mode | boundary | smoke_focus |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | Creative design | `quality_sprint08_diffusers_product_scene_payload_candidate` | route-config mock | `route_config_mock` | no model run, no upload, no generated media | product metadata -> image/video prompt and payload plan |
| 2 | P1 | Creative design | `quality_sprint08_manim_training_explainer_candidate` | metadata mock | `metadata_mock` | no Python execution, no render | training topic -> scene plan |
| 3 | P1 | Creative design | `quality_sprint08_replicate_brand_asset_route_candidate` | route-check | `route_check` | Replicate disabled, no upload, no media output | brand brief -> provider route payload |
| 4 | P0 | Creative design | `quality_sprint08_openai_images_packshot_variant_candidate` | dry-run payload | `dry_run_payload_only` | OpenAI Images endpoint disabled, no upload | product metadata -> image request payload |
| 5 | P0 | Operations | `quality_sprint08_dagster_ops_metric_pipeline_candidate` | metadata mock | `metadata_mock` | no scheduler, no DB connection | ops metrics -> pipeline brief |
| 6 | P1 | Operations | `quality_sprint08_prefect_daily_ops_flow_monitor_candidate` | metadata mock | `metadata_mock` | no cloud login, no flow run | mock flow statuses -> risk brief |
| 7 | P0 | Operations | `quality_sprint08_superset_dashboard_digest_candidate` | read-only mock | `read_only_mock` | no Superset/DB connection, no SQL | mock dashboard cards -> digest |
| 8 | P1 | Operations | `quality_sprint08_redash_query_anomaly_digest_candidate` | read-only mock | `read_only_mock` | no query execution, no DB/API connection | mock query rows -> anomaly digest |
| 9 | P0 | Sales | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | read-only mock | `read_only_mock` | no real Cal.com account, no booking changes | mock bookings -> meeting prep brief |
| 10 | P1 | Sales | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | read-only mock | `read_only_mock` | no PandaDoc account, no send/sign/write | mock proposal status -> follow-up brief |
| 11 | P1 | Sales | `quality_sprint08_apify_partner_research_brief_candidate` | text mock | `mock_text_only` | no real crawling, no browser, no proxy/API | user-provided snippets -> partner brief |
| 12 | P0 | Ecommerce | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | read-only mock | `read_only_mock` | no store login, no product/order/inventory write | mock products -> catalog QC |
| 13 | P0 | Ecommerce | `quality_sprint08_saleor_order_margin_readonly_candidate` | read-only mock | `read_only_mock` | no checkout/order/product write | mock orders/promos -> margin risk brief |
| 14 | P1 | Ecommerce | `quality_sprint08_sylius_promo_margin_readonly_candidate` | read-only mock | `read_only_mock` | no promotion/order/catalog write | mock promos/orders -> margin QC |
| 15 | P1 | Ecommerce | `quality_sprint08_crawlee_competitor_listing_snapshot_candidate` | HTML mock | `mock_html_only` | no live scraping, no browser, no proxy | mock HTML -> competitor listing snapshot |
| 16 | P1 | Support | `quality_sprint08_rasa_intent_policy_gap_candidate` | mock | `mock_only` | no training, no deployment, no live chat | mock intents/policies -> gap report |
| 17 | P0 | Support | `quality_sprint08_docling_product_manual_kb_parser_candidate` | text mock | `mock_text_only` | no real file read, no OCR/PDF, no artifact | mock manual text -> KB outline |
| 18 | P0 | Support | `quality_sprint08_unstructured_support_sop_parser_candidate` | text mock | `mock_text_only` | no real file read, no OCR/upload | mock SOP text -> FAQ seed |
| 19 | P1 | Management / HR / finance | `quality_sprint08_airflow_admin_approval_workflow_candidate` | metadata mock | `metadata_mock` | no DAG run, no scheduler/DB connection | approval process -> DAG/state-machine brief |
| 20 | P0 | Management / HR / finance | `quality_sprint08_actualbudget_cashflow_warning_candidate` | rows mock | `mock_rows_only` | no real ledger, no bank sync, no transaction write | mock ledger rows -> cashflow warning |

## Excluded From Smoke

| candidate_id | L1 结论 | reason |
| --- | --- | --- |
| `quality_sprint08_remotion_campaign_video_template_candidate` | `needs_more_license_info` | GitHub API NOASSERTION；需补 repo license、renderer/output terms、npm 依赖边界。 |
| `quality_sprint08_baserow_ops_board_health_candidate` | `needs_more_license_info` | GitHub API NOASSERTION；需补 license/commercial/API terms。 |
| `quality_sprint08_twenty_crm_lead_source_qc_candidate` | `needs_more_license_info` | GitHub API NOASSERTION；需补 CRM license、数据隐私、read-only scope。 |
| `quality_sprint08_bruno_sales_api_demo_collection_candidate` | `needs_more_license_info` | GitHub API blocked；需补 license、secret storage、collection/API 调用边界。 |
| `quality_sprint08_vendure_inventory_exception_candidate` | `needs_more_license_info` | GitHub API NOASSERTION；需补 license 和库存写入禁用边界。 |
| `quality_sprint08_chatwoot_support_macro_gap_candidate` | `needs_more_license_info` | GitHub API NOASSERTION；需补 support desk license、会话隐私和写入边界。 |
| `quality_sprint08_openrefine_expense_cleaning_plan_candidate` | `needs_more_license_info` | license needs review；需补本地文件处理和输出边界。 |
| `quality_sprint08_tabula_invoice_table_extract_plan_candidate` | `needs_more_license_info` | 需补 license、Java 依赖、PDF 隐私和输出 artifact 边界。 |
| `quality_sprint08_invoiceplane_receivable_aging_candidate` | `needs_more_license_info` | GitHub API NOASSERTION；需补 invoice/payment terms 和催收/账务写入边界。 |
| `quality_sprint08_promptfoo_support_reply_regression_candidate` | `component_only` | eval component，不进入普通 candidate smoke。 |

