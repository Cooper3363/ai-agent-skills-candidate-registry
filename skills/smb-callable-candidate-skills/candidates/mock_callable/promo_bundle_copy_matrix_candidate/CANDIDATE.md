# promo_bundle_copy_matrix_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: pending_or_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 营销内容生产包
- roles: 营销运营
- scenario: 促销套装文案矩阵

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 两件套、三件套、满减活动生成不同渠道文案
- 预期输出字段: copy_matrix, channel_variants, forbidden_claims, risk_flags

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- copy_matrix
- channel_variants
- forbidden_claims
- risk_flags

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不发布
- 不投放
- 不改价格

## 人工复核触发
- 价格承诺
- 库存
- 广告法

## 复用 / 重复关系
高可用，可进入 Top 15

## 下一步动作
进入正式 L2 simulated 队列；当前仅为 smoke passed 候选卡。
