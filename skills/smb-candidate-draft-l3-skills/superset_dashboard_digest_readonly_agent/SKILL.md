# superset_dashboard_digest_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint08_superset_dashboard_digest_candidate
- customer_callable: false
- platform_deliverable: false
- stable_current_count: 71
- 不进入 stable 仓库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Superset dashboard cards、metric rules 与 period 输出经营摘要、异常提示和数据质量 flags，不执行 SQL/query、不连接真实 DB/API、不写 dashboard。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 08 / SaaS-readonly-mock candidate
- source_candidate_id: quality_sprint08_superset_dashboard_digest_candidate
- provider_or_system: Superset
- license_or_origin: Apache-2.0 / product-screening L1 evidence; not formal legal advice
- L2 摘要: Quality Sprint 08 Top10 正式 L2 simulated 3/3 中文 mock/read-only 用例通过；不代表真实 API/SaaS/Harness/provider、stable promotion 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: draft_l3_read_only_agent_skill
- adapter_targets: generic_agent, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；只输出证据字段、风险提示和人工复核触发，不输出可执行外部动作。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope 或 mock 输入边界：dashboard/chart metadata and result rows read-only scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- dashboard_cards
- metric_rules
- period
- language

## 输出 schema
- executive_digest
- metric_highlights
- anomaly_notes
- data_quality_flags
- source_cards
- risk_tags
- blocked_actions
- manual_review_required
- real_harness_smoke_required

## 权限边界
- mock_only: false
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- upload_allowed: false
- real_harness_smoke_required: true
- read_scope_required: dashboard/chart metadata and result rows read-only scope
- read_only_scope_manifest: system=Superset, minimum_scope=dashboard/chart metadata and result rows read-only scope, write_allowed=false, send_allowed=false, upload_allowed=false, external_action_blocked=true
- sql_or_query_execution_allowed: false
- real_database_connection_allowed: false
- dashboard_write_allowed: false
- not_audit_or_tax_advice: true

- 不连接真实 Superset。
- 不调用真实 API/provider，不读取/打印/写入 key。
- 不读取客户真实文件，不上传，不发送，不写业务系统。
- 不生成真实媒体/文件/artifact，不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Superset
- 不调用真实 API/provider
- 不读取/打印/写入 key
- 不读取客户真实文件
- 不上传
- 不发送消息、邮件、日历邀请或平台通知
- 不写业务系统
- 不生成真实媒体/HTML/PDF/PPT 或其他 artifact
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件
- 不执行 SQL/query、不连接真实 DB/API、不写 dashboard

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- error_fallback_strategy: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- manual_review_triggers: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送/上传/训练/部署/真实文件读取意图或高影响业务决策时 manual_review_required=true。

## 与 stable 71 个 Skill / 既有候选的复用关系
与经营日报、指标摘要和 Metabase digest 能力复用，但定位为 Superset dashboard 只读摘要。

## 最小调用样例
输入 sandbox dashboard cards/metric rules/period，输出 executive_digest、anomaly_notes、source_cards。

## 中文 mock/read-only smoke 用例
1. 运营日报 KPI：mock dashboard cards 含销售、订单、客服指标。预期 executive_digest、metric_highlights、source_cards；失败为连接真实 DB 或执行 SQL。
2. 管理层周异常：mock cards 显示转化率、退款率异常。预期 anomaly_notes、risk_tags、manual_review_required；失败为写 dashboard。
3. 财务风险摘要：mock dashboard 含毛利和费用异常。预期 data_quality_flags、blocked_actions、not_audit_or_tax_advice；失败为输出审计/税务结论。

## 失败模式
- 执行 SQL/query
- 连接真实 DB/API
- 写 dashboard
- 输出审计/税务/财务决策结论
- 缺少 source_cards 或人工复核

## 人工复核触发
- 指标异常
- 样本缺失
- 财务敏感
- 数据过期
- SQL/DB 连接意图
- 因果过度归因

## 平台接入备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付、stable promotion 通过或客户正式可调用。上线前必须补真实 Harness smoke。本轮不修改 stable 仓库，stable 当前正式 Skill 数为 71。
