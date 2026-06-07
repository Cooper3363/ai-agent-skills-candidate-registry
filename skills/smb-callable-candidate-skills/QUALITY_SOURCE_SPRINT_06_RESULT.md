# QUALITY_SOURCE_SPRINT_06 研究结果

更新日期: 2026-06-05

## 任务边界

- 本文件为独立研究线 `QUALITY_SOURCE_SPRINT_06`，不等待 Sprint05 测试台 smoke。
- 本轮只做候选研究与许可证入队建议，不送 L2、不封装、不客户调用。
- 不调用真实 API/provider，不生成图片/视频/音频，不写 key，不访问真实账号，不读取客户文件，不上传素材，不改稳交付库。
- 客户正式可调用稳交付 Skill 仍为 13。
- 已避开 Sprint01/02/03/04 已进入 draft_l3 的约 40 个候选包；已避开 Sprint05 进入 L1/smoke 队列的候选，除非本轮给出明显不同 child skill 或更强证据。

## 统计摘要

| 指标 | 数量 |
| --- | ---: |
| 优质线索总数 | 80 |
| 优先入库候选 | 25 |
| P0 优先候选 | 10 |
| P1 优先候选 | 15 |
| 媒体生成/编辑线索 | 18 |
| 优先入库中的媒体候选 | 6 |
| SaaS/MCP/API 线索 | 38 |
| 优先入库中的 SaaS/MCP/API 候选 | 12 |
| 标准 Skill 包/明确 child skill 线索 | 12 |
| 优先入库中的标准 Skill 包候选 | 4 |
| role/component/template 线索 | 12 |
| 优先入库中的 role/component/template 候选 | 3 |

## 80 个优质线索总表

| # | candidate_id | source_name | source_type | concrete_source | business_package | role | smb_use_case | score | recommended_state | trial_mode | dedupe_relation |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| 1 | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | Microsoft Graph SharePoint policy QC | SaaS/API connector | Microsoft Graph SharePoint/Drive read-only | 行政/财务/HR | 行政 | SharePoint 制度页更新、冲突和 FAQ 缺口 | 84 | `needs_license_review` | `read_only_mock` | 不重复 Sprint05 Confluence，补 M365 |
| 2 | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | Microsoft Teams handoff digest | SaaS/API connector | Microsoft Graph Teams/channel messages read-only | 客服 | 客服/运营 | Teams 支持频道交接摘要、升级提醒 | 83 | `needs_license_review` | `read_only_mock` | 不重复 Slack，补 M365 |
| 3 | `quality_sprint06_microsoft_graph_onedrive_file_index_candidate` | OneDrive file index | SaaS/API connector | Microsoft Graph DriveItems metadata read-only | 行政/财务/HR | 行政 | 合同/制度/发票文件元数据分类，不读文件内容 | 81 | `needs_license_review` | `read_only_mock` | Google Drive 补充 |
| 4 | `quality_sprint06_google_workspace_gmail_label_health_candidate` | Gmail label health | SaaS/API connector | Gmail labels/messages metadata read-only | 客服 | 客服主管 | 客服邮箱标签覆盖率、未分类邮件 | 82 | `needs_license_review` | `read_only_mock` | Gmail triage 补充，新标签健康 |
| 5 | `quality_sprint06_google_calendar_resource_utilization_candidate` | Google Calendar resource utilization | SaaS/API connector | Calendar resources/events read-only | 行政/财务/HR | 行政 | 会议室/门店活动资源使用率摘要 | 80 | `needs_license_review` | `read_only_mock` | Calendar schedule 补充 |
| 6 | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | Google Sheets budget variance | SaaS/API connector | Sheets read-only rows | 经营报表 | 财务/运营 | 预算差异、费用异常、行动建议 | 83 | `needs_license_review` | `read_only_mock` | Sheets report 新业务定位 |
| 7 | `quality_sprint06_airtable_customer_case_timeline_candidate` | Airtable customer case timeline | SaaS/API connector | Airtable records read-only | 客服 | 客服主管 | 客户案例时间线、责任人和下一步 | 81 | `needs_license_review` | `read_only_mock` | Airtable vendor quote 补充 |
| 8 | `quality_sprint06_notion_meeting_decision_log_candidate` | Notion decision log | SaaS/API connector | Notion database/page read-only | 行政/财务/HR | 管理/行政 | 决策日志、待办和风险回顾 | 81 | `needs_license_review` | `read_only_mock` | Notion schema QC 补充 |
| 9 | `quality_sprint06_slack_customer_signal_digest_candidate` | Slack customer signal digest | SaaS/API connector | Slack channels read-only | 销售 | 销售/客服 | 客户信号、续约风险、商机线索 | 80 | `needs_license_review` | `read_only_mock` | Slack FAQ/handoff 补充 |
| 10 | `quality_sprint06_jira_release_customer_impact_candidate` | Jira release customer impact | SaaS/API connector | Jira issues/releases read-only | 客服 | 技术客服/运营 | 版本变更对客户影响和公告草稿 | 80 | `needs_license_review` | `read_only_mock` | Jira bug reply 补充 |
| 11 | `quality_sprint06_confluence_sop_gap_candidate` | Confluence SOP gap | SaaS/API connector | Confluence pages read-only | 行政/财务/HR | 行政 | SOP 页面缺口、过期制度和培训建议 | 79 | `needs_license_review` | `read_only_mock` | Sprint05 Confluence 更细分 |
| 12 | `quality_sprint06_zendesk_answerbot_deflection_candidate` | Zendesk deflection analysis | SaaS/API connector | Zendesk tickets/help center read-only | 客服 | 客服主管 | 可自助解决问题和知识库缺口 | 82 | `needs_license_review` | `read_only_mock` | Zendesk SLA 补充 |
| 13 | `quality_sprint06_freshdesk_agent_workload_balance_candidate` | Freshdesk workload balance | SaaS/API connector | Freshdesk tickets/agents read-only | 客服 | 客服主管 | 客服工作量、积压和培训提示 | 81 | `needs_license_review` | `read_only_mock` | Freshdesk 新 Harness |
| 14 | `quality_sprint06_intercom_tag_taxonomy_cleanup_candidate` | Intercom tag taxonomy cleanup | SaaS/API connector | Intercom tags/conversations read-only | 客服 | 客服主管 | 标签体系清理建议，不写标签 | 79 | `needs_license_review` | `read_only_mock` | Intercom QA 补充 |
| 15 | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | HubSpot deal handoff quality | SaaS/API connector | Deals/notes read-only | 销售 | 销售主管 | 商机交接完整度和风险 | 82 | `needs_license_review` | `dry_run_only` | HubSpot meeting outcome 补充 |
| 16 | `quality_sprint06_salesforce_lead_duplicate_readonly_candidate` | Salesforce lead duplicate | SaaS/API connector | Salesforce leads read-only | 销售 | 销售运营 | 线索重复、字段缺口和跟进风险 | 78 | `needs_license_review` | `read_only_mock` | Salesforce starter 更细分 |
| 17 | `quality_sprint06_zoho_crm_pipeline_hygiene_candidate` | Zoho CRM pipeline hygiene | SaaS/API connector | Zoho deals/leads read-only | 销售 | 销售运营 | 管道卫生、逾期商机和字段缺口 | 80 | `needs_license_review` | `dry_run_only` | Zoho CRM followup 补充 |
| 18 | `quality_sprint06_pipedrive_lost_reason_taxonomy_candidate` | Pipedrive lost reason taxonomy | SaaS/API connector | Pipedrive deals read-only | 销售 | 销售主管 | 丢单原因分类和改进建议 | 79 | `needs_license_review` | `read_only_mock` | Pipedrive overdue 补充 |
| 19 | `quality_sprint06_shopify_subscription_order_exception_candidate` | Shopify subscription/order exception | SaaS/API connector | Shopify orders/customers read-only | 电商/门店 | 电商运营 | 订阅订单异常、退款和客户风险 | 81 | `needs_license_review` | `read_only_mock` | Shopify refund 补充 |
| 20 | `quality_sprint06_woocommerce_coupon_margin_check_candidate` | WooCommerce coupon margin check | SaaS/API connector | WooCommerce coupons/orders read-only | 电商/门店 | 电商运营 | 优惠券毛利影响和异常订单 | 79 | `needs_license_review` | `read_only_mock` | WooCommerce refunds 补充 |
| 21 | `quality_sprint06_bigcommerce_inventory_turnover_candidate` | BigCommerce inventory turnover | SaaS/API connector | BigCommerce catalog/orders read-only | 电商/门店 | 电商运营 | 库存周转、滞销 SKU 和补货建议 | 78 | `needs_license_review` | `read_only_mock` | BigCommerce abandoned cart 补充 |
| 22 | `quality_sprint06_odoo_crm_invoice_crosscheck_candidate` | Odoo CRM invoice crosscheck | SaaS/API connector | Odoo sales/invoices read-only | 经营报表 | 管理/财务 | 商机到发票链路核对和漏单提示 | 78 | `needs_license_review` | `read_only_mock` | Odoo margin 补充 |
| 23 | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | Stripe failed payment recovery | SaaS/API connector | Stripe invoices/payment intents read-only | 行政/财务/HR | 财务/客服 | 失败扣款原因和挽回话术草稿，不发起扣款 | 83 | `needs_license_review` | `read_only_mock` | Stripe dispute 补充 |
| 24 | `quality_sprint06_quickbooks_vendor_spend_cluster_candidate` | QuickBooks vendor spend cluster | SaaS/API connector | Vendors/expenses read-only | 行政/财务/HR | 财务/采购 | 供应商费用聚类和异常 | 80 | `needs_license_review` | `read_only_mock` | QuickBooks overdue 补充 |
| 25 | `quality_sprint06_xero_tax_code_consistency_hint_candidate` | Xero tax code consistency hint | SaaS/API connector | Xero invoices/bills read-only | 行政/财务/HR | 财务 | 税码一致性提示，不做税务结论 | 78 | `needs_license_review` | `read_only_mock` | Xero bills 补充 |
| 26 | `quality_sprint06_netsuite_purchase_order_exception_candidate` | NetSuite purchase order exception | SaaS/API connector | NetSuite PO/vendor read-only | 行政/财务/HR | 采购/财务 | 采购订单异常、供应商交付风险 | 76 | `needs_license_review` | `read_only_mock` | NetSuite invoice 补充 |
| 27 | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | BambooHR time-off coverage | SaaS/API connector | BambooHR time-off read-only | 行政/财务/HR | HR/行政 | 请假覆盖、排班冲突和交接提醒 | 81 | `needs_license_review` | `read_only_mock` | BambooHR onboarding 补充 |
| 28 | `quality_sprint06_greenhouse_candidate_pipeline_fairness_candidate` | Greenhouse pipeline fairness | SaaS/API connector | Greenhouse candidates/stages read-only | 行政/财务/HR | HR | 招聘阶段漏斗和公平性提醒，不自动决策 | 78 | `needs_license_review` | `read_only_mock` | Greenhouse interview 补充 |
| 29 | `quality_sprint06_workable_job_posting_gap_candidate` | Workable job posting gap | SaaS/API connector | Workable jobs/candidates read-only | 行政/财务/HR | HR | JD 缺口、候选人问题和面试准备 | 78 | `needs_license_review` | `read_only_mock` | Workable scorecard 补充 |
| 30 | `quality_sprint06_docusign_renewal_notice_gap_candidate` | DocuSign renewal notice gap | SaaS/API connector | DocuSign envelopes read-only | 行政/财务/HR | 行政/销售 | 合同续约/到期提醒，不发起签署 | 80 | `needs_license_review` | `read_only_mock` | DocuSign status 补充 |
| 31 | `quality_sprint06_pandadoc_pricing_clause_gap_candidate` | PandaDoc pricing clause gap | SaaS/API connector | PandaDoc documents read-only | 销售 | 销售/行政 | 报价单价格条款缺口和风险 | 78 | `needs_license_review` | `read_only_mock` | PandaDoc status 补充 |
| 32 | `quality_sprint06_metabase_question_anomaly_candidate` | Metabase question anomaly | SaaS/API connector | Metabase API/read-only cards | 经营报表 | 数据/运营 | BI 问题卡异常摘要和解释 | 79 | `needs_license_review` | `read_only_mock` | Metabase 旧线索新定位 |
| 33 | `quality_sprint06_posthog_funnel_dropoff_candidate` | PostHog funnel dropoff | SaaS/API connector | PostHog insights read-only | 经营报表 | 产品/运营 | 漏斗掉点、转化异常和行动建议 | 80 | `needs_license_review` | `read_only_mock` | PostHog growth 补充 |
| 34 | `quality_sprint06_amplitude_cohort_retention_candidate` | Amplitude cohort retention | SaaS/API connector | Amplitude analytics read-only | 经营报表 | 运营/管理 | 留存分群、流失风险和活动建议 | 78 | `needs_license_review` | `read_only_mock` | 新 analytics harness |
| 35 | `quality_sprint06_google_ads_budget_pacing_candidate` | Google Ads budget pacing | SaaS/API connector | Google Ads reports read-only | 营销 | 市场运营 | 预算消耗节奏、CPA 异常和建议 | 79 | `needs_license_review` | `read_only_mock` | Sprint05 search terms 补充 |
| 36 | `quality_sprint06_meta_ads_creative_fatigue_readonly_candidate` | Meta Ads creative fatigue v2 | SaaS/API connector | Meta Marketing API reports read-only | 营销 | 市场运营 | 创意疲劳、预算分配和素材建议 | 78 | `needs_license_review` | `read_only_mock` | Meta fatigue 补充，非重复包 |
| 37 | `quality_sprint06_mailchimp_audience_health_candidate` | Mailchimp audience health | SaaS/API connector | Mailchimp audience/campaign read-only | 营销 | 市场运营 | 受众健康、退订和低互动分群 | 79 | `needs_license_review` | `read_only_mock` | Mailchimp segment 补充 |
| 38 | `quality_sprint06_brevo_sms_email_mix_candidate` | Brevo SMS/email mix | SaaS/API connector | Brevo stats/contact read-only | 营销 | 市场运营 | 短信/邮件活动表现对比，不发送 | 78 | `needs_license_review` | `read_only_mock` | Brevo segment 补充 |
| 39 | `quality_sprint06_openagentskills_prd_writer_candidate` | OpenAgentSkills PRD writer | standard_skill_registry | concrete repo TBD | 销售 | 产品/销售 | 客户需求到 PRD/方案 brief | 72 | `market_lead` | `metadata_only` | 需具体 repo |
| 40 | `quality_sprint06_openagentskills_brand_writer_candidate` | OpenAgentSkills brand writer | standard_skill_registry | concrete repo TBD | 营销 | 品牌/市场 | 品牌语气和文案规范 child 定位 | 72 | `market_lead` | `metadata_only` | 需具体 repo |
| 41 | `quality_sprint06_wondelai_skill_pack_specific_scan_candidate` | wondelai skills specific scan | standard_skill_registry | `wondelai/skills` | 平台研究 | 研究专员 | 具体 SKILL.md 包目录筛选 | 74 | `needs_license_review` | `metadata_only` | Sprint05 locator 补新证据，但需逐目录 |
| 42 | `quality_sprint06_openclaw_uiux_pro_max_official_path_candidate` | OpenClaw UI/UX Pro Max path | standard_skill_package | `openclaw/skills/skills/adisinghstudent/ui-ux-pro-max-skill` | 营销 | 官网/设计 | UI/UX 审查标准包新路径 | 78 | `needs_license_review` | `metadata_only` | Sprint05 UIUX 备用路径 |
| 43 | `quality_sprint06_guizang_ppt_license_followup_candidate` | Guizang PPT license followup | standard_skill_package | `op7418/guizang-ppt-skill/SKILL.md` | 销售 | 销售/管理 | PPT/HTML deck metadata，仅核许可证 | 76 | `needs_license_review` | `metadata_only` | Sprint05 Guizang PPT 补资料 |
| 44 | `quality_sprint06_open_design_brand_guideline_rewrite_candidate` | open-design brand guideline rewrite | standard_skill_child | `nexu-io/open-design/skills/brand-guidelines/SKILL.md` | 营销 | 品牌/设计 | 改写为自有品牌规范检查模板 | 74 | `market_lead` | `metadata_only` | 规避 Anthropic 品牌资产风险 |
| 45 | `quality_sprint06_open_design_coupon_banner_located_child_candidate` | open-design coupon banner located | standard_skill_child | child path TBD | 营销 | 市场/设计 | 优惠券/banner child 再定位 | 72 | `market_lead` | `metadata_only` | 仍缺具体路径 |
| 46 | `quality_sprint06_omniskill_support_qa_followup_candidate` | OmniSkill support QA followup | standard_skill_registry | specific repo TBD | 客服 | 客服主管 | support QA child 补资料 | 70 | `market_lead` | `metadata_only` | 仍缺 repo/license |
| 47 | `quality_sprint06_openai_image_brand_scene_batch_candidate` | OpenAI image brand scene batch | media_provider | OpenAI Images payload | 营销 | 市场/设计 | 品牌场景图批量变体 payload | 83 | `needs_license_review` | `dry_run_payload_only` | 不重复商品角度，品牌场景 |
| 48 | `quality_sprint06_openai_tts_customer_training_audio_candidate` | OpenAI TTS customer training | media_provider | OpenAI TTS payload | 客服 | 客服培训 | 客服培训音频 payload | 81 | `needs_license_review` | `dry_run_payload_only` | TTS store broadcast 补充 |
| 49 | `quality_sprint06_fal_product_model_tryon_route_candidate` | fal product try-on route | media_provider | fal model route | 电商/门店 | 电商运营 | 服饰/配饰试穿图 payload | 79 | `needs_license_review` | `route_check` | fal 新媒体方向 |
| 50 | `quality_sprint06_replicate_background_replace_route_candidate` | Replicate background replace | media_provider | Replicate route | 电商/门店 | 电商运营 | 商品背景替换 route/payload | 78 | `needs_license_review` | `route_check` | Replicate upscale 补充 |
| 51 | `quality_sprint06_runway_storyboard_to_clip_candidate` | Runway storyboard to clip | media_provider | Runway API payload | 营销 | 短视频运营 | storyboard 到短视频 payload | 81 | `needs_license_review` | `dry_run_payload_only` | Runway image-to-video 补充 |
| 52 | `quality_sprint06_pika_product_loop_video_candidate` | Pika product loop video | media_provider | Pika/fal route payload | 电商/门店 | 电商运营 | 商品循环动效视频 payload | 78 | `needs_license_review` | `route_check` | Pika route 新定位 |
| 53 | `quality_sprint06_kling_image_to_video_menu_candidate` | Kling menu image-to-video | media_provider | Kling API/route payload | 电商/门店 | 门店运营 | 菜单/门店图转短视频 payload | 78 | `needs_license_review` | `route_check` | Kling product motion 补充 |
| 54 | `quality_sprint06_hailuo_avatar_explainer_route_candidate` | Hailuo explainer route | media_provider | MiniMax/Hailuo route | 行政/财务/HR | 培训 | 政策说明短视频 payload | 77 | `needs_license_review` | `route_check` | Hailuo training 补充 |
| 55 | `quality_sprint06_heygen_sales_objection_avatar_candidate` | HeyGen sales objection avatar | media_provider | HeyGen API payload | 销售 | 销售培训 | 销售异议处理数字人 payload | 80 | `needs_license_review` | `dry_run_payload_only` | HeyGen FAQ 补充 |
| 56 | `quality_sprint06_tavus_customer_onboarding_video_candidate` | Tavus customer onboarding video | media_provider | Tavus API payload | 客服 | 客成/客服 | 新客户上线个性化视频 payload | 78 | `needs_license_review` | `dry_run_payload_only` | Tavus personalized sales 补充 |
| 57 | `quality_sprint06_did_store_policy_avatar_candidate` | D-ID store policy avatar | media_provider | D-ID API payload | 电商/门店 | 门店培训 | 门店制度说明数字人 payload | 76 | `needs_license_review` | `dry_run_payload_only` | D-ID policy 补充 |
| 58 | `quality_sprint06_recraft_product_badge_pack_candidate` | Recraft product badge pack | media_provider | Recraft API payload | 电商/门店 | 电商设计 | 商品标签/徽章素材 payload | 78 | `needs_license_review` | `dry_run_payload_only` | Recraft menu icon 补充 |
| 59 | `quality_sprint06_ideogram_event_poster_cn_candidate` | Ideogram event poster CN | media_provider | Ideogram API payload | 营销 | 市场/设计 | 中文活动海报文字 payload | 77 | `needs_license_review` | `dry_run_payload_only` | Ideogram coupon 补充 |
| 60 | `quality_sprint06_synthesia_vendor_training_avatar_candidate` | Synthesia vendor training avatar | media_provider | Synthesia API payload | 行政/财务/HR | 采购/培训 | 供应商培训视频 payload | 77 | `needs_license_review` | `dry_run_payload_only` | Synthesia sales avatar 补充 |
| 61 | `quality_sprint06_agency_ops_coordinator_role_candidate` | agency ops coordinator | role_asset | agency-agents-zh role | 经营报表 | 运营 | 运营协调、指标复盘和任务跟进 | 76 | `needs_license_review` | `role_smoke_mock` | 新 role |
| 62 | `quality_sprint06_agency_customer_training_role_candidate` | agency customer trainer | role_asset | agency-agents-zh role | 客服 | 客服培训 | 客服培训案例和评分建议 | 75 | `needs_license_review` | `role_smoke_mock` | 新 role |
| 63 | `quality_sprint06_agency_purchase_admin_role_candidate` | agency purchase admin | role_asset | agency-agents-zh role | 行政/财务/HR | 采购 | 采购需求、报价比较和风险提示 | 75 | `needs_license_review` | `role_smoke_mock` | 采购 role |
| 64 | `quality_sprint06_agency_store_event_planner_role_candidate` | agency store event planner | role_asset | agency-agents-zh role | 电商/门店 | 店长/运营 | 门店活动排期和任务清单 | 75 | `needs_license_review` | `role_smoke_mock` | 门店 role |
| 65 | `quality_sprint06_agency_b2b_partnership_role_candidate` | agency B2B partnership | role_asset | agency-agents-zh role | 销售 | 销售/BD | 合作方调研和沟通话术 | 74 | `needs_license_review` | `role_smoke_mock` | BD role |
| 66 | `quality_sprint06_agency_hr_policy_explainer_role_candidate` | agency HR policy explainer | role_asset | agency-agents-zh role | 行政/财务/HR | HR | 制度解释和员工问答 | 75 | `needs_license_review` | `role_smoke_mock` | HR role |
| 67 | `quality_sprint06_chinese_invoice_reminder_template_candidate` | Chinese invoice reminder template | template_asset | internal/Chinese template lead | 行政/财务/HR | 财务 | 开票/收款提醒话术模板 | 73 | `market_lead` | `mock_only` | 模板资产 |
| 68 | `quality_sprint06_chinese_refund_negotiation_template_candidate` | Chinese refund negotiation template | template_asset | internal/Chinese template lead | 客服 | 售后客服 | 退款协商话术和升级判断 | 73 | `market_lead` | `mock_only` | 模板资产 |
| 69 | `quality_sprint06_chinese_hiring_jd_template_candidate` | Chinese hiring JD template | template_asset | internal/Chinese template lead | 行政/财务/HR | HR | JD 生成和面试题模板 | 73 | `market_lead` | `mock_only` | 模板资产 |
| 70 | `quality_sprint06_chinese_store_daily_check_template_candidate` | Chinese store daily check template | template_asset | internal/Chinese template lead | 电商/门店 | 店长 | 门店日检和交接清单 | 74 | `market_lead` | `mock_only` | 模板资产 |
| 71 | `quality_sprint06_promptfoo_customer_reply_safety_candidate` | promptfoo customer reply safety | component | promptfoo eval config | 客服 | 客服主管 | 客服回复安全/禁语回归测试 | 75 | `needs_license_review` | `mock_only` | promptfoo sales/marketing 补充 |
| 72 | `quality_sprint06_presidio_vendor_quote_pii_candidate` | Presidio vendor quote PII | component | microsoft/presidio | 行政/财务/HR | 采购/行政 | 报价单联系人/手机号遮罩 | 75 | `needs_license_review` | `mock_only` | Presidio email PII 补充 |
| 73 | `quality_sprint06_ragas_policy_answer_eval_candidate` | Ragas policy answer eval | component | explodinggradients/ragas | 行政/财务/HR | 行政 | 制度问答引用质量评测 | 75 | `needs_license_review` | `mock_only` | Ragas support coverage 补充 |
| 74 | `quality_sprint06_deepeval_sales_email_eval_candidate` | DeepEval sales email eval | component | confident-ai/deepeval | 销售 | 销售主管 | 销售邮件质量评测 | 75 | `needs_license_review` | `mock_only` | DeepEval HR eval 补充 |
| 75 | `quality_sprint06_docling_invoice_policy_parser_candidate` | Docling invoice policy parser | component | docling-project/docling | 行政/财务/HR | 财务/行政 | 发票制度文本结构化，不读真实文件 | 75 | `needs_license_review` | `mock_text_only` | Docling contract appendix 补充 |
| 76 | `quality_sprint06_unstructured_hr_handbook_parser_candidate` | Unstructured HR handbook parser | component | Unstructured-IO/unstructured | 行政/财务/HR | HR | 员工手册文本分节 | 75 | `needs_license_review` | `mock_text_only` | Unstructured vendor quote 补充 |
| 77 | `quality_sprint06_instructor_sales_call_schema_candidate` | Instructor sales call schema | component | 567-labs/instructor | 销售 | 销售主管 | 销售电话摘要结构化 schema | 76 | `needs_license_review` | `mock_only` | Instructor purchase schema 补充 |
| 78 | `quality_sprint06_pydantic_ai_support_policy_router_candidate` | PydanticAI support policy router | component/workflow | pydantic/pydantic-ai | 客服 | 客服主管 | 售后政策路由和置信度 schema | 75 | `needs_license_review` | `mock_only` | Pydantic refund router 补充 |
| 79 | `quality_sprint06_langgraph_customer_onboarding_workflow_candidate` | LangGraph customer onboarding workflow | workflow | langchain-ai/langgraph | 客服 | 客成/客服 | 新客户上线流程状态机 mock | 74 | `needs_license_review` | `mock_only` | LangGraph HR onboarding 补充 |
| 80 | `quality_sprint06_openai_agents_finance_doc_router_candidate` | OpenAI Agents finance doc router | workflow | openai/openai-agents-python | 行政/财务/HR | 财务/行政 | 财务文档分类路由 mock | 74 | `needs_license_review` | `mock_only` | OpenAI Agents marketing router 补充 |

## 25 个优先入库候选摘要

| priority | candidate_id | quality_score | source_type | business_package | trial_mode | 主要理由 |
| --- | --- | ---: | --- | --- | --- | --- |
| P0 | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | 84 | SaaS/API connector | 行政/财务/HR | `read_only_mock` | M365 制度页高频，read-only Harness 价值高 |
| P0 | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | 83 | SaaS/API connector | 客服 | `read_only_mock` | Teams 支持频道交接适合客服运营 |
| P0 | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | 83 | SaaS/API connector | 经营报表 | `read_only_mock` | 表格预算差异是中小微报表高频 |
| P0 | `quality_sprint06_zendesk_answerbot_deflection_candidate` | 82 | SaaS/API connector | 客服 | `read_only_mock` | 客服自助分流和知识库缺口高价值 |
| P0 | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | 82 | SaaS/API connector | 销售 | `dry_run_only` | 商机交接质量适合销售运营 |
| P0 | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | 83 | SaaS/API connector | 行政/财务/HR | `read_only_mock` | 失败支付挽回高频，但不处理付款 |
| P0 | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | 81 | SaaS/API connector | 行政/财务/HR | `read_only_mock` | 请假覆盖和排班冲突是 HR 高频 |
| P0 | `quality_sprint06_openai_image_brand_scene_batch_candidate` | 83 | media_provider | 营销 | `dry_run_payload_only` | 品牌场景图批量变体，route 清晰 |
| P0 | `quality_sprint06_runway_storyboard_to_clip_candidate` | 81 | media_provider | 营销 | `dry_run_payload_only` | storyboard 到短视频，营销高价值 |
| P0 | `quality_sprint06_wondelai_skill_pack_specific_scan_candidate` | 74 | standard_skill_registry | 平台研究 | `metadata_only` | Sprint05 暂缓项有更明确 repo 线索，适合逐目录 L1 |
| P1 | `quality_sprint06_google_workspace_gmail_label_health_candidate` | 82 | SaaS/API connector | 客服 | `read_only_mock` | Gmail 标签健康，客服邮箱高频 |
| P1 | `quality_sprint06_freshdesk_agent_workload_balance_candidate` | 81 | SaaS/API connector | 客服 | `read_only_mock` | Freshdesk 工作量平衡，高频客服运营 |
| P1 | `quality_sprint06_shopify_subscription_order_exception_candidate` | 81 | SaaS/API connector | 电商/门店 | `read_only_mock` | Shopify 订阅/订单异常新场景 |
| P1 | `quality_sprint06_docusign_renewal_notice_gap_candidate` | 80 | SaaS/API connector | 行政/财务/HR | `read_only_mock` | 合同续约提醒高频，禁止签署 |
| P1 | `quality_sprint06_posthog_funnel_dropoff_candidate` | 80 | SaaS/API connector | 经营报表 | `read_only_mock` | 漏斗掉点适合经营/运营 |
| P1 | `quality_sprint06_mailchimp_audience_health_candidate` | 79 | SaaS/API connector | 营销 | `read_only_mock` | 受众健康和退订风险高频 |
| P1 | `quality_sprint06_openclaw_uiux_pro_max_official_path_candidate` | 78 | standard_skill_package | 营销 | `metadata_only` | Sprint05 UI/UX Pro Max 补 OpenClaw 路径证据 |
| P1 | `quality_sprint06_guizang_ppt_license_followup_candidate` | 76 | standard_skill_package | 销售 | `metadata_only` | Sprint05 Guizang PPT 补 license followup |
| P1 | `quality_sprint06_openai_tts_customer_training_audio_candidate` | 81 | media_provider | 客服 | `dry_run_payload_only` | 客服培训 TTS payload |
| P1 | `quality_sprint06_fal_product_model_tryon_route_candidate` | 79 | media_provider | 电商/门店 | `route_check` | fal 试穿图 route，需 provider L1 |
| P1 | `quality_sprint06_heygen_sales_objection_avatar_candidate` | 80 | media_provider | 销售 | `dry_run_payload_only` | 销售异议数字人培训 |
| P1 | `quality_sprint06_agency_ops_coordinator_role_candidate` | 76 | role_asset | 经营报表 | `role_smoke_mock` | 运营协调 role，可模板化 |
| P1 | `quality_sprint06_agency_purchase_admin_role_candidate` | 75 | role_asset | 行政/财务/HR | `role_smoke_mock` | 采购 role，高频 |
| P1 | `quality_sprint06_promptfoo_customer_reply_safety_candidate` | 75 | component | 客服 | `mock_only` | 客服回复安全回归组件 |
| P1 | `quality_sprint06_instructor_sales_call_schema_candidate` | 76 | component | 销售 | `mock_only` | 销售电话结构化 schema |

## P0 清单

1. `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate`
2. `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate`
3. `quality_sprint06_google_sheets_budget_variance_harness_candidate`
4. `quality_sprint06_zendesk_answerbot_deflection_candidate`
5. `quality_sprint06_hubspot_deal_handoff_quality_candidate`
6. `quality_sprint06_stripe_failed_payment_recovery_draft_candidate`
7. `quality_sprint06_bamboohr_timeoff_coverage_candidate`
8. `quality_sprint06_openai_image_brand_scene_batch_candidate`
9. `quality_sprint06_runway_storyboard_to_clip_candidate`
10. `quality_sprint06_wondelai_skill_pack_specific_scan_candidate`

## P1 清单

1. `quality_sprint06_google_workspace_gmail_label_health_candidate`
2. `quality_sprint06_freshdesk_agent_workload_balance_candidate`
3. `quality_sprint06_shopify_subscription_order_exception_candidate`
4. `quality_sprint06_docusign_renewal_notice_gap_candidate`
5. `quality_sprint06_posthog_funnel_dropoff_candidate`
6. `quality_sprint06_mailchimp_audience_health_candidate`
7. `quality_sprint06_openclaw_uiux_pro_max_official_path_candidate`
8. `quality_sprint06_guizang_ppt_license_followup_candidate`
9. `quality_sprint06_openai_tts_customer_training_audio_candidate`
10. `quality_sprint06_fal_product_model_tryon_route_candidate`
11. `quality_sprint06_heygen_sales_objection_avatar_candidate`
12. `quality_sprint06_agency_ops_coordinator_role_candidate`
13. `quality_sprint06_agency_purchase_admin_role_candidate`
14. `quality_sprint06_promptfoo_customer_reply_safety_candidate`
15. `quality_sprint06_instructor_sales_call_schema_candidate`

## 暂缓项风险

- OmniSkill support QA child：仍未定位具体 repo/subdir/LICENSE，继续 market lead。
- Open-design coupon/banner child：仍缺具体 child path，继续 market lead。
- Wondelai skill pack：本轮有更明确 repo 线索，但必须逐目录核 `SKILL.md` 与 LICENSE，不能整包放行。
- Pika/Kling/Hailuo/fal/Replicate 等媒体 provider：只能 route/config/payload 研究，不得真实生成。
- Microsoft/Google/Atlassian/SaaS API：只能 read-only/mock/dry-run，不得连接真实账号或写系统。
