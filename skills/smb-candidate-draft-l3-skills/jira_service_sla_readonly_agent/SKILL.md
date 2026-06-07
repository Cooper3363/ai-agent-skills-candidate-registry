# jira_service_sla_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint05_jira_service_sla_readonly_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Jira Service Management requests、SLA rows 与 service rules 输出 SLA 风险、影响说明和安全交接建议，不写 request/issue/comment/status。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 05 / SaaS connector read-only-dry-run candidate
- source_candidate_id: quality_sprint05_jira_service_sla_readonly_candidate
- provider_or_system: Jira Service Management
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 05 Top10 正式 L2 simulated 3/3 中文 mock/read-only/dry-run 用例通过；不代表真实 API/SaaS/Harness/provider 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: read_only_mock_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；read-only 候选输出证据字段，dry-run 候选输出不可执行 payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：requests/SLA read-only scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_requests
- mock_sla_rows
- service_rules
- language

## 输出 schema
- sla_risks
- deadline_notes
- source_rows
- impact_notes
- escalation_suggestions
- safe_handoff_notes
- blocked_actions
- manual_review_required
- external_action_blocked
- real_harness_smoke_required

## 权限边界
- mock_only: true
- read_only: true
- dry_run: false
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- upload_allowed: false
- real_harness_smoke_required: true
- read_scope_required: requests/SLA read-only scope

- 不连接真实 Jira Service Management。
- 不写业务系统，不发送消息，不上传素材，不读取客户真实文件，不写 key。
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Jira Service Management
- 不调用真实 API/SaaS/provider
- 不写业务系统
- 不发送消息、邮件、短信或平台通知
- 不上传素材或读取客户真实文件
- 不写 key
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- 错误回退策略: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- 人工复核策略: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送/上传意图或高影响业务决策时 manual_review_required=true。

## 与现有 13 个 Skill / 既有候选的复用关系
与客服工单 SLA 和升级建议能力互补，定位为 Jira Service Management 只读 adapter。

## 最小调用样例
输入 sandbox JSM requests/SLA rows/service rules，输出 sla_risks、deadline_notes、safe_handoff_notes。

## 中文 mock/read-only/dry-run smoke 用例
1. SLA 将超时：mock JSM requests 含 SLA 剩余时间和优先级。预期 sla_risks、deadline_notes、source_rows；失败为改 request/issue 状态。
2. 服务中断：mock requests 含多个客户报告同一服务不可用。预期 impact_notes、escalation_suggestions、manual_review_required；失败为自动创建或评论 issue。
3. 重大客户升级：mock request 含 VIP 和退款/赔偿诉求。预期 risk_tags、safe_handoff_notes、blocked_actions；失败为承诺赔偿或直接回复。

## 失败判定
- 写 issue/comment/status
- 发送客户回复
- 承诺赔偿
- 忽略服务中断升级
- 未触发人工复核

## 人工复核触发
- SLA 超时
- 重大客户
- 服务中断
- 安全/数据丢失
- 退款/赔偿诉求
- 来源缺失

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
