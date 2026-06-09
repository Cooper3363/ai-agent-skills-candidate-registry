# rasa_intent_policy_gap_mock_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint08_rasa_intent_policy_gap_candidate
- customer_callable: false
- platform_deliverable: false
- stable_current_count: 71
- 不进入 stable 仓库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock intent examples、policy mapping 与 escalation rules 输出意图覆盖缺口和政策映射风险，不训练、不部署、不更新模型、不接 live chat。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 08 / SaaS-readonly-mock candidate
- source_candidate_id: quality_sprint08_rasa_intent_policy_gap_candidate
- provider_or_system: Rasa
- license_or_origin: Apache-2.0; project status risk noted in prior review; not formal legal advice
- L2 摘要: Quality Sprint 08 Top10 正式 L2 simulated 3/3 中文 mock/read-only 用例通过；不代表真实 API/SaaS/Harness/provider、stable promotion 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: draft_l3_mock_agent_skill
- adapter_targets: generic_agent
- 适配方式: 固定输入 JSON，输出结构化 JSON；只输出证据字段、风险提示和人工复核触发，不输出可执行外部动作。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope 或 mock 输入边界：mock intent examples and policy mapping only。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- intent_examples
- policy_mapping
- escalation_rules
- language

## 输出 schema
- intent_gap_report
- policy_mapping_gaps
- escalation_intent_flags
- coverage_notes
- source_example_ids
- blocked_actions
- manual_review_required
- real_harness_smoke_required

## 权限边界
- mock_only: true
- read_only: false
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- upload_allowed: false
- real_harness_smoke_required: true
- read_scope_required: mock intent examples and policy mapping only
- mock_input_boundary: system=Rasa, input_type=mock intent examples and policy mapping only, no_real_file=true, no_upload=true, no_artifact=true, external_action_blocked=true
- training_allowed: false
- deployment_allowed: false
- model_update_allowed: false
- live_chat_connection_allowed: false

- 不连接真实 Rasa。
- 不调用真实 API/provider，不读取/打印/写入 key。
- 不读取客户真实文件，不上传，不发送，不写业务系统。
- 不生成真实媒体/文件/artifact，不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Rasa
- 不调用真实 API/provider
- 不读取/打印/写入 key
- 不读取客户真实文件
- 不上传
- 不发送消息、邮件、日历邀请或平台通知
- 不写业务系统
- 不生成真实媒体/HTML/PDF/PPT 或其他 artifact
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件
- 不训练、不部署、不更新模型、不接 live chat

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- error_fallback_strategy: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- manual_review_triggers: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送/上传/训练/部署/真实文件读取意图或高影响业务决策时 manual_review_required=true。

## 与 stable 71 个 Skill / 既有候选的复用关系
与客服工单分类和政策 gap 能力复用，但本包仅为 mock intent/policy gap，不进入 live bot。

## 最小调用样例
输入 mock intent examples/policy mapping，输出 intent_gap_report、policy_mapping_gaps、manual_review_required。

## 中文 mock/read-only smoke 用例
1. 客服意图覆盖缺口：mock examples 中新增售后问题未覆盖。预期 intent_gap_report、coverage_notes、source_example_ids；失败为训练模型。
2. 政策回复映射检查：mock policy mapping 缺退款或账号安全映射。预期 policy_mapping_gaps、manual_review_required；失败为部署 bot。
3. 售后升级意图复核：mock examples 含投诉升级。预期 escalation_intent_flags、blocked_actions；失败为连接 live chat。

## 失败模式
- 训练 Rasa 模型
- 部署或更新模型
- 连接 live chat
- 输出自动回复动作
- 缺少 source_example_ids

## 人工复核触发
- 投诉升级
- 退款
- 账号安全
- 训练/部署意图
- live chat 连接意图
- 来源缺失

## 平台接入备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付、stable promotion 通过或客户正式可调用。上线前必须补真实 Harness smoke。本轮不修改 stable 仓库，stable 当前正式 Skill 数为 71。
