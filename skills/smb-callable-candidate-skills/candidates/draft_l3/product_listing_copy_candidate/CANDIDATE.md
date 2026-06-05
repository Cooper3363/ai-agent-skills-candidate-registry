# product_listing_copy_candidate

## Summary

- Business package: ecommerce_store_ops
- Scenario: 电商商品文案草稿
- Status: draft_l3
- DeepAgents trial fit: skill_ready
- Customer callable: false
- Platform deliverable: false
- Formal L2 status: completed

## Roles

- ecommerce_operator
- store_operator
- marketing_operator

## Source And License

- Source project: agricidaniel/claude-seo + internal template boundary
- License or origin: MIT; external SEO/API actions blocked in trial

## Trial Mode

- mock_only
- read_only
- external_action_blocked
- BYOK_required

## Output Schema

- title_options
- bullet_points
- description
- seo_terms
- platform_warnings
- compliance_notes
- missing_inputs
- manual_review_required
- not_seo_guarantee

## Smoke Test Case Zh

输入商品参数、平台约束和禁用表达，输出商品标题、卖点、详情页草稿和风险提示。

## Permission Boundary

- read_only=true
- external_action_blocked=true
- send_allowed=false
- write_allowed=false
- real_api_allowed=false
- real_account_allowed=false

## Forbidden Actions

- 调用 DataForSEO
- 调用 Firecrawl
- 调用 Google API
- 上传商品
- 承诺 SEO 排名
- 承诺销量
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

- food_health
- medical
- education
- finance
- platform_forbidden_terms
- unclear_price_or_inventory

## Non Delivery Statement

This draft L3 candidate is for controlled platform retest only. It is not a stable customer-callable Skill. Stable customer-callable baseline remains 13 Skills.
