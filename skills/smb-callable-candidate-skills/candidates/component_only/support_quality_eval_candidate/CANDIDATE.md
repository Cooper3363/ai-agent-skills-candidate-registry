# support_quality_eval_candidate

## Summary

- Business package: customer_support
- Scenario: 客服质检组合组件
- Status: component_only
- DeepAgents trial fit: component_only
- DeepAgents smoke status: component_only_not_independent_smoke
- Customer callable: false
- Platform deliverable: false
- Count toward 100: false

## Roles

- support_lead
- quality_reviewer

## Source And License

- Source project: internal_template + support_reply_guardrail + support_ticket_classifier + support_pii_redactor
- License or origin: existing stable skill combo; no new third-party code

## Trial Mode

- mock_only
- read_only
- external_action_blocked

## Input Schema

- input_text: Chinese mock/read-only input.
- business_context: Optional mock policy, metrics, order, resume, or campaign context.
- constraints: Optional permission and policy constraints.

## Output Schema

- overall_score
- score_breakdown
- failed_checks
- risk_flags
- training_notes
- manual_review_required

## Smoke Test Case Zh

mock 客服对话质检，输出评分、失败项和培训建议。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 写质检系统
- 处罚客服
- 保留未脱敏 PII
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
- complaint
- privacy_sensitive
- account_security

## Next Step

keep_in_component_pool

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
