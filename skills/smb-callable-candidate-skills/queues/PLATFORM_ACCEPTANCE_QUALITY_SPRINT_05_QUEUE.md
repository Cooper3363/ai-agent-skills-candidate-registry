# PLATFORM_ACCEPTANCE_QUALITY_SPRINT_05_QUEUE

生成时间: 2026-06-05
来源: PACKAGING_QUALITY_SPRINT_05_RESULT.md
队列性质: Quality Sprint 05 draft_l3 候选调用验收复验队列。

重要边界：本队列不代表客户正式可调用，不进入稳交付库；客户正式可调用数量仍为 13。

| draft_skill_id | source_candidate_id | 验收状态 | 必查边界 |
| --- | --- | --- | --- |
| `intercom_conversation_macro_gap_readonly_agent` | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `helpscout_article_gap_readonly_agent` | `quality_sprint05_helpscout_article_gap_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `front_inbox_handoff_readonly_agent` | `quality_sprint05_front_inbox_handoff_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `klaviyo_campaign_health_readonly_agent` | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `woocommerce_catalog_qc_readonly_agent` | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `bigcommerce_catalog_gap_readonly_agent` | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `google_ads_creative_budget_anomaly_readonly_agent` | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `ga4_landing_page_dropoff_readonly_agent` | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `canva_design_brief_dryrun_agent` | `quality_sprint05_canva_design_brief_dryrun_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |
| `jira_service_sla_readonly_agent` | `quality_sprint05_jira_service_sla_readonly_candidate` | pending_candidate_retest | customer_callable=false, platform_deliverable=false, stable_baseline_count=13, real_harness_smoke_required=true |

## 平台验收重点

- 校验 SKILL.md 与 skill.yaml 是否齐全。
- 校验 status=draft_l3、customer_callable=false、platform_deliverable=false、stable_baseline_count=13。
- 校验 9 个 read-only 包保留 read_only=true、最小只读 scope、write_allowed=false、send_allowed=false、upload_allowed=false、external_action_blocked=true、real_harness_smoke_required=true。
- 校验 Canva dry-run 包保留 send_allowed=false、write_allowed=false、upload_allowed=false、external_action_blocked=true、real_media_generation_allowed=false、export_allowed=false。
- 校验 Google Ads 包 no_seo_or_ads_performance_guarantee=true。
- 校验 GA4 包 analytics_not_causality=true。
- 校验审计日志、错误回退、人工复核触发和失败判定。
- 校验真实 Harness smoke 待办，不得把 simulated L2 误写为真实 API/SaaS/provider passed。
