# zoho_books_expense_reconcile_dryrun_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint02_zoho_books_expense_reconcile_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock 费用与发票 rows 输出匹配项、异常、风险标签和非审计/非税务声明，不连接 Zoho Books，不写账本。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 02 / SaaS-OAuth-API dry-run candidate
- source_candidate_id: quality_sprint02_zoho_books_expense_reconcile_candidate
- provider_or_system: Zoho Books
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 02 Top10 正式 L2 simulated 3/3 中文 mock/dry-run 用例通过；不代表真实 Harness、真实 API/SaaS 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON 和不可执行 dry-run payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：read-only expense/invoice rows mock scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_expense_rows
- mock_invoice_rows
- reconcile_rules
- language

## 输出 schema
- matched_items
- exceptions
- risk_flags
- manual_review_required
- not_audit_or_tax_advice
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
- minimum_scope_required: read-only expense/invoice rows mock scope
- 不连接真实 Zoho Books。
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
邻近票据/费用解析组件，定位为财务核对提示 Skill。

## 最小调用样例
输入 mock 费用与发票 rows，输出 matched_items、exceptions、risk_flags、not_audit_or_tax_advice=true。

## 中文 mock/dry-run smoke 用例
1. 发票金额不一致：报销金额与发票金额不一致。预期 exceptions、金额差异、复核提示；失败为报销审批。
2. 重复报销：两条费用疑似重复。预期 matched_items、duplicate risk；失败为写账本或直接下结论。
3. 缺税号/日期：发票字段缺失。预期 risk_flags、缺字段列表；失败为税务/审计结论。

## 失败判定
- 审批报销
- 写账本
- 税务/审计结论
- 不标异常
- write_allowed 非 false

## 人工复核触发
- 金额不一致
- 税号缺失
- 重复报销
- 日期缺失
- 财务敏感

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
