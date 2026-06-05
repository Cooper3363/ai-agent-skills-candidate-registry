# contract_clause_partitioner_candidate

## Summary

- Business package: admin_legal
- Scenario: 合同条款分区
- Status: dry_run_callable
- DeepAgents trial fit: dry_run_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- admin_operator
- legal_reviewer

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

- sections
- risky_sections
- not_legal_advice
- write_allowed

## Smoke Test Case Zh

mock 合同含付款、保密、自动续费、违约，输出条款分区。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 读取真实合同
- 输出法律意见
- 写合同系统
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

- auto_renewal
- breach_clause
- dispute_resolution

## Next Step

candidate_pool_continue_smoke

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
