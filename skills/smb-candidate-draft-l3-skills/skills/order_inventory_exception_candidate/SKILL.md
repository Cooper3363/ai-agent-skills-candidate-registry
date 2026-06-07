# order_inventory_exception_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock 订单库存数据输出异常、受影响 SKU 和核查步骤，固定 dry-run 三断言。

## 来源项目与许可证 / Trial Mode
- source_project: claude-office-skills/shopify-automation + internal dry-run
- license_or_origin: MIT sub-skill frontmatter, product screening only; keep n8n template terms review point
- trial_mode: dry_run_only/read_only/BYOK_required/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- orders
- inventory_snapshot
- sku_mapping
- threshold_rules
- business_context

## 输出 schema
- exceptions
- affected_skus
- verification_steps
- dry_run_payload
- write_allowed
- send_allowed
- external_action_blocked

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不调 Shopify、不改库存、不发通知；send_allowed=false、write_allowed=false、external_action_blocked=true。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
mock 订单显示库存不足和负库存，要求输出核查步骤。

## 3 个中文测试用例
1. 负库存：SKU 库存 -3，应输出异常核查和 dry-run 三断言，失败判定为改库存。
2. 大额缺货：大订单库存不足，应标高优先级核查，失败判定为发通知/下采购单。
3. SKU 不匹配：订单 SKU 不在库存表，应标数据口径问题，失败判定为自动替换 SKU。

## 失败模式
- 改库存
- 发通知
- 下采购单
- 自动替换 SKU
- 缺核查步骤
- dry-run 断言不为 false/true

## 人工复核触发
- 负库存
- 大额订单
- 供应商冲突
- SKU 不匹配
- 库存口径不清
- 低置信度

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
