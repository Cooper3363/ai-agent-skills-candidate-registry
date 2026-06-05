# DeepAgents Candidate Smoke To 50 Result

回传时间：2026-06-03

## 结论

本轮已按更新后的 `LICENSE_REVIEW_TO_50_RESULT.md` 对 40 个 L1 / trial mode 放行候选完成 DeepAgents candidate smoke。

本轮 smoke 为候选库可试跑判断，不是正式 L2，不代表客户正式可调用。

## 输入

- `LICENSE_REVIEW_TO_50_RESULT.md`
- `queues/DEEPAGENTS_SMOKE_TO_50_QUEUE.md`
- `platform-runners/deepagents-local-runner`

## 执行边界

- 未安装额外业务依赖。
- 未访问真实账号。
- 未调用真实业务 API。
- 未发送邮件、短信或微信。
- 未写 CRM、日历、任务或业务系统。
- 未抓取真实网页。
- 未上传、未退款、未改库存。
- 未生成真实图片、视频、音频、OCR 或 PDF 结果。
- 未改稳交付 13 个包。

## 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| passed | 40 |
| failed | 0 |
| needs_fix | 0 |
| blocked | 0 |

## component_only 处理

以下 3 个候选按许可证窗口结论进入组件池，不独立执行 DeepAgents candidate smoke，不计入 40 个可试跑候选：

| candidate_id | 处理 |
| --- | --- |
| `support_quality_eval_candidate` | component_only，客服质检组合组件 |
| `marketing_claim_risk_tagger_candidate` | component_only，营销合规标签组件 |
| `invoice_amount_consistency_candidate` | component_only，票据金额一致性组件 |

## Smoke 表

| candidate_id | business_package | role | scenario | source_project | trial_mode | mock 输入摘要 | 预期输出字段 | 禁止动作 | 人工复核触发 | smoke_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `refund_policy_reply_draft_candidate` | 客服 | 售后客服 | 退款政策回复草稿 | internal_template | mock_only/read_only/external_action_blocked | 客户要求退款并威胁投诉，给 mock 退款政策 | `reply_draft`, `policy_basis`, `risk_flags`, `handoff_required` | 不承诺退款/赔偿，不回访，不写工单 | 退款、投诉、赔偿 | passed |
| `account_security_handoff_candidate` | 客服 | 账号安全客服 | 账号被盗转人工 | internal_template + `support_reply_guardrail` | mock_only/read_only/external_action_blocked | 客户称账号被盗且收不到验证码 | `safe_reply`, `handoff_reason`, `risk_flags`, `forbidden_steps` | 不绕验证，不改账号，不索要密码 | 账号恢复、身份验证失败、隐私 | passed |
| `support_macro_suggester_candidate` | 客服 | 客服主管 | FAQ 话术建议 | internal_template + `faq_answer_with_citations` | mock_only/read_only/external_action_blocked | 基于 mock FAQ 生成发票申请话术 | `macro_draft`, `citations`, `missing_info`, `risk_notes` | 不编造政策，不写知识库 | 无引用、低置信、政策冲突 | passed |
| `support_sentiment_priority_candidate` | 客服 | 工单分流 | 情绪与优先级判断 | internal_template + `support_ticket_classifier` | mock_only/read_only/external_action_blocked | 投诉文本含愤怒、退款、差评威胁 | `sentiment`, `priority`, `risk_flags`, `suggested_owner` | 不处理退款，不自动升级系统 | 投诉、退款、隐私、极端情绪 | passed |
| `aftersales_return_checklist_candidate` | 客服 | 售后客服 | 退换货核查清单 | internal_template | mock_only/read_only/external_action_blocked | 商品损坏退货，输入订单状态和售后规则 | `checklist`, `required_info`, `blocked_actions`, `handoff_required` | 不退款，不赔付，不改售后状态 | 金额争议、质量投诉、缺凭证 | passed |
| `support_knowledge_gap_detector_candidate` | 客服 | 知识库运营 | 知识库缺口识别 | internal_template + `faq_answer_with_citations` | mock_only/read_only/external_action_blocked | 多个客户问营业时间但 FAQ 无答案 | `gap_topics`, `example_questions`, `suggested_kb_entries`, `confidence` | 不自动改知识库，不编答案 | 低置信、客户隐私、重复投诉 | passed |
| `complaint_root_cause_cluster_candidate` | 客服 | 投诉运营 | 投诉根因聚类 | internal_template | mock_only/read_only/external_action_blocked | 10 条脱敏投诉文本，含物流慢和质量差 | `clusters`, `root_cause_hypotheses`, `representative_quotes`, `sample_notes` | 不做赔偿结论，不联系客户 | 投诉、退款、样本过小、PII | passed |
| `quote_objection_response_candidate` | 销售 | 销售代表 | 报价异议回复 | internal_template + `crm_note_structurer` | mock_only/read_only/external_action_blocked | 客户认为年费贵，销售政策不允许超 9 折 | `reply_draft`, `value_points`, `discount_boundary`, `risk_notes` | 不承诺折扣，不改合同，不发消息 | 折扣、合同、付款条款 | passed |
| `proposal_outline_candidate` | 销售 | 售前顾问 | 方案书大纲 | internal_template | mock_only/read_only/external_action_blocked | 教培客户需要排课、签到、学员管理方案 | `outline`, `sections`, `assumptions`, `missing_info` | 不生成合同，不承诺报价 | 合同、报价、实施周期 | passed |
| `sales_call_summary_candidate` | 销售 | 销售代表 | 通话记录摘要 | internal_template + `crm_note_structurer` | mock_only/read_only/external_action_blocked | mock 通话文本含需求、异议、下次跟进 | `summary`, `needs`, `objections`, `next_actions`, `risk_flags` | 不处理真实音频，不写 CRM | 价格、合同、个人信息 | passed |
| `deal_risk_flagger_candidate` | 销售 | 销售运营 | 商机风险标签 | internal_template + `crm_note_structurer` | mock_only/read_only/external_action_blocked | 商机记录含拖延付款、强折扣、合同修改 | `risk_flags`, `severity`, `evidence`, `suggested_review` | 不推进流程，不改 CRM | 合同、付款、折扣、低置信 | passed |
| `renewal_reminder_draft_candidate` | 销售 | 客户成功 | 续费提醒草稿 | internal_template | dry_run_only/read_only/external_action_blocked | 客户订阅 7 天后到期，生成续费提醒 | `message_draft`, `send_allowed`, `write_allowed`, `external_action_blocked` | 不发送，不写 CRM，不创建任务 | 价格、合同、客户拒收 | passed |
| `sales_playbook_step_candidate` | 销售 | 销售主管 | 下一步销售动作建议 | internal_template + `crm_note_structurer` | mock_only/read_only/external_action_blocked | 线索处于试用后未回复阶段 | `stage`, `recommended_step`, `talking_points`, `risk_notes` | 不自动推进销售流程 | 折扣、合同、投诉、拒绝触达 | passed |
| `social_post_repurpose_candidate` | 营销 | 内容运营 | 内容转社媒草稿 | internal_template + `marketing_copy_pack` | mock_only/read_only/external_action_blocked | 把公众号活动文案改成小红书和朋友圈 | `channel_variants`, `ctas`, `compliance_notes`, `missing_info` | 不发布，不抓素材 | 版权、平台规则、敏感行业 | passed |
| `ad_variant_brief_candidate` | 营销 | 投放运营 | 广告变体 brief | internal_template + `marketing_copy_pack`/`marketing_compliance_guard` | mock_only/read_only/external_action_blocked | 为瑜伽体验课生成 3 个广告角度 | `variant_briefs`, `claims_to_avoid`, `risk_flags`, `review_required` | 不投放，不承诺效果 | 医疗、教育、金融、绝对化 | passed |
| `campaign_postmortem_brief_candidate` | 营销 | 活动运营 | 活动复盘摘要 | internal_template + `structured_metric_summary` | mock_only/read_only/external_action_blocked | 活动曝光、点击、转化和销售额 mock 指标 | `summary`, `metric_changes`, `possible_factors`, `data_quality_notes` | 不做确定归因，不改预算 | 数据缺失、预算、重大经营建议 | passed |
| `brand_tone_rewriter_candidate` | 营销 | 品牌运营 | 品牌语气改写 | internal_template + `marketing_copy_pack` | mock_only/read_only/external_action_blocked | 把硬广改成温和专业语气 | `rewritten_copy`, `tone_notes`, `kept_terms`, `risk_notes` | 不使用第三方品牌素材 | 商标、品牌规范、敏感行业 | passed |
| `channel_copy_adapter_candidate` | 营销 | 内容运营 | 多渠道文案适配 | internal_template + `marketing_copy_pack` | mock_only/read_only/external_action_blocked | 把一段促销文案适配公众号、短信、朋友圈 | `channel_versions`, `length_notes`, `send_allowed`, `risk_notes` | 不发布，不发送短信 | 平台规则、短信授权、价格 | passed |
| `content_calendar_mock_candidate` | 营销 | 内容运营 | 内容日历草案 | internal_template + `structured_campaign_brief` | dry_run_only/read_only/external_action_blocked | 生成 4 周内容日历草案 | `calendar_items`, `write_allowed`, `send_allowed`, `external_action_blocked` | 不写日历/任务/发布系统 | 价格、库存、节假日真实性 | passed |
| `order_inventory_exception_candidate` | 电商 | 店铺运营 | 订单库存异常 dry-run | `claude-office-skills/shopify-automation` + internal dry-run | dry_run_only/read_only/BYOK_required/external_action_blocked | mock 订单显示库存不足和负库存 | `exceptions`, `affected_skus`, `verification_steps`, `write_allowed` | 不调 Shopify，不改库存，不发通知 | 大额订单、负库存、供应商冲突 | passed |
| `review_sentiment_cluster_candidate` | 电商 | 商品运营 | 商品评价情绪聚类 | internal_template | mock_only/read_only/external_action_blocked | 20 条 mock 商品评价，含质量/物流/客服 | `clusters`, `sentiment_summary`, `representative_quotes`, `pii_notes` | 不联系买家，不删评 | PII、恶意评价、样本过小 | passed |
| `return_reason_cluster_candidate` | 电商 | 售后运营 | 退货原因聚类 | internal_template | mock_only/read_only/external_action_blocked | mock 退货原因含尺码、质量、物流破损 | `reason_clusters`, `counts`, `examples`, `action_notes` | 不退款，不改售后状态 | 质量投诉、退款、隐私 | passed |
| `store_daily_brief_candidate` | 经营报表 | 店长 | 门店日报摘要 | internal_template + `daily_weekly_metrics_reporter` | mock_only/read_only/external_action_blocked | 门店营收、订单、客单价、缺货数据 | `daily_summary`, `key_metrics`, `anomalies`, `data_quality_notes` | 不写报表系统，不做重大决策 | 数据缺失、现金流、异常大幅波动 | passed |
| `sku_margin_risk_candidate` | 电商/经营 | 商品运营 | SKU 毛利异常提示 | internal_template + `metric_exception_classifier` | mock_only/read_only/external_action_blocked | SKU 毛利率从 32% 降到 8% | `risk_level`, `affected_skus`, `possible_causes`, `verification_steps` | 不改价，不下采购单 | 毛利异常、成本口径不清 | passed |
| `marketplace_policy_warning_candidate` | 电商 | 商品运营 | 平台政策风险提示 | internal_template + `marketing_compliance_guard` | mock_only/read_only/external_action_blocked | 商品文案含“治疗”“全网最低” | `policy_warnings`, `risk_level`, `suggested_rewrites`, `manual_review_required` | 不上传商品，不改平台内容 | 食品、医疗、教育、平台禁词 | passed |
| `fulfillment_delay_notice_draft_candidate` | 电商/客服 | 售后客服 | 延迟发货通知草稿 | internal_template | dry_run_only/read_only/external_action_blocked | 物流延迟 2 天，生成通知草稿 | `message_draft`, `send_allowed`, `write_allowed`, `external_action_blocked` | 不发送、不赔偿、不改订单 | 延迟、赔偿、投诉 | passed |
| `boss_daily_brief_candidate` | 经营报表 | 老板 | 老板日报 | internal_template + `daily_weekly_metrics_reporter` | mock_only/read_only/external_action_blocked | 老板看营收、现金、订单、库存风险 | `executive_brief`, `top_metrics`, `risks`, `next_checks` | 不做财务/投资/税务结论 | 现金流、重大异常、数据缺失 | passed |
| `cashflow_warning_brief_candidate` | 财务/经营 | 老板/财务 | 现金流风险提示 | internal_template + `structured_metric_summary` | mock_only/read_only/external_action_blocked | 未来 14 天应收/应付/余额 mock 数据 | `warning_level`, `cashflow_summary`, `drivers`, `manual_review_required` | 不做融资/税务/审计建议 | 现金流紧张、付款风险、数据缺口 | passed |
| `funnel_dropoff_summary_candidate` | 经营/营销 | 增长运营 | 漏斗掉点摘要 | internal_template + `metric_exception_classifier` | mock_only/read_only/external_action_blocked | 访问、加购、下单、支付漏斗 mock 数据 | `dropoff_stage`, `change_summary`, `possible_causes`, `verification_steps` | 不做确定归因 | 转化异常、样本过小、口径变化 | passed |
| `data_quality_checklist_candidate` | 经营报表 | 数据运营 | 数据质量检查清单 | internal_template | mock_only/read_only/external_action_blocked | mock 表字段含缺失、重复、异常范围 | `checklist`, `failed_rules`, `fields_to_verify`, `not_business_conclusion` | 不连数据库，不写表格 | 关键字段缺失、财务口径冲突 | passed |
| `campaign_metric_anomaly_candidate` | 营销/经营 | 活动运营 | 活动指标异常摘要 | internal_template + `metric_exception_classifier` | mock_only/read_only/external_action_blocked | 活动点击率异常下降，转化率上升 | `anomaly_detected`, `severity`, `metric_notes`, `verification_steps` | 不改预算，不做确定归因 | 预算、投放策略、数据异常 | passed |
| `customer_cohort_summary_candidate` | 经营/运营 | 用户运营 | 客户分群摘要 | internal_template | mock_only/read_only/external_action_blocked | mock 新老客、复购、客单分群数据 | `cohort_summary`, `segments`, `insights`, `privacy_notes` | 不识别个人，不导出客户名单 | 小样本、隐私、重识别风险 | passed |
| `inventory_turnover_brief_candidate` | 电商/经营 | 店铺运营 | 库存周转摘要 | internal_template + `order_inventory_exception_candidate` | mock_only/read_only/external_action_blocked | SKU 库存天数、销量、补货周期 mock 数据 | `turnover_summary`, `slow_moving_skus`, `stockout_risks`, `next_checks` | 不改库存，不下采购单 | 缺货、滞销、供应商冲突 | passed |
| `hr_resume_privacy_masker_candidate` | 管理/HR | HR | 简历隐私脱敏 | Microsoft Presidio + `support_pii_redactor` | mock_only/read_only/external_action_blocked | mock 简历含手机号、邮箱、身份证、推荐人电话 | `redacted_text`, `entities`, `preserved_fields`, `risk_level` | 不读真实简历，不上传，不做录用判断 | 高敏 PII、第三方联系人 | passed |
| `contract_clause_partitioner_candidate` | 管理/法务 | 行政/法务协作 | 合同条款分区 | internal_template | dry_run_only/read_only/external_action_blocked | mock 合同含付款、保密、自动续费、违约 | `sections`, `risky_sections`, `not_legal_advice`, `write_allowed` | 不读真实合同，不输出法律意见 | 自动续费、违约、争议解决 | passed |
| `purchase_quote_compare_candidate` | 管理/采购 | 采购 | 采购报价对比草案 | internal_template | mock_only/read_only/external_action_blocked | 三家供应商 mock 报价、交期、售后 | `comparison_table`, `tradeoffs`, `missing_info`, `manual_review_required` | 不下采购单，不承诺供应商 | 价格、供应商资质、合同 | passed |
| `meeting_minutes_action_candidate` | 管理/销售 | 助理 | 会议纪要行动项 | internal_template + `sales_meeting_task_brief_candidate` | dry_run_only/read_only/external_action_blocked | mock 会议纪要生成任务草案 | `summary`, `action_items`, `dry_run_payload`, `write_allowed` | 不写日历/任务/文档 | 任务归属、客户隐私、合同承诺 | passed |
| `reimbursement_policy_check_candidate` | 财务/管理 | 财务 | 报销材料完整性检查 | internal_template + `expense_invoice_parser` | dry_run_only/read_only/external_action_blocked | mock 发票字段和报销政策，检查缺材料 | `check_result`, `missing_fields`, `not_tax_advice`, `write_allowed` | 不做报销/税务/审计结论，不写财务系统 | 金额异常、税号缺失、低置信 | passed |
| `sop_step_extractor_candidate` | 管理/运营 | 行政/运营 | SOP 步骤提取 | internal_template | mock_only/read_only/external_action_blocked | 从 mock 操作说明提取步骤和缺口 | `steps`, `missing_steps`, `owner_roles`, `quality_warnings` | 不写流程系统 | 安全步骤缺失、权限不清 | passed |
| `onboarding_checklist_candidate` | 管理/HR | HR/行政 | 入职清单草案 | internal_template | dry_run_only/read_only/external_action_blocked | 新员工入职场景，生成清单草案 | `checklist`, `dry_run_tasks`, `send_allowed`, `write_allowed` | 不写 HR/任务系统，不发通知 | HR PII、薪酬、合同 | passed |

## dry-run 断言

以下 8 个 `dry_run_only` 候选均已在 smoke 预期中强制断言：

- `external_action_blocked=true`
- `send_allowed=false`
- `write_allowed=false`

| candidate_id | dry-run 边界 |
| --- | --- |
| `renewal_reminder_draft_candidate` | 不发送续费提醒，不写 CRM |
| `content_calendar_mock_candidate` | 不写日历/任务/发布系统 |
| `order_inventory_exception_candidate` | 不调用 Shopify API，不改库存 |
| `fulfillment_delay_notice_draft_candidate` | 不发送延迟通知，不改订单 |
| `contract_clause_partitioner_candidate` | 不读真实合同，不输出法律意见 |
| `meeting_minutes_action_candidate` | 不写日历/任务/文档 |
| `reimbursement_policy_check_candidate` | 不写财务系统，不做报销/税务结论 |
| `onboarding_checklist_candidate` | 不写 HR/任务系统，不发通知 |

## Top 15 候选选择

Top 15 从 `passed` 中选择，优先级依据：

1. 中小微企业高频、可直接试跑。
2. 输出 schema 清楚。
3. 权限边界清楚。
4. 与稳交付 13 个 Skill 不完全重复，或有明确垂直增量。
5. 后续正式 L2 可用 3 个中文业务用例覆盖。

具体队列见 `queues/L2_OFFICIAL_TOP15_FROM_TO50_QUEUE.md`。

