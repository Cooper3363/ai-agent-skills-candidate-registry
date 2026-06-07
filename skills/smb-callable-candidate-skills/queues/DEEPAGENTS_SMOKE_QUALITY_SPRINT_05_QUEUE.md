# DEEPAGENTS_SMOKE_QUALITY_SPRINT_05_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_05_RESULT.md`

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
| `can_mock_smoke` | 16 |
| `can_dry_run_smoke` | 1 |
| `can_route_check` | 3 |
| smoke queue total | 20 |

## Queue

| # | priority | candidate_id | smoke_type | trial_mode | provider_boundary | notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Intercom account | mock conversations + articles -> macro gap report |
| 2 | P0 | `quality_sprint05_helpscout_article_gap_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Help Scout account | mock mailbox rows -> article gaps and handoff notes |
| 3 | P0 | `quality_sprint05_front_inbox_handoff_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Front inbox | mock inbox messages -> handoff summary |
| 4 | P0 | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock campaign metrics -> campaign health |
| 5 | P0 | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real WooCommerce store | mock products -> catalog QC report |
| 6 | P0 | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real BigCommerce store | mock catalog rows -> gap report |
| 7 | P0 | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Google Ads account | mock campaign report -> anomaly brief |
| 8 | P0 | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real GA4 property | mock GA4 rows -> dropoff report |
| 9 | P0 | `quality_sprint05_canva_design_brief_dryrun_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | no Canva write/export/upload | mock campaign brief -> design brief and dry-run export spec |
| 10 | P0 | `quality_sprint05_openai_tts_support_voiceover_payload_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI TTS disabled | mock script -> TTS payload and safety fields |
| 11 | P1 | `quality_sprint05_fal_flux_product_image_payload_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | fal disabled | mock product brief -> image payload |
| 12 | P1 | `quality_sprint05_replicate_background_replace_payload_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Replicate disabled | mock asset metadata -> background replace payload |
| 13 | P1 | `quality_sprint05_figma_design_token_audit_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Figma file read/write | mock figma nodes -> token audit |
| 14 | P1 | `quality_sprint05_asana_project_risk_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Asana tasks | mock tasks -> project risk summary |
| 15 | P1 | `quality_sprint05_trello_board_handoff_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Trello board | mock cards -> handoff summary |
| 16 | P1 | `quality_sprint05_jira_service_sla_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real JSM requests | mock requests -> SLA risk report |
| 17 | P1 | `quality_sprint05_confluence_policy_gap_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Confluence pages | mock pages -> policy gap report |
| 18 | P1 | `quality_sprint05_bamboohr_onboarding_gap_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real BambooHR records | mock onboarding rows -> gap report |
| 19 | P1 | `quality_sprint05_greenhouse_candidate_packet_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Greenhouse records | mock candidate rows -> packet summary and privacy flags |
| 20 | P1 | `quality_sprint05_docusign_contract_status_readonly_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real DocuSign envelopes | mock envelopes -> status summary |

## Excluded From Smoke

| candidate_id | l1_result | reason |
| --- | --- | --- |
| `quality_sprint05_pika_video_ad_payload_route_candidate` | `needs_more_license_info` | API 可用性、pika.rest/provider route、商用条款、费用上限、素材上传/存储和生成内容权属未清 |
| `quality_sprint05_openclaw_ui_ux_pro_max_skill_candidate` | `needs_more_license_info` | 缺 exact repo/subdir/`SKILL.md`/LICENSE/工具脚本和文件生成边界 |
| `quality_sprint05_openagentskills_guizang_ppt_brief_candidate` | `needs_more_license_info` | 缺 exact repo/subdir/LICENSE 和 PPT/HTML artifact 写入/导出边界 |
| `quality_sprint05_open_design_design_brief_child_candidate` | `needs_more_license_info` | 需确认具体 child skill、Apache-2.0 继承、frontmatter/manifest、模板资产和文件写入边界 |
| `quality_sprint05_agency_agents_zh_hr_recruiting_role_component_candidate` | `component_only` | 角色库只作 HR role/component，不进普通 candidate smoke，不进 draft L3 |

