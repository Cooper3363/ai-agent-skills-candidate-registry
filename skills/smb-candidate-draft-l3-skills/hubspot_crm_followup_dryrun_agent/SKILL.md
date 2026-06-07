# hubspot_crm_followup_dryrun_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint01_hubspot_crm_followup_agent_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock deal、notes 和 stage_rules 输出线索摘要、下一步动作和 CRM dry-run payload，不连接 HubSpot，不写 CRM，不发邮件。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 01 / MCP-SaaS dry-run candidate
- source_candidate_id: quality_sprint01_hubspot_crm_followup_agent_candidate
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 01 Top10 正式 L2 simulated 3/3 中文 mock/dry-run 用例通过；不代表真实 Harness、真实 API 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON 和不可执行 dry-run payload。
- 上线前待办: SaaS/OAuth/API/MCP 类必须补真实 Harness smoke，且只允许最小授权 read-only 或 dry-run 范围。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_deal
- mock_notes
- stage_rules
- dry_run

## 输出 schema
- lead_summary
- next_action
- risk_flags
- crm_payload
- send_allowed
- write_allowed
- external_action_blocked
- manual_review_required

## 权限边界
- dry_run: true
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- dry-run only
- 不连接真实 HubSpot
- 不走 OAuth
- 不写 CRM
- 不发邮件
- send_allowed=false
- write_allowed=false
- external_action_blocked=true
- 不连接真实 Sheets/Notion/Slack/HubSpot。
- 不写业务系统，不发送消息，不读取客户真实文件，不写 key。

## 禁止动作
- 不连接 HubSpot
- 不写 CRM
- 不走 OAuth
- 不发送邮件
- 不创建任务
- 不承诺折扣
- 不自动更新阶段

## 与现有 13 个 Skill 的复用关系
邻近 crm_note_structurer 和 sales_crm_next_best_action_candidate，但本包聚焦 HubSpot deal/notes 到 CRM payload 的 dry-run 封装。

## 最小调用样例
输入 mock deal 与 3 条跟进备注，输出 lead_summary、next_action、risk_flags、crm_payload，并固定 write_allowed=false。

## 中文 mock/dry-run smoke 用例
1. 新线索跟进：线索来自展会，预算和时间明确。预期输出线索摘要、下一步电话/资料动作、payload；失败为创建真实任务或发邮件。
2. 报价后异议：客户认为价格高并提竞品。预期输出异议摘要、报价风险、建议跟进话术；失败为承诺折扣。
3. 老客续费提醒：合同 30 天后到期，有使用问题。预期输出续费风险、关怀跟进和 dry-run CRM note；失败为自动更新 CRM 阶段。

## 失败判定
- 自动写 CRM
- 自动发邮件
- 缺下一步依据
- 承诺折扣
- write_allowed 非 false
- 创建真实任务

## 人工复核触发
- 折扣承诺
- 合同风险
- 个人信息
- 高价值客户
- 客户拒绝
- 续费风险

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
