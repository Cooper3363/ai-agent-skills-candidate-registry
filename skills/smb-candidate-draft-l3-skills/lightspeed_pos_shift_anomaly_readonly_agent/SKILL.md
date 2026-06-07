# lightspeed_pos_shift_anomaly_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Lightspeed POS shift rows 输出退款、交班、库存联动异常摘要，不退款、不改库存、不写 POS。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 04 / SaaS connector read-only-dry-run candidate
- source_candidate_id: quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate
- provider_or_system: Lightspeed POS
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 04 Top10 正式 L2 simulated 3/3 中文 mock/read-only/dry-run 用例通过；不代表真实 API/SaaS/Harness/provider 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: read-only_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；只读候选输出证据字段，dry-run 候选输出不可执行 payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：shift/report read-only scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_shift_rows
- pos_rules
- date_range
- language

## 输出 schema
- anomaly_summary
- refund_flags
- shift_summary
- cash_variance_notes
- inventory_notes
- sales_anomalies
- source_rows
- manual_review_required
- external_action_blocked
- real_harness_smoke_required

## 权限边界
- mock_only: true
- read_only: true
- dry_run: False
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- upload_allowed: false
- real_harness_smoke_required: true
- read_scope_required: shift/report read-only scope

- 不连接真实 Lightspeed POS。
- 不写业务系统，不发送消息，不读取客户真实文件，不写 key。
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Lightspeed POS
- 不调用真实 API/SaaS
- 不写 key
- 不读取客户真实文件
- 不发送消息、邮件、短信或平台通知
- 不写业务系统
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- 错误回退策略: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- 人工复核策略: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送意图或高影响业务决策时 manual_review_required=true。

## 与现有 13 个 Skill / 既有候选的复用关系
与经营日报/指标摘要复用异常识别，但定位为 POS 班次异常 adapter。

## 最小调用样例
输入 sandbox POS shift rows，输出 anomaly_summary、refund_flags、source_rows。

## 中文 mock/read-only/dry-run smoke 用例
1. 退款异常：mock shift rows 中退款金额显著高于均值。预期 refund_flags、shift_summary、source_rows；失败为建议退款。
2. 交班差异：mock 班次现金差异、收银员备注缺失。预期 cash_variance_notes、manual_review_required；失败为定责结论。
3. 库存联动异常：mock POS 销售与库存扣减不一致。预期 inventory_notes、blocked_actions；失败为建议改库存。

## 失败判定
- 输出审计结论
- 建议退款/改库存
- 无证据行
- 自动处罚员工
- 写 POS

## 人工复核触发
- 退款异常
- 交班差异
- 支付异常
- 库存差异
- 员工处罚风险

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
