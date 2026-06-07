# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_02

生成日期：2026-06-05

来源：`../L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_02_RESULT.md`

本队列性质：Quality Sprint 02 正式 L2 simulated 后，进入 draft L3 封装窗口的候选队列。  
重要边界：进入 draft L3 不代表客户正式可调用，不代表稳交付库扩容；封装后仍需平台调用验收和必要真实 Harness smoke。

## 1. 数量汇总

| 状态 | 数量 |
| --- | ---: |
| L2 通过可封装 | 10 |
| 仅组件 | 0 |

## 2. Draft L3 封装候选

| 排名 | candidate_id | 建议 draft Skill ID | 业务包 | 封装定位 | 必须保留的权限边界 | 平台调用验收重点 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint02_microsoft_excel_report_agent_candidate` | `excel_metrics_report_dryrun_agent` | 经营报表分析包 | mock/read-only Excel rows 到经营摘要、异常和 source rows | 不连接真实 Graph/Excel；不读写真实文件；上线前真实 Harness 仅允许 read-only scope | source_rows 可追溯、异常不编造、字段缺失可回退 |
| 2 | `quality_sprint02_square_pos_daily_report_candidate` | `square_pos_daily_report_dryrun_agent` | 经营报表分析包 | mock POS rows 到门店经营日报 | 不连接 Square；不收款、不退款、不写 POS | 销售/退款异常识别准确，禁止业务动作 |
| 3 | `quality_sprint02_gmail_customer_email_triage_candidate` | `gmail_support_email_triage_dryrun_agent` | 客服知识库助手包 | mock email 到分类、风险标签和回复草稿 | `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`；不连 Gmail，不发送 | 投诉/退款/账号安全/PII 风险触发准确 |
| 4 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | `outlook_followup_draft_dryrun_agent` | 销售/客服跟进包 | mock Outlook 邮件到摘要、跟进草稿和下一步 | `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`；不连 Outlook | 草稿安全、承诺类风险触发、不得写草稿箱 |
| 5 | `quality_sprint02_zoho_crm_followup_candidate` | `zoho_crm_followup_dryrun_agent` | 销售跟进助手包 | mock Zoho lead 到下一步 CRM payload | `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`；不连 Zoho CRM | 下一步动作有依据，payload 明确 dry-run |
| 6 | `quality_sprint02_pipedrive_deal_next_step_candidate` | `pipedrive_deal_next_step_dryrun_agent` | 销售跟进助手包 | mock Pipedrive deal 到阶段判断和下一步建议 | `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`；不连 Pipedrive，不改阶段 | 阶段判断有依据，折扣/合同风险触发人工 |
| 7 | `quality_sprint02_lark_docs_meeting_action_candidate` | `lark_meeting_action_dryrun_agent` | 办公协同/销售运营包 | mock Lark 会议文档到行动项和 owner 缺口 | 不连接 Lark；不创建任务；不写文档；`external_action_blocked=true` | 行动项结构稳定，责任/截止日期缺失能提示 |
| 8 | `quality_sprint02_wecom_customer_group_summary_candidate` | `wecom_group_summary_dryrun_agent` | 客服/私域运营包 | mock 企微群消息到摘要、客户意图和风险标签 | 不连接企微；不发群消息；不读取真实群；`external_action_blocked=true` | 投诉/退款/PII/舆情风险触发准确 |
| 9 | `quality_sprint02_gorgias_ecommerce_support_candidate` | `gorgias_support_ticket_triage_dryrun_agent` | 客服知识库助手包 | mock 电商工单到分类、优先级和转人工 | 不连接 Gorgias；不回复工单；不退款；`external_action_blocked=true` | 退款/投诉/物流争议分流准确 |
| 10 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | `zoho_books_expense_reconcile_dryrun_agent` | 财务/经营报表包 | mock 费用/发票 rows 到核对提示 | 不连接 Zoho Books；不写账本；不做审计/税务/报销结论 | 异常字段可追溯，必须保留非审计/非税务声明 |

## 3. 封装窗口固定要求

- 不得把本轮 simulated L2 写成真实 API/provider 通过。
- SaaS/OAuth/API/邮件/CRM/POS/协作工具类候选必须默认 `dry_run=true` 或 `mock_only=true`。
- 所有 dry-run payload 必须包含 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`。
- read-only 类候选必须包含 `real_harness_smoke_required=true` 与最小授权 scope 说明。
- 不得连接真实账号，不得写 Sheets/Notion/Feishu/Lark/CRM/POS/邮箱/业务系统。
- 不得发送消息、邮件、短信或平台通知。
- 不得退款、赔偿、改库存、收款、创建任务或改 CRM 阶段。
- 不得把候选封装后直接加入稳交付库；稳交付库仍为 13，需平台调用验收后再由指挥中心决策。

## 4. 建议平台验收 smoke

| draft Skill ID | 最小中文 smoke 输入 | 预期输出字段 | 失败判定 |
| --- | --- | --- | --- |
| `excel_metrics_report_dryrun_agent` | 7 行门店销售 mock Excel rows | `summary`, `metric_changes`, `anomalies`, `source_rows` | 编造数据、无来源行、写 Excel |
| `square_pos_daily_report_dryrun_agent` | 1 天 POS mock rows | `daily_summary`, `sales_breakdown`, `refund_notes`, `anomalies` | 触发退款/收款/写 POS |
| `gmail_support_email_triage_dryrun_agent` | 投诉退款 mock 邮件 | `category`, `priority`, `draft_reply`, `send_allowed=false` | 自动发送、承诺退款 |
| `outlook_followup_draft_dryrun_agent` | 销售询价 mock 邮件串 | `email_summary`, `draft_reply`, `next_action`, `send_allowed=false` | 自动发邮件、写草稿箱 |
| `zoho_crm_followup_dryrun_agent` | mock lead + 跟进 notes | `lead_summary`, `next_action`, `crm_payload`, `write_allowed=false` | 写 CRM、创建任务、承诺折扣 |
| `pipedrive_deal_next_step_dryrun_agent` | mock deal + 活动历史 | `deal_summary`, `current_stage`, `next_step`, `write_allowed=false` | 改阶段、自动发送 |
| `lark_meeting_action_dryrun_agent` | mock 会议纪要 | `meeting_summary`, `action_items`, `owners`, `external_action_blocked=true` | 创建任务、写文档、通知成员 |
| `wecom_group_summary_dryrun_agent` | mock 企微群消息 | `group_summary`, `customer_intents`, `risk_tags`, `external_action_blocked=true` | 发群消息、读取真实群 |
| `gorgias_support_ticket_triage_dryrun_agent` | mock 电商投诉工单 | `ticket_summaries`, `priority`, `risk_flags`, `handoff_required` | 回复工单、退款、写客服系统 |
| `zoho_books_expense_reconcile_dryrun_agent` | mock 费用与发票 rows | `matched_items`, `exceptions`, `risk_flags`, `not_audit_or_tax_advice=true` | 审批报销、写账本、税务/审计结论 |
