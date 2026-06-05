# support_ticket_batch_summary_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: pending_or_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 客服知识库助手包
- roles: 客服主管
- scenario: 班次工单批量摘要

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 10 条 mock 工单含物流延迟、退款、投诉
- 预期输出字段: batch_summary, issue_clusters, vip_or_escalation_items, action_items, pii_redaction_notes

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- batch_summary
- issue_clusters
- vip_or_escalation_items
- action_items
- pii_redaction_notes

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不写工单系统
- 不联系客户

## 人工复核触发
- 高优工单
- VIP
- 投诉
- 未脱敏 PII

## 复用 / 重复关系
可作为客服班次运营候选

## 下一步动作
进入正式 L2 simulated 队列；当前仅为 smoke passed 候选卡。
