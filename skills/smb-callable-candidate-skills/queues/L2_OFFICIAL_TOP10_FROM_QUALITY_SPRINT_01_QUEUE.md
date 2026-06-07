# L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_QUEUE

生成日期：2026-06-05

来源：`../DEEPAGENTS_SMOKE_QUALITY_SPRINT_01_RESULT.md`

本队列性质：Quality Sprint 01 DeepAgents candidate smoke passed 后筛选的正式 L2 simulated Top10。  
重要边界：进入本队列不代表 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 正式 L2 simulated 统一口径

- 每个候选至少 3 个中文中小微六部门 mock/dry-run 用例。
- 固定检查输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill/既有候选的重复关系、是否只能作为组件。
- SaaS/OAuth/API/MCP 类只生成 dry-run payload，不连接真实账号，不写业务系统。
- 必须保留 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true` 的候选不得在 L2 中改为真实动作。
- 不安装依赖，不访问外网，不读取客户文件，不调用真实 API/provider，不写 key，不发送，不上传，不抓取真实网页，不生成真实媒体，不改稳交付库。

## 2. Top10 队列

| 排名 | candidate_id | 业务包 | smoke_type | trial mode | 正式 L2 重点 | 3 个中文用例方向 | 保留权限边界 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint01_google_sheets_mcp_report_agent_candidate` | 经营报表分析包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock 表格 rows 到经营摘要与异常字段 | 门店日销周报；渠道转化下滑；库存周转异常 | 不连接 Google Sheets，不读写真实表格 |
| 2 | `quality_sprint01_notion_ops_knowledge_agent_candidate` | 客服知识库助手包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Notion pages 到 FAQ 缺口与过期条款 | 售后政策整理；发票 FAQ 缺口；配送规则冲突 | 不连接 Notion，不读写真实页面 |
| 3 | `quality_sprint01_slack_support_triage_agent_candidate` | 客服知识库助手包 | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | 客服频道交接摘要与风险分流 | 投诉退款升级；账号安全求助；普通咨询交接 | `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` |
| 4 | `quality_sprint01_hubspot_crm_followup_agent_candidate` | 销售跟进助手包 | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | CRM 跟进建议与 dry-run payload | 新线索跟进；报价后异议；老客续费提醒 | `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` |
| 5 | `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | 客服/运营通用 Agent 包 | mock | `mock_only`, `read_only`, `external_action_blocked` | 工具计划、流程编排、安全边界 | 售后工单处理计划；知识库查询计划；投诉升级流程 | 不调用真实工具，不写业务系统 |
| 6 | `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | 销售跟进助手包 | mock | `mock_only`, `read_only`, `external_action_blocked` | 销售 pipeline 状态机与下一步检查 | 初访到方案；报价到谈判；停滞商机唤醒 | 不写 CRM，不自动推进阶段 |
| 7 | `quality_sprint01_microsoft_presidio_hr_pii_candidate` | HR/客服隐私组件包 | mock | `mock_only`, `read_only`, `external_action_blocked` | 中文简历/人员文本 PII 脱敏 | 中文简历脱敏；面试纪要脱敏；客服含个人信息文本脱敏 | 不读取真实简历，不上传外部服务，不保留未脱敏 PII |
| 8 | `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | 客服知识库助手包 | mock | `mock_only`, `read_only`, `external_action_blocked` | mock docs 到知识库刷新建议 | 新旧退款政策对比；FAQ 缺口识别；过期活动条款清理 | 不读取真实文档，不写线上知识库/向量库 |
| 9 | `quality_sprint01_pydantic_ai_structured_tool_candidate` | 通用结构化组件包 | mock | `mock_only`, `read_only`, `external_action_blocked` | typed JSON、schema 校验、失败回退 | 采购申请结构化；客户需求表单结构化；异常字段校验 | 不调用真实 provider tool，不写业务系统 |
| 10 | `quality_sprint01_unstructured_contract_invoice_agent_candidate` | 合同/票据文档组件包 | mock | `mock_only`, `read_only`, `external_action_blocked` | mock 文档分段、字段抽取、风险标签 | 合同条款分段；发票字段抽取；付款条款风险提示 | 不读取真实文件，不上传，不做法律/审计/税务结论 |

## 3. 未选入 Top10 但 smoke passed 的候选处理

| candidate_id | 处理建议 | 原因 |
| --- | --- | --- |
| `quality_sprint01_shopify_mcp_order_ops_candidate` | 作为候补 dry-run connector | 业务价值高，但 Shopify 订单/库存写入风险更高，需更严格 dry-run L2 |
| `quality_sprint01_product_photo_background_cleanup_candidate` | 真实 provider smoke 后再定 | 媒体 provider，只完成 route/config check |
| `quality_sprint01_creatomate_template_video_candidate` | 真实 provider smoke 后再定 | 视频 provider，只完成 route/config check |
| `quality_sprint01_zapier_actions_smb_connector_candidate` | 候补 dry-run connector | 动作面较宽，需先收窄动作白名单 |
| `quality_sprint01_make_scenario_dryrun_agent_candidate` | 候补 dry-run connector | 自动化执行风险较高，需固定 scenario 白名单 |
| `quality_sprint01_browser_use_store_audit_candidate` | 需后续限定 local/mock HTML | 真实网页/浏览器边界敏感 |
| `quality_sprint01_apify_authorized_competitor_snapshot_candidate` | 需后续限定 mock snapshot | 抓取/ToS/robots 边界敏感 |
| `quality_sprint01_docling_office_parser_candidate` | 候补文档解析组件 | 与 Unstructured 文档候选相邻，本轮优先取后者 |
| `quality_sprint01_paddleocr_receipt_doc_agent_candidate` | 候补 OCR downstream 组件 | 本轮不跑真实 OCR，需模型/权重边界复测 |
| `quality_sprint01_shopify_product_image_bulk_agent_candidate` | 真实 provider smoke 后再定 | 同时涉及 Shopify 写入和媒体生成，风险较高 |
| `quality_sprint01_shotstack_video_api_candidate` | 真实 provider smoke 后再定 | 视频 provider，只完成 route/config check |
| `quality_sprint01_did_avatar_video_candidate` | 真实 provider smoke 后再定 | 数字人肖像/声音授权风险高 |
| `quality_sprint01_canva_design_export_dryrun_candidate` | 候补 design dry-run | 导出/写设计系统边界需先锁定 |
| `quality_sprint01_figma_to_brand_qc_candidate` | 候补品牌 QC | read-only mock 可用，但需与设计类候选排序 |
| `quality_sprint01_agency_douyin_short_video_role_candidate` | role smoke 资产，不送正式 L2 | 角色库不是客户 callable Skill |
| `quality_sprint01_agency_xiaohongshu_store_role_candidate` | role smoke 资产，不送正式 L2 | 角色库不是客户 callable Skill |

## 4. 指挥中心确认点

- 是否批准本 Top10 进入正式 L2 simulated。
- 是否要求媒体 provider 类候选另建真实 provider smoke 审批队列。
- 是否要求 SaaS/OAuth/API/MCP 类候选在 L2 前统一补充 dry-run payload schema 模板。
