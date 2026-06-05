# proposal_requirement_gap_checker_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 销售跟进助手包
- roles: 售前
- scenario: 检查方案需求缺口

## 来源与许可证 / Trial Mode
- source_project: existing_skill_combo
- license_or_origin: 复用 To50 proposal_outline_candidate 边界
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 客户需求含预算、上线时间，但缺成功标准
- 预期输出字段: missing_requirements, clarification_questions, risk_flags, next_steps

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- missing_requirements
- clarification_questions
- risk_flags
- next_steps

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不生成合同/报价承诺

## 人工复核触发
- 价格
- 交付范围
- 法务条款缺失

## 复用 / 重复关系
与 proposal_outline_candidate 相邻但检查型更清晰

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
