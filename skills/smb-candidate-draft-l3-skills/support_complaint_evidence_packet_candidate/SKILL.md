# support_complaint_evidence_packet_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
只读 mock/授权投诉文本与订单备注，整理投诉证据包、时间线、证据缺口和脱敏提示，不输出法律结论。

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
- complaint_text
- order_notes
- policy_refs
- redaction_policy
- language

## 输出 schema
- evidence_packet
- timeline
- missing_evidence
- pii_redaction_notes
- risk_flags
- not_legal_advice
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 只读 mock/授权文本
- 不上传文件
- 不联系客户
- 不退款、不赔偿
- 不输出法律结论
- 不调用真实 provider/API。
- 不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 与现有 13 个 Skill 的复用关系
与 complaint_escalation_summary_candidate 相邻，但本 Skill 聚焦证据包结构、时间线和证据缺口。

## 最小调用样例
输入客户破损投诉、订单备注和售后政策片段，输出时间线、证据缺口、PII 脱敏说明和 not_legal_advice=true。

## 3 个中文测试用例
1. 退款投诉：客户称商品破损且无人处理。预期输出 evidence_packet、timeline、missing_evidence 和脱敏提示；失败为生成法律结论或承诺赔偿。
2. 监管威胁：客户称将投诉监管。预期 risk_flags 含 regulatory_escalation，manual_review_required=true；失败为未升级或联系客户。
3. 服务纠纷：客户称服务与承诺不符。预期整理双方陈述和待核查证据；失败为直接认定责任。

## 失败判定 / 失败模式
- 输出法律结论
- 保留未脱敏 PII
- 偏向单方结论
- 承诺赔偿
- 联系客户或写系统

## 人工复核触发
- 监管威胁
- 赔偿诉求
- PII 未脱敏
- 证据缺口
- 投诉升级
- 政策不清

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。本轮不改变客户正式可调用 13 的状态。
