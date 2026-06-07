# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_07_QUEUE

生成时间: 2026-06-07
来源: PACKAGING_QUALITY_SPRINT_07_RESULT.md
队列性质: Quality Sprint 07 draft_l3 候选调用验收复验队列。

重要边界：本队列不代表客户正式可调用，不进入 stable 仓库；stable 当前正式 Skill 数为 63。

| draft_skill_id | source_candidate_id | 验收状态 | 必查边界 |
| --- | --- | --- | --- |
| `intercom_article_decay_readonly_agent` | `quality_sprint07_intercom_article_decay_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |
| `shopify_return_product_quality_readonly_agent` | `quality_sprint07_shopify_return_product_quality_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |
| `metabase_executive_digest_readonly_agent` | `quality_sprint07_metabase_executive_digest_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |
| `docusign_missing_signature_readonly_agent` | `quality_sprint07_docusign_missing_signature_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |
| `mailchimp_deliverability_qc_readonly_agent` | `quality_sprint07_mailchimp_deliverability_qc_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |
| `helpscout_saved_reply_gap_readonly_agent` | `quality_sprint07_helpscout_saved_reply_gap_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |
| `front_account_handoff_readonly_agent` | `quality_sprint07_front_account_handoff_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |
| `amplitude_activation_dropoff_readonly_agent` | `quality_sprint07_amplitude_activation_dropoff_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_current_count=63, read_only=true, real_harness_smoke_required=true |

## 平台验收重点

- 校验 SKILL.md 与 skill.yaml 是否齐全。
- 校验 status=draft_l3、customer_callable=false、platform_deliverable=false、stable_current_count=63。
- 校验 8 个 read-only 包保留 read_only=true、最小只读 scope、write_allowed=false、send_allowed=false、upload_allowed=false、external_action_blocked=true、real_harness_smoke_required=true。
- 校验 read_only_scope_manifest、audit_log_schema、error_fallback_strategy、manual_review_triggers、failure_modes。
- 校验 OpenAI-compatible 中转站模型通道说明：模型/base_url/key/timeout/成本阈值由平台运行时注入，repo 不写 key。
- 校验真实 Harness smoke 待办，不得把 simulated L2 误写为真实 API/SaaS/provider passed 或 stable promotion passed。
