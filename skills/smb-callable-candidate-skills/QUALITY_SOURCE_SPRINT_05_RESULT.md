# QUALITY_SOURCE_SPRINT_05_RESULT

更新日期: 2026-06-05
生成窗口: AI.Skills 指挥中心主线程补落
任务: Quality Source Sprint 05 研究结果

## Summary

本文件为 Sprint05 候选研究结果。研究窗口已启动但未及时落盘，为避免许可证窗口和测试台空转，指挥中心先补落一版可执行队列。

本轮仍只做候选研究和 L1 队列准备：
- 不调用真实 API/provider。
- 不生成真实图片、视频、音频、HTML、PDF、PPT 或客户文件。
- 不读取、打印或写入 key。
- 不访问真实账号，不读取客户文件，不上传素材。
- 不修改稳交付库。
- 客户正式可调用 Skill 仍为 13。

## Counts

| 指标 | 数量 |
| --- | ---: |
| 优质线索总数 | 80 |
| 优先入库候选 | 25 |
| P0 | 10 |
| P1 | 15 |
| 优先队列中的 SaaS/MCP/API 候选 | 14 |
| 优先队列中的媒体/provider 候选 | 4 |
| 优先队列中的标准 Skill/Agent Skill 候选 | 5 |
| 优先队列中的 role/component 候选 | 2 |
| 本轮新增客户正式可调用 Skill | 0 |
| 客户正式可调用 Skill | 13 |

## De-Dupe Notes

- 已避开 Sprint01/02/03/04 已封装的 40 个 draft_l3 包。
- 已避开已明确 blocked_by_license 或 market_lead_or_retire 的重复项。
- 与已封装 SaaS connector 相邻的候选只保留新渠道或新业务切面。
- 媒体/provider 候选只进入 route/config/payload 研究，不代表真实生成可用。
- SaaS/API/MCP 候选只进入 mock/read-only/dry-run 研究，不代表真实账号或真实 API 通过。
- 标准 Skill 包必须在 L1 阶段继续定位具体 repo、subdir、SKILL.md/manifest、LICENSE 和文件写入边界。

## Priority Candidates

| priority | candidate_id | source_name | source_type | business_package | six_department_role | trial_mode | quality_score | recommended_state |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| P0 | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | Intercom API | SaaS/API connector | 客服 | 客服主管 | read_only_mock | 88 | needs_license_review |
| P0 | `quality_sprint05_helpscout_article_gap_readonly_candidate` | Help Scout API | SaaS/API connector | 客服 | 客服主管 | read_only_mock | 87 | needs_license_review |
| P0 | `quality_sprint05_front_inbox_handoff_readonly_candidate` | Front API | SaaS/API connector | 客服 | 客服主管 | read_only_mock | 86 | needs_license_review |
| P0 | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | Klaviyo API | SaaS/API connector | 营销 | 市场运营 | read_only_mock | 86 | needs_license_review |
| P0 | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | WooCommerce REST API | SaaS/API connector | 电商/门店 | 电商运营 | read_only_mock | 85 | needs_license_review |
| P0 | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | BigCommerce API | SaaS/API connector | 电商/门店 | 电商运营 | read_only_mock | 85 | needs_license_review |
| P0 | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | Google Ads API | SaaS/API connector | 营销 | 投放运营 | read_only_mock | 84 | needs_license_review |
| P0 | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | Google Analytics Data API | SaaS/API connector | 经营报表 | 经营分析 | read_only_mock | 84 | needs_license_review |
| P0 | `quality_sprint05_canva_design_brief_dryrun_candidate` | Canva Connect API | SaaS/design connector | 营销 | 市场/设计 | dry_run_only | 83 | needs_license_review |
| P0 | `quality_sprint05_openai_tts_support_voiceover_payload_candidate` | OpenAI Audio/TTS relay | Media/provider route | 客服/HR | 客服培训/HR 培训 | route_check | 83 | needs_license_review |
| P1 | `quality_sprint05_pika_video_ad_payload_route_candidate` | Pika/pika.rest | Media/provider route | 营销 | 市场/设计 | metadata_or_route_check | 82 | needs_license_review |
| P1 | `quality_sprint05_fal_flux_product_image_payload_candidate` | fal.ai FLUX route | Media/provider route | 电商/门店 | 电商设计 | route_check | 82 | needs_license_review |
| P1 | `quality_sprint05_replicate_background_replace_payload_candidate` | Replicate image workflow | Media/provider route | 电商/门店 | 电商设计 | route_check | 81 | needs_license_review |
| P1 | `quality_sprint05_figma_design_token_audit_readonly_candidate` | Figma REST API | SaaS/API connector | 营销/电商 | 设计运营 | read_only_mock | 81 | needs_license_review |
| P1 | `quality_sprint05_asana_project_risk_readonly_candidate` | Asana API | SaaS/API connector | 行政/销售 | 运营主管 | read_only_mock | 80 | needs_license_review |
| P1 | `quality_sprint05_trello_board_handoff_readonly_candidate` | Trello API | SaaS/API connector | 行政/销售 | 运营主管 | read_only_mock | 79 | needs_license_review |
| P1 | `quality_sprint05_jira_service_sla_readonly_candidate` | Jira Service Management API | SaaS/API connector | 客服/产品 | 客服主管/产品运营 | read_only_mock | 79 | needs_license_review |
| P1 | `quality_sprint05_confluence_policy_gap_readonly_candidate` | Confluence API | SaaS/API connector | 行政/客服 | 运营主管 | read_only_mock | 78 | needs_license_review |
| P1 | `quality_sprint05_bamboohr_onboarding_gap_readonly_candidate` | BambooHR API | SaaS/API connector | 行政/财务/HR | HR | read_only_mock | 78 | needs_license_review |
| P1 | `quality_sprint05_greenhouse_candidate_packet_readonly_candidate` | Greenhouse API | SaaS/API connector | 行政/财务/HR | HR 招聘 | read_only_mock | 77 | needs_license_review |
| P1 | `quality_sprint05_docusign_contract_status_readonly_candidate` | DocuSign eSignature API | SaaS/API connector | 行政/财务/销售 | 行政/销售运营 | read_only_mock | 77 | needs_license_review |
| P1 | `quality_sprint05_openclaw_ui_ux_pro_max_skill_candidate` | OpenClaw / UI UX Pro Max Skill | Standard Agent Skill | 营销/电商 | 市场/设计 | metadata_only | 76 | needs_license_review |
| P1 | `quality_sprint05_openagentskills_guizang_ppt_brief_candidate` | Open Agent Skills / guizang-ppt-skill | Standard Agent Skill | 销售/行政 | 销售/培训 | metadata_only | 76 | needs_license_review |
| P1 | `quality_sprint05_open_design_design_brief_child_candidate` | nexu-io/open-design | Standard Agent Skill | 营销/电商 | 市场/设计 | metadata_only | 75 | needs_license_review |
| P1 | `quality_sprint05_agency_agents_zh_hr_recruiting_role_component_candidate` | agency-agents-zh | Role/component library | 行政/财务/HR | HR 招聘 | role_smoke_component | 74 | needs_license_review |

## 80 Quality Leads

| # | candidate_id | source | type | package | use_case | recommended_state | trial_mode | risk_focus |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | Intercom API | SaaS/API | 客服 | 对话主题、宏回复缺口、升级风险 | needs_license_review | read_only_mock | no reply/no status write |
| 2 | `quality_sprint05_helpscout_article_gap_readonly_candidate` | Help Scout API | SaaS/API | 客服 | mailbox 对话与知识库缺口 | needs_license_review | read_only_mock | conversation privacy |
| 3 | `quality_sprint05_front_inbox_handoff_readonly_candidate` | Front API | SaaS/API | 客服 | 共享 inbox 交接摘要 | needs_license_review | read_only_mock | no send/no assign |
| 4 | `quality_sprint05_livechat_transcript_quality_readonly_candidate` | LiveChat API | SaaS/API | 客服 | 聊天记录质检摘要 | needs_license_review | read_only_mock | no message send |
| 5 | `quality_sprint05_crisp_inbox_faq_gap_readonly_candidate` | Crisp API | SaaS/API | 客服 | inbox FAQ gap | market_lead | read_only_mock | API terms |
| 6 | `quality_sprint05_tidio_chat_coverage_candidate` | Tidio API | SaaS/API | 客服 | 覆盖率与训练建议 | market_lead | read_only_mock | API availability |
| 7 | `quality_sprint05_kustomer_thread_risk_readonly_candidate` | Kustomer API | SaaS/API | 客服 | 客户线程风险 | market_lead | read_only_mock | privacy |
| 8 | `quality_sprint05_jira_service_sla_readonly_candidate` | Jira Service Management | SaaS/API | 客服/产品 | 服务台 SLA 风险 | needs_license_review | read_only_mock | no ticket write |
| 9 | `quality_sprint05_intercom_article_quality_candidate` | Intercom Articles | SaaS/API | 客服 | help article 质量与缺口 | needs_license_review | read_only_mock | no article write |
| 10 | `quality_sprint05_zendesk_sell_pipeline_readonly_candidate` | Zendesk Sell API | SaaS/API | 销售 | pipeline health | market_lead | read_only_mock | no CRM write |
| 11 | `quality_sprint05_close_crm_pipeline_risk_readonly_candidate` | Close API | SaaS/API | 销售 | pipeline risk | needs_license_review | read_only_mock | no email/call |
| 12 | `quality_sprint05_copper_crm_followup_gap_readonly_candidate` | Copper API | SaaS/API | 销售 | follow-up gap | needs_license_review | read_only_mock | no task write |
| 13 | `quality_sprint05_insightly_deal_handoff_readonly_candidate` | Insightly API | SaaS/API | 销售 | deal handoff summary | market_lead | read_only_mock | CRM privacy |
| 14 | `quality_sprint05_capsule_crm_contact_health_candidate` | Capsule API | SaaS/API | 销售 | contact health | market_lead | read_only_mock | no contact update |
| 15 | `quality_sprint05_apollo_lead_list_quality_candidate` | Apollo API | SaaS/API | 销售 | lead list quality | market_lead | dry_run_only | data terms |
| 16 | `quality_sprint05_outreach_sequence_risk_readonly_candidate` | Outreach API | SaaS/API | 销售 | sequence risk | market_lead | read_only_mock | no send |
| 17 | `quality_sprint05_salesloft_cadence_gap_readonly_candidate` | Salesloft API | SaaS/API | 销售 | cadence gap | market_lead | read_only_mock | no send |
| 18 | `quality_sprint05_docusign_contract_status_readonly_candidate` | DocuSign API | SaaS/API | 销售/行政 | 合同状态与缺资料提示 | needs_license_review | read_only_mock | no send/no sign |
| 19 | `quality_sprint05_pandadoc_proposal_gap_readonly_candidate` | PandaDoc API | SaaS/API | 销售 | proposal gap | market_lead | read_only_mock | no document send |
| 20 | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | Klaviyo API | SaaS/API | 营销 | 活动健康与异常 | needs_license_review | read_only_mock | no send/no contact write |
| 21 | `quality_sprint05_constantcontact_campaign_digest_candidate` | Constant Contact API | SaaS/API | 营销 | email digest | needs_license_review | read_only_mock | no send |
| 22 | `quality_sprint05_buffer_social_calendar_gap_candidate` | Buffer API | SaaS/API | 营销 | social calendar gap | needs_license_review | read_only_mock | no publish |
| 23 | `quality_sprint05_hootsuite_social_queue_qc_candidate` | Hootsuite API | SaaS/API | 营销 | social queue QC | market_lead | dry_run_only | no publish |
| 24 | `quality_sprint05_sproutsocial_response_risk_candidate` | Sprout Social API | SaaS/API | 营销 | social response risk | market_lead | read_only_mock | no reply |
| 25 | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | Google Ads API | SaaS/API | 营销 | 创意与预算异常 | needs_license_review | read_only_mock | no campaign write |
| 26 | `quality_sprint05_meta_ads_creative_fatigue_readonly_candidate` | Meta Marketing API | SaaS/API | 营销 | creative fatigue | needs_license_review | read_only_mock | no ad write |
| 27 | `quality_sprint05_linkedin_ads_leadgen_readonly_candidate` | LinkedIn Ads API | SaaS/API | 营销 | lead gen health | needs_license_review | read_only_mock | no campaign write |
| 28 | `quality_sprint05_tiktok_ads_creative_readonly_candidate` | TikTok Ads API | SaaS/API | 营销 | creative performance | needs_license_review | read_only_mock | no campaign write |
| 29 | `quality_sprint05_canva_design_brief_dryrun_candidate` | Canva Connect API | SaaS/design | 营销 | design brief/export plan | needs_license_review | dry_run_only | no export/no upload |
| 30 | `quality_sprint05_figma_design_token_audit_readonly_candidate` | Figma API | SaaS/API | 营销/设计 | token and component audit | needs_license_review | read_only_mock | no file edit |
| 31 | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | WooCommerce REST API | SaaS/API | 电商/门店 | catalog QC | needs_license_review | read_only_mock | no product write |
| 32 | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | BigCommerce API | SaaS/API | 电商/门店 | catalog gap | needs_license_review | read_only_mock | no product write |
| 33 | `quality_sprint05_magento_order_exception_readonly_candidate` | Adobe Commerce API | SaaS/API | 电商/门店 | order exception | needs_license_review | read_only_mock | no order write |
| 34 | `quality_sprint05_prestashop_listing_gap_readonly_candidate` | PrestaShop API | SaaS/API | 电商/门店 | listing gap | needs_license_review | read_only_mock | no product write |
| 35 | `quality_sprint05_odoo_inventory_exception_readonly_candidate` | Odoo API | SaaS/API | 电商/门店 | inventory exception | needs_license_review | read_only_mock | no stock write |
| 36 | `quality_sprint05_toast_menu_sales_digest_candidate` | Toast API | SaaS/API | 电商/门店 | menu sales digest | market_lead | read_only_mock | no order/refund |
| 37 | `quality_sprint05_clover_pos_shift_anomaly_candidate` | Clover API | SaaS/API | 电商/门店 | POS shift anomaly | market_lead | read_only_mock | no payment/refund |
| 38 | `quality_sprint05_ecwid_listing_gap_candidate` | Ecwid API | SaaS/API | 电商/门店 | listing gap | market_lead | read_only_mock | API terms |
| 39 | `quality_sprint05_aftership_tracking_exception_readonly_candidate` | AfterShip API | SaaS/API | 电商/门店 | delivery exception | needs_license_review | read_only_mock | no notify |
| 40 | `quality_sprint05_shippo_label_exception_readonly_candidate` | Shippo API | SaaS/API | 电商/门店 | shipment label exception | market_lead | read_only_mock | no label create |
| 41 | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | Google Analytics Data API | SaaS/API | 经营报表 | landing page dropoff | needs_license_review | read_only_mock | analytics privacy |
| 42 | `quality_sprint05_looker_studio_dashboard_gap_candidate` | Looker Studio/Connector | SaaS/API | 经营报表 | dashboard gap | market_lead | metadata_only | connector terms |
| 43 | `quality_sprint05_mixpanel_retention_drop_readonly_candidate` | Mixpanel API | SaaS/API | 经营报表 | retention drop | needs_license_review | read_only_mock | event privacy |
| 44 | `quality_sprint05_amplitude_activation_gap_candidate` | Amplitude API | SaaS/API | 经营报表 | activation gap | needs_license_review | read_only_mock | event privacy |
| 45 | `quality_sprint05_plausible_traffic_anomaly_candidate` | Plausible API | SaaS/API | 经营报表 | traffic anomaly | needs_license_review | read_only_mock | site privacy |
| 46 | `quality_sprint05_matomo_kpi_daily_brief_candidate` | Matomo API | SaaS/API | 经营报表 | KPI daily brief | needs_license_review | read_only_mock | privacy config |
| 47 | `quality_sprint05_metabase_question_summary_candidate` | Metabase API | SaaS/API | 经营报表 | question summary | needs_license_review | read_only_mock | DB exposure |
| 48 | `quality_sprint05_superset_dashboard_anomaly_candidate` | Superset API | SaaS/API | 经营报表 | dashboard anomaly | needs_license_review | read_only_mock | auth/data scope |
| 49 | `quality_sprint05_grafana_alert_digest_candidate` | Grafana API | SaaS/API | 经营报表 | alert digest | needs_license_review | read_only_mock | no alert write |
| 50 | `quality_sprint05_mode_dashboard_digest_candidate` | Mode API | SaaS/API | 经营报表 | dashboard digest | market_lead | read_only_mock | data privacy |
| 51 | `quality_sprint05_bamboohr_onboarding_gap_readonly_candidate` | BambooHR API | SaaS/API | 行政/财务/HR | onboarding gap | needs_license_review | read_only_mock | HR privacy |
| 52 | `quality_sprint05_greenhouse_candidate_packet_readonly_candidate` | Greenhouse API | SaaS/API | 行政/财务/HR | candidate packet | needs_license_review | read_only_mock | no hiring decision |
| 53 | `quality_sprint05_workable_interview_packet_readonly_candidate` | Workable API | SaaS/API | 行政/财务/HR | interview packet | needs_license_review | read_only_mock | no hiring decision |
| 54 | `quality_sprint05_lever_interview_packet_candidate` | Lever API | SaaS/API | 行政/财务/HR | interview packet | needs_license_review | read_only_mock | candidate privacy |
| 55 | `quality_sprint05_gusto_payroll_exception_metadata_candidate` | Gusto API | SaaS/API | 行政/财务/HR | payroll exception metadata | market_lead | metadata_only | payroll sensitive |
| 56 | `quality_sprint05_deel_contract_renewal_readonly_candidate` | Deel API | SaaS/API | 行政/财务/HR | contract renewal | market_lead | read_only_mock | worker privacy |
| 57 | `quality_sprint05_ramp_card_spend_anomaly_readonly_candidate` | Ramp API | SaaS/API | 行政/财务/HR | spend anomaly | needs_license_review | read_only_mock | card data |
| 58 | `quality_sprint05_expensify_policy_exception_candidate` | Expensify API | SaaS/API | 行政/财务/HR | expense policy exception | needs_license_review | read_only_mock | no approval |
| 59 | `quality_sprint05_freshbooks_invoice_overdue_candidate` | FreshBooks API | SaaS/API | 财务 | overdue invoice | needs_license_review | read_only_mock | no send/no payment |
| 60 | `quality_sprint05_wave_receipt_expense_candidate` | Wave API | SaaS/API | 财务 | receipt expense exception | market_lead | read_only_mock | finance privacy |
| 61 | `quality_sprint05_asana_project_risk_readonly_candidate` | Asana API | SaaS/API | 行政/销售 | project risk | needs_license_review | read_only_mock | no task write |
| 62 | `quality_sprint05_trello_board_handoff_readonly_candidate` | Trello API | SaaS/API | 行政/销售 | board handoff | needs_license_review | read_only_mock | no card write |
| 63 | `quality_sprint05_confluence_policy_gap_readonly_candidate` | Confluence API | SaaS/API | 行政/客服 | policy gap | needs_license_review | read_only_mock | no page write |
| 64 | `quality_sprint05_coda_doc_ops_gap_candidate` | Coda API | SaaS/API | 行政 | doc/table gap | market_lead | read_only_mock | no doc write |
| 65 | `quality_sprint05_dropbox_doc_classifier_candidate` | Dropbox API | SaaS/API | 行政 | file metadata classifier | needs_license_review | read_only_mock | no file move/share |
| 66 | `quality_sprint05_box_contract_folder_risk_candidate` | Box API | SaaS/API | 行政/财务 | contract folder risk | needs_license_review | read_only_mock | no file share |
| 67 | `quality_sprint05_onedrive_doc_privacy_candidate` | Microsoft Graph OneDrive | SaaS/API | 行政 | doc privacy metadata | needs_license_review | read_only_mock | minimal scope |
| 68 | `quality_sprint05_openai_tts_support_voiceover_payload_candidate` | OpenAI Audio/TTS relay | Media/provider | 客服/HR | support training voiceover payload | needs_license_review | route_check | no real audio |
| 69 | `quality_sprint05_pika_video_ad_payload_route_candidate` | Pika/pika.rest | Media/provider | 营销 | short video ad payload | needs_license_review | metadata_or_route_check | API/terms |
| 70 | `quality_sprint05_fal_flux_product_image_payload_candidate` | fal.ai FLUX route | Media/provider | 电商/门店 | product image payload | needs_license_review | route_check | output rights/cost |
| 71 | `quality_sprint05_replicate_background_replace_payload_candidate` | Replicate | Media/provider | 电商/门店 | background replace payload | needs_license_review | route_check | upload/storage |
| 72 | `quality_sprint05_stability_brand_banner_payload_candidate` | Stability AI API | Media/provider | 营销 | brand banner payload | needs_license_review | route_check | output rights |
| 73 | `quality_sprint05_elevenlabs_training_voice_payload_candidate` | ElevenLabs API | Media/provider | HR/客服 | training narration payload | needs_license_review | route_check | voice rights |
| 74 | `quality_sprint05_descript_podcast_clip_payload_candidate` | Descript/Studio API lead | Media/provider | 营销 | podcast clip payload | market_lead | metadata_only | API availability |
| 75 | `quality_sprint05_openclaw_ui_ux_pro_max_skill_candidate` | OpenClaw / UI UX Pro Max | Standard Skill | 营销/电商 | UI rule checklist | needs_license_review | metadata_only | repo/license |
| 76 | `quality_sprint05_openagentskills_guizang_ppt_brief_candidate` | Open Agent Skills / guizang-ppt | Standard Skill | 销售/行政 | PPT brief only | needs_license_review | metadata_only | artifact write |
| 77 | `quality_sprint05_open_design_design_brief_child_candidate` | nexu-io/open-design | Standard Skill | 营销/电商 | design brief child skill | needs_license_review | metadata_only | assets/manifest |
| 78 | `quality_sprint05_deepagents_skills_example_locator_candidate` | langchain-ai/deepagents | Framework/Skill example | 多部门 | skill example locator | needs_license_review | metadata_only | docs/example license |
| 79 | `quality_sprint05_omniskill_support_qa_locator_candidate` | OmniSkill Registry | Standard Skill registry | 客服 | support QA child locator | needs_more_license_info | metadata_only | concrete child skill |
| 80 | `quality_sprint05_agency_agents_zh_hr_recruiting_role_component_candidate` | agency-agents-zh | Role/component | HR | recruiting role card | needs_license_review | role_smoke_component | role license |

## Next Window Assignment

请许可证窗口读取 `queues/LICENSE_REVIEW_QUALITY_SPRINT_05_QUEUE.md`，对 25 个优先候选做轻量 L1 / trial mode 复核。L1 通过只代表可进入 DeepAgents candidate smoke，不代表 L2、封装或客户正式可调用。
