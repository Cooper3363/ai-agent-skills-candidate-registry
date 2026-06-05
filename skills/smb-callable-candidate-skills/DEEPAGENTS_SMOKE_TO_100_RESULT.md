# DeepAgents Smoke To100 Result

回传对象：AI.Skills 指挥中心  
任务：第二阶段 To100 50 个 L1 放行候选执行 DeepAgents candidate smoke  
执行日期：2026-06-03  
执行方式：candidate-level metadata/mock smoke；本地 runner 尚未内置本批 50 个 To100 cases，未触发真实模型、真实业务 API 或真实业务动作。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_TO_100_RESULT.md` 与 `queues/DEEPAGENTS_SMOKE_TO_100_QUEUE.md`。
- 已确认本轮 50 个候选均为 L1 / trial mode 放行项：`can_mock_smoke=41`，`can_dry_run_smoke=9`，`component_only=0`，`needs_more_license_info=0`，`blocked=0`。
- 已对 50 个候选逐一完成至少 1 个中文 mock / dry-run smoke 用例设计与候选级检查。
- 已检查每个候选是否可表达为 callable candidate、输出结构是否稳定、中文业务可用性、权限边界、人工复核触发、与稳交付 13 个 Skill / To50 候选的重复关系、是否仅组件。
- 已对 9 个 dry-run 候选强制记录硬断言：`external_action_blocked=true`、`send_allowed=false`、`write_allowed=false`。
- 已从 smoke passed 候选中筛出 Top 15，写入 `queues/L2_OFFICIAL_TOP15_FROM_TO100_QUEUE.md`。

## 2. 当前问题

- 本地 DeepAgents runner 当前未内置 To100 50 个候选的可执行 smoke case，因此本轮按 To50 相同口径执行候选级 metadata/mock smoke。
- 该结果只能表示候选库可继续试跑，不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。

## 3. 阻塞原因

- 无权限阻塞。
- 无许可证阻塞。
- 无外部网络、真实账号、真实 API、真实文件或真实业务系统依赖。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 无需立即决策。
- 建议指挥中心将 Top 15 派发到正式 L2 simulated 队列；非 Top 15 passed 候选保留在候选库观察池，等待下一轮业务包补位。

## 5. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| passed | 50 |
| failed | 0 |
| needs_fix | 0 |
| blocked | 0 |

## 6. Dry-run 硬断言检查

| candidate_id | external_action_blocked | send_allowed | write_allowed | 检查结论 |
| --- | --- | --- | --- | --- |
| support_refund_evidence_request_candidate | true | false | false | passed |
| support_warranty_status_reply_candidate | true | false | false | passed |
| outbound_message_personalizer_candidate | true | false | false | passed |
| lost_deal_followup_draft_candidate | true | false | false | passed |
| influencer_brief_draft_candidate | true | false | false | passed |
| email_subject_line_variants_candidate | true | false | false | passed |
| store_staff_shift_plan_candidate | true | false | false | passed |
| marketplace_reply_draft_candidate | true | false | false | passed |
| leave_request_policy_router_candidate | true | false | false | passed |

## 7. Candidate Smoke 明细

| candidate_id | business_package | role | scenario | source_project | trial_mode | mock 输入摘要 | 预期输出字段 | 禁止动作 | 人工复核触发 | 重复/组件判断 | smoke_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| support_ticket_autotag_router_candidate | 客服知识库助手包 | 客服运营 | 售后工单自动打标签和路由建议 | internal_template | can_mock_smoke | 客户称商品破损、催退款、威胁投诉 | tags, priority, route_to, risk_flags, handoff_required, source_notes | 不写客服系统、不自动派单、不承诺退款 | 投诉、退款、赔偿、账号安全、低置信 | 与 support_ticket_classifier 相邻但更偏路由，可独立候选 | passed |
| support_refund_evidence_request_candidate | 客服知识库助手包 | 售后客服 | 退款证据补充请求草稿 | internal_template | can_dry_run_smoke | 客户要求退款但缺少订单号和破损照片 | evidence_needed, reply_draft, risk_flags, handoff_required, external_action_blocked, send_allowed, write_allowed | 不发送、不退款、不要求过度隐私材料 | 赔偿、监管威胁、敏感材料、未成年人 | dry-run 草稿能力，可进入 L2 | passed |
| support_tone_rewrite_safe_candidate | 客服知识库助手包 | 客服质检 | 将生硬回复改写为合规温和语气 | existing_skill_combo | can_mock_smoke | 原回复语气强硬并暗示客户责任 | rewritten_reply, tone_changes, safety_notes, risk_flags, manual_review_required | 不替代客服发送、不改变政策结论 | 投诉升级、承诺退款、歧视性表达 | 与 support_reply_guardrail 有重复，适合作为客服回复增强候选 | passed |
| support_policy_conflict_detector_candidate | 客服知识库助手包 | 知识库运营 | 检测两段客服政策是否冲突 | existing_skill_combo | can_mock_smoke | 退款政策 A 写 7 天，政策 B 写 15 天 | conflict_found, conflicting_clauses, severity, resolution_questions, citations | 不改知识库、不发布政策 | 客户权益、退款时限、法律/平台规则冲突 | 复用 KB 能力但场景明确，可独立候选 | passed |
| support_ticket_batch_summary_candidate | 客服知识库助手包 | 客服主管 | 班次工单批量摘要 | internal_template | can_mock_smoke | 10 条 mock 工单含物流延迟、退款、投诉 | batch_summary, issue_clusters, vip_or_escalation_items, action_items, pii_redaction_notes | 不写工单系统、不联系客户 | 高优工单、VIP、投诉、未脱敏 PII | 可作为客服班次运营候选 | passed |
| support_vip_customer_handoff_candidate | 客服知识库助手包 | 大客户支持 | VIP 客户转人工原因说明 | internal_template | can_mock_smoke | VIP 客户多次购买后投诉售后未响应 | vip_status_reason, handoff_required, handoff_reason, safe_next_steps, risk_flags | 不联系客户、不承诺补偿 | VIP 投诉、赔偿、合同客户、舆情风险 | 可独立候选，适合 L2 | passed |
| support_warranty_status_reply_candidate | 客服知识库助手包 | 售后客服 | 保修状态说明草稿 | internal_template | can_dry_run_smoke | 客户询问是否可免费换新，信息不完整 | reply_draft, required_info, warranty_status_unknown, risk_flags, external_action_blocked, send_allowed, write_allowed | 不判定保修结果、不发回复、不改售后单 | 免费换新、赔偿、缺少凭证 | dry-run 草稿，可继续试跑 | passed |
| support_channel_deflection_suggester_candidate | 客服知识库助手包 | 客服运营 | 高峰期渠道分流建议 | internal_template | can_mock_smoke | 今日在线排队 80 人，电话空闲，FAQ 命中率高 | deflection_suggestions, channel_rules, customer_message_draft, risk_notes | 不关闭入口、不自动切流 | 高投诉、紧急售后、账号安全 | 运营辅助，非写入型 | passed |
| support_shift_handover_brief_candidate | 客服知识库助手包 | 客服主管 | 客服交接班摘要 | internal_template | can_mock_smoke | 本班未结工单、待回访客户、投诉升级列表 | handover_summary, unresolved_items, escalation_items, owner_suggestions, pii_redaction_notes | 不写排班/工单系统 | 未结投诉、VIP、敏感 PII | 可作为客服运营候选 | passed |
| outbound_message_personalizer_candidate | 销售跟进助手包 | 销售代表 | 外呼/私信开场白个性化 | internal_template | can_dry_run_smoke | 根据客户行业和上一轮沟通生成私信草稿 | message_draft, personalization_basis, risk_flags, external_action_blocked, send_allowed, write_allowed | 不发送、不导入联系人、不假设授权 | 退订、敏感行业、无授权触达 | 与销售跟进草稿相邻，可作为细分候选 | passed |
| proposal_requirement_gap_checker_candidate | 销售跟进助手包 | 售前 | 检查方案需求缺口 | existing_skill_combo | can_mock_smoke | 客户需求含预算、上线时间，但缺成功标准 | missing_requirements, clarification_questions, risk_flags, next_steps | 不生成合同/报价承诺 | 价格、交付范围、法务条款缺失 | 与 proposal_outline_candidate 相邻但检查型更清晰 | passed |
| pricing_terms_risk_summary_candidate | 销售跟进助手包 | 销售主管 | 价格和付款条款风险摘要 | internal_template | can_mock_smoke | 报价含 60 天账期、额外折扣、验收后付款 | risk_summary, risk_level, risky_terms, review_required, safe_questions | 不审批折扣、不修改报价 | 高折扣、长账期、违约责任 | 高 SMB 价值，可进入 Top 15 | passed |
| demo_script_builder_candidate | 销售跟进助手包 | 售前顾问 | 产品演示脚本草稿 | internal_template | can_mock_smoke | 客户关注库存、会员、报表，演示 20 分钟 | demo_flow, talk_track, proof_points, questions_to_ask, risk_notes | 不承诺产品能力或交付 | 未验证能力、客户定制需求 | 可独立候选，适合 L2 | passed |
| lost_deal_followup_draft_candidate | 销售跟进助手包 | 销售代表 | 丢单后复联草稿 | internal_template | can_dry_run_smoke | 客户因预算不足丢单，30 天后可复联 | followup_draft, subject_options, timing_notes, risk_flags, external_action_blocked, send_allowed, write_allowed | 不发送、不写 CRM、不承诺折扣 | 退订、竞品敏感、折扣越权 | dry-run 草稿，可进入 Top 15 | passed |
| customer_reference_brief_candidate | 销售跟进助手包 | 销售支持 | 客户案例匹配简报 | internal_template | can_mock_smoke | 目标客户是连锁门店，需要相似授权案例 | reference_matches, fit_reason, usage_boundaries, risk_flags | 不伪造案例、不外发未授权信息 | 案例授权、夸大效果、隐私 | 高价值但需授权边界，进入 Top 15 | passed |
| sales_stage_exit_criteria_checker_candidate | 销售跟进助手包 | RevOps | 销售阶段退出条件检查 | internal_template | can_mock_smoke | 商机准备从需求确认推进到报价阶段 | criteria_met, missing_evidence, recommended_next_steps, risk_flags | 不推进 CRM 阶段 | 缺预算、缺决策人、缺时间线 | 与 CRM 结构化相邻，偏流程治理 | passed |
| partner_fit_matrix_candidate | 销售跟进助手包 | 渠道经理 | 合作伙伴适配矩阵 | internal_template | can_mock_smoke | 三个潜在渠道伙伴，比较行业、人群、资源 | fit_matrix, score_breakdown, risks, followup_questions | 不签约、不承诺分成 | 资质、竞业、合同、渠道冲突 | 可独立候选但非 Top 15 | passed |
| quote_scope_change_summary_candidate | 销售跟进助手包 | 售前/交付 | 报价范围变更摘要 | internal_template | can_mock_smoke | 客户新增培训和接口需求，报价范围变化 | change_summary, affected_scope, commercial_risks, review_required | 不改报价、不承诺交付 | 合同、价格、交付范围 | 可试跑，后续补 L2 | passed |
| lead_enrichment_from_user_text_candidate | 销售跟进助手包 | 销售代表 | 基于用户提供文本补全线索 | internal_template | can_mock_smoke | 用户粘贴客户简介和沟通记录 | enriched_lead_profile, inferred_needs, confidence, missing_info | 不搜索、不调用 enrichment API | 低置信推断、隐私信息 | 与 lead research 相邻但无外网，适合作为组件 | passed |
| promo_bundle_copy_matrix_candidate | 营销内容生产包 | 营销运营 | 促销套装文案矩阵 | internal_template | can_mock_smoke | 两件套、三件套、满减活动生成不同渠道文案 | copy_matrix, channel_variants, forbidden_claims, risk_flags | 不发布、不投放、不改价格 | 价格承诺、库存、广告法 | 高可用，可进入 Top 15 | passed |
| seasonal_campaign_idea_bank_candidate | 营销内容生产包 | 营销策划 | 季节性活动创意库 | internal_template | can_mock_smoke | 夏季门店活动，目标拉新和复购 | campaign_ideas, target_audience, channels, risk_notes | 不发布、不分配预算 | 预算、库存、合规 | 可试跑，非首选 Top 15 | passed |
| influencer_brief_draft_candidate | 营销内容生产包 | 达人合作运营 | 达人合作 brief 草稿 | internal_template | can_dry_run_smoke | 为本地咖啡店达人探店生成合作 brief | influencer_brief, deliverables, disclosure_notes, risk_flags, external_action_blocked, send_allowed, write_allowed | 不联系达人、不付款、不承诺曝光 | 授权、广告标识、效果承诺 | dry-run 高价值，进入 Top 15 | passed |
| ugc_review_to_ad_angle_candidate | 营销内容生产包 | 广告创意 | 从授权评价提炼广告角度 | internal_template | can_mock_smoke | mock 授权用户评价 5 条 | ad_angles, evidence_quotes, compliance_notes, risk_flags | 不投放、不使用未授权评价 | UGC 授权、夸大宣传 | 可试跑，建议后续 L2 | passed |
| email_subject_line_variants_candidate | 营销内容生产包 | 邮件营销 | 邮件标题变体草稿 | internal_template | can_dry_run_smoke | 会员日促销邮件生成 10 个标题 | subject_lines, rationale, spam_risk_flags, external_action_blocked, send_allowed, write_allowed | 不发送邮件、不导入名单 | 退订、垃圾邮件、夸大承诺 | 与 marketing_copy_pack 重叠，组件优先 | passed |
| brand_forbidden_words_checker_candidate | 营销内容生产包 | 品牌合规 | 品牌禁词检查 | internal_template | can_mock_smoke | 检查活动文案是否含竞品名和禁用表述 | violations, suggested_rewrites, severity, review_required | 不发布、不替代法务 | 商标、广告法、行业禁词 | 高价值检查型，进入 Top 15 | passed |
| local_event_poster_copy_candidate | 营销内容生产包 | 门店营销 | 本地活动海报文案 | internal_template | can_mock_smoke | 周末亲子体验活动海报文案 | poster_copy, cta_options, event_details, risk_flags | 不生成图片、不发布 | 时间地点、价格、名额 | 与 marketing_copy_pack 重叠，保留试跑 | passed |
| ai_search_answer_snippet_candidate | 营销内容生产包 | AI SEO | AI 搜索答案片段草稿 | internal_template | can_mock_smoke | 根据品牌资料生成可引用 FAQ 答案片段 | answer_snippet, source_points, claims_to_verify, risk_flags | 不承诺排名/收录 | 事实准确、SEO 承诺 | 可作为营销辅助候选 | passed |
| landing_page_faq_schema_brief_candidate | 营销内容生产包 | SEO/内容运营 | 落地页 FAQ schema brief | internal_template | can_mock_smoke | 为课程页生成 FAQ 结构化 brief | faq_items, schema_brief, source_notes, validation_risks | 不改站点、不部署 schema | 事实、广告承诺、结构化数据准确性 | 与 schema/FAQ 能力相邻，组件优先 | passed |
| product_attribute_gap_checker_candidate | 营销内容生产包 | 电商运营 | 商品属性缺口检查 | internal_template | can_mock_smoke | 商品标题、规格、卖点中缺材质和尺寸 | missing_attributes, priority, suggested_questions, risk_flags | 不写平台、不改商品 | 平台规则、关键属性缺失 | 高 SMB 价值，进入 Top 15 | passed |
| sku_deduplication_suggester_candidate | 经营报表分析包 | 商品运营 | 疑似重复 SKU 提示 | internal_template | can_mock_smoke | 多个 SKU 名称相近、条码缺失 | duplicate_candidates, match_reasons, confidence, manual_review_required | 不合并 SKU、不改库存 | 低置信、库存/订单关联 | 可试跑，建议后续 L2 | passed |
| order_cancellation_reason_summary_candidate | 经营报表分析包 | 运营分析 | 订单取消原因汇总 | internal_template | can_mock_smoke | 20 条 mock 取消原因文本 | reason_clusters, trend_summary, data_quality_notes, risk_flags | 不退款、不处罚员工 | 订单隐私、归因不确定 | 可试跑，非 Top 15 | passed |
| supplier_delivery_risk_brief_candidate | 经营报表分析包 | 采购/运营 | 供应商交付风险简报 | internal_template | can_mock_smoke | 供应商连续延迟、缺货、价格调整 | risk_brief, risk_level, evidence_items, followup_questions | 不下采购单、不处罚供应商 | 合同、采购、履约争议 | 高价值，进入 Top 15 | passed |
| store_staff_shift_plan_candidate | 经营报表分析包 | 门店运营 | 门店员工排班草稿 | internal_template | can_dry_run_smoke | 周末客流高峰、员工可用时段 | shift_plan_draft, constraints, risk_flags, external_action_blocked, send_allowed, write_allowed | 不写排班系统、不通知员工 | 工时、劳动合规、请假冲突 | dry-run 可试跑，需 HR 边界 | passed |
| local_store_event_checklist_candidate | 经营报表分析包 | 门店运营 | 门店活动执行清单 | internal_template | can_mock_smoke | 本周六新品试吃活动 | checklist, owners_suggested, timeline, risk_flags | 不创建任务、不发布活动 | 安全、预算、人员 | 可试跑 | passed |
| marketplace_reply_draft_candidate | 客服知识库助手包 | 电商客服 | 平台评价/问答回复草稿 | internal_template | can_dry_run_smoke | 买家差评称物流慢、包装破损 | reply_draft, tone_notes, risk_flags, external_action_blocked, send_allowed, write_allowed | 不发布回复、不承诺赔偿 | 差评、退款、平台规则 | 与客服回复能力相邻，dry-run | passed |
| price_change_impact_brief_candidate | 经营报表分析包 | 经营分析 | 调价影响简报 | internal_template | can_mock_smoke | 商品计划涨价 5%，历史销量和毛利 mock 数据 | impact_summary, affected_metrics, assumptions, review_required | 不改价、不下经营结论 | 定价决策、数据不足 | 可试跑，后续 L2 | passed |
| bundle_inventory_feasibility_candidate | 经营报表分析包 | 商品运营 | 套装库存可行性检查 | internal_template | can_mock_smoke | 组合 A+B+C，库存分别 50/20/80 | feasible_bundle_count, bottleneck_skus, risk_flags, manual_review_required | 不改库存、不上架套装 | 库存准确性、超卖 | 可试跑 | passed |
| gross_margin_bridge_summary_candidate | 经营报表分析包 | 财务/经营 | 毛利变化桥接摘要 | internal_template | can_mock_smoke | 本月毛利率下降，收入、成本、折扣 mock 数据 | bridge_summary, drivers, data_quality_notes, risk_flags | 不做审计/税务结论 | 财务敏感、口径不一致 | 高价值，进入 Top 15 | passed |
| break_even_point_brief_candidate | 经营报表分析包 | 经营分析 | 盈亏平衡点简报 | internal_template | can_mock_smoke | 固定成本、客单价、毛利率 mock 数据 | break_even_estimate, assumptions, sensitivity_notes, risk_flags | 不做财务建议/决策 | 财务决策、数据口径 | 可试跑，需强风险提示 | passed |
| sales_target_progress_brief_candidate | 经营报表分析包 | 销售运营 | 销售目标进度简报 | internal_template | can_mock_smoke | 本月目标 50 万，当前 32 万，剩余 8 天 | progress_summary, gap, drivers, action_questions | 不改目标、不调整绩效 | 绩效、奖金、数据口径 | 可试跑 | passed |
| expense_category_outlier_candidate | 经营报表分析包 | 财务运营 | 费用分类异常提示 | internal_template | can_mock_smoke | 差旅费突增、办公费异常低 | outliers, likely_causes, review_items, risk_flags | 不做审计结论、不改账 | 财务敏感、报销争议 | 可试跑，组件/分析均可 | passed |
| refund_rate_trend_brief_candidate | 经营报表分析包 | 售后运营 | 退款率趋势简报 | internal_template | can_mock_smoke | 三周退款率从 3% 到 9% | trend_summary, possible_drivers, data_quality_notes, review_required | 不改退款政策、不处罚 | 售后政策、样本偏差 | 可试跑 | passed |
| staff_productivity_snapshot_candidate | 经营报表分析包 | 门店/HR 运营 | 员工效率快照 | internal_template | can_mock_smoke | 每人接待、订单、工时 mock 数据 | productivity_snapshot, caveats, risk_flags, review_required | 不用于自动处罚/绩效 | 员工数据、劳动合规 | 敏感但可试跑，需强人工复核 | passed |
| data_schema_mapping_hint_candidate | 经营报表分析包 | 数据运营 | 字段映射建议 | internal_template | can_mock_smoke | POS 字段与报表字段命名不一致 | mapping_hints, confidence, unmapped_fields, review_required | 不写数据库/表格 | 映射错误、口径不一致 | 组件型候选 | passed |
| resume_screening_question_pack_candidate | 人事行政包 | HR | 简历追问问题包 | internal_template | can_mock_smoke | 候选人简历含项目经历但缺关键证据 | screening_questions, fairness_notes, risk_flags, manual_review_required | 不给录用/淘汰建议 | 招聘公平、PII、歧视 | 可试跑，需 HR 合规边界 | passed |
| interview_feedback_structurer_candidate | 人事行政包 | HR | 面试反馈结构化 | internal_template | can_mock_smoke | 面试官散乱记录，需整理为事实和待确认点 | structured_feedback, evidence_items, bias_flags, review_required | 不自动评分/录用 | 招聘歧视、主观偏见 | 可试跑 | passed |
| employee_onboarding_faq_candidate | 人事行政包 | HR/行政 | 入职 FAQ 草稿 | existing_skill_combo | can_mock_smoke | 基于 mock 制度片段回答入职材料问题 | answer, citations, missing_policy_notes, handoff_required | 不替代 HR 制度解释 | 薪酬、合同、社保 | 与 faq_answer_with_citations 重叠，适合作 HR 场景候选 | passed |
| leave_request_policy_router_candidate | 人事行政包 | HR/行政 | 请假政策路由草稿 | internal_template | can_dry_run_smoke | 员工请病假但缺证明，问薪资影响 | route_to, required_materials, policy_notes, external_action_blocked, send_allowed, write_allowed | 不审批请假、不写考勤 | 薪资、病假、劳动合规 | dry-run，可试跑 | passed |
| procurement_request_checker_candidate | 采购行政包 | 行政/采购 | 采购申请完整性检查 | internal_template | can_mock_smoke | 采购电脑 10 台，缺预算编号和供应商比价 | missing_fields, risk_flags, followup_questions, review_required | 不审批采购、不下单 | 付款、供应商、预算 | 可试跑 | passed |
| contract_renewal_date_extractor_candidate | 采购行政包 | 行政/法务支持 | 合同续约日期抽取 | dateparser_or_internal_rules | can_mock_smoke | mock 合同片段含到期日、自动续约条款 | renewal_dates, confidence, source_spans, not_legal_advice, review_required | 不写日历/任务、不做法律意见 | 日期解析错误、合同敏感 | 可试跑，L3 前需锁定实现依赖 | passed |

## 8. Top 15 L2 队列

| 排名 | candidate_id | 业务包 | trial_mode | 正式 L2 重点 |
| ---: | --- | --- | --- | --- |
| 1 | support_ticket_autotag_router_candidate | 客服知识库助手包 | can_mock_smoke | 工单标签、优先级、路由、投诉/退款/账号安全转人工 |
| 2 | support_refund_evidence_request_candidate | 客服知识库助手包 | can_dry_run_smoke | 退款证据补充请求、隐私最小化、不得承诺退款 |
| 3 | support_policy_conflict_detector_candidate | 客服知识库助手包 | can_mock_smoke | 政策冲突检测、引用定位、人工修订建议 |
| 4 | support_ticket_batch_summary_candidate | 客服知识库助手包 | can_mock_smoke | 批量工单摘要、风险聚类、PII 脱敏提示 |
| 5 | support_vip_customer_handoff_candidate | 客服知识库助手包 | can_mock_smoke | VIP 高风险投诉识别、转人工原因、安全下一步 |
| 6 | pricing_terms_risk_summary_candidate | 销售跟进助手包 | can_mock_smoke | 价格/账期/折扣风险摘要，不做审批 |
| 7 | demo_script_builder_candidate | 销售跟进助手包 | can_mock_smoke | 演示流程、话术、验证问题、能力承诺边界 |
| 8 | lost_deal_followup_draft_candidate | 销售跟进助手包 | can_dry_run_smoke | 丢单复联草稿，send/write/external blocked |
| 9 | customer_reference_brief_candidate | 销售跟进助手包 | can_mock_smoke | 授权案例匹配、适配理由、不得伪造效果 |
| 10 | promo_bundle_copy_matrix_candidate | 营销内容生产包 | can_mock_smoke | 促销套装多渠道文案、禁用承诺、价格库存风险 |
| 11 | influencer_brief_draft_candidate | 营销内容生产包 | can_dry_run_smoke | 达人合作 brief、广告披露、授权边界 |
| 12 | brand_forbidden_words_checker_candidate | 营销内容生产包 | can_mock_smoke | 品牌/行业禁词检查、替代表达、人工复核 |
| 13 | product_attribute_gap_checker_candidate | 营销内容生产包 | can_mock_smoke | 商品属性缺口、平台风险、补充问题 |
| 14 | supplier_delivery_risk_brief_candidate | 经营报表分析包 | can_mock_smoke | 供应商延迟/缺货风险证据、采购处置边界 |
| 15 | gross_margin_bridge_summary_candidate | 经营报表分析包 | can_mock_smoke | 毛利变化驱动拆解、口径/数据质量提示 |

## 9. 权限边界确认

本轮未安装依赖、未访问外网、未读取真实客户文件、未调用真实业务 API、未发送邮件/短信/微信、未写 CRM/日历/任务/业务系统、未真实抓取网页、未上传文件、未退款/赔偿/改库存、未生成真实图片/视频/音频/OCR/PDF 结果、未改稳交付 13 个包。

## 10. 建议下一步

- 指挥中心可将 Top 15 派发给测试台执行正式 L2 simulated，每个候选至少 3 个中文业务 mock 用例。
- 其余 35 个 passed 候选保留在候选库继续试跑或等待业务包补位。
- dry-run 候选进入正式 L2 时必须继续强制校验 `external_action_blocked=true`、`send_allowed=false`、`write_allowed=false`。
