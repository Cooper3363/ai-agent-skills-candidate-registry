# L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_07_QUEUE

生成日期：2026-06-07

来源：`../DEEPAGENTS_SMOKE_QUALITY_SPRINT_07_RESULT.md`

本队列性质：Quality Sprint 07 DeepAgents candidate smoke passed 后筛选的正式 L2 simulated Top8。  
重要边界：进入本队列不代表 L2 通过，不代表可封装，不代表自动进入 stable 或客户正式可调用；按 2026-06-06 新规则，stable 仓库正式 Skill 已扩容为 55 个。

## 1. 正式 L2 simulated 统一口径

- 每个候选至少 3 个中文中小微业务 mock/read-only 用例。
- 固定检查输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与 stable 55 个 Skill/既有候选的重复关系、是否只能作为组件。
- SaaS/API connector 类只允许 mock/read-only payload，不连接真实账号，不写业务系统。
- read-only 候选必须保留 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- 媒体/provider route-check passed 候选未进入本 Top8；后续若推进，必须另走真实 provider smoke 审批，不能在正式 L2 中写成真实生成通过。

## 2. Top8 队列

| 排名 | candidate_id | 业务包 | smoke_type | trial mode | 正式 L2 重点 | 3 个中文用例方向 | 保留权限边界 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint07_intercom_article_decay_readonly_candidate` | 客服知识库助手包 | read-only mock | `read_only_mock` | mock Intercom articles/conversations 到文章衰减和缺口报告 | 文章过期；高频问题缺口；政策冲突 | 不连接 Intercom，不写文章/发消息 |
| 2 | `quality_sprint07_shopify_return_product_quality_candidate` | 电商售后质量包 | read-only mock | `read_only_mock` | mock returns/products 到商品质量问题聚类 | 高退货率；质量安全；退款边界 | 不连接 Shopify，不退款/改商品/改库存 |
| 3 | `quality_sprint07_metabase_executive_digest_candidate` | 经营报表摘要包 | read-only mock | `read_only_mock` | mock dashboard cards 到经营摘要和数据质量提示 | 日报摘要；异常指标；数据质量 | 不连接 Metabase/DB，不写 query/dashboard |
| 4 | `quality_sprint07_docusign_missing_signature_readonly_candidate` | 合同签署状态包 | read-only mock | `read_only_mock` | mock envelopes 到缺签和停滞报告 | 缺签；签署方异常；临期合同 | 不连接 DocuSign，不发送/签署/改 envelope |
| 5 | `quality_sprint07_mailchimp_deliverability_qc_candidate` | 邮件营销健康包 | read-only mock | `read_only_mock` | mock campaign reports 到送达 QC | bounce 异常；投诉/退订；受众健康 | 不连接 Mailchimp，不发送/改 audience |
| 6 | `quality_sprint07_helpscout_saved_reply_gap_candidate` | 客服回复模板包 | read-only mock | `read_only_mock` | mock conversations/saved replies 到模板缺口报告 | 高频问题；政策冲突；账号安全/退款 | 不连接 Help Scout，不回复/写 saved reply |
| 7 | `quality_sprint07_front_account_handoff_candidate` | 客户交接包 | read-only mock | `read_only_mock` | mock account conversations 到客户交接 brief | VIP 交接；承诺日期；未闭环事项 | 不连接 Front，不发送/分派/评论 |
| 8 | `quality_sprint07_amplitude_activation_dropoff_candidate` | 产品/增长分析包 | read-only mock | `read_only_mock` | mock activation metrics 到激活掉点报告 | 注册掉点；激活事件缺失；样本质量 | 不连接 Amplitude，不写 cohorts/charts |

## 3. 媒体 Route-check Passed 候选

| candidate_id | 状态 | 后续处理 |
| --- | --- | --- |
| `quality_sprint07_openai_image_review_to_product_scene_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint07_runway_customer_story_clip_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint07_fal_packshot_to_lifestyle_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint07_heygen_new_employee_avatar_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |

## 4. 未选入 Top8 的 passed 候选

| candidate_id | 处理建议 | 原因 |
| --- | --- | --- |
| `quality_sprint07_workable_interview_question_bank_candidate` | 候补正式 L2 | 招聘题库有价值，但候选人 PII 与反歧视边界更重，建议 HR 专题 L2 |
| `quality_sprint07_greenhouse_offer_risk_readonly_candidate` | 候补正式 L2 | offer 风险价值高，但薪酬/录用边界敏感，建议 HR 专题 L2 |
| `quality_sprint07_hubspot_lead_source_quality_candidate` | 候补正式 L2 | CRM 线索质量可行，但本轮 Top8 优先客服/电商/报表/合同/产品分析 |

## 5. 指挥中心确认点

- 是否批准本 Top8 进入正式 L2 simulated。
- 是否为 5 个媒体/provider route-check passed 项另建真实 provider smoke 审批队列。
- 是否将 Workable/Greenhouse/HubSpot passed 候选纳入后续 HR/CRM 专题 L2 队列。
