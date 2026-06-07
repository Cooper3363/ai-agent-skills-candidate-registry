# L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_05_QUEUE

生成日期：2026-06-05

来源：`../DEEPAGENTS_SMOKE_QUALITY_SPRINT_05_RESULT.md`

本队列性质：Quality Sprint 05 DeepAgents candidate smoke passed 后筛选的正式 L2 simulated Top10。  
重要边界：进入本队列不代表 L2 通过，不代表可封装，不代表客户正式可调用；客户正式可调用 Skill 仍为 13。

## 1. 正式 L2 simulated 统一口径

- 每个候选至少 3 个中文中小微业务 mock/read-only/dry-run 用例。
- 固定检查输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill/既有候选的重复关系、是否只能作为组件。
- SaaS/API connector 类只允许 mock/read-only/dry-run payload，不连接真实账号，不写业务系统。
- read-only 候选必须保留 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- Canva dry-run 必须保留 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- 媒体/provider route-check passed 候选未进入本 Top10；后续若推进，必须另走真实 provider smoke 审批，不能在正式 L2 中写成真实生成通过。

## 2. Top10 队列

| 排名 | candidate_id | 业务包 | smoke_type | trial mode | 正式 L2 重点 | 3 个中文用例方向 | 保留权限边界 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | 客服知识库助手包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Intercom conversations/articles/macros 到客服宏缺口和升级建议 | macro 缺口；投诉升级；账号安全 | 不连接 Intercom，不回复/更新/写宏 |
| 2 | `quality_sprint05_helpscout_article_gap_readonly_candidate` | 客服知识库助手包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock mailbox/docs 到知识库文章缺口和交接提示 | FAQ 缺口；政策冲突；高频投诉 | 不连接 Help Scout，不回复/打 tag/写 docs |
| 3 | `quality_sprint05_front_inbox_handoff_readonly_candidate` | 客服/运营交接包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock inbox messages 到跨班次交接摘要 | 班次交接；负责人缺口；VIP 未处理 | 不连接 Front，不发送/分配/评论 |
| 4 | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | 营销活动健康包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock campaign metrics 到活动健康和风险提示 | 退订异常；打开点击异常；样本质量 | 不连接 Klaviyo，不发送邮件/改联系人/campaign |
| 5 | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | 电商运营包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock products 到商品目录 QC | 属性缺失；价格异常；图片/合规风险 | 不连接 WooCommerce，不改商品/订单/库存/价格 |
| 6 | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | 电商运营包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock catalog/variants 到上架缺口报告 | 变体缺口；上架 readiness；库存敏感 | 不连接 BigCommerce，不改商品/变体/库存 |
| 7 | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | 营销投放分析包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock campaign reports 到预算/素材异常摘要 | 预算异常；素材风险；投放承诺边界 | 不连接 Google Ads，不改 budget/bid/ad |
| 8 | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | 营销/经营分析包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock GA4 rows 到落地页掉点报告 | 注册掉点；支付掉点；事件/样本质量 | 不连接 GA4，不改 property/config |
| 9 | `quality_sprint05_canva_design_brief_dryrun_candidate` | 营销设计 brief 包 | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | mock campaign brief 到设计 brief 与不可执行导出 spec | 活动海报 brief；菜单海报 brief；品牌素材风险 | 不连接 Canva，不创建/上传/导出 |
| 10 | `quality_sprint05_jira_service_sla_readonly_candidate` | 客服/服务台 SLA 包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock JSM requests/SLA 到服务 SLA 风险报告 | SLA 将超时；服务中断；重大客户升级 | 不连接 Jira，不写 request/issue/comment/status |

## 3. 媒体 Route-check Passed 候选

| candidate_id | 状态 | 后续处理 |
| --- | --- | --- |
| `quality_sprint05_openai_tts_support_voiceover_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint05_fal_flux_product_image_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint05_replicate_background_replace_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |

## 4. 未选入 Top10 的 passed 候选

| candidate_id | 处理建议 | 原因 |
| --- | --- | --- |
| `quality_sprint05_figma_design_token_audit_readonly_candidate` | 候补正式 L2 | 适合设计系统专题，当前 Top10 优先客服/电商/营销/服务台 |
| `quality_sprint05_asana_project_risk_readonly_candidate` | 候补正式 L2 | 与 Sprint04 monday/ClickUp 场景相近 |
| `quality_sprint05_trello_board_handoff_readonly_candidate` | 候补正式 L2 | 与项目交接类候选相近 |
| `quality_sprint05_confluence_policy_gap_readonly_candidate` | 候补正式 L2 | 适合知识库/政策专题 |
| `quality_sprint05_bamboohr_onboarding_gap_readonly_candidate` | 候补正式 L2 | HR 场景需更强隐私和人工复核 |
| `quality_sprint05_greenhouse_candidate_packet_readonly_candidate` | 候补正式 L2 | 招聘候选人 PII 与反歧视边界较重 |
| `quality_sprint05_docusign_contract_status_readonly_candidate` | 候补正式 L2 | 签约状态只读可行，但合同敏感度较高 |

## 5. 指挥中心确认点

- 是否批准本 Top10 进入正式 L2 simulated。
- 是否为 3 个媒体/provider route-check passed 项另建真实 provider smoke 审批队列。
- 是否将未入 Top10 的协作/HR/签约 passed 候选纳入后续专题 L2 队列。
