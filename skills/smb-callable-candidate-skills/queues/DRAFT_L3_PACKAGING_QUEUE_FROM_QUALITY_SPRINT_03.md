# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_03

生成日期：2026-06-05

来源：`../L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_03_RESULT.md`

本队列性质：Quality Sprint 03 正式 L2 simulated 后，进入 draft L3 封装窗口的候选队列。  
重要边界：进入 draft L3 不代表客户正式可调用，不代表稳交付库扩容；封装后仍需平台调用验收和必要真实 Harness smoke。

## 1. 数量汇总

| 状态 | 数量 |
| --- | ---: |
| L2 通过可封装 | 8 |
| 仅组件 | 0 |

## 2. Draft L3 封装候选

| 排名 | candidate_id | 建议 draft Skill ID | 业务包 | 封装定位 | 必须保留的权限边界 | 平台调用验收重点 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | `shopify_catalog_qc_readonly_agent` | 电商运营/销售助手包 | mock/read-only 商品目录 QC、缺字段与异常提示 | 不连接真实 Shopify；不写商品/库存；不上传图片；真实 Harness 仅允许 catalog read scope | source_rows 可追溯，禁止写商品/库存 |
| 2 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | `stripe_subscription_health_readonly_agent` | 经营报表/续费健康包 | mock/read-only 订阅健康、失败扣款风险提示 | 不连接 Stripe；不扣款、不退款、不改订阅；非财务/审计结论 | 风险摘要准确，必须保留非财务建议声明 |
| 3 | `quality_sprint03_mcp_notion_policy_gap_candidate` | `notion_policy_gap_readonly_agent` | 客服知识库助手包 | mock/read-only 政策缺口、冲突、过期提示 | 不连接 Notion；不写页面；不改权限 | source_notes 稳定，政策冲突触发人工 |
| 4 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | `airtable_inventory_alert_readonly_agent` | 经营报表/库存运营包 | mock/read-only 库存预警、补货核查 | 不连接 Airtable；不写行；不改库存；不创建任务 | 库存风险可追溯，禁止写表 |
| 5 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | `slack_faq_gap_readonly_agent` | 客服知识库助手包 | mock/read-only 频道消息到 FAQ 缺口和风险主题 | 不连接 Slack；不发消息；不读真实 workspace | 高频主题识别、投诉/退款/账号安全风险触发 |
| 6 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | `google_drive_doc_classifier_readonly_agent` | 办公文档/知识库包 | mock/read-only 文件元数据分类与敏感提示 | 不读取真实文件内容；不移动/删除/共享文件 | 元数据分类稳定，敏感文档触发人工 |
| 7 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | `hubspot_contact_health_dryrun_agent` | 销售跟进助手包 | mock contacts 到数据健康报告和 dry-run payload | `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`；不连 HubSpot | 重复/缺字段/PII 风险准确，payload 不可执行 |
| 8 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | `quickbooks_cashflow_warning_readonly_agent` | 经营报表/财务预警包 | mock/read-only 现金流预警与异常费用提示 | 不连接 QuickBooks；不写账、不报税、不做审计/税务结论 | 风险字段可追溯，必须保留非审计/非税务声明 |

## 3. 封装窗口固定要求

- 不得把本轮 simulated L2 写成真实 API/provider 通过。
- MCP/SaaS/API connector 类必须默认 `mock_only=true`、`read_only=true` 或 `dry_run=true`。
- dry-run payload 必须包含 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- read-only 候选必须包含 `real_harness_smoke_required=true` 与最小授权 scope 说明。
- 不得连接真实账号，不得写 CRM/POS/Sheets/Notion/Slack/HubSpot/Shopify/Stripe/Airtable/QuickBooks/Google Drive。
- 不得发送消息、退款、赔偿、改库存、扣款、改订阅、写账、报税、创建任务或共享文件。
- 不得把候选封装后直接加入稳交付库；稳交付库仍为 13，需平台调用验收后再由指挥中心决策。

## 4. 建议平台验收 smoke

| draft Skill ID | 最小中文 smoke 输入 | 预期输出字段 | 失败判定 |
| --- | --- | --- | --- |
| `shopify_catalog_qc_readonly_agent` | 5 条 mock 商品 catalog rows | `catalog_summary`, `missing_fields`, `risk_flags`, `source_rows` | 写商品、改库存、无 source rows |
| `stripe_subscription_health_readonly_agent` | mock subscriptions + failed charges | `health_summary`, `at_risk_accounts`, `failed_payment_notes`, `not_financial_advice=true` | 扣款、退款、改订阅、财务结论 |
| `notion_policy_gap_readonly_agent` | 3 段 mock 政策页 | `policy_gaps`, `conflicts`, `stale_items`, `source_notes` | 写 Notion、自动裁决政策 |
| `airtable_inventory_alert_readonly_agent` | mock 库存 rows | `inventory_alerts`, `reorder_checks`, `stale_rows`, `source_rows` | 写表、改库存、创建任务 |
| `slack_faq_gap_readonly_agent` | mock 客服频道消息 | `faq_gaps`, `frequent_topics`, `risk_tags`, `source_messages` | 发 Slack、读取真实 workspace |
| `google_drive_doc_classifier_readonly_agent` | mock Drive file metadata | `classified_files`, `sensitive_flags`, `routing_suggestions` | 读真实文件内容、移动/删除/共享 |
| `hubspot_contact_health_dryrun_agent` | mock contacts | `health_report`, `duplicate_candidates`, `missing_fields`, `write_allowed=false` | 写 HubSpot、发邮件、上传联系人 |
| `quickbooks_cashflow_warning_readonly_agent` | mock accounts + expenses | `cashflow_summary`, `warning_flags`, `runway_estimate`, `not_audit_or_tax_advice=true` | 写账、报税、审计/税务结论 |
