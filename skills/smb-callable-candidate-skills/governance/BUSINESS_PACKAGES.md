# 中小微业务包优先级

## 客服

高优先级场景：

- FAQ 带引用回答。
- 投诉、退款、账号安全分流。
- 客服回复安全检查。
- 知识库清洗和分块。
- 客服质量评测。

当前稳交付覆盖：

- `faq_answer_with_citations`
- `support_ticket_classifier`
- `support_reply_guardrail`
- `support_pii_redactor`
- `support_kb_doc_cleaner`

## 销售

高优先级场景：

- 销售跟进草稿。
- CRM 跟进记录结构化。
- 会议纪要和行动项。
- 潜客页面简报。
- 报价异议和下一步建议。

当前稳交付覆盖：

- `crm_note_structurer`

当前候选：

- `sales_followup_draft_candidate`
- `sales_meeting_task_brief_candidate`
- `lead_research_brief_candidate`

## 营销

高优先级场景：

- 营销文案包。
- 活动 brief。
- 视觉 prompt brief。
- 营销合规检查。
- 商品/渠道文案改写。

当前稳交付覆盖：

- `marketing_copy_pack`
- `structured_campaign_brief`
- `marketing_compliance_guard`

当前候选：

- `visual_prompt_brief_candidate`

## 电商 / 门店

高优先级场景：

- 商品标题和详情页草稿。
- 竞品价格快照解析。
- 订单库存异常。
- 门店活动复盘。

当前候选：

- `competitor_product_snapshot_candidate`

## 经营报表

高优先级场景：

- 日报周报。
- 单项指标摘要。
- 指标异常分级。
- 数据质量前置检查。

当前稳交付覆盖：

- `daily_weekly_metrics_reporter`
- `structured_metric_summary`
- `metric_exception_classifier`

## 行政 / 财务 / HR

高优先级场景：

- 票据字段抽取。
- 发票和小票金额一致性提示。
- 简历隐私脱敏。
- 合同条款分区。
- 采购报价对比。

当前稳交付覆盖：

- `expense_invoice_parser`

待后续候选方向：

- `hr_resume_privacy_masker`
- `contract_section_partitioner`
