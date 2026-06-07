# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_01_QUEUE

生成日期: 2026-06-05
来源: PACKAGING_QUALITY_SPRINT_01_RESULT.md
性质: 候选库 draft_l3 平台候选调用验收队列；不代表客户正式可调用。

## 验收对象

| draft_skill_id | source_candidate_id | 验收重点 | 强制权限边界 |
| --- | --- | --- | --- |
| sheets_metrics_report_dryrun_agent | quality_sprint01_google_sheets_mcp_report_agent_candidate | schema 稳定、source_rows 可追溯、异常不编造、字段缺失能回退 | 不连接真实 Google Sheets；不写表；send/write blocked |
| notion_kb_gap_review_dryrun_agent | quality_sprint01_notion_ops_knowledge_agent_candidate | source_notes 稳定、政策冲突触发人工复核、不自动发布 | 不连接真实 Notion；不写页面；send/write blocked |
| slack_support_triage_dryrun_agent | quality_sprint01_slack_support_triage_agent_candidate | 投诉/退款/账号安全/PII 风险触发准确，dry-run payload 不可执行 | 不连 Slack；不发消息；send/write blocked |
| hubspot_crm_followup_dryrun_agent | quality_sprint01_hubspot_crm_followup_agent_candidate | 下一步动作有依据，折扣/合同/PII 触发人工复核，payload 明确 dry-run | 不连 HubSpot；不写 CRM；send/write blocked |

## 固定验收边界

- customer_callable=false。
- platform_deliverable=false。
- stable_baseline_count=13。
- 不得连接真实 SaaS 账号。
- 不得写业务系统或发送消息。
- 不得写 key。
- 上线前必须补真实 Harness smoke。
