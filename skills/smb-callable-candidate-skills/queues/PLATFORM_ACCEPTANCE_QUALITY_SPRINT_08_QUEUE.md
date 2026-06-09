# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_08_QUEUE

生成时间: 2026-06-09
来源: PACKAGING_QUALITY_SPRINT_08_RESULT.md
队列性质: Quality Sprint 08 draft_l3 候选调用验收复验队列。

重要边界：本队列不代表客户正式可调用，不进入 stable 仓库；stable 当前正式 Skill 数为 71。

| draft_skill_id | source_candidate_id | 验收状态 | 必查边界 |
| --- | --- | --- | --- |
| `superset_dashboard_digest_readonly_agent` | `quality_sprint08_superset_dashboard_digest_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `redash_query_anomaly_digest_readonly_agent` | `quality_sprint08_redash_query_anomaly_digest_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `calcom_meeting_prep_readonly_agent` | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `pandadoc_proposal_status_readonly_agent` | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `medusa_catalog_qc_readonly_agent` | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `saleor_order_margin_readonly_agent` | `quality_sprint08_saleor_order_margin_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `sylius_promo_margin_readonly_agent` | `quality_sprint08_sylius_promo_margin_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `rasa_intent_policy_gap_mock_agent` | `quality_sprint08_rasa_intent_policy_gap_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `unstructured_support_sop_parser_mock_text_agent` | `quality_sprint08_unstructured_support_sop_parser_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |
| `actualbudget_cashflow_warning_mock_rows_agent` | `quality_sprint08_actualbudget_cashflow_warning_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=71, real_harness_smoke_required=true |

## 平台验收重点

- 校验 SKILL.md 与 skill.yaml 是否齐全。
- 校验 status=draft_l3、customer_callable=false、platform_deliverable=false、stable_current_count=71。
- 校验 SaaS/API/read-only 包保留 read_only=true、最小只读 scope、write_allowed=false、send_allowed=false、upload_allowed=false、external_action_blocked=true、real_harness_smoke_required=true。
- 校验 mock/text/rows 包不读真实文件、不上传、不生成 artifact、不训练/部署、不接 live chat、不读真实账本、不银行同步、不写交易。
- 校验 Superset/Redash 不执行 SQL/query、不连接 DB/API、不写 dashboard。
- 校验 Cal.com 不写 booking、不发送邮件/日历。
- 校验 PandaDoc 不发送文档、不发签名请求、不写状态。
- 校验 Medusa/Saleor/Sylius 不写商品/订单/库存/促销/catalog/checkout。
- 校验 audit_log_schema、error_fallback_strategy、manual_review_triggers、failure_modes。
- 校验真实 Harness smoke 待办，不得把 simulated L2 误写为真实 API/SaaS/provider passed 或 stable promotion passed。
