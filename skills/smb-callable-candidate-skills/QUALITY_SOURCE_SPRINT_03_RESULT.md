# QUALITY_SOURCE_SPRINT_03 研究结果

更新日期: 2026-06-05

## 任务边界

- 本文件为独立研究线 `QUALITY_SOURCE_SPRINT_03`，不等待 Sprint 01 L2 或 Sprint 02 L1。
- 本轮只做候选研究和许可证入队建议，不送 L2、不封装、不客户调用。
- 不调用真实 API，不生成图片/视频/音频，不写 API key，不访问真实账号，不写 CRM/店铺/邮箱/日历/财务/HR 系统。
- 稳交付库仍只认 13 个客户可调用 Skill；本文件不修改稳交付库。
- 已避开 Sprint 01/02 同名候选、Next50/To100 已落盘同名候选；能力相近时在 `dedupe_relation` 标明替代、补充或底层来源。

## 统计摘要

| 指标 | 数量 |
| --- | ---: |
| 优质线索总数 | 60 |
| 优先入库候选 | 20 |
| P0 优先候选 | 8 |
| P1 优先候选 | 12 |
| 媒体生成/编辑线索 | 14 |
| 优先入库中的媒体候选 | 6 |
| SaaS/MCP/API 线索 | 23 |
| 优先入库中的 SaaS/MCP/API 候选 | 9 |
| 标准 Skill 包/可定位 SKILL.md 线索 | 13 |
| 优先入库中的标准 Skill 包候选 | 5 |
| 中文角色库/业务模板线索 | 10 |

## 评分规则

总分 100 分：

| 维度 | 分值 |
| --- | ---: |
| 六部门业务价值 | 25 |
| 底座适配性 | 20 |
| 模型通道适配性 | 15 |
| 权限/安全可控 | 15 |
| 许可证/商用清晰 | 10 |
| 与现有 13/候选库重复度 | 10 |
| 中文中小微可用性 | 5 |

## 60 个优质线索总表

| # | candidate_id | source_name | source_url | source_type | has_skill_md | has_skill_yaml | deepagents_fit | openai_compatible_route_fit | external_provider_dependency | business_package | six_department_role | smb_use_case | quality_score | deduction_reason | dedupe_relation | recommended_state | trial_mode | license_review_focus | test_smoke_focus | 是否媒体生成 | 是否可真实生成 | 是否需要 BYOK |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint03_openagentskills_social_card_candidate` | Open Agent Skills social card skill | https://openagentskills.dev/ | Agent Skill registry | yes_possible | no | skill_adapter_possible | openai_compatible | possible | 营销 | 市场/设计 | 社媒卡片/活动封面生成规范和素材 brief | 82 | 需定位具体仓库与 SKILL.md 许可证，扣 18 | Sprint01/02 海报类补充，偏标准包 | needs_license_review | metadata_review_only | 具体 SKILL.md、license、是否调用外部图像 provider | 活动 brief -> social card spec | 是 | 可能 | 可能 |
| 2 | `quality_sprint03_openagentskills_drawio_process_candidate` | Open Agent Skills drawio skill | https://openagentskills.dev/ | Agent Skill registry | yes_possible | no | skill_adapter_possible | openai_compatible | no | 行政/财务/HR | 行政/运营 | SOP 流程图、售后流程图、培训图示 | 84 | 需定位上游仓库和输出文件边界，扣 16 | 新增标准 Skill 包方向 | needs_license_review | dry_run_metadata_only | SKILL.md、drawio 生成文件许可、是否写文件 | 售后流程 -> Mermaid/drawio spec | 否 | 否 | 否 |
| 3 | `quality_sprint03_mdskills_presentation_brief_candidate` | mdskills.ai presentation skills | https://www.mdskills.ai/ | Agent Skill marketplace | yes_possible | no | skill_adapter_possible | openai_compatible | possible | 销售 | 销售/管理 | 销售方案/培训课件 brief 到 slide spec | 81 | 需定位具体 skill 和商用许可，扣 19 | 与销售资料生成候选补充 | needs_license_review | metadata_review_only | 具体 skill、license、是否生成真实 PPT | 销售方案 -> slide outline | 否 | 可能 | 可能 |
| 4 | `quality_sprint03_mdskills_file_processing_excel_candidate` | mdskills.ai spreadsheet/file skills | https://www.mdskills.ai/ | Agent Skill marketplace | yes_possible | no | skill_adapter_possible | openai_compatible | possible | 经营报表 | 经营/财务 | 表格清洗、指标口径检查、周报结构化 | 83 | 需定位子 skill 和依赖，扣 17 | 稳交付报表类补充来源 | needs_license_review | metadata_review_only | SKILL.md、license、文件读取权限 | mock rows -> clean/report spec | 否 | 否 | 可能 |
| 5 | `quality_sprint03_skillsmd_shopify_ops_skill_candidate` | SkillsMD Shopify skill lead | https://skillsmd.dev/ | Agent Skill registry | yes_possible | possible | skill_adapter_possible | openai_compatible | possible | 电商/门店 | 电商运营 | Shopify 商品/订单运营 skill 子项定位 | 80 | 需定位真实仓库和 API 权限，扣 20 | Sprint01 Shopify MCP 的标准包补充 | needs_license_review | metadata_review_only | 具体 repo、license、OAuth/write 边界 | mock order -> skill IO spec | 否 | 否 | 可能 |
| 6 | `quality_sprint03_skillsmd_google_ads_report_skill_candidate` | SkillsMD Google Ads skill lead | https://skillsmd.dev/ | Agent Skill registry | yes_possible | possible | skill_adapter_possible | openai_compatible | yes | 营销 | 市场运营 | 广告账户报表摘要和优化建议，不改投放 | 79 | 需定位子目录、广告 API 条款，扣 21 | Sprint01 Google Ads report 补充 | needs_license_review | metadata_review_only | SKILL.md、Google Ads API 条款、禁止改投放 | mock ads stats -> insight spec | 否 | 否 | 是 |
| 7 | `quality_sprint03_omniskill_customer_support_skill_candidate` | OmniSkill support skill lead | https://omniskill.online/ | Agent Skill marketplace | yes_possible | possible | skill_adapter_possible | openai_compatible | possible | 客服 | 客服主管 | 客服工单摘要/质检标准包线索 | 78 | 需定位具体上游，不能直接当可调用，扣 22 | 客服质检来源补充 | needs_license_review | metadata_review_only | 具体 skill package、license、输入输出 | mock ticket -> support skill spec | 否 | 否 | 可能 |
| 8 | `quality_sprint03_omniskill_finance_invoice_skill_candidate` | OmniSkill invoice/admin skill lead | https://omniskill.online/ | Agent Skill marketplace | yes_possible | possible | skill_adapter_possible | openai_compatible | possible | 行政/财务/HR | 财务/行政 | 发票/费用/报销字段抽取标准包线索 | 77 | 与稳交付票据类重复较多，扣 23 | `expense_invoice_parser` 替代来源 | needs_license_review | metadata_review_only | SKILL.md、license、财务结论边界 | mock invoice text -> schema spec | 否 | 否 | 可能 |
| 9 | `quality_sprint03_vercel_agent_skills_data_report_candidate` | vercel-labs/skills | https://github.com/vercel-labs/skills | Agent Skill repository | yes | no | skill_adapter_possible | openai_compatible | possible | 经营报表 | 运营/管理 | 从标准 SKILL.md 模板抽数据报告 skill 规范 | 82 | 需确认具体子 skill 是否面向业务，扣 18 | 标准 SKILL.md 来源补强 | needs_license_review | metadata_review_only | repo license、子 skill、依赖 | mock metrics -> skill trigger/spec | 否 | 否 | 可能 |
| 10 | `quality_sprint03_deepagents_customer_ops_example_candidate` | DeepAgents examples | https://github.com/langchain-ai/deepagents | DeepAgents workflow/examples | possible | no | native_like | openai_compatible | no | 客服 | 客服主管 | 客服处理 workflow 的本地可迁移样例 | 83 | 需定位 examples 和 license，扣 17 | 本地底座适配性强 | needs_license_review | mock_only | license、示例依赖、工具调用边界 | mock support case -> agent plan | 否 | 否 | 否 |
| 11 | `quality_sprint03_deepagents_research_report_example_candidate` | DeepAgents research examples | https://github.com/langchain-ai/deepagents | DeepAgents workflow/examples | possible | no | native_like | openai_compatible | no | 销售 | 销售/市场 | 潜客/竞品 research report workflow，本地 mock | 82 | 外部搜索需禁用或替换为用户给定资料，扣 18 | lead research 补充 | needs_license_review | mock_only | license、工具禁用、外部搜索边界 | mock company docs -> research brief | 否 | 否 | 否 |
| 12 | `quality_sprint03_hermes_meeting_minutes_skill_lead_candidate` | Hermes meeting minutes skill lead | https://github.com/ | Hermes-like skill lead | possible | possible | skill_adapter_possible | openai_compatible | unknown | 行政/财务/HR | 行政/销售 | 会议纪要转待办标准包线索 | 74 | 需要真实上游/manifest，扣 26 | 会议纪要类能力补充 | market_lead | metadata_review_only | 真实 repo、manifest、license | transcript -> action schema spec | 否 | 否 | 可能 |
| 13 | `quality_sprint03_openclow_contract_review_skill_lead_candidate` | OpenClow/OpenClaw contract skill lead | https://github.com/ | OpenClaw-like skill lead | possible | possible | skill_adapter_possible | openai_compatible | unknown | 行政/财务/HR | 行政/销售 | 合同条款摘要/风险提示标准包线索 | 75 | 需定位真实子 skill，法律边界需控，扣 25 | 合同候选补充 | market_lead | metadata_review_only | 上游子目录、license、非法律意见声明 | mock contract -> risk flags spec | 否 | 否 | 可能 |
| 14 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | Shopify product catalog API/MCP | https://shopify.dev/docs/api | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | 商品目录只读审查：标题、属性、缺图、库存提示 | 86 | OAuth scope、商品数据隐私扣 14 | Sprint01 order ops 的细分只读补充 | needs_license_review | read_only_mock | Shopify read-only catalog scope、禁止写商品 | mock products -> catalog review | 否 | 否 | 是 |
| 15 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | Stripe API | https://docs.stripe.com/api | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 经营/财务 | 订阅/收款健康度、失败支付摘要，不处理付款 | 84 | 支付数据敏感，非财务/审计结论，扣 16 | Sprint01 Stripe invoice 补充 | needs_license_review | read_only_mock | Stripe API 条款、read-only、PCI/隐私边界 | mock charges/subscriptions -> health summary | 否 | 否 | 是 |
| 16 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | Airtable API | https://airtable.com/developers/web/api/introduction | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | Airtable 库存/活动表异常摘要，只读 | 83 | 表格隐私和写入边界扣 17 | Sprint01 Airtable ops 细分 | needs_license_review | read_only_mock | Airtable API terms、read-only base scope | mock base rows -> inventory alerts | 否 | 否 | 是 |
| 17 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | Google Drive API | https://developers.google.com/drive/api | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 行政 | 文档分类、制度/合同/票据归档建议，不移动文件 | 82 | 文件隐私和写入边界扣 18 | 行政文档补充 | needs_license_review | read_only_mock | Drive read-only scope、文件隐私、禁止移动/删除 | mock file metadata -> classify | 否 | 否 | 是 |
| 18 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | HubSpot CRM API | https://developers.hubspot.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售主管 | 联系人资料完整度、跟进风险、下一步建议 | 82 | 与 Sprint01 HubSpot followup 相近但更偏数据健康，扣 18 | Sprint01 HubSpot 能力补充 | needs_license_review | dry_run_only | HubSpot API scope、禁止写联系人 | mock contacts -> data health report | 否 | 否 | 是 |
| 19 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | Slack API | https://api.slack.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服主管 | 从支持频道摘要 FAQ 缺口，不发消息 | 83 | 频道隐私和发送边界扣 17 | Sprint01 Slack triage 细分 | needs_license_review | read_only_mock | Slack history scope、隐私、禁止发送 | mock channel messages -> FAQ gaps | 否 | 否 | 是 |
| 20 | `quality_sprint03_mcp_notion_policy_gap_candidate` | Notion API | https://developers.notion.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服/行政 | 知识库政策缺口、冲突和过期提醒 | 84 | Notion 页面权限和隐私扣 16 | Sprint01 Notion 知识库细分 | needs_license_review | read_only_mock | Notion API terms、read-only pages | mock docs -> gap/conflict report | 否 | 否 | 是 |
| 21 | `quality_sprint03_mcp_google_merchant_feed_qc_candidate` | Google Merchant API | https://developers.google.com/shopping-content | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | 商品 feed 缺字段、标题/图片/价格风险检查 | 81 | 商户数据敏感、平台规则需核扣 19 | Merchant feed 候选细分 | needs_license_review | read_only_mock | API terms、商品数据隐私、禁止改 feed | mock feed rows -> QC report | 否 | 否 | 是 |
| 22 | `quality_sprint03_mcp_meta_ads_creative_fatigue_candidate` | Meta Marketing API | https://developers.facebook.com/docs/marketing-apis/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场运营 | 广告素材疲劳和换素材建议，不改广告 | 80 | 广告 API 条款、隐私和投放边界扣 20 | Sprint01 Meta Ads report 细分 | needs_license_review | read_only_mock | Marketing API terms、禁止改投放 | mock ad stats -> fatigue report | 否 | 否 | 是 |
| 23 | `quality_sprint03_mcp_klaviyo_campaign_retention_candidate` | Klaviyo API | https://developers.klaviyo.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场运营 | 会员留存/邮件活动摘要，不发送 | 80 | 联系人隐私和发送禁用需核扣 20 | Mailchimp/Brevo 补充 | needs_license_review | read_only_mock | API terms、audience privacy、禁止发送 | mock campaign metrics -> retention brief | 否 | 否 | 是 |
| 24 | `quality_sprint03_mcp_intercom_article_gap_candidate` | Intercom API | https://developers.intercom.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服主管 | 工单问题到帮助中心文章缺口 | 80 | 客户隐私、写文章边界扣 20 | Intercom 摘要的知识库补充 | needs_license_review | read_only_mock | API terms、conversation privacy、no article write | mock tickets/articles -> gap list | 否 | 否 | 是 |
| 25 | `quality_sprint03_mcp_zendesk_macro_gap_candidate` | Zendesk API | https://developer.zendesk.com/api-reference/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服主管 | 宏回复覆盖率、模板缺口和培训建议 | 80 | Zendesk scope、客户隐私扣 20 | Zendesk triage 补充 | needs_license_review | read_only_mock | API terms、ticket/macro read-only | mock tickets/macros -> gap report | 否 | 否 | 是 |
| 26 | `quality_sprint03_mcp_tally_form_lead_router_candidate` | Tally forms | https://tally.so/ | SaaS/API connector | no | no | tool_adapter_possible | n/a_model_via_deepagents | yes | 销售 | 销售/客服 | 表单线索路由、意图分类、跟进建议 | 76 | API/开放性需核，扣 24 | Typeform/Forms 补充 | needs_license_review | mock_rows_only | API availability、data privacy | mock form entries -> lead route | 否 | 否 | 可能 |
| 27 | `quality_sprint03_mcp_jotform_intake_summary_candidate` | Jotform API | https://api.jotform.com/docs/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售/行政 | 客户申请/售后表单摘要与分派 | 78 | 表单隐私、写入边界扣 22 | 表单来源补充 | needs_license_review | read_only_mock | API terms、form data privacy | mock submissions -> triage | 否 | 否 | 是 |
| 28 | `quality_sprint03_mcp_xero_ar_followup_candidate` | Xero API | https://developer.xero.com/documentation/api/accounting/overview | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 财务 | 应收账款提醒建议，不发送、不做审计 | 82 | 财务敏感、非审计声明扣 18 | Sprint01 Xero 补充 | needs_license_review | read_only_mock | API terms、read-only、非审计税务 | mock invoices -> AR followup plan | 否 | 否 | 是 |
| 29 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | QuickBooks API | https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 财务/管理 | 现金流风险提示、费用趋势，不给税务结论 | 82 | 财务数据敏感、地区规则差异扣 18 | QuickBooks 摘要补充 | needs_license_review | read_only_mock | API terms、privacy、非税务/审计 | mock accounts -> cashflow warning | 否 | 否 | 是 |
| 30 | `quality_sprint03_mcp_square_menu_margin_candidate` | Square Catalog/Orders API | https://developer.squareup.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | 菜单/商品毛利提醒和热销组合建议 | 81 | 支付/订单数据敏感扣 19 | Sprint02 Square 日报细分 | needs_license_review | read_only_mock | API terms、read-only catalog/orders | mock catalog/orders -> margin hints | 否 | 否 | 是 |
| 31 | `quality_sprint03_mcp_clover_pos_shift_report_candidate` | Clover API | https://docs.clover.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | 门店班次销售、退款和异常摘要 | 79 | 地区和支付数据边界需核扣 21 | POS 来源补充 | needs_license_review | read_only_mock | API terms、payments data privacy | mock shift sales -> report | 否 | 否 | 是 |
| 32 | `quality_sprint03_mcp_square_appointment_noshow_candidate` | Square Appointments API | https://developer.squareup.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | 预约未到店风险、排班提醒，不改预约 | 78 | 预约/客户隐私扣 22 | 门店服务业补充 | needs_license_review | read_only_mock | API terms、customer privacy、no booking write | mock appointments -> no-show risk | 否 | 否 | 是 |
| 33 | `quality_sprint03_openai_image_product_variant_candidate` | OpenAI Images API | https://platform.openai.com/docs/guides/images | Image API | no | no | payload_adapter | native_openai_route | yes | 电商/门店 | 电商运营 | 商品图变体、背景替换 prompt/payload | 86 | 需确认中转站 image route 和素材权利扣 14 | Next50 OpenAI image 路线细分 | needs_license_review | dry_run_payload_only | Images API 条款、素材上传、商用输出 | product brief -> image payload | 是 | 是 | 是 |
| 34 | `quality_sprint03_openai_image_poster_layout_candidate` | OpenAI Images API | https://platform.openai.com/docs/guides/images | Image API | no | no | payload_adapter | native_openai_route | yes | 营销 | 市场/设计 | 门店海报/优惠券视觉 prompt/payload | 85 | 需确认中转站、中文字渲染与素材授权扣 15 | OpenAI image 路线细分 | needs_license_review | dry_run_payload_only | image route、商用、上传素材 | campaign brief -> poster payload | 是 | 是 | 是 |
| 35 | `quality_sprint03_openai_tts_training_microcourse_candidate` | OpenAI Audio/TTS route | https://platform.openai.com/docs/guides/text-to-speech | Audio API | no | no | payload_adapter | native_openai_route | yes | 行政/财务/HR | HR/培训 | SOP/制度培训音频脚本和 TTS payload | 82 | 音色授权和真实生成需禁用到 L1 后扣 18 | Sprint01 TTS 培训补充 | needs_license_review | dry_run_payload_only | TTS 条款、声音权利、内容政策 | training text -> TTS payload | 是 | 是 | 是 |
| 36 | `quality_sprint03_elevenlabs_customer_service_voice_candidate` | ElevenLabs API | https://elevenlabs.io/docs | Audio/voice API | no | no | payload_adapter | provider_route | yes | 客服 | 客服主管 | 客服培训话术语音、质检示例音频 payload | 80 | 声音授权和费用风险扣 20 | Sprint01 voiceover 补充 | needs_license_review | dry_run_payload_only | voice license、cloning 禁用、商用 | script -> voice payload | 是 | 是 | 是 |
| 37 | `quality_sprint03_descript_video_edit_brief_candidate` | Descript API/product lead | https://www.descript.com/ | Video edit provider | no | no | payload_adapter_possible | provider_route_possible | yes | 营销 | 短视频运营 | 口播视频剪辑、字幕、片段 brief | 73 | API 开放性不清，扣 27 | media market lead | market_lead | metadata_review_only | API availability、commercial terms | script/transcript -> edit brief | 是 | 可能 | 可能 |
| 38 | `quality_sprint03_speechmatics_transcription_cn_candidate` | Speechmatics API | https://www.speechmatics.com/ | Speech API | no | no | payload_adapter | provider_route | yes | 行政/财务/HR | 行政/销售 | 会议/培训音频转写和摘要 payload | 78 | 中文效果/费用/上传隐私需核扣 22 | Whisper 路线替代 | needs_license_review | dry_run_payload_only | API terms、audio upload privacy、中文 | audio metadata -> transcript request payload | 是 | 是 | 是 |
| 39 | `quality_sprint03_assemblyai_meeting_summary_candidate` | AssemblyAI API | https://www.assemblyai.com/docs | Speech API | no | no | payload_adapter | provider_route | yes | 销售 | 销售/行政 | 销售会议转写、摘要、待办 payload | 79 | 音频隐私、费用和中文支持扣 21 | 转写候选补充 | needs_license_review | dry_run_payload_only | API terms、audio privacy、language support | audio metadata -> summary payload | 是 | 是 | 是 |
| 40 | `quality_sprint03_murf_voiceover_ad_candidate` | Murf AI API/provider | https://murf.ai/ | Voice provider | no | no | payload_adapter_possible | provider_route_possible | yes | 营销 | 市场/短视频 | 广告配音/培训配音 payload | 74 | API 开放性和声音商用需核扣 26 | voice market lead | market_lead | metadata_review_only | API availability、voice license | script -> voice plan | 是 | 是 | 是 |
| 41 | `quality_sprint03_elai_training_avatar_candidate` | Elai.io API/provider | https://elai.io/ | Avatar video provider | no | no | payload_adapter_possible | provider_route_possible | yes | 行政/财务/HR | HR/培训 | 培训数字人视频 payload | 75 | API/人物授权/商用需核扣 25 | avatar 补充 | needs_license_review | dry_run_payload_only | API terms、avatar/voice rights | training script -> avatar payload | 是 | 是 | 是 |
| 42 | `quality_sprint03_deepbrain_ai_avatar_candidate` | DeepBrain AI | https://www.deepbrain.io/ | Avatar video provider | no | no | payload_adapter_possible | provider_route_possible | yes | 营销 | 市场/培训 | 数字人口播广告/培训 payload | 73 | API 可用性和授权需核扣 27 | avatar market lead | market_lead | metadata_review_only | API availability、rights、content policy | script -> avatar plan | 是 | 是 | 是 |
| 43 | `quality_sprint03_sora_storyboard_payload_candidate` | OpenAI video/Sora route lead | https://openai.com/sora | Video provider lead | no | no | payload_adapter_possible | native_route_possible | yes | 营销 | 市场/短视频 | 短视频 storyboard 到 video payload 预案 | 76 | API/中转站可用性和条款不确定扣 24 | 视频路线观察 | market_lead | metadata_review_only | API availability、commercial terms、safety | storyboard -> payload spec | 是 | 可能 | 是 |
| 44 | `quality_sprint03_canva_connect_brand_kit_qc_candidate` | Canva Connect APIs | https://www.canva.dev/docs/ | Design SaaS/API | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场/设计 | 品牌套件一致性检查，不导出、不写设计 | 81 | OAuth/设计素材隐私扣 19 | Sprint02 Canva export 的低风险细分 | needs_license_review | read_only_mock | Canva API terms、read-only、no export | mock brand kit -> QC report | 是 | 否 | 是 |
| 45 | `quality_sprint03_figma_component_usage_qc_candidate` | Figma API | https://www.figma.com/developers/api | Design SaaS/API | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场/设计 | Banner/海报组件使用一致性检查 | 80 | 设计文件隐私和 read-only scope 扣 20 | Sprint01 Figma brand QC 细分 | needs_license_review | read_only_mock | Figma API terms、read-only file scope | mock frame JSON -> component QC | 是 | 否 | 是 |
| 46 | `quality_sprint03_agency_after_sales_specialist_role_candidate` | agency-agents-zh 售后角色 | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 客服 | 售后客服 | 退换货/投诉处理话术和升级建议 | 76 | 角色非 Skill，需模板化，扣 24 | support role 补充 | needs_license_review | role_smoke_mock | license、平台规则、非自动回复 | mock complaint -> handling plan | 否 | 否 | 否 |
| 47 | `quality_sprint03_agency_store_manager_role_candidate` | agency-agents-zh 门店店长角色 | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 电商/门店 | 门店店长 | 门店晨会、库存、排班、活动检查清单 | 77 | 角色非 callable，需稳定 IO，扣 23 | 门店模板补充 | needs_license_review | role_smoke_mock | license、角色授权、任务边界 | mock store day -> checklist | 否 | 否 | 否 |
| 48 | `quality_sprint03_agency_procurement_role_candidate` | agency-agents-zh 采购角色 | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 行政/财务/HR | 采购/行政 | 采购需求清单、供应商对比、报价问题 | 76 | 角色非 Skill，采购决策边界需控扣 24 | 采购候选补充 | needs_license_review | role_smoke_mock | license、非自动下单、报价隐私 | mock purchase need -> RFQ checklist | 否 | 否 | 否 |
| 49 | `quality_sprint03_agency_livecommerce_host_role_candidate` | agency-agents-zh 直播主播角色 | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 营销 | 直播/短视频 | 直播脚本、互动话术、商品卖点 | 75 | 平台规则和角色模板化扣 25 | 直播脚本补充 | needs_license_review | role_smoke_mock | license、平台发布规则、禁词 | mock product -> live script | 否 | 否 | 否 |
| 50 | `quality_sprint03_agency_hr_interviewer_role_candidate` | agency-agents-zh 面试官角色 | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 行政/财务/HR | HR | 面试问题、候选人评分建议，禁止自动录用 | 76 | HR 决策边界和角色模板化扣 24 | HR 候选补充 | needs_license_review | role_smoke_mock | license、反歧视、非自动录用 | mock JD/resume -> interview questions | 否 | 否 | 否 |
| 51 | `quality_sprint03_open_design_store_price_tag_child_candidate` | open-design price tag child lead | https://github.com/nexu-io/open-design | Open design skill pack | possible | possible | skill_adapter_possible | openai_compatible_possible | possible | 电商/门店 | 门店运营/设计 | 价签、菜单牌、货架标签子 skill 定位 | 78 | 需定位子 skill、license、生成/写文件边界扣 22 | open-design 菜单海报补充 | needs_license_review | dry_run_metadata_only | 子目录 license、API/文件写入 | mock menu -> price tag payload | 是 | 可能 | 可能 |
| 52 | `quality_sprint03_open_design_coupon_banner_child_candidate` | open-design coupon/banner child lead | https://github.com/nexu-io/open-design | Open design skill pack | possible | possible | skill_adapter_possible | openai_compatible_possible | possible | 营销 | 市场/设计 | 优惠券/banner 设计子 skill 定位 | 78 | 子 skill 未定位，扣 22 | open-design 视觉补充 | needs_license_review | dry_run_metadata_only | 子 skill、license、API 权限 | campaign -> coupon/banner spec | 是 | 可能 | 可能 |
| 53 | `quality_sprint03_xiaohongshu_note_review_template_candidate` | 小红书笔记业务模板 | https://www.xiaohongshu.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 营销 | 新媒体运营 | 小红书笔记标题/封面建议和风险词检查 | 73 | 平台规则、来源非开源、重复度扣 27 | 作为模板线索，不直接 Skill | market_lead | mock_only | 平台规则、版权、禁止发布 | product brief -> note outline | 否 | 否 | 否 |
| 54 | `quality_sprint03_douyin_shop_after_sales_template_candidate` | 抖店售后模板线索 | https://fxg.jinritemai.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 客服 | 电商客服 | 抖店售后原因归类和回复草稿 | 72 | 平台权限/规则不清，扣 28 | 电商客服模板补充 | market_lead | mock_only | 平台规则、禁止真实回复 | mock after-sales text -> category/draft | 否 | 否 | 否 |
| 55 | `quality_sprint03_pinduoduo_product_title_template_candidate` | 拼多多商品标题模板线索 | https://www.pinduoduo.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 电商/门店 | 电商运营 | 商品标题合规和卖点改写模板 | 71 | 非开放来源、平台规则需核扣 29 | 商品标题模板补充 | market_lead | mock_only | 平台规则、商标/夸大用语 | mock product -> title variants | 否 | 否 | 否 |
| 56 | `quality_sprint03_meituan_store_menu_template_candidate` | 美团门店菜单模板线索 | https://www.meituan.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 电商/门店 | 门店店长 | 菜品描述、菜单分类、促销套餐建议 | 72 | 平台规则/非开放来源扣 28 | 门店菜单补充 | market_lead | mock_only | 平台规则、禁止发布/改价 | mock menu -> copy/checklist | 否 | 否 | 否 |
| 57 | `quality_sprint03_dianping_review_response_template_candidate` | 大众点评回复模板线索 | https://www.dianping.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 客服 | 门店客服 | 差评回复草稿、升级和补偿建议 | 73 | 平台规则、禁止自动回复，扣 27 | 客服回复补充 | market_lead | mock_only | 平台规则、禁止真实发布 | mock review -> reply draft | 否 | 否 | 否 |
| 58 | `quality_sprint03_tiktok_shop_listing_qc_candidate` | TikTok Shop API | https://partner.tiktokshop.com/docv2 | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 跨境电商运营 | 商品 listing 只读质量检查和风险提示 | 80 | API 条款、地区和商品数据隐私扣 20 | Google Merchant/Shopify 补充 | needs_license_review | read_only_mock | TikTok Shop API terms、read-only scope | mock listing -> QC report | 否 | 否 | 是 |
| 59 | `quality_sprint03_amazon_spapi_listing_gap_candidate` | Amazon Selling Partner API | https://developer-docs.amazon.com/sp-api/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 跨境电商运营 | 亚马逊 listing 缺口、库存/价格风险摘要 | 79 | API 审批复杂、地区和隐私扣 21 | 跨境电商高价值但复杂 | needs_license_review | read_only_mock | SP-API terms、read-only、no listing write | mock listing/orders -> gap report | 否 | 否 | 是 |
| 60 | `quality_sprint03_etsy_listing_seo_candidate` | Etsy API | https://developers.etsy.com/documentation/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 小店/手作电商 | Etsy 商品标题、标签、描述 SEO 检查 | 78 | 市场相对细分、API 条款需核扣 22 | 商品 SEO 来源补充 | needs_license_review | read_only_mock | Etsy API terms、shop/listing privacy | mock listing -> SEO suggestions | 否 | 否 | 是 |

## 20 个优先入库候选

| priority | candidate_id | quality_score | business_package | source_type | recommended_state | trial_mode | media | real_generation | BYOK | 主要理由 |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | 86 | 电商/门店 | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 商品目录只读审查高频，输入输出清楚，写入风险低 |
| P0 | `quality_sprint03_openai_image_product_variant_candidate` | 86 | 电商/门店 | Image API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 商品图变体是中小微高价值媒体场景，OpenAI route 适配强 |
| P0 | `quality_sprint03_openai_image_poster_layout_candidate` | 85 | 营销 | Image API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 门店海报和优惠券视觉适配中小微营销 |
| P0 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | 84 | 经营报表 | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 收款/订阅健康度价值高，read-only 可控 |
| P0 | `quality_sprint03_openagentskills_drawio_process_candidate` | 84 | 行政/财务/HR | Agent Skill registry | `needs_license_review` | `dry_run_metadata_only` | 否 | 否 | 否 | 标准 Skill 包潜力强，SOP/售后流程图高频 |
| P0 | `quality_sprint03_mcp_notion_policy_gap_candidate` | 84 | 客服 | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 知识库政策缺口和冲突检查能补强客服包 |
| P0 | `quality_sprint03_deepagents_customer_ops_example_candidate` | 83 | 客服 | DeepAgents workflow/examples | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 与本地底座适配强，适合抽客服 workflow |
| P0 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | 83 | 电商/门店 | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 库存/活动表只读异常摘要，中小微落地快 |
| P1 | `quality_sprint03_mdskills_file_processing_excel_candidate` | 83 | 经营报表 | Agent Skill marketplace | `needs_license_review` | `metadata_review_only` | 否 | 否 | 可能 | 标准 Skill 包来源，表格清洗和报表场景强 |
| P1 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | 83 | 客服 | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 支持频道到 FAQ 缺口，read-only 可控 |
| P1 | `quality_sprint03_deepagents_research_report_example_candidate` | 82 | 销售 | DeepAgents workflow/examples | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 潜客/竞品 research workflow 可迁移，但禁外部抓取 |
| P1 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | 82 | 行政/财务/HR | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 文档分类和归档建议高频，禁止移动/删除即可控 |
| P1 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | 82 | 销售 | SaaS/API connector | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | 联系人资料完整度和跟进风险是 CRM 轻量场景 |
| P1 | `quality_sprint03_mcp_xero_ar_followup_candidate` | 82 | 行政/财务/HR | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 应收账款提醒建议高价值，但需非审计声明 |
| P1 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | 82 | 经营报表 | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 现金流风险提示适合经营报表包，需财务边界 |
| P1 | `quality_sprint03_openagentskills_social_card_candidate` | 82 | 营销 | Agent Skill registry | `needs_license_review` | `metadata_review_only` | 是 | 可能 | 可能 | 标准 Skill 包方向，适合社媒活动视觉 |
| P1 | `quality_sprint03_vercel_agent_skills_data_report_candidate` | 82 | 经营报表 | Agent Skill repository | `needs_license_review` | `metadata_review_only` | 否 | 否 | 可能 | 已有 SKILL.md 仓库，可作为标准包研究样本 |
| P1 | `quality_sprint03_openai_tts_training_microcourse_candidate` | 82 | 行政/财务/HR | Audio API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 培训音频/制度说明价值高，payload smoke 可控 |
| P1 | `quality_sprint03_canva_connect_brand_kit_qc_candidate` | 81 | 营销 | Design SaaS/API | `needs_license_review` | `read_only_mock` | 是 | 否 | 是 | 品牌一致性检查低风险，read-only 设计 JSON 即可 |
| P1 | `quality_sprint03_mcp_google_merchant_feed_qc_candidate` | 81 | 电商/门店 | SaaS/API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 商品 feed QC 适合电商运营，禁止改 feed |

## P0 清单

1. `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate`
2. `quality_sprint03_openai_image_product_variant_candidate`
3. `quality_sprint03_openai_image_poster_layout_candidate`
4. `quality_sprint03_mcp_stripe_subscription_health_candidate`
5. `quality_sprint03_openagentskills_drawio_process_candidate`
6. `quality_sprint03_mcp_notion_policy_gap_candidate`
7. `quality_sprint03_deepagents_customer_ops_example_candidate`
8. `quality_sprint03_mcp_airtable_inventory_ops_candidate`

## P1 清单

1. `quality_sprint03_mdskills_file_processing_excel_candidate`
2. `quality_sprint03_mcp_slack_channel_faq_gap_candidate`
3. `quality_sprint03_deepagents_research_report_example_candidate`
4. `quality_sprint03_mcp_google_drive_doc_classifier_candidate`
5. `quality_sprint03_mcp_hubspot_contact_health_candidate`
6. `quality_sprint03_mcp_xero_ar_followup_candidate`
7. `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate`
8. `quality_sprint03_openagentskills_social_card_candidate`
9. `quality_sprint03_vercel_agent_skills_data_report_candidate`
10. `quality_sprint03_openai_tts_training_microcourse_candidate`
11. `quality_sprint03_canva_connect_brand_kit_qc_candidate`
12. `quality_sprint03_mcp_google_merchant_feed_qc_candidate`

## 许可证窗口建议

- 优先核 P0 8 个；重点看 API/OAuth scope、read-only 边界、Provider 生成物商用权、素材上传/存储、BYOK 是否必需。
- 标准 Skill 包候选先核“是否已有真实 SKILL.md / skill.yaml / manifest、具体子目录、LICENSE 文件、是否调用外部 API、是否写文件”。
- SaaS/MCP/API 候选 L1 前只允许 mock/read-only/dry-run，不允许连接真实账号，不允许写入、发送、上传或发布。
- 媒体类候选 L1 前只允许 `dry_run_payload_only`，不允许真实生成图片、音频或视频。
- 中文角色库/业务模板不得直接宣称为标准 Skill；必须先模板化为稳定输入输出。
