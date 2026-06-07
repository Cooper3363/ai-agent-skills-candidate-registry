# DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_03_RESULT.md`

本队列只包含 L1 放行项：`can_mock_smoke`、`can_dry_run_smoke`、`can_route_check`。

硬边界：

- 不调用真实 API/provider。
- 不安装依赖。
- 不写 key。
- 不读取客户文件。
- 不上传素材。
- 不生成图片、音频、视频或真实文件。
- 不连接真实账号。
- 不写 SaaS/CRM/POS/Sheets/Notion/Slack/HubSpot/业务系统。
- 媒体/provider 类只允许 payload/route-check，不允许真实生成。
- SaaS/API connector 类只允许 mock/read-only/dry-run，不允许真实账号连接。
- DeepAgents workflow 只允许 mock tools。
- 本轮不送正式 L2，不封装，不新增客户正式可调用 Skill。

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 12 |
| `can_dry_run_smoke` | 1 |
| `can_route_check` | 3 |
| smoke queue total | 16 |

## Queue

| # | priority | candidate_id | smoke_type | trial_mode | provider_boundary | notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Shopify connection | mock products -> catalog QC |
| 2 | P0 | `quality_sprint03_openai_image_product_variant_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI Images disabled | product brief -> image payload |
| 3 | P0 | `quality_sprint03_openai_image_poster_layout_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI Images disabled | campaign brief -> poster payload |
| 4 | P0 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Stripe read/write | mock subscriptions -> health summary |
| 5 | P0 | `quality_sprint03_mcp_notion_policy_gap_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Notion workspace | mock pages -> policy gap report |
| 6 | P0 | `quality_sprint03_deepagents_customer_ops_example_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | mock tools only | mock support case -> workflow plan |
| 7 | P0 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Airtable base | mock rows -> inventory alerts |
| 8 | P1 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock channel messages -> FAQ gaps |
| 9 | P1 | `quality_sprint03_deepagents_research_report_example_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no browsing/API | mock company docs -> research brief |
| 10 | P1 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Drive file read/write | mock file metadata -> classifier |
| 11 | P1 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | write_allowed=false | mock contacts -> data health report |
| 12 | P1 | `quality_sprint03_mcp_xero_ar_followup_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Xero read/write | mock invoices -> AR followup plan |
| 13 | P1 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real QuickBooks read/write | mock accounts -> cashflow warning |
| 14 | P1 | `quality_sprint03_openai_tts_training_microcourse_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | OpenAI TTS disabled | training text -> TTS payload |
| 15 | P1 | `quality_sprint03_canva_connect_brand_kit_qc_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Canva read/export/write | mock brand kit JSON -> QC report |
| 16 | P1 | `quality_sprint03_mcp_google_merchant_feed_qc_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Merchant feed read/write | mock feed rows -> QC report |

## Excluded From Smoke

| candidate_id | reason |
| --- | --- |
| `quality_sprint03_openagentskills_drawio_process_candidate` | 需定位具体上游子目录、`SKILL.md`、LICENSE、manifest、drawio 文件输出/写入边界 |
| `quality_sprint03_mdskills_file_processing_excel_candidate` | 需定位具体 spreadsheet/file 子 skill、LICENSE、依赖、文件读取边界 |
| `quality_sprint03_openagentskills_social_card_candidate` | 需定位具体 social card 子 skill、LICENSE、是否调用外部图像 provider、素材上传边界 |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | 需定位具体 data-report child skill、LICENSE、manifest、依赖和业务适配边界 |

