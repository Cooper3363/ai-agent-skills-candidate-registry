# inventory_turnover_brief_candidate

## Summary

- Business package: ecommerce_reporting
- Scenario: 库存周转摘要
- Status: mock_callable
- DeepAgents trial fit: mock_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- store_operator
- owner_operator

## Source And License

- Source project: internal_template + order_inventory_exception_candidate
- License or origin: internal_template / dry-run candidate boundary reused

## Trial Mode

- mock_only
- read_only
- external_action_blocked

## Input Schema

- input_text: Chinese mock/read-only input.
- business_context: Optional mock policy, metrics, order, resume, or campaign context.
- constraints: Optional permission and policy constraints.

## Output Schema

- turnover_summary
- slow_moving_skus
- stockout_risks
- next_checks

## Smoke Test Case Zh

SKU 库存天数、销量、补货周期 mock 数据，输出摘要。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 修改库存
- 下采购单
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

- stockout
- slow_moving_inventory
- supplier_conflict

## Next Step

candidate_pool_continue_smoke

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
