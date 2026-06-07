# DEEPAGENTS_SMOKE_QUALITY_SPRINT_02_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_02_RESULT.md`

本队列只包含 L1 放行项：`can_mock_smoke`、`can_dry_run_smoke`、`can_route_check`。

硬边界：

- 不调用真实 API/provider。
- 不安装。
- 不写 key。
- 不读取客户文件。
- 不生成图片、视频、音频、PDF。
- 不写 SaaS/CRM/日历/任务/业务系统。
- 媒体/provider 类只允许 payload/route-check，不允许真实生成。
- SaaS/API 类只允许 mock/read-only/dry-run，不连接真实账号。
- 本轮不送正式 L2。

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 8 |
| `can_dry_run_smoke` | 8 |
| `can_route_check` | 13 |
| smoke queue total | 29 |

## Queue

| # | priority | candidate_id | smoke_type | trial_mode | provider_boundary | notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint02_microsoft_excel_report_agent_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Excel/Graph read | mock workbook rows -> weekly report |
| 2 | P0 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | dry-run | `dry_run_only`, `read_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock emails -> follow-up draft |
| 3 | P0 | `quality_sprint02_stability_product_scene_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Stability disabled | product info -> scene image payload |
| 4 | P0 | `quality_sprint02_adobe_firefly_product_ad_image_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Firefly disabled | activity brief -> image JSON |
| 5 | P0 | `quality_sprint02_fal_flux_product_photo_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | fal disabled | product metadata -> provider payload |
| 6 | P0 | `quality_sprint02_runway_gen4_short_ad_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Runway disabled | campaign brief -> video payload |
| 7 | P0 | `quality_sprint02_gmail_customer_email_triage_candidate` | dry-run | `dry_run_only`, `read_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock email -> triage + draft |
| 8 | P0 | `quality_sprint02_zoho_crm_followup_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | write_allowed=false | mock leads -> next action |
| 9 | P0 | `quality_sprint02_lark_docs_meeting_action_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no task creation | mock meeting doc -> action list |
| 10 | P0 | `quality_sprint02_recraft_brand_banner_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Recraft disabled | brand brief -> banner payload |
| 11 | P0 | `quality_sprint02_pipedrive_deal_next_step_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | write_allowed=false | mock deals -> next-step report |
| 12 | P0 | `quality_sprint02_square_pos_daily_report_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real POS read | mock POS rows -> daily report |
| 13 | P1 | `quality_sprint02_ideogram_poster_text_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Ideogram disabled | poster prompt/payload |
| 14 | P1 | `quality_sprint02_fal_kontext_image_edit_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | fal disabled | image edit instruction payload |
| 15 | P1 | `quality_sprint02_removebg_cutout_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | remove.bg disabled | image metadata -> cutout payload |
| 16 | P1 | `quality_sprint02_luma_dream_machine_store_video_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Luma disabled | store brief -> video payload |
| 17 | P1 | `quality_sprint02_wecom_customer_group_summary_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock group messages -> summary |
| 18 | P1 | `quality_sprint02_gorgias_ecommerce_support_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no ticket reply | mock tickets -> triage |
| 19 | P1 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | non-audit | mock expenses -> reconcile hints |
| 20 | P1 | `quality_sprint02_google_veo_store_campaign_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Veo/Gemini disabled | Chinese brief -> video payload |
| 21 | P1 | `quality_sprint02_heygen_training_avatar_cn_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | HeyGen disabled | training script -> avatar payload |
| 22 | P1 | `quality_sprint02_haystack_faq_rag_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | mock docs only | mock docs -> cited answer |
| 23 | P1 | `quality_sprint02_shopline_order_digest_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real orders | mock orders -> ops digest |
| 24 | P1 | `quality_sprint02_feishu_bitable_ops_tracker_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no write rows | mock rows -> ops tracker summary |
| 25 | P1 | `quality_sprint02_mailchimp_campaign_report_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock campaign stats -> report |
| 26 | P1 | `quality_sprint02_autogen_sales_roleplay_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real tools | mock lead -> roleplay script/eval |
| 27 | P1 | `quality_sprint02_crewai_market_research_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no browsing/API | mock company -> research brief |
| 28 | P1 | `quality_sprint02_instructor_schema_extraction_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | mock text only | mock text -> typed JSON |
| 29 | P1 | `quality_sprint02_promptfoo_support_regression_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | mock eval only | 3 mock cases -> eval report |

