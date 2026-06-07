# DEEPAGENTS_SMOKE_QUALITY_SPRINT_01_RESULT

回传日期：2026-06-05

本轮性质：DeepAgents candidate-level metadata/mock/dry-run/route-check smoke。  
结论边界：smoke passed 只代表候选库可继续试跑，不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_01_RESULT.md` 与 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_01_QUEUE.md`。
- 已确认 Quality Sprint 01 共 26 个 L1/trial mode 放行候选进入 smoke 队列。
- 已对 26 个候选完成 candidate-level metadata/mock/dry-run/route-check smoke 设计与判定。
- 已为每个候选记录中文 mock/dry-run/route-check 场景、callable 表达、模型通道路由适配、输入输出字段、权限边界、人工复核触发、禁止动作和 smoke_status。
- 已从 passed 候选中筛选 Top10，生成正式 L2 simulated 队列建议。

## 2. 当前问题

- SaaS/MCP/OAuth/API 类候选只完成 dry-run 或 mock smoke，未连接真实账号，未写入业务系统。
- 媒体 provider 类候选只完成 route/config/payload check，未真实生成图片、视频、音频或 PDF。
- 角色库类候选只能证明岗位建议输出稳定，不应作为客户正式 callable Skill 直接送 L3。
- 4 个 needs_more_license_info 候选未进入本轮 smoke：`quality_sprint01_firecrawl_authorized_page_to_brief_candidate`、`quality_sprint01_kling_video_route_candidate`、`quality_sprint01_minimax_hailuo_video_candidate`、`quality_sprint01_open_design_poster_child_skill_candidate`。

## 3. 阻塞原因

- 本轮无权限阻塞。
- 本轮无工具阻塞。
- 本轮未触发外部网络、真实 provider、真实账号、真实文件、发送、上传或写业务系统动作。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Top10 进入正式 L2 simulated，每个候选至少 3 个中文业务 mock/dry-run 用例。
- 是否另行安排媒体 provider 类候选的真实 provider smoke 前置 route/env/key 审批流程。
- 是否让研究/许可证窗口继续补齐 4 个暂缓项的许可证、商用条款、provider 边界或具体 child skill 定位。

## 5. 建议下一步

- 将 Top10 文本/结构化/dry-run 类候选送正式 L2 simulated。
- 暂不将媒体 route-check 候选写入正式 L2 通过或封装队列；后续如需推进，应先走真实 provider smoke 审批。
- 角色库候选继续保留为 role smoke 资产，不纳入客户正式 callable Skill。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 26 |
| `failed` | 0 |
| `needs_fix` | 0 |
| `blocked` | 0 |

| smoke_type | 数量 |
| --- | ---: |
| `can_mock_smoke` | 14 |
| `can_dry_run_smoke` | 7 |
| `can_route_check` | 5 |

## 7. Top10 正式 L2 队列建议

| 排名 | candidate_id | 推荐原因 | 正式 L2 重点 |
| ---: | --- | --- | --- |
| 1 | `quality_sprint01_google_sheets_mcp_report_agent_candidate` | 经营报表高频、mock rows 可稳定测试、真实动作风险低 | 表格行结构化、指标摘要、异常字段、read-only 边界 |
| 2 | `quality_sprint01_notion_ops_knowledge_agent_candidate` | 客服/运营知识库整理高频，可复用 KB cleaner/FAQ 能力 | mock page 到 FAQ gap、引用来源、Notion read/write 边界 |
| 3 | `quality_sprint01_slack_support_triage_agent_candidate` | 客服交接价值明确，dry-run 可验证不发送 | 投诉/退款/安全问题分流、交接摘要、send_allowed=false |
| 4 | `quality_sprint01_hubspot_crm_followup_agent_candidate` | 销售跟进高价值，dry-run payload 可控 | 线索摘要、下一步动作、CRM write_allowed=false |
| 5 | `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | 通用 agent workflow 底座适配价值高 | 工具计划、边界检查、人工复核路由 |
| 6 | `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | 销售 pipeline 状态机适合结构化 L2 | 阶段判断、风险节点、下一步清单、CRM 不写入 |
| 7 | `quality_sprint01_microsoft_presidio_hr_pii_candidate` | HR/客服脱敏低风险高频，可复用规则增强经验 | 中文简历 PII 识别、脱敏稳定性、隐私边界 |
| 8 | `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | 知识库刷新/缺口识别适合组件化 | mock docs 新旧对比、过期条款、缺口建议 |
| 9 | `quality_sprint01_pydantic_ai_structured_tool_candidate` | 结构化输出底座价值高，可服务多包 schema 稳定性 | 输入校验、类型字段、错误回退、schema 稳定 |
| 10 | `quality_sprint01_unstructured_contract_invoice_agent_candidate` | 合同/票据文本解析适合 mock L2，不做法律/审计结论 | mock 文档分段、字段抽取、风险标签、人工复核 |

## 8. 26 个候选 smoke 明细

| # | candidate_id | smoke_type | 中文 smoke 场景 | callable_fit | model_route_fit | expected_inputs | expected_outputs | permission_boundary | manual_review_triggers | blocked_actions | deepagents_smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint01_shopify_mcp_order_ops_candidate` | dry-run | 模拟店铺订单缺货，生成订单核查与 Shopify 操作草案 | 可表达为 dry-run connector agent | 文本中转生成 payload，不连 Shopify | `mock_order_json`, `mock_inventory`, `operation_intent` | `order_summary`, `proposed_actions`, `dry_run_payload`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不读真实店铺，不写 Shopify，不改库存 | 退款、赔偿、改库存、客户通知 | Shopify 写入、库存修改、订单取消、通知发送 | passed |
| 2 | `quality_sprint01_google_sheets_mcp_report_agent_candidate` | mock | 模拟门店日报表 rows，生成周报摘要与异常字段 | 可表达为 read-only report agent | mock rows 走文本/结构化模型路由 | `mock_sheet_rows`, `metric_schema`, `date_range` | `summary`, `metric_changes`, `anomalies`, `source_rows`, `manual_review_required` | 不连接 Google，不读取真实 Sheets | 缺失关键字段、异常波动、口径冲突 | 真实 Sheets 读取、写入、分享权限修改 | passed |
| 3 | `quality_sprint01_notion_ops_knowledge_agent_candidate` | mock | 模拟 Notion 知识库页面，输出 FAQ 缺口和过期条款 | 可表达为 KB整理 agent | mock pages 走文本/结构化模型路由 | `mock_pages`, `kb_goal`, `policy_version` | `page_summary`, `faq_gaps`, `stale_items`, `source_notes` | 不连接 Notion，不读写真实页面 | 政策冲突、客户承诺、无法引用来源 | Notion 读取、写入、发布、权限变更 | passed |
| 4 | `quality_sprint01_slack_support_triage_agent_candidate` | dry-run | 模拟客服频道消息，生成投诉升级交接摘要 | 可表达为 Slack triage dry-run agent | 文本中转生成交接 payload | `mock_channel_messages`, `policy_snippets`, `triage_rules` | `handoff_summary`, `risk_tags`, `suggested_channel`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Slack，不发消息，不读真实频道 | 投诉、退款、安全、PII、舆情 | Slack 发送、拉人、建频道、改消息 | passed |
| 5 | `quality_sprint01_hubspot_crm_followup_agent_candidate` | dry-run | 模拟 CRM 线索备注，生成下一步跟进 payload | 可表达为 CRM follow-up dry-run agent | 文本中转生成 CRM payload | `mock_deal`, `mock_notes`, `stage_rules` | `lead_summary`, `next_action`, `crm_payload`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 HubSpot，不写联系人/交易 | 高价值客户、价格争议、个人信息、承诺折扣 | CRM 写入、邮件发送、任务创建 | passed |
| 6 | `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | mock | 模拟客户运营工单，输出 agent 工具调用计划和安全边界 | 可表达为通用 workflow candidate | OpenAI-compatible 文本 route，可禁用真实工具 | `mock_case`, `available_mock_tools`, `policy_snippets` | `workflow_plan`, `tool_plan`, `blocked_steps`, `manual_review_required` | 不调用真实工具，不写系统 | 工具越权、退款/赔偿、账号安全、低置信 | 真实工具调用、外部 API、业务写入 | passed |
| 7 | `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | mock | 模拟销售 pipeline 阶段变化，输出下一阶段清单 | 可表达为状态机 workflow candidate | 文本模型生成状态转移与检查项 | `mock_opportunity`, `pipeline_rules`, `recent_events` | `current_stage`, `next_stage`, `required_checks`, `risk_flags` | 不写 CRM，不自动推进阶段 | 金额异常、合同条款、客户流失风险 | CRM 阶段更新、任务写入、报价发送 | passed |
| 8 | `quality_sprint01_microsoft_presidio_hr_pii_candidate` | mock | 模拟中文简历文本，输出脱敏结果和 PII 类型 | 可表达为 HR PII redaction component/agent | 本地规则 + 文本中转辅助，不上传简历 | `mock_resume_text`, `pii_rules`, `masking_policy` | `redacted_text`, `entities`, `risk_flags`, `manual_review_required` | 不读取真实简历，不上传外部服务 | 身份证、手机号、住址、薪资、敏感经历 | 存储未脱敏 PII、外传简历、自动筛人 | passed |
| 9 | `quality_sprint01_product_photo_background_cleanup_candidate` | route-check | 模拟商品图元数据，生成背景清理 provider payload | 可表达为 image route candidate，需真实 provider 审批后再定 | 只检查 route/config/payload，不调用 PhotoRoom | `mock_image_metadata`, `edit_goal`, `asset_policy`, `cost_limit` | `provider_payload`, `output_path_schema`, `cost_cap`, `content_safety`, `real_media_generation_requires_approval=true` | 不上传素材，不生成图片，不写 key | 商标、版权、人物肖像、费用超限、违规商品 | provider 调用、素材上传、图片生成、发布 | passed |
| 10 | `quality_sprint01_creatomate_template_video_candidate` | route-check | 模拟促销活动素材说明，生成模板视频 JSON | 可表达为 video render route candidate，需真实 provider 审批后再定 | 只检查 video payload，不调用 Creatomate | `mock_campaign`, `template_id`, `asset_policy`, `cost_limit` | `render_spec`, `scene_list`, `asset_requirements`, `real_media_generation_requires_approval=true` | 不上传素材，不渲染视频，不写 key | 素材授权、水印、费用、平台违规 | provider 调用、视频渲染、上传发布 | passed |
| 11 | `quality_sprint01_zapier_actions_smb_connector_candidate` | dry-run | 模拟售后自动化流程，生成 Zapier action plan | 可表达为 automation dry-run agent | 文本中转生成 action spec | `mock_trigger`, `mock_app_actions`, `business_rule` | `automation_plan`, `dry_run_steps`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Zapier，不执行 action | 会发送客户消息、写 CRM、创建付款/退款 | action 执行、发送、写系统、OAuth 连接 | passed |
| 12 | `quality_sprint01_make_scenario_dryrun_agent_candidate` | dry-run | 模拟报销审批流程，生成 Make scenario spec | 可表达为 scenario dry-run agent | 文本中转生成 scenario spec | `mock_process`, `mock_modules`, `approval_rules` | `scenario_spec`, `execution_plan`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Make，不执行 scenario | 审批、付款、通知、写表 | scenario 执行、Webhook 调用、业务写入 | passed |
| 13 | `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | mock | 模拟知识库旧文档和新增政策，输出刷新建议 | 可表达为 KB refresh component/agent | mock docs 走文本/结构化模型路由 | `mock_old_docs`, `mock_new_docs`, `refresh_policy` | `stale_docs`, `new_faq_candidates`, `conflicts`, `source_notes` | 不读取真实文档，不接向量库 | 规则冲突、缺少来源、客户承诺 | 真实索引写入、文档上传、线上 KB 发布 | passed |
| 14 | `quality_sprint01_pydantic_ai_structured_tool_candidate` | mock | 模拟采购申请文本，输出严格 typed JSON | 可表达为 schema/structured output utility | OpenAI-compatible 文本 route，schema 本地校验 | `mock_text`, `target_schema`, `validation_rules` | `typed_json`, `validation_errors`, `confidence`, `fallback_required` | 不调用真实 provider tool，不写系统 | schema 缺字段、低置信、金额异常 | 外部工具调用、业务系统写入 | passed |
| 15 | `quality_sprint01_browser_use_store_audit_candidate` | dry-run | 模拟授权本地页面 HTML，输出门店页面审计建议 | 可表达为 local page audit dry-run | 只处理 mock/local HTML 文本，不开浏览器抓取 | `mock_html`, `audit_rules`, `business_context` | `audit_findings`, `priority`, `suggested_fixes`, `external_action_blocked=true` | 不抓真实网页，不登录，不绕 ToS | 价格/资质/隐私/违法承诺 | 浏览器自动访问、登录、抓取、提交表单 | passed |
| 16 | `quality_sprint01_apify_authorized_competitor_snapshot_candidate` | mock | 模拟竞品页面快照文本，输出竞品摘要 | 可表达为 snapshot analysis candidate | mock HTML/text 走文本模型路由 | `mock_snapshot_text`, `comparison_scope`, `source_notes` | `competitor_summary`, `feature_changes`, `pricing_notes`, `risk_notes` | 不调用 Apify，不抓网页，不代理 | 版权引用、价格误读、ToS 风险 | 真实抓取、代理、批量采集、联系人采集 | passed |
| 17 | `quality_sprint01_unstructured_contract_invoice_agent_candidate` | mock | 模拟合同/票据提取文本，输出分段和字段 | 可表达为 doc parsing component/agent | mock extracted text 走结构化 route | `mock_doc_text`, `doc_type`, `extraction_schema` | `sections`, `key_fields`, `risk_flags`, `manual_review_required` | 不读真实文件，不做法律/审计结论 | 付款条款、违约责任、税号/金额异常 | 文件上传、法律结论、报销/税务审批 | passed |
| 18 | `quality_sprint01_docling_office_parser_candidate` | mock | 模拟 Office/PDF 抽取文本，输出 SOP 结构 | 可表达为 document parser component | mock extracted text 走文本模型路由 | `mock_extracted_text`, `layout_hints`, `target_format` | `document_outline`, `tables`, `action_items`, `parse_warnings` | 不读取真实 Office/PDF 文件 | 表格缺失、章节错位、合同敏感信息 | 文件解析真实执行、上传、OCR | passed |
| 19 | `quality_sprint01_paddleocr_receipt_doc_agent_candidate` | mock | 模拟 OCR 后票据文本，输出票据字段和金额校验 | 可表达为 OCR downstream parser component | mock OCR text 走结构化 route | `mock_ocr_text`, `receipt_schema`, `confidence_notes` | `merchant`, `line_items`, `amount_check`, `low_confidence_fields` | 不上传图片，不跑 OCR，不做税务结论 | 金额不一致、税号缺失、低置信字段 | OCR 真实执行、票据上传、报销审批 | passed |
| 20 | `quality_sprint01_shopify_product_image_bulk_agent_candidate` | dry-run | 模拟商品清单，生成批量图片/上架 dry-run payload | 可表达为 Shopify/media dry-run agent | 文本生成 payload，不调 Shopify/image provider | `mock_products`, `image_policy`, `listing_rules` | `bulk_plan`, `image_requests`, `shopify_payload`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不写 Shopify，不生成/上传图片 | 商标/版权、库存价格、违规商品、费用 | 图片生成、商品上传、库存/价格修改 | passed |
| 21 | `quality_sprint01_shotstack_video_api_candidate` | route-check | 模拟短视频脚本，生成 Shotstack render payload | 可表达为 video route candidate，需真实 provider 审批后再定 | 只检查 render spec，不调用 Shotstack | `mock_storyboard`, `asset_policy`, `cost_limit` | `render_payload`, `timeline`, `asset_requirements`, `real_media_generation_requires_approval=true` | 不上传素材，不渲染视频，不写 key | 肖像/版权、费用超限、违规内容 | provider 调用、渲染、上传发布 | passed |
| 22 | `quality_sprint01_did_avatar_video_candidate` | route-check | 模拟销售数字人口播脚本，生成 D-ID payload | 可表达为 avatar video route candidate，需真实 provider 审批后再定 | 只检查 payload，不调用 D-ID | `mock_script`, `avatar_policy`, `voice_policy`, `cost_limit` | `avatar_payload`, `script_review`, `consent_required`, `real_media_generation_requires_approval=true` | 不使用真人素材，不生成视频，不写 key | 肖像授权、声音授权、医疗/金融承诺 | provider 调用、视频生成、发布 | passed |
| 23 | `quality_sprint01_canva_design_export_dryrun_candidate` | dry-run | 模拟门店海报需求，生成 Canva design/export dry-run spec | 可表达为 design export dry-run agent | 文本中转生成 design spec | `mock_design_brief`, `brand_rules`, `export_policy` | `design_spec`, `export_plan`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Canva，不导出，不写设计文件 | 品牌素材授权、导出权限、二维码/价格错误 | Canva 写入、导出、发布、素材上传 | passed |
| 24 | `quality_sprint01_figma_to_brand_qc_candidate` | mock | 模拟 Figma frame JSON，输出品牌一致性 QC | 可表达为 read-only brand QC agent | mock frame JSON 走文本/结构化 route | `mock_frame_json`, `brand_rules`, `qc_scope` | `qc_findings`, `severity`, `fix_suggestions`, `manual_review_required` | 不连 Figma，不读取真实文件 | 品牌错色、商标使用、价格/承诺文案 | Figma 文件读取、写入、评论、导出 | passed |
| 25 | `quality_sprint01_agency_douyin_short_video_role_candidate` | mock role smoke | 模拟餐饮店抖音短视频岗位场景，输出角色建议 | 仅 role smoke，不是客户 callable Skill | 文本模型输出岗位建议 | `mock_business`, `role_goal`, `platform_rules` | `role_summary`, `department_fit`, `expected_deliverables`, `risk_notes`, `manual_review_required`, `not_customer_callable=true` | 不发布抖音，不生成视频 | 平台规则、夸大承诺、素材授权 | 发布、投放、视频生成、账号操作 | passed |
| 26 | `quality_sprint01_agency_xiaohongshu_store_role_candidate` | mock role smoke | 模拟美甲店小红书运营岗位场景，输出选题与风险建议 | 仅 role smoke，不是客户 callable Skill | 文本模型输出岗位建议 | `mock_store_profile`, `content_goal`, `platform_rules` | `role_summary`, `department_fit`, `expected_deliverables`, `risk_notes`, `manual_review_required`, `not_customer_callable=true` | 不发布小红书，不操作账号 | 平台合规、夸大效果、用户隐私 | 发布、私信、投放、账号操作 | passed |

## 9. 权限边界确认

- 未安装依赖。
- 未访问真实账号。
- 未调用真实 API/provider。
- 未写 key，未读取或打印 key。
- 未读取客户文件。
- 未发送邮件、短信、微信、Slack 或平台消息。
- 未写 CRM、Shopify、Sheets、Notion、Slack、HubSpot、Google、Figma、Canva 或其他业务系统。
- 未抓取真实网页。
- 未上传素材。
- 未生成真实图片、视频、音频、OCR 或 PDF 结果。
- 未改稳交付库；客户正式可调用 Skill 仍为 13。
