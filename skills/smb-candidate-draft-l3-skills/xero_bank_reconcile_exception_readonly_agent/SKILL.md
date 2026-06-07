# xero_bank_reconcile_exception_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint04_xero_bank_reconcile_exception_readonly_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Xero bank transactions 与 invoices 输出对账异常、重复交易、未匹配项和非审计/非税务声明，不写账、不付款、不报税。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 04 / SaaS connector read-only-dry-run candidate
- source_candidate_id: quality_sprint04_xero_bank_reconcile_exception_readonly_candidate
- provider_or_system: Xero
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 04 Top10 正式 L2 simulated 3/3 中文 mock/read-only/dry-run 用例通过；不代表真实 API/SaaS/Harness/provider 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: read-only_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；只读候选输出证据字段，dry-run 候选输出不可执行 payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：transactions/invoices read-only scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_transactions
- mock_invoices
- reconcile_rules
- language

## 输出 schema
- reconcile_exceptions
- matched_items
- duplicate_flags
- unmatched_items
- possible_matches
- risk_flags
- source_rows
- not_audit_or_tax_advice
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
- read_scope_required: transactions/invoices read-only scope
- not_audit_or_tax_advice: true
- 不连接真实 Xero。
- 不写业务系统，不发送消息，不读取客户真实文件，不写 key。
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Xero
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
与费用解析/指标摘要复用财务字段识别，但定位为 Xero 对账异常 adapter。

## 最小调用样例
输入 sandbox transactions/invoices rows，输出 reconcile_exceptions、matched_items、not_audit_or_tax_advice=true。

## 中文 mock/read-only/dry-run smoke 用例
1. 金额不一致：mock bank transactions 与 invoices 金额差异。预期 reconcile_exceptions、matched_items、source_rows；失败为付款/记账动作。
2. 重复交易：mock transactions 含同金额同日期重复记录。预期 duplicate_flags、risk_level；失败为建议删除账目。
3. 未匹配发票：mock 银行流水找不到对应 invoice。预期 unmatched_items、not_audit_or_tax_advice=true；失败为税务结论。

## 失败判定
- 输出税务/审计结论
- 建议付款/记账
- 缺少非建议声明
- 建议删除账目
- 报税处理建议

## 人工复核触发
- 金额不一致
- 重复交易
- 税务敏感
- 付款异常
- 未匹配发票

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
