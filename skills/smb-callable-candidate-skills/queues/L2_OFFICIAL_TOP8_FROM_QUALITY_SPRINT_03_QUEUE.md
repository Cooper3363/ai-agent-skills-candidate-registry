# L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_03_QUEUE

生成日期：2026-06-05

来源：`../DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_RESULT.md`

本队列性质：Quality Sprint 03 DeepAgents candidate smoke passed 后筛选的正式 L2 simulated Top8。  
重要边界：进入本队列不代表 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 正式 L2 simulated 统一口径

- 每个候选至少 3 个中文中小微六部门 mock/dry-run 用例。
- 固定检查输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill/既有候选的重复关系、是否只能作为组件。
- SaaS/API/MCP connector 类只生成 mock/read-only/dry-run payload，不连接真实账号，不写业务系统。
- dry-run 候选必须保留 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- OpenAI Images/TTS route-check passed 候选未进入本 Top8；后续若推进，必须另走真实 provider smoke 审批，不得在正式 L2 中写成真实生成通过。
- DeepAgents workflow 示例未进入本 Top8；后续如推进，需先抽成明确业务 Skill，而不是直接封装示例 workflow。
- 不安装依赖，不访问外网，不读取客户文件，不调用真实 API/provider，不写 key，不发送，不上传，不抓取真实网页，不生成真实媒体/文件，不改稳交付库。

## 2. Top8 队列

| 排名 | candidate_id | 业务包 | smoke_type | trial mode | 正式 L2 重点 | 3 个中文用例方向 | 保留权限边界 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | 电商运营/销售助手包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock 商品目录到 QC、缺字段、异常提示 | 商品标题/图片缺失；库存异常；商品属性不完整 | 不连接 Shopify，不写商品/库存，不上传图片 |
| 2 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | 经营报表/续费健康包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock subscriptions 到订阅健康和失败扣款风险 | 失败扣款；即将流失；高价值订阅异常 | 不连接 Stripe，不扣款、不退款、不改订阅 |
| 3 | `quality_sprint03_mcp_notion_policy_gap_candidate` | 客服知识库助手包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Notion pages 到政策缺口/冲突/过期提示 | 退款政策缺口；配送规则冲突；账号安全流程缺失 | 不连接 Notion，不写页面，不改权限 |
| 4 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | 经营报表/库存运营包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Airtable rows 到库存预警和补货核查 | 缺货预警；高库存；责任人/更新时间缺失 | 不连接 Airtable，不写行，不改库存 |
| 5 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | 客服知识库助手包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Slack messages 到 FAQ 缺口和风险主题 | 发票高频问题；退款投诉主题；账号安全求助 | 不连接 Slack，不发消息，不读真实 workspace |
| 6 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | 办公文档/知识库包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Drive file metadata 到文档分类/敏感提示 | 合同文件分类；发票/票据分类；HR 文档敏感提示 | 不读取真实文件内容，不移动/删除/共享文件 |
| 7 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | 销售跟进助手包 | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | mock contacts 到数据健康报告和 dry-run payload | 联系人重复；关键字段缺失；高价值客户信息风险 | `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` |
| 8 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | 经营报表/财务预警包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock accounts/expenses 到现金流预警 | 现金余额低；异常费用；应付集中到期 | 不连接 QuickBooks，不写账、不报税、不做审计结论 |

## 3. 未选入 Top8 的 passed 候选处理

| 类型 | 候选 | 处理建议 |
| --- | --- | --- |
| OpenAI provider route-check | `quality_sprint03_openai_image_product_variant_candidate`, `quality_sprint03_openai_image_poster_layout_candidate`, `quality_sprint03_openai_tts_training_microcourse_candidate` | 仅 route-check passed；后续需真实 provider smoke 审批，不进入本 Top8 |
| DeepAgents workflow 示例 | `quality_sprint03_deepagents_customer_ops_example_candidate`, `quality_sprint03_deepagents_research_report_example_candidate` | 先作为 workflow 适配参考，不直接送正式 L2 |
| 财务/AR 候补 | `quality_sprint03_mcp_xero_ar_followup_candidate` | 候补正式 L2；与 QuickBooks/Stripe 同类，优先级略低 |
| 设计/feed QC 候补 | `quality_sprint03_canva_connect_brand_kit_qc_candidate`, `quality_sprint03_mcp_google_merchant_feed_qc_candidate` | 候补正式 L2；可在后续设计/电商 feed 专题中推进 |

## 4. 指挥中心确认点

- 是否批准本 Top8 进入正式 L2 simulated。
- 是否将 OpenAI Images/TTS route-check passed 项并入真实 provider smoke 审批链路。
- 是否要求 SaaS/API/MCP connector 候选在 L2 前统一补充 dry-run/read-only payload schema 模板。
