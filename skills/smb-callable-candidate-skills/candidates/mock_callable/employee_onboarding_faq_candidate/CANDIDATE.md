# employee_onboarding_faq_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 人事行政包
- roles: HR/行政
- scenario: 入职 FAQ 草稿

## 来源与许可证 / Trial Mode
- source_project: existing_skill_combo
- license_or_origin: 复用 faq_answer_with_citations 与 To50 入职清单边界
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 基于 mock 制度片段回答入职材料问题
- 预期输出字段: answer, citations, missing_policy_notes, handoff_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- answer
- citations
- missing_policy_notes
- handoff_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不替代 HR 制度解释

## 人工复核触发
- 薪酬
- 合同
- 社保

## 复用 / 重复关系
与 faq_answer_with_citations 重叠，适合作 HR 场景候选

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
