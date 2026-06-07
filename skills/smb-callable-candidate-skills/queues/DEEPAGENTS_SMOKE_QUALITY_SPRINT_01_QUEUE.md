# DEEPAGENTS_SMOKE_QUALITY_SPRINT_01_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_01_RESULT.md`

本队列只包含 L1 放行项：`can_mock_smoke`、`can_dry_run_smoke`、`can_route_check`。

硬边界：

- 不调用真实 API。
- 不安装。
- 不写 key。
- 不生成图片/视频/音频。
- 不读取客户文件。
- 不连接真实账号。
- 不写 CRM/Shopify/Slack/HubSpot/Google/Notion/Figma/Canva。
- 媒体 provider 只允许 payload/route-check，不允许真实生成。
- 角色库只允许 role smoke，不得当作可调用 Skill。
- 本轮不送正式 L2。

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 14 |
| `can_dry_run_smoke` | 7 |
| `can_route_check` | 5 |
| smoke queue total | 26 |

## Queue

| # | priority | candidate_id | smoke_type | trial_mode | provider_boundary | notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint01_shopify_mcp_order_ops_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | no Shopify write | mock order/product JSON -> dry-run payload |
| 2 | P0 | `quality_sprint01_google_sheets_mcp_report_agent_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no real Sheets read | mock sheet rows -> weekly report |
| 3 | P0 | `quality_sprint01_notion_ops_knowledge_agent_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | no Notion write/read | mock pages -> FAQ gap report |
| 4 | P0 | `quality_sprint01_slack_support_triage_agent_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | send_allowed=false | mock channel messages -> handoff summary |
| 5 | P0 | `quality_sprint01_hubspot_crm_followup_agent_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | write_allowed=false | mock deals -> next action payload |
| 6 | P0 | `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real tools | mock support case -> tool plan |
| 7 | P0 | `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no CRM write | mock pipeline -> next-stage checklist |
| 8 | P0 | `quality_sprint01_microsoft_presidio_hr_pii_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real resume upload | mock resume -> redacted fields |
| 9 | P0 | `quality_sprint01_product_photo_background_cleanup_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | PhotoRoom disabled | mock image metadata -> edit payload |
| 10 | P0 | `quality_sprint01_creatomate_template_video_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Creatomate disabled | mock campaign -> video JSON |
| 11 | P1 | `quality_sprint01_zapier_actions_smb_connector_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | no action execution | mock automation plan |
| 12 | P1 | `quality_sprint01_make_scenario_dryrun_agent_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | no scenario execution | mock reimbursement workflow spec |
| 13 | P1 | `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | mock docs only | docs -> stale/gap report |
| 14 | P1 | `quality_sprint01_pydantic_ai_structured_tool_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real provider | mock invoice/form -> typed schema |
| 15 | P1 | `quality_sprint01_browser_use_store_audit_candidate` | dry-run | `dry_run_only`, `read_only`, `external_action_blocked` | local authorized page only | local HTML page audit |
| 16 | P1 | `quality_sprint01_apify_authorized_competitor_snapshot_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no crawl | mock HTML -> competitor summary |
| 17 | P1 | `quality_sprint01_unstructured_contract_invoice_agent_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no real documents | mock doc -> sections/risk flags |
| 18 | P1 | `quality_sprint01_docling_office_parser_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | mock extracted text only | extracted text -> SOP |
| 19 | P1 | `quality_sprint01_paddleocr_receipt_doc_agent_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | no image upload | mock OCR text -> invoice fields |
| 20 | P1 | `quality_sprint01_shopify_product_image_bulk_agent_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | no Shopify write / no image generation | mock products -> media/listing payload |
| 21 | P1 | `quality_sprint01_shotstack_video_api_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | Shotstack disabled | storyboard -> render payload |
| 22 | P1 | `quality_sprint01_did_avatar_video_candidate` | route-check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | D-ID disabled | mock script -> avatar payload |
| 23 | P1 | `quality_sprint01_canva_design_export_dryrun_candidate` | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | no export/no write | mock design -> Canva payload |
| 24 | P1 | `quality_sprint01_figma_to_brand_qc_candidate` | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | Figma read-only mock | mock frame JSON -> brand QC |
| 25 | P1 | `quality_sprint01_agency_douyin_short_video_role_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | role smoke only | mock business -> Douyin plan |
| 26 | P1 | `quality_sprint01_agency_xiaohongshu_store_role_candidate` | mock | `mock_only`, `read_only`, `external_action_blocked` | role smoke only | mock store -> Xiaohongshu note plan |

