# lost_deal_followup_draft_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: pending_or_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 销售跟进助手包
- roles: 销售代表
- scenario: 丢单后复联草稿

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: dry_run_only, read_only, external_action_blocked
- l1_result: can_dry_run_smoke
- deepagents_trial_fit: dry_run_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 客户因预算不足丢单，30 天后可复联
- 预期输出字段: followup_draft, subject_options, timing_notes, risk_flags, external_action_blocked, send_allowed, write_allowed

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- followup_draft
- subject_options
- timing_notes
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
- 不发送
- 不写 CRM
- 不承诺折扣

## 人工复核触发
- 退订
- 竞品敏感
- 折扣越权

## 复用 / 重复关系
dry-run 草稿，可进入 Top 15

## 下一步动作
进入正式 L2 simulated 队列；当前仅为 smoke passed 候选卡。
