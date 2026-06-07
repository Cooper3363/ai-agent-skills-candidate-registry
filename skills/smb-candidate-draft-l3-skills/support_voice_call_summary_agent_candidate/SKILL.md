# support_voice_call_summary_agent_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
对 mock 或已转文本的客服通话 transcript 生成摘要、客户问题、行动项和风险提示，不读取真实音频、不做 ASR、不写工单。

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
- transcript_text
- customer_context
- summary_policy
- language

## 输出 schema
- call_summary
- customer_issue
- action_items
- risk_flags
- pii_notes
- confidence
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 只处理 mock/已转文本输入
- 不读取真实音频
- 不上传音频
- 不做 ASR
- 不写工单/日历/任务
- 不调用真实 provider/API。
- 不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 与现有 13 个 Skill 的复用关系
与销售会议摘要组件相邻，但本 Skill 专用于客服通话 transcript 的问题、风险和行动项摘要。

## 最小调用样例
输入一段已转文本的售后通话 transcript，输出 call_summary、customer_issue、action_items、pii_notes。

## 3 个中文测试用例
1. 售后通话：客户咨询换货流程。预期输出摘要、行动项和缺失信息；失败为编造承诺或读取音频。
2. 投诉通话：客户威胁投诉监管。预期 risk_flags 含 complaint_escalation；失败为漏高风险。
3. 预约咨询：客户预约到店服务。预期输出预约待确认项，不写日历；失败为写日历或联系客户。

## 失败判定 / 失败模式
- 编造通话内容
- 漏行动项
- 保留未脱敏 PII
- 写工单或任务
- 读取真实音频

## 人工复核触发
- PII
- 投诉
- 退款承诺
- 行动项缺失
- 低置信度
- 客户敏感信息

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。本轮不改变客户正式可调用 13 的状态。
