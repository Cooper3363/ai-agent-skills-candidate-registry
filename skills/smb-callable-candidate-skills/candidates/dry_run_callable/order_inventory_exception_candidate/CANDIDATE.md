# order_inventory_exception_candidate

## Summary

- Business package: ecommerce_store_ops
- Scenario: 订单库存异常 dry-run
- Status: dry_run_callable
- DeepAgents trial fit: dry_run_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- store_operator
- ecommerce_operator

## Source And License

- Source project: claude-office-skills/shopify-automation + internal dry-run
- License or origin: child skill frontmatter MIT; external Shopify/API terms blocked in trial

## Trial Mode

- dry_run_only
- read_only
- BYOK_required
- external_action_blocked

## Input Schema

- input_text: Chinese mock/read-only input.
- business_context: Optional mock policy, metrics, order, resume, or campaign context.
- constraints: Optional permission and policy constraints.

## Output Schema

- exceptions
- affected_skus
- verification_steps
- write_allowed

## Smoke Test Case Zh

mock 订单显示库存不足和负库存，输出异常核查步骤。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 调用 Shopify API
- 修改库存
- 发送通知
- 写业务系统
- 访问真实账号
- 调用真实业务 API
- 发送邮件/短信/微信
- 写 CRM/日历/任务/业务系统
- 抓取真实网页
- 上传文件
- 退款或赔偿
- 生成真实图片/视频/音频/OCR/PDF 结果

## Human Review Triggers

- large_order
- negative_inventory
- supplier_conflict

## Next Step

formal_l2_completed_send_draft_l3

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
