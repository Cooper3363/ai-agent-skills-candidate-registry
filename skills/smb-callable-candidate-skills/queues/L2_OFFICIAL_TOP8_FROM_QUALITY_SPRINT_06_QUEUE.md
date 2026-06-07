# L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_06_QUEUE

生成日期：2026-06-05

来源：`../DEEPAGENTS_SMOKE_QUALITY_SPRINT_06_RESULT.md`

本队列性质：Quality Sprint 06 DeepAgents candidate smoke passed 后筛选的正式 L2 simulated Top8。  
重要边界：进入本队列不代表 L2 通过，不代表可封装，不代表客户正式可调用；客户正式可调用 Skill 仍为 13。

## 1. 正式 L2 simulated 统一口径

- 每个候选至少 3 个中文中小微业务 mock/read-only/dry-run 用例。
- 固定检查输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill/既有候选的重复关系、是否只能作为组件。
- SaaS/API connector 类只允许 mock/read-only/dry-run payload，不连接真实账号，不写业务系统。
- read-only 候选必须保留 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- HubSpot dry-run 必须保留 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- 媒体/provider route-check passed 候选未进入本 Top8；后续若推进，必须另走真实 provider smoke 审批，不能在正式 L2 中写成真实生成通过。

## 2. Top8 队列

| 排名 | candidate_id | 业务包 | smoke_type | trial mode | 正式 L2 重点 | 3 个中文用例方向 | 保留权限边界 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | 知识库/政策 QC 包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock SharePoint pages 到政策缺口、过期政策和 QC flags | 政策过期；政策冲突；敏感制度缺口 | 不连接 M365，不写页面/文件/权限 |
| 2 | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | 协作交接包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock Teams messages 到交接 digest 和 owner gap | 班次交接；负责人缺口；承诺日期风险 | 不连接 Teams，不发消息/建任务/写频道 |
| 3 | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | 财务/经营分析包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock budget rows 到预算差异和复核提示 | 超预算；科目错分；预算缺口 | 不读真实 Sheets，不写单元格/生成文件 |
| 4 | `quality_sprint06_zendesk_answerbot_deflection_candidate` | 客服知识库助手包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock tickets/articles 到 answerbot deflection 机会 | 高频问题；文章缺口；账号安全/退款边界 | 不连接 Zendesk，不回复/写文章/改工单 |
| 5 | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | 销售交接助手包 | dry-run | `dry_run_only`, `BYOK_required`, `external_action_blocked` | mock deals/notes 到交接质量报告和不可执行 payload | 大额商机；下一步缺失；PII/承诺折扣 | 不连接 HubSpot，不写 deal/note/task/邮件 |
| 6 | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | 付款挽回草稿包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock failed payments 到挽回草稿和支付风险 | 失败付款；重复扣款风险；订阅挽回草稿 | 不连接 Stripe，不扣款/退款/发邮件 |
| 7 | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | HR 排班覆盖包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock time-off rows 到覆盖缺口和隐私提示 | 请假覆盖；关键岗位缺口；员工 PII | 不连接 BambooHR，不写员工记录/做 HR 决策 |
| 8 | `quality_sprint06_google_workspace_gmail_label_health_candidate` | 邮箱运营健康包 | read-only mock | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | mock labels/message headers 到标签健康报告 | 标签失效；客户邮件漏分；敏感发件人 | 不连接 Gmail，不读正文/发送/改标签 |

## 3. 媒体 Route-check Passed 候选

| candidate_id | 状态 | 后续处理 |
| --- | --- | --- |
| `quality_sprint06_openai_image_brand_scene_batch_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint06_runway_storyboard_to_clip_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint06_openai_tts_customer_training_audio_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint06_fal_product_model_tryon_route_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint06_heygen_sales_objection_avatar_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |

## 4. 未选入 Top8 的 passed 候选

| candidate_id | 处理建议 | 原因 |
| --- | --- | --- |
| `quality_sprint06_freshdesk_agent_workload_balance_candidate` | 候补正式 L2 | 与既有客服 SLA/工作量候选相近，后续客服运营专题可补测 |
| `quality_sprint06_shopify_subscription_order_exception_candidate` | 候补正式 L2 | 订阅订单异常价值高，但退款/订阅边界较重 |
| `quality_sprint06_docusign_renewal_notice_gap_candidate` | 候补正式 L2 | 合同续约状态只读可行，但合同敏感度较高 |
| `quality_sprint06_posthog_funnel_dropoff_candidate` | 候补正式 L2 | 与既有 PostHog/GA4 漏斗分析候选相近 |
| `quality_sprint06_mailchimp_audience_health_candidate` | 候补正式 L2 | 与 Klaviyo/Mailchimp 邮件健康候选相近，适合邮件营销专题 |

## 5. 指挥中心确认点

- 是否批准本 Top8 进入正式 L2 simulated。
- 是否为 5 个媒体/provider route-check passed 项另建真实 provider smoke 审批队列。
- 是否将未入 Top8 的客服/电商/签约/分析/邮件健康 passed 候选纳入后续专题 L2 队列。
