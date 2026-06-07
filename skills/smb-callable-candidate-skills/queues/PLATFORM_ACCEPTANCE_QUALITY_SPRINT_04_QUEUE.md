# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_04_QUEUE

生成日期: 2026-06-05
来源: PACKAGING_QUALITY_SPRINT_04_RESULT.md
性质: 候选库 draft_l3 平台候选调用验收队列；不代表客户正式可调用。

## 验收对象

| draft_skill_id | source_candidate_id | 验收重点 | 强制权限边界 |
| --- | --- | --- | --- |
| zendesk_sla_macro_gap_readonly_agent | quality_sprint04_zendesk_sla_macro_gap_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| freshdesk_ticket_sla_risk_readonly_agent | quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| salesforce_opportunity_hygiene_dryrun_agent | quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| shopline_catalog_qc_readonly_agent | quality_sprint04_shopline_catalog_qc_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| lightspeed_pos_shift_anomaly_readonly_agent | quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| xero_bank_reconcile_exception_readonly_agent | quality_sprint04_xero_bank_reconcile_exception_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| posthog_funnel_dropoff_readonly_agent | quality_sprint04_posthog_funnel_dropoff_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| linear_customer_bug_triage_readonly_agent | quality_sprint04_linear_customer_bug_triage_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| monday_board_health_readonly_agent | quality_sprint04_monday_board_health_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |
| clickup_task_risk_readonly_agent | quality_sprint04_clickup_task_risk_readonly_candidate | schema、source/evidence、审计日志、错误回退、人工复核、真实 Harness 待办 | write_allowed=false; external_action_blocked=true; real_harness_smoke_required=true |

## 固定验收边界

- customer_callable=false。
- platform_deliverable=false。
- stable_baseline_count=13。
- 不得连接真实 SaaS 账号。
- 不得写业务系统或发送消息。
- 不得写 key。
- 不得退款、赔偿、扣款、改库存、改订阅、写账、报税、创建任务或共享文件。
- Xero 包必须保留 not_audit_or_tax_advice=true。
- 上线前必须补真实 Harness smoke。
