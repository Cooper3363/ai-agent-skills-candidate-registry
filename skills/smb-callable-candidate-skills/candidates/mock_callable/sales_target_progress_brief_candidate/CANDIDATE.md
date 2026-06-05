# sales_target_progress_brief_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 经营报表分析包
- roles: 销售运营
- scenario: 销售目标进度简报

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 本月目标 50 万，当前 32 万，剩余 8 天
- 预期输出字段: progress_summary, gap, drivers, action_questions

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- progress_summary
- gap
- drivers
- action_questions

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不改目标
- 不调整绩效

## 人工复核触发
- 绩效
- 奖金
- 数据口径

## 复用 / 重复关系
可试跑

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
