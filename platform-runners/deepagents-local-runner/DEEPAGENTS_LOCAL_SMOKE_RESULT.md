# DeepAgents Local Smoke Result

Generated: 2026-06-03 17:14:07

## Summary

- Stable customer-callable Skill count remains: 13.
- Discovered stable baseline Skills: 13.
- Discovered draft L3 candidate Skills: 4.
- Total discovered Skills for local DeepAgents smoke: 17.
- Planned mock smoke cases: 25.
- DeepAgents import: ok.
- Model API key: configured.
- OpenAI-compatible base URL: configured.
- Smoke mode: model_smoke.
- Customer-callable additions from this runner: 0.

## Count Warnings

- none

## Inventory

| Skill ID | Library | Status | Source |
| --- | --- | --- | --- |
| crm_note_structurer | stable_baseline | stable_baseline | stable_13 |
| daily_weekly_metrics_reporter | stable_baseline | stable_baseline | stable_13 |
| expense_invoice_parser | stable_baseline | stable_baseline | stable_13 |
| faq_answer_with_citations | stable_baseline | stable_baseline | stable_13 |
| marketing_compliance_guard | stable_baseline | stable_baseline | stable_13 |
| marketing_copy_pack | stable_baseline | stable_baseline | stable_13 |
| metric_exception_classifier | stable_baseline | stable_baseline | stable_13 |
| structured_campaign_brief | stable_baseline | stable_baseline | stable_13 |
| structured_metric_summary | stable_baseline | stable_baseline | stable_13 |
| support_kb_doc_cleaner | stable_baseline | stable_baseline | stable_13 |
| support_pii_redactor | stable_baseline | stable_baseline | stable_13 |
| support_reply_guardrail | stable_baseline | stable_baseline | stable_13 |
| support_ticket_classifier | stable_baseline | stable_baseline | stable_13 |
| sales_followup_draft_candidate | candidate_draft_l3 | draft_l3 | six_department_draft_l3 |
| visual_prompt_brief_candidate | candidate_draft_l3 | draft_l3 | six_department_draft_l3 |
| complaint_escalation_summary_candidate | candidate_draft_l3 | draft_l3 | top8_draft_l3 |
| product_listing_copy_candidate | candidate_draft_l3 | draft_l3 | top8_draft_l3 |

## Model Smoke Results

| Skill ID | Case | Status | Findings |
| --- | --- | --- | --- |
| marketing_copy_pack | 营销文案包 | passed |  |
| daily_weekly_metrics_reporter | 日报周报 | passed |  |
| metric_exception_classifier | 指标异常分类 | passed |  |
| faq_answer_with_citations | FAQ 引用回复 | passed |  |
| support_ticket_classifier | 工单分类 | passed |  |
| structured_campaign_brief | 活动 brief | passed |  |
| structured_metric_summary | 指标摘要 | passed |  |
| crm_note_structurer | CRM 记录 | passed |  |
| support_reply_guardrail | 客服回复防护 | passed |  |
| marketing_compliance_guard | 营销合规检查 | passed |  |
| support_pii_redactor | 客服 PII 脱敏 | passed |  |
| support_kb_doc_cleaner | 知识库清洗 | passed |  |
| expense_invoice_parser | 票据字段抽取 | passed |  |
| visual_prompt_brief_candidate | 生鲜海报视觉 brief | passed |  |
| visual_prompt_brief_candidate | 瑜伽馆小红书封面 brief | passed |  |
| visual_prompt_brief_candidate | 电商主图 brief | passed |  |
| sales_followup_draft_candidate | 试用后微信跟进 | passed |  |
| sales_followup_draft_candidate | 报价后价格异议邮件 | passed |  |
| sales_followup_draft_candidate | 沉睡线索唤醒短信 | passed |  |
| complaint_escalation_summary_candidate | 退款投诉升级 | passed |  |
| complaint_escalation_summary_candidate | 赔偿和监管威胁 | passed |  |
| complaint_escalation_summary_candidate | 隐私投诉摘要 | passed |  |
| product_listing_copy_candidate | 普通商品页 | passed |  |
| product_listing_copy_candidate | 食品商品风险 | passed |  |
| product_listing_copy_candidate | 教育资料风险 | passed |  |

## Boundaries

- This runner does not expose business action tools.
- No email, SMS, CRM, OAuth, calendar, task, support system, ecommerce upload, refund, inventory write, crawl, SEO API, or image generation tool is provided.
- Stable baseline smoke does not rerun platform acceptance.
- Draft L3 smoke does not promote candidates to stable delivery.
