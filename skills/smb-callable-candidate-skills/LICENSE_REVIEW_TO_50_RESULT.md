# 许可证窗口：候选库扩到 50 第一阶段 L1 / Trial Mode 复核结果

回传时间：2026-06-03

输入文件：

- `RESEARCH_TO_50_RESULT.md`
- `queues/LICENSE_REVIEW_TO_50_QUEUE.md`

## 总体结论

本轮已按指挥中心 v0 研究结果，对推荐进入许可证 / trial mode 的 43 个候选完成轻量 L1 复核。

本轮不安装依赖、不运行真实工具、不登录账号、不读取真实客户文件、不发送、不写入、不抓取、不上传、不生成真实媒体。

| 类别 | 数量 | 说明 |
| --- | ---: | --- |
| 可送 smoke | 40 | 32 个 `can_mock_smoke`，8 个 `can_dry_run_smoke` |
| component_only | 3 | 可作为组合组件或内部评测组件，不独立算可试跑 Skill |
| needs_more_license_info | 0 | 本轮 43 个均为 internal_template、existing_skill_combo 或已完成上游定位 |
| blocked | 0 | 无输入阻塞 |

## 复核口径

- `internal_template`：不复用第三方代码，只使用内部模板和 mock 输入，可按 `internal_template` 进入 mock smoke。
- `existing_skill_combo`：复用 13 个稳交付 Skill 的能力边界，不新增第三方许可证风险。
- `GitHub / internal dry-run`：仅允许 mock/dry-run，不允许真实 API、OAuth、库存写入、通知发送或外部动作。
- 财务、合同、薪酬、邮件、日历、任务、网页抓取、图片/视频生成等高风险动作，统一加 `external_action_blocked`，且只允许 mock 或 dry-run。

## 可送 smoke 候选表

| candidate_id | source_project | license | commercial_use_notes | maintenance_status | dependency_risks | trial_mode | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `refund_policy_reply_draft_candidate` | internal_template | internal_template，无第三方代码 | 仅输出退款政策回复草稿，不承诺退款 | N/A | 客服退款高敏，需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `account_security_handoff_candidate` | internal_template + `support_reply_guardrail` | 复用稳交付 Skill 边界 | 账号安全只做转人工提示，不绕验证 | N/A | 账号恢复/验证码/身份验证高风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `support_macro_suggester_candidate` | internal_template + `faq_answer_with_citations` | 复用稳交付 Skill 边界 | 只基于 mock FAQ 输出话术草稿 | N/A | 引用准确性、不得编造政策 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `support_sentiment_priority_candidate` | internal_template + `support_ticket_classifier` | 复用稳交付 Skill 边界 | 仅做情绪/优先级建议 | N/A | 投诉、退款、隐私需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `aftersales_return_checklist_candidate` | internal_template | internal_template，无第三方代码 | 仅生成退换货核查清单 | N/A | 不做退款/赔付/售后处置结论 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `support_knowledge_gap_detector_candidate` | internal_template + `faq_answer_with_citations` | 复用稳交付 Skill 边界 | 仅识别知识库缺口，不自动改知识库 | N/A | 知识库引用、客户问题脱敏 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `complaint_root_cause_cluster_candidate` | internal_template | internal_template，无第三方代码 | 只处理 mock/脱敏投诉文本 | N/A | 投诉、退款、赔偿必须人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `quote_objection_response_candidate` | internal_template + `crm_note_structurer` | 复用稳交付 Skill 边界 | 仅输出报价异议回复草稿，不承诺折扣 | N/A | 折扣、合同、付款承诺高风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `proposal_outline_candidate` | internal_template | internal_template，无第三方代码 | 仅输出方案书大纲 | N/A | 不生成合同/报价承诺 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `sales_call_summary_candidate` | internal_template + `crm_note_structurer` | 复用稳交付 Skill 边界 | 只处理 mock 通话记录 | N/A | 销售录音/客户数据需授权，本轮不处理真实音频 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `deal_risk_flagger_candidate` | internal_template + `crm_note_structurer` | 复用稳交付 Skill 边界 | 仅输出商机风险标签 | N/A | 合同、付款、折扣风险需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `renewal_reminder_draft_candidate` | internal_template | internal_template，无第三方代码 | 只生成 `send_allowed=false` 的续费提醒草稿 | N/A | 邮件/短信/CRM 发送禁止 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `sales_playbook_step_candidate` | internal_template + `crm_note_structurer` | 复用稳交付 Skill 边界 | 仅输出下一步建议，不自动推进销售流程 | N/A | 折扣、合同、付款承诺需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `social_post_repurpose_candidate` | internal_template + `marketing_copy_pack` | 复用稳交付 Skill 边界 | 只生成社媒草稿，不发布 | N/A | 内容版权、平台规则、广告合规 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `ad_variant_brief_candidate` | internal_template + `marketing_copy_pack` / `marketing_compliance_guard` | 复用稳交付 Skill 边界 | 只生成广告变体 brief，不投放 | N/A | 广告法、禁词、敏感行业 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `campaign_postmortem_brief_candidate` | internal_template + `structured_metric_summary` | 复用稳交付 Skill 边界 | 仅输出活动复盘摘要 | N/A | 经营数据解释不得当作确定归因 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `brand_tone_rewriter_candidate` | internal_template + `marketing_copy_pack` | 复用稳交付 Skill 边界 | 只改写 mock 文案，不使用第三方品牌素材 | N/A | 品牌/商标/素材来源 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `channel_copy_adapter_candidate` | internal_template + `marketing_copy_pack` | 复用稳交付 Skill 边界 | 只生成多渠道草稿，不发布 | N/A | 短信/公众号/平台发布动作禁止 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `content_calendar_mock_candidate` | internal_template + `structured_campaign_brief` | 复用稳交付 Skill 边界 | 只输出内容日历草案，不写日历/任务/发布系统 | N/A | 日历、任务、发布动作禁止 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `order_inventory_exception_candidate` | `claude-office-skills/skills/shopify-automation` + internal dry-run | 子 Skill frontmatter 标 MIT；需保留后续 n8n 模板条款核验点 | 仅 mock/dry-run，不真实调用 Shopify API | 一般，具体子 Skill 已定位 | Shopify API、库存更新、采购单、通知、CRM/财务系统写入全部禁止 | `dry_run_only`, `read_only`, `BYOK_required`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `review_sentiment_cluster_candidate` | internal_template | internal_template，无第三方代码 | 只处理 mock 商品评价 | N/A | 评价中可能含个人信息，需脱敏 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `return_reason_cluster_candidate` | internal_template | internal_template，无第三方代码 | 只处理 mock 退货原因 | N/A | 不做售后处置/退款结论 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `store_daily_brief_candidate` | internal_template + `daily_weekly_metrics_reporter` | 复用稳交付 Skill 边界 | 只输出门店日报摘要 | N/A | 经营数据隐私，不做重大经营决策 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `sku_margin_risk_candidate` | internal_template + `metric_exception_classifier` | 复用稳交付 Skill 边界 | 只提示 SKU 毛利异常和核查步骤 | N/A | 不做定价/采购决策 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `marketplace_policy_warning_candidate` | internal_template + `marketing_compliance_guard` | 复用稳交付 Skill 边界 | 只提示平台政策风险，不上传商品 | N/A | 平台规则、禁词、类目合规需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `fulfillment_delay_notice_draft_candidate` | internal_template | internal_template，无第三方代码 | 只生成 `send_allowed=false` 的延迟发货通知草稿 | N/A | 短信/邮件/站内信发送禁止 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `boss_daily_brief_candidate` | internal_template + `daily_weekly_metrics_reporter` | 复用稳交付 Skill 边界 | 只输出老板日报摘要 | N/A | 经营建议边界，需数据质量提示 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `cashflow_warning_brief_candidate` | internal_template + `structured_metric_summary` | 复用稳交付 Skill 边界 | 只输出现金流风险提示，不做财务建议 | N/A | 财务高敏，不做融资/税务/审计结论 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `funnel_dropoff_summary_candidate` | internal_template + `metric_exception_classifier` | 复用稳交付 Skill 边界 | 只输出漏斗掉点和核查步骤 | N/A | 不做确定归因 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `data_quality_checklist_candidate` | internal_template | internal_template，无第三方代码 | 只输出数据质量检查清单 | N/A | 不连接外部数据库，不写表格 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `campaign_metric_anomaly_candidate` | internal_template + `metric_exception_classifier` | 复用稳交付 Skill 边界 | 只输出活动指标异常摘要 | N/A | 不做确定归因或预算建议 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `customer_cohort_summary_candidate` | internal_template | internal_template，无第三方代码 | 只处理 mock 分群数据 | N/A | 用户分群隐私、小样本重识别风险 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `inventory_turnover_brief_candidate` | internal_template + `order_inventory_exception_candidate` | 复用候选 dry-run 边界 | 只输出库存周转摘要 | N/A | 不写库存系统，不触发采购单 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `hr_resume_privacy_masker_candidate` | Microsoft Presidio + `support_pii_redactor` | Presidio 为 MIT；复用已测 PII 脱敏路线 | 只处理 mock 或授权简历文本 | 活跃 | HR PII、中文实体规则覆盖率、误脱敏/漏脱敏；不做录用/淘汰判断 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `contract_clause_partitioner_candidate` | internal_template | internal_template，无第三方代码 | 只做合同条款分区，必须 `not_legal_advice=true` | N/A | 合同/法务高风险，不输出法律意见 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `purchase_quote_compare_candidate` | internal_template | internal_template，无第三方代码 | 只输出采购报价对比草案，不做采购决策 | N/A | 供应商数据、价格承诺、采购决策需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `meeting_minutes_action_candidate` | internal_template + `sales_meeting_task_brief_candidate` | 复用候选 dry-run 边界 | 只输出 dry-run 任务草案，不写日历/任务系统 | N/A | 日历/任务写入禁止 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `reimbursement_policy_check_candidate` | internal_template + `expense_invoice_parser` | 复用稳交付 Skill 边界 | 只检查材料完整性，不做报销/税务/审计结论 | N/A | 财务/报销高敏 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |
| `sop_step_extractor_candidate` | internal_template | internal_template，无第三方代码 | 只提取 SOP 步骤和缺口 | N/A | 不写流程系统 | `mock_only`, `read_only`, `external_action_blocked` | `can_mock_smoke` | 送 DeepAgents mock smoke |
| `onboarding_checklist_candidate` | internal_template | internal_template，无第三方代码 | 只生成入职清单草案，不写 HR 系统 | N/A | HR/任务系统写入禁止 | `dry_run_only`, `read_only`, `external_action_blocked` | `can_dry_run_smoke` | 送 DeepAgents dry-run smoke |

## component_only 候选表

| candidate_id | source_project | license | commercial_use_notes | maintenance_status | dependency_risks | trial_mode | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `support_quality_eval_candidate` | internal_template / existing_skill_combo | 复用稳交付 Skill 边界 | 可作为客服质检组合组件，不建议独立封装 | N/A | 客服对话 PII、投诉/退款复核 | `mock_only`, `read_only`, `external_action_blocked` | `component_only` | 进入组件池；不独立送 smoke |
| `marketing_claim_risk_tagger_candidate` | internal_template + `marketing_compliance_guard` | 复用稳交付 Skill 边界 | 与营销合规检查重叠，适合作为标签组件 | N/A | 广告法、敏感行业、禁词需人工复核 | `mock_only`, `read_only`, `external_action_blocked` | `component_only` | 进入组件池；不独立送 smoke |
| `invoice_amount_consistency_candidate` | internal_template + `expense_invoice_parser` | 复用稳交付 Skill 边界 | 仅作票据金额一致性组件 | N/A | 财务/票据敏感，不做报销/税务/审计结论 | `mock_only`, `read_only`, `external_action_blocked` | `component_only` | 进入组件池；不独立送 smoke |

## 需补资料候选表

| candidate_id | source_project | 缺失信息 | trial_mode | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- | --- |
| 暂无 | 暂无 | 暂无 | 暂无 | 暂无 | 暂无 |

## blocked 候选表

| candidate_id | blocking_reason | impact | L1/trial 结论 | 建议动作 |
| --- | --- | --- | --- | --- |
| 暂无 | 暂无 | 暂无 | 暂无 | 暂无 |

## 建议测试台下一步

1. 将 40 个 `can_mock_smoke` / `can_dry_run_smoke` 候选送 DeepAgents candidate smoke。
2. 对 `dry_run_only` 候选统一断言：
   - `external_action_blocked=true`
   - `send_allowed=false`
   - `write_allowed=false`
   - 不调用真实 API / OAuth / 日历 / 邮件 / 库存 / HR / 财务系统。
3. 3 个 `component_only` 候选进入组件池，不独立计入可试跑 Skill。
4. smoke 通过后，再由测试台决定哪些进入正式 L2 simulated；本文件不构成 L2 通过或封装许可。
