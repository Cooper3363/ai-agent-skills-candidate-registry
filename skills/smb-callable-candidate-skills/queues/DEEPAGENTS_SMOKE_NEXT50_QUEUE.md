# DEEPAGENTS_SMOKE_NEXT50_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_NEXT50_RESULT.md`

本队列只包含 L1 放行项：`can_mock_smoke`、`can_dry_run_smoke`、`can_route_check`。

统一边界：

- 不安装依赖。
- 不写真实 API key。
- 不调用真实 provider/API。
- 不真实生成图片、视频、音频、PPT 或文件。
- 不上传客户素材。
- 不发送、不发布、不写 CRM/Shopify/Figma/Canva/审批系统/广告账户。
- 许可证不清或上游不明项不得进入本队列。
- 本轮不送正式 L2。

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 10 |
| `can_dry_run_smoke` | 30 |
| `can_route_check` | 5 |
| smoke queue total | 45 |

## Queue

| # | candidate_id | smoke_type | trial_mode | provider_boundary | notes |
| ---: | --- | --- | --- | --- | --- |
| 1 | `support_voice_call_summary_agent_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real audio upload | 使用 mock transcript 做摘要 |
| 2 | `support_training_microvideo_agent_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | HeyGen disabled | 只生成 payload，不生成视频 |
| 3 | `support_reply_multilingual_localizer_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | text relay only | 只做本地化文本 |
| 4 | `support_faq_video_answer_script_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Synthesia disabled | 只生成脚本/payload |
| 5 | `support_ticket_auto_reply_quality_gate_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no send | 只做回复质检闸门 |
| 6 | `support_complaint_evidence_packet_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real files | 只用 mock 投诉文本 |
| 7 | `support_afterhours_triage_bot_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | text relay only | 只做分流建议 |
| 8 | `sales_demo_video_brief_to_clip_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Runway disabled | 只生成视频 brief/payload |
| 9 | `sales_avatar_pitch_video_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | HeyGen disabled | 只生成数字人口播 payload |
| 10 | `sales_proposal_deck_generator_candidate` | dry-run | `dry_run_only`, `read_only`, `external_action_blocked` | no PPT write | 只输出 slide spec |
| 11 | `sales_call_roleplay_coach_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | text relay only | 只做训练模拟 |
| 12 | `sales_contract_redline_summary_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real contracts | 只用 mock 合同文本 |
| 13 | `sales_crm_next_best_action_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | no CRM write | 只输出 CRM action payload |
| 14 | `marketing_real_poster_banner_agent_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI image relay route only | 不生成图片，只查 route/payload |
| 15 | `marketing_text_overlay_poster_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Ideogram disabled | 只生成 payload |
| 16 | `marketing_brand_asset_generator_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Recraft disabled | 只生成品牌资产 payload |
| 17 | `marketing_short_video_ad_agent_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Veo/Gemini route only | 不生成视频，只查 route/payload |
| 18 | `marketing_product_launch_video_script_to_render_candidate` | dry-run | `dry_run_only`, `read_only`, `external_action_blocked` | no render | 只输出 Remotion render spec |
| 19 | `marketing_ad_creative_batch_generator_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | fal disabled | 只生成批量 payload |
| 20 | `marketing_thumbnail_generator_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Stability disabled | 只生成封面 payload |
| 21 | `marketing_figma_banner_spec_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | no Figma write | 只输出 Figma spec/payload |
| 22 | `marketing_canva_template_brief_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | no Canva create/export | 只输出 Canva brief/payload |
| 23 | `ecommerce_product_main_image_agent_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI image relay route only | 不生成图片，只查 route/payload |
| 24 | `ecommerce_background_replace_agent_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | fal image edit disabled | 不上传素材，只生成 edit payload |
| 25 | `ecommerce_tryon_model_image_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | fal try-on disabled | 不使用真实客户照片 |
| 26 | `ecommerce_product_video_from_image_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Luma route only | 不生成视频，只查 route/payload |
| 27 | `ecommerce_review_to_product_image_prompt_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | text relay only | 只生成商品图 prompt |
| 28 | `ecommerce_shopify_listing_asset_dryrun_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | no Shopify write | 只输出 listing payload |
| 29 | `ecommerce_marketplace_ad_image_variants_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Ideogram disabled | 只生成广告图 payload |
| 30 | `ecommerce_livecommerce_avatar_script_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | HeyGen disabled | 只生成直播口播 payload |
| 31 | `ecommerce_storefront_screenshot_audit_candidate` | dry-run | `dry_run_only`, `read_only`, `external_action_blocked` | no web crawl | 只用授权/本地截图场景 |
| 32 | `ecommerce_inventory_photo_qc_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | vision API disabled | 只生成 mock image payload |
| 33 | `metrics_video_daily_report_candidate` | dry-run | `dry_run_only`, `read_only`, `external_action_blocked` | no render | 只输出 Remotion render spec |
| 34 | `metrics_chart_image_generation_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | no external chart API | 只输出 chart spec |
| 35 | `metrics_anomaly_narrative_audio_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | TTS disabled | 只输出 TTS payload |
| 36 | `metrics_forecast_scenario_simulator_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | text relay only | 非财务建议 |
| 37 | `hr_training_avatar_video_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Synthesia disabled | 只生成培训视频 payload |
| 38 | `hr_resume_interview_avatar_roleplay_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | HeyGen disabled | 不做录用/淘汰建议 |
| 39 | `admin_policy_explainer_video_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Veo/Gemini disabled | 只生成制度视频 payload |
| 40 | `finance_receipt_image_vision_extract_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | vision API disabled | 只生成票据视觉 payload |
| 41 | `admin_document_ocr_to_sop_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no OCR/image upload | 只用 mock OCR text |
| 42 | `finance_invoice_approval_workflow_dryrun_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | no approval write | 只输出审批 payload |
| 43 | `admin_meeting_to_slide_brief_candidate` | dry-run | `dry_run_only`, `read_only`, `external_action_blocked` | no PPT write | 只输出 slide spec |
| 44 | `store_menu_poster_generation_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI image relay route only | 不生成图片，只查 route/payload |
| 45 | `store_digital_signage_video_candidate` | dry-run | `dry_run_only`, `read_only`, `external_action_blocked` | no render | 只输出 Remotion render spec |
