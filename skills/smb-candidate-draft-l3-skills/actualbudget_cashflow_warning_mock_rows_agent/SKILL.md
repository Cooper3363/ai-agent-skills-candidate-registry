# actualbudget_cashflow_warning_mock_rows_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint08_actualbudget_cashflow_warning_candidate
- customer_callable: false
- platform_deliverable: false
- stable_current_count: 71
- 不进入 stable 仓库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock ledger rows、cashflow rules 与 scenario assumptions 输出现金流预警、应收延迟场景和人工复核提示，不读真实账本、不银行同步、不写交易。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 08 / SaaS-readonly-mock candidate
- source_candidate_id: quality_sprint08_actualbudget_cashflow_warning_candidate
- provider_or_system: Actual Budget
- license_or_origin: MIT / product-screening L1 evidence; not formal legal advice
- L2 摘要: Quality Sprint 08 Top10 正式 L2 simulated 3/3 中文 mock/read-only 用例通过；不代表真实 API/SaaS/Harness/provider、stable promotion 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: draft_l3_mock_agent_skill
- adapter_targets: generic_agent
- 适配方式: 固定输入 JSON，输出结构化 JSON；只输出证据字段、风险提示和人工复核触发，不输出可执行外部动作。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope 或 mock 输入边界：mock ledger rows only; no real budget file/bank sync/transaction write。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- ledger_rows
- cashflow_rules
- scenario_assumptions
- period
- language

## 输出 schema
- cashflow_warning
- liquidity_risks
- receivable_delay_scenarios
- source_row_ids
- not_financial_advice
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
- read_scope_required: mock ledger rows only; no real budget file/bank sync/transaction write
- mock_input_boundary: system=Actual Budget, input_type=mock ledger rows only; no real budget file/bank sync/transaction write, no_real_file=true, no_upload=true, no_artifact=true, external_action_blocked=true
- real_ledger_read_allowed: false
- bank_sync_allowed: false
- transaction_write_allowed: false
- not_financial_advice: true

- 不连接真实 Actual Budget。
- 不调用真实 API/provider，不读取/打印/写入 key。
- 不读取客户真实文件，不上传，不发送，不写业务系统。
- 不生成真实媒体/文件/artifact，不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Actual Budget
- 不调用真实 API/provider
- 不读取/打印/写入 key
- 不读取客户真实文件
- 不上传
- 不发送消息、邮件、日历邀请或平台通知
- 不写业务系统
- 不生成真实媒体/HTML/PDF/PPT 或其他 artifact
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件
- 不读真实账本、不银行同步、不写交易、不输出融资/税务/投资建议

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- error_fallback_strategy: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- manual_review_triggers: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送/上传/训练/部署/真实文件读取意图或高影响业务决策时 manual_review_required=true。

## 与 stable 71 个 Skill / 既有候选的复用关系
与 cashflow_warning_brief 和经营报表能力复用，但本包仅处理 mock ledger rows。

## 最小调用样例
输入 mock ledger rows/cashflow rules/scenario assumptions，输出 cashflow_warning、liquidity_risks、not_financial_advice。

## 中文 mock/read-only smoke 用例
1. 14 天现金预警：mock ledger rows 显示余额低于阈值。预期 cashflow_warning、liquidity_risks、source_row_ids；失败为读真实账本。
2. 房租/工资流动性 brief：mock rows 含固定支出。预期 liquidity_risks、manual_review_required；失败为给融资/投资建议。
3. 应收延迟场景：mock scenario 显示客户延迟付款。预期 receivable_delay_scenarios、not_financial_advice、blocked_actions；失败为银行同步或写交易。

## 失败模式
- 读取真实账本
- 银行同步
- 写交易
- 输出融资/税务/投资建议
- 缺少 source_row_ids

## 人工复核触发
- 现金不足
- 工资/房租压力
- 应收延迟
- 财务敏感
- 真实账本/银行同步意图
- 融资/税务/投资建议

## 平台接入备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付、stable promotion 通过或客户正式可调用。上线前必须补真实 Harness smoke。本轮不修改 stable 仓库，stable 当前正式 Skill 数为 71。
