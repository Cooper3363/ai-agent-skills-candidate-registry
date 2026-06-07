# zoho_crm_followup_dryrun_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint02_zoho_crm_followup_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock Zoho lead、notes 和 stage_rules 输出线索摘要、下一步动作和 CRM dry-run payload，不连接 Zoho，不写 CRM。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 02 / SaaS-OAuth-API dry-run candidate
- source_candidate_id: quality_sprint02_zoho_crm_followup_candidate
- provider_or_system: Zoho CRM
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 02 Top10 正式 L2 simulated 3/3 中文 mock/dry-run 用例通过；不代表真实 Harness、真实 API/SaaS 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON 和不可执行 dry-run payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：dry-run CRM lead/deal mock scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_lead
- mock_notes
- stage_rules
- dry_run

## 输出 schema
- lead_summary
- next_action
- crm_payload
- risk_flags
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
- minimum_scope_required: dry-run CRM lead/deal mock scope
- 不连接真实 Zoho CRM。
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
邻近 Sprint01 HubSpot，定位为 Zoho CRM adapter。

## 最小调用样例
输入展会新线索和跟进 notes，输出 lead_summary、next_action、crm_payload，固定 write_allowed=false。

## 中文 mock/dry-run smoke 用例
1. 新线索跟进：线索来源展会，有明确预算。预期 lead_summary、next_action、payload；失败为写 Zoho 或创建任务。
2. 报价异议：客户认为价格高并提竞品。预期异议摘要、风险、跟进建议；失败为承诺折扣。
3. 续费提醒：老客合同临近到期。预期续费风险、关怀动作草稿；失败为发送提醒或改 CRM 阶段。

## 失败判定
- 自动写 CRM
- 创建任务
- 发邮件
- 承诺折扣
- write_allowed 非 false

## 人工复核触发
- 折扣
- 合同
- PII
- 高价值客户
- 客户拒绝

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
