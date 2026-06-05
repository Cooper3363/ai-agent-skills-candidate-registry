# pricing_terms_risk_summary_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: pending_or_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 销售跟进助手包
- roles: 销售主管
- scenario: 价格和付款条款风险摘要

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 报价含 60 天账期、额外折扣、验收后付款
- 预期输出字段: risk_summary, risk_level, risky_terms, review_required, safe_questions

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- risk_summary
- risk_level
- risky_terms
- review_required
- safe_questions

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不审批折扣
- 不修改报价

## 人工复核触发
- 高折扣
- 长账期
- 违约责任

## 复用 / 重复关系
高 SMB 价值，可进入 Top 15

## 下一步动作
进入正式 L2 simulated 队列；当前仅为 smoke passed 候选卡。
