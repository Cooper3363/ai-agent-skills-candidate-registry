# QUALITY_SOURCE_SPRINT_02 许可证复核队列

更新日期: 2026-06-05

## 来源

- 研究文件: `../QUALITY_SOURCE_SPRINT_02_RESULT.md`
- 优质线索: 80
- 本队列只收 30 个优先入库候选。
- 不送 L2，不封装，不客户调用。

## 队列摘要

| 分类 | 数量 |
| --- | ---: |
| P0 | 12 |
| P1 | 18 |
| 媒体生成/编辑类 | 14 |
| MCP / API / SaaS connector 类 | 12 |
| Agent workflow / framework / component 类 | 5 |
| 中文/设计 skill pack 细分来源 | 1 |

## 30 个优先入库候选复核表

| priority | candidate_id | source_name | source_url | source_type | has_skill_md | has_skill_yaml | deepagents_fit | openai_compatible_route_fit | external_provider_dependency | business_package | six_department_role | smb_use_case | quality_score | recommended_state | trial_mode | media | real_generation | BYOK | dedupe_relation | license_review_focus | route / provider focus | test_smoke_focus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | `quality_sprint02_microsoft_excel_report_agent_candidate` | Microsoft Graph Excel | https://learn.microsoft.com/graph/api/resources/excel | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 经营/财务 | Excel 表格日报/周报、异常说明 | 87 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Sprint01 Sheets 的 Microsoft 替代 | Graph Excel 条款、Files.Read、数据隐私、禁止写文件 | read-only workbook/mock rows | mock workbook rows -> 周报和异常解释 |
| P0 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | Microsoft Graph Mail | https://learn.microsoft.com/graph/api/resources/mail-api-overview | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售/客服 | Outlook 邮件跟进摘要和草稿，不发送 | 86 | `needs_license_review` | `read_only_or_draft_only` | 否 | 否 | 是 | 新增 Microsoft 路线 | Microsoft Graph 条款、Mail.Read、邮箱隐私、禁止发送 | read-only or local draft, `send_allowed=false` | mock emails -> follow-up draft |
| P0 | `quality_sprint02_stability_product_scene_candidate` | Stability AI API | https://platform.stability.ai/docs | Image API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品场景图、主图背景、广告素材 | 85 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 product photo 来源替代 | Stability API 商用条款、模型输出权利、上传素材存储 | provider key / relay if available | 商品信息 -> 场景图 payload，不真实生成 |
| P0 | `quality_sprint02_adobe_firefly_product_ad_image_candidate` | Adobe Firefly Services | https://developer.adobe.com/firefly-services/ | Image API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 门店活动海报、商品广告图生成 payload | 84 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 媒体候选的高质量替代来源 | Firefly API 商用条款、素材上传、生成图权利、费用 | provider key / Adobe route | 活动 brief -> 图片生成 JSON，不真实生成 |
| P0 | `quality_sprint02_fal_flux_product_photo_candidate` | fal.ai FLUX routes | https://fal.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品图风格化、背景替换、场景扩展 | 84 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 fal/upscale 的新任务补充 | fal 模型路由、每个模型 license、上传图片存储 | provider key; model-specific license check | 商品图 metadata -> provider payload |
| P0 | `quality_sprint02_runway_gen4_short_ad_candidate` | Runway API | https://docs.dev.runwayml.com/ | Video API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/短视频 | 15 秒广告短视频、商品动效视频 | 84 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 视频候选补充 | Runway API 商用、素材上传、输出权利、内容政策 | provider key only; no render in L1 | 活动 brief -> video generation payload |
| P0 | `quality_sprint02_gmail_customer_email_triage_candidate` | Gmail API | https://developers.google.com/gmail/api | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服主管 | 客户邮件分类、优先级和回复草稿 | 84 | `needs_license_review` | `read_only_or_draft_only` | 否 | 否 | 是 | 与 support_ticket_classifier 部分重复，作为邮件渠道补充 | Gmail API 条款、scope、邮箱隐私、禁止发送 | read-only emails; local draft only | mock email -> triage + reply draft |
| P0 | `quality_sprint02_zoho_crm_followup_candidate` | Zoho CRM API | https://www.zoho.com/crm/developer/docs/api/ | CRM API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售代表 | Zoho CRM 线索跟进建议、下一步草稿 | 84 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | Sprint01 HubSpot 替代来源 | Zoho API 条款、CRM scope、联系人隐私、禁止写回 | `write_allowed=false` | mock leads -> next action |
| P0 | `quality_sprint02_lark_docs_meeting_action_candidate` | Lark Open Platform | https://open.larksuite.com/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 行政/销售 | 飞书文档/会议纪要转待办 dry-run | 84 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 国内协作工具补充 | Lark API 条款、文档 read-only、禁止写任务 | read-only docs; no task creation | mock meeting doc -> action list |
| P0 | `quality_sprint02_recraft_brand_banner_candidate` | Recraft API | https://www.recraft.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 品牌 banner、图标风格、海报视觉生成 | 83 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 视觉候选补充 | API 可用性、商用授权、品牌素材上传边界 | provider key / relay if available | 品牌 brief -> banner payload |
| P0 | `quality_sprint02_pipedrive_deal_next_step_candidate` | Pipedrive API | https://developers.pipedrive.com/ | CRM API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售主管 | 商机阶段摘要、风险和跟进动作 | 83 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | CRM 补充来源 | Pipedrive 条款、scope、联系人隐私、禁止写 deal | `write_allowed=false` | mock deals -> next-step report |
| P0 | `quality_sprint02_square_pos_daily_report_candidate` | Square API | https://developer.squareup.com/ | POS API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | POS 销售日报、退款异常和热销品 | 83 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 门店经营数据补强 | Square API 条款、支付数据隐私、read-only | read-only/mock POS rows | mock POS sales -> daily report |
| P1 | `quality_sprint02_ideogram_poster_text_candidate` | Ideogram API | https://ideogram.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 中文/英文促销海报文字生成与版式测试 | 82 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 海报能力补充 | API 条款、文本生成版权、中文文字可控性 | provider key / no generation | 门店优惠文案 -> 海报 prompt/payload |
| P1 | `quality_sprint02_fal_kontext_image_edit_candidate` | fal.ai Kontext image edit | https://fal.ai/ | Image edit API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品局部编辑、背景清理、文字替换建议 | 82 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 image edit 补充 | 模型 license、上传/删除策略、商品图授权 | provider key; model-specific review | mock image ref -> edit instruction payload |
| P1 | `quality_sprint02_removebg_cutout_candidate` | remove.bg API | https://www.remove.bg/api | Image edit API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品白底图、证件照/员工照去背景 | 82 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 product cleanup 的轻量替代 | API 条款、上传素材、商业白底图权利 | provider key | 图片 metadata -> cutout payload |
| P1 | `quality_sprint02_luma_dream_machine_store_video_candidate` | Luma AI API | https://lumalabs.ai/ | Video API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/短视频 | 门店氛围、产品展示短视频 | 82 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 视频来源补充 | Luma API 条款、素材授权、生成视频权利 | provider key; no render | 门店 brief -> video payload |
| P1 | `quality_sprint02_wecom_customer_group_summary_candidate` | WeCom API | https://developer.work.weixin.qq.com/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服/私域运营 | 企业微信群客户问题摘要、转人工建议 | 82 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 国内客服渠道补充 | WeCom API 条款、群消息权限、隐私、禁止发送 | read-only/mock group messages | mock group messages -> summary |
| P1 | `quality_sprint02_gorgias_ecommerce_support_candidate` | Gorgias API | https://developers.gorgias.com/ | Support API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 电商客服 | 电商售后工单摘要、退款/物流意图分类 | 82 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 电商客服来源补强 | Gorgias API 条款、scope、禁止回复 | read-only/mock tickets | mock tickets -> triage |
| P1 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | Zoho Books API | https://www.zoho.com/books/api/v3/ | Finance API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 财务/行政 | 费用分类、重复报销线索、应收提醒 | 82 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | QuickBooks/Xero 替代来源 | Zoho Books 条款、财务数据隐私、非审计声明 | read-only/mock finance rows | mock expenses -> reconcile hints |
| P1 | `quality_sprint02_google_veo_store_campaign_candidate` | Google Veo / Gemini API | https://ai.google.dev/ | Video API | no | no | payload_adapter | provider_route_possible | yes | 营销 | 市场/短视频 | 商品/门店宣传视频生成路线 | 81 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Next50 Veo 候选的外部路线补充，不重复入稳交付 | Gemini/Veo 条款、地区、商用、费用 | provider route if available | 中文 brief -> video payload |
| P1 | `quality_sprint02_heygen_training_avatar_cn_candidate` | HeyGen API | https://docs.heygen.com/ | Avatar Video API | no | no | payload_adapter | provider_route | yes | 行政/财务/HR | HR/培训 | 员工培训、制度说明、客服培训口播 | 83 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 D-ID/Synthesia 补充 | 肖像授权、声音授权、商用、内容政策 | provider key; no render | 培训脚本 -> avatar video payload |
| P1 | `quality_sprint02_haystack_faq_rag_candidate` | Haystack | https://github.com/deepset-ai/haystack | RAG framework | no | no | workflow_adapter | openai_compatible_possible | no | 客服 | 客服主管 | FAQ/RAG 引用回答的替代底层 | 81 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | stable `faq_answer_with_citations` 替代来源 | Haystack license、依赖、RAG 本地化 | no external tools | mock docs -> cited answer |
| P1 | `quality_sprint02_shopline_order_digest_candidate` | SHOPLINE Open API | https://open.shopline.io/ | Ecommerce API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | SHOPLINE 订单摘要、售后原因、商品表现 | 82 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Shopify/WooCommerce 补充来源 | SHOPLINE API 条款、订单隐私、禁止写入 | read-only/mock orders | mock orders -> ops digest |
| P1 | `quality_sprint02_feishu_bitable_ops_tracker_candidate` | Feishu Bitable API | https://open.feishu.cn/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 运营/行政 | 多门店活动/库存/客服指标跟踪摘要 | 81 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Lark/Feishu 数据源补强 | Bitable API 条款、read-only、禁止写表 | read-only/mock rows | mock rows -> ops tracker summary |
| P1 | `quality_sprint02_mailchimp_campaign_report_candidate` | Mailchimp Marketing API | https://mailchimp.com/developer/marketing/api/ | Marketing SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场运营 | 邮件营销数据摘要、下次活动建议 | 81 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 营销报表补充 | API terms、audience privacy、禁止发送 | read-only/mock stats | mock campaign stats -> report |
| P1 | `quality_sprint02_open_design_menu_poster_child_candidate` | open-design child skill lead | https://github.com/nexu-io/open-design | Open design skill pack | possible | possible | skill_adapter_possible | openai_compatible_possible | possible | 电商/门店 | 门店运营/设计 | 菜单海报、价目表、门店公告设计子 skill | 79 | `needs_license_review` | `dry_run_metadata_only` | 是 | 可能 | 可能 | Sprint01 open-design 海报候选的细分来源 | 子目录 license、是否生成/写文件、API 依赖 | child skill mapping only | 菜单 brief -> child payload |
| P1 | `quality_sprint02_autogen_sales_roleplay_candidate` | Microsoft AutoGen | https://github.com/microsoft/autogen | Agent workflow | no | no | workflow_adapter | openai_compatible_possible | no | 销售 | 销售主管 | 销售异议处理和角色扮演训练 mock | 80 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | Agent workflow 来源，不直接当 Skill | AutoGen license、依赖、工具调用边界 | no real tools | mock lead -> roleplay script/eval |
| P1 | `quality_sprint02_crewai_market_research_candidate` | CrewAI | https://github.com/crewAIInc/crewAI | Agent workflow | no | no | workflow_adapter | openai_compatible_possible | no | 销售 | 销售/市场 | 潜客/竞品调研 crew 的本地 mock 流程 | 79 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | workflow 来源，不直接当 Skill | CrewAI license、依赖、工具禁用 | no browsing/API in L1 | mock company -> research brief |
| P1 | `quality_sprint02_instructor_schema_extraction_candidate` | Instructor | https://github.com/567-labs/instructor | Structured extraction | no | no | component_adapter | openai_compatible | no | 行政/财务/HR | 行政/财务 | 合同/票据/表单结构化抽取 schema | 80 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | expense/parser 类稳定能力补充 | license、provider adapter、schema 输出 | OpenAI-compatible relay | mock text -> typed JSON |
| P1 | `quality_sprint02_promptfoo_support_regression_candidate` | promptfoo | https://github.com/promptfoo/promptfoo | Eval framework | no | no | component_adapter | openai_compatible | no | 客服 | 客服主管/平台测试 | 客服回复回归测试、禁语和引用质量测试 | 82 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | support eval 路线补强 | license、eval 数据隐私、CLI/服务边界 | no production data | 3 mock cases -> eval report |

## P0 / P1 处理建议

- P0 12 个优先做 L1：目标是快速筛出可进入 mock/dry-run smoke 的高业务价值候选。
- P1 18 个保留为高质量候选，先解决 Provider/OAuth/素材授权/框架 license/平台规则。
- 媒体类候选在 L1 前不得真实生成。
- SaaS/MCP/API connector 在 L1 前不得连接真实账号或写系统。
- Agent workflow/framework 类候选不得直接当 Skill，上游 license 通过后再抽轻量 callable workflow。

## 禁止动作

- 不真实调用 API。
- 不生成图片、视频、音频或真实文件。
- 不写 API key。
- 不写稳交付库。
- 不把 market lead 宣称为可调用 Skill。
