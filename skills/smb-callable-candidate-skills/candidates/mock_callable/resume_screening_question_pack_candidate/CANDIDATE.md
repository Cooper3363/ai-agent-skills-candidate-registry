# resume_screening_question_pack_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 人事行政包
- roles: HR
- scenario: 简历追问问题包

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 候选人简历含项目经历但缺关键证据
- 预期输出字段: screening_questions, fairness_notes, risk_flags, manual_review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- screening_questions
- fairness_notes
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
- 不给录用/淘汰建议

## 人工复核触发
- 招聘公平
- PII
- 歧视

## 复用 / 重复关系
可试跑，需 HR 合规边界

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
