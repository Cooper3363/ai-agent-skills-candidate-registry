# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_08

生成日期：2026-06-09

来源：`../L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_08_RESULT.md`

队列性质：Quality Sprint 08 正式 L2 simulated 后的 draft L3 封装准备队列。进入本队列不代表真实 SaaS/API/Harness/provider 通过，不代表自动进入 stable 或客户正式可调用。stable 正式 Skill 基线仍为 71；promotion/platform acceptance 需要另行决策。

## 1. 入队标准

- L2 结论为 `L2 通过可封装`。
- 可表达为 DeepAgents / 通用 Agent Skill callable candidate。
- 当前只允许 mock/read-only 语义。
- SaaS/API/BI/commerce connector 必须保留最小只读 scope 和 read-only 硬断言。
- mock-text/mock-rows candidate 必须保留不读取真实文件、不上传、不生成 artifact、不写业务系统边界。
- 后续封装必须补齐真实 Harness smoke 计划、审计日志、错误回退、权限声明、人工复核触发和 source evidence 字段。

## 2. 封装队列

| 排名 | draft_skill_id | source_candidate_id | 业务包 | trial mode | 封装目标 | 必须保留的权限边界 | 最小平台 smoke 输入 | 后续真实 Harness 要求 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `superset_dashboard_digest_readonly_agent` | `quality_sprint08_superset_dashboard_digest_candidate` | 经营报表摘要包 | `read_only_mock` | Superset dashboard 只读经营摘要和异常卡片说明 | `read_only=true`, 最小 dashboard/card 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox dashboard cards | 禁止 Superset login 直连、SQL/DB/API、query 执行和 dashboard 写入 |
| 2 | `redash_query_anomaly_digest_readonly_agent` | `quality_sprint08_redash_query_anomaly_digest_candidate` | 运营数据异常包 | `read_only_mock` | Redash query rows 异常摘要和 owner follow-up 草稿 | `read_only=true`, 最小 query metadata/rows 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox query rows | 禁止 query 执行、DB/API 连接、dashboard 写入和自动通知 |
| 3 | `calcom_meeting_prep_readonly_agent` | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | 销售/客服会前准备包 | `read_only_mock` | Cal.com booking 只读会前准备 brief | `read_only=true`, 最小 bookings/attendees 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox bookings | 禁止创建/更新/取消 booking，禁止邮件或日历邀请 |
| 4 | `pandadoc_proposal_status_readonly_agent` | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | 销售提案状态包 | `read_only_mock` | PandaDoc proposal 状态只读跟进 brief | `read_only=true`, 最小 proposals/status 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox proposals | 禁止发送文档、请求签名、写文档或状态 |
| 5 | `medusa_catalog_qc_readonly_agent` | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | 电商商品目录 QC 包 | `read_only_mock` | Medusa products/variants 只读 QC 报告 | `read_only=true`, 最小 products/variants 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox products/variants | 禁止商品、订单、库存、促销、checkout、catalog 写入 |
| 6 | `saleor_order_margin_readonly_agent` | `quality_sprint08_saleor_order_margin_readonly_candidate` | 电商订单毛利风险包 | `read_only_mock` | Saleor orders/promos 只读毛利风险 brief | `read_only=true`, 最小 orders/promotions 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox orders/line_items | 禁止 checkout/order/product/promo 写入；保留 `not_financial_advice=true` |
| 7 | `sylius_promo_margin_readonly_agent` | `quality_sprint08_sylius_promo_margin_readonly_candidate` | 电商促销毛利 QC 包 | `read_only_mock` | Sylius promotions/orders 只读促销毛利 QC | `read_only=true`, 最小 promotions/orders 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox promotions/orders | 禁止 promotion/order/catalog 写入；不得自动停用优惠 |
| 8 | `rasa_intent_policy_gap_mock_agent` | `quality_sprint08_rasa_intent_policy_gap_candidate` | 客服意图/政策质检包 | `mock_only` | Rasa intents/policies mock 差距分析 | mock only, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | mock intents + policy snippets | 禁止训练、部署、接入 live chat、发送消息或修改训练集 |
| 9 | `unstructured_support_sop_parser_mock_text_agent` | `quality_sprint08_unstructured_support_sop_parser_candidate` | 客服 SOP 结构化包 | `mock_text_only` | mock SOP text 解析为 outline/FAQ seed/escalation paths | mock text only, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | mock SOP text | 禁止真实文件读取、OCR、upload、PDF/Office 处理和 artifact 输出 |
| 10 | `actualbudget_cashflow_warning_mock_rows_agent` | `quality_sprint08_actualbudget_cashflow_warning_candidate` | 财务现金流预警包 | `mock_rows_only` | synthetic ledger rows 现金流风险提示 | mock rows only, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true`, `not_financial_advice=true` | synthetic ledger rows | 禁止真实账本读取、银行同步、交易写入、扣款、报税或财务建议 |

## 3. 封装窗口统一要求

- 每个 draft Skill 必须声明 `customer_callable=false`，直到真实 Harness、权限、安全和验收流程完成。
- 每个 read-only Skill 必须声明 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- mock-text/mock-rows Skill 必须声明不得读取真实文件、不得上传、不得生成本地 artifact、不得写业务系统。
- 输出必须保留 `source_rows`、`source_ids`、`source_spans` 或等价证据字段。
- 输出必须保留 `manual_review_required` 和 `manual_review_triggers`。
- 禁止自动发送、发布、上传、写任何业务系统、扣款、退款、改库存、改订阅、记账、报税、创建任务、共享文件。
- 后续如需真实平台 smoke，必须由指挥中心另行批准，并使用 sandbox/测试租户、最小权限、审计日志、脱敏数据和人工复核。

## 4. 未纳入本封装队列的项

- 3 个媒体/provider route-check passed 候选未纳入本队列；如继续推进，必须走独立真实 provider smoke 审批链路，且不得写成真实 provider 已通过：
  - `quality_sprint08_diffusers_product_scene_payload_candidate`
  - `quality_sprint08_replicate_brand_asset_route_candidate`
  - `quality_sprint08_openai_images_packshot_variant_candidate`
- 9 个 `needs_more_license_info` 候选未处理，不能进入本队列。
- 1 个 `component_only` 候选未处理，不能进入本队列。
- smoke passed 但未进入 Top10 的非媒体候选可后续按专题另行排队；本队列不自动覆盖。
