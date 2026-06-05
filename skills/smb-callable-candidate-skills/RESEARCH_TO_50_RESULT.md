# Research To 50 Result

生成日期：2026-06-03

说明：本文件为 AI.Skills 指挥中心临时收口版 v0。由于研究窗口长时间停留在落盘阶段，为避免许可证窗口、测试台继续空等，先提供可执行研究结果。若研究窗口后续产出正式版本，以正式版本合并或覆盖本文件。

## 结论

- 当前候选库已有候选卡：7 个。
- 第一阶段目标：达到 50 个可试跑候选。
- 本文件输出 70 个候选线索，并推荐其中 43 个进入许可证 / trial mode 复核。
- 本轮不送 L2、不封装、不改稳交付 13 个包。
- 客户正式可调用 Skill 数量仍为 13。

## 推荐 43 个候选业务包分布

| 业务包 | 推荐数量 |
| --- | ---: |
| 客服 | 8 |
| 销售 | 6 |
| 营销 | 7 |
| 电商/门店 | 7 |
| 经营报表 | 7 |
| 行政/财务/HR | 8 |

叠加当前 7 张候选卡后，第一阶段可达到 50 个可试跑候选目标。

## 推荐进入许可证 / Trial Mode 复核的 43 个候选

| candidate_id | 业务包 | 适配角色 | 场景 | 来源类型 | 来源链接或复用关系 | 是否被 13 个稳交付覆盖 | 建议状态 | deepagents_trial_fit | 中文 smoke 用例一句话 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| support_quality_eval_candidate | 客服 | 客服主管 | 客服对话评分与培训建议 | internal_template / existing_skill_combo | 复用 support_reply_guardrail + support_ticket_classifier + support_pii_redactor | 部分覆盖 | component_only | component_only | 输入退款投诉对话，输出评分、违规项、培训建议和转人工原因 |
| refund_policy_reply_draft_candidate | 客服 | 售后客服 | 退款政策回复草稿 | internal_template | 内部模板，不复用第三方代码 | 部分覆盖 | mock_callable | mock_only | 输入客户退款诉求和政策片段，输出不承诺退款的回复草稿 |
| account_security_handoff_candidate | 客服 | 账号安全客服 | 账号被盗/验证码失败转人工 | internal_template | 复用 support_reply_guardrail | 部分覆盖 | mock_callable | mock_only | 输入账号被盗求助，输出安全转人工原因和禁止绕验证提示 |
| support_macro_suggester_candidate | 客服 | 客服运营 | 从知识库生成客服快捷话术 | internal_template | 复用 faq_answer_with_citations + support_kb_doc_cleaner | 部分覆盖 | mock_callable | mock_only | 输入 FAQ 条目，输出 3 条带边界的客服快捷回复 |
| support_sentiment_priority_candidate | 客服 | 客服主管 | 客户情绪与优先级判断 | internal_template | 复用 support_ticket_classifier | 部分覆盖 | mock_callable | mock_only | 输入投诉文本，输出情绪、优先级、风险标签 |
| aftersales_return_checklist_candidate | 客服 | 售后专员 | 退换货核查清单 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入退货原因和订单状态，输出核查步骤和人工复核触发 |
| support_knowledge_gap_detector_candidate | 客服 | 知识库运营 | 识别客服问题中的知识库缺口 | internal_template | 复用 faq_answer_with_citations | 部分覆盖 | mock_callable | mock_only | 输入未命中问题列表，输出缺口主题和补文档建议 |
| complaint_root_cause_cluster_candidate | 客服 | 客诉主管 | 投诉原因聚类 | internal_template | 可复用 complaint_escalation_summary_candidate | 部分覆盖 | mock_callable | mock_only | 输入 10 条 mock 投诉，输出原因聚类和代表性脱敏引用 |
| quote_objection_response_candidate | 销售 | 销售顾问 | 报价异议回复草稿 | internal_template | 复用 crm_note_structurer + sales_followup_draft_candidate | 部分覆盖 | mock_callable | mock_only | 输入客户嫌贵和折扣边界，输出不越权的跟进草稿 |
| proposal_outline_candidate | 销售 | 商务支持 | 轻量方案书大纲 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入客户行业和需求，输出方案大纲、缺失信息和风险提示 |
| sales_call_summary_candidate | 销售 | 销售主管 | 销售电话纪要结构化 | internal_template | 复用 crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入 mock 通话记录，输出需求、异议、下一步和人工复核 |
| deal_risk_flagger_candidate | 销售 | 销售运营 | 商机风险标记 | internal_template | 复用 crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入商机备注，输出价格、合同、付款等风险标签 |
| renewal_reminder_draft_candidate | 销售 | 客户成功 | 续费提醒草稿 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入到期时间和使用摘要，输出 send_allowed=false 的续费提醒草稿 |
| sales_playbook_step_candidate | 销售 | 销售主管 | 下一步销售动作建议 | internal_template | 复用 crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入销售阶段和客户反馈，输出下一步建议和禁止承诺 |
| social_post_repurpose_candidate | 营销 | 内容运营 | 长文改写社媒帖 | internal_template | 复用 marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入活动长文，输出小红书/朋友圈/公众号短文草稿 |
| ad_variant_brief_candidate | 营销 | 投放运营 | 广告变体 brief | internal_template | 复用 marketing_copy_pack + marketing_compliance_guard | 部分覆盖 | mock_callable | mock_only | 输入产品卖点和禁用词，输出 5 个广告变体和合规提示 |
| campaign_postmortem_brief_candidate | 营销 | 运营主管 | 活动复盘摘要 | internal_template | 复用 structured_metric_summary | 部分覆盖 | mock_callable | mock_only | 输入 mock 活动指标，输出复盘摘要、问题和下一步 |
| brand_tone_rewriter_candidate | 营销 | 品牌运营 | 品牌语气改写 | internal_template | 部分复用 marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入不符合品牌语气的文案，输出改写和保留点 |
| channel_copy_adapter_candidate | 营销 | 内容运营 | 多渠道文案适配 | internal_template | 复用 marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入同一活动 brief，输出微信、短信、海报短文案 |
| marketing_claim_risk_tagger_candidate | 营销 | 合规运营 | 营销承诺风险打标 | internal_template | 复用 marketing_compliance_guard | 覆盖较多 | component_only | component_only | 输入食品/教育文案，输出绝对化、功效、结果承诺风险 |
| content_calendar_mock_candidate | 营销 | 内容运营 | 内容日历草案 | internal_template | 部分复用 structured_campaign_brief | 部分覆盖 | dry_run_callable | dry_run_only | 输入 4 周主题和渠道，输出不写日历的内容排期草案 |
| order_inventory_exception_candidate | 电商/门店 | 店铺运营 | 订单库存异常识别 | GitHub / internal dry-run | claude-office-skills shopify-automation；仅 mock/dry-run | 否 | dry_run_callable | dry_run_only | 输入 mock 订单和库存表，输出异常类型和核查步骤 |
| review_sentiment_cluster_candidate | 电商/门店 | 店铺运营 | 商品评价聚类 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入 20 条 mock 评价，输出好评点、差评点和行动建议 |
| return_reason_cluster_candidate | 电商/门店 | 售后运营 | 退货原因聚类 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入 mock 退货原因，输出聚类、代表性引用和复核触发 |
| store_daily_brief_candidate | 电商/门店 | 店长 | 门店日报老板摘要 | internal_template / existing_skill_combo | 复用 daily_weekly_metrics_reporter | 部分覆盖 | mock_callable | mock_only | 输入门店营收、客流和库存指标，输出日报摘要 |
| sku_margin_risk_candidate | 电商/门店 | 商品运营 | SKU 毛利异常提示 | internal_template | 复用 metric_exception_classifier | 部分覆盖 | mock_callable | mock_only | 输入 SKU 成本和售价，输出毛利风险和核查步骤 |
| marketplace_policy_warning_candidate | 电商/门店 | 商品运营 | 平台禁词/政策提示 | internal_template | 复用 marketing_compliance_guard | 部分覆盖 | mock_callable | mock_only | 输入商品文案和平台，输出禁词和人工复核 |
| fulfillment_delay_notice_draft_candidate | 电商/门店 | 售后客服 | 延迟发货通知草稿 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入延迟原因和订单状态，输出不发送的通知草稿 |
| boss_daily_brief_candidate | 经营报表 | 老板/店长 | 老板日报摘要 | internal_template / existing_skill_combo | 复用 daily_weekly_metrics_reporter | 覆盖较多 | mock_callable | mock_only | 输入 mock 经营指标，输出老板可读摘要和异常 |
| cashflow_warning_brief_candidate | 经营报表 | 财务/老板 | 现金流预警摘要 | internal_template | 复用 structured_metric_summary | 部分覆盖 | mock_callable | mock_only | 输入应收应付和余额，输出现金流风险，不做财务建议 |
| funnel_dropoff_summary_candidate | 经营报表 | 运营 | 漏斗流失摘要 | internal_template | 复用 metric_exception_classifier | 部分覆盖 | mock_callable | mock_only | 输入访问、咨询、下单漏斗，输出掉点和核查步骤 |
| data_quality_checklist_candidate | 经营报表 | 数据运营 | 数据质量检查清单 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入指标表字段，输出缺失、口径冲突和核查建议 |
| campaign_metric_anomaly_candidate | 经营报表 | 营销运营 | 活动指标异常摘要 | internal_template | 复用 metric_exception_classifier | 部分覆盖 | mock_callable | mock_only | 输入活动前后指标，输出异常类型和可能因素 |
| customer_cohort_summary_candidate | 经营报表 | 运营 | 用户分群摘要 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入 mock 分群数据，输出分群洞察和样本量提醒 |
| inventory_turnover_brief_candidate | 经营报表 | 店铺运营 | 库存周转摘要 | internal_template | 部分复用 order_inventory_exception_candidate | 部分覆盖 | mock_callable | mock_only | 输入 SKU 库存和销量，输出周转异常和核查步骤 |
| hr_resume_privacy_masker_candidate | 行政/财务/HR | HR | 简历隐私脱敏 | GitHub / existing_skill_combo | Microsoft Presidio + support_pii_redactor | 部分覆盖 | mock_callable | mock_only | 输入 mock 简历，输出脱敏文本和实体列表 |
| contract_clause_partitioner_candidate | 行政/财务/HR | 行政/法务助理 | 合同条款分区 | internal_template | 内部模板；not_legal_advice | 否 | mock_callable | mock_only | 输入 mock 合同文本，输出条款分区和非法律意见提示 |
| purchase_quote_compare_candidate | 行政/财务/HR | 采购 | 采购报价对比 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入三家报价，输出价格/交期/风险对比 |
| meeting_minutes_action_candidate | 行政/财务/HR | 行政 | 会议纪要行动项 | internal_template | 复用 sales_meeting_task_brief_candidate | 部分覆盖 | dry_run_callable | dry_run_only | 输入会议纪要，输出行动项和 dry-run 任务草案 |
| reimbursement_policy_check_candidate | 行政/财务/HR | 财务 | 报销材料完整性检查 | internal_template | 复用 expense_invoice_parser | 部分覆盖 | mock_callable | mock_only | 输入 mock 报销文本，输出缺失材料，不做报销结论 |
| invoice_amount_consistency_candidate | 行政/财务/HR | 财务 | 发票/小票金额一致性 | internal_template | 复用 expense_invoice_parser | 部分覆盖 | component_only | component_only | 输入 mock OCR 文本，输出金额一致性和人工复核 |
| sop_step_extractor_candidate | 行政/财务/HR | 行政 | SOP 步骤提取 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入杂乱 SOP 文档，输出步骤、负责人和缺口 |
| onboarding_checklist_candidate | 行政/财务/HR | HR/行政 | 入职清单草案 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入岗位和入职日期，输出不写系统的入职清单 |

## 70 个候选线索总表

| # | candidate_id | 业务包 | 适配角色 | 场景 | 来源类型 | 来源链接或复用关系 | 覆盖关系 | 建议状态 | deepagents_trial_fit | 中文 smoke 用例一句话 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | support_quality_eval_candidate | 客服 | 客服主管 | 客服对话评分与培训建议 | internal_template | support_reply_guardrail + support_ticket_classifier + support_pii_redactor | 部分覆盖 | component_only | component_only | 输入退款投诉对话，输出质检评分和培训建议 |
| 2 | refund_policy_reply_draft_candidate | 客服 | 售后客服 | 退款政策回复草稿 | internal_template | 内部模板 | 部分覆盖 | mock_callable | mock_only | 输入退款诉求，输出不承诺退款的回复草稿 |
| 3 | account_security_handoff_candidate | 客服 | 账号安全客服 | 账号安全转人工 | internal_template | support_reply_guardrail | 部分覆盖 | mock_callable | mock_only | 输入账号被盗，输出转人工原因 |
| 4 | support_macro_suggester_candidate | 客服 | 客服运营 | 快捷话术生成 | internal_template | faq_answer_with_citations | 部分覆盖 | mock_callable | mock_only | 输入 FAQ，输出客服快捷话术 |
| 5 | support_sentiment_priority_candidate | 客服 | 客服主管 | 情绪与优先级判断 | internal_template | support_ticket_classifier | 部分覆盖 | mock_callable | mock_only | 输入投诉文本，输出情绪和优先级 |
| 6 | aftersales_return_checklist_candidate | 客服 | 售后专员 | 退换货核查清单 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入退货原因，输出核查步骤 |
| 7 | support_knowledge_gap_detector_candidate | 客服 | 知识库运营 | 知识库缺口识别 | internal_template | faq_answer_with_citations | 部分覆盖 | mock_callable | mock_only | 输入未命中问题，输出补文档建议 |
| 8 | complaint_root_cause_cluster_candidate | 客服 | 客诉主管 | 投诉原因聚类 | internal_template | complaint_escalation_summary_candidate | 部分覆盖 | mock_callable | mock_only | 输入多条投诉，输出原因聚类 |
| 9 | support_reply_flow_candidate | 客服 | 售前/售后客服 | 客服回复流程 | GitHub | asgard-ai-platform/skills | 稳交付覆盖较多 | needs_license_review | mock_only | 输入客服问题，输出流程草案 |
| 10 | faq_article_outline_candidate | 客服 | 知识库运营 | FAQ 文档大纲 | internal_template | support_kb_doc_cleaner | 部分覆盖 | mock_callable | mock_only | 输入客服问答，输出 FAQ 大纲 |
| 11 | escalation_sla_classifier_candidate | 客服 | 客服主管 | SLA 升级分级 | internal_template | support_ticket_classifier | 部分覆盖 | mock_callable | mock_only | 输入工单，输出 SLA 等级 |
| 12 | privacy_complaint_summary_candidate | 客服 | 隐私客服 | 隐私投诉摘要 | internal_template | support_pii_redactor | 部分覆盖 | mock_callable | mock_only | 输入隐私投诉，输出脱敏摘要 |
| 13 | quote_objection_response_candidate | 销售 | 销售顾问 | 报价异议回复 | internal_template | crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入价格异议，输出回复草稿 |
| 14 | proposal_outline_candidate | 销售 | 商务支持 | 方案书大纲 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入客户需求，输出方案大纲 |
| 15 | sales_call_summary_candidate | 销售 | 销售主管 | 销售电话纪要 | internal_template | crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入通话记录，输出纪要 |
| 16 | deal_risk_flagger_candidate | 销售 | 销售运营 | 商机风险打标 | internal_template | crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入商机备注，输出风险标签 |
| 17 | renewal_reminder_draft_candidate | 销售 | 客户成功 | 续费提醒草稿 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入到期信息，输出提醒草稿 |
| 18 | sales_playbook_step_candidate | 销售 | 销售主管 | 下一步动作建议 | internal_template | crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入销售阶段，输出下一步 |
| 19 | sales_meeting_task_brief_candidate | 销售 | 销售助理 | 会议任务草案 | existing_candidate | 当前 component card | 已存在候选 | component_only | component_only | 输入会议纪要，输出任务草案 |
| 20 | lead_research_brief_candidate | 销售 | 销售顾问 | 潜客简报 | existing_candidate | 当前 component card | 已存在候选 | component_only | component_only | 输入页面文本，输出潜客简报 |
| 21 | sales_followup_draft_candidate | 销售 | 销售顾问 | 销售跟进草稿 | existing_candidate | 当前 draft_l3 | 已存在候选 | draft_l3 | skill_ready | 输入试用信息，输出跟进草稿 |
| 22 | crm_field_gap_detector_candidate | 销售 | 销售运营 | CRM 字段缺口提示 | internal_template | crm_note_structurer | 部分覆盖 | mock_callable | mock_only | 输入销售记录，输出缺失字段 |
| 23 | social_post_repurpose_candidate | 营销 | 内容运营 | 长文转社媒帖 | internal_template | marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入长文，输出社媒帖 |
| 24 | ad_variant_brief_candidate | 营销 | 投放运营 | 广告变体 brief | internal_template | marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入卖点，输出广告变体 |
| 25 | campaign_postmortem_brief_candidate | 营销 | 运营主管 | 活动复盘 | internal_template | structured_metric_summary | 部分覆盖 | mock_callable | mock_only | 输入活动指标，输出复盘 |
| 26 | brand_tone_rewriter_candidate | 营销 | 品牌运营 | 品牌语气改写 | internal_template | marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入文案，输出品牌语气改写 |
| 27 | channel_copy_adapter_candidate | 营销 | 内容运营 | 多渠道文案适配 | internal_template | marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入活动 brief，输出多渠道文案 |
| 28 | marketing_claim_risk_tagger_candidate | 营销 | 合规运营 | 营销承诺风险 | internal_template | marketing_compliance_guard | 覆盖较多 | component_only | component_only | 输入文案，输出风险标签 |
| 29 | content_calendar_mock_candidate | 营销 | 内容运营 | 内容日历草案 | internal_template | structured_campaign_brief | 部分覆盖 | dry_run_callable | dry_run_only | 输入主题，输出日历草案 |
| 30 | visual_prompt_brief_candidate | 营销 | 设计/运营 | 视觉 prompt brief | existing_candidate | 当前 draft_l3 | 已存在候选 | draft_l3 | skill_ready | 输入海报需求，输出视觉 brief |
| 31 | product_listing_copy_candidate | 营销 | 商品运营 | 商品文案 | existing_candidate | 当前 draft_l3 | 已存在候选 | draft_l3 | skill_ready | 输入商品参数，输出商品页草稿 |
| 32 | landing_page_copy_outline_candidate | 营销 | 运营 | 落地页文案大纲 | internal_template | marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入产品和人群，输出落地页大纲 |
| 33 | newsletter_draft_candidate | 营销 | 内容运营 | 会员 newsletter 草稿 | internal_template | marketing_copy_pack | 部分覆盖 | dry_run_callable | dry_run_only | 输入主题，输出不发送的邮件草稿 |
| 34 | order_inventory_exception_candidate | 电商/门店 | 店铺运营 | 订单库存异常 | GitHub / internal dry-run | shopify-automation | 否 | dry_run_callable | dry_run_only | 输入订单库存表，输出异常 |
| 35 | review_sentiment_cluster_candidate | 电商/门店 | 店铺运营 | 评价聚类 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入评价，输出聚类 |
| 36 | return_reason_cluster_candidate | 电商/门店 | 售后运营 | 退货原因聚类 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入退货原因，输出聚类 |
| 37 | store_daily_brief_candidate | 电商/门店 | 店长 | 门店日报 | internal_template | daily_weekly_metrics_reporter | 部分覆盖 | mock_callable | mock_only | 输入门店指标，输出日报 |
| 38 | sku_margin_risk_candidate | 电商/门店 | 商品运营 | SKU 毛利风险 | internal_template | metric_exception_classifier | 部分覆盖 | mock_callable | mock_only | 输入 SKU 成本售价，输出风险 |
| 39 | marketplace_policy_warning_candidate | 电商/门店 | 商品运营 | 平台政策提示 | internal_template | marketing_compliance_guard | 部分覆盖 | mock_callable | mock_only | 输入商品文案，输出平台风险 |
| 40 | fulfillment_delay_notice_draft_candidate | 电商/门店 | 售后客服 | 延迟发货通知草稿 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入延迟原因，输出通知草稿 |
| 41 | competitor_product_snapshot_candidate | 电商/门店 | 店铺运营 | 竞品快照 | existing_candidate | 当前 component card | 已存在候选 | component_only | component_only | 输入 mock 快照，输出价格变化 |
| 42 | ecommerce_metric_brief_candidate | 电商/门店 | 电商运营 | 电商指标摘要 | existing_skill_combo | 经营报表 3 件套 | 覆盖较多 | market_lead | not_suitable | 输入商品指标，输出摘要 |
| 43 | stockout_customer_notice_candidate | 电商/门店 | 店铺客服 | 缺货通知草稿 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入缺货信息，输出通知草稿 |
| 44 | boss_daily_brief_candidate | 经营报表 | 老板/店长 | 老板日报 | existing_skill_combo | daily_weekly_metrics_reporter | 覆盖较多 | mock_callable | mock_only | 输入指标，输出老板摘要 |
| 45 | cashflow_warning_brief_candidate | 经营报表 | 财务/老板 | 现金流预警 | internal_template | structured_metric_summary | 部分覆盖 | mock_callable | mock_only | 输入应收应付，输出风险 |
| 46 | funnel_dropoff_summary_candidate | 经营报表 | 运营 | 漏斗流失摘要 | internal_template | metric_exception_classifier | 部分覆盖 | mock_callable | mock_only | 输入漏斗指标，输出掉点 |
| 47 | data_quality_checklist_candidate | 经营报表 | 数据运营 | 数据质量检查 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入字段表，输出质量问题 |
| 48 | campaign_metric_anomaly_candidate | 经营报表 | 营销运营 | 活动指标异常 | internal_template | metric_exception_classifier | 部分覆盖 | mock_callable | mock_only | 输入活动指标，输出异常 |
| 49 | customer_cohort_summary_candidate | 经营报表 | 运营 | 用户分群摘要 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入分群数据，输出洞察 |
| 50 | inventory_turnover_brief_candidate | 经营报表 | 店铺运营 | 库存周转摘要 | internal_template | order_inventory_exception_candidate | 部分覆盖 | mock_callable | mock_only | 输入库存销量，输出周转风险 |
| 51 | operations_metric_brief_candidate | 经营报表 | 老板/运营 | 运营指标 brief | existing_skill_combo | 报表 3 件套 | 覆盖较多 | market_lead | not_suitable | 输入指标，输出摘要 |
| 52 | revenue_leakage_hint_candidate | 经营报表 | 财务/运营 | 收入漏损提示 | internal_template | metric_exception_classifier | 部分覆盖 | mock_callable | mock_only | 输入订单支付差异，输出核查建议 |
| 53 | unit_economics_brief_candidate | 经营报表 | 老板 | 单位经济摘要 | internal_template | structured_metric_summary | 部分覆盖 | mock_callable | mock_only | 输入成本收入，输出摘要 |
| 54 | hr_resume_privacy_masker_candidate | 行政/财务/HR | HR | 简历脱敏 | GitHub / existing_skill_combo | Presidio + support_pii_redactor | 部分覆盖 | mock_callable | mock_only | 输入 mock 简历，输出脱敏 |
| 55 | contract_clause_partitioner_candidate | 行政/财务/HR | 行政/法务助理 | 合同条款分区 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入合同，输出条款分区 |
| 56 | purchase_quote_compare_candidate | 行政/财务/HR | 采购 | 报价对比 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入报价，输出对比 |
| 57 | meeting_minutes_action_candidate | 行政/财务/HR | 行政 | 会议行动项 | internal_template | sales_meeting_task_brief_candidate | 部分覆盖 | dry_run_callable | dry_run_only | 输入纪要，输出行动项 |
| 58 | reimbursement_policy_check_candidate | 行政/财务/HR | 财务 | 报销材料完整性 | internal_template | expense_invoice_parser | 部分覆盖 | mock_callable | mock_only | 输入报销文本，输出缺失材料 |
| 59 | invoice_amount_consistency_candidate | 行政/财务/HR | 财务 | 金额一致性 | internal_template | expense_invoice_parser | 部分覆盖 | component_only | component_only | 输入票据文本，输出金额校验 |
| 60 | sop_step_extractor_candidate | 行政/财务/HR | 行政 | SOP 步骤提取 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入 SOP，输出步骤 |
| 61 | onboarding_checklist_candidate | 行政/财务/HR | HR/行政 | 入职清单草案 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入岗位，输出清单 |
| 62 | invoice_receipt_review_candidate | 行政/财务/HR | 财务 | 票据复核 | existing_skill_combo | expense_invoice_parser | 覆盖较多 | market_lead | not_suitable | 输入票据文本，输出字段 |
| 63 | contract_section_review_candidate | 行政/财务/HR | 法务助理 | 合同风险线索 | internal_template | not_legal_advice | 否 | market_lead | mock_only | 输入合同，输出非法律风险线索 |
| 64 | employee_handbook_qa_candidate | 行政/财务/HR | HR | 员工手册问答 | internal_template | faq_answer_with_citations | 部分覆盖 | mock_callable | mock_only | 输入制度片段，输出带引用回答 |
| 65 | vendor_onboarding_check_candidate | 行政/财务/HR | 采购/行政 | 供应商资料检查 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入供应商资料，输出缺失项 |
| 66 | privacy_policy_summary_candidate | 行政/财务/HR | 行政/合规 | 隐私政策摘要 | internal_template | support_pii_redactor | 部分覆盖 | mock_callable | mock_only | 输入政策，输出摘要和人工复核 |
| 67 | payroll_question_router_candidate | 行政/财务/HR | HR | 薪酬问题分流 | internal_template | 内部模板 | 否 | dry_run_callable | dry_run_only | 输入薪酬问题，输出转人工原因 |
| 68 | training_material_outline_candidate | 行政/财务/HR | HR/培训 | 培训材料大纲 | internal_template | marketing_copy_pack | 部分覆盖 | mock_callable | mock_only | 输入培训目标，输出大纲 |
| 69 | asset_request_form_checker_candidate | 行政/财务/HR | 行政 | 资产申请完整性 | internal_template | 内部模板 | 否 | mock_callable | mock_only | 输入资产申请，输出缺失信息 |
| 70 | policy_change_brief_candidate | 行政/财务/HR | 行政 | 制度变更摘要 | internal_template | support_kb_doc_cleaner | 部分覆盖 | mock_callable | mock_only | 输入制度变更文本，输出摘要 |

## 禁止与边界

- 本轮只做研究收口，不送 L2、不封装、不新增客户可调用。
- 高风险外部动作默认仅允许 mock/dry-run：邮件、短信、CRM/OAuth、日历、任务、财务、合同、薪酬、网页抓取、图片/视频生成。
- `market_lead` 不计入 100 个可试跑候选。
- `needs_license_review` 未放行前不计入 100 个可试跑候选。

## 建议许可证窗口下一步

- 优先复核推荐 43 个候选。
- 内部模板类重点确认：不复用第三方代码，可走 internal_template + mock_only。
- GitHub/外部来源类重点确认：许可证、商用限制、依赖/API/模型条款、trial mode。
- 对 `dry_run_callable` 候选统一标注 `external_action_blocked`。
