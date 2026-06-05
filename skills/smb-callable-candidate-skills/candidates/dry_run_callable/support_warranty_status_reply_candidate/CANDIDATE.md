# support_warranty_status_reply_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 客服知识库助手包
- roles: 售后客服
- scenario: 保修状态说明草稿

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: dry_run_only, read_only, external_action_blocked
- l1_result: can_dry_run_smoke
- deepagents_trial_fit: dry_run_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 客户询问是否可免费换新，信息不完整
- 预期输出字段: reply_draft, required_info, warranty_status_unknown, risk_flags, external_action_blocked, send_allowed, write_allowed

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- reply_draft
- required_info
- warranty_status_unknown
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
- 不判定保修结果
- 不发回复
- 不改售后单

## 人工复核触发
- 免费换新
- 赔偿
- 缺少凭证

## 复用 / 重复关系
dry-run 草稿，可继续试跑

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
