# support_policy_conflict_detector_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: pending_or_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 客服知识库助手包
- roles: 知识库运营
- scenario: 检测两段客服政策是否冲突

## 来源与许可证 / Trial Mode
- source_project: existing_skill_combo
- license_or_origin: 复用 support_kb_doc_cleaner / faq_answer_with_citations 边界
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 退款政策 A 写 7 天，政策 B 写 15 天
- 预期输出字段: conflict_found, conflicting_clauses, severity, resolution_questions, citations

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- conflict_found
- conflicting_clauses
- severity
- resolution_questions
- citations

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不改知识库
- 不发布政策

## 人工复核触发
- 客户权益
- 退款时限
- 法律/平台规则冲突

## 复用 / 重复关系
复用 KB 能力但场景明确，可独立候选

## 下一步动作
进入正式 L2 simulated 队列；当前仅为 smoke passed 候选卡。
