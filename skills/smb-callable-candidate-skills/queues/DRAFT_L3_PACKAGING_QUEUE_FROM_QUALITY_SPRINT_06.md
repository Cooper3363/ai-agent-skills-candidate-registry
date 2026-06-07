# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_06

生成日期：2026-06-05

来源：`../L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_06_RESULT.md`

队列性质：Quality Sprint 06 正式 L2 simulated 后的 draft L3 封装准备队列。  
重要边界：进入本队列不代表真实 SaaS/API/Harness/provider 通过，不代表客户正式可调用，不进入稳交付库；客户正式可调用 Skill 仍为 13。

## 1. 入队标准

- L2 结论为：`L2 通过可封装`。
- 可表达为 DeepAgents/通用 Agent Skill callable candidate。
- 当前仅允许 mock/read-only/dry-run 语义。
- SaaS/API connector 必须保留最小只读 scope 或 dry-run 硬断言。
- 后续封装必须补齐真实 Harness smoke 计划、审计日志、错误回退、权限声明和人工复核触发。

## 2. 封装队列

| 排名 | draft_skill_id | source_candidate_id | 业务包 | trial mode | 封装目标 | 必须保留的权限边界 | 最小平台 smoke 输入 | 后续真实 Harness 要求 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `sharepoint_policy_qc_readonly_agent` | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | 知识库/政策 QC 包 | `read_only_mock` | SharePoint 政策缺口、过期政策和 QC flags 只读分析 | `read_only=true`, 最小 pages/files 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox SharePoint pages | 禁止写页面/文件/权限/共享文件 |
| 2 | `teams_handoff_digest_readonly_agent` | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | 协作交接包 | `read_only_mock` | Teams 频道交接 digest 和 owner gap 只读分析 | `read_only=true`, 最小 channel message 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox Teams messages/team roster | 禁止发消息/建任务/写频道 |
| 3 | `google_sheets_budget_variance_readonly_agent` | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | 财务/经营分析包 | `read_only_mock` | Google Sheets 预算差异只读分析 | `read_only=true`, 最小 spreadsheet read-only scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox budget rows | 禁止写单元格/生成文件/写账/报税 |
| 4 | `zendesk_answerbot_deflection_readonly_agent` | `quality_sprint06_zendesk_answerbot_deflection_candidate` | 客服知识库助手包 | `read_only_mock` | Zendesk answerbot deflection 机会只读分析 | `read_only=true`, 最小 tickets/help-center 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox tickets/articles | 禁止回复客户/写文章/改工单 |
| 5 | `hubspot_deal_handoff_quality_dryrun_agent` | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | 销售交接助手包 | `dry_run_only` | HubSpot deal handoff quality 和不可执行 payload | `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox deals/notes | 禁止写 deal/note/task、发邮件、上传 |
| 6 | `stripe_failed_payment_recovery_draft_readonly_agent` | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | 付款挽回草稿包 | `read_only_mock` | Stripe 失败支付挽回草稿只读分析 | `read_only=true`, 最小 invoices/payment metadata 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox failed payments/invoices | 禁止扣款/退款/改订阅/发送催收 |
| 7 | `bamboohr_timeoff_coverage_readonly_agent` | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | HR 排班覆盖包 | `read_only_mock` | BambooHR 请假覆盖风险只读分析 | `read_only=true`, 最小 time-off/employee metadata 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox time-off rows/staffing rules | 禁止改排班/改请假状态/发通知/做 HR 决策 |
| 8 | `gmail_label_health_readonly_agent` | `quality_sprint06_google_workspace_gmail_label_health_candidate` | 邮箱运营健康包 | `read_only_mock` | Gmail label health metadata-only 只读分析 | `read_only=true`, 最小 labels/metadata 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox labels/message headers | 禁止读真实正文/发送/改标签 |

## 3. 封装窗口统一要求

- 每个 draft Skill 必须声明 `customer_callable=false`，直到真实 Harness、权限、安全和验收流程完成。
- 每个 read-only Skill 必须声明 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- HubSpot dry-run Skill 必须声明 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- 输出必须保留 `source_rows`、`source_ids` 或等价证据字段。
- 输出必须保留 `manual_review_required` 和 `manual_review_triggers`。
- 禁止自动发送、发布、上传、写 M365/Google/Zendesk/HubSpot/Stripe/BambooHR/Gmail 或业务系统、扣款、退款、改订阅、创建任务、共享文件。
- 后续如需真实平台 smoke，必须由指挥中心另行批准并使用沙盒账号、最小权限和审计日志。

## 4. 未纳入本封装队列的项

- 媒体/provider route-check passed 候选未纳入本队列；如继续推进，必须走独立真实 provider smoke 审批链路。
- Freshdesk/Shopify/DocuSign/PostHog/Mailchimp passed 候选未纳入本队列；建议后续按客服运营/电商订阅/签约/分析/邮件专题补做正式 L2。
- `needs_more_license_info` 与 `component_only` 项未处理，不能进入本队列。
