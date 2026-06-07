# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_03_QUEUE

生成日期: 2026-06-05
来源: PACKAGING_QUALITY_SPRINT_03_RESULT.md
性质: 候选库 draft_l3 平台候选调用验收队列；不代表客户正式可调用。

## 验收对象

| draft_skill_id | source_candidate_id | 验收重点 | 强制权限边界 |
| --- | --- | --- | --- |
| shopify_catalog_qc_readonly_agent | quality_sprint03_mcp_shopify_readonly_product_catalog_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| stripe_subscription_health_readonly_agent | quality_sprint03_mcp_stripe_subscription_health_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| notion_policy_gap_readonly_agent | quality_sprint03_mcp_notion_policy_gap_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| airtable_inventory_alert_readonly_agent | quality_sprint03_mcp_airtable_inventory_ops_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| slack_faq_gap_readonly_agent | quality_sprint03_mcp_slack_channel_faq_gap_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| google_drive_doc_classifier_readonly_agent | quality_sprint03_mcp_google_drive_doc_classifier_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| hubspot_contact_health_dryrun_agent | quality_sprint03_mcp_hubspot_contact_health_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| quickbooks_cashflow_warning_readonly_agent | quality_sprint03_mcp_quickbooks_cashflow_warning_candidate | schema 稳定、source 可追溯、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |

## 固定验收边界

- customer_callable=false。
- platform_deliverable=false。
- stable_baseline_count=13。
- 不得连接真实 SaaS/MCP 账号。
- 不得写业务系统或发送消息。
- 不得写 key。
- 不得退款、赔偿、改库存、扣款、改订阅、写账、报税、创建任务或共享文件。
- 上线前必须补真实 Harness smoke。
