# data_quality_checklist_candidate

## Summary

- Business package: business_reporting
- Scenario: 数据质量检查清单
- Status: mock_callable
- DeepAgents trial fit: mock_only
- DeepAgents smoke status: passed
- Customer callable: false
- Platform deliverable: false
- Count toward 100: true

## Roles

- data_operator
- owner_operator

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

- checklist
- failed_rules
- fields_to_verify
- not_business_conclusion

## Smoke Test Case Zh

mock 表字段含缺失、重复、异常范围，输出检查清单。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 连接数据库
- 写表格
- 做经营结论
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

- key_field_missing
- finance_conflict
- low_confidence

## Next Step

candidate_pool_continue_smoke

## Non Delivery Statement

This candidate is for the SMB candidate library controlled trial only. It is not a stable customer-callable Skill, not platform-deliverable, and not evidence of formal L2 pass unless a separate L2 result says so. Stable customer-callable baseline remains 13 Skills.
