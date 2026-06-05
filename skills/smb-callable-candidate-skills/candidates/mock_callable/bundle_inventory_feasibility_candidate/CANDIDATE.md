# bundle_inventory_feasibility_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 经营报表分析包
- roles: 商品运营
- scenario: 套装库存可行性检查

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 组合 A+B+C，库存分别 50/20/80
- 预期输出字段: feasible_bundle_count, bottleneck_skus, risk_flags, manual_review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- feasible_bundle_count
- bottleneck_skus
- risk_flags
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不改库存
- 不上架套装

## 人工复核触发
- 库存准确性
- 超卖

## 复用 / 重复关系
可试跑

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
