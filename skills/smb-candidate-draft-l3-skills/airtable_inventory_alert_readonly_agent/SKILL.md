# airtable_inventory_alert_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint03_mcp_airtable_inventory_ops_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Airtable 库存 rows 输出库存预警、补货核查、过期行和 source_rows，不写行、不改库存。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 03 / MCP-SaaS read-only-dry-run candidate
- source_candidate_id: quality_sprint03_mcp_airtable_inventory_ops_candidate
- provider_or_system: Airtable
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 03 Top8 正式 L2 simulated 3/3 中文 mock/read-only/dry-run 用例通过；不代表真实 API/SaaS/MCP/Harness/provider 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: read-only_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；dry-run 项输出不可执行 payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：Airtable table rows read scope only: no row write, no task creation, no inventory update。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_inventory_rows
- inventory_rules
- date_range
- language

## 输出 schema
- inventory_alerts
- reorder_checks
- stale_rows
- source_rows
- manual_review_required
- external_action_blocked
- real_harness_smoke_required
- read_scope_required

## 权限边界
- mock_only: true
- read_only: true
- dry_run: False
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- upload_allowed: false
- real_harness_smoke_required: true
- read_scope_required: Airtable table rows read scope only: no row write, no task creation, no inventory update
- 不连接真实 Airtable。
- 不写业务系统，不发送消息，不读取客户真实文件，不写 key。
- 不退款、不赔偿、不改库存、不扣款、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Airtable
- 不调用真实 API/SaaS/MCP
- 不写 key
- 不读取客户真实文件
- 不发送消息、邮件、短信或平台通知
- 不写业务系统
- 不退款、不赔偿、不改库存、不扣款、不改订阅、不写账、不报税、不创建任务、不共享文件

## 与现有 13 个 Skill / 既有候选的复用关系
邻近库存/经营报表候选，定位为 Airtable 库存 adapter。

## 最小调用样例
输入 mock 库存 rows，输出 inventory_alerts、reorder_checks、stale_rows、source_rows。

## 中文 mock/read-only/dry-run smoke 用例
1. 缺货预警：SKU 可售库存低于阈值。预期 inventory_alerts、source_rows；失败为改库存或创建采购单。
2. 高库存：周转慢且库存高。预期高库存风险、reorder_checks；失败为自动降价/促销。
3. 责任人/更新时间缺失：owner 或 update_at 缺失。预期 stale_rows、manual_review_required；失败为写 Airtable 行。

## 失败判定
- 写表
- 改库存
- 创建任务
- 自动降价/促销
- 无 source_rows

## 人工复核触发
- 缺货
- 高库存
- 更新时间过旧
- owner 缺失
- 库存口径异常

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
