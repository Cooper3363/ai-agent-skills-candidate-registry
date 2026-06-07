# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_04

生成日期：2026-06-05

来源：`../L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_04_RESULT.md`

队列性质：Quality Sprint 04 正式 L2 simulated 后的 draft L3 封装准备队列。  
重要边界：进入本队列不代表真实 Harness/API 通过，不代表客户正式可调用，不进入稳交付库；客户正式可调用 Skill 仍为 13。

## 1. 入队标准

- L2 结论为：`L2 通过可封装`。
- 可表达为 DeepAgents/通用 Agent Skill callable candidate。
- 当前仅允许 mock/read-only/dry-run 语义。
- SaaS/API connector 必须保留最小只读 scope 或 dry-run 硬断言。
- 后续封装必须补齐真实 Harness smoke 计划、审计日志、错误回退、权限声明和人工复核触发。

## 2. 封装队列

| 排名 | draft_skill_id | source_candidate_id | 业务包 | trial mode | 封装目标 | 必须保留的权限边界 | 最小平台 smoke 输入 | 后续真实 Harness 要求 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `zendesk_sla_macro_gap_readonly_agent` | `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | 客服知识库助手包 | `read_only_mock` | Zendesk SLA 风险与 macro 缺口只读分析 | `read_only=true`, 最小 ticket/macro/help-center 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox tickets/macros/help-center rows | 只读 OAuth scope、工单来源行、禁止回复/改状态/写 macro |
| 2 | `freshdesk_ticket_sla_risk_readonly_agent` | `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | 客服知识库助手包 | `read_only_mock` | Freshdesk SLA 超时风险与升级建议 | `read_only=true`, 最小 ticket/SLA 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox tickets/SLA rows | 只读 OAuth scope、风险等级稳定性、禁止回复/改状态 |
| 3 | `salesforce_opportunity_hygiene_dryrun_agent` | `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | 销售跟进助手包 | `dry_run_only` | Salesforce 商机卫生检查与不可执行 payload | `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox opportunities/accounts rows | dry-run schema、禁止写商机/联系人/任务/邮件、审计日志 |
| 4 | `shopline_catalog_qc_readonly_agent` | `quality_sprint04_shopline_catalog_qc_readonly_candidate` | 电商运营/销售助手包 | `read_only_mock` | Shopline 商品目录字段与价格/图片风险 QC | `read_only=true`, 最小 catalog 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox product catalog rows | 禁止改商品/价格/库存/上下架，素材与禁售词复核 |
| 5 | `lightspeed_pos_shift_anomaly_readonly_agent` | `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | 经营报表/门店运营包 | `read_only_mock` | Lightspeed POS 班次、退款、交班异常摘要 | `read_only=true`, 最小 shift/report 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox POS shift rows | 禁止退款/改库存/写 POS，员工处罚需人工排除 |
| 6 | `xero_bank_reconcile_exception_readonly_agent` | `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | 财务/经营报表包 | `read_only_mock` | Xero 银行对账异常提示 | `read_only=true`, 最小 transactions/invoices 只读 scope, `write_allowed=false`, `external_action_blocked=true`, `not_audit_or_tax_advice=true` | sandbox transactions/invoices rows | 禁止写账/付款/报税，非审计/非税务建议声明 |
| 7 | `posthog_funnel_dropoff_readonly_agent` | `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | 产品/营销分析包 | `read_only_mock` | PostHog 漏斗掉点和数据质量只读分析 | `read_only=true`, 最小 event/funnel 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox funnel/event stats | 禁止改 tracking 配置，低样本和事件缺失提示 |
| 8 | `linear_customer_bug_triage_readonly_agent` | `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | 产品/客服协同包 | `read_only_mock` | Linear 客户反馈 bug 影响分流 | `read_only=true`, 最小 issue/comment 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox issues/customer feedback rows | 禁止写 issue/comment/status，安全和数据丢失强制复核 |
| 9 | `monday_board_health_readonly_agent` | `quality_sprint04_monday_board_health_readonly_candidate` | 办公协同/项目运营包 | `read_only_mock` | monday 看板健康和负责人缺口只读分析 | `read_only=true`, 最小 board item 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox board items | 禁止写 item/comment/status，负责人分配需人工确认 |
| 10 | `clickup_task_risk_readonly_agent` | `quality_sprint04_clickup_task_risk_readonly_candidate` | 办公协同/项目运营包 | `read_only_mock` | ClickUp 延期、依赖阻塞和交接风险只读分析 | `read_only=true`, 最小 task/list 只读 scope, `write_allowed=false`, `external_action_blocked=true` | sandbox tasks/dependency rows | 禁止写任务/comment/status，客户承诺日期需人工确认 |

## 3. 封装窗口统一要求

- 每个 draft Skill 必须声明 `customer_callable=false`，直到真实 Harness、权限、安全和验收流程完成。
- 每个 read-only Skill 必须声明 `read_only=true`、最小只读 scope、`write_allowed=false`、`external_action_blocked=true`。
- Salesforce dry-run Skill 必须声明 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- 输出必须保留 `source_rows` 或等价证据字段，避免无来源判断。
- 输出必须保留 `manual_review_required` 和 `manual_review_triggers`。
- 禁止自动发送、发布、上传、写 CRM/POS/财务/协作系统、改库存、扣款、退款、报税、创建任务、共享文件。
- 后续如需真实平台 smoke，必须由指挥中心另行批准并使用沙盒账号、最小权限和审计日志。

## 4. 未纳入本封装队列的项

- 媒体/provider route-check passed 候选未纳入本队列；如继续推进，必须走独立真实 provider smoke 审批链路。
- Mailchimp/Brevo passed 候选未纳入本队列；建议后续放入邮件营销健康专题 L2。
- `needs_more_license_info` 与 `component_only` 项未处理，不能进入本队列。
