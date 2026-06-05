# sales_stage_exit_criteria_checker_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 销售跟进助手包
- roles: RevOps
- scenario: 销售阶段退出条件检查

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 商机准备从需求确认推进到报价阶段
- 预期输出字段: criteria_met, missing_evidence, recommended_next_steps, risk_flags

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- criteria_met
- missing_evidence
- recommended_next_steps
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
- 不推进 CRM 阶段

## 人工复核触发
- 缺预算
- 缺决策人
- 缺时间线

## 复用 / 重复关系
与 CRM 结构化相邻，偏流程治理

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
