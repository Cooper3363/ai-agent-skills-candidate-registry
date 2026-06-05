# store_staff_shift_plan_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 经营报表分析包
- roles: 门店运营
- scenario: 门店员工排班草稿

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: dry_run_only, read_only, external_action_blocked
- l1_result: can_dry_run_smoke
- deepagents_trial_fit: dry_run_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 周末客流高峰、员工可用时段
- 预期输出字段: shift_plan_draft, constraints, risk_flags, external_action_blocked, send_allowed, write_allowed

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- shift_plan_draft
- constraints
- risk_flags
- external_action_blocked
- send_allowed
- write_allowed

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不写排班系统
- 不通知员工

## 人工复核触发
- 工时
- 劳动合规
- 请假冲突

## 复用 / 重复关系
dry-run 可试跑，需 HR 边界

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
