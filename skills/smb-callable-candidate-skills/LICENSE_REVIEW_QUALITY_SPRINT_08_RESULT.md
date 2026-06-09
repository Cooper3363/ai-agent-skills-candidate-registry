# LICENSE_REVIEW_QUALITY_SPRINT_08_RESULT

回传日期：2026-06-09

## 1. 已完成事项

- 已只读复核 `QUALITY_SOURCE_SPRINT_08_RESULT.md` 与 `queues/LICENSE_REVIEW_QUALITY_SPRINT_08_QUEUE.md`。
- 已对队列内 exactly 30 个候选完成轻量 L1 / trial mode 复核。
- 已生成 DeepAgents candidate smoke 队列：`queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_QUEUE.md`。
- 本轮未安装依赖、未运行仓库代码、未调用真实 API/provider、未生成图片/视频/音频/PPT/PDF/HTML/真实文件、未读取 key/.env/客户文件、未访问真实账号、未上传素材、未写业务系统、未修改 stable 仓库。

## 2. 当前问题

- 9 个候选缺许可证、API terms、provider terms、具体商业边界或文件处理边界证据，暂不进入 smoke。
- SaaS/API adapter 即使 L1 放行，也只能使用 mock/read-only 数据，不连接真实账号、不发送、不写系统。
- 媒体/provider 候选即使 L1 放行，也只能做 route/config/payload check，不得真实生成或上传素材。
- browser/crawler 候选只允许 user-provided snippets 或 mock HTML，不做真实抓取、browser automation、代理或 API 调用。
- eval/component 类候选默认 component_only；本轮 promptfoo 不进入普通 candidate smoke。

## 3. 阻塞原因

- 无权限阻塞。
- 无 `blocked_by_license` 项。
- 暂缓项的阻塞不是工具权限，而是产品筛选证据不足：LICENSE/SPDX、provider/API ToS、商业输出权、具体文件读写边界或真实上游可核验性不足。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 20 个 `allow_smoke` 项进入 DeepAgents candidate smoke，仅限各自 trial mode。
- 是否要求研究窗口补齐 9 个 `needs_more_license_info` 项的 LICENSE/SPDX、API/provider terms、商业输出权、文件处理/OAuth/read-only 边界。
- 是否为 `promptfoo_support_reply_regression` 开 component/eval 专线，而不是普通 candidate smoke。

## 5. 建议下一步

- 测试台只读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_QUEUE.md` 中 20 个放行项执行 candidate smoke。
- 媒体/provider 项只做 route/config/payload check；真实 provider smoke 另走审批。
- SaaS/API 项只做 mock/read-only/dry-run；不得连接真实账号或写系统。
- 暂缓项补资料后再开补充 L1；不得送正式 L2、不得封装、不得客户调用。
- stable 仓库正式 Skill 基线仍为 71；本轮不修改 stable。

## 6. 数量汇总

| L1 结论 | 数量 |
| --- | ---: |
| `allow_smoke` | 20 |
| `needs_more_license_info` | 9 |
| `blocked_by_license` | 0 |
| `component_only` | 1 |
| `market_lead_or_retire` | 0 |
| 合计 | 30 |

| trial_mode | 数量 |
| --- | ---: |
| `metadata_mock` | 5 |
| `read_only_mock` | 7 |
| `mock_text_only` | 4 |
| `mock_html_only` | 1 |
| `mock_rows_only` | 1 |
| `route_config_mock` | 1 |
| `route_check` | 1 |
| `dry_run_payload_only` | 1 |
| `component_mock` | 1 |
| 暂缓但保留原建议模式 | 9 |

## 7. 暂缓 / blocked / component 清单

| candidate_id | L1 结论 | 缺口 / 原因 |
| --- | --- | --- |
| `quality_sprint08_remotion_campaign_video_template_candidate` | `needs_more_license_info` | GitHub API 返回 NOASSERTION；需补 repo LICENSE/SPDX、renderer/output terms、npm 依赖和商业视频输出边界。 |
| `quality_sprint08_baserow_ops_board_health_candidate` | `needs_more_license_info` | GitHub API 返回 NOASSERTION；需补 license/commercial terms、API terms、workspace/read-only 边界。 |
| `quality_sprint08_twenty_crm_lead_source_qc_candidate` | `needs_more_license_info` | GitHub API 返回 NOASSERTION；需补 CRM license、客户/联系人数据隐私、OAuth/read-only scope。 |
| `quality_sprint08_bruno_sales_api_demo_collection_candidate` | `needs_more_license_info` | GitHub API blocked；需补 license、secret storage、collection import/export 与 API 调用边界。 |
| `quality_sprint08_vendure_inventory_exception_candidate` | `needs_more_license_info` | GitHub API 返回 NOASSERTION；需补 license、商业使用边界、库存/商品写入禁用边界。 |
| `quality_sprint08_chatwoot_support_macro_gap_candidate` | `needs_more_license_info` | GitHub API 返回 NOASSERTION；需补 support desk license、会话隐私、reply/tag/assignment 写入禁用边界。 |
| `quality_sprint08_openrefine_expense_cleaning_plan_candidate` | `needs_more_license_info` | 队列标记 license needs review；需补 license/SPDX、本地文件处理、CSV/XLSX 读写和 app launch 边界。 |
| `quality_sprint08_tabula_invoice_table_extract_plan_candidate` | `needs_more_license_info` | 需补 license、Java 依赖、PDF 隐私、表格输出 artifact 边界。 |
| `quality_sprint08_invoiceplane_receivable_aging_candidate` | `needs_more_license_info` | GitHub API 返回 NOASSERTION；需补 license、invoice/payment terms、催收提醒/账务写入禁用边界。 |
| `quality_sprint08_promptfoo_support_reply_regression_candidate` | `component_only` | eval framework component；可做 mock eval config，不作为六部门 callable business Skill 直接进入普通 smoke。 |

## 8. 媒体 / Provider 边界

| candidate_id | trial_mode | smoke 允许范围 |
| --- | --- | --- |
| `quality_sprint08_diffusers_product_scene_payload_candidate` | `route_config_mock` | product metadata -> image/video route config and prompt payload plan；不运行模型、不上传、不出图/视频。 |
| `quality_sprint08_replicate_brand_asset_route_candidate` | `route_check` | brand brief -> provider route payload；不调用 Replicate、不上传素材、不生成媒体。 |
| `quality_sprint08_openai_images_packshot_variant_candidate` | `dry_run_payload_only` | product metadata -> OpenAI Images request payload；不调用 endpoint、不上传真实商品图、不产生成本。 |

统一禁止：真实生成、素材上传、provider 调用、读取或写入 key、下载产物、声明商业输出权已通过。

## 9. SaaS / Read-only 边界

| candidate_id | trial_mode | smoke 允许范围 |
| --- | --- | --- |
| `quality_sprint08_calcom_meeting_prep_readonly_candidate` | `read_only_mock` | mock bookings -> meeting prep brief。 |
| `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | `read_only_mock` | mock proposal status -> follow-up brief。 |
| `quality_sprint08_superset_dashboard_digest_candidate` | `read_only_mock` | mock dashboard cards -> narrative/anomaly digest。 |
| `quality_sprint08_redash_query_anomaly_digest_candidate` | `read_only_mock` | mock query rows -> anomaly digest。 |
| `quality_sprint08_medusa_catalog_qc_readonly_candidate` | `read_only_mock` | mock products -> catalog QC。 |
| `quality_sprint08_saleor_order_margin_readonly_candidate` | `read_only_mock` | mock orders/promos -> margin risk brief。 |
| `quality_sprint08_sylius_promo_margin_readonly_candidate` | `read_only_mock` | mock promos/orders -> margin QC。 |

统一禁止：连接真实账号、OAuth 真实租户、发送、分配、改状态、写 CRM/电商/财务/协作系统、读真实订单或客户数据。

## 10. L1 复核表

| # | priority | candidate_id | department | L1 结论 | trial_mode | smoke | 许可证/商用条款关注点 | 上游证据是否足够 | 外部依赖/API/provider | 禁止动作 | smoke 允许范围 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint08_diffusers_product_scene_payload_candidate` | Creative design | `allow_smoke` | `route_config_mock` | yes | Apache-2.0 signal；需后续核具体模型权重/训练数据/输出权 | repo/source sufficient for route mock | local/GPU/model/provider optional | 不运行模型、不上传、不生成媒体 | product metadata -> prompt/payload plan |
| 2 | P1 | `quality_sprint08_remotion_campaign_video_template_candidate` | Creative design | `needs_more_license_info` | `metadata_mock` | no | GitHub API NOASSERTION；需补 repo license 和输出商业边界 | 不足 | npm/renderer/screenshot/video output | 不安装 npm、不渲染、不截图 | 暂缓 |
| 3 | P1 | `quality_sprint08_manim_training_explainer_candidate` | Creative design | `allow_smoke` | `metadata_mock` | yes | MIT signal；需保持输出仅为 scene plan | sufficient | Python/render/video dependencies | 不运行 Python、不生成视频 | training topic -> scene plan |
| 4 | P1 | `quality_sprint08_replicate_brand_asset_route_candidate` | Creative design | `allow_smoke` | `route_check` | yes | provider terms/model license/BYOK/cost/content safety 后续核 | docs/source sufficient for route check | Replicate/provider/model routes | 不调用 provider、不上传、不生成媒体 | brand brief -> route payload |
| 5 | P0 | `quality_sprint08_openai_images_packshot_variant_candidate` | Creative design | `allow_smoke` | `dry_run_payload_only` | yes | OpenAI Images terms、产品/品牌素材权、成本上限后续核 | docs/source sufficient for payload mock | OpenAI Images provider | 不调用 endpoint、不上传、不出图 | product metadata -> image request payload |
| 6 | P0 | `quality_sprint08_dagster_ops_metric_pipeline_candidate` | Operations | `allow_smoke` | `metadata_mock` | yes | Apache-2.0 signal；cloud/service terms 另核 | sufficient | scheduler/DB/cloud optional | 不运行 pipeline、不连 DB | ops metrics -> pipeline brief |
| 7 | P1 | `quality_sprint08_prefect_daily_ops_flow_monitor_candidate` | Operations | `allow_smoke` | `metadata_mock` | yes | Apache-2.0 signal；Prefect Cloud/API terms 后续核 | sufficient | cloud login/flow run optional | 不登录 cloud、不运行 flow | mock flow statuses -> risk brief |
| 8 | P0 | `quality_sprint08_superset_dashboard_digest_candidate` | Operations | `allow_smoke` | `read_only_mock` | yes | Apache-2.0 signal；dashboard data privacy | sufficient | BI API/SQL/DB | 不连 DB、不执行 SQL | mock dashboard cards -> digest |
| 9 | P1 | `quality_sprint08_redash_query_anomaly_digest_candidate` | Operations | `allow_smoke` | `read_only_mock` | yes | BSD-2-Clause signal；query data privacy | sufficient | BI API/query DB | 不执行 query、不写 dashboard | mock query rows -> anomaly digest |
| 10 | P1 | `quality_sprint08_baserow_ops_board_health_candidate` | Operations | `needs_more_license_info` | `read_only_mock` | no | NOASSERTION；需补 license/commercial/API terms | 不足 | Baserow API/workspace | 不登录、不写 row | 暂缓 |
| 11 | P0 | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | Sales | `allow_smoke` | `read_only_mock` | yes | MIT signal；Cal.com API/OAuth/read-only scope 后续核 | sufficient | scheduling API/OAuth | 不创建/取消/更新 booking，不发送 | mock bookings -> meeting prep |
| 12 | P1 | `quality_sprint08_twenty_crm_lead_source_qc_candidate` | Sales | `needs_more_license_info` | `read_only_mock` | no | NOASSERTION；需补 CRM license/privacy/read-only terms | 不足 | CRM API/OAuth | 不写 CRM、不建任务、不发邮件 | 暂缓 |
| 13 | P1 | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | Sales | `allow_smoke` | `read_only_mock` | yes | SaaS terms/document privacy/signature restrictions 后续核 | API docs enough for mock | PandaDoc API/BYOK future | 不发送、不签署、不改文档 | mock status -> follow-up brief |
| 14 | P1 | `quality_sprint08_apify_partner_research_brief_candidate` | Sales | `allow_smoke` | `mock_text_only` | yes | Crawlee permissive signal；真实目标站 ToS/抓取合规另核 | enough for snippet-only mock | crawler/browser/proxy optional | 不抓取、不跑 browser、不用代理/API | user snippets -> partner brief |
| 15 | P2 | `quality_sprint08_bruno_sales_api_demo_collection_candidate` | Sales | `needs_more_license_info` | `metadata_mock` | no | GitHub API blocked；需补 license/secret handling | 不足 | API client/collections/secrets | 不读写 secret、不调用 API | 暂缓 |
| 16 | P0 | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | Ecommerce | `allow_smoke` | `read_only_mock` | yes | MIT signal；commerce data privacy | sufficient | commerce API/store | 不写商品/订单/库存 | mock products -> catalog QC |
| 17 | P0 | `quality_sprint08_saleor_order_margin_readonly_candidate` | Ecommerce | `allow_smoke` | `read_only_mock` | yes | BSD-3-Clause signal；order/margin privacy | sufficient | commerce API | 不写 checkout/order/product | mock orders/promos -> margin brief |
| 18 | P1 | `quality_sprint08_vendure_inventory_exception_candidate` | Ecommerce | `needs_more_license_info` | `read_only_mock` | no | NOASSERTION；需补 license/inventory write boundary | 不足 | commerce API | 不改库存、不改商品 | 暂缓 |
| 19 | P1 | `quality_sprint08_sylius_promo_margin_readonly_candidate` | Ecommerce | `allow_smoke` | `read_only_mock` | yes | MIT signal；commerce API boundary | sufficient | commerce API | 不写 promotion/order/catalog | mock promos/orders -> margin QC |
| 20 | P1 | `quality_sprint08_crawlee_competitor_listing_snapshot_candidate` | Ecommerce | `allow_smoke` | `mock_html_only` | yes | Crawlee permissive signal；真实抓取/目标站 ToS 另核 | enough for mock HTML | crawler/browser/proxy optional | 不真实抓取、不跑 browser/proxy | mock HTML -> listing snapshot |
| 21 | P0 | `quality_sprint08_chatwoot_support_macro_gap_candidate` | Support | `needs_more_license_info` | `read_only_mock` | no | NOASSERTION；需补 support desk license/privacy | 不足 | support inbox API | 不回复、不分配、不写 tag | 暂缓 |
| 22 | P1 | `quality_sprint08_rasa_intent_policy_gap_candidate` | Support | `allow_smoke` | `mock_only` | yes | Apache-2.0 historical signal；需后续复核当前 commercial/model terms | sufficient for mock | model/training/live chat optional | 不训练、不部署、不接 live chat | mock intents/policies -> gap report |
| 23 | P0 | `quality_sprint08_docling_product_manual_kb_parser_candidate` | Support | `allow_smoke` | `mock_text_only` | yes | MIT signal；document privacy and OCR/file boundary | sufficient | parser/OCR/PDF optional | 不读文件、不跑 OCR/PDF、不产 artifact | mock manual text -> KB outline |
| 24 | P0 | `quality_sprint08_unstructured_support_sop_parser_candidate` | Support | `allow_smoke` | `mock_text_only` | yes | Apache-2.0 signal；enterprise/cloud terms and file boundary 后续核 | sufficient | document ETL/OCR/upload optional | 不读文件、不 OCR、不上传 | mock SOP text -> FAQ seed |
| 25 | P1 | `quality_sprint08_promptfoo_support_reply_regression_candidate` | Support | `component_only` | `component_mock` | no | MIT signal；eval data/provider-call privacy | sufficient as component | eval/provider optional | 不跑生产 eval、不读客户日志、不调 provider | component mock only |
| 26 | P1 | `quality_sprint08_airflow_admin_approval_workflow_candidate` | Management / HR / finance | `allow_smoke` | `metadata_mock` | yes | Apache-2.0 signal；scheduler/DAG execution boundary | sufficient | scheduler/DB/DAG | 不运行 DAG、不写 scheduler、不连 DB | approval process -> state-machine brief |
| 27 | P1 | `quality_sprint08_openrefine_expense_cleaning_plan_candidate` | Management / HR / finance | `needs_more_license_info` | `mock_rows_only` | no | license needs review；需补 local file/app launch/output terms | 不足 | local app/CSV/XLSX | 不启动 app、不读写文件 | 暂缓 |
| 28 | P2 | `quality_sprint08_tabula_invoice_table_extract_plan_candidate` | Management / HR / finance | `needs_more_license_info` | `metadata_mock` | no | license/Java/PDF privacy/output boundary 不足 | 不足 | Java/PDF extraction | 不读 PDF、不运行 Java、不写输出 | 暂缓 |
| 29 | P2 | `quality_sprint08_invoiceplane_receivable_aging_candidate` | Management / HR / finance | `needs_more_license_info` | `read_only_mock` | no | NOASSERTION；需补 invoice/payment terms | 不足 | invoicing app/API | 不写发票/付款、不发催收 | 暂缓 |
| 30 | P0 | `quality_sprint08_actualbudget_cashflow_warning_candidate` | Management / HR / finance | `allow_smoke` | `mock_rows_only` | yes | MIT signal；local-first finance privacy | sufficient | ledger/bank sync optional | 不读真实账本、不同步银行、不写交易 | mock ledger rows -> cashflow warning |

