# invoice_amount_consistency_candidate

## Summary

- Business package: finance_admin
- Scenario: 票据金额一致性组件
- Status: component_only
- DeepAgents trial fit: component_only
- DeepAgents smoke status: component_only_not_independent_smoke
- Customer callable: false
- Platform deliverable: false
- Count toward 100: false

## Roles

- finance_operator
- admin_operator

## Source And License

- Source project: internal_template + expense_invoice_parser
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

- amount_consistency
- mismatched_fields
- evidence
- manual_review_required

## Smoke Test Case Zh

mock OCR 文本中发票金额、税额、报销金额不一致，输出核查提示。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 报销审批
- 税务建议
- 审计结论
- 写财务系统
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

- amount_mismatch
- missing_tax_id
- low_confidence

## Next Step

keep_in_component_pool

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
