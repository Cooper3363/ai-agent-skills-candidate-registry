# 候选库扩到 100 第二阶段研究结果

回传时间：2026-06-03

## 1. 已完成事项

- 已读取 `INDEX.md`、`STATUS_SUMMARY.md`、`RESEARCH_TO_50_RESULT.md`、`PACKAGING_TO_50_RESULT.md`、`L2_OFFICIAL_TOP15_FROM_TO50_RESULT.md`。
- 已确认第一阶段候选库实际落盘候选卡为 50 张，客户正式可调用 Skill 仍为 13 个。
- 已围绕六大中小微高频业务包输出第二轮 70 个候选线索。
- 已从 70 个线索中筛出 50 个新增候选，推荐进入许可证 / trial mode 复核。
- 已避开当前 50 张候选卡同名 ID；已被稳交付 13 个或 To50 候选完整覆盖的能力，仅记录复用关系，不放入推荐 50。

## 2. 当前问题

- 第二阶段候选以内部模板和现有能力组合为主，业务上可快速 mock，但仍需许可证窗口确认“不复用第三方代码”与 trial mode 边界。
- 少量 GitHub / MCP 方向仅作为可复核来源，未做安装、运行或真实 API 调用，必须先过 L1/trial mode。
- 本报告不改变稳交付库；候选库补到 100 不等于客户可调用扩容。

## 3. 阻塞原因

无阻塞。未安装依赖、未访问真实客户账号、未调用真实业务 API、未发送、未写 CRM/日历/任务、未抓取真实网页、未生成真实媒体、未请求权限。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否接受第二阶段推荐分布：客服 9、销售 9、营销 9、电商/门店 9、经营报表 7、行政/财务/HR 7。
- 是否允许内部模板类候选继续作为补齐 100 的主力来源，许可证窗口只做 trial mode 和第三方复用边界复核。
- 是否把本轮 `component_only` 和 `market_lead` 线索保留为后续 100 之外的组件池 / 方向池，不进入本轮推荐 50。

## 5. 建议下一步

- 许可证窗口读取本报告第 7 节推荐 50 表，逐项输出 `can_mock_smoke`、`can_dry_run_smoke`、`component_only`、`needs_more_license_info` 或 `blocked`。
- 测试台只接收许可证窗口放行项，不直接读取本报告送 smoke。
- 封装窗口等待 smoke 通过后再生成候选卡；本轮研究窗口不生成 `CANDIDATE.md` 或 `candidate.yaml`。

## 6. 候选数量与业务包分布

当前候选卡基线：50 个。

| 业务包 | 当前 To50 估算分布 | 第二阶段推荐新增 | 推荐后预计数量 | 是否贴近 100 目标 |
| --- | ---: | ---: | ---: | --- |
| 客服 | 9 | 9 | 18 | 是 |
| 销售 | 9 | 9 | 18 | 是 |
| 营销 | 8 | 9 | 17 | 是 |
| 电商/门店 | 9 | 9 | 18 | 是 |
| 经营报表 | 7 | 7 | 14 | 是 |
| 行政/财务/HR | 8 | 7 | 15 | 是 |
| 合计 | 50 | 50 | 100 | 是 |

## 7. 推荐进入许可证 / trial mode 复核的 50 个候选

| # | candidate_id | 业务包 | 适配角色 | 场景 | 来源类型 | 来源链接或复用关系 | 是否被 13 个稳交付覆盖 | 是否被 To50 覆盖 | 建议状态 | deepagents_trial_fit | 建议中文 smoke 用例一句话 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `support_ticket_autotag_router_candidate` | 客服 | 客服主管 | 工单自动标签和队列路由建议 | internal_template | `internal_template: support_ticket_autotag_router` | 部分：`support_ticket_classifier` | 部分：客服分类候选 | `mock_callable` | `mock_only` | 输入 10 条 mock 工单，输出标签、优先级和建议队列。 |
| 2 | `support_refund_evidence_request_candidate` | 客服 | 售后客服 | 退款/退货补证材料请求草稿 | internal_template | `internal_template: support_refund_evidence_request` | 部分：客服稳交付包 | 部分：退款回复候选 | `dry_run_callable` | `dry_run_only` | 输入客户退货理由和政策，输出补证材料请求草稿但不发送。 |
| 3 | `support_tone_rewrite_safe_candidate` | 客服 | 客服质检 / 一线客服 | 客服回复语气安全改写 | existing_skill_combo | 复用：`support_reply_guardrail` + To50 退款/账号候选 | 部分覆盖 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入一段生硬回复，输出礼貌版、禁用表达和风险提示。 |
| 4 | `support_policy_conflict_detector_candidate` | 客服 | 知识库运营 | 客服政策文档冲突检测 | existing_skill_combo | 复用：`support_kb_doc_cleaner`, `faq_answer_with_citations` | 部分覆盖 | 否 | `mock_callable` | `mock_only` | 输入两版售后政策，输出冲突条款和需确认问题。 |
| 5 | `support_ticket_batch_summary_candidate` | 客服 | 客服主管 | 批量工单班次摘要 | internal_template | `internal_template: support_ticket_batch_summary` | 部分：`support_ticket_classifier` | 部分：客诉聚类候选 | `mock_callable` | `mock_only` | 输入一个班次的 mock 工单，输出高频问题、风险工单和交接事项。 |
| 6 | `support_vip_customer_handoff_candidate` | 客服 | 客服主管 | VIP / 大客户转人工原因生成 | internal_template | `internal_template: support_vip_customer_handoff` | 部分：`support_reply_guardrail` | 否 | `mock_callable` | `mock_only` | 输入大客户投诉对话，输出转人工原因、风险等级和禁答项。 |
| 7 | `support_warranty_status_reply_candidate` | 客服 | 售后客服 | 保修状态说明草稿 | internal_template | `internal_template: support_warranty_status_reply` | 部分：客服稳交付包 | 部分：售后清单候选 | `dry_run_callable` | `dry_run_only` | 输入保修状态和客户问题，输出不承诺结果的回复草稿。 |
| 8 | `support_channel_deflection_suggester_candidate` | 客服 | 客服运营 | 高峰期渠道分流建议 | internal_template | `internal_template: support_channel_deflection_suggester` | 否 | 否 | `mock_callable` | `mock_only` | 输入各渠道排队量，输出分流建议和人工复核触发。 |
| 9 | `support_shift_handover_brief_candidate` | 客服 | 班组长 | 客服班次交接摘要 | internal_template | `internal_template: support_shift_handover_brief` | 部分：客服稳交付包 | 部分：工单摘要候选 | `mock_callable` | `mock_only` | 输入当天未结工单列表，输出下一班交接重点。 |
| 10 | `outbound_message_personalizer_candidate` | 销售 | 销售代表 | 外呼/私信个性化开场白草稿 | internal_template | `internal_template: outbound_message_personalizer` | 否 | 部分：销售跟进候选 | `dry_run_callable` | `dry_run_only` | 输入客户行业和痛点，输出三版开场白草稿并标记不发送。 |
| 11 | `proposal_requirement_gap_checker_candidate` | 销售 | 售前顾问 | 方案需求缺口检查 | existing_skill_combo | 复用：To50 `proposal_outline_candidate` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入客户需求和方案大纲，输出缺失需求和确认问题。 |
| 12 | `pricing_terms_risk_summary_candidate` | 销售 | 销售经理 | 价格和付款条款风险摘要 | internal_template | `internal_template: pricing_terms_risk_summary` | 否 | 部分：报价异议候选 | `mock_callable` | `mock_only` | 输入报价备注和付款条件，输出折扣、账期和合同风险。 |
| 13 | `demo_script_builder_candidate` | 销售 | 售前 / 销售 | 产品演示脚本 | internal_template | `internal_template: demo_script_builder` | 否 | 否 | `mock_callable` | `skill_ready` | 输入客户行业、痛点和功能清单，输出 10 分钟演示脚本。 |
| 14 | `lost_deal_followup_draft_candidate` | 销售 | 销售运营 | 丢单复盘和复联草稿 | internal_template | `internal_template: lost_deal_followup_draft` | 部分：`crm_note_structurer` | 部分：商机风险候选 | `dry_run_callable` | `dry_run_only` | 输入丢单原因，输出复盘问题和复联草稿但不发送。 |
| 15 | `customer_reference_brief_candidate` | 销售 | 销售顾问 | 客户案例匹配 brief | internal_template | `internal_template: customer_reference_brief` | 否 | 否 | `mock_callable` | `mock_only` | 输入客户行业和案例库摘要，输出可引用案例和禁用承诺。 |
| 16 | `sales_stage_exit_criteria_checker_candidate` | 销售 | 销售主管 | 商机阶段退出条件检查 | internal_template | `internal_template: sales_stage_exit_criteria_checker` | 部分：`crm_note_structurer` | 部分：商机风险候选 | `mock_callable` | `mock_only` | 输入商机阶段和记录，输出是否满足进入下一阶段的证据。 |
| 17 | `partner_fit_matrix_candidate` | 销售 | 渠道经理 | 合作伙伴适配矩阵 | internal_template | `internal_template: partner_fit_matrix` | 否 | 否 | `mock_callable` | `mock_only` | 输入合作方资料，输出渠道适配度、风险和下一步问题。 |
| 18 | `quote_scope_change_summary_candidate` | 销售 | 商务支持 | 报价范围变更摘要 | internal_template | `internal_template: quote_scope_change_summary` | 否 | 部分：方案/报价候选 | `mock_callable` | `mock_only` | 输入新旧报价范围，输出变更点、影响和需人工确认项。 |
| 19 | `lead_enrichment_from_user_text_candidate` | 销售 | 商务支持 | 基于用户提供文本的线索补全 | internal_template | `internal_template: lead_enrichment_from_user_text` | 否 | 部分：潜客简报组件 | `mock_callable` | `mock_only` | 输入名片和企业简介文本，输出线索字段和缺失信息。 |
| 20 | `promo_bundle_copy_matrix_candidate` | 营销 | 活动运营 | 组合促销文案矩阵 | internal_template | `internal_template: promo_bundle_copy_matrix` | 部分：`marketing_copy_pack` | 部分：商品文案候选 | `mock_callable` | `skill_ready` | 输入三类套餐和折扣，输出不同人群的促销文案矩阵。 |
| 21 | `seasonal_campaign_idea_bank_candidate` | 营销 | 内容运营 | 节日/季节活动创意库 | internal_template | `internal_template: seasonal_campaign_idea_bank` | 部分：`structured_campaign_brief` | 部分：内容日历候选 | `mock_callable` | `skill_ready` | 输入门店类型和节日，输出 10 个活动主题和适用渠道。 |
| 22 | `influencer_brief_draft_candidate` | 营销 | 品牌/投放 | 达人合作 brief 草稿 | internal_template | `internal_template: influencer_brief_draft` | 部分：营销稳交付包 | 否 | `dry_run_callable` | `dry_run_only` | 输入达人画像和产品卖点，输出合作 brief 草稿和禁用承诺。 |
| 23 | `ugc_review_to_ad_angle_candidate` | 营销 | 投放运营 | 用户评价转广告角度 | internal_template | `internal_template: ugc_review_to_ad_angle` | 部分：`marketing_copy_pack` | 部分：评价聚类候选 | `mock_callable` | `mock_only` | 输入 20 条用户评价，输出可用于广告的角度和风险提示。 |
| 24 | `email_subject_line_variants_candidate` | 营销 | 私域运营 | 邮件标题变体 | internal_template | `internal_template: email_subject_line_variants` | 部分：`marketing_copy_pack` | 部分：newsletter 候选线索 | `dry_run_callable` | `dry_run_only` | 输入会员活动说明，输出 10 个邮件标题但不发送邮件。 |
| 25 | `brand_forbidden_words_checker_candidate` | 营销 | 品牌/合规 | 品牌禁用词和语气规则检查 | internal_template | `internal_template: brand_forbidden_words_checker` | 部分：`marketing_compliance_guard` | 部分：品牌语气候选 | `mock_callable` | `skill_ready` | 输入品牌规则和广告文案，输出禁用词、替换建议和人工复核项。 |
| 26 | `local_event_poster_copy_candidate` | 营销 | 门店运营 | 本地活动海报文案 | internal_template | `internal_template: local_event_poster_copy` | 部分：`marketing_copy_pack` | 部分：视觉 brief 候选 | `mock_callable` | `skill_ready` | 输入门店活动信息，输出海报标题、副标题和注意事项。 |
| 27 | `ai_search_answer_snippet_candidate` | 营销 | 内容/SEO | AI 搜索答案片段草稿 | internal_template | `internal_template: ai_search_answer_snippet` | 部分：`marketing_copy_pack` | 否 | `mock_callable` | `mock_only` | 输入产品介绍和 FAQ，输出可被引用的简短答案片段。 |
| 28 | `landing_page_faq_schema_brief_candidate` | 营销 | 内容/SEO | 落地页 FAQ 和结构化摘要 brief | internal_template | `internal_template: landing_page_faq_schema_brief` | 部分：`marketing_copy_pack` | 部分：落地页大纲线索 | `mock_callable` | `skill_ready` | 输入落地页文案，输出 FAQ 问答和 schema brief。 |
| 29 | `product_attribute_gap_checker_candidate` | 电商/门店 | 商品运营 | 商品属性缺失检查 | internal_template | `internal_template: product_attribute_gap_checker` | 否 | 部分：商品文案候选 | `mock_callable` | `mock_only` | 输入商品标题和属性表，输出缺失属性、疑似错误和补充建议。 |
| 30 | `sku_deduplication_suggester_candidate` | 电商/门店 | 商品运营 | SKU 重复和命名冲突提示 | internal_template | `internal_template: sku_deduplication_suggester` | 否 | 部分：库存候选 | `mock_callable` | `mock_only` | 输入 SKU 清单，输出疑似重复商品和合并核查建议。 |
| 31 | `order_cancellation_reason_summary_candidate` | 电商/门店 | 店铺运营 | 订单取消原因摘要 | internal_template | `internal_template: order_cancellation_reason_summary` | 否 | 部分：退货聚类候选 | `mock_callable` | `mock_only` | 输入取消订单原因，输出分类、占比和运营建议。 |
| 32 | `supplier_delivery_risk_brief_candidate` | 电商/门店 | 采购/库存 | 供应商交付风险 brief | internal_template | `internal_template: supplier_delivery_risk_brief` | 否 | 部分：订单库存候选 | `mock_callable` | `mock_only` | 输入供应商交期和历史延迟，输出风险等级和核查清单。 |
| 33 | `store_staff_shift_plan_candidate` | 电商/门店 | 店长 | 门店排班建议草案 | internal_template | `internal_template: store_staff_shift_plan` | 否 | 否 | `dry_run_callable` | `dry_run_only` | 输入客流峰谷和员工可用时间，输出排班草案但不写系统。 |
| 34 | `local_store_event_checklist_candidate` | 电商/门店 | 店长/运营 | 门店活动执行检查表 | internal_template | `internal_template: local_store_event_checklist` | 否 | 部分：内容日历候选 | `mock_callable` | `skill_ready` | 输入活动日期和物料，输出执行清单、负责人和风险点。 |
| 35 | `marketplace_reply_draft_candidate` | 电商/门店 | 店铺客服 | 平台评价/问答回复草稿 | internal_template | `internal_template: marketplace_reply_draft` | 部分：客服稳交付包 | 部分：评价聚类候选 | `dry_run_callable` | `dry_run_only` | 输入买家差评，输出平台回复草稿和禁用表达。 |
| 36 | `price_change_impact_brief_candidate` | 电商/门店 | 商品运营 | 调价影响摘要 | internal_template | `internal_template: price_change_impact_brief` | 部分：经营报表稳交付包 | 部分：SKU 毛利候选 | `mock_callable` | `mock_only` | 输入调价前后销量和毛利，输出影响摘要和核查建议。 |
| 37 | `bundle_inventory_feasibility_candidate` | 电商/门店 | 商品运营 | 套餐组合库存可行性检查 | internal_template | `internal_template: bundle_inventory_feasibility` | 否 | 部分：订单库存候选 | `mock_callable` | `mock_only` | 输入套餐 SKU 和库存，输出可售数量、短板 SKU 和风险提示。 |
| 38 | `gross_margin_bridge_summary_candidate` | 经营报表 | 老板/财务 | 毛利变化桥接摘要 | internal_template | `internal_template: gross_margin_bridge_summary` | 部分：报表稳交付包 | 部分：SKU 毛利候选 | `mock_callable` | `mock_only` | 输入收入、成本、折扣变化，输出毛利变化来源和核查项。 |
| 39 | `break_even_point_brief_candidate` | 经营报表 | 老板 | 盈亏平衡点简报 | internal_template | `internal_template: break_even_point_brief` | 部分：`structured_metric_summary` | 否 | `mock_callable` | `mock_only` | 输入固定成本、毛利率和客单价，输出盈亏平衡估算和非财务建议提示。 |
| 40 | `sales_target_progress_brief_candidate` | 经营报表 | 销售主管/老板 | 销售目标进度摘要 | internal_template | `internal_template: sales_target_progress_brief` | 部分：报表稳交付包 | 部分：销售阶段候选 | `mock_callable` | `skill_ready` | 输入月目标和当前销售额，输出进度、缺口和追赶建议。 |
| 41 | `expense_category_outlier_candidate` | 经营报表 | 财务 | 费用分类异常提示 | internal_template | `internal_template: expense_category_outlier` | 部分：`expense_invoice_parser` | 否 | `mock_callable` | `mock_only` | 输入费用分类表，输出异常类别、重复项和人工核查建议。 |
| 42 | `refund_rate_trend_brief_candidate` | 经营报表 | 售后主管/老板 | 退款率趋势简报 | internal_template | `internal_template: refund_rate_trend_brief` | 部分：报表和客服稳交付包 | 部分：退货聚类候选 | `mock_callable` | `mock_only` | 输入退款率和订单量，输出趋势、可能因素和核查项。 |
| 43 | `staff_productivity_snapshot_candidate` | 经营报表 | 店长/主管 | 员工产能快照 | internal_template | `internal_template: staff_productivity_snapshot` | 否 | 否 | `mock_callable` | `mock_only` | 输入员工工时和完成量，输出产能摘要和不可用于处罚提示。 |
| 44 | `data_schema_mapping_hint_candidate` | 经营报表 | 数据运营 | 表格字段映射建议 | internal_template | `internal_template: data_schema_mapping_hint` | 部分：数据质量候选 | 否 | `mock_callable` | `mock_only` | 输入两张表字段名，输出可能映射和需人工确认项。 |
| 45 | `resume_screening_question_pack_candidate` | 行政/财务/HR | HR | 简历追问问题包 | internal_template | `internal_template: resume_screening_question_pack` | 否 | 部分：简历脱敏候选 | `mock_callable` | `mock_only` | 输入脱敏简历和岗位要求，输出面试追问问题，不给录用建议。 |
| 46 | `interview_feedback_structurer_candidate` | 行政/财务/HR | HR | 面试反馈结构化 | internal_template | `internal_template: interview_feedback_structurer` | 否 | 否 | `mock_callable` | `mock_only` | 输入面试官笔记，输出能力项、证据和人工评分表。 |
| 47 | `employee_onboarding_faq_candidate` | 行政/财务/HR | HR/行政 | 入职 FAQ 问答草稿 | existing_skill_combo | 复用：`faq_answer_with_citations`, To50 入职清单候选 | 部分：`faq_answer_with_citations` | 部分覆盖 | `mock_callable` | `skill_ready` | 输入入职制度片段，输出带引用的新人 FAQ 草稿。 |
| 48 | `leave_request_policy_router_candidate` | 行政/财务/HR | HR/行政 | 请假政策分流和材料提示 | internal_template | `internal_template: leave_request_policy_router` | 否 | 否 | `dry_run_callable` | `dry_run_only` | 输入请假类型和制度片段，输出材料提示和转人工原因。 |
| 49 | `procurement_request_checker_candidate` | 行政/财务/HR | 采购/行政 | 采购申请完整性检查 | internal_template | `internal_template: procurement_request_checker` | 否 | 部分：采购报价候选 | `mock_callable` | `mock_only` | 输入采购申请，输出预算、规格、审批材料缺口。 |
| 50 | `contract_renewal_date_extractor_candidate` | 行政/财务/HR | 合同经办 | 合同续约/到期日期抽取 | GitHub | `https://github.com/dateparser/dateparser`; 可改内部规则实现 | 否 | 部分：合同分区候选 | `needs_license_review` | `mock_only` | 输入合同日期条款，输出到期日、续约提醒和人工复核点。 |

## 8. 第二轮 70 个候选线索总表

| # | candidate_id | 业务包 | 适配角色 | 场景 | 来源类型 | 来源链接或复用关系 | 是否被 13 个稳交付覆盖 | 是否被 To50 覆盖 | 建议状态 | deepagents_trial_fit | 建议中文 smoke 用例一句话 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `support_ticket_autotag_router_candidate` | 客服 | 客服主管 | 工单标签和路由建议 | internal_template | `internal_template: support_ticket_autotag_router` | 部分：`support_ticket_classifier` | 部分：客服分类候选 | `mock_callable` | `mock_only` | 输入 mock 工单，输出标签和队列建议。 |
| 2 | `support_refund_evidence_request_candidate` | 客服 | 售后客服 | 退款补证请求草稿 | internal_template | `internal_template: support_refund_evidence_request` | 部分：客服稳交付包 | 部分：退款回复候选 | `dry_run_callable` | `dry_run_only` | 输入退款诉求，输出补证请求草稿。 |
| 3 | `support_tone_rewrite_safe_candidate` | 客服 | 一线客服 | 回复语气安全改写 | existing_skill_combo | `support_reply_guardrail` + To50 客服候选 | 部分覆盖 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入生硬回复，输出礼貌安全版。 |
| 4 | `support_policy_conflict_detector_candidate` | 客服 | 知识库运营 | 政策冲突检测 | existing_skill_combo | `support_kb_doc_cleaner` + `faq_answer_with_citations` | 部分覆盖 | 否 | `mock_callable` | `mock_only` | 输入两版政策，输出冲突条款。 |
| 5 | `support_ticket_batch_summary_candidate` | 客服 | 客服主管 | 批量工单摘要 | internal_template | `internal_template: support_ticket_batch_summary` | 部分覆盖 | 部分：投诉聚类候选 | `mock_callable` | `mock_only` | 输入班次工单，输出交接摘要。 |
| 6 | `support_vip_customer_handoff_candidate` | 客服 | 客服主管 | VIP 转人工原因 | internal_template | `internal_template: support_vip_customer_handoff` | 部分覆盖 | 否 | `mock_callable` | `mock_only` | 输入 VIP 投诉，输出转人工原因。 |
| 7 | `support_warranty_status_reply_candidate` | 客服 | 售后客服 | 保修状态回复草稿 | internal_template | `internal_template: support_warranty_status_reply` | 部分覆盖 | 部分：售后清单候选 | `dry_run_callable` | `dry_run_only` | 输入保修信息，输出回复草稿。 |
| 8 | `support_channel_deflection_suggester_candidate` | 客服 | 客服运营 | 渠道分流建议 | internal_template | `internal_template: support_channel_deflection_suggester` | 否 | 否 | `mock_callable` | `mock_only` | 输入排队量，输出分流建议。 |
| 9 | `support_shift_handover_brief_candidate` | 客服 | 班组长 | 班次交接摘要 | internal_template | `internal_template: support_shift_handover_brief` | 部分覆盖 | 部分覆盖 | `mock_callable` | `mock_only` | 输入未结工单，输出交接重点。 |
| 10 | `support_agent_coaching_scorecard_candidate` | 客服 | 培训负责人 | 客服辅导评分卡 | internal_template | `internal_template: support_agent_coaching_scorecard` | 部分覆盖 | 完整：`support_quality_eval_candidate` | `component_only` | `component_only` | 输入客服对话，输出评分卡组件。 |
| 11 | `support_faq_test_case_generator_candidate` | 客服 | 知识库运营 | FAQ 测试用例生成 | internal_template | `internal_template: support_faq_test_case_generator` | 部分覆盖 | 部分覆盖 | `component_only` | `component_only` | 输入 FAQ，输出测试问题。 |
| 12 | `support_refund_abuse_signal_candidate` | 客服 | 风控/售后主管 | 异常退款线索 | internal_template | `internal_template: support_refund_abuse_signal` | 否 | 部分覆盖 | `market_lead` | `not_suitable` | 输入退款记录，输出仅供人工复核的异常线索。 |
| 13 | `outbound_message_personalizer_candidate` | 销售 | 销售代表 | 外呼私信开场白 | internal_template | `internal_template: outbound_message_personalizer` | 否 | 部分：销售跟进候选 | `dry_run_callable` | `dry_run_only` | 输入客户画像，输出开场白草稿。 |
| 14 | `proposal_requirement_gap_checker_candidate` | 销售 | 售前顾问 | 方案需求缺口检查 | existing_skill_combo | To50 `proposal_outline_candidate` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入需求和方案，输出缺口。 |
| 15 | `pricing_terms_risk_summary_candidate` | 销售 | 销售经理 | 价格付款风险摘要 | internal_template | `internal_template: pricing_terms_risk_summary` | 否 | 部分：报价异议候选 | `mock_callable` | `mock_only` | 输入报价条款，输出风险摘要。 |
| 16 | `demo_script_builder_candidate` | 销售 | 售前 | 演示脚本 | internal_template | `internal_template: demo_script_builder` | 否 | 否 | `mock_callable` | `skill_ready` | 输入客户痛点，输出演示脚本。 |
| 17 | `lost_deal_followup_draft_candidate` | 销售 | 销售运营 | 丢单复联草稿 | internal_template | `internal_template: lost_deal_followup_draft` | 部分覆盖 | 部分覆盖 | `dry_run_callable` | `dry_run_only` | 输入丢单原因，输出复联草稿。 |
| 18 | `customer_reference_brief_candidate` | 销售 | 销售顾问 | 客户案例匹配 | internal_template | `internal_template: customer_reference_brief` | 否 | 否 | `mock_callable` | `mock_only` | 输入客户行业，输出案例 brief。 |
| 19 | `sales_stage_exit_criteria_checker_candidate` | 销售 | 销售主管 | 阶段退出条件检查 | internal_template | `internal_template: sales_stage_exit_criteria_checker` | 部分覆盖 | 部分覆盖 | `mock_callable` | `mock_only` | 输入商机记录，输出是否满足阶段条件。 |
| 20 | `partner_fit_matrix_candidate` | 销售 | 渠道经理 | 合作伙伴适配矩阵 | internal_template | `internal_template: partner_fit_matrix` | 否 | 否 | `mock_callable` | `mock_only` | 输入伙伴资料，输出适配矩阵。 |
| 21 | `quote_scope_change_summary_candidate` | 销售 | 商务支持 | 报价范围变更摘要 | internal_template | `internal_template: quote_scope_change_summary` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入新旧报价，输出变更摘要。 |
| 22 | `lead_enrichment_from_user_text_candidate` | 销售 | 商务支持 | 用户文本线索补全 | internal_template | `internal_template: lead_enrichment_from_user_text` | 否 | 部分：潜客组件 | `mock_callable` | `mock_only` | 输入名片文本，输出线索字段。 |
| 23 | `crm_duplicate_lead_detector_candidate` | 销售 | 销售运营 | CRM 重复线索检测 | GitHub | `https://github.com/rapidfuzz/RapidFuzz` | 否 | 否 | `needs_license_review` | `component_only` | 输入线索清单，输出疑似重复项。 |
| 24 | `sales_commission_question_router_candidate` | 销售 | 销售/财务 | 提成问题分流 | internal_template | `internal_template: sales_commission_question_router` | 否 | 否 | `market_lead` | `not_suitable` | 输入提成疑问，输出转人工原因。 |
| 25 | `promo_bundle_copy_matrix_candidate` | 营销 | 活动运营 | 套餐促销文案矩阵 | internal_template | `internal_template: promo_bundle_copy_matrix` | 部分覆盖 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入套餐，输出文案矩阵。 |
| 26 | `seasonal_campaign_idea_bank_candidate` | 营销 | 内容运营 | 节日活动创意库 | internal_template | `internal_template: seasonal_campaign_idea_bank` | 部分覆盖 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入节日和门店类型，输出活动主题。 |
| 27 | `influencer_brief_draft_candidate` | 营销 | 品牌/投放 | 达人合作 brief | internal_template | `internal_template: influencer_brief_draft` | 部分覆盖 | 否 | `dry_run_callable` | `dry_run_only` | 输入达人画像，输出合作 brief。 |
| 28 | `ugc_review_to_ad_angle_candidate` | 营销 | 投放运营 | 评价转广告角度 | internal_template | `internal_template: ugc_review_to_ad_angle` | 部分覆盖 | 部分：评价聚类候选 | `mock_callable` | `mock_only` | 输入评价，输出广告角度。 |
| 29 | `email_subject_line_variants_candidate` | 营销 | 私域运营 | 邮件标题变体 | internal_template | `internal_template: email_subject_line_variants` | 部分覆盖 | 部分覆盖 | `dry_run_callable` | `dry_run_only` | 输入活动说明，输出标题变体。 |
| 30 | `brand_forbidden_words_checker_candidate` | 营销 | 品牌/合规 | 品牌禁用词检查 | internal_template | `internal_template: brand_forbidden_words_checker` | 部分覆盖 | 部分：品牌语气候选 | `mock_callable` | `skill_ready` | 输入品牌规则，输出禁词风险。 |
| 31 | `local_event_poster_copy_candidate` | 营销 | 门店运营 | 本地活动海报文案 | internal_template | `internal_template: local_event_poster_copy` | 部分覆盖 | 部分：视觉 brief 候选 | `mock_callable` | `skill_ready` | 输入活动信息，输出海报文案。 |
| 32 | `ai_search_answer_snippet_candidate` | 营销 | 内容/SEO | AI 搜索答案片段 | internal_template | `internal_template: ai_search_answer_snippet` | 部分覆盖 | 否 | `mock_callable` | `mock_only` | 输入 FAQ，输出答案片段。 |
| 33 | `landing_page_faq_schema_brief_candidate` | 营销 | 内容/SEO | FAQ schema brief | internal_template | `internal_template: landing_page_faq_schema_brief` | 部分覆盖 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入落地页，输出 FAQ brief。 |
| 34 | `competitor_ad_angle_summary_candidate` | 营销 | 投放运营 | 竞品广告角度摘要 | ClawHub | `market_lead: competitor ad angle`; 仅用户提供文本 | 否 | 部分：竞品快照组件 | `market_lead` | `not_suitable` | 输入用户粘贴的竞品广告，输出角度摘要。 |
| 35 | `image_prompt_variant_pack_candidate` | 营销 | 设计运营 | 图片 prompt 变体包 | existing_skill_combo | To50 `visual_prompt_brief_candidate` | 否 | 完整覆盖 | `component_only` | `component_only` | 输入视觉 brief，输出 prompt 变体组件。 |
| 36 | `marketing_budget_allocation_brief_candidate` | 营销 | 老板/运营 | 营销预算分配 brief | internal_template | `internal_template: marketing_budget_allocation_brief` | 部分：报表稳交付包 | 否 | `market_lead` | `not_suitable` | 输入预算和渠道，输出非财务建议的分配思路。 |
| 37 | `product_attribute_gap_checker_candidate` | 电商/门店 | 商品运营 | 商品属性缺失检查 | internal_template | `internal_template: product_attribute_gap_checker` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入商品属性，输出缺失项。 |
| 38 | `sku_deduplication_suggester_candidate` | 电商/门店 | 商品运营 | SKU 重复提示 | internal_template | `internal_template: sku_deduplication_suggester` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入 SKU，输出疑似重复项。 |
| 39 | `order_cancellation_reason_summary_candidate` | 电商/门店 | 店铺运营 | 订单取消原因摘要 | internal_template | `internal_template: order_cancellation_reason_summary` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入取消原因，输出分类。 |
| 40 | `supplier_delivery_risk_brief_candidate` | 电商/门店 | 采购/库存 | 供应商交付风险 | internal_template | `internal_template: supplier_delivery_risk_brief` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入交付记录，输出风险 brief。 |
| 41 | `store_staff_shift_plan_candidate` | 电商/门店 | 店长 | 门店排班草案 | internal_template | `internal_template: store_staff_shift_plan` | 否 | 否 | `dry_run_callable` | `dry_run_only` | 输入客流和排班限制，输出排班草案。 |
| 42 | `local_store_event_checklist_candidate` | 电商/门店 | 店长/运营 | 门店活动执行表 | internal_template | `internal_template: local_store_event_checklist` | 否 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入门店活动，输出执行清单。 |
| 43 | `marketplace_reply_draft_candidate` | 电商/门店 | 店铺客服 | 平台评价回复草稿 | internal_template | `internal_template: marketplace_reply_draft` | 部分覆盖 | 部分覆盖 | `dry_run_callable` | `dry_run_only` | 输入差评，输出回复草稿。 |
| 44 | `price_change_impact_brief_candidate` | 电商/门店 | 商品运营 | 调价影响摘要 | internal_template | `internal_template: price_change_impact_brief` | 部分覆盖 | 部分覆盖 | `mock_callable` | `mock_only` | 输入调价数据，输出影响摘要。 |
| 45 | `bundle_inventory_feasibility_candidate` | 电商/门店 | 商品运营 | 套餐库存可行性 | internal_template | `internal_template: bundle_inventory_feasibility` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入套餐和库存，输出可售数量。 |
| 46 | `product_image_prompt_qc_candidate` | 电商/门店 | 设计/商品运营 | 商品图 prompt 质检 | existing_skill_combo | To50 `visual_prompt_brief_candidate` | 否 | 完整覆盖 | `component_only` | `component_only` | 输入商品图 prompt，输出质检项。 |
| 47 | `competitor_review_theme_summary_candidate` | 电商/门店 | 店铺运营 | 竞品评价主题摘要 | ClawHub | `market_lead: competitor review text`; 仅用户提供文本 | 否 | 部分：竞品快照组件 | `market_lead` | `not_suitable` | 输入用户粘贴评价，输出主题摘要。 |
| 48 | `loyalty_member_segment_brief_candidate` | 电商/门店 | 会员运营 | 会员分层运营 brief | internal_template | `internal_template: loyalty_member_segment_brief` | 部分：报表稳交付包 | 否 | `market_lead` | `mock_only` | 输入会员消费数据，输出分层建议。 |
| 49 | `gross_margin_bridge_summary_candidate` | 经营报表 | 老板/财务 | 毛利变化桥接 | internal_template | `internal_template: gross_margin_bridge_summary` | 部分覆盖 | 部分覆盖 | `mock_callable` | `mock_only` | 输入收入成本，输出毛利变化来源。 |
| 50 | `break_even_point_brief_candidate` | 经营报表 | 老板 | 盈亏平衡简报 | internal_template | `internal_template: break_even_point_brief` | 部分覆盖 | 否 | `mock_callable` | `mock_only` | 输入成本和客单价，输出盈亏平衡估算。 |
| 51 | `sales_target_progress_brief_candidate` | 经营报表 | 销售主管 | 目标进度摘要 | internal_template | `internal_template: sales_target_progress_brief` | 部分覆盖 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入销售目标，输出进度摘要。 |
| 52 | `expense_category_outlier_candidate` | 经营报表 | 财务 | 费用分类异常 | internal_template | `internal_template: expense_category_outlier` | 部分覆盖 | 否 | `mock_callable` | `mock_only` | 输入费用表，输出异常类别。 |
| 53 | `refund_rate_trend_brief_candidate` | 经营报表 | 售后主管 | 退款率趋势 | internal_template | `internal_template: refund_rate_trend_brief` | 部分覆盖 | 部分覆盖 | `mock_callable` | `mock_only` | 输入退款率，输出趋势简报。 |
| 54 | `staff_productivity_snapshot_candidate` | 经营报表 | 店长/主管 | 员工产能快照 | internal_template | `internal_template: staff_productivity_snapshot` | 否 | 否 | `mock_callable` | `mock_only` | 输入工时和完成量，输出产能摘要。 |
| 55 | `data_schema_mapping_hint_candidate` | 经营报表 | 数据运营 | 字段映射建议 | internal_template | `internal_template: data_schema_mapping_hint` | 部分覆盖 | 否 | `mock_callable` | `mock_only` | 输入字段名，输出映射建议。 |
| 56 | `customer_ltv_simple_summary_candidate` | 经营报表 | 运营/老板 | 简单 LTV 摘要 | internal_template | `internal_template: customer_ltv_simple_summary` | 部分覆盖 | 部分：分群摘要候选 | `mock_callable` | `mock_only` | 输入客户消费数据，输出 LTV 摘要。 |
| 57 | `inventory_cash_tieup_brief_candidate` | 经营报表 | 老板/库存 | 库存占用资金简报 | internal_template | `internal_template: inventory_cash_tieup_brief` | 部分覆盖 | 部分：库存周转候选 | `mock_callable` | `mock_only` | 输入库存金额，输出资金占用摘要。 |
| 58 | `tax_risk_language_guard_candidate` | 经营报表 | 财务 | 税务表述风险提示 | internal_template | `internal_template: tax_risk_language_guard` | 否 | 否 | `market_lead` | `not_suitable` | 输入税务说明草稿，输出需专业复核提示。 |
| 59 | `budget_variance_explainer_candidate` | 经营报表 | 财务/老板 | 预算差异解释 | internal_template | `internal_template: budget_variance_explainer` | 部分覆盖 | 部分：现金流候选 | `mock_callable` | `mock_only` | 输入预算与实际，输出差异解释。 |
| 60 | `resume_screening_question_pack_candidate` | 行政/财务/HR | HR | 简历追问问题包 | internal_template | `internal_template: resume_screening_question_pack` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入脱敏简历，输出面试追问。 |
| 61 | `interview_feedback_structurer_candidate` | 行政/财务/HR | HR | 面试反馈结构化 | internal_template | `internal_template: interview_feedback_structurer` | 否 | 否 | `mock_callable` | `mock_only` | 输入面试笔记，输出结构化反馈。 |
| 62 | `employee_onboarding_faq_candidate` | 行政/财务/HR | HR/行政 | 入职 FAQ | existing_skill_combo | `faq_answer_with_citations` + To50 入职清单 | 部分覆盖 | 部分覆盖 | `mock_callable` | `skill_ready` | 输入制度，输出入职 FAQ。 |
| 63 | `leave_request_policy_router_candidate` | 行政/财务/HR | HR/行政 | 请假政策分流 | internal_template | `internal_template: leave_request_policy_router` | 否 | 否 | `dry_run_callable` | `dry_run_only` | 输入请假诉求，输出材料提示。 |
| 64 | `procurement_request_checker_candidate` | 行政/财务/HR | 采购/行政 | 采购申请完整性 | internal_template | `internal_template: procurement_request_checker` | 否 | 部分覆盖 | `mock_callable` | `mock_only` | 输入采购申请，输出缺失信息。 |
| 65 | `contract_renewal_date_extractor_candidate` | 行政/财务/HR | 合同经办 | 合同续约日期抽取 | GitHub | `https://github.com/dateparser/dateparser` | 否 | 部分覆盖 | `needs_license_review` | `mock_only` | 输入日期条款，输出到期日。 |
| 66 | `petty_cash_reconciliation_hint_candidate` | 行政/财务/HR | 财务 | 备用金核对提示 | internal_template | `internal_template: petty_cash_reconciliation_hint` | 部分：`expense_invoice_parser` | 否 | `mock_callable` | `mock_only` | 输入备用金流水，输出核对线索。 |
| 67 | `payroll_anomaly_question_router_candidate` | 行政/财务/HR | HR/财务 | 薪酬异常问题分流 | internal_template | `internal_template: payroll_anomaly_question_router` | 否 | 否 | `market_lead` | `not_suitable` | 输入薪酬问题，输出转人工原因。 |
| 68 | `vendor_contract_comparison_candidate` | 行政/财务/HR | 采购/合同 | 供应商合同对比 | internal_template | `internal_template: vendor_contract_comparison` | 否 | 部分：合同分区候选 | `market_lead` | `mock_only` | 输入两份合同摘要，输出差异和非法律提示。 |
| 69 | `employee_training_quiz_generator_candidate` | 行政/财务/HR | HR/培训 | 培训题生成 | existing_skill_combo | To50 `sop_step_extractor_candidate` | 否 | 完整覆盖 | `component_only` | `component_only` | 输入 SOP，输出培训题组件。 |
| 70 | `office_asset_inventory_check_candidate` | 行政/财务/HR | 行政 | 办公资产盘点异常 | internal_template | `internal_template: office_asset_inventory_check` | 否 | 否 | `mock_callable` | `mock_only` | 输入资产台账，输出异常和缺失项。 |

## 9. 本轮暂不推荐进入 50 的线索

| candidate_id | 原因 |
| --- | --- |
| `support_agent_coaching_scorecard_candidate` | 与 To50 `support_quality_eval_candidate` 高度重叠，保留为组件。 |
| `support_faq_test_case_generator_candidate` | 更适合作为知识库测试组件，不单独进入第二阶段推荐。 |
| `support_refund_abuse_signal_candidate` | 风控误判和客户权益风险较高，先保留为 `market_lead`。 |
| `crm_duplicate_lead_detector_candidate` | 依赖 fuzzy matching 组件，建议先作为 `component_only` 复核，暂不占推荐名额。 |
| `sales_commission_question_router_candidate` | 涉及薪酬/提成敏感场景，先不进 trial。 |
| `competitor_ad_angle_summary_candidate` | 竞品广告来源容易涉及真实网页和平台 ToS，本轮只保留为用户粘贴文本线索。 |
| `image_prompt_variant_pack_candidate` | 已被 To50 `visual_prompt_brief_candidate` 完整覆盖。 |
| `marketing_budget_allocation_brief_candidate` | 容易被理解为预算/财务建议，先暂缓。 |
| `product_image_prompt_qc_candidate` | 已被 To50 视觉 brief 路线覆盖。 |
| `competitor_review_theme_summary_candidate` | 若涉及抓取真实评价需审批，本轮不推荐。 |
| `loyalty_member_segment_brief_candidate` | 需要更多客户数据边界设计，先保留为后续线索。 |
| `customer_ltv_simple_summary_candidate` | 与分群/经营报表能力相邻，本轮经营报表名额有限，先作为候补。 |
| `inventory_cash_tieup_brief_candidate` | 与库存周转、现金流候选相邻，先不重复推荐。 |
| `tax_risk_language_guard_candidate` | 税务高风险，仅可做专业复核提示，不进入本轮推荐。 |
| `budget_variance_explainer_candidate` | 与现金流/费用异常场景相邻，先作为候补。 |
| `payroll_anomaly_question_router_candidate` | 薪酬敏感，先保留为人工分流线索。 |
| `vendor_contract_comparison_candidate` | 合同法律风险较高，先保留为 `market_lead`。 |
| `employee_training_quiz_generator_candidate` | 已被 SOP 提取与培训组件覆盖。 |
| `office_asset_inventory_check_candidate` | 行政价值有，但第二阶段 HR/财务优先级更高，先作为候补。 |

## 10. 建议许可证窗口下一步

优先顺序：

1. `internal_template` 候选：确认无第三方代码复用，直接复核 trial mode、输入输出和人工复核触发。
2. `existing_skill_combo` 候选：确认只是 To50 / 稳交付能力组合，不重复进入稳交付，适合 DeepAgents mock smoke。
3. `GitHub` 候选：先核验 LICENSE、README 商用限制、维护状态、依赖许可和是否只是组件。
4. `dry_run_callable` 候选：统一要求 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`。

本轮重点复核候选：

| candidate_id | 复核重点 |
| --- | --- |
| `contract_renewal_date_extractor_candidate` | 若使用 `dateparser`，需核验许可证；也可改为内部日期规则模板规避依赖。 |
| `support_refund_evidence_request_candidate` | 不得承诺退款、赔偿或要求过度隐私材料。 |
| `outbound_message_personalizer_candidate` | 必须 dry-run，不得发送，不得写 CRM。 |
| `influencer_brief_draft_candidate` | 不得承诺曝光、转化或授权素材。 |
| `marketplace_reply_draft_candidate` | 不得直接发布平台回复，需人工审核。 |
| `staff_productivity_snapshot_candidate` | 不得用于员工处罚或自动绩效判断。 |
| `resume_screening_question_pack_candidate` | 不得给录用/淘汰建议，只输出追问问题。 |

## 11. 回传结论

- 第二轮 70 个候选线索已完成。
- 已推荐 50 个新增候选进入许可证 / trial mode 复核。
- 推荐后研究侧口径可支撑候选库从 50 补齐到 100；实际计入仍需许可证、测试台和封装窗口完成后续落盘。
- 本轮不送 L2、不封装、不改稳交付 13 个包。
- 客户正式可调用 Skill 仍只有 13 个。
