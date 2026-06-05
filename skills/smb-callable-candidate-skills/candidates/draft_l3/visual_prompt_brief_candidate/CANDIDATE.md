# visual_prompt_brief_candidate

## Summary

- Business package: marketing
- Scenario: 视觉提示词 brief
- Status: draft_l3
- DeepAgents trial fit: skill_ready
- Customer callable: false
- Platform deliverable: false
- Formal L2 status: completed

## Roles

- marketing_operator
- creative_designer
- ecommerce_operator

## Source And License

- Source project: eachlabs/skills
- License or origin: MIT product screening passed; formal legal review still required

## Trial Mode

- mock_only
- prompt_brief_only
- read_only
- external_action_blocked

## Output Schema

- prompt_brief
- asset_requirements
- style_constraints
- negative_prompts
- channel_specs
- risk_notes
- manual_review_required

## Smoke Test Case Zh

输入生鲜海报、瑜伽封面或电商主图需求，输出视觉提示词 brief。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 生成图片
- 调用 Eachlabs API
- 声明素材授权
- 承诺商用素材可用
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

- portrait_or_person_asset
- trademark_or_brand_asset
- unclear_copyright
- regulated_industry_promotion

## Non Delivery Statement

This draft L3 candidate is for controlled platform retest only. It is not a stable customer-callable Skill. Stable customer-callable baseline remains 13 Skills.
