# L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_04_QUEUE

生成日期：2026-06-05

来源：`../DEEPAGENTS_SMOKE_QUALITY_SPRINT_04_RESULT.md`

本队列性质：Quality Sprint 04 DeepAgents candidate smoke passed 后筛选的正式 L2 simulated Top10。  
重要边界：进入本队列不代表 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 正式 L2 simulated 统一口径

- 每个候选至少 3 个中文中小微六部门 mock/dry-run 用例。
- 固定检查输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill/既有候选的重复关系、是否只能作为组件。
- SaaS/API connector 类只生成 mock/read-only/dry-run payload，不连接真实账号，不写业务系统。
- dry-run 候选必须保留 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- read-only 候选必须保留最小只读 scope、`write_allowed=false` 和 `external_action_blocked=true`。
- 媒体 provider route-check passed 候选未进入本 Top10；后续若推进，必须另走真实 provider smoke 审批，不得在正式 L2 中写成真实生成通过。

## 2. Top10 队列

| 排名 | candidate_id | 业务包 | smoke_type | trial mode | 正式 L2 重点 | 3 个中文用例方向 | 保留权限边界 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | 客服知识库助手包 | read-only mock | `read_only_mock` | mock Zendesk tickets/macros/help-center 到 SLA 风险与 macro 缺口 | SLA 将超时；macro 缺口；投诉升级 | 不连接 Zendesk，不回复/改状态/写 macro |
| 2 | `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | 客服知识库助手包 | read-only mock | `read_only_mock` | mock Freshdesk tickets/SLA 到超时风险和升级建议 | SLA 超时；高价值客户投诉；低优先级误分 | 不连接 Freshdesk，不回复/改状态 |
| 3 | `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | 销售跟进助手包 | dry-run | `dry_run_only` | mock opportunities/accounts 到商机健康 dry-run payload | 商机字段缺失；停滞商机；大额商机风险 | `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` |
| 4 | `quality_sprint04_shopline_catalog_qc_readonly_candidate` | 电商运营/销售助手包 | read-only mock | `read_only_mock` | mock catalog 到商品字段缺口、价格/图片风险 | 商品属性缺失；价格异常；图片缺失 | 不连接 Shopline，不写商品/库存/价格 |
| 5 | `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | 经营报表/门店运营包 | read-only mock | `read_only_mock` | mock POS shift rows 到班次异常摘要 | 退款异常；交班差异；库存联动异常 | 不连接 POS，不退款、不改库存 |
| 6 | `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | 财务/经营报表包 | read-only mock | `read_only_mock` | mock transactions/invoices 到对账异常提示 | 金额不一致；重复交易；未匹配发票 | 不连接 Xero，不写账/付款/报税 |
| 7 | `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | 产品/营销分析包 | read-only mock | `read_only_mock` | mock funnel/event stats 到漏斗掉点和数据质量 | 注册掉点；支付转化异常；事件缺失 | 不连接 PostHog，不改 tracking 配置 |
| 8 | `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | 产品/客服协同包 | read-only mock | `read_only_mock` | mock issues/customer feedback 到 bug 分流 | 关键客户反馈；高影响 bug；客服回传建议 | 不连接 Linear，不写 issue/comment/status |
| 9 | `quality_sprint04_monday_board_health_readonly_candidate` | 办公协同/项目运营包 | read-only mock | `read_only_mock` | mock board items 到项目健康和负责人缺口 | 逾期事项；负责人缺失；高优先级项目风险 | 不连接 monday，不写 item/comment/status |
| 10 | `quality_sprint04_clickup_task_risk_readonly_candidate` | 办公协同/项目运营包 | read-only mock | `read_only_mock` | mock tasks 到延期/阻塞/跨部门交接风险 | 延期任务；依赖阻塞；跨部门交接 | 不连接 ClickUp，不写任务/comment/status |

## 3. 媒体 Route-check Passed 候选

| candidate_id | 状态 | 后续处理 |
| --- | --- | --- |
| `quality_sprint04_runway_video_ad_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint04_heygen_avatar_training_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint04_synthesia_hr_training_video_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint04_recraft_brand_asset_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint04_ideogram_poster_copy_image_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint04_tavus_sales_avatar_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |
| `quality_sprint04_did_avatar_support_script_payload_candidate` | route-check passed | 真实 provider smoke 待定，`real_provider_smoke_required=true` |

## 4. 未选入 Top10 的 Passed 候选

| candidate_id | 处理建议 | 原因 |
| --- | --- | --- |
| `quality_sprint04_mailchimp_campaign_health_readonly_candidate` | 候补正式 L2 | 与 Brevo 同类，营销活动健康可另做邮件营销专题 |
| `quality_sprint04_brevo_email_campaign_health_readonly_candidate` | 候补正式 L2 | 与 Mailchimp 同类，本轮 Top10 优先项目协同/客服/销售/财务 |

## 5. 指挥中心确认点

- 是否批准本 Top10 进入正式 L2 simulated。
- 是否为媒体 provider route-check passed 项另建真实 provider smoke 审批队列。
- 是否将 Mailchimp/Brevo 放入后续邮件营销健康专题 L2 队列。
