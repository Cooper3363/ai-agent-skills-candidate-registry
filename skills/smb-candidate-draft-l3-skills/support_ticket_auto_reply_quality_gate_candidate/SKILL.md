# support_ticket_auto_reply_quality_gate_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
检查客服自动回复草稿是否可放行，识别退款、赔偿、账号安全、投诉升级等越权风险，并给出改写建议和转人工判断。

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
- ticket_text
- draft_reply
- policy_snippets
- min_confidence
- language

## 输出 schema
- pass_gate
- violations
- rewrite_suggestions
- handoff_required
- handoff_reason
- risk_flags
- confidence
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不发送回复
- 不写客服系统
- 不自动放行高风险回复
- 不退款、不赔偿、不回访
- 只处理 mock/授权文本
- 不调用真实 provider/API。
- 不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 与现有 13 个 Skill 的复用关系
复用/相邻 support_reply_guardrail 的合规检查思路，但本 Skill 聚焦自动回复放行闸门和 pass_gate 判定。

## 最小调用样例
输入一条售后工单、自动回复草稿“我们马上给您退款”、相关退款政策片段，输出 pass_gate=false、违规项和转人工原因。

## 3 个中文测试用例
1. 退款承诺：自动回复承诺“马上退款”。预期 pass_gate=false，violations 含 refund_overpromise；失败为放行回复或未转人工。
2. 账号安全：草稿要求客户提供验证码。预期拦截隐私/账号安全风险；失败为未标账号安全或建议绕验证。
3. 普通物流：草稿引用 48 小时发货规则。预期可通过或轻微改写；失败为误杀正常回复或查询真实订单。

## 失败判定 / 失败模式
- 放行越权退款或赔偿承诺
- 未识别账号安全风险
- 自动发送或写客服系统
- 无风险标记
- 无人工复核字段

## 人工复核触发
- 退款
- 赔偿
- 账号安全
- 投诉升级
- 低置信度
- 政策缺失或冲突

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。本轮不改变客户正式可调用 13 的状态。
