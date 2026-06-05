# L2 Official Top 15 From To 50 Queue

生成时间：2026-06-03

## 来源

- `LICENSE_REVIEW_TO_50_RESULT.md`
- `DEEPAGENTS_SMOKE_TO_50_RESULT.md`

## 结论

本轮 DeepAgents candidate smoke 中 40 个候选 `passed`。从中选择 Top 15 进入正式 L2 simulated 队列。

DeepAgents smoke 通过只代表候选库可试跑，不代表正式 L2 通过，不代表客户正式可调用。

## Top 15 正式 L2 simulated 队列

| rank | candidate_id | business_package | source_project | trial_mode | 入选原因 | 正式 L2 重点 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `refund_policy_reply_draft_candidate` | 客服 | internal_template | mock_only/read_only/external_action_blocked | 退款咨询高频，边界清楚，客服可直接试跑 | 退款政策回复、投诉升级、不得承诺退款/赔偿 |
| 2 | `account_security_handoff_candidate` | 客服 | internal_template + `support_reply_guardrail` | mock_only/read_only/external_action_blocked | 账号安全高风险高频，转人工边界明确 | 账号被盗、验证码失败、不得绕验证 |
| 3 | `support_macro_suggester_candidate` | 客服 | internal_template + `faq_answer_with_citations` | mock_only/read_only/external_action_blocked | 客服话术宏高频，适合引用型 mock L2 | FAQ 宏建议、引用一致性、缺口提示 |
| 4 | `aftersales_return_checklist_candidate` | 客服 | internal_template | mock_only/read_only/external_action_blocked | 售后退换货流程高频，输出清单稳定 | 退货信息核查、换货边界、退款转人工 |
| 5 | `quote_objection_response_candidate` | 销售 | internal_template + `crm_note_structurer` | mock_only/read_only/external_action_blocked | 销售报价异议高频，能体现不越权折扣 | 价格异议、价值回应、折扣边界 |
| 6 | `proposal_outline_candidate` | 销售 | internal_template | mock_only/read_only/external_action_blocked | 方案书大纲适合轻量 callable Skill | 售前方案结构、假设/缺失信息、非合同 |
| 7 | `sales_call_summary_candidate` | 销售 | internal_template + `crm_note_structurer` | mock_only/read_only/external_action_blocked | 销售通话摘要高频，结构化价值明显 | 需求、异议、下一步、隐私边界 |
| 8 | `deal_risk_flagger_candidate` | 销售 | internal_template + `crm_note_structurer` | mock_only/read_only/external_action_blocked | 商机风险标签有明确增量 | 合同/付款/折扣风险、证据片段 |
| 9 | `renewal_reminder_draft_candidate` | 销售/客户成功 | internal_template | dry_run_only/read_only/external_action_blocked | 续费提醒高频，但必须 dry-run | send_allowed=false、write_allowed=false、续费合规 |
| 10 | `ad_variant_brief_candidate` | 营销 | internal_template + `marketing_copy_pack` / `marketing_compliance_guard` | mock_only/read_only/external_action_blocked | 广告变体 brief 高频，合规边界清楚 | 多变体 brief、禁词、敏感行业风险 |
| 11 | `campaign_postmortem_brief_candidate` | 营销/经营 | internal_template + `structured_metric_summary` | mock_only/read_only/external_action_blocked | 活动复盘高频，避免确定归因即可试跑 | 指标复盘、可能原因、数据质量 |
| 12 | `order_inventory_exception_candidate` | 电商 | `claude-office-skills/shopify-automation` + internal dry-run | dry_run_only/read_only/BYOK_required/external_action_blocked | 订单库存异常是新增电商能力，需 dry-run L2 | 不调 Shopify、不改库存、异常核查 |
| 13 | `store_daily_brief_candidate` | 经营报表 | internal_template + `daily_weekly_metrics_reporter` | mock_only/read_only/external_action_blocked | 门店日报适配中小微老板，高频可试跑 | 日报摘要、异常、数据质量 |
| 14 | `cashflow_warning_brief_candidate` | 财务/经营 | internal_template + `structured_metric_summary` | mock_only/read_only/external_action_blocked | 现金流预警价值高，但需财务边界 | 风险提示、非财务建议、人工复核 |
| 15 | `hr_resume_privacy_masker_candidate` | 管理/HR | Microsoft Presidio + `support_pii_redactor` | mock_only/read_only/external_action_blocked | HR PII 脱敏高频，已有 Presidio 路线 | 简历脱敏、保留经历、第三方联系人 |

## 正式 L2 要求

每个 Top 15 候选正式 L2 simulated 必须满足：

- 至少 3 个中文业务用例。
- 固定输入输出 schema。
- 明确失败判定。
- 明确权限边界。
- 明确人工复核触发。
- 明确是否与稳交付 13 个 Skill 重复或组合复用。
- 结论只能为：`L2 通过可封装` / `需补测` / `暂缓` / `未通过` / `仅组件`。

## 未入 Top 15 但 smoke passed 的候选

以下候选保持 `deepagents_smoke_passed` 候选池状态，暂不进入本轮 Top 15 正式 L2：

| candidate_id | 暂缓进入 Top 15 原因 |
| --- | --- |
| `support_sentiment_priority_candidate` | 与工单分类能力接近，优先级低于退款/账号安全/宏建议 |
| `support_knowledge_gap_detector_candidate` | 更适合知识库运营后续批次 |
| `complaint_root_cause_cluster_candidate` | 需要更多投诉样本和脱敏规则 |
| `sales_playbook_step_candidate` | 与销售跟进/CRM 结构化部分重叠 |
| `social_post_repurpose_candidate` | 与营销文案包重叠，后续可做垂直模板 |
| `brand_tone_rewriter_candidate` | 品牌规范输入差异大，后续批次 |
| `channel_copy_adapter_candidate` | 多渠道发布边界复杂，后续批次 |
| `content_calendar_mock_candidate` | dry-run 日历边界清楚，但与 campaign brief 接近 |
| `review_sentiment_cluster_candidate` | 需要评价脱敏/样本量规则 |
| `return_reason_cluster_candidate` | 可与售后退换货组合，后续批次 |
| `sku_margin_risk_candidate` | 需更多成本口径模板 |
| `marketplace_policy_warning_candidate` | 与营销合规包接近 |
| `fulfillment_delay_notice_draft_candidate` | dry-run 通知类，发送边界复杂 |
| `boss_daily_brief_candidate` | 与日报周报稳交付 Skill 接近 |
| `funnel_dropoff_summary_candidate` | 与指标异常分类接近，后续批次 |
| `data_quality_checklist_candidate` | 更适合数据质量组件池 |
| `campaign_metric_anomaly_candidate` | 与 campaign postmortem / metric classifier 接近 |
| `customer_cohort_summary_candidate` | 用户分群隐私和重识别风险需更多规则 |
| `inventory_turnover_brief_candidate` | 依赖库存候选正式 L2 后再推进 |
| `contract_clause_partitioner_candidate` | 合同/法务边界高，后续单独 L2 |
| `purchase_quote_compare_candidate` | 采购决策边界需更多规则 |
| `meeting_minutes_action_candidate` | dry-run 任务类，与 sales meeting component 接近 |
| `reimbursement_policy_check_candidate` | 财务/报销边界高，后续单独 L2 |
| `sop_step_extractor_candidate` | 可作为管理通用模板后续测试 |
| `onboarding_checklist_candidate` | HR/任务写入边界复杂，后续批次 |

## component_only 确认

以下候选不进入 Top 15，不独立送 L2，进入组件池：

| candidate_id | 处理 |
| --- | --- |
| `support_quality_eval_candidate` | 客服质检组合组件 |
| `marketing_claim_risk_tagger_candidate` | 营销合规标签组件 |
| `invoice_amount_consistency_candidate` | 票据金额一致性组件 |

## 权限边界

正式 L2 simulated 仍必须遵守：

- 不安装额外业务依赖。
- 不访问真实账号。
- 不调用真实业务 API。
- 不发送邮件、短信或微信。
- 不写 CRM、日历、任务或业务系统。
- 不抓取真实网页。
- 不上传、不退款、不改库存。
- 不生成真实图片、视频、音频、OCR 或 PDF 结果。
- 不改稳交付 13 个包。

