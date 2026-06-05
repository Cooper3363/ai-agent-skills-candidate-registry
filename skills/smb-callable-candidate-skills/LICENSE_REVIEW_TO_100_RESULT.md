# 许可证窗口：候选库扩到 100 第二阶段 L1 / Trial Mode 复核结果

回传时间：2026-06-03

输入文件：

- `RESEARCH_TO_100_RESULT.md`
- `queues/LICENSE_REVIEW_TO_100_QUEUE.md`

## 已完成事项

已按 `RESEARCH_TO_100_RESULT.md` 第 7 节，对第二阶段推荐进入许可证 / trial mode 复核的 50 个新增候选完成轻量 L1。

本轮不安装依赖、不运行真实工具、不登录真实账号、不读取真实客户文件、不发送邮件/短信/微信、不写 CRM/日历/任务/业务系统、不真实抓取网页、不上传文件、不退款、不赔偿、不改库存、不生成真实图片/视频/音频/OCR/PDF 结果、不改稳交付 13 个包。

## 数量汇总

| 结论 | 数量 |
| --- | ---: |
| `can_mock_smoke` | 41 |
| `can_dry_run_smoke` | 9 |
| `component_only` | 0 |
| `needs_more_license_info` | 0 |
| `blocked` | 0 |

## 可送 smoke 候选表

| candidate_id | source_project | license / 来源授权口径 | commercial_use_notes | maintenance_status | dependency_risks | trial_mode | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `support_ticket_autotag_router_candidate` | internal_template | internal_template，无第三方代码 | 只对 mock 工单打标签和建议队列 | N/A | 客服 PII、投诉/退款需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `support_refund_evidence_request_candidate` | internal_template | internal_template，无第三方代码 | 不承诺退款/赔偿，不要求过度隐私材料 | N/A | 退款、退货、隐私材料高风险 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `support_tone_rewrite_safe_candidate` | existing_skill_combo | 复用稳交付客服能力边界 | 只做语气改写和风险提示 | N/A | 不替代客服处置，不发送回复 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `support_policy_conflict_detector_candidate` | existing_skill_combo | 复用 `support_kb_doc_cleaner` / `faq_answer_with_citations` 边界 | 只检测 mock 政策冲突，不改知识库 | N/A | 政策解释、客户权益影响需人工确认 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `support_ticket_batch_summary_candidate` | internal_template | internal_template，无第三方代码 | 只汇总 mock 工单班次 | N/A | 工单 PII、投诉升级需脱敏和人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `support_vip_customer_handoff_candidate` | internal_template | internal_template，无第三方代码 | 只输出 VIP 转人工原因，不直接联系客户 | N/A | 大客户投诉、赔付、账号安全高风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `support_warranty_status_reply_candidate` | internal_template | internal_template，无第三方代码 | 只生成保修说明草稿，不承诺保修结果 | N/A | 保修/退换权益需人工复核 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `support_channel_deflection_suggester_candidate` | internal_template | internal_template，无第三方代码 | 只做高峰期分流建议 | N/A | 不自动改渠道、不关停入口 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `support_shift_handover_brief_candidate` | internal_template | internal_template，无第三方代码 | 只输出交接摘要 | N/A | 未结工单和客户数据需脱敏 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `outbound_message_personalizer_candidate` | internal_template | internal_template，无第三方代码 | 只生成外呼/私信开场白草稿，不发送 | N/A | 外呼、私信、反骚扰/反垃圾规则 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `proposal_requirement_gap_checker_candidate` | existing_skill_combo | 复用 To50 `proposal_outline_candidate` 边界 | 只检查方案需求缺口 | N/A | 不生成合同/报价承诺 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `pricing_terms_risk_summary_candidate` | internal_template | internal_template，无第三方代码 | 只提示价格/付款风险，不做审批 | N/A | 折扣、账期、合同、付款承诺高风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `demo_script_builder_candidate` | internal_template | internal_template，无第三方代码 | 只生成演示脚本草案 | N/A | 不承诺产品能力或交付结果 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `lost_deal_followup_draft_candidate` | internal_template | internal_template，无第三方代码 | 只生成复联草稿，不发送 | N/A | 邮件/短信/CRM 写入禁止 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `customer_reference_brief_candidate` | internal_template | internal_template，无第三方代码 | 只基于授权案例摘要匹配案例 | N/A | 客户案例授权、夸大承诺风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `sales_stage_exit_criteria_checker_candidate` | internal_template | internal_template，无第三方代码 | 只检查阶段证据，不自动推进商机 | N/A | CRM 写入、阶段变更禁止 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `partner_fit_matrix_candidate` | internal_template | internal_template，无第三方代码 | 只输出合作适配矩阵 | N/A | 合同、渠道承诺、资质核验需人工 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `quote_scope_change_summary_candidate` | internal_template | internal_template，无第三方代码 | 只摘要报价范围变更 | N/A | 报价、合同、交付范围需人工确认 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `lead_enrichment_from_user_text_candidate` | internal_template | internal_template，无第三方代码 | 只基于用户提供文本补全线索 | N/A | 不抓取外部网页，不调用数据 enrichment API | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `promo_bundle_copy_matrix_candidate` | internal_template | internal_template，无第三方代码 | 只生成促销文案矩阵，不发布/投放 | N/A | 价格、促销承诺、广告合规 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `seasonal_campaign_idea_bank_candidate` | internal_template | internal_template，无第三方代码 | 只输出活动创意草案 | N/A | 活动合规、预算、库存需人工确认 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `influencer_brief_draft_candidate` | internal_template | internal_template，无第三方代码 | 不承诺曝光/转化/素材授权 | N/A | 达人合作、授权素材、投放合规 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `ugc_review_to_ad_angle_candidate` | internal_template | internal_template，无第三方代码 | 只从 mock/授权评价提炼广告角度 | N/A | UGC 授权、广告合规、个人信息脱敏 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `email_subject_line_variants_candidate` | internal_template | internal_template，无第三方代码 | 只生成标题，不发送邮件 | N/A | 邮件营销、反垃圾邮件、退订要求 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `brand_forbidden_words_checker_candidate` | internal_template | internal_template，无第三方代码 | 只基于用户提供品牌规则检查 | N/A | 品牌/商标/行业合规需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `local_event_poster_copy_candidate` | internal_template | internal_template，无第三方代码 | 只生成海报文案，不生成图片 | N/A | 活动合规、价格和库存信息需确认 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `ai_search_answer_snippet_candidate` | internal_template | internal_template，无第三方代码 | 只生成答案片段草稿，不承诺搜索排名 | N/A | SEO/AEO 承诺、事实准确性 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `landing_page_faq_schema_brief_candidate` | internal_template | internal_template，无第三方代码 | 只输出 FAQ/schema brief，不改站点 | N/A | 结构化数据准确性、广告合规 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `product_attribute_gap_checker_candidate` | internal_template | internal_template，无第三方代码 | 只检查 mock 商品属性缺口 | N/A | 不写电商平台，不自动改商品 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `sku_deduplication_suggester_candidate` | internal_template | internal_template，无第三方代码 | 只提示疑似重复 SKU，不合并商品 | N/A | 商品合并/库存系统写入禁止 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `order_cancellation_reason_summary_candidate` | internal_template | internal_template，无第三方代码 | 只汇总取消原因 | N/A | 订单数据隐私，不做退款/处罚结论 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `supplier_delivery_risk_brief_candidate` | internal_template | internal_template，无第三方代码 | 只输出供应商交付风险 brief | N/A | 采购决策、合同处罚需人工 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `store_staff_shift_plan_candidate` | internal_template | internal_template，无第三方代码 | 只生成排班草案，不写排班系统 | N/A | 员工排班/工时/劳动合规 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `local_store_event_checklist_candidate` | internal_template | internal_template，无第三方代码 | 只输出门店活动执行清单 | N/A | 预算、人员安排、发布动作需人工 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `marketplace_reply_draft_candidate` | internal_template | internal_template，无第三方代码 | 只生成平台回复草稿，不发布 | N/A | 平台评论/问答发布、客户权益 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `price_change_impact_brief_candidate` | internal_template | internal_template，无第三方代码 | 只输出调价影响摘要 | N/A | 不自动改价，不做定价决策 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `bundle_inventory_feasibility_candidate` | internal_template | internal_template，无第三方代码 | 只检查套餐库存可行性，不改库存 | N/A | 库存写入、上架下架、采购单禁止 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `gross_margin_bridge_summary_candidate` | internal_template | internal_template，无第三方代码 | 只输出毛利变化桥接摘要 | N/A | 财务数据敏感，不做审计/税务结论 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `break_even_point_brief_candidate` | internal_template | internal_template，无第三方代码 | 只做盈亏平衡估算，必须非财务建议提示 | N/A | 财务/经营决策需人工 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `sales_target_progress_brief_candidate` | internal_template | internal_template，无第三方代码 | 只输出销售目标进度摘要 | N/A | 不自动调整目标/奖金/绩效 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `expense_category_outlier_candidate` | internal_template | internal_template，无第三方代码 | 只提示费用分类异常 | N/A | 财务、报销、审计结论禁止 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `refund_rate_trend_brief_candidate` | internal_template | internal_template，无第三方代码 | 只输出退款率趋势和核查项 | N/A | 不做处罚/退款政策变更结论 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `staff_productivity_snapshot_candidate` | internal_template | internal_template，无第三方代码 | 不得用于员工处罚或自动绩效判断 | N/A | 员工数据、绩效/劳动合规高敏 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `data_schema_mapping_hint_candidate` | internal_template | internal_template，无第三方代码 | 只输出字段映射建议 | N/A | 不写数据库/表格，映射需人工确认 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `resume_screening_question_pack_candidate` | internal_template | internal_template，无第三方代码 | 只输出面试追问问题，不给录用/淘汰建议 | N/A | HR PII、招聘公平、歧视风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `interview_feedback_structurer_candidate` | internal_template | internal_template，无第三方代码 | 只结构化面试笔记，不给自动评分/录用结论 | N/A | HR PII、招聘决策、偏见风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `employee_onboarding_faq_candidate` | existing_skill_combo | 复用 `faq_answer_with_citations` 与 To50 入职清单边界 | 只基于制度片段输出 FAQ 草稿 | N/A | HR 制度解释需人工确认 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `leave_request_policy_router_candidate` | internal_template | internal_template，无第三方代码 | 只输出请假材料提示和转人工原因 | N/A | HR 制度、薪酬/考勤影响需人工 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `procurement_request_checker_candidate` | internal_template | internal_template，无第三方代码 | 只检查采购申请完整性 | N/A | 采购审批、付款、供应商选择需人工 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke |
| `contract_renewal_date_extractor_candidate` | GitHub: `dateparser/dateparser` 或内部日期规则模板 | `dateparser` 为 BSD-3-Clause；也可改内部规则实现规避依赖 | 只抽取合同日期，不做法律意见，必须 `not_legal_advice=true` | 活跃/一般 | 合同文本敏感；日期解析可能误判；不写日历/任务提醒系统 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents candidate smoke；L3 前锁定是否引入 dateparser |

## component_only 候选表

| candidate_id | source_project | license / 来源授权口径 | dependency_risks | trial_mode | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- | --- | --- |
| 暂无 | 暂无 | 暂无 | 暂无 | 暂无 | 暂无 | 暂无 |

## 需补资料候选表

| candidate_id | source_project | 缺失信息 | trial_mode | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- | --- |
| 暂无 | 暂无 | 暂无 | 暂无 | 暂无 | 暂无 |

## blocked 候选表

| candidate_id | blocking_reason | impact | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- |
| 暂无 | 暂无 | 暂无 | 暂无 | 暂无 |

## 测试台下一步建议

1. 只对本文件中 `can_mock_smoke` 和 `can_dry_run_smoke` 的 50 个候选进入 DeepAgents candidate smoke。
2. 对 9 个 `dry_run_only` 候选统一断言：
   - `external_action_blocked=true`
   - `send_allowed=false`
   - `write_allowed=false`
   - 不调用真实 API / OAuth / 邮件 / 短信 / 微信 / 日历 / 任务 / 库存 / HR / 财务 / 合同系统。
3. 对合同、HR、财务、员工产能、价格/付款条款类候选，测试用例必须包含人工复核触发和非专业意见声明。
4. 本轮不送 L2、不封装、不新增客户正式可调用 Skill；稳交付库仍为 13。
