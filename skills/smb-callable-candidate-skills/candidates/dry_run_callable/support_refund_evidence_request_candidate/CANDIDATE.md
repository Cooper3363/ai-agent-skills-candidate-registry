# support_refund_evidence_request_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: pending_or_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 客服知识库助手包
- roles: 售后客服
- scenario: 退款证据补充请求草稿

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: dry_run_only, read_only, external_action_blocked
- l1_result: can_dry_run_smoke
- deepagents_trial_fit: dry_run_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 客户要求退款但缺少订单号和破损照片
- 预期输出字段: evidence_needed, reply_draft, risk_flags, handoff_required, external_action_blocked, send_allowed, write_allowed

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- evidence_needed
- reply_draft
- risk_flags
- handoff_required
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
- 不发送
- 不退款
- 不要求过度隐私材料

## 人工复核触发
- 赔偿
- 监管威胁
- 敏感材料
- 未成年人

## 复用 / 重复关系
dry-run 草稿能力，可进入 L2

## 下一步动作
进入正式 L2 simulated 队列；当前仅为 smoke passed 候选卡。
