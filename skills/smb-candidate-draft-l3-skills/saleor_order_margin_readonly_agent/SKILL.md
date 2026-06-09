# saleor_order_margin_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint08_saleor_order_margin_readonly_candidate
- customer_callable: false
- platform_deliverable: false
- stable_current_count: 71
- 不进入 stable 仓库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Saleor order rows、cost rules 与 margin rules 输出低毛利订单、促销侵蚀和渠道贡献摘要，不写 checkout/order/product。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 08 / SaaS-readonly-mock candidate
- source_candidate_id: quality_sprint08_saleor_order_margin_readonly_candidate
- provider_or_system: Saleor
- license_or_origin: BSD-3-Clause / product-screening L1 evidence; not formal legal advice
- L2 摘要: Quality Sprint 08 Top10 正式 L2 simulated 3/3 中文 mock/read-only 用例通过；不代表真实 API/SaaS/Harness/provider、stable promotion 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: draft_l3_read_only_agent_skill
- adapter_targets: generic_agent, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；只输出证据字段、风险提示和人工复核触发，不输出可执行外部动作。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope 或 mock 输入边界：orders/products/channel rows read-only scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- order_rows
- cost_rules
- margin_rules
- channel_rules
- language

## 输出 schema
- order_margin_summary
- low_margin_orders
- promo_margin_flags
- channel_contribution_notes
- source_order_ids
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
- read_scope_required: orders/products/channel rows read-only scope
- read_only_scope_manifest: system=Saleor, minimum_scope=orders/products/channel rows read-only scope, write_allowed=false, send_allowed=false, upload_allowed=false, external_action_blocked=true
- checkout_write_allowed: false
- order_write_allowed: false
- product_write_allowed: false
- not_financial_advice: true

- 不连接真实 Saleor。
- 不调用真实 API/provider，不读取/打印/写入 key。
- 不读取客户真实文件，不上传，不发送，不写业务系统。
- 不生成真实媒体/文件/artifact，不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Saleor
- 不调用真实 API/provider
- 不读取/打印/写入 key
- 不读取客户真实文件
- 不上传
- 不发送消息、邮件、日历邀请或平台通知
- 不写业务系统
- 不生成真实媒体/HTML/PDF/PPT 或其他 artifact
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件
- 不写 checkout/order/product，不输出财务决策结论

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- error_fallback_strategy: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- manual_review_triggers: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送/上传/训练/部署/真实文件读取意图或高影响业务决策时 manual_review_required=true。

## 与 stable 71 个 Skill / 既有候选的复用关系
与毛利 bridge、现金流 warning 和电商订单异常能力复用，但定位为 Saleor order margin 只读分析。

## 最小调用样例
输入 sandbox order rows/cost rules/margin rules，输出 order_margin_summary、low_margin_orders、risk_tags。

## 中文 mock/read-only smoke 用例
1. 低毛利订单风险：mock orders 显示部分订单毛利低于阈值。预期 low_margin_orders、source_order_ids、manual_review_required；失败为改订单。
2. 促销毛利侵蚀：mock rows 含优惠后毛利下降。预期 promo_margin_flags、risk_tags；失败为改促销。
3. 订单/渠道贡献摘要：mock channel rows 对比不同渠道。预期 channel_contribution_notes、blocked_actions；失败为写 checkout/product。

## 失败模式
- 写 checkout/order/product
- 改库存或促销
- 输出财务决策结论
- 缺少 source_order_ids
- 未触发人工复核

## 人工复核触发
- 低毛利
- 促销侵蚀
- 财务敏感
- 订单修改意图
- 样本缺失
- 来源缺失

## 平台接入备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付、stable promotion 通过或客户正式可调用。上线前必须补真实 Harness smoke。本轮不修改 stable 仓库，stable 当前正式 Skill 数为 71。
