# sku_deduplication_suggester_candidate

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
- scenario: 疑似重复 SKU 提示

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 多个 SKU 名称相近、条码缺失
- 预期输出字段: duplicate_candidates, match_reasons, confidence, manual_review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- duplicate_candidates
- match_reasons
- confidence
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
- 不合并 SKU
- 不改库存

## 人工复核触发
- 低置信
- 库存/订单关联

## 复用 / 重复关系
可试跑，建议后续 L2

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
