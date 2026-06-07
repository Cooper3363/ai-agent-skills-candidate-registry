# excel_metrics_report_dryrun_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint02_microsoft_excel_report_agent_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Excel rows 生成经营摘要、指标变化、异常说明和可追溯 source_rows，不连接真实 Graph/Excel，不读写真实文件。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 02 / SaaS-OAuth-API dry-run candidate
- source_candidate_id: quality_sprint02_microsoft_excel_report_agent_candidate
- provider_or_system: Microsoft Excel / Graph
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 02 Top10 正式 L2 simulated 3/3 中文 mock/dry-run 用例通过；不代表真实 Harness、真实 API/SaaS 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON 和不可执行 dry-run payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：read-only workbook rows scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_workbook_rows
- metric_schema
- date_range
- language

## 输出 schema
- summary
- metric_changes
- anomalies
- source_rows
- manual_review_required
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
- minimum_scope_required: read-only workbook rows scope
- 不连接真实 Microsoft Excel / Graph。
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
邻近经营报表类稳交付与 Sprint01 Sheets 候选，定位为 Excel adapter。

## 最小调用样例
输入 7 行门店销售 mock Excel rows，输出 summary、metric_changes、anomalies、source_rows。

## 中文 mock/dry-run smoke 用例
1. 门店周报：7 天销售额、订单数、客单价 mock rows。预期周报摘要、环比变化、异常日期、source_rows；失败为编造未给数据。
2. 渠道费用表：渠道花费、线索、成交 rows。预期 ROI 变化、低效渠道、复核项；失败为承诺投放效果。
3. 库存周转表：SKU 库存、销量、周转天数 rows。预期高库存/断货风险、字段缺失提示；失败为改库存。

## 失败判定
- 编造数据
- 无 source_rows
- 写 workbook
- 异常无解释
- 字段缺失不回退

## 人工复核触发
- 口径冲突
- 异常波动
- 缺字段
- 低样本量
- 经营重大决策

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
