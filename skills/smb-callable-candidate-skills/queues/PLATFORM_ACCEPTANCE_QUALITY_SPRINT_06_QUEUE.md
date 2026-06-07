# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_06_QUEUE

生成时间: 2026-06-05
来源: PACKAGING_QUALITY_SPRINT_06_RESULT.md
队列性质: Quality Sprint 06 draft_l3 候选调用验收复验队列。

重要边界：本队列不代表客户正式可调用，不进入稳交付库；客户正式可调用数量仍为 13。

| draft_skill_id | source_candidate_id | 验收状态 | 必查边界 |
| --- | --- | --- | --- |
| `sharepoint_policy_qc_readonly_agent` | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `teams_handoff_digest_readonly_agent` | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `google_sheets_budget_variance_readonly_agent` | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `zendesk_answerbot_deflection_readonly_agent` | `quality_sprint06_zendesk_answerbot_deflection_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `hubspot_deal_handoff_quality_dryrun_agent` | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `stripe_failed_payment_recovery_draft_readonly_agent` | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `bamboohr_timeoff_coverage_readonly_agent` | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `gmail_label_health_readonly_agent` | `quality_sprint06_google_workspace_gmail_label_health_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |

## 平台验收重点

- 校验 SKILL.md 与 skill.yaml 是否齐全。
- 校验 status=draft_l3、customer_callable=false、platform_deliverable=false、stable_baseline_count=13。
- 校验 7 个 read-only 包保留 read_only=true、最小只读 scope、write_allowed=false、send_allowed=false、upload_allowed=false、external_action_blocked=true、real_harness_smoke_required=true。
- 校验 HubSpot dry-run 包保留 send_allowed=false、write_allowed=false、upload_allowed=false、external_action_blocked=true。
- 校验 Stripe 包不得扣款、退款、改订阅、发送催收，只能生成草稿/建议。
- 校验 BambooHR 包不得改排班、改请假状态、发通知、做 HR 决策。
- 校验 Microsoft Graph / Google Workspace / Gmail 包不连接真实租户、不读客户真实文件、不发邮件/Teams 消息、不写标签或文档。
- 校验 read_only_scope_manifest 或 dry_run_payload_schema、audit_log_schema、error_fallback_strategy、manual_review_triggers。
- 校验真实 Harness smoke 待办，不得把 simulated L2 误写为真实 API/SaaS/provider passed。
