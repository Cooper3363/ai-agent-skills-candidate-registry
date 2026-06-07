# DEEPAGENTS_SMOKE_QUALITY_SPRINT_07_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_07_RESULT.md`

本队列只包含 L1 放行项：`allow_smoke`。

硬边界：

- 不安装依赖。
- 不调用真实 API/provider。
- 不生成图片、视频、音频、PPT、PDF、HTML 或真实文件。
- 不读取、打印或写入 key。
- 不访问真实账号。
- 不读取客户文件。
- 不上传素材。
- SaaS/API 只允许 mock/read-only，不写系统、不发送、不分派、不改状态。
- 媒体/provider 只允许 route/config/payload check，不真实生成。
- 本轮不送正式 L2，不封装，不客户调用。

## Summary

| 类型 | 数量 |
| --- | ---: |
| SaaS/API `read_only_mock` | 11 |
| 媒体/provider `route_check` / `dry_run_payload_only` | 5 |
| smoke queue total | 16 |

## Queue

| # | priority | candidate_id | smoke_type | trial_mode | boundary | smoke_focus |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint07_intercom_article_decay_readonly_candidate` | mock | `read_only_mock` | no real Intercom account | mock articles/conversations -> decay/gap report |
| 2 | P0 | `quality_sprint07_workable_interview_question_bank_candidate` | mock | `read_only_mock` | no real Workable account | mock JD/candidate profile -> question bank |
| 3 | P0 | `quality_sprint07_shopify_return_product_quality_candidate` | mock | `read_only_mock` | no real Shopify store | mock returns/products -> quality issue clusters |
| 4 | P0 | `quality_sprint07_metabase_executive_digest_candidate` | mock | `read_only_mock` | no real Metabase/DB | mock dashboard cards -> executive digest |
| 5 | P0 | `quality_sprint07_openai_image_review_to_product_scene_candidate` | route-check | `dry_run_payload_only` | OpenAI Images disabled | review themes + product metadata -> image payload |
| 6 | P0 | `quality_sprint07_docusign_missing_signature_readonly_candidate` | mock | `read_only_mock` | no real DocuSign account | mock envelopes -> missing signature report |
| 7 | P0 | `quality_sprint07_mailchimp_deliverability_qc_candidate` | mock | `read_only_mock` | send_allowed=false | mock campaign reports -> deliverability QC |
| 8 | P1 | `quality_sprint07_helpscout_saved_reply_gap_candidate` | mock | `read_only_mock` | no real Help Scout account | mock conversations/saved replies -> gap report |
| 9 | P1 | `quality_sprint07_front_account_handoff_candidate` | mock | `read_only_mock` | no real Front account | mock account conversations -> handoff brief |
| 10 | P1 | `quality_sprint07_greenhouse_offer_risk_readonly_candidate` | mock | `read_only_mock` | no hiring decision | mock offers/candidates -> risk checklist |
| 11 | P1 | `quality_sprint07_amplitude_activation_dropoff_candidate` | mock | `read_only_mock` | no real Amplitude project | mock activation metrics -> dropoff report |
| 12 | P1 | `quality_sprint07_hubspot_lead_source_quality_candidate` | mock | `read_only_mock` | no CRM write | mock contacts/deals -> source quality report |
| 13 | P1 | `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | route-check | `dry_run_payload_only` | OpenAI TTS disabled | roleplay script -> TTS payload JSON |
| 14 | P1 | `quality_sprint07_runway_customer_story_clip_candidate` | route-check | `dry_run_payload_only` | Runway disabled | customer story brief -> video payload |
| 15 | P1 | `quality_sprint07_fal_packshot_to_lifestyle_candidate` | route-check | `route_check` | fal disabled | product metadata -> route payload only |
| 16 | P1 | `quality_sprint07_heygen_new_employee_avatar_candidate` | route-check | `dry_run_payload_only` | HeyGen disabled | onboarding script -> avatar payload |

## Excluded From Smoke

| candidate_id | L1 结论 | reason |
| --- | --- | --- |
| `quality_sprint07_last30days_market_signal_brief_candidate` | `needs_more_license_info` | 需核 LICENSE、脚本、外网搜索/抓取源、API key 和保存目录 |
| `quality_sprint07_baoyu_wechat_summary_candidate` | `needs_more_license_info` | 需核 LICENSE、wx-cli、微信账号权限、群聊隐私和本地历史数据存储 |
| `quality_sprint07_graphify_kb_structure_candidate` | `needs_more_license_info` | 缺 concrete repo、LICENSE、subdir、脚本和文件写入/clone 边界 |
| `quality_sprint07_fireworks_tech_graph_process_candidate` | `needs_more_license_info` | 缺 concrete repo、LICENSE、diagram output 和文件写入/导出边界 |
| `quality_sprint07_guizang_ppt_sales_training_candidate` | `needs_more_license_info` | 需确认 LICENSE、assets/references、HTML/PPT 生成、截图/导出边界 |
| `quality_sprint07_agency_sales_ops_forecast_role_candidate` | `component_only` | role asset，不进普通 candidate smoke |
| `quality_sprint07_agency_finance_ap_ar_clerk_role_candidate` | `component_only` | role asset，不进普通 candidate smoke |
| `quality_sprint07_promptfoo_recruiting_fairness_regression_candidate` | `component_only` | eval component，不进普通 candidate smoke |
| `quality_sprint07_instructor_refund_case_schema_candidate` | `component_only` | schema component，不进普通 candidate smoke |

