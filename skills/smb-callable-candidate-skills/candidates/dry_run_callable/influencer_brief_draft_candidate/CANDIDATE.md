# influencer_brief_draft_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: pending_or_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 营销内容生产包
- roles: 达人合作运营
- scenario: 达人合作 brief 草稿

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: dry_run_only, read_only, external_action_blocked
- l1_result: can_dry_run_smoke
- deepagents_trial_fit: dry_run_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 为本地咖啡店达人探店生成合作 brief
- 预期输出字段: influencer_brief, deliverables, disclosure_notes, risk_flags, external_action_blocked, send_allowed, write_allowed

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- influencer_brief
- deliverables
- disclosure_notes
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
- 不联系达人
- 不付款
- 不承诺曝光

## 人工复核触发
- 授权
- 广告标识
- 效果承诺

## 复用 / 重复关系
dry-run 高价值，进入 Top 15

## 下一步动作
进入正式 L2 simulated 队列；当前仅为 smoke passed 候选卡。
