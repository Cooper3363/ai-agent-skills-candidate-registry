# marketplace_reply_draft_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 客服知识库助手包
- roles: 电商客服
- scenario: 平台评价/问答回复草稿

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: dry_run_only, read_only, external_action_blocked
- l1_result: can_dry_run_smoke
- deepagents_trial_fit: dry_run_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 买家差评称物流慢、包装破损
- 预期输出字段: reply_draft, tone_notes, risk_flags, external_action_blocked, send_allowed, write_allowed

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- reply_draft
- tone_notes
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
- 不发布回复
- 不承诺赔偿

## 人工复核触发
- 差评
- 退款
- 平台规则

## 复用 / 重复关系
与客服回复能力相邻，dry-run

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
