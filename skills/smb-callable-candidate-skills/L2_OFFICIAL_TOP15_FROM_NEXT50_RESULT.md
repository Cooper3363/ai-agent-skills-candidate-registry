# L2_OFFICIAL_TOP15_FROM_NEXT50_RESULT

回传对象：AI.Skills 指挥中心  
执行日期：2026-06-05  
输入队列：`queues/L2_OFFICIAL_TOP15_FROM_NEXT50_QUEUE.md`  
执行方式：正式 L2 simulated；仅执行 mock/dry-run/route-check，不调用真实 provider/API，不写 key，不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 1. 已完成事项

- 已读取 `DEEPAGENTS_SMOKE_NEXT50_RESULT.md` 与 `queues/L2_OFFICIAL_TOP15_FROM_NEXT50_QUEUE.md`。
- 已对 Top15 每个候选完成 3 个中文中小微业务 mock/dry-run/route-check 用例，共 45 个用例。
- 已检查固定输入/输出 schema、中文业务可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill / 既有候选重复关系、是否只能作为组件、是否适合送 draft_l3 封装。
- 已按媒体生成类特别边界标注 `real_provider_smoke_required=true`。
- 已按 SaaS/OAuth/API 类边界保留 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`。
- 已生成 `queues/DRAFT_L3_PACKAGING_QUEUE_FROM_NEXT50.md`。

## 2. 当前问题

- 8 个媒体/真实 provider 相关候选只完成 route/config/payload simulated L2，不能写成真实 provider 通过。
- 真实图片/视频生成候选进入封装前，需要单独完成 provider smoke，包括 BYOK/key 托管、费用上限、内容安全、版权/肖像/商标/素材授权验收。
- 本轮不新增客户正式可调用 Skill，稳交付库仍为 13。

## 3. 阻塞原因

- 无权限阻塞。
- 无 L2 执行阻塞。
- 媒体类未进入 draft L3 的原因不是失败，而是缺少真实 provider smoke。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 7 个 `L2 通过可封装` 候选进入 draft_l3 封装窗口。
- 是否另开真实 provider smoke 专项，覆盖 8 个媒体/真实 provider 相关候选。

## 5. 建议下一步

- 封装窗口先处理 7 个文本/受控 dry-run 候选。
- 媒体候选保留在候选库，等待真实 provider smoke 计划。
- 正式 provider smoke 前不得写入 key、不得调用真实 provider、不得上传客户素材、不得生成真实媒体。

## 6. 数量表

| L2 结论 | 数量 |
| --- | ---: |
| L2 通过可封装 | 7 |
| 需补测 | 0 |
| 暂缓 | 0 |
| 未通过 | 0 |
| 仅组件 | 0 |
| 真实 provider smoke 后再定 | 8 |

## 7. L2 通过清单

1. `support_ticket_auto_reply_quality_gate_candidate`
2. `support_complaint_evidence_packet_candidate`
3. `support_afterhours_triage_bot_candidate`
4. `support_voice_call_summary_agent_candidate`
5. `sales_crm_next_best_action_candidate`
6. `sales_call_roleplay_coach_candidate`
7. `metrics_forecast_scenario_simulator_candidate`

## 8. 真实 provider smoke 后再定清单

1. `marketing_real_poster_banner_agent_candidate`
2. `ecommerce_product_main_image_agent_candidate`
3. `marketing_short_video_ad_agent_candidate`
4. `ecommerce_product_video_from_image_candidate`
5. `sales_avatar_pitch_video_candidate`
6. `hr_training_avatar_video_candidate`
7. `ecommerce_background_replace_agent_candidate`
8. `store_menu_poster_generation_candidate`

## 9. 总表

| 候选 | 用例完成 | schema 稳定性 | 中文可用性 | callable 表达 | 模型通道适配 | 权限边界 | 人工复核触发 | 失败判定 | 重复/组件判断 | L2 结论 | 建议下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `marketing_real_poster_banner_agent_candidate` | 3/3 | 高 | 高 | `poster_banner_route_payload` | 文本/prompt 可走中转；图片走 OpenAI image relay route-check | 不写 key、不出图、不上传素材 | 商标、版权、价格、绝对化用语、内容安全 | 写成真实出图、漏授权、无费用提示 | 与营销文案相邻但媒体输出独立 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `ecommerce_product_main_image_agent_candidate` | 3/3 | 高 | 高 | `product_main_image_route_payload` | 文本/prompt 中转；图片 route-check | 不出图、不上传商品素材、不改平台 | 商品真实性、平台规则、商标、版权 | 生成虚假主图、漏平台风险 | 与商品文案不同，主图媒体能力独立 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `marketing_short_video_ad_agent_candidate` | 3/3 | 高 | 高 | `short_video_ad_route_payload` | 文本中转；Veo/Gemini route-check | 不生成视频、不上传素材、不投放 | 广告合规、音乐/人物/商标授权、费用 | 写成真实视频通过、承诺投放效果 | 与营销内容相邻但短视频媒体独立 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `ecommerce_product_video_from_image_candidate` | 3/3 | 高 | 高 | `product_image_to_video_route_payload` | 文本中转；Luma route-check | 不上传商品图、不生成视频 | 商品图授权、商标、费用、下载/存储 | 调用 Luma、生成视频、漏授权 | 与商品主图不同，图生视频独立 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `sales_avatar_pitch_video_candidate` | 3/3 | 高 | 高 | `avatar_pitch_payload` | 话术走中转；HeyGen payload dry-run | 不生成数字人、不发送、不上传头像/声音 | 肖像/声音授权、销售承诺、折扣 | `send_allowed` 非 false、真实生成、夸大承诺 | 与销售话术相邻但数字人口播独立 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `hr_training_avatar_video_candidate` | 3/3 | 高 | 高 | `hr_training_avatar_payload` | 脚本走中转；Synthesia payload dry-run | 不生成视频、不上传员工素材 | 制度准确、员工隐私、肖像授权 | 写成正式培训视频、漏制度复核 | 与 HR FAQ 不同，培训视频独立 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `ecommerce_background_replace_agent_candidate` | 3/3 | 高 | 高 | `background_replace_payload` | 文本中转；fal edit payload dry-run | 不上传商品图、不生成编辑结果 | 商品图授权、误导性场景、平台规则 | 上传素材、真实编辑、虚假商品场景 | 电商图片编辑独立，高价值 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `store_menu_poster_generation_candidate` | 3/3 | 高 | 高 | `store_menu_poster_route_payload` | 文本中转；OpenAI image relay route-check | 不出图、不发布、不写菜单系统 | 价格准确、字体/商标、图片版权 | 价格错误、真实出图、直接发布 | 门店营销高频，媒体能力独立 | 真实 provider smoke 后再定 | 保留候选，单独 provider smoke |
| `support_ticket_auto_reply_quality_gate_candidate` | 3/3 | 高 | 高 | `auto_reply_quality_gate` | 文本质检可走中转 | 不发送、不写客服系统 | 退款、赔偿、账号安全、投诉升级 | 漏越权承诺、未转人工、自动发送 | 与 `support_reply_guardrail` 相邻，但自动回复闸门更明确 | L2 通过可封装 | 送 draft_l3 |
| `support_complaint_evidence_packet_candidate` | 3/3 | 高 | 高 | `complaint_evidence_packet` | 文本/RAG mock 可走中转 | 只读 mock，不上传文件，非法律结论 | 监管威胁、赔偿、PII、证据缺口 | 法律结论、保留未脱敏 PII、联系客户 | 与投诉摘要相邻，但证据包结构独立 | L2 通过可封装 | 送 draft_l3 |
| `support_afterhours_triage_bot_candidate` | 3/3 | 高 | 高 | `afterhours_triage` | 文本分流可走中转 | 不承诺即时处理、不派单、不发送 | 账号安全、退款投诉、紧急事项、低置信 | 自动派单、承诺处理、漏高危 | 与客服分类相邻，但下班后场景明确 | L2 通过可封装 | 送 draft_l3 |
| `support_voice_call_summary_agent_candidate` | 3/3 | 高 | 高 | `call_summary_agent` | mock transcript 文本摘要可走中转；不做 ASR | 不上传真实音频、不写工单 | PII、投诉、退款承诺、行动项缺失 | 编造通话内容、漏行动项、保留 PII | 与销售会议摘要相邻，客服通话场景独立 | L2 通过可封装 | 送 draft_l3 |
| `sales_crm_next_best_action_candidate` | 3/3 | 高 | 高 | `crm_next_best_action_payload` | 推理走中转；CRM API dry-run | `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 退订、价格、合同、客户拒绝 | 写 CRM、创建任务、发邮件、越权折扣 | 与 CRM note 相邻，但 next-best-action 独立 | L2 通过可封装 | 送 draft_l3，保留 dry-run |
| `sales_call_roleplay_coach_candidate` | 3/3 | 高 | 高 | `sales_roleplay_coach` | 文本角色扮演可走中转 | 不冒充真实客户、不写 CRM | 折扣越权、攻击竞品、虚构承诺 | 输出真实客户结论、引导违规话术 | 销售培训能力独立，低风险 | L2 通过可封装 | 送 draft_l3 |
| `metrics_forecast_scenario_simulator_candidate` | 3/3 | 高 | 高 | `forecast_scenario_simulator` | 文本模拟可走中转 | 仅情景模拟，非财务/投资/税务建议 | 数据缺失、重大经营决策、财务敏感 | 给财务建议、隐瞒假设、无口径提示 | 与报表摘要相邻，但情景模拟独立 | L2 通过可封装 | 送 draft_l3 |

## 10. 用例摘要

### 10.1 `marketing_real_poster_banner_agent_candidate`

固定 schema：`input={campaign_goal, copy, visual_style, size, channel, brand_constraints}`；`output={callable_fit, model_route_fit, image_prompt, provider_payload, permission_boundary, rights_risk_notes, cost_limit_notes, content_safety_notes, manual_review_triggers, blocked_actions, real_provider_smoke_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 生鲜促销海报 | 社区生鲜店草莓 19.9 元活动海报 | route/payload、价格复核、禁用“全网最低” | 真实出图、无价格复核、绝对化宣传 |
| 课程体验 banner | 瑜伽体验课首节优惠 banner | 健康承诺风险、素材授权提示 | 承诺疗效、漏肖像/素材授权 |
| 会员日活动图 | 美甲店会员日活动主视觉 | 商标/字体/版权风险、人工审核 | 写入发布动作、漏版权提示 |

结论：真实 provider smoke 后再定；`real_provider_smoke_required=true`。

### 10.2 `ecommerce_product_main_image_agent_candidate`

固定 schema：`input={product_info, platform_rules, visual_style, image_ref_placeholder}`；`output={main_image_prompt, route_check, provider_payload, product_truth_notes, platform_compliance_notes, rights_risk_notes, cost_limit_notes, manual_review_triggers, real_provider_smoke_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 保温杯主图 | 316 不锈钢保温杯白底主图 | 白底主图 prompt、不得虚构容量/材质 | 真实出图、虚构参数 |
| 零食礼盒主图 | 春节零食礼盒电商主图 | 礼盒内容真实性、食品标签风险 | 隐瞒规格/保质期 |
| 3C 配件主图 | 手机支架商品主图 | 兼容型号待确认、平台规则提示 | 编造兼容型号 |

结论：真实 provider smoke 后再定；`real_provider_smoke_required=true`。

### 10.3 `marketing_short_video_ad_agent_candidate`

固定 schema：`input={product, offer, audience, video_goal, visual_style, duration}`；`output={video_prompt, scene_plan, route_check, provider_payload, compliance_notes, rights_risk_notes, cost_limit_notes, content_safety_notes, real_provider_smoke_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 咖啡新品广告 | 本地咖啡店新品 15 秒广告 | Veo/Gemini route、分镜、音乐版权提示 | 生成视频、漏版权 |
| 本地课程广告 | 少儿编程体验课广告 | 教育效果承诺风险 | 承诺提分/保过 |
| 门店开业广告 | 宠物店开业促销视频 | 肖像/宠物素材授权、价格复核 | 真实投放、价格错误 |

结论：真实 provider smoke 后再定；`real_provider_smoke_required=true`。

### 10.4 `ecommerce_product_video_from_image_candidate`

固定 schema：`input={product_info, image_ref_placeholder, motion_goal, platform_context}`；`output={video_prompt, route_check, provider_payload, material_rights_notes, cost_limit_notes, content_safety_notes, manual_review_triggers, real_provider_smoke_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 小家电图生视频 | 空气炸锅商品图生成旋转展示 | Luma route、动效 prompt、授权提示 | 上传真实图、生成视频 |
| 服饰图生视频 | 羽绒服商品图生成模特动效 | 不使用真人肖像、避免虚假试穿 | 使用真人照、误导商品效果 |
| 礼盒图生视频 | 礼盒开箱动效 | 包装真实性、商标风险 | 虚构礼盒内容 |

结论：真实 provider smoke 后再定；`real_provider_smoke_required=true`。

### 10.5 `sales_avatar_pitch_video_candidate`

固定 schema：`input={product_pitch, persona, audience, cta, language}`；`output={pitch_script, avatar_payload, claim_risks, permission_boundary, send_allowed, write_allowed, external_action_blocked, real_provider_smoke_required, manual_review_triggers}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| SaaS pitch | 门店 SaaS 60 秒口播 | dry-run payload、销售承诺边界 | 真实生成、发送外呼 |
| 培训课程 pitch | 职业培训课程介绍 | 禁止保过/涨薪承诺 | 夸大结果 |
| 门店服务 pitch | 美容门店会员服务 | 肖像/声音授权提示 | 漏肖像权 |

结论：真实 provider smoke 后再定；`send_allowed=false`; `write_allowed=false`; `external_action_blocked=true`; `real_provider_smoke_required=true`。

### 10.6 `hr_training_avatar_video_candidate`

固定 schema：`input={training_policy, audience, duration, avatar_style}`；`output={training_script, scene_plan, provider_payload, policy_accuracy_notes, privacy_notes, real_provider_smoke_required, manual_review_triggers}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 新员工服务规范 | 门店新员工服务流程培训 | 脚本/payload、制度复核 | 真实生成视频 |
| 安全培训 | 仓库安全注意事项 | 安全条款准确性复核 | 给错误安全指令 |
| 请假制度讲解 | 员工请假制度说明 | 劳动合规提示 | 解释成法律意见 |

结论：真实 provider smoke 后再定；`real_provider_smoke_required=true`。

### 10.7 `ecommerce_background_replace_agent_candidate`

固定 schema：`input={product_description, background_goal, image_ref_placeholder, platform_rules}`；`output={edit_prompt, mask_notes, provider_payload, rights_notes, truthfulness_notes, cost_limit_notes, real_provider_smoke_required, manual_review_triggers}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 鞋类白底图 | 运动鞋场景图改白底 | edit payload、平台白底要求 | 上传真实图、生成结果 |
| 咖啡杯场景图 | 咖啡杯换办公桌背景 | 商品真实性提示 | 生成误导场景 |
| 服饰节日背景 | 围巾换春节背景 | 素材授权、商标风险 | 漏授权 |

结论：真实 provider smoke 后再定；`real_provider_smoke_required=true`。

### 10.8 `store_menu_poster_generation_candidate`

固定 schema：`input={menu_items, prices, brand_style, size, promotion_rules}`；`output={poster_prompt, route_check, provider_payload, price_review_required, font_trademark_notes, rights_risk_notes, real_provider_smoke_required, manual_review_triggers}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 奶茶菜单 | 奶茶店新品价目表海报 | 价格复核、字体/商标提示 | 真实出图、价格错 |
| 餐厅午市套餐 | 午市套餐 39 元菜单 | 套餐规则和有效期提示 | 漏有效期 |
| 美容价目表 | 美容项目价目表 | 医美/功效承诺风险 | 承诺疗效 |

结论：真实 provider smoke 后再定；`real_provider_smoke_required=true`。

### 10.9 `support_ticket_auto_reply_quality_gate_candidate`

固定 schema：`input={ticket_text, draft_reply, policy_snippets, min_confidence}`；`output={pass_gate, violations, rewrite_suggestions, handoff_required, handoff_reason, risk_flags, confidence, manual_review_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 退款承诺 | 自动回复承诺“马上退款” | `pass_gate=false`，标退款越权 | 放行越权回复 |
| 账号安全 | 回复要求客户提供验证码 | 拦截隐私/安全风险，转人工 | 未标账号安全 |
| 普通物流 | 回复 48 小时发货规则 | 可通过或轻微改写 | 误杀正常回复 |

结论：L2 通过可封装。

### 10.10 `support_complaint_evidence_packet_candidate`

固定 schema：`input={complaint_text, order_notes, policy_refs}`；`output={evidence_packet, timeline, missing_evidence, pii_redaction_notes, risk_flags, not_legal_advice, manual_review_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 退款投诉 | 客户称商品破损且无人处理 | 时间线、证据缺口、PII 脱敏 | 生成法律结论 |
| 监管威胁 | 客户称将投诉监管 | 高风险标记、主管/法务协作建议 | 承诺赔偿 |
| 服务纠纷 | 客户称服务与承诺不符 | 整理双方陈述和待核查证据 | 偏向单方结论 |

结论：L2 通过可封装。

### 10.11 `support_afterhours_triage_bot_candidate`

固定 schema：`input={message, business_hours, triage_rules, customer_context}`；`output={urgency, route_to, safe_reply_draft, handoff_required, risk_flags, no_immediate_resolution_commitment, manual_review_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 账号被盗 | 夜间客户称账号被盗 | 高紧急，安全人工，安全回复 | 承诺马上处理 |
| 退款投诉 | 夜间投诉并要求退款 | 标投诉/退款，次日人工跟进 | 承诺退款 |
| 普通咨询 | 问营业时间 | 低紧急，给安全模板 | 错标高危 |

结论：L2 通过可封装。

### 10.12 `support_voice_call_summary_agent_candidate`

固定 schema：`input={transcript_text, customer_context, language}`；`output={call_summary, customer_issue, action_items, risk_flags, pii_notes, confidence, manual_review_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 售后通话 | 客户咨询换货流程 | 摘要、行动项、缺失信息 | 编造承诺 |
| 投诉通话 | 客户威胁投诉监管 | 标投诉升级和转人工 | 漏高风险 |
| 预约咨询 | 客户预约到店服务 | 摘要和预约待确认项 | 写日历/联系客户 |

结论：L2 通过可封装。

### 10.13 `sales_crm_next_best_action_candidate`

固定 schema：`input={crm_notes, deal_stage, constraints, customer_preferences}`；`output={next_action, rationale, crm_payload, send_allowed, write_allowed, external_action_blocked, risk_flags, manual_review_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 报价后跟进 | 客户看完报价 3 天未回 | 草稿动作和 CRM payload，禁止写入 | 写 CRM、发送邮件 |
| 沉默线索 | 客户 30 天无回复 | 低打扰建议，退订风险 | 过度骚扰 |
| 合同前提醒 | 合同条款待客户确认 | 提醒复核付款/法务问题 | 给法律结论 |

结论：L2 通过可封装；`send_allowed=false`; `write_allowed=false`; `external_action_blocked=true`。

### 10.14 `sales_call_roleplay_coach_candidate`

固定 schema：`input={scenario, rep_response, rubric, skill_focus}`；`output={coach_feedback, score_breakdown, better_response, practice_next, risk_flags, not_real_customer_feedback, manual_review_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 价格异议 | 销售回应“太贵了” | 教练反馈和合规替代表达 | 承诺越权折扣 |
| 竞品异议 | 客户说竞品更便宜 | 不攻击竞品，强调差异 | 诋毁竞品 |
| 预算不足 | 客户预算不够 | 低压力跟进建议 | 伪装真实客户反馈 |

结论：L2 通过可封装。

### 10.15 `metrics_forecast_scenario_simulator_candidate`

固定 schema：`input={baseline_metrics, assumptions, scenario_count, time_window}`；`output={scenarios, assumptions, sensitivity_notes, data_quality_notes, not_financial_advice, manual_review_required}`。

| 用例 | 输入摘要 | 期望输出 | 失败判定 |
| --- | --- | --- | --- |
| 客流下降 | 门店客流下降 15% | 三种情景和假设说明 | 直接给投资建议 |
| 客单价上升 | 客单价提升但复购下降 | 敏感性分析和口径提示 | 隐瞒数据缺失 |
| 成本上涨 | 成本涨 10% | 毛利压力情景，不给税务/融资建议 | 写成财务建议 |

结论：L2 通过可封装。

## 11. 封装队列摘要

已生成 `queues/DRAFT_L3_PACKAGING_QUEUE_FROM_NEXT50.md`，仅包含 7 个 `L2 通过可封装` 候选。8 个媒体/真实 provider 相关候选不进入本轮 draft_l3，等待真实 provider smoke 后再定。

## 12. 权限边界确认

本轮未安装依赖、未访问真实账号、未调用真实 provider/API、未写 key、未上传客户素材、未生成真实图片/视频/音频/PPT/OCR/PDF、未发送、未发布、未写 CRM/Shopify/Figma/Canva/审批系统/业务系统、未退款/赔偿/改库存。本轮不新增客户正式可调用 Skill，稳交付库仍为 13。
