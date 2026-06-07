# L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_02_QUEUE

生成日期：2026-06-05

来源：`../DEEPAGENTS_SMOKE_QUALITY_SPRINT_02_RESULT.md`

本队列性质：Quality Sprint 02 DeepAgents candidate smoke passed 后筛选的正式 L2 simulated Top10。  
重要边界：进入本队列不代表 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 正式 L2 simulated 统一口径

- 每个候选至少 3 个中文中小微六部门 mock/dry-run 用例。
- 固定检查输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill/既有候选的重复关系、是否只能作为组件。
- SaaS/OAuth/API/邮件/CRM/POS/协作工具类只生成 mock 或 dry-run payload，不连接真实账号，不写业务系统。
- dry-run 候选必须保留 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`。
- 媒体/provider route-check passed 候选未进入本 Top10；后续若推进，必须另走真实 provider smoke 审批，不得在正式 L2 中写成真实生成通过。
- 不安装依赖，不访问外网，不读取客户文件，不调用真实 API/provider，不写 key，不发送，不上传，不抓取真实网页，不生成真实媒体，不改稳交付库。

## 2. Top10 队列

| 排名 | candidate_id | 业务包 | smoke_type | trial mode | 正式 L2 重点 | 3 个中文用例方向 | 保留权限边界 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint02_microsoft_excel_report_agent_candidate` | 经营报表分析包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Excel rows 到经营摘要、异常、source rows | 门店周报；渠道费用表；库存周转表 | 不连接 Graph/Excel，不读取或写入真实文件 |
| 2 | `quality_sprint02_square_pos_daily_report_candidate` | 经营报表分析包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock POS rows 到门店经营日报 | 门店销售日报；退款异常；热销品类变化 | 不连接 Square，不收款、不退款、不写 POS |
| 3 | `quality_sprint02_gmail_customer_email_triage_candidate` | 客服知识库助手包 | dry-run | `dry_run_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock email 到分类、风险标签和回复草稿 | 投诉退款邮件；账号安全邮件；普通发票咨询 | `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` |
| 4 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | 销售/客服跟进包 | dry-run | `dry_run_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Outlook 邮件到跟进草稿 | 销售询价跟进；售后争议跟进；会议后邮件草稿 | `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` |
| 5 | `quality_sprint02_zoho_crm_followup_candidate` | 销售跟进助手包 | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | mock Zoho lead 到下一步 CRM payload | 新线索跟进；报价异议；续费提醒 | `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` |
| 6 | `quality_sprint02_pipedrive_deal_next_step_candidate` | 销售跟进助手包 | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | mock deal 到阶段判断和下一步建议 | 初访后推进；谈判停滞；大额折扣审批 | `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` |
| 7 | `quality_sprint02_lark_docs_meeting_action_candidate` | 办公协同/销售运营包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock 会议文档到行动项和 owner 缺口 | 销售例会；运营复盘；客户项目会 | 不连接 Lark，不创建任务，不写文档 |
| 8 | `quality_sprint02_wecom_customer_group_summary_candidate` | 客服/私域运营包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock 群消息到摘要、客户意图、风险标签 | 促销群咨询；投诉群消息；售后 FAQ 群答疑 | 不连接企微，不发群消息，不读取真实群 |
| 9 | `quality_sprint02_gorgias_ecommerce_support_candidate` | 客服知识库助手包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock 电商工单到分类、优先级、转人工 | 物流延迟；退款争议；差评投诉 | 不连接 Gorgias，不回复工单、不退款 |
| 10 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | 财务/经营报表包 | mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock 费用/发票 rows 到核对提示 | 发票金额不一致；重复报销；缺税号/日期 | 不连接 Zoho Books，不做审计/税务/报销结论 |

## 3. 未选入 Top10 的 passed 候选处理

| 类型 | 候选 | 处理建议 |
| --- | --- | --- |
| 媒体/provider route-check | Stability、Adobe Firefly、fal FLUX、Runway、Recraft、Ideogram、fal Kontext、remove.bg、Luma、Google Veo、HeyGen | 仅 route-check passed；后续需真实 provider smoke 审批，不进入本 Top10 |
| 订单/运营 mock | `quality_sprint02_shopline_order_digest_candidate`, `quality_sprint02_feishu_bitable_ops_tracker_candidate`, `quality_sprint02_mailchimp_campaign_report_candidate` | 作为候补正式 L2；与 Top10 同类能力相比优先级略低 |
| FAQ/eval/结构化组件 | `quality_sprint02_haystack_faq_rag_candidate`, `quality_sprint02_instructor_schema_extraction_candidate`, `quality_sprint02_promptfoo_support_regression_candidate` | 候补或组件池；注意与稳交付 13 个重复 |
| Agent workflow | `quality_sprint02_autogen_sales_roleplay_candidate`, `quality_sprint02_crewai_market_research_candidate` | 先作为 workflow/roleplay 组件候补，不直接送封装 |

## 4. 指挥中心确认点

- 是否批准本 Top10 进入正式 L2 simulated。
- 是否为媒体/provider route-check passed 项另建真实 provider smoke 审批队列。
- 是否要求 SaaS/API/CRM/邮件类候选在 L2 前统一补充 dry-run payload schema 模板。
