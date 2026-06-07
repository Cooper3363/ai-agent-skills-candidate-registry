# QUALITY_SOURCE_SPRINT_07 研究结果

更新日期: 2026-06-05

## 任务边界

- 本文件为独立研究线 `QUALITY_SOURCE_SPRINT_07`，不等待 Sprint06 L2/封装。
- 本轮只做候选研究与许可证入队建议，不送 L2、不封装、不客户调用。
- 不调用真实 API/provider，不生成图片/视频/音频，不写 key，不访问真实账号，不读取客户文件，不上传素材，不改稳交付库。
- 客户正式可调用稳交付 Skill 仍为 13。
- 已避开 Sprint01/02/03/04 已平台候选验收的 draft_l3 包、Sprint05 已封装候选、Sprint06 Top8 L2 与 smoke 已处理候选；已明确 `blocked_by_license`、`component_only`、`market_lead_or_retire` 的重复项不再推进，除非本轮给出新 child skill、新许可证证据或新业务定位。

## 统计摘要

| 指标 | 数量 |
| --- | ---: |
| 优质线索总数 | 80 |
| 优先入库候选 | 25 |
| P0 优先候选 | 10 |
| P1 优先候选 | 15 |
| 媒体生成/编辑线索 | 16 |
| 优先入库中的媒体候选 | 5 |
| SaaS/MCP/API 线索 | 34 |
| 优先入库中的 SaaS/MCP/API 候选 | 10 |
| 标准 SKILL.md 包/明确 child skill 线索 | 18 |
| 优先入库中的标准 Skill 包候选 | 7 |
| role/component/template 线索 | 12 |
| 优先入库中的 role/component/template 候选 | 3 |

## 80 个优质线索总表

| # | candidate_id | source_name | source_type | concrete_source | business_package | role | smb_use_case | score | recommended_state | trial_mode | dedupe_relation |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| 1 | `quality_sprint07_last30days_market_signal_brief_candidate` | last30days Skill | standard_skill_package | `mvanhorn/last30days-skill/skills/last30days/SKILL.md` | 销售 | 销售/市场 | 最近 30 天行业/客户/竞品信号简报 | 84 | `needs_license_review` | `metadata_only` | X 线索，需禁真实外网抓取 |
| 2 | `quality_sprint07_graphify_kb_structure_candidate` | graphify Skill | standard_skill_package | `safishamsi/graphify` skill lead | 客服 | 知识库/运营 | 知识库/代码库结构图谱，客服文档结构化 | 80 | `needs_license_review` | `metadata_only` | X 线索，需定位 license/subdir |
| 3 | `quality_sprint07_baoyu_wechat_summary_candidate` | baoyu-wechat-summary | standard_skill_package | `JimLiu/baoyu-skills/skills/baoyu-wechat-summary/SKILL.md` | 客服 | 私域/社群客服 | 微信群聊摘要、客户问题/商机线索 | 82 | `needs_license_review` | `metadata_only` | X 线索，wx-cli/隐私高风险 |
| 4 | `quality_sprint07_fireworks_tech_graph_process_candidate` | fireworks-tech-graph | standard_skill_package | `yizhiyanhua-ai/fireworks-tech-graph` skill lead | 行政/财务/HR | 运营/培训 | 流程图、架构图、SOP 图示 | 79 | `needs_license_review` | `metadata_only` | X 线索，需核 repo/license |
| 5 | `quality_sprint07_guizang_ppt_sales_training_candidate` | Guizang PPT followup | standard_skill_package | `op7418/guizang-ppt-skill/SKILL.md` | 销售 | 销售/培训 | 销售培训/客户方案 deck 元数据 | 78 | `needs_license_review` | `metadata_only` | Sprint05/06 补证据，仍不生成 PPT |
| 6 | `quality_sprint07_baoyu_post_to_wechat_draft_candidate` | baoyu-post-to-wechat | standard_skill_package | `JimLiu/baoyu-skills/skills/baoyu-post-to-wechat/SKILL.md` | 营销 | 新媒体运营 | 公众号文章发布草稿流程，仅 metadata | 70 | `market_lead` | `metadata_only` | 真实发布风险高，不进优先 |
| 7 | `quality_sprint07_awesome_design_skill_child_scan_candidate` | awesome-design-skills child scan | standard_skill_registry | awesome-design-skills child locator | 营销 | 设计/市场 | 设计 child skill 筛选，不整包入库 | 74 | `needs_license_review` | `metadata_only` | X 线索，只作具体 child 定位 |
| 8 | `quality_sprint07_openagentskills_prd_review_child_candidate` | OpenAgentSkills PRD review child | standard_skill_registry | OpenAgentSkills repo TBD | 销售 | 销售/产品 | 客户需求到 PRD/方案检查 | 72 | `market_lead` | `metadata_only` | 需具体 repo |
| 9 | `quality_sprint07_openclaw_customer_support_child_locator_candidate` | OpenClaw support child locator | standard_skill_registry | OpenClaw skills repo TBD | 客服 | 客服主管 | support child 定位 | 72 | `market_lead` | `metadata_only` | 需具体 repo/subdir |
| 10 | `quality_sprint07_hermes_sales_workflow_manifest_candidate` | Hermes sales workflow manifest | standard_skill_registry | Hermes skill lead | 销售 | 销售运营 | 销售跟进 manifest 定位 | 70 | `market_lead` | `metadata_only` | 需真实 manifest |
| 11 | `quality_sprint07_open_design_price_tag_located_candidate` | open-design price tag located | standard_skill_child | `nexu-io/open-design` price-tag locator | 电商/门店 | 门店设计 | 价签/货架标签 child 继续定位 | 73 | `market_lead` | `metadata_only` | 仍缺具体 child |
| 12 | `quality_sprint07_open_design_event_checklist_child_candidate` | open-design event checklist child | standard_skill_child | `nexu-io/open-design` event/template lead | 电商/门店 | 门店运营 | 门店活动海报/清单 child 定位 | 72 | `market_lead` | `metadata_only` | 需具体 child |
| 13 | `quality_sprint07_mdskills_presentation_sales_followup_candidate` | mdskills presentation followup | standard_skill_registry | mdskills presentation lead | 销售 | 销售/管理 | 销售方案 slide spec | 72 | `market_lead` | `metadata_only` | 需具体 repo/license |
| 14 | `quality_sprint07_skillsmd_content_calendar_followup_candidate` | SkillsMD content calendar followup | standard_skill_registry | SkillsMD content planner lead | 营销 | 市场运营 | 内容日历 child 定位 | 71 | `market_lead` | `metadata_only` | 需具体 child |
| 15 | `quality_sprint07_intercom_article_decay_readonly_candidate` | Intercom article decay | SaaS/API connector | Intercom articles/conversations read-only | 客服 | 客服主管 | 帮助中心文章过期/低覆盖提醒 | 82 | `needs_license_review` | `read_only_mock` | Intercom QA 补充 |
| 16 | `quality_sprint07_helpscout_saved_reply_gap_candidate` | Help Scout saved reply gap | SaaS/API connector | Help Scout saved replies/conversations read-only | 客服 | 客服主管 | 宏回复缺口和培训建议 | 81 | `needs_license_review` | `read_only_mock` | Help Scout trend 补充 |
| 17 | `quality_sprint07_front_account_handoff_candidate` | Front account handoff | SaaS/API connector | Front inbox/accounts read-only | 销售 | 销售/客服 | 大客户邮件交接和风险摘要 | 80 | `needs_license_review` | `read_only_mock` | Front SLA 补充 |
| 18 | `quality_sprint07_workable_interview_question_bank_candidate` | Workable interview question bank | SaaS/API connector | Workable jobs/candidates read-only | 行政/财务/HR | HR | JD 到面试题库，不自动录用 | 82 | `needs_license_review` | `read_only_mock` | Workable job posting 补充 |
| 19 | `quality_sprint07_greenhouse_offer_risk_readonly_candidate` | Greenhouse offer risk | SaaS/API connector | Greenhouse offers/candidates read-only | 行政/财务/HR | HR | offer 风险和材料缺口，不发 offer | 80 | `needs_license_review` | `read_only_mock` | Greenhouse pipeline 补充 |
| 20 | `quality_sprint07_bamboohr_probation_review_candidate` | BambooHR probation review | SaaS/API connector | BambooHR employee/time-off read-only | 行政/财务/HR | HR | 试用期提醒、培训完成度和材料缺口 | 81 | `needs_license_review` | `read_only_mock` | BambooHR time-off 补充 |
| 21 | `quality_sprint07_docusign_missing_signature_readonly_candidate` | DocuSign missing signature | SaaS/API connector | DocuSign envelopes read-only | 行政/财务/HR | 行政/销售 | 签署缺口、续约提醒，不发起签署 | 81 | `needs_license_review` | `read_only_mock` | DocuSign renewal 补充 |
| 22 | `quality_sprint07_pandadoc_proposal_followup_candidate` | PandaDoc proposal followup | SaaS/API connector | PandaDoc docs read-only | 销售 | 销售代表 | 提案查看状态和跟进草稿 | 80 | `needs_license_review` | `read_only_mock` | PandaDoc pricing gap 补充 |
| 23 | `quality_sprint07_odoo_receivable_inventory_bridge_candidate` | Odoo receivable inventory bridge | SaaS/API connector | Odoo invoices/inventory read-only | 经营报表 | 管理/财务 | 应收和库存联动风险 | 80 | `needs_license_review` | `read_only_mock` | Odoo crosscheck 补充 |
| 24 | `quality_sprint07_netsuite_vendor_scorecard_candidate` | NetSuite vendor scorecard | SaaS/API connector | NetSuite vendor/PO read-only | 行政/财务/HR | 采购/财务 | 供应商交付/费用评分卡 | 77 | `needs_license_review` | `read_only_mock` | NetSuite PO 补充 |
| 25 | `quality_sprint07_metabase_executive_digest_candidate` | Metabase executive digest | SaaS/API connector | Metabase cards/dashboard read-only | 经营报表 | 管理/运营 | 管理层日报/周报摘要 | 81 | `needs_license_review` | `read_only_mock` | Metabase anomaly 补充 |
| 26 | `quality_sprint07_looker_studio_marketing_digest_candidate` | Looker Studio marketing digest | SaaS/API connector | Looker/Google report lead | 经营报表 | 市场/运营 | 营销看板叙述和异常说明 | 76 | `market_lead` | `mock_only` | API 仍需确认 |
| 27 | `quality_sprint07_amplitude_activation_dropoff_candidate` | Amplitude activation dropoff | SaaS/API connector | Amplitude analytics read-only | 经营报表 | 产品/运营 | 激活漏斗掉点和建议 | 80 | `needs_license_review` | `read_only_mock` | Amplitude retention 补充 |
| 28 | `quality_sprint07_mailchimp_deliverability_qc_candidate` | Mailchimp deliverability QC | SaaS/API connector | Mailchimp reports read-only | 营销 | 市场运营 | 送达率、退订、低互动风险 | 80 | `needs_license_review` | `read_only_mock` | Mailchimp audience health 补充 |
| 29 | `quality_sprint07_brevo_sms_consent_qc_candidate` | Brevo SMS consent QC | SaaS/API connector | Brevo contacts/stats read-only | 营销 | 市场运营 | 短信同意状态和发送风险，不发送 | 79 | `needs_license_review` | `read_only_mock` | Brevo mix 补充 |
| 30 | `quality_sprint07_shopify_return_product_quality_candidate` | Shopify return product quality | SaaS/API connector | Shopify returns/orders read-only | 电商/门店 | 电商运营 | 退货与商品质量问题聚类 | 82 | `needs_license_review` | `read_only_mock` | Shopify subscription 补充 |
| 31 | `quality_sprint07_bigcommerce_promo_margin_candidate` | BigCommerce promo margin | SaaS/API connector | BigCommerce orders/promotions read-only | 电商/门店 | 电商运营 | 促销毛利和库存风险 | 79 | `needs_license_review` | `read_only_mock` | BigCommerce turnover 补充 |
| 32 | `quality_sprint07_woocommerce_product_review_qc_candidate` | WooCommerce review QC | SaaS/API connector | WooCommerce products/reviews read-only | 电商/门店 | 电商运营 | 商品评论主题和售后改进 | 79 | `needs_license_review` | `read_only_mock` | Woo coupon margin 补充 |
| 33 | `quality_sprint07_quickbooks_bill_vendor_trend_candidate` | QuickBooks bill vendor trend | SaaS/API connector | QuickBooks bills/vendors read-only | 行政/财务/HR | 财务/采购 | 供应商账单趋势和异常 | 79 | `needs_license_review` | `read_only_mock` | QuickBooks vendor spend 补充 |
| 34 | `quality_sprint07_xero_cash_collection_gap_candidate` | Xero cash collection gap | SaaS/API connector | Xero invoices/payments read-only | 行政/财务/HR | 财务 | 收款缺口和提醒草稿，不发送 | 80 | `needs_license_review` | `read_only_mock` | Xero tax code 补充 |
| 35 | `quality_sprint07_stripe_refund_policy_mismatch_candidate` | Stripe refund policy mismatch | SaaS/API connector | Stripe refunds/charges read-only | 客服 | 财务/客服 | 退款记录与政策差异提示 | 80 | `needs_license_review` | `read_only_mock` | Stripe failed payment 补充 |
| 36 | `quality_sprint07_hubspot_lead_source_quality_candidate` | HubSpot lead source quality | SaaS/API connector | HubSpot contacts/deals read-only | 销售 | 销售运营 | 线索来源质量和转化风险 | 80 | `needs_license_review` | `read_only_mock` | HubSpot handoff 补充 |
| 37 | `quality_sprint07_salesforce_account_whitespace_candidate` | Salesforce account whitespace | SaaS/API connector | Salesforce account/opportunity read-only | 销售 | 销售主管 | 客户空白机会和跟进建议 | 77 | `needs_license_review` | `read_only_mock` | Salesforce duplicate 补充 |
| 38 | `quality_sprint07_zoho_desk_escalation_matrix_candidate` | Zoho Desk escalation matrix | SaaS/API connector | Zoho Desk tickets read-only | 客服 | 客服主管 | 升级矩阵、SLA 风险和培训建议 | 79 | `needs_license_review` | `read_only_mock` | Zoho Desk KB gap 补充 |
| 39 | `quality_sprint07_pipedrive_next_meeting_prep_candidate` | Pipedrive next meeting prep | SaaS/API connector | Pipedrive activities/deals read-only | 销售 | 销售代表 | 下次会议准备和风险问题 | 79 | `needs_license_review` | `read_only_mock` | Pipedrive lost reason 补充 |
| 40 | `quality_sprint07_freshsales_contact_hygiene_candidate` | Freshsales contact hygiene | SaaS/API connector | Freshsales API lead | 销售 | 销售运营 | 联系人卫生和重复线索 | 76 | `needs_license_review` | `read_only_mock` | Freshworks CRM 新 harness |
| 41 | `quality_sprint07_openai_image_review_to_product_scene_candidate` | OpenAI review to product scene | media_provider | OpenAI Images payload | 电商/门店 | 电商运营 | 用户评价到商品场景图 prompt/payload | 83 | `needs_license_review` | `dry_run_payload_only` | OpenAI brand scene 补充 |
| 42 | `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | OpenAI TTS sales roleplay | media_provider | OpenAI TTS payload | 销售 | 销售培训 | 销售 roleplay 音频 payload | 80 | `needs_license_review` | `dry_run_payload_only` | TTS training 补充 |
| 43 | `quality_sprint07_runway_customer_story_clip_candidate` | Runway customer story clip | media_provider | Runway API payload | 营销 | 市场/短视频 | 客户案例短视频 payload | 80 | `needs_license_review` | `dry_run_payload_only` | Runway storyboard 补充 |
| 44 | `quality_sprint07_fal_packshot_to_lifestyle_candidate` | fal packshot to lifestyle | media_provider | fal image route payload | 电商/门店 | 电商运营 | 白底商品图到生活方式场景 payload | 80 | `needs_license_review` | `route_check` | fal try-on 补充 |
| 45 | `quality_sprint07_replicate_model_catalog_qc_candidate` | Replicate model catalog QC | media_provider | Replicate route catalog | 平台研究 | 研究专员 | 可商用图像/视频模型筛选 | 75 | `needs_license_review` | `route_check` | provider catalog 研究 |
| 46 | `quality_sprint07_pika_product_explainer_route_candidate` | Pika product explainer | media_provider | Pika/fal route payload | 营销 | 短视频运营 | 商品说明视频 payload | 77 | `needs_license_review` | `route_check` | Pika loop 补充 |
| 47 | `quality_sprint07_kling_storefront_video_route_candidate` | Kling storefront video | media_provider | Kling route payload | 电商/门店 | 门店运营 | 门店橱窗视频 payload | 77 | `needs_license_review` | `route_check` | Kling menu video 补充 |
| 48 | `quality_sprint07_hailuo_product_demo_route_candidate` | Hailuo product demo | media_provider | MiniMax/Hailuo route | 营销 | 市场运营 | 产品演示短视频 payload | 77 | `needs_license_review` | `route_check` | Hailuo explainer 补充 |
| 49 | `quality_sprint07_heygen_new_employee_avatar_candidate` | HeyGen new employee avatar | media_provider | HeyGen API payload | 行政/财务/HR | HR/培训 | 新员工培训数字人 payload | 80 | `needs_license_review` | `dry_run_payload_only` | HeyGen sales objection 补充 |
| 50 | `quality_sprint07_tavus_customer_success_avatar_candidate` | Tavus customer success avatar | media_provider | Tavus API payload | 客服 | 客成/客服 | 客户上线视频 payload | 78 | `needs_license_review` | `dry_run_payload_only` | Tavus onboarding 补充 |
| 51 | `quality_sprint07_did_refund_policy_avatar_candidate` | D-ID refund policy avatar | media_provider | D-ID API payload | 客服 | 售后客服 | 退款政策口播 payload | 76 | `needs_license_review` | `dry_run_payload_only` | D-ID store policy 补充 |
| 52 | `quality_sprint07_recraft_packaging_label_candidate` | Recraft packaging label | media_provider | Recraft API payload | 电商/门店 | 电商设计 | 包装标签/贴纸视觉 payload | 78 | `needs_license_review` | `dry_run_payload_only` | Recraft badge 补充 |
| 53 | `quality_sprint07_ideogram_store_event_poster_candidate` | Ideogram store event poster | media_provider | Ideogram API payload | 电商/门店 | 门店运营 | 门店活动海报文字 payload | 77 | `needs_license_review` | `dry_run_payload_only` | Ideogram CN poster 补充 |
| 54 | `quality_sprint07_synthesia_partner_training_avatar_candidate` | Synthesia partner training avatar | media_provider | Synthesia route payload | 销售 | 渠道/培训 | 合作伙伴培训视频 payload | 77 | `needs_license_review` | `dry_run_payload_only` | Synthesia vendor training 补充 |
| 55 | `quality_sprint07_elevenlabs_support_scenario_voice_candidate` | ElevenLabs support scenario voice | media_provider | ElevenLabs API payload | 客服 | 客服培训 | 客服场景音频 payload | 78 | `needs_license_review` | `dry_run_payload_only` | ElevenLabs product voiceover 补充 |
| 56 | `quality_sprint07_creatomate_customer_story_template_candidate` | Creatomate customer story template | media_provider | Creatomate API payload | 营销 | 市场运营 | 客户案例模板视频 payload | 78 | `needs_license_review` | `dry_run_payload_only` | Creatomate product variant 补充 |
| 57 | `quality_sprint07_agency_customer_success_retention_role_candidate` | agency CS retention role | role_asset | agency-agents-zh role | 客服 | 客成/客服 | 续约风险、客户上线和回访 | 76 | `needs_license_review` | `role_smoke_mock` | 客成 role |
| 58 | `quality_sprint07_agency_sales_ops_forecast_role_candidate` | agency sales ops forecast role | role_asset | agency-agents-zh role | 销售 | 销售运营 | 销售预测、商机卫生和周会 | 76 | `needs_license_review` | `role_smoke_mock` | 销售运营 role |
| 59 | `quality_sprint07_agency_hr_recruiting_coordinator_role_candidate` | agency recruiting coordinator | role_asset | agency-agents-zh role | 行政/财务/HR | HR | 招聘协调、面试安排和候选人沟通 | 75 | `needs_license_review` | `role_smoke_mock` | HR role |
| 60 | `quality_sprint07_agency_finance_ap_ar_clerk_role_candidate` | agency AP/AR clerk role | role_asset | agency-agents-zh role | 行政/财务/HR | 财务 | 应收应付提醒、单据核对 | 75 | `needs_license_review` | `role_smoke_mock` | 财务 role |
| 61 | `quality_sprint07_agency_store_visual_merchandiser_role_candidate` | agency visual merchandiser | role_asset | agency-agents-zh role | 电商/门店 | 门店运营/设计 | 陈列、海报、促销视觉检查 | 75 | `needs_license_review` | `role_smoke_mock` | 门店 role |
| 62 | `quality_sprint07_agency_procurement_supplier_manager_role_candidate` | agency supplier manager role | role_asset | agency-agents-zh role | 行政/财务/HR | 采购 | 供应商评分、交付和报价风险 | 75 | `needs_license_review` | `role_smoke_mock` | 采购 role |
| 63 | `quality_sprint07_chinese_collection_call_template_candidate` | Chinese collection call template | template_asset | internal/Chinese template lead | 行政/财务/HR | 财务 | 催款电话/企微话术模板 | 73 | `market_lead` | `mock_only` | 模板资产 |
| 64 | `quality_sprint07_chinese_trial_shift_training_template_candidate` | Chinese trial shift template | template_asset | internal/Chinese template lead | 电商/门店 | 店长/HR | 试岗培训清单和评分表 | 73 | `market_lead` | `mock_only` | 模板资产 |
| 65 | `quality_sprint07_chinese_supplier_rfq_template_candidate` | Chinese supplier RFQ template | template_asset | internal/Chinese template lead | 行政/财务/HR | 采购 | 供应商询价模板和报价口径 | 73 | `market_lead` | `mock_only` | 模板资产 |
| 66 | `quality_sprint07_chinese_support_compensation_template_candidate` | Chinese support compensation template | template_asset | internal/Chinese template lead | 客服 | 客服主管 | 补偿边界、道歉话术和升级模板 | 73 | `market_lead` | `mock_only` | 模板资产 |
| 67 | `quality_sprint07_promptfoo_recruiting_fairness_regression_candidate` | promptfoo recruiting fairness | component | promptfoo eval config | 行政/财务/HR | HR | 招聘文案/问题公平性回归测试 | 76 | `needs_license_review` | `mock_only` | Promptfoo component |
| 68 | `quality_sprint07_deepeval_refund_reply_eval_candidate` | DeepEval refund reply eval | component | confident-ai/deepeval | 客服 | 客服主管 | 售后回复质量评测 | 75 | `needs_license_review` | `mock_only` | DeepEval component |
| 69 | `quality_sprint07_presidio_sales_lead_pii_candidate` | Presidio sales lead PII | component | microsoft/presidio | 销售 | 销售运营 | 潜客资料 PII 遮罩 | 76 | `needs_license_review` | `mock_only` | Presidio component |
| 70 | `quality_sprint07_ragas_hr_policy_qa_eval_candidate` | Ragas HR policy QA eval | component | explodinggradients/ragas | 行政/财务/HR | HR/行政 | HR 制度问答引用质量 | 75 | `needs_license_review` | `mock_only` | Ragas component |
| 71 | `quality_sprint07_docling_product_manual_parser_candidate` | Docling product manual parser | component | docling-project/docling | 客服 | 客服/产品 | 产品说明书结构化，不读真实文件 | 75 | `needs_license_review` | `mock_text_only` | Docling component |
| 72 | `quality_sprint07_unstructured_sop_parser_candidate` | Unstructured SOP parser | component | Unstructured-IO/unstructured | 行政/财务/HR | 行政 | SOP 文档分节，不读真实文件 | 75 | `needs_license_review` | `mock_text_only` | Unstructured component |
| 73 | `quality_sprint07_instructor_refund_case_schema_candidate` | Instructor refund case schema | component | 567-labs/instructor | 客服 | 售后客服 | 售后案例结构化 schema | 76 | `needs_license_review` | `mock_only` | Instructor component |
| 74 | `quality_sprint07_pydantic_ai_lead_intake_router_candidate` | PydanticAI lead intake router | component/workflow | pydantic/pydantic-ai | 销售 | 销售运营 | 表单线索路由 schema | 75 | `needs_license_review` | `mock_only` | PydanticAI component |
| 75 | `quality_sprint07_langgraph_invoice_approval_workflow_candidate` | LangGraph invoice approval workflow | workflow | langchain-ai/langgraph | 行政/财务/HR | 财务/行政 | 发票审批状态机 mock | 74 | `needs_license_review` | `mock_only` | LangGraph workflow |
| 76 | `quality_sprint07_openai_agents_customer_training_router_candidate` | OpenAI Agents customer training router | workflow | openai/openai-agents-python | 客服 | 客服培训 | 培训素材请求路由 mock | 74 | `needs_license_review` | `mock_only` | Agents workflow |
| 77 | `quality_sprint07_autogen_procurement_roleplay_candidate` | AutoGen procurement roleplay | workflow | microsoft/autogen | 行政/财务/HR | 采购 | 采购谈判 roleplay mock | 73 | `needs_license_review` | `mock_only` | AutoGen workflow |
| 78 | `quality_sprint07_crewai_partner_research_workflow_candidate` | CrewAI partner research | workflow | crewAIInc/crewAI | 销售 | BD/销售 | 合作方调研 mock，不抓网页 | 73 | `needs_license_review` | `mock_only` | CrewAI workflow |
| 79 | `quality_sprint07_browser_use_local_listing_audit_candidate` | Browser-use local listing audit | component/tool | browser-use lead | 电商/门店 | 电商运营 | 本地商品页检查，不抓真实网页 | 70 | `market_lead` | `local_only` | 浏览器权限风险 |
| 80 | `quality_sprint07_mcp_local_sql_metrics_mock_candidate` | MCP local SQL metrics mock | MCP/tool | MCP SQL server lead | 经营报表 | 数据/运营 | 本地 mock SQL 指标查询计划 | 70 | `market_lead` | `mock_only` | 数据库权限风险 |

## 25 个优先入库候选摘要

| priority | candidate_id | quality_score | source_type | business_package | trial_mode | 主要理由 |
| --- | --- | ---: | --- | --- | --- | --- |
| P0 | `quality_sprint07_last30days_market_signal_brief_candidate` | 84 | standard_skill_package | 销售 | `metadata_only` | X 线索已定位 SKILL.md，适合市场/竞品信号，但禁真实抓取 |
| P0 | `quality_sprint07_baoyu_wechat_summary_candidate` | 82 | standard_skill_package | 客服 | `metadata_only` | 中文私域/微信群摘要高价值，需严控隐私和 wx-cli |
| P0 | `quality_sprint07_intercom_article_decay_readonly_candidate` | 82 | SaaS/API connector | 客服 | `read_only_mock` | 帮助中心文章过期/低覆盖，高频客服运营 |
| P0 | `quality_sprint07_workable_interview_question_bank_candidate` | 82 | SaaS/API connector | 行政/财务/HR | `read_only_mock` | 招聘面试题库，禁止自动录用 |
| P0 | `quality_sprint07_shopify_return_product_quality_candidate` | 82 | SaaS/API connector | 电商/门店 | `read_only_mock` | 退货与商品质量聚类，电商高频 |
| P0 | `quality_sprint07_metabase_executive_digest_candidate` | 81 | SaaS/API connector | 经营报表 | `read_only_mock` | 管理层报表摘要，适合经营报表 |
| P0 | `quality_sprint07_openai_image_review_to_product_scene_candidate` | 83 | media_provider | 电商/门店 | `dry_run_payload_only` | 用户评价转商品场景图 payload，业务价值高 |
| P0 | `quality_sprint07_graphify_kb_structure_candidate` | 80 | standard_skill_package | 客服 | `metadata_only` | 知识库结构图谱，适合客服文档整理 |
| P0 | `quality_sprint07_docusign_missing_signature_readonly_candidate` | 81 | SaaS/API connector | 行政/财务/HR | `read_only_mock` | 签署缺口/续约提醒，高频且 read-only |
| P0 | `quality_sprint07_mailchimp_deliverability_qc_candidate` | 80 | SaaS/API connector | 营销 | `read_only_mock` | 送达率/退订风险，营销运营高频 |
| P1 | `quality_sprint07_fireworks_tech_graph_process_candidate` | 79 | standard_skill_package | 行政/财务/HR | `metadata_only` | 流程图/SOP 图示，高价值但需补 repo/license |
| P1 | `quality_sprint07_guizang_ppt_sales_training_candidate` | 78 | standard_skill_package | 销售 | `metadata_only` | 销售培训/方案 deck，不生成真实 PPT |
| P1 | `quality_sprint07_helpscout_saved_reply_gap_candidate` | 81 | SaaS/API connector | 客服 | `read_only_mock` | 宏回复缺口和培训建议 |
| P1 | `quality_sprint07_front_account_handoff_candidate` | 80 | SaaS/API connector | 销售 | `read_only_mock` | 大客户邮件交接和风险摘要 |
| P1 | `quality_sprint07_greenhouse_offer_risk_readonly_candidate` | 80 | SaaS/API connector | 行政/财务/HR | `read_only_mock` | offer 风险，不自动决策 |
| P1 | `quality_sprint07_amplitude_activation_dropoff_candidate` | 80 | SaaS/API connector | 经营报表 | `read_only_mock` | 激活漏斗和运营分析 |
| P1 | `quality_sprint07_hubspot_lead_source_quality_candidate` | 80 | SaaS/API connector | 销售 | `read_only_mock` | 线索来源质量，销售运营高频 |
| P1 | `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | 80 | media_provider | 销售 | `dry_run_payload_only` | 销售 roleplay 音频 payload |
| P1 | `quality_sprint07_runway_customer_story_clip_candidate` | 80 | media_provider | 营销 | `dry_run_payload_only` | 客户案例短视频 payload |
| P1 | `quality_sprint07_fal_packshot_to_lifestyle_candidate` | 80 | media_provider | 电商/门店 | `route_check` | 白底商品图转生活方式场景 |
| P1 | `quality_sprint07_heygen_new_employee_avatar_candidate` | 80 | media_provider | 行政/财务/HR | `dry_run_payload_only` | 新员工培训数字人 |
| P1 | `quality_sprint07_agency_sales_ops_forecast_role_candidate` | 76 | role_asset | 销售 | `role_smoke_mock` | 销售运营 role，可模板化 |
| P1 | `quality_sprint07_agency_finance_ap_ar_clerk_role_candidate` | 75 | role_asset | 行政/财务/HR | `role_smoke_mock` | 应收应付 role，高频 |
| P1 | `quality_sprint07_promptfoo_recruiting_fairness_regression_candidate` | 76 | component | 行政/财务/HR | `mock_only` | 招聘公平性回归测试组件 |
| P1 | `quality_sprint07_instructor_refund_case_schema_candidate` | 76 | component | 客服 | `mock_only` | 售后案例结构化 schema |

## P0 清单

1. `quality_sprint07_last30days_market_signal_brief_candidate`
2. `quality_sprint07_baoyu_wechat_summary_candidate`
3. `quality_sprint07_intercom_article_decay_readonly_candidate`
4. `quality_sprint07_workable_interview_question_bank_candidate`
5. `quality_sprint07_shopify_return_product_quality_candidate`
6. `quality_sprint07_metabase_executive_digest_candidate`
7. `quality_sprint07_openai_image_review_to_product_scene_candidate`
8. `quality_sprint07_graphify_kb_structure_candidate`
9. `quality_sprint07_docusign_missing_signature_readonly_candidate`
10. `quality_sprint07_mailchimp_deliverability_qc_candidate`

## P1 清单

1. `quality_sprint07_fireworks_tech_graph_process_candidate`
2. `quality_sprint07_guizang_ppt_sales_training_candidate`
3. `quality_sprint07_helpscout_saved_reply_gap_candidate`
4. `quality_sprint07_front_account_handoff_candidate`
5. `quality_sprint07_greenhouse_offer_risk_readonly_candidate`
6. `quality_sprint07_amplitude_activation_dropoff_candidate`
7. `quality_sprint07_hubspot_lead_source_quality_candidate`
8. `quality_sprint07_openai_tts_sales_roleplay_audio_candidate`
9. `quality_sprint07_runway_customer_story_clip_candidate`
10. `quality_sprint07_fal_packshot_to_lifestyle_candidate`
11. `quality_sprint07_heygen_new_employee_avatar_candidate`
12. `quality_sprint07_agency_sales_ops_forecast_role_candidate`
13. `quality_sprint07_agency_finance_ap_ar_clerk_role_candidate`
14. `quality_sprint07_promptfoo_recruiting_fairness_regression_candidate`
15. `quality_sprint07_instructor_refund_case_schema_candidate`

## 暂缓项风险

- `last30days`：真实运行会外网抓取 Reddit/X/YouTube/HN 等，本轮只做 metadata，后续必须禁用真实抓取或改为用户提供素材。
- `baoyu-wechat-summary`：依赖 `wx-cli` 和微信群数据，隐私/账号/本地权限风险高，只能 metadata/mock。
- `graphify`、`fireworks-tech-graph`：需补 GitHub repo、LICENSE、是否写文件和脚本依赖。
- `guizang-ppt`：不得生成真实 PPT/HTML deck，先核 LICENSE 和文件输出边界。
- 媒体 provider：只做 route/config/payload 研究，不真实生成。
- SaaS/API：只做 read-only/mock/dry-run，不连接真实账号。
