# QUALITY_SOURCE_SPRINT_01 许可证复核队列

更新日期: 2026-06-05

## 来源

- 研究文件: `../QUALITY_SOURCE_SPRINT_01_RESULT.md`
- 优质线索: 80
- 本队列只收 30 个优先入库候选。
- 不送 L2，不封装，不客户调用。

## 队列摘要

| 分类 | 数量 |
| --- | ---: |
| P0 | 10 |
| P1 | 20 |
| 媒体类 | 11 |
| MCP / API / SaaS connector 类 | 11 |
| Agent workflow / framework 类 | 6 |
| 文档 / OCR / PII 类 | 5 |

## 30 个优先入库候选复核表

| priority | candidate_id | source_url | source_type | quality_score | recommended_state | trial_mode | media | real_generation | BYOK | license_review_focus | route / provider focus | test_smoke_focus |
| --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | `quality_sprint01_shopify_mcp_order_ops_candidate` | https://shopify.dev/docs/api | MCP / SaaS connector | 88 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | Shopify API 条款、OAuth scope、商用、店铺写入边界 | `write_allowed=false`, `upload_allowed=false` | mock order/product JSON -> dry-run payload |
| P0 | `quality_sprint01_google_sheets_mcp_report_agent_candidate` | https://developers.google.com/sheets/api | MCP / SaaS connector | 87 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Google Sheets API 条款、read-only scope、数据隐私 | only read/mock rows | mock sheet rows -> 周报和异常 |
| P0 | `quality_sprint01_notion_ops_knowledge_agent_candidate` | https://developers.notion.com/ | MCP / SaaS connector | 86 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Notion API 条款、页面权限、知识库隐私 | read-only pages | mock pages -> FAQ 缺口 |
| P0 | `quality_sprint01_slack_support_triage_agent_candidate` | https://api.slack.com/ | MCP / SaaS connector | 85 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | Slack API 条款、频道隐私、发送权限 | `send_allowed=false` | mock messages -> 客服交接摘要 |
| P0 | `quality_sprint01_hubspot_crm_followup_agent_candidate` | https://developers.hubspot.com/ | CRM API connector | 85 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | HubSpot API 条款、CRM scopes、联系人隐私 | `write_allowed=false` | mock deals -> next action |
| P0 | `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | https://github.com/openai/openai-agents-python | Agent SDK | 84 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | SDK 许可证、工具调用边界 | no real tools | mock support case -> tool plan |
| P0 | `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | https://github.com/langchain-ai/langgraph | Agent workflow | 84 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | LangGraph 许可证、状态机依赖 | no CRM write | mock pipeline -> next-stage checklist |
| P0 | `quality_sprint01_microsoft_presidio_hr_pii_candidate` | https://github.com/microsoft/presidio | PII tool | 86 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | Presidio 许可证、中文 PII 规则、HR 材料边界 | local/mock only | mock resume -> redacted fields |
| P0 | `quality_sprint01_product_photo_background_cleanup_candidate` | https://www.photoroom.com/api | Image edit API | 82 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | PhotoRoom 条款、素材上传/存储、商用图片权限 | provider key / relay if available | mock image metadata -> edit payload |
| P0 | `quality_sprint01_creatomate_template_video_candidate` | https://creatomate.com/docs | Video API | 82 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Creatomate 条款、素材授权、水印/费用 | provider key | mock campaign -> video JSON |
| P1 | `quality_sprint01_zapier_actions_smb_connector_candidate` | https://zapier.com/app/developer | SaaS connector | 83 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | Zapier app/action terms、scope、真实执行边界 | no action execution | mock automation plan |
| P1 | `quality_sprint01_make_scenario_dryrun_agent_candidate` | https://www.make.com/en/api-documentation | SaaS connector | 82 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | Make API 条款、scenario 执行权限 | no execution | mock reimbursement scenario |
| P1 | `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | https://github.com/run-llama/llama_index | RAG framework | 83 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | LlamaIndex 许可证、依赖、RAG 本地化 | local/mock docs | docs -> gap report |
| P1 | `quality_sprint01_pydantic_ai_structured_tool_candidate` | https://github.com/pydantic/pydantic-ai | Agent framework | 82 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | PydanticAI 许可证、provider adapter | OpenAI-compatible route | invoice/form -> typed schema |
| P1 | `quality_sprint01_browser_use_store_audit_candidate` | https://github.com/browser-use/browser-use | Browser agent | 80 | `needs_license_review` | `local_authorized_page_only` | 否 | 否 | 否 | Browser Use 许可证、网页 ToS、登录/抓取边界 | local HTML only | local store page audit |
| P1 | `quality_sprint01_apify_authorized_competitor_snapshot_candidate` | https://github.com/apify/crawlee | Web automation | 79 | `needs_license_review` | `mock_snapshot_only` | 否 | 否 | 可选 | Crawlee 许可证、robots/ToS、竞品页面来源 | user-provided snapshot only | mock HTML -> competitor summary |
| P1 | `quality_sprint01_unstructured_contract_invoice_agent_candidate` | https://github.com/Unstructured-IO/unstructured | Document parser | 81 | `needs_license_review` | `mock_doc_text_only` | 否 | 否 | 否 | Unstructured 许可证、文件隐私、非法律/审计结论 | local/mock doc text | doc -> sections/risk flags |
| P1 | `quality_sprint01_docling_office_parser_candidate` | https://github.com/docling-project/docling | Document parser | 80 | `needs_license_review` | `mock_file_text_only` | 否 | 否 | 否 | Docling 许可证、依赖体积、文件处理 | local/mock extracted text | extracted text -> SOP |
| P1 | `quality_sprint01_paddleocr_receipt_doc_agent_candidate` | https://github.com/PaddlePaddle/PaddleOCR | OCR tool | 80 | `needs_license_review` | `mock_ocr_text_only` | 否 | 否 | 否 | PaddleOCR 许可证、模型权重、图片存储 | no real image upload | mock OCR text -> invoice fields |
| P1 | `quality_sprint01_firecrawl_authorized_page_to_brief_candidate` | https://github.com/mendableai/firecrawl | Web extraction | 78 | `needs_license_review` | `mock_html_only` | 否 | 否 | 可选 | Firecrawl 许可证/服务条款、robots、BYOK | provided HTML first | HTML -> lead brief |
| P1 | `quality_sprint01_shopify_product_image_bulk_agent_candidate` | https://shopify.dev/docs/api | SaaS + media route | 81 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Shopify scopes、图片 provider 条款、write block | no upload/no write | mock products -> media/listing payload |
| P1 | `quality_sprint01_shotstack_video_api_candidate` | https://shotstack.io/docs/ | Video API | 79 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Shotstack 条款、素材上传、费用 | provider key | storyboard -> render payload |
| P1 | `quality_sprint01_did_avatar_video_candidate` | https://docs.d-id.com/ | Avatar API | 80 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | D-ID 条款、肖像/声音授权、真人素材禁止 | provider key | script -> avatar payload |
| P1 | `quality_sprint01_kling_video_route_candidate` | https://app.klingai.com/ | Video provider | 76 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Kling API 可用性、商用条款、费用、素材授权 | provider adapter | prompt -> payload |
| P1 | `quality_sprint01_minimax_hailuo_video_candidate` | https://www.minimax.io/ | Video provider | 77 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | MiniMax/Hailuo API、内容政策、商用、费用 | provider adapter | Chinese prompt -> payload |
| P1 | `quality_sprint01_canva_design_export_dryrun_candidate` | https://www.canva.dev/docs/ | Design SaaS | 80 | `needs_license_review` | `dry_run_payload_only` | 是 | 否 | 是 | Canva 条款、OAuth、导出/写入禁止 | no export/no write | mock design -> Canva payload |
| P1 | `quality_sprint01_figma_to_brand_qc_candidate` | https://www.figma.com/developers/api | Design SaaS | 79 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Figma scopes、read-only、品牌素材隐私 | read-only frame JSON | mock frame -> brand QC |
| P1 | `quality_sprint01_open_design_poster_child_skill_candidate` | https://github.com/nexu-io/open-design | OpenClaw-like skill pack | 78 | `needs_license_review` | `dry_run_metadata_only` | 是 | 可能 | 可能 | open-design 子 skill、LICENSE、是否写文件/调用 API | child skill mapping | brief -> child payload |
| P1 | `quality_sprint01_agency_douyin_short_video_role_candidate` | https://github.com/jnMetaCode/agency-agents-zh | Agent role library | 78 | `needs_license_review` | `role_smoke_mock` | 否 | 否 | 否 | MIT、上游版权、平台发布规则 | role only | mock business -> Douyin plan |
| P1 | `quality_sprint01_agency_xiaohongshu_store_role_candidate` | https://github.com/jnMetaCode/agency-agents-zh | Agent role library | 79 | `needs_license_review` | `role_smoke_mock` | 否 | 否 | 否 | MIT、上游版权、小红书平台规则 | role only | mock store -> note plan |

## P0 / P1 处理建议

- P0 10 个优先做 L1，目标是快速筛出可进入 mock/dry-run smoke 的候选。
- P1 20 个保留为高质量候选，但先解决 provider/OAuth/文件读取/媒体素材授权等风险。
- 所有媒体类候选在 L1 前不得真实生成。
- 所有 SaaS/MCP connector 在 L1 前不得连接真实账号或写系统。

## 禁止动作

- 不真实调用 API。
- 不生成图片、视频、音频或真实文件。
- 不写 API key。
- 不写稳交付库。
- 不把 market lead 宣称为可调用 Skill。
