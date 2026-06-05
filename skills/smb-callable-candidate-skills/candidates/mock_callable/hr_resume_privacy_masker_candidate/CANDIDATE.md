# hr_resume_privacy_masker_candidate

## Summary

- Business package: admin_hr
- Scenario: 简历隐私脱敏
- Status: mock_callable
- DeepAgents trial fit: mock_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- hr_operator
- admin_operator

## Source And License

- Source project: Microsoft Presidio + support_pii_redactor
- License or origin: Presidio MIT; stable PII redactor boundary reused

## Trial Mode

- mock_only
- read_only
- external_action_blocked

## Input Schema

- input_text: Chinese mock/read-only input.
- business_context: Optional mock policy, metrics, order, resume, or campaign context.
- constraints: Optional permission and policy constraints.

## Output Schema

- redacted_text
- entities
- preserved_fields
- risk_level

## Smoke Test Case Zh

mock 简历含手机号、邮箱、身份证、推荐人电话，输出脱敏文本。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 读取真实简历
- 上传文件
- 录用/淘汰判断
- 访问真实账号
- 调用真实业务 API
- 发送邮件/短信/微信
- 写 CRM/日历/任务/业务系统
- 抓取真实网页
- 退款或赔偿
- 修改库存
- 生成真实图片/视频/音频/OCR/PDF 结果

## Human Review Triggers

- high_sensitive_pii
- third_party_contact
- low_confidence_entity

## Next Step

formal_l2_completed_send_draft_l3

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
