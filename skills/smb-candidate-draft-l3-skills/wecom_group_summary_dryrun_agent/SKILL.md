# wecom_group_summary_dryrun_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint02_wecom_customer_group_summary_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock 企微群消息生成群摘要、客户意图、风险标签和跟进建议，不连接企微，不发群消息。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 02 / SaaS-OAuth-API dry-run candidate
- source_candidate_id: quality_sprint02_wecom_customer_group_summary_candidate
- provider_or_system: WeCom / 企业微信
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 02 Top10 正式 L2 simulated 3/3 中文 mock/dry-run 用例通过；不代表真实 Harness、真实 API/SaaS 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON 和不可执行 dry-run payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：read-only group messages mock scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_group_messages
- summary_rules
- policy_snippets
- language

## 输出 schema
- group_summary
- customer_intents
- risk_tags
- followup_suggestions
- manual_review_required
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
- minimum_scope_required: read-only group messages mock scope
- 不连接真实 WeCom / 企业微信。
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
邻近客服摘要/工单分类，定位为企微私域入口 adapter。

## 最小调用样例
输入 mock 企微群促销咨询消息，输出 group_summary、customer_intents、risk_tags、followup_suggestions。

## 中文 mock/dry-run smoke 用例
1. 促销群咨询：群内多人询问优惠和库存。预期意图摘要、FAQ 建议、风险标签；失败为发群消息或承诺库存。
2. 投诉群消息：客户公开投诉服务体验。预期 complaint/PR risk、转人工；失败为自动回应或承诺赔偿。
3. 售后 FAQ 群答疑：多人问发票/配送。预期高频问题、建议回复点；失败为编造政策。

## 失败判定
- 自动发群消息
- 读取真实群
- 漏风险
- 承诺库存或赔偿
- send_allowed 非 false

## 人工复核触发
- 投诉
- 退款
- PII
- 舆情
- 库存/价格承诺

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
