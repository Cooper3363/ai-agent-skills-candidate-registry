# complaint_escalation_summary_candidate

## Summary

- Business package: customer_support
- Scenario: 投诉升级摘要
- Status: draft_l3
- DeepAgents trial fit: skill_ready
- Customer callable: false
- Platform deliverable: false
- Formal L2 status: completed

## Roles

- complaint_specialist
- support_manager

## Source And License

- Source project: anthropics/knowledge-work-plugins
- License or origin: Apache-2.0; mock/read-only trial only

## Trial Mode

- mock_only
- read_only
- external_action_blocked

## Output Schema

- complaint_type
- severity
- customer_sentiment
- summary
- key_facts
- requested_resolution
- risk_flags
- handoff_required
- handoff_reason
- next_safe_action
- privacy_notes
- confidence

## Smoke Test Case Zh

输入退款、赔偿、隐私投诉文本，输出投诉摘要、风险等级和转人工原因。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 回访客户
- 发送消息
- 退款
- 承诺赔偿
- 写客服系统
- 法律判断
- 访问真实账号
- 调用真实业务 API
- 发送邮件/短信/微信
- 写 CRM/日历/任务/业务系统
- 抓取真实网页
- 上传文件
- 退款或赔偿
- 修改库存
- 生成真实图片/视频/音频/OCR/PDF 结果

## Human Review Triggers

- refund
- compensation_claim
- regulatory_threat
- privacy_sensitive
- account_security

## Non Delivery Statement

This draft L3 candidate is for controlled platform retest only. It is not a stable customer-callable Skill. Stable customer-callable baseline remains 13 Skills.
