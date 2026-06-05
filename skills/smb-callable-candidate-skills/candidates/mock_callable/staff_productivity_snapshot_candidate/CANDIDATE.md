# staff_productivity_snapshot_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 经营报表分析包
- roles: 门店/HR 运营
- scenario: 员工效率快照

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 每人接待、订单、工时 mock 数据
- 预期输出字段: productivity_snapshot, caveats, risk_flags, review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- productivity_snapshot
- caveats
- risk_flags
- review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不用于自动处罚/绩效

## 人工复核触发
- 员工数据
- 劳动合规

## 复用 / 重复关系
敏感但可试跑，需强人工复核

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
