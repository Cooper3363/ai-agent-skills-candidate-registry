# support_tone_rewrite_safe_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 客服知识库助手包
- roles: 客服质检
- scenario: 将生硬回复改写为合规温和语气

## 来源与许可证 / Trial Mode
- source_project: existing_skill_combo
- license_or_origin: 复用稳交付客服能力边界
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 原回复语气强硬并暗示客户责任
- 预期输出字段: rewritten_reply, tone_changes, safety_notes, risk_flags, manual_review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- rewritten_reply
- tone_changes
- safety_notes
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
- 不替代客服发送
- 不改变政策结论

## 人工复核触发
- 投诉升级
- 承诺退款
- 歧视性表达

## 复用 / 重复关系
与 support_reply_guardrail 有重复，适合作为客服回复增强候选

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
