# LICENSE_REVIEW_QUALITY_SPRINT_01_RESULT

回传日期：2026-06-05

## 1. 已完成事项

- 已读取 `QUALITY_SOURCE_SPRINT_01_RESULT.md` 与 `queues/LICENSE_REVIEW_QUALITY_SPRINT_01_QUEUE.md`。
- 已对队列中的 30 个优质适配候选完成 L1 / provider / trial mode 复核。
- 已生成 DeepAgents smoke 队列：`queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_01_QUEUE.md`。
- 本轮未调用真实 API，未安装，未写 key，未生成图片/视频，未读取客户文件。

## 2. 当前问题

- SaaS/MCP/OAuth/CRM/Shopify/Slack/HubSpot/Google/Notion 等连接器类只能 dry-run 或 read-only mock，不得连接真实账号，不得写系统。
- 图片/视频/数字人 provider 类只能做 payload/route-check，不得真实生成；BYOK、费用、素材授权、内容安全和输出审计需后续平台验收。
- `Firecrawl`、`Kling`、`MiniMax/Hailuo`、`open-design poster child skill` 需要补许可证、商用条款或具体子 skill 定位，不进入 smoke 队列。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 候选项级 blocked 为 0。
- 暂缓项 4 个，原因是许可证/商用条款/真实上游或子 skill 定位不足。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 26 个放行项进入 DeepAgents mock/dry-run/route-check smoke。
- 是否让研究窗口优先补齐 4 个暂缓项：`Firecrawl`、`Kling`、`MiniMax/Hailuo`、`open-design poster child skill`。
- 是否把 P0 中 10 个全部作为本 Sprint 优先 smoke 队列，其中 provider 类只允许 route/payload，不允许真实生成。

## 5. 建议下一步

- 测试台读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_01_QUEUE.md`，只执行 mock/dry-run/route-check。
- SaaS/MCP/OAuth 类统一 `write_allowed=false`、`send_allowed=false`、`upload_allowed=false`。
- 媒体 provider 类统一 `BYOK_required`、`provider_api_required`、`real_media_generation_requires_approval`。
- 暂缓项不得送正式 L2，不得封装，不得客户调用。

## 6. 数量汇总

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 14 |
| `can_dry_run_smoke` | 7 |
| `can_route_check` | 5 |
| `can_real_provider_smoke_later` | 0 |
| `component_only` | 0 |
| `needs_more_license_info` | 4 |
| `blocked` | 0 |

| 回传口径 | 数量 |
| --- | ---: |
| 放行 smoke | 26 |
| 暂缓 | 4 |
| blocked | 0 |
| 可直接送正式 L2 | 0 |

## 7. P0 / P1 清单

### P0 放行 smoke

1. `quality_sprint01_shopify_mcp_order_ops_candidate`
2. `quality_sprint01_google_sheets_mcp_report_agent_candidate`
3. `quality_sprint01_notion_ops_knowledge_agent_candidate`
4. `quality_sprint01_slack_support_triage_agent_candidate`
5. `quality_sprint01_hubspot_crm_followup_agent_candidate`
6. `quality_sprint01_openai_agents_customer_ops_workflow_candidate`
7. `quality_sprint01_langgraph_sales_pipeline_workflow_candidate`
8. `quality_sprint01_microsoft_presidio_hr_pii_candidate`
9. `quality_sprint01_product_photo_background_cleanup_candidate`
10. `quality_sprint01_creatomate_template_video_candidate`

### P1 放行 smoke

`quality_sprint01_zapier_actions_smb_connector_candidate`, `quality_sprint01_make_scenario_dryrun_agent_candidate`, `quality_sprint01_llamaindex_kb_refresh_agent_candidate`, `quality_sprint01_pydantic_ai_structured_tool_candidate`, `quality_sprint01_browser_use_store_audit_candidate`, `quality_sprint01_apify_authorized_competitor_snapshot_candidate`, `quality_sprint01_unstructured_contract_invoice_agent_candidate`, `quality_sprint01_docling_office_parser_candidate`, `quality_sprint01_paddleocr_receipt_doc_agent_candidate`, `quality_sprint01_shopify_product_image_bulk_agent_candidate`, `quality_sprint01_shotstack_video_api_candidate`, `quality_sprint01_did_avatar_video_candidate`, `quality_sprint01_canva_design_export_dryrun_candidate`, `quality_sprint01_figma_to_brand_qc_candidate`, `quality_sprint01_agency_douyin_short_video_role_candidate`, `quality_sprint01_agency_xiaohongshu_store_role_candidate`

### P1 暂缓补资料

`quality_sprint01_firecrawl_authorized_page_to_brief_candidate`, `quality_sprint01_kling_video_route_candidate`, `quality_sprint01_minimax_hailuo_video_candidate`, `quality_sprint01_open_design_poster_child_skill_candidate`

## 8. L1 / Provider / Trial Mode 复核表

| # | priority | candidate_id | source / provider | license / terms | platform_fit | relay_fit | dependency_risk | BYOK / cost / rights | dedupe_relation | trial_mode | smoke_allowed | formal_l2 | l1_result |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint01_shopify_mcp_order_ops_candidate` | Shopify API | Shopify API terms；需 OAuth scope | 适合店铺运营 dry-run connector | 文本中转生成 payload；Shopify adapter 后续 | 店铺/订单/库存写入高风险 | BYOK；write_allowed=false；费用按 Shopify/API 计划 | 与 Shopify dry-run 候选相邻 | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 2 | P0 | `quality_sprint01_google_sheets_mcp_report_agent_candidate` | Google Sheets API | Google API terms；需 read-only scope | 适合经营报表 read-only mock | 文本中转分析 mock rows | 表格隐私、OAuth、数据权限 | BYOK；read-only；不读取真实表 | 复用报表 3 件套 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 3 | P0 | `quality_sprint01_notion_ops_knowledge_agent_candidate` | Notion API | Notion API terms；需页面权限控制 | 适合客服知识库整理 | 文本中转可用；Notion adapter 后续 | 知识库隐私、页面读写边界 | BYOK；read-only pages；不写 Notion | 复用 FAQ / KB cleaner | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 4 | P0 | `quality_sprint01_slack_support_triage_agent_candidate` | Slack API | Slack API terms；需 channel privacy / send scope 控制 | 适合客服交接摘要 dry-run | 文本中转可用；Slack adapter 后续 | 频道隐私、消息发送风险 | BYOK；send_allowed=false | 与客服摘要候选相邻 | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 5 | P0 | `quality_sprint01_hubspot_crm_followup_agent_candidate` | HubSpot API | HubSpot developer/API terms；CRM scopes 需控制 | 适合销售跟进 dry-run | 文本中转生成 next action payload | CRM 写入、联系人隐私、OAuth | BYOK；write_allowed=false | 复用 `crm_note_structurer` | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 6 | P0 | `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | openai-agents-python | MIT；产品筛选可接受 | 适合通用 Agent Skill workflow | 可走 OpenAI-compatible 文本 route | tool calling 边界；不得真实调用工具 | 无 BYOK；无真实工具 | 与客服稳交付包互补 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 7 | P0 | `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | LangGraph | MIT；产品筛选可接受 | 适合销售 pipeline 状态机 | 可走 OpenAI-compatible 文本 route | 不得写 CRM；状态机只 mock | 无 BYOK；无真实 CRM | 复用销售候选 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 8 | P0 | `quality_sprint01_microsoft_presidio_hr_pii_candidate` | Microsoft Presidio | MIT；产品筛选可接受 | 适合 HR/客服 PII 脱敏组件 | 可本地规则 + 文本中转辅助 | 中文 PII 规则、HR bias、真实简历隐私 | 无 BYOK；不上传简历 | 复用 `support_pii_redactor` / HR masker | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 9 | P0 | `quality_sprint01_product_photo_background_cleanup_candidate` | PhotoRoom API | 专有 API terms；需商用和上传/存储条款 | 适合商品图处理 provider route | 需 provider adapter；文本中转只生成 payload | 图片上传、素材授权、商标、存储 | BYOK；单图费用上限；不真实上传 | 与背景替换候选相邻 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 10 | P0 | `quality_sprint01_creatomate_template_video_candidate` | Creatomate API | 专有 API terms；需素材、水印、费用条款 | 适合模板视频 JSON dry-run | 文本中转生成 video JSON；provider 后续 | 视频素材授权、输出水印、费用 | BYOK；单次模板渲染费用上限；不生成视频 | 与 Remotion/programmatic video 相邻 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 11 | P1 | `quality_sprint01_zapier_actions_smb_connector_candidate` | Zapier Developer Platform | Zapier app/action terms；scope 需逐项控制 | 适合跨 SaaS automation dry-run | 文本中转生成 action plan | 动作面过宽，真实执行高风险 | BYOK；no action execution | 与 Composio connector 相邻 | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 12 | P1 | `quality_sprint01_make_scenario_dryrun_agent_candidate` | Make.com API | Make API terms；scenario execution 权限需封禁 | 适合流程 spec dry-run | 文本中转生成 scenario spec | 自动化执行、写系统风险 | BYOK；execution_allowed=false | 与 Zapier/Composio 相邻 | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 13 | P1 | `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | LlamaIndex | MIT；产品筛选可接受 | 适合知识库刷新/RAG 组件 | 文本中转可用；mock docs | 框架较重，真实文档隐私 | 无 BYOK；本地/mock docs | 复用 KB cleaner / FAQ | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 14 | P1 | `quality_sprint01_pydantic_ai_structured_tool_candidate` | PydanticAI | 需核正式 SPDX；按产品筛选可先 mock | 适合结构化输出工具 | OpenAI-compatible route 可配置 | provider adapter 和依赖需补测试 | 无真实 provider；仅 mock schema | 与结构化抽取候选相邻 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 15 | P1 | `quality_sprint01_browser_use_store_audit_candidate` | browser-use | MIT；产品筛选可接受 | 适合授权页面本地审计 | 文本中转分析；browser 本地后续 | 网页 ToS、登录、抓取边界 | BYOK 可选；只 local HTML | 与 screenshot audit 相邻 | `dry_run_only`, `read_only`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 16 | P1 | `quality_sprint01_apify_authorized_competitor_snapshot_candidate` | Crawlee / Apify | Apache-2.0；Apify Cloud/代理另核 | 只适合用户提供快照 mock | 文本中转分析 HTML snapshot | ToS/robots/抓取风险 | BYOK optional；不抓取真实网页 | 与 competitor snapshot 重复，作为替代来源 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 17 | P1 | `quality_sprint01_unstructured_contract_invoice_agent_candidate` | Unstructured | Apache-2.0；产品筛选可接受 | 适合文档解析组件 | 文本中转摘要；mock doc text | 文件隐私，非法律/审计结论 | 无 BYOK；不读真实文件 | 与合同/票据候选相邻 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 18 | P1 | `quality_sprint01_docling_office_parser_candidate` | IBM Docling | MIT/Apache 需以仓库 LICENSE 为准；产品筛选先 mock | 适合本地文档解析候选 | 文本中转处理 extracted text | 依赖体积、文件隐私 | 无 BYOK；不处理真实文件 | 与 OCR/PDF 候选相邻 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 19 | P1 | `quality_sprint01_paddleocr_receipt_doc_agent_candidate` | PaddleOCR | Apache-2.0；模型权重需锁定官方可商用版本 | 适合 OCR 后文本抽取 | OCR 后文本可走中转站 | 模型权重、图片隐私、票据财税边界 | 无 BYOK；不上传图片 | 与 Next50 OCR 候选相邻 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 20 | P1 | `quality_sprint01_firecrawl_authorized_page_to_brief_candidate` | Firecrawl | GitHub/服务条款需补；可能存在强 copyleft / SaaS terms 风险 | 来源价值明确但不宜直接放行 | 文本中转可分析 provided HTML | Web extraction、robots、BYOK、服务条款 | BYOK optional；需补条款 | 与 lead research 相邻 | `mock_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 21 | P1 | `quality_sprint01_shopify_product_image_bulk_agent_candidate` | Shopify + image route | Shopify API terms + image provider terms 双重约束 | 适合商品批量 payload dry-run | 文本 + image route payload | 店铺写入、图片生成、素材授权 | BYOK；write/upload blocked；费用上限 | 与 Shopify/media 候选相邻 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 22 | P1 | `quality_sprint01_shotstack_video_api_candidate` | Shotstack API | 专有 API terms；素材上传/费用需核 | 适合视频 render payload | 文本中转生成 render spec | 素材上传、费用、输出版权 | BYOK；不真实渲染 | 与 Remotion/Runway 相邻 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 23 | P1 | `quality_sprint01_did_avatar_video_candidate` | D-ID API | 专有 API terms；头像/声音授权需核 | 适合数字人 payload | 文本中转生成脚本；D-ID provider 后续 | 真人素材、肖像/声音、发布风险 | BYOK；只 stock/授权 avatar | 与 HeyGen/Synthesia 相邻 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 24 | P1 | `quality_sprint01_kling_video_route_candidate` | Kling provider | API 可用性、商用条款、费用和地区条款需补 | 市场价值高但条款未清 | 文本中转只能生成 prompt | provider/API 与商用条款不清 | BYOK 待定 | 与 Veo/Luma 相邻 | `dry_run_only`, `provider_api_required`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 25 | P1 | `quality_sprint01_minimax_hailuo_video_candidate` | MiniMax / Hailuo | API 文档、商用条款、费用和内容政策需补 | 中文视频价值高但条款未清 | 文本中转只能生成 prompt | provider/API 与商用条款不清 | BYOK 待定 | 与中文视频 provider 相邻 | `dry_run_only`, `provider_api_required`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 26 | P1 | `quality_sprint01_canva_design_export_dryrun_candidate` | Canva Developer Platform | Canva terms；OAuth/export/write 需封禁 | 适合设计 payload dry-run | 文本中转生成 design spec | 导出/写入/素材版权 | BYOK；no export/no write | 与 Canva brief 候选相邻 | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 27 | P1 | `quality_sprint01_figma_to_brand_qc_candidate` | Figma API | Figma terms；read-only scope | 适合品牌 QC read-only mock | 文本中转分析 mock frame JSON | 品牌素材隐私、文件权限 | BYOK；read-only | 与 design system candidate 相邻 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 28 | P1 | `quality_sprint01_open_design_poster_child_skill_candidate` | open-design child skill | Apache-2.0 仓库；具体子 skill/manifest 未定位 | 需定位 child skill 后再评估 | 文本+图像 route 需看子 skill | 聚合仓库、写文件/API/导出风险 | BYOK 待定 | 与 open-design source pack 相邻 | `dry_run_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 29 | P1 | `quality_sprint01_agency_douyin_short_video_role_candidate` | agency-agents-zh role library | MIT；上游版权边界已按角色库口径复核 | 适合 role smoke，不是可调用 Skill | 文本中转可用 | 角色 prompt 非 Skill；不得发布抖音内容 | 无 BYOK；不发布 | 与 agency Top60 角色相邻 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 30 | P1 | `quality_sprint01_agency_xiaohongshu_store_role_candidate` | agency-agents-zh role library | MIT；上游版权边界已按角色库口径复核 | 适合 role smoke，不是可调用 Skill | 文本中转可用 | 小红书平台规则、不得发布 | 无 BYOK；不发布 | 与 agency Top60 角色相邻 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
