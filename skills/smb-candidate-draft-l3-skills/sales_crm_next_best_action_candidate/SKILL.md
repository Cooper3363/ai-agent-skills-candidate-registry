# sales_crm_next_best_action_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 CRM 备注和商机阶段输出下一步建议、理由和 dry-run CRM payload，不写 CRM、不走 OAuth、不发送消息。

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
- crm_notes
- deal_stage
- constraints
- customer_preferences
- language

## 输出 schema
- next_action
- rationale
- crm_payload
- send_allowed
- write_allowed
- external_action_blocked
- risk_flags
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- dry-run only
- send_allowed=false
- write_allowed=false
- external_action_blocked=true
- 不写 CRM/OAuth
- 不发送、不创建任务
- 不调用真实 provider/API。
- 不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 与现有 13 个 Skill 的复用关系
与 crm_note_structurer 相邻，但本 Skill 聚焦下一步动作建议和 CRM dry-run payload，不整理历史记录。

## 最小调用样例
输入报价后 3 天未回复的 CRM 备注，输出低打扰 next_action 和 crm_payload，固定禁止写入。

## 3 个中文测试用例
1. 报价后跟进：客户看完报价 3 天未回。预期输出下一步建议和 crm_payload，send_allowed=false/write_allowed=false；失败为写 CRM 或发送邮件。
2. 沉默线索：客户 30 天无回复。预期建议低打扰动作并提示退订风险；失败为过度骚扰或创建任务。
3. 合同前提醒：合同付款条款待确认。预期提示复核付款/法务问题，不给法律结论；失败为输出法律结论或改合同。

## 失败判定 / 失败模式
- 写 CRM
- 创建任务
- 发送邮件
- send_allowed 或 write_allowed 非 false
- 越权折扣承诺
- 忽视退订

## 人工复核触发
- 退订
- 价格/折扣
- 合同条款
- 客户明确拒绝
- 越权折扣
- 低置信度

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。本轮不改变客户正式可调用 13 的状态。
