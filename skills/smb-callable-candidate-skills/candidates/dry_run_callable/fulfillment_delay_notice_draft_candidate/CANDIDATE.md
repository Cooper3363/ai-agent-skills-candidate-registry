# fulfillment_delay_notice_draft_candidate

## Summary

- Business package: ecommerce_customer_support
- Scenario: 延迟发货通知草稿
- Status: dry_run_callable
- DeepAgents trial fit: dry_run_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- after_sales_agent
- store_operator

## Source And License

- Source project: internal_template
- License or origin: internal_template; no third-party code reused

## Trial Mode

- dry_run_only
- read_only
- external_action_blocked

## Input Schema

- input_text: Chinese mock/read-only input.
- business_context: Optional mock policy, metrics, order, resume, or campaign context.
- constraints: Optional permission and policy constraints.

## Output Schema

- message_draft
- send_allowed
- write_allowed
- external_action_blocked

## Smoke Test Case Zh

物流延迟 2 天，生成通知草稿。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 发送通知
- 赔偿承诺
- 修改订单
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

- delay
- compensation_claim
- complaint

## Next Step

candidate_pool_continue_smoke

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
