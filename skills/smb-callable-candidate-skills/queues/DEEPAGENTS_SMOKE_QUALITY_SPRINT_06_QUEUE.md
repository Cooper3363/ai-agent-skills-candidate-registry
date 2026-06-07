# DEEPAGENTS_SMOKE_QUALITY_SPRINT_06_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_06_RESULT.md`

本队列只包含 L1 放行项：`can_mock_smoke`、`can_dry_run_smoke`、`can_route_check`。

硬边界：

- 不安装依赖。
- 不访问外网。
- 不调用真实 API/provider。
- 不读取、打印或写入 key。
- 不读取客户文件。
- 不上传素材。
- 不发送消息。
- 不写 CRM/POS/财务/HR/协作/营销/客服系统。
- 不生成真实图片、视频、音频、HTML、PDF、PPT 或任何文件。
- SaaS/API connector 只允许 mock/read-only/dry-run，不连接真实账号。
- 媒体/provider 只允许 route/config/payload check，不真实生成。
- 本轮不送正式 L2，不封装，不客户调用。

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 12 |
| `can_dry_run_smoke` | 1 |
| `can_route_check` | 5 |
| smoke queue total | 18 |

## Queue

| # | priority | candidate_id | smoke_type | trial_mode | provider_boundary | notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real M365 tenant | mock SharePoint pages -> policy gap report |
| 2 | P0 | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Teams tenant | mock Teams messages -> handoff digest |
| 3 | P0 | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Sheets read/write | mock budget rows -> variance report |
| 4 | P0 | `quality_sprint06_zendesk_answerbot_deflection_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Zendesk account | mock tickets/articles -> deflection opportunities |
| 5 | P0 | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | write_allowed=false | mock deals/notes -> handoff quality report |
| 6 | P0 | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Stripe read/write | mock failed payments -> recovery draft |
| 7 | P0 | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real BambooHR records | mock time-off rows -> coverage summary |
| 8 | P0 | `quality_sprint06_openai_image_brand_scene_batch_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI Images disabled | brand brief -> batch image payload JSON |
| 9 | P0 | `quality_sprint06_runway_storyboard_to_clip_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Runway disabled | storyboard -> video payload only |
| 10 | P1 | `quality_sprint06_google_workspace_gmail_label_health_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Gmail read/send | mock labels/message headers -> label health report |
| 11 | P1 | `quality_sprint06_freshdesk_agent_workload_balance_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Freshdesk account | mock tickets/agents -> workload balance |
| 12 | P1 | `quality_sprint06_shopify_subscription_order_exception_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Shopify store | mock orders/customers -> exception summary |
| 13 | P1 | `quality_sprint06_docusign_renewal_notice_gap_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real DocuSign envelopes | mock envelopes -> renewal notice gaps |
| 14 | P1 | `quality_sprint06_posthog_funnel_dropoff_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real PostHog project | mock funnel metrics -> dropoff report |
| 15 | P1 | `quality_sprint06_mailchimp_audience_health_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock audience metrics -> health report |
| 16 | P1 | `quality_sprint06_openai_tts_customer_training_audio_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI TTS disabled | training script -> TTS payload JSON |
| 17 | P1 | `quality_sprint06_fal_product_model_tryon_route_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | fal disabled | product/model metadata -> route payload |
| 18 | P1 | `quality_sprint06_heygen_sales_objection_avatar_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | HeyGen disabled | objection script -> avatar payload only |

## Excluded From Smoke

| candidate_id | l1_result | reason |
| --- | --- | --- |
| `quality_sprint06_wondelai_skill_pack_specific_scan_candidate` | `needs_more_license_info` | 必须逐目录核具体 `SKILL.md` 与 LICENSE，不允许整包放行 |
| `quality_sprint06_openclaw_uiux_pro_max_official_path_candidate` | `needs_more_license_info` | 需确认子目录存在、LICENSE、`SKILL.md`、脚本/工具和文件生成边界 |
| `quality_sprint06_guizang_ppt_license_followup_candidate` | `needs_more_license_info` | 需确认 LICENSE、assets/references、HTML/PPT 文件生成、截图/导出边界 |
| `quality_sprint06_agency_ops_coordinator_role_candidate` | `component_only` | role component，不进普通 candidate smoke，不进 draft L3 |
| `quality_sprint06_agency_purchase_admin_role_candidate` | `component_only` | role component，不进普通 candidate smoke，不进 draft L3 |
| `quality_sprint06_promptfoo_customer_reply_safety_candidate` | `component_only` | eval component，不进普通 candidate smoke，不进 draft L3 |
| `quality_sprint06_instructor_sales_call_schema_candidate` | `component_only` | schema component，不进普通 candidate smoke，不进 draft L3 |

