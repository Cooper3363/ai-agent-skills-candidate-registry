# L2_OFFICIAL_TOP15_FROM_NEXT50_QUEUE

来源：`DEEPAGENTS_SMOKE_NEXT50_RESULT.md`  
生成日期：2026-06-05  
说明：本队列来自 Next50 candidate smoke passed 候选筛选。进入本队列不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 正式 L2 口径

- 每个候选至少 3 个中文业务 mock/dry-run/route-check 用例。
- 检查固定 schema、失败判定、权限边界、人工复核触发、与稳交付 13 个 Skill 重复关系、是否仅组件。
- 媒体生成类仍默认只做 route/config/payload simulated；不真实生成图片、视频或音频。
- 如后续要真实 provider smoke，必须单独派发并明确 BYOK/key 托管、费用、内容安全、版权/肖像/商标/素材授权验收。

## 2. 统一禁止动作

- 不调用真实 provider/API。
- 不写 key。
- 不上传客户素材。
- 不生成真实图片、视频、音频、PPT、OCR 或 PDF。
- 不发送、不发布。
- 不写 CRM、Shopify、Figma、Canva、审批系统、日历、任务或其他业务系统。
- 不退款、不赔偿、不改库存。

## 3. Top15 队列

| 排名 | candidate_id | 业务包 | smoke 类型 | 正式 L2 重点 | 推荐 3 个中文用例方向 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `marketing_real_poster_banner_agent_candidate` | 营销内容生产包 | route-check | 海报/banner route、prompt、provider payload、版权/商标/价格边界 | 生鲜促销海报、课程体验 banner、会员日活动图 |
| 2 | `ecommerce_product_main_image_agent_candidate` | 电商/商品运营包 | route-check | 商品主图 route/payload、商品真实性、平台规则 | 保温杯主图、零食礼盒主图、3C 配件主图 |
| 3 | `marketing_short_video_ad_agent_candidate` | 营销投放包 | route-check | 短视频广告 route/payload、广告合规、素材授权 | 咖啡新品广告、本地课程广告、门店开业广告 |
| 4 | `ecommerce_product_video_from_image_candidate` | 电商/商品运营包 | route-check | 商品图生视频 route/payload、图片授权、成本提示 | 小家电图生视频、服饰图生视频、礼盒图生视频 |
| 5 | `sales_avatar_pitch_video_candidate` | 销售跟进助手包 | dry-run | 销售数字人口播脚本/payload、肖像/声音授权、禁止发送 | SaaS pitch、培训课程 pitch、门店服务 pitch |
| 6 | `hr_training_avatar_video_candidate` | 人事行政包 | dry-run | HR 培训数字人脚本/payload、制度准确、员工隐私 | 新员工服务规范、安全培训、请假制度讲解 |
| 7 | `ecommerce_background_replace_agent_candidate` | 电商/商品运营包 | dry-run | 商品图背景替换 edit payload、商品图授权、不上传素材 | 鞋类白底图、咖啡杯场景图、服饰节日背景 |
| 8 | `store_menu_poster_generation_candidate` | 门店经营/营销包 | route-check | 菜单海报 route/payload、价格准确、字体/商标边界 | 奶茶菜单、餐厅午市套餐、美容门店价目表 |
| 9 | `support_ticket_auto_reply_quality_gate_candidate` | 客服知识库助手包 | mock | 自动回复质检、违规拦截、转人工字段 | 退款承诺、账号安全、普通物流咨询 |
| 10 | `support_complaint_evidence_packet_candidate` | 客服知识库助手包 | mock | 投诉证据包、PII 脱敏、非法律结论 | 退款投诉、监管威胁、服务纠纷 |
| 11 | `support_afterhours_triage_bot_candidate` | 客服知识库助手包 | mock | 下班后分流、紧急度、不可承诺即时处理 | 账号被盗、退款投诉、普通咨询 |
| 12 | `support_voice_call_summary_agent_candidate` | 客服知识库助手包 | mock | mock transcript 摘要、行动项、PII/授权边界 | 售后通话、投诉通话、预约咨询通话 |
| 13 | `sales_crm_next_best_action_candidate` | 销售跟进助手包 | dry-run | CRM next action payload、write_allowed=false、禁止发送 | 报价后跟进、沉默线索、合同前提醒 |
| 14 | `sales_call_roleplay_coach_candidate` | 销售培训包 | mock | 销售角色扮演反馈、低风险训练、不可冒充真实客户 | 价格异议、竞品异议、预算不足 |
| 15 | `metrics_forecast_scenario_simulator_candidate` | 经营报表分析包 | mock | 经营情景模拟、假设透明、非财务建议 | 客流下降、客单价上升、成本上涨 |

## 4. 后续真实 provider smoke 计划提醒

以下 Top15 媒体类若进入真实 provider smoke，必须单独验收：`marketing_real_poster_banner_agent_candidate`、`ecommerce_product_main_image_agent_candidate`、`marketing_short_video_ad_agent_candidate`、`ecommerce_product_video_from_image_candidate`、`sales_avatar_pitch_video_candidate`、`hr_training_avatar_video_candidate`、`ecommerce_background_replace_agent_candidate`、`store_menu_poster_generation_candidate`。

真实 provider smoke 前置条件：
- BYOK/key 托管方案明确。
- 费用和调用上限明确。
- 内容安全策略明确。
- 版权、肖像、商标、素材授权复核明确。
- 输出不得直接发布或写入业务系统。

## 5. 当前状态

本队列仅用于正式 L2 simulated 派发。客户正式可调用 Skill 未新增，稳交付库状态不变。
