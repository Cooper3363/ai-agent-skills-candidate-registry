# refund_policy_reply_draft_candidate

## Summary

- Business package: customer_support
- Scenario: 退款政策回复草稿
- Status: mock_callable
- DeepAgents trial fit: mock_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- after_sales_agent
- support_manager

## Source And License

- Source project: internal_template
- License or origin: internal_template; no third-party code reused

## Trial Mode

- mock_only
- read_only
- external_action_blocked

## Input Schema

- input_text: Chinese mock/read-only input.
- business_context: Optional mock policy, metrics, order, resume, or campaign context.
- constraints: Optional permission and policy constraints.

## Output Schema

- reply_draft
- policy_basis
- risk_flags
- handoff_required

## Smoke Test Case Zh

客户要求退款并威胁投诉，输入 mock 退款政策，生成只读回复草稿。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 承诺退款
- 承诺赔偿
- 回访客户
- 发送消息
- 写工单
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

- refund_request
- complaint
- compensation_claim
- policy_conflict

## Next Step

formal_l2_completed_send_draft_l3

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
