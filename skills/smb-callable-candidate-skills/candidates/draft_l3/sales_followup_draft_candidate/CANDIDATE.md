# sales_followup_draft_candidate

## Summary

- Business package: sales
- Scenario: 销售跟进草稿
- Status: draft_l3
- DeepAgents trial fit: skill_ready
- Customer callable: false
- Platform deliverable: false
- Formal L2 status: completed

## Roles

- sales_representative
- sales_manager
- founder_operator

## Source And License

- Source project: Marketing Skills / existing CRM note boundary
- License or origin: MIT product screening passed; formal legal review still required

## Trial Mode

- mock_only
- draft_only
- read_only
- external_action_blocked

## Output Schema

- message_draft
- subject_options
- talking_points
- personalization_basis
- risk_notes
- send_allowed
- missing_info
- manual_review_required

## Smoke Test Case Zh

输入试用后跟进、报价异议或沉睡线索场景，输出跟进草稿且 send_allowed=false。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 发送邮件
- 发送短信
- 发送微信
- 写 CRM
- 触发外部动作
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

- discount
- contract
- complaint
- personal_info
- do_not_contact

## Non Delivery Statement

This draft L3 candidate is for controlled platform retest only. It is not a stable customer-callable Skill. Stable customer-callable baseline remains 13 Skills.
