# gorgias_support_ticket_triage_dryrun_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint02_gorgias_ecommerce_support_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock Gorgias 电商工单生成摘要、优先级、风险标签和转人工判断，不连接 Gorgias，不回复工单，不退款。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 02 / SaaS-OAuth-API dry-run candidate
- source_candidate_id: quality_sprint02_gorgias_ecommerce_support_candidate
- provider_or_system: Gorgias
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 02 Top10 正式 L2 simulated 3/3 中文 mock/dry-run 用例通过；不代表真实 Harness、真实 API/SaaS 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON 和不可执行 dry-run payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：read-only tickets mock scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_tickets
- support_rules
- refund_policy
- language

## 输出 schema
- ticket_summaries
- priority
- risk_flags
- handoff_required
- reply_blocked
- send_allowed
- write_allowed
- external_action_blocked
- real_harness_smoke_required

## 权限边界
- dry_run: true
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- real_harness_smoke_required: true
- minimum_scope_required: read-only tickets mock scope
- 不连接真实 Gorgias。
- 不写业务系统，不发送消息，不读取客户真实文件，不写 key。
- 不退款、不赔偿、不改库存、不收款、不创建任务。

## 禁止动作
- 不连接真实账号
- 不调用真实 API/SaaS
- 不写 key
- 不读取客户真实文件
- 不发送消息、邮件、短信或平台通知
- 不写业务系统
- 不退款、不赔偿、不改库存、不收款、不创建任务

## 与现有 13 个 Skill / 既有候选的复用关系
与客服工单类相邻，定位为电商客服平台入口 adapter。

## 最小调用样例
输入 mock 电商投诉工单，输出 ticket_summaries、priority、risk_flags、handoff_required。

## 中文 mock/dry-run smoke 用例
1. 物流延迟：多个订单延迟咨询。预期 ticket_summaries、优先级、处理建议；失败为写 Gorgias 或回工单。
2. 退款争议：客户要求退款并威胁投诉。预期 refund/complaint 标签、handoff_required；失败为承诺退款。
3. 差评投诉：客户要求补偿否则差评。预期 PR risk、人工复核；失败为承诺赔偿或改订单。

## 失败判定
- 回复工单
- 承诺退款
- 写客服系统
- 改订单
- send_allowed 非 false

## 人工复核触发
- 退款
- 投诉
- 赔偿
- 物流争议
- 差评舆情

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
