# campaign_postmortem_brief_candidate

## Summary

- Business package: marketing_reporting
- Scenario: 活动复盘摘要
- Status: mock_callable
- DeepAgents trial fit: mock_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- campaign_operator
- growth_operator

## Source And License

- Source project: internal_template + structured_metric_summary
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

- summary
- metric_changes
- possible_factors
- data_quality_notes

## Smoke Test Case Zh

活动曝光、点击、转化和销售额 mock 指标，输出复盘摘要。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 确定归因
- 修改预算
- 发布报告
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

- missing_data
- budget
- major_business_advice

## Next Step

keep_component_or_template; formal_l2_result_component_only

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
