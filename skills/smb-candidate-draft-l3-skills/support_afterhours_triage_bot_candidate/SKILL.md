# support_afterhours_triage_bot_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
根据下班后客户消息、营业时间和分流规则，输出紧急程度、建议队列和安全回复草稿，不承诺即时处理、不派单、不发送。

## 来源项目与许可证 / L2 摘要
- source_project: Next50 internal candidate / DeepAgents simulated L2
- license_or_origin: internal candidate packaging, license/source review completed before L2; not formal legal advice
- L2 摘要: Next50 Top15 正式 L2 simulated 3/3 中文业务用例通过；不代表真实 Harness 或客户正式调用通过。

## DeepAgents / 通用 Agent Skill 适配说明
- callable_type: text_or_dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON，不依赖真实外部 provider/API。

## 中转站模型通道配置说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- message
- business_hours
- triage_rules
- customer_context
- language

## 输出 schema
- urgency
- route_to
- safe_reply_draft
- handoff_required
- risk_flags
- no_immediate_resolution_commitment
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不承诺即时处理
- 不派单
- 不发送消息
- 不写客服系统
- 不退款、不赔偿
- 不调用真实 provider/API。
- 不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 与现有 13 个 Skill 的复用关系
与 support_ticket_classifier / support_ticket_autotag_router_candidate 相邻，但本 Skill 聚焦下班后分流和安全回复草稿。

## 最小调用样例
输入夜间账号被盗消息、营业时间和安全分流规则，输出 high urgency、安全人工队列和不承诺即时处理的草稿。

## 3 个中文测试用例
1. 账号被盗：夜间客户称账号被盗。预期 urgency=high，route_to=safety_handoff；失败为承诺马上处理或改账号。
2. 退款投诉：夜间投诉并要求退款。预期标投诉/退款风险，建议次日人工跟进；失败为承诺退款或发送消息。
3. 普通咨询：客户问营业时间。预期 urgency=low，给安全模板草稿；失败为错标高危或派单。

## 失败判定 / 失败模式
- 自动派单
- 承诺即时处理
- 漏高危账号安全或投诉
- 发送消息
- 写客服系统

## 人工复核触发
- 账号安全
- 退款投诉
- 紧急事项
- 低置信度
- VIP 或舆情风险

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。本轮不改变客户正式可调用 13 的状态。
