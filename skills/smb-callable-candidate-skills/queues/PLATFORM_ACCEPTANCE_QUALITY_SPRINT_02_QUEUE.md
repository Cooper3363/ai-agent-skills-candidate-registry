# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_02_QUEUE

生成日期: 2026-06-05
来源: PACKAGING_QUALITY_SPRINT_02_RESULT.md
性质: 候选库 draft_l3 平台候选调用验收队列；不代表客户正式可调用。

## 验收对象

| draft_skill_id | source_candidate_id | 验收重点 | 强制权限边界 |
| --- | --- | --- | --- |
| excel_metrics_report_dryrun_agent | quality_sprint02_microsoft_excel_report_agent_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| square_pos_daily_report_dryrun_agent | quality_sprint02_square_pos_daily_report_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| gmail_support_email_triage_dryrun_agent | quality_sprint02_gmail_customer_email_triage_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| outlook_followup_draft_dryrun_agent | quality_sprint02_microsoft_graph_outlook_followup_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| zoho_crm_followup_dryrun_agent | quality_sprint02_zoho_crm_followup_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| pipedrive_deal_next_step_dryrun_agent | quality_sprint02_pipedrive_deal_next_step_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| lark_meeting_action_dryrun_agent | quality_sprint02_lark_docs_meeting_action_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| wecom_group_summary_dryrun_agent | quality_sprint02_wecom_customer_group_summary_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| gorgias_support_ticket_triage_dryrun_agent | quality_sprint02_gorgias_ecommerce_support_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| zoho_books_expense_reconcile_dryrun_agent | quality_sprint02_zoho_books_expense_reconcile_candidate | schema 稳定、dry-run payload、风险触发、真实 Harness 待办 | send_allowed=false; write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |

## 固定验收边界

- customer_callable=false。
- platform_deliverable=false。
- stable_baseline_count=13。
- 不得连接真实 SaaS 账号。
- 不得写业务系统或发送消息。
- 不得写 key。
- 不得退款、赔偿、改库存、收款或创建任务。
- 上线前必须补真实 Harness smoke。
