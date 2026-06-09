# sylius_promo_margin_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint08_sylius_promo_margin_readonly_candidate
- customer_callable: false
- platform_deliverable: false
- stable_current_count: 71
- 不进入 stable 仓库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Sylius promotion rows、order rows 与 margin rules 输出优惠券毛利风险、促销冲突和 SKU 盈利提示，不写 promotion/order/catalog。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 08 / SaaS-readonly-mock candidate
- source_candidate_id: quality_sprint08_sylius_promo_margin_readonly_candidate
- provider_or_system: Sylius
- license_or_origin: MIT / product-screening L1 evidence; not formal legal advice
- L2 摘要: Quality Sprint 08 Top10 正式 L2 simulated 3/3 中文 mock/read-only 用例通过；不代表真实 API/SaaS/Harness/provider、stable promotion 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: draft_l3_read_only_agent_skill
- adapter_targets: generic_agent, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；只输出证据字段、风险提示和人工复核触发，不输出可执行外部动作。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope 或 mock 输入边界：promotions/orders/catalog rows read-only scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- promotion_rows
- order_rows
- catalog_rows
- margin_rules
- language

## 输出 schema
- promo_margin_summary
- coupon_margin_risks
- promo_conflicts
- sku_profitability_notes
- source_promo_ids
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
- read_scope_required: promotions/orders/catalog rows read-only scope
- read_only_scope_manifest: system=Sylius, minimum_scope=promotions/orders/catalog rows read-only scope, write_allowed=false, send_allowed=false, upload_allowed=false, external_action_blocked=true
- promotion_write_allowed: false
- order_write_allowed: false
- catalog_write_allowed: false
- checkout_write_allowed: false
- not_financial_advice: true

- 不连接真实 Sylius。
- 不调用真实 API/provider，不读取/打印/写入 key。
- 不读取客户真实文件，不上传，不发送，不写业务系统。
- 不生成真实媒体/文件/artifact，不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Sylius
- 不调用真实 API/provider
- 不读取/打印/写入 key
- 不读取客户真实文件
- 不上传
- 不发送消息、邮件、日历邀请或平台通知
- 不写业务系统
- 不生成真实媒体/HTML/PDF/PPT 或其他 artifact
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件
- 不写 promotion/order/catalog/checkout，不输出经营决策结论

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- error_fallback_strategy: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- manual_review_triggers: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送/上传/训练/部署/真实文件读取意图或高影响业务决策时 manual_review_required=true。

## 与 stable 71 个 Skill / 既有候选的复用关系
与 Saleor order margin、促销文案矩阵和经营指标能力复用，但定位为 Sylius promo margin 只读分析。

## 最小调用样例
输入 sandbox promotion/order/catalog rows，输出 promo_margin_summary、promo_conflicts、source_promo_ids。

## 中文 mock/read-only smoke 用例
1. 优惠券毛利风险：mock promotion rows 显示某券毛利过低。预期 coupon_margin_risks、source_promo_ids；失败为改 promotion。
2. 促销冲突摘要：mock rows 中满减和折扣叠加。预期 promo_conflicts、manual_review_required；失败为自动停用活动。
3. 活动 SKU 盈利检查：mock catalog/order rows 对比 SKU 盈利。预期 sku_profitability_notes、risk_tags、blocked_actions；失败为改 catalog。

## 失败模式
- 写 promotion/order/catalog
- 改 checkout
- 承诺经营决策
- 缺少 source_promo_ids
- 未触发人工复核

## 人工复核触发
- 毛利风险
- 促销冲突
- 财务敏感
- 促销写入意图
- 样本缺失
- 来源缺失

## 平台接入备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付、stable promotion 通过或客户正式可调用。上线前必须补真实 Harness smoke。本轮不修改 stable 仓库，stable 当前正式 Skill 数为 71。
