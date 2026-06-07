# QUALITY_SOURCE_SPRINT_04_RESULT

更新日期: 2026-06-05

## Summary

本文件为 Quality Source Sprint 04 的候选研究结果。因研究窗口长时间停在落盘阶段，指挥中心先补落一版可供许可证窗口继续处理的合格队列。

本轮只做候选研究与 L1 队列准备：

- 不调用真实 API/provider。
- 不生成图片、视频、音频、HTML、PDF、PPT 或真实文件。
- 不写 key，不读取密钥，不访问真实账号，不读取客户文件。
- 不上传素材，不发送消息，不写 CRM/POS/财务/HR/协作系统。
- 不修改稳交付库。
- 客户正式可调用 Skill 仍为 13。

## Counts

| 指标 | 数量 |
| --- | ---: |
| 优质线索总数 | 80 |
| 优先入库候选 | 25 |
| P0 | 10 |
| P1 | 15 |
| 优先队列中的 SaaS/MCP/API 候选 | 12 |
| 优先队列中的媒体/provider 候选 | 8 |
| 优先队列中的标准 Skill/Agent Skill 候选 | 4 |
| 优先队列中的 role/component 候选 | 1 |
| 客户正式可调用 Skill | 13 |

## De-dupe Notes

- 已避开 Sprint01/02/03 已封装的 30 个 draft_l3 包。
- 与旧线索能力相邻但业务切面不同的候选，已在 `dedupe_relation` 中标明。
- SaaS/MCP/API 类默认只允许 `read_only_mock` 或 `dry_run_only`。
- 媒体类默认只允许 `route_check` / `dry_run_payload_only`，真实生成必须另走真实 provider smoke 审批。
- 标准 Skill 包必须由许可证窗口继续定位具体 repo、subdir、`SKILL.md`、manifest 与 LICENSE；只凭 marketplace 页面不能进入正式 smoke。

## Priority Candidates

| priority | candidate_id | source_name | source_url | source_type | concrete_subdir_or_manifest | has_skill_md | has_skill_yaml | has_manifest | deepagents_fit | openai_compatible_route_fit | external_provider_dependency | business_package | six_department_role | smb_use_case | quality_score | dedupe_relation | recommended_state | trial_mode | license_review_focus | test_smoke_focus | is_media_generation | real_generation_possible | byok_required | real_harness_or_provider_smoke_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | Zendesk API | https://developer.zendesk.com/api-reference/ | SaaS/API connector | Zendesk tickets/macros/help-center adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 客服 | 客服主管 | 只读分析工单 SLA 风险、宏回复缺口和知识库缺口 | 88 | 避开 Sprint03 `zendesk_macro_gap`，本轮聚焦 SLA + macro 双视角 | needs_license_review | read_only_mock | Zendesk API terms, ticket privacy, macro/help-center read-only scope | mock tickets + macros -> sla_risk, macro_gaps, manual_review | no | no | yes | true |
| P0 | `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | Freshdesk API | https://developers.freshdesk.com/api/ | SaaS/API connector | Freshdesk tickets/SLA read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 客服 | 客服主管 | 只读识别超时工单、升级建议、风险标签 | 87 | 新客服 SaaS 来源，补 Zendesk/Gorgias 之外渠道 | needs_license_review | read_only_mock | Freshdesk API terms, SLA/ticket read scope, no reply/no update | mock tickets -> sla_risks, escalation_candidates | no | no | yes | true |
| P0 | `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | Salesforce API | https://developer.salesforce.com/docs/ | SaaS/API connector | Salesforce opportunities/accounts dry-run adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 销售 | 销售主管 | 生成商机健康度、缺字段、下一步建议的 dry-run payload | 87 | 与 HubSpot/Zoho/Pipedrive 不重复，补 Salesforce 生态 | needs_license_review | dry_run_only | Salesforce API/OAuth terms, CRM privacy, no write/no task/no email | mock opportunities -> health_report, dryrun_payload | no | no | yes | true |
| P0 | `quality_sprint04_shopline_catalog_qc_readonly_candidate` | Shopline Open API | https://open.shopline.io/ | SaaS/API connector | Shopline products/catalog read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 电商/门店 | 电商运营 | 只读检查商品标题、属性、图片、价格字段缺口 | 86 | 补 Shopify/Square 之外的亚洲电商渠道 | needs_license_review | read_only_mock | Shopline API terms, catalog read scope, no product/write/inventory change | mock products -> catalog_qc_report | no | no | yes | true |
| P0 | `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | Lightspeed API | https://developers.lightspeedhq.com/ | SaaS/API connector | Lightspeed POS sales/inventory read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 电商/门店 | 门店店长 | 只读生成班次销售异常、退货异常、库存提示 | 86 | 补 Square/Clover 之外门店 POS 渠道 | needs_license_review | read_only_mock | Lightspeed API terms, POS data privacy, no refund/no inventory write | mock shift rows -> anomaly_report | no | no | yes | true |
| P0 | `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | Xero API | https://developer.xero.com/documentation/api/accounting/overview | SaaS/API connector | Xero bank transactions/invoices read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 行政/财务/HR | 财务 | 只读提示银行流水与发票/应收应付不一致，非审计结论 | 85 | 区别于旧 Xero AR followup，本轮聚焦 reconciliation exception | needs_license_review | read_only_mock | Xero API terms, accounting data privacy, non-tax/non-audit disclaimer | mock transactions -> reconciliation_flags | no | no | yes | true |
| P0 | `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | PostHog API | https://posthog.com/docs/api | SaaS/API connector | PostHog events/funnels read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 经营报表 | 经营/产品 | 只读分析漏斗掉点、转化异常、数据质量 | 85 | 新增长/产品分析渠道，不重复日报类 Skill | needs_license_review | read_only_mock | PostHog API terms, event privacy, no tracking config write | mock funnel stats -> dropoff_brief | no | no | yes | true |
| P0 | `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | Linear API | https://developers.linear.app/docs/graphql/working-with-the-graphql-api | SaaS/API connector | Linear issues/custom fields read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 客服/产品 | 客服主管/产品运营 | 从客户反馈类 issue 中提炼影响范围、优先级和客服回传建议 | 84 | 新产品/客服协作渠道，补 Slack/Jira 之外入口 | needs_license_review | read_only_mock | Linear API terms, issue privacy, no status/write/comment | mock issues -> triage_summary | no | no | yes | true |
| P0 | `quality_sprint04_runway_video_ad_payload_candidate` | Runway API | https://docs.dev.runwayml.com/ | Media provider API | provider route/payload manifest to be generated | no | no | no | payload_adapter | provider_route_or_openai_compatible_relay | yes | 营销 | 市场/设计 | 短视频广告脚本到 provider payload，不真实生成 | 84 | 补真实视频 provider 链路，区别于 OpenAI image route | needs_license_review | route_check | Runway API terms, commercial output, cost cap, asset upload/storage | mock ad brief -> video_payload, safety_fields | yes | yes | yes | true |
| P0 | `quality_sprint04_heygen_avatar_training_payload_candidate` | HeyGen API | https://docs.heygen.com/ | Media/avatar provider API | provider route/payload manifest to be generated | no | no | no | payload_adapter | provider_route_or_openai_compatible_relay | yes | 行政/财务/HR | HR/培训 | 培训脚本到数字人口播 payload，不真实生成 | 84 | 补数字人培训视频路线 | needs_license_review | route_check | HeyGen API terms, avatar/voice/likeness rights, cost cap | mock training script -> avatar_video_payload | yes | yes | yes | true |
| P1 | `quality_sprint04_synthesia_hr_training_video_payload_candidate` | Synthesia API | https://docs.synthesia.io/ | Media/avatar provider API | provider route/payload manifest to be generated | no | no | no | payload_adapter | provider_route | yes | 行政/财务/HR | HR/培训 | 员工制度培训视频 payload，不真实生成 | 82 | 与 HeyGen 同类，作为备选 provider | needs_license_review | route_check | Synthesia API terms, avatar rights, commercial use, cost cap | mock HR brief -> video_payload | yes | yes | yes | true |
| P1 | `quality_sprint04_recraft_brand_asset_payload_candidate` | Recraft API | https://www.recraft.ai/ | Image provider API | provider route/payload manifest to be generated | no | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 品牌 banner、图标、促销视觉 payload，不真实生成 | 82 | 补 image provider，多路由备选 | needs_license_review | route_check | Recraft API terms, output rights, brand asset policy | mock campaign -> image_payload | yes | yes | yes | true |
| P1 | `quality_sprint04_ideogram_poster_copy_image_payload_candidate` | Ideogram API | https://ideogram.ai/ | Image provider API | provider route/payload manifest to be generated | no | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 带文字海报/门店菜单视觉 payload，不真实生成 | 81 | 补中文文字海报可能路线，需验 provider 能力 | needs_license_review | route_check | Ideogram terms, text rendering, output rights, cost cap | mock poster brief -> image_payload | yes | yes | yes | true |
| P1 | `quality_sprint04_pika_short_video_payload_candidate` | Pika API/product | https://pika.art/ | Media provider lead | provider route/payload manifest required | no | no | no | payload_adapter_possible | provider_route_possible | yes | 营销 | 市场/设计 | 商品短视频创意 payload 或 provider lead，不真实生成 | 80 | 视频 provider 备选，API/条款需进一步定位 | needs_license_review | metadata_or_route_check | API availability, commercial terms, cost, asset upload policy | mock product brief -> video_payload_spec | yes | possible | possible | true |
| P1 | `quality_sprint04_tavus_sales_avatar_payload_candidate` | Tavus API | https://docs.tavus.io/ | Avatar/video provider API | provider route/payload manifest to be generated | no | no | no | payload_adapter | provider_route | yes | 销售 | 销售主管 | 销售跟进数字人口播 payload，不发送、不真实生成 | 80 | 补销售数字人场景 | needs_license_review | route_check | Tavus API terms, consent/likeness, no outbound send | mock pitch script -> avatar_payload | yes | yes | yes | true |
| P1 | `quality_sprint04_did_avatar_support_script_payload_candidate` | D-ID API | https://docs.d-id.com/ | Avatar/video provider API | provider route/payload manifest to be generated | no | no | no | payload_adapter | provider_route | yes | 客服 | 客服培训 | 客服话术训练数字人口播 payload，不真实生成 | 80 | 客服培训 avatar provider 备选 | needs_license_review | route_check | D-ID API terms, face/voice rights, upload/storage, cost cap | mock support script -> avatar_payload | yes | yes | yes | true |
| P1 | `quality_sprint04_omniskill_support_qa_child_locator_candidate` | OmniSkill Registry | https://omniskill.online/ | Standard Skill registry | concrete GitHub child skill required by L1 | yes_possible | possible | possible | skill_adapter_possible | openai_compatible | possible | 客服 | 客服主管 | 定位可迁移的客服 QA / ticket summary 标准 Skill 包 | 79 | 标准包来源补强，不能仅凭 registry 页面 | needs_license_review | metadata_only | specific repo/subdir/SKILL.md/LICENSE, dependency risk | metadata -> candidate card, no tool execution | no | no | possible | false |
| P1 | `quality_sprint04_openagentskills_ui_ux_pro_max_candidate` | Open Agent Skills | https://openagentskills.dev/ | Standard Skill registry | listing indicates SKILL.md package; exact repo/subdir required by L1 | yes_possible | no | possible | skill_adapter_possible | openai_compatible | no | 营销/电商 | 市场/设计 | 作为营销页面/商品页 UI 规则组件或设计审查 Skill 候选 | 79 | 组件/设计规则，避免直接当媒体生成 | needs_license_review | metadata_only | exact GitHub repo, license, whether scripts/tools exist | mock page brief -> UI rule checklist | no | no | no | false |
| P1 | `quality_sprint04_openagentskills_guizang_ppt_candidate` | Open Agent Skills / guizang-ppt-skill | https://openagentskills.dev/ | Standard Skill registry | exact repo/subdir required by L1 | yes_possible | no | possible | skill_adapter_possible | openai_compatible | possible | 销售/行政 | 销售/培训 | 销售方案/培训课件结构化 brief；不生成真实 PPT/HTML | 78 | 与 PPT/海报生成相邻，先按 metadata/mock | needs_license_review | metadata_only | exact repo, license, HTML/PPT artifact write boundary | mock sales brief -> slide_outline/spec | possible | possible | possible | true |
| P1 | `quality_sprint04_wondelai_skill_pack_locator_candidate` | wondelai/skills lead | https://github.com/wondelai/skills | Standard Skill repository lead | repo/subdir/SKILL.md list required by L1 | yes_possible | unknown | possible | skill_adapter_possible | openai_compatible | unknown | 多部门 | 运营 | 复核是否存在可迁移中小微业务 Skill 子包 | 77 | 标准 Skill 包线索，需要 L1 定位 child skill | needs_license_review | metadata_only | repo license, subdir list, commercial use, dependency risk | repo metadata -> candidate shortlist | no | no | unknown | false |
| P1 | `quality_sprint04_monday_board_health_readonly_candidate` | monday.com API | https://developer.monday.com/api-reference/docs | SaaS/API connector | monday boards/items read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 行政/销售 | 运营/销售主管 | 只读看板健康、逾期事项、负责人缺口 | 77 | 补协作项目管理渠道 | needs_license_review | read_only_mock | monday API terms, board data privacy, no item update | mock board items -> board_health | no | no | yes | true |
| P1 | `quality_sprint04_clickup_task_risk_readonly_candidate` | ClickUp API | https://clickup.com/api | SaaS/API connector | ClickUp tasks/spaces read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 行政/销售 | 运营/项目负责人 | 只读任务延期、阻塞、跨部门交接风险 | 77 | 补项目/运营工具渠道 | needs_license_review | read_only_mock | ClickUp API terms, task privacy, no write/no comment | mock tasks -> risk_summary | no | no | yes | true |
| P1 | `quality_sprint04_mailchimp_campaign_health_readonly_candidate` | Mailchimp Marketing API | https://mailchimp.com/developer/marketing/api/ | SaaS/API connector | Mailchimp campaigns/reports read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 营销 | 市场运营 | 只读活动健康、退订/打开率异常、复盘建议；不发送 | 77 | 与旧营销复盘相邻，补 Mailchimp channel adapter | needs_license_review | read_only_mock | Mailchimp API terms, audience privacy, no send/no list write | mock campaign metrics -> health_brief | no | no | yes | true |
| P1 | `quality_sprint04_brevo_email_campaign_health_readonly_candidate` | Brevo API | https://developers.brevo.com/ | SaaS/API connector | Brevo campaigns/contacts read-only adapter manifest to be generated | no | no | no | tool_adapter | model_via_deepagents | yes | 营销 | 市场运营 | 只读邮件活动表现与风险，不发送、不改联系人 | 76 | 补 Brevo channel adapter | needs_license_review | read_only_mock | Brevo API terms, contact privacy, no send/no write | mock campaign stats -> health_brief | no | no | yes | true |
| P1 | `quality_sprint04_agency_agents_zh_sales_ops_role_component_candidate` | agency-agents-zh | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | role library; no SKILL.md assumed until L1 confirms | unknown | unknown | unknown | role_component_adapter | openai_compatible | no | 销售/客服 | 销售运营/客服主管 | 中文角色模板资产，用于组合流程中的角色提示与场景测试 | 75 | role/component，不独立客户 callable | needs_license_review | role_smoke_component | repo license, role content boundary, no autonomous action | role metadata -> six-department role card | no | no | no | false |

## 80 Quality Leads

| # | candidate_id | source | type | package | use_case | recommended_state | trial_mode | risk_focus |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | Zendesk API | SaaS/API | 客服 | SLA + macro gap read-only | needs_license_review | read_only_mock | ticket privacy, no update |
| 2 | `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | Freshdesk API | SaaS/API | 客服 | ticket SLA risk read-only | needs_license_review | read_only_mock | no reply/no status write |
| 3 | `quality_sprint04_helpscout_mailbox_gap_readonly_candidate` | Help Scout API | SaaS/API | 客服 | mailbox topic and article gap | needs_license_review | read_only_mock | conversation privacy |
| 4 | `quality_sprint04_front_inbox_handoff_readonly_candidate` | Front API | SaaS/API | 客服 | shared inbox handoff summary | needs_license_review | read_only_mock | no send/no assignee write |
| 5 | `quality_sprint04_kustomer_thread_risk_readonly_candidate` | Kustomer API | SaaS/API | 客服 | customer thread risk flags | market_lead | read_only_mock | API terms and privacy |
| 6 | `quality_sprint04_livechat_transcript_quality_candidate` | LiveChat API | SaaS/API | 客服 | chat transcript quality summary | needs_license_review | read_only_mock | no message send |
| 7 | `quality_sprint04_crisp_inbox_faq_gap_candidate` | Crisp API | SaaS/API | 客服 | inbox FAQ gap | needs_license_review | read_only_mock | no outbound |
| 8 | `quality_sprint04_tidio_chat_coverage_candidate` | Tidio API | SaaS/API | 客服 | chat coverage and training notes | market_lead | read_only_mock | API availability |
| 9 | `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | Salesforce API | SaaS/API | 销售 | opportunity hygiene dry-run | needs_license_review | dry_run_only | no CRM write |
| 10 | `quality_sprint04_close_crm_pipeline_risk_readonly_candidate` | Close API | SaaS/API | 销售 | pipeline risk read-only | needs_license_review | read_only_mock | no email/call |
| 11 | `quality_sprint04_copper_crm_followup_gap_readonly_candidate` | Copper API | SaaS/API | 销售 | follow-up gap read-only | needs_license_review | read_only_mock | no task write |
| 12 | `quality_sprint04_insightly_deal_handoff_readonly_candidate` | Insightly API | SaaS/API | 销售 | deal handoff summary | market_lead | read_only_mock | CRM privacy |
| 13 | `quality_sprint04_capsule_crm_contact_health_candidate` | Capsule API | SaaS/API | 销售 | contact health summary | market_lead | read_only_mock | no contact update |
| 14 | `quality_sprint04_apollo_lead_list_quality_candidate` | Apollo API | SaaS/API | 销售 | lead list quality dry-run | needs_license_review | dry_run_only | enrichment/data terms |
| 15 | `quality_sprint04_outreach_sequence_risk_readonly_candidate` | Outreach API | SaaS/API | 销售 | sequence risk review | market_lead | read_only_mock | no send/no sequence edit |
| 16 | `quality_sprint04_salesloft_cadence_gap_readonly_candidate` | Salesloft API | SaaS/API | 销售 | cadence gap read-only | market_lead | read_only_mock | no send/no CRM write |
| 17 | `quality_sprint04_mailchimp_campaign_health_readonly_candidate` | Mailchimp API | SaaS/API | 营销 | campaign health read-only | needs_license_review | read_only_mock | audience privacy |
| 18 | `quality_sprint04_brevo_email_campaign_health_readonly_candidate` | Brevo API | SaaS/API | 营销 | email campaign health | needs_license_review | read_only_mock | no send/no contact write |
| 19 | `quality_sprint04_constantcontact_campaign_digest_candidate` | Constant Contact API | SaaS/API | 营销 | campaign digest | needs_license_review | read_only_mock | no send |
| 20 | `quality_sprint04_hootsuite_social_queue_qc_candidate` | Hootsuite API | SaaS/API | 营销 | social post queue QC | market_lead | dry_run_only | no publish |
| 21 | `quality_sprint04_buffer_social_calendar_gap_candidate` | Buffer API | SaaS/API | 营销 | social calendar gap | needs_license_review | read_only_mock | no publish |
| 22 | `quality_sprint04_sproutsocial_response_risk_candidate` | Sprout Social API | SaaS/API | 营销 | social response risk | market_lead | read_only_mock | no reply |
| 23 | `quality_sprint04_tiktok_ads_creative_readonly_candidate` | TikTok Ads API | SaaS/API | 营销 | creative performance read-only | needs_license_review | read_only_mock | no campaign write |
| 24 | `quality_sprint04_linkedin_ads_leadgen_readonly_candidate` | LinkedIn Ads API | SaaS/API | 营销 | lead gen form health | needs_license_review | read_only_mock | no ad changes |
| 25 | `quality_sprint04_shopline_catalog_qc_readonly_candidate` | Shopline API | SaaS/API | 电商/门店 | catalog QC read-only | needs_license_review | read_only_mock | no product write |
| 26 | `quality_sprint04_woocommerce_product_listing_qc_candidate` | WooCommerce REST API | SaaS/API | 电商/门店 | listing QC read-only | needs_license_review | read_only_mock | no inventory/write |
| 27 | `quality_sprint04_bigcommerce_catalog_gap_candidate` | BigCommerce API | SaaS/API | 电商/门店 | catalog gap read-only | needs_license_review | read_only_mock | no product write |
| 28 | `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | Lightspeed API | SaaS/API | 电商/门店 | POS shift anomaly | needs_license_review | read_only_mock | no refund |
| 29 | `quality_sprint04_toast_menu_sales_digest_candidate` | Toast API | SaaS/API | 电商/门店 | restaurant menu sales digest | needs_license_review | read_only_mock | no order/refund |
| 30 | `quality_sprint04_ecwid_listing_gap_candidate` | Ecwid API | SaaS/API | 电商/门店 | listing gap read-only | market_lead | read_only_mock | API terms |
| 31 | `quality_sprint04_shoplazza_catalog_qc_candidate` | Shoplazza API | SaaS/API | 电商/门店 | catalog QC read-only | market_lead | read_only_mock | no product write |
| 32 | `quality_sprint04_prestashop_order_exception_candidate` | PrestaShop API | SaaS/API | 电商/门店 | order exception read-only | needs_license_review | read_only_mock | no status write |
| 33 | `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | PostHog API | SaaS/API | 经营报表 | funnel dropoff | needs_license_review | read_only_mock | event privacy |
| 34 | `quality_sprint04_mixpanel_retention_drop_readonly_candidate` | Mixpanel API | SaaS/API | 经营报表 | retention drop read-only | needs_license_review | read_only_mock | analytics privacy |
| 35 | `quality_sprint04_amplitude_activation_gap_candidate` | Amplitude API | SaaS/API | 经营报表 | activation gap | needs_license_review | read_only_mock | event privacy |
| 36 | `quality_sprint04_plausible_traffic_anomaly_candidate` | Plausible API | SaaS/API | 经营报表 | traffic anomaly read-only | needs_license_review | read_only_mock | site analytics |
| 37 | `quality_sprint04_matomo_kpi_daily_brief_candidate` | Matomo API | SaaS/API | 经营报表 | KPI daily brief | needs_license_review | read_only_mock | privacy settings |
| 38 | `quality_sprint04_metabase_question_summary_candidate` | Metabase API | SaaS/API | 经营报表 | question/dashboard summary | needs_license_review | read_only_mock | DB exposure |
| 39 | `quality_sprint04_superset_dashboard_anomaly_candidate` | Apache Superset API | SaaS/API | 经营报表 | dashboard anomaly | needs_license_review | read_only_mock | auth/data scope |
| 40 | `quality_sprint04_grafana_alert_digest_candidate` | Grafana API | SaaS/API | 经营报表 | alert digest | needs_license_review | read_only_mock | no alert write |
| 41 | `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | Xero API | SaaS/API | 财务 | reconciliation exception | needs_license_review | read_only_mock | non-audit/non-tax |
| 42 | `quality_sprint04_freshbooks_invoice_overdue_candidate` | FreshBooks API | SaaS/API | 财务 | overdue invoice brief | needs_license_review | read_only_mock | no send/no payment |
| 43 | `quality_sprint04_wave_receipt_expense_candidate` | Wave API | SaaS/API | 财务 | expense/receipt exception | market_lead | read_only_mock | finance privacy |
| 44 | `quality_sprint04_expensify_policy_exception_candidate` | Expensify API | SaaS/API | 财务/行政 | policy exception read-only | needs_license_review | read_only_mock | no approval |
| 45 | `quality_sprint04_ramp_card_spend_anomaly_candidate` | Ramp API | SaaS/API | 财务 | spend anomaly | needs_license_review | read_only_mock | card data privacy |
| 46 | `quality_sprint04_deel_contract_renewal_readonly_candidate` | Deel API | SaaS/API | HR/行政 | contract renewal read-only | market_lead | read_only_mock | HR privacy |
| 47 | `quality_sprint04_gusto_payroll_exception_candidate` | Gusto API | SaaS/API | HR/财务 | payroll exception metadata | market_lead | metadata_only | payroll sensitive |
| 48 | `quality_sprint04_bamboohr_onboarding_gap_candidate` | BambooHR API | SaaS/API | HR | onboarding gap | needs_license_review | read_only_mock | HR privacy |
| 49 | `quality_sprint04_greenhouse_candidate_privacy_candidate` | Greenhouse API | SaaS/API | HR | candidate data privacy mask | needs_license_review | read_only_mock | recruiting privacy |
| 50 | `quality_sprint04_lever_interview_packet_candidate` | Lever API | SaaS/API | HR | interview packet summary | needs_license_review | read_only_mock | no hiring decision |
| 51 | `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | Linear API | SaaS/API | 客服/产品 | customer bug triage | needs_license_review | read_only_mock | no issue write |
| 52 | `quality_sprint04_jira_service_sla_readonly_candidate` | Jira Service Management API | SaaS/API | 客服/产品 | service desk SLA | needs_license_review | read_only_mock | no ticket write |
| 53 | `quality_sprint04_confluence_policy_gap_candidate` | Confluence API | SaaS/API | 行政/客服 | policy gap | needs_license_review | read_only_mock | no page write |
| 54 | `quality_sprint04_asana_project_risk_readonly_candidate` | Asana API | SaaS/API | 行政/销售 | project risk | needs_license_review | read_only_mock | no task write |
| 55 | `quality_sprint04_monday_board_health_readonly_candidate` | monday.com API | SaaS/API | 行政/销售 | board health | needs_license_review | read_only_mock | no item write |
| 56 | `quality_sprint04_clickup_task_risk_readonly_candidate` | ClickUp API | SaaS/API | 行政/销售 | task risk | needs_license_review | read_only_mock | no comment/write |
| 57 | `quality_sprint04_coda_doc_ops_gap_candidate` | Coda API | SaaS/API | 行政 | doc/table gap | needs_license_review | read_only_mock | no doc write |
| 58 | `quality_sprint04_dropbox_doc_classifier_candidate` | Dropbox API | SaaS/API | 行政 | file metadata classifier | needs_license_review | read_only_mock | no file move/share |
| 59 | `quality_sprint04_box_contract_folder_risk_candidate` | Box API | SaaS/API | 行政/财务 | contract folder risk | needs_license_review | read_only_mock | no file share |
| 60 | `quality_sprint04_onedrive_doc_privacy_candidate` | Microsoft Graph OneDrive | SaaS/API | 行政 | doc privacy metadata | needs_license_review | read_only_mock | no file read/write beyond scope |
| 61 | `quality_sprint04_runway_video_ad_payload_candidate` | Runway API | Media provider | 营销 | video ad payload | needs_license_review | route_check | no real generation |
| 62 | `quality_sprint04_heygen_avatar_training_payload_candidate` | HeyGen API | Media provider | HR | avatar training payload | needs_license_review | route_check | likeness/voice rights |
| 63 | `quality_sprint04_synthesia_hr_training_video_payload_candidate` | Synthesia API | Media provider | HR | training video payload | needs_license_review | route_check | no real generation |
| 64 | `quality_sprint04_recraft_brand_asset_payload_candidate` | Recraft | Media provider | 营销 | brand asset payload | needs_license_review | route_check | output rights |
| 65 | `quality_sprint04_ideogram_poster_copy_image_payload_candidate` | Ideogram | Media provider | 营销 | text poster payload | needs_license_review | route_check | text rendering/output rights |
| 66 | `quality_sprint04_pika_short_video_payload_candidate` | Pika | Media lead | 营销 | short video payload | needs_license_review | metadata_or_route_check | API availability |
| 67 | `quality_sprint04_tavus_sales_avatar_payload_candidate` | Tavus API | Media provider | 销售 | sales avatar payload | needs_license_review | route_check | consent/likeness |
| 68 | `quality_sprint04_did_avatar_support_script_payload_candidate` | D-ID API | Media provider | 客服 | support avatar payload | needs_license_review | route_check | face/voice rights |
| 69 | `quality_sprint04_luma_product_video_payload_candidate` | Luma API/product | Media provider | 电商 | product video payload | needs_license_review | route_check | API/cost/output rights |
| 70 | `quality_sprint04_leonardo_product_scene_payload_candidate` | Leonardo AI API | Media provider | 电商 | product scene payload | needs_license_review | route_check | asset upload policy |
| 71 | `quality_sprint04_cartesia_training_voice_payload_candidate` | Cartesia API | Audio provider | HR | training voice payload | needs_license_review | route_check | voice rights |
| 72 | `quality_sprint04_playht_store_announcement_payload_candidate` | PlayHT API | Audio provider | 门店 | store announcement voice | needs_license_review | route_check | voice/commercial terms |
| 73 | `quality_sprint04_omniskill_support_qa_child_locator_candidate` | OmniSkill | Standard Skill registry | 客服 | locate support QA skill | needs_license_review | metadata_only | repo/license locator |
| 74 | `quality_sprint04_openagentskills_ui_ux_pro_max_candidate` | Open Agent Skills | Standard Skill registry | 营销/电商 | UI rules component | needs_license_review | metadata_only | exact repo/license |
| 75 | `quality_sprint04_openagentskills_guizang_ppt_candidate` | Open Agent Skills | Standard Skill registry | 销售/行政 | PPT outline/spec | needs_license_review | metadata_only | artifact write boundary |
| 76 | `quality_sprint04_wondelai_skill_pack_locator_candidate` | wondelai/skills | Standard Skill repository lead | 多部门 | locate SMB child skills | needs_license_review | metadata_only | license/subdir list |
| 77 | `quality_sprint04_skillsmd_customer_success_skill_locator_candidate` | SkillsMD | Standard Skill registry | 客服/销售 | customer success skill locator | needs_license_review | metadata_only | exact repo/license |
| 78 | `quality_sprint04_openclaw_business_ops_skill_locator_candidate` | OpenClaw ecosystem | Standard Skill lead | 多部门 | business ops skill locator | market_lead | metadata_only | exact repo needed |
| 79 | `quality_sprint04_agency_agents_zh_sales_ops_role_component_candidate` | agency-agents-zh | Role library | 销售/客服 | role component | needs_license_review | role_smoke_component | role content license |
| 80 | `quality_sprint04_open_design_ad_creative_component_candidate` | open-design | Design role/template | 营销 | ad creative design component | needs_license_review | metadata_only | manifest/assets/write policy |

## Window Handoff

建议许可证窗口优先复核 P0 10 个，再处理 P1 15 个。

媒体/provider 候选复核时只允许进入 `route_check` 或 `dry_run_payload_only`，不得真实生成。SaaS/MCP/API 候选复核时只允许进入 `read_only_mock` 或 `dry_run_only`，不得连接真实账号、发送、写入、上传、退款、赔偿、扣款、改库存、改订阅、创建任务或共享文件。

