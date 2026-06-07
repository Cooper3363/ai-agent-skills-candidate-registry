# QUALITY_SOURCE_SPRINT_02 研究结果

更新日期: 2026-06-05

## 任务边界

- 本文件为独立研究线 `QUALITY_SOURCE_SPRINT_02`，不等待 Sprint 01 L1 结果。
- 本轮只做候选研究与入队建议，不送 L2、不封装、不客户调用。
- 不调用真实 API，不生成图片/视频/音频，不写 API key，不上传素材，不写 CRM/店铺/日历/任务/财务/HR 系统。
- 稳交付库仍只认 13 个客户可调用 Skill；本文件不修改稳交付库。
- 已避开 Sprint 01 同名候选、Next50 / To100 已落盘候选的同名候选；如能力相近，在 `dedupe_relation` 标为替代/补充来源。

## 统计摘要

| 指标 | 数量 |
| --- | ---: |
| 优质线索总数 | 80 |
| 优先入库候选 | 30 |
| P0 优先候选 | 12 |
| P1 优先候选 | 18 |
| 媒体生成/编辑线索 | 24 |
| 优先入库中的媒体候选 | 14 |
| MCP / API / SaaS 连接器线索 | 31 |
| 优先入库中的 MCP / API / SaaS 候选 | 13 |
| Agent Skill / workflow / prompt framework 线索 | 18 |
| 中文角色库/业务模板线索 | 7 |

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

## 80 个优质线索总表

| # | candidate_id | source_name | source_url | source_type | has_skill_md | has_skill_yaml | deepagents_fit | openai_compatible_route_fit | external_provider_dependency | business_package | six_department_role | smb_use_case | quality_score | deduction_reason | dedupe_relation | recommended_state | trial_mode | license_review_focus | test_smoke_focus | 是否媒体生成 | 是否可真实生成 | 是否需要 BYOK |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint02_adobe_firefly_product_ad_image_candidate` | Adobe Firefly Services | https://developer.adobe.com/firefly-services/ | Image API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 门店活动海报、商品广告图生成 payload | 84 | 依赖 Adobe 条款、素材授权和付费 Provider，扣 16 | Sprint01 媒体候选的高质量替代来源 | needs_license_review | dry_run_payload_only | Firefly API 商用条款、素材上传、生成图权利、费用 | 活动 brief -> 图片生成 JSON，不真实生成 | 是 | 是 | 是 |
| 2 | `quality_sprint02_recraft_brand_banner_candidate` | Recraft API | https://www.recraft.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 品牌 banner、图标风格、海报视觉生成 | 83 | API/商用条款需复核，中文字体稳定性待测，扣 17 | Sprint01 视觉候选补充 | needs_license_review | dry_run_payload_only | API 可用性、商用授权、品牌素材上传边界 | 品牌 brief -> banner payload | 是 | 是 | 是 |
| 3 | `quality_sprint02_ideogram_poster_text_candidate` | Ideogram API | https://ideogram.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 中文/英文促销海报文字生成与版式测试 | 82 | 官方 API/商业使用和中文排版需确认，扣 18 | Sprint01 海报能力补充 | needs_license_review | dry_run_payload_only | API 条款、文本生成版权、中文文字可控性 | 门店优惠文案 -> 海报 prompt/payload | 是 | 是 | 是 |
| 4 | `quality_sprint02_stability_product_scene_candidate` | Stability AI API | https://platform.stability.ai/docs | Image API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品场景图、主图背景、广告素材 | 85 | Provider 费用、模型条款、图片上传授权扣 15 | Sprint01 product photo 来源替代 | needs_license_review | dry_run_payload_only | Stability API 商用条款、模型输出权利、上传素材 | 商品信息 -> 场景图 payload | 是 | 是 | 是 |
| 5 | `quality_sprint02_fal_flux_product_photo_candidate` | fal.ai FLUX routes | https://fal.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品图风格化、背景替换、场景扩展 | 84 | 多模型路由许可证差异和费用需核，扣 16 | Sprint01 fal/upscale 的新任务补充 | needs_license_review | dry_run_payload_only | fal 模型路由、每个模型 license、上传图片存储 | 商品图 metadata -> provider payload | 是 | 是 | 是 |
| 6 | `quality_sprint02_fal_kontext_image_edit_candidate` | fal.ai Kontext image edit | https://fal.ai/ | Image edit API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品局部编辑、背景清理、文字替换建议 | 82 | 具体模型许可、上传素材留存和编辑稳定性扣 18 | Sprint01 image edit 补充 | needs_license_review | dry_run_payload_only | 模型 license、上传/删除策略、商品图授权 | mock image ref -> edit instruction payload | 是 | 是 | 是 |
| 7 | `quality_sprint02_bria_product_background_candidate` | BRIA AI API | https://bria.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 合规商品背景、商用视觉素材生成 | 81 | 商用与训练数据声明需复核，中文资料较少扣 19 | 新增媒体来源 | needs_license_review | dry_run_payload_only | BRIA 条款、生成图权利、素材上传 | 商品 SKU -> 背景生成 payload | 是 | 是 | 是 |
| 8 | `quality_sprint02_clipdrop_cleanup_upscale_candidate` | Clipdrop API | https://clipdrop.co/apis | Image edit API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品图清理、去背景、放大 | 80 | Provider 条款和功能边界需复核，扣 20 | 与 removebg/PhotoRoom 能力重叠 | needs_license_review | dry_run_payload_only | API 商用、图片上传、功能水印/费用 | 商品图 metadata -> cleanup payload | 是 | 是 | 是 |
| 9 | `quality_sprint02_removebg_cutout_candidate` | remove.bg API | https://www.remove.bg/api | Image edit API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品白底图、证件照/员工照去背景 | 82 | 单点功能，依赖上传和付费额度，扣 18 | Sprint01 product cleanup 的轻量替代 | needs_license_review | dry_run_payload_only | API 条款、上传素材、商业白底图权利 | 图片 metadata -> cutout payload | 是 | 是 | 是 |
| 10 | `quality_sprint02_pixelcut_bulk_product_photo_candidate` | Pixelcut API | https://www.pixelcut.ai/ | Image edit API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 批量商品图优化、背景/阴影 | 78 | API 文档和商用边界需深核，扣 22 | 媒体补充来源 | needs_license_review | dry_run_payload_only | API 是否开放、素材上传、费用 | SKU 列表 -> 批量图像任务 payload | 是 | 是 | 是 |
| 11 | `quality_sprint02_pebblely_lifestyle_photo_candidate` | Pebblely | https://pebblely.com/ | Image API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 小商品生活方式场景图 | 79 | API/条款需复核，中小微价值高但依赖强，扣 21 | 新增商品图来源 | needs_license_review | dry_run_payload_only | API 可用性、商用图权利、上传素材 | 商品描述 -> lifestyle photo payload | 是 | 是 | 是 |
| 12 | `quality_sprint02_leonardo_product_scene_candidate` | Leonardo AI API | https://docs.leonardo.ai/ | Image API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/设计 | 活动素材、商品场景图、广告视觉 | 77 | 商用条款、模型权限、中文 prompt 需测，扣 23 | 媒体补充来源 | needs_license_review | dry_run_payload_only | API license、输出权利、品牌素材上传 | brief -> creative payload | 是 | 是 | 是 |
| 13 | `quality_sprint02_runway_gen4_short_ad_candidate` | Runway API | https://docs.dev.runwayml.com/ | Video API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/短视频 | 15 秒广告短视频、商品动效视频 | 84 | 费用、素材授权、内容政策和中文口播需核，扣 16 | Sprint01 视频候选补充 | needs_license_review | dry_run_payload_only | API 商用、素材上传、输出权利、内容政策 | 活动 brief -> video generation payload | 是 | 是 | 是 |
| 14 | `quality_sprint02_luma_dream_machine_store_video_candidate` | Luma AI API | https://lumalabs.ai/ | Video API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/短视频 | 门店氛围、产品展示短视频 | 82 | API 可用性、商用条款和费用需核，扣 18 | Sprint01 视频来源补充 | needs_license_review | dry_run_payload_only | Luma API 条款、素材授权、生成视频权利 | 门店 brief -> video payload | 是 | 是 | 是 |
| 15 | `quality_sprint02_google_veo_store_campaign_candidate` | Google Veo / Gemini API | https://ai.google.dev/ | Video API | no | no | payload_adapter | provider_route_possible | yes | 营销 | 市场/短视频 | 商品/门店宣传视频生成路线 | 81 | 可用地区、商用和 Provider route 不确定，扣 19 | Next50 Veo 候选的外部路线补充，不重复入稳交付 | needs_license_review | dry_run_payload_only | Gemini/Veo 条款、地区、商用、费用 | 中文 brief -> video payload | 是 | 是 | 是 |
| 16 | `quality_sprint02_pika_product_clip_candidate` | Pika | https://pika.art/ | Video provider | no | no | payload_adapter | provider_route_possible | yes | 营销 | 市场/短视频 | 商品图转短视频、活动短片 | 75 | API 开放性和商用边界不清，扣 25 | market lead，非优先 | market_lead | dry_run_payload_only | 是否有正式 API、商用条款、费用 | prompt -> provider plan | 是 | 是 | 是 |
| 17 | `quality_sprint02_heygen_training_avatar_cn_candidate` | HeyGen API | https://docs.heygen.com/ | Avatar Video API | no | no | payload_adapter | provider_route | yes | 行政/财务/HR | HR/培训 | 员工培训、制度说明、客服培训口播 | 83 | 真人肖像/声音授权和费用需核，扣 17 | Sprint01 D-ID/Synthesia 补充 | needs_license_review | dry_run_payload_only | 肖像授权、声音授权、商用、内容政策 | 培训脚本 -> avatar video payload | 是 | 是 | 是 |
| 18 | `quality_sprint02_synthesia_sop_avatar_candidate` | Synthesia API | https://www.synthesia.io/ | Avatar Video API | no | no | payload_adapter | provider_route | yes | 行政/财务/HR | HR/行政 | SOP/制度口播视频 | 81 | API/商用条款、中文声音和人物授权需核，扣 19 | Sprint01 avatar 候选补充 | needs_license_review | dry_run_payload_only | API 条款、avatar 授权、内容政策 | SOP text -> avatar payload | 是 | 是 | 是 |
| 19 | `quality_sprint02_tavus_sales_avatar_candidate` | Tavus API | https://docs.tavus.io/ | Avatar Video API | no | no | payload_adapter | provider_route | yes | 销售 | 销售代表 | 个性化销售介绍视频 dry-run | 79 | 真人授权和销售发送边界风险，扣 21 | 新增 avatar 销售来源 | needs_license_review | dry_run_payload_only | 肖像/声音授权、发送限制、商用 | lead brief -> avatar payload，不发送 | 是 | 是 | 是 |
| 20 | `quality_sprint02_colossyan_training_video_candidate` | Colossyan | https://www.colossyan.com/ | Avatar Video provider | no | no | payload_adapter | provider_route_possible | yes | 行政/财务/HR | HR/培训 | 新员工培训微课视频 | 76 | API 细节和商用需核，扣 24 | media market lead | market_lead | dry_run_payload_only | API 是否开放、商用、人物授权 | training outline -> video plan | 是 | 是 | 是 |
| 21 | `quality_sprint02_akool_avatar_local_ad_candidate` | AKOOL API | https://akool.com/ | Avatar / media API | no | no | payload_adapter | provider_route | yes | 营销 | 市场/短视频 | 本地门店促销口播、数字人广告 | 77 | 条款、肖像、声音与广告合规需核，扣 23 | 新增 avatar 来源 | needs_license_review | dry_run_payload_only | API 条款、素材授权、广告合规 | 活动脚本 -> avatar payload | 是 | 是 | 是 |
| 22 | `quality_sprint02_capcut_commerce_template_candidate` | CapCut Commerce Pro | https://www.capcut.com/ | Video/design SaaS | no | no | payload_adapter | provider_route_possible | yes | 电商/门店 | 电商运营 | 电商短视频模板、商品素材组合 | 74 | API/开放性不清，平台条款需核，扣 26 | market lead，不作 L1 优先 | market_lead | dry_run_metadata_only | API 是否开放、模板权利、素材上传 | 商品 brief -> template plan | 是 | 是 | 是 |
| 23 | `quality_sprint02_cloudinary_media_transform_candidate` | Cloudinary APIs | https://cloudinary.com/documentation | Media API | no | no | payload_adapter | provider_route | yes | 电商/门店 | 电商运营 | 商品图裁剪、压缩、格式转换、基础增强 | 80 | 偏工具型，生成能力有限，扣 20 | 可作为媒体底层组件 | needs_license_review | dry_run_payload_only | API 条款、上传素材、存储和 CDN 权限 | image metadata -> transform payload | 是 | 部分 | 是 |
| 24 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | Microsoft Graph Mail | https://learn.microsoft.com/graph/api/resources/mail-api-overview | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售/客服 | Outlook 邮件跟进摘要和草稿，不发送 | 86 | OAuth scope、邮箱隐私和发送边界扣 14 | 新增 Microsoft 路线 | needs_license_review | read_only_or_draft_only | Microsoft Graph 条款、Mail.Read、禁止发送边界 | mock emails -> follow-up draft | 否 | 否 | 是 |
| 25 | `quality_sprint02_microsoft_excel_report_agent_candidate` | Microsoft Graph Excel | https://learn.microsoft.com/graph/api/resources/excel | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 经营/财务 | Excel 表格日报/周报、异常说明 | 87 | OAuth scope、文件隐私和写回边界扣 13 | Sprint01 Sheets 的 Microsoft 替代 | needs_license_review | read_only_mock | Graph Excel 条款、Files.Read、数据隐私 | mock workbook rows -> 周报 | 否 | 否 | 是 |
| 26 | `quality_sprint02_google_calendar_staff_schedule_candidate` | Google Calendar API | https://developers.google.com/calendar/api | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 行政/门店店长 | 员工排班、活动日程冲突检查 | 81 | OAuth scope 和写日历风险扣 19 | 新增日程连接器 | needs_license_review | read_only_mock | Calendar API 条款、read-only scope、禁止写入 | mock events -> conflict summary | 否 | 否 | 是 |
| 27 | `quality_sprint02_gmail_customer_email_triage_candidate` | Gmail API | https://developers.google.com/gmail/api | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服主管 | 客户邮件分类、优先级和回复草稿 | 84 | 邮箱隐私、发送边界、Google scope 扣 16 | 与 support_ticket_classifier 部分重复，作为邮件渠道补充 | needs_license_review | read_only_or_draft_only | Gmail API 条款、scope、禁止发送 | mock email -> triage + draft | 否 | 否 | 是 |
| 28 | `quality_sprint02_zoho_crm_followup_candidate` | Zoho CRM API | https://www.zoho.com/crm/developer/docs/api/ | CRM API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售代表 | Zoho CRM 线索跟进建议、下一步草稿 | 84 | OAuth scope、CRM 写入边界扣 16 | Sprint01 HubSpot 替代来源 | needs_license_review | dry_run_only | Zoho API 条款、CRM scope、禁止写回 | mock leads -> next action | 否 | 否 | 是 |
| 29 | `quality_sprint02_pipedrive_deal_next_step_candidate` | Pipedrive API | https://developers.pipedrive.com/ | CRM API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售主管 | 商机阶段摘要、风险和跟进动作 | 83 | OAuth、联系人隐私、写入风险扣 17 | CRM 补充来源 | needs_license_review | dry_run_only | Pipedrive 条款、scope、禁止写 deal | mock deals -> next-step report | 否 | 否 | 是 |
| 30 | `quality_sprint02_salesforce_starter_summary_candidate` | Salesforce REST API | https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/ | CRM API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售运营 | 小团队 Salesforce 商机摘要和异常提醒 | 78 | 企业级复杂度偏高，scope 风险扣 22 | 只作大型 CRM 线索，不优先 | needs_license_review | dry_run_only | API 条款、scope、客户数据隐私 | mock opportunities -> summary | 否 | 否 | 是 |
| 31 | `quality_sprint02_lark_docs_meeting_action_candidate` | Lark Open Platform | https://open.larksuite.com/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 行政/销售 | 飞书文档/会议纪要转待办 dry-run | 84 | 文档权限和写任务边界扣 16 | 国内协作工具补充 | needs_license_review | read_only_mock | Lark API 条款、文档 read-only、禁止写任务 | mock meeting doc -> action list | 否 | 否 | 是 |
| 32 | `quality_sprint02_dingtalk_notice_task_candidate` | DingTalk Open Platform | https://open.dingtalk.com/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 行政主管 | 钉钉通知草稿、任务拆解，不发送 | 80 | 中文平台权限与发送边界需核，扣 20 | 国内协作工具补充 | needs_license_review | dry_run_only | DingTalk 条款、消息发送禁用、OAuth | mock notice -> task draft | 否 | 否 | 是 |
| 33 | `quality_sprint02_wecom_customer_group_summary_candidate` | WeCom API | https://developer.work.weixin.qq.com/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服/私域运营 | 企业微信群客户问题摘要、转人工建议 | 82 | 群聊隐私、发送和合规边界扣 18 | 国内客服渠道补充 | needs_license_review | read_only_mock | WeCom API 条款、群消息权限、隐私 | mock group messages -> summary | 否 | 否 | 是 |
| 34 | `quality_sprint02_asana_task_status_report_candidate` | Asana API | https://developers.asana.com/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 运营/行政 | 项目任务周报、延期风险摘要 | 79 | 偏协作工具，需控制写入权限扣 21 | 与 Trello/ClickUp 类似，补充来源 | needs_license_review | read_only_mock | Asana 条款、read-only scope、任务隐私 | mock tasks -> weekly status | 否 | 否 | 是 |
| 35 | `quality_sprint02_monday_ops_risk_candidate` | monday.com API | https://developer.monday.com/api-reference/docs | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 运营主管 | 运营看板风险、逾期任务和负责人摘要 | 78 | 平台复杂度、scope 风险扣 22 | 协作工具补充来源 | needs_license_review | read_only_mock | monday API 条款、read-only board scope | mock board -> risk summary | 否 | 否 | 是 |
| 36 | `quality_sprint02_clickup_ops_task_brief_candidate` | ClickUp API | https://clickup.com/api | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 运营/行政 | 任务列表摘要、逾期提醒、会议跟进 | 79 | 与 To50 任务类能力部分重叠扣 21 | 已有会议/待办候选的连接器补充 | needs_license_review | read_only_mock | ClickUp API 条款、scope、禁止写任务 | mock tasks -> action brief | 否 | 否 | 是 |
| 37 | `quality_sprint02_jira_service_ticket_classifier_candidate` | Atlassian Jira REST API | https://developer.atlassian.com/cloud/jira/platform/rest/v3/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服/技术支持 | Jira 工单分类、升级和 SLA 风险 | 78 | 中小微普及度一般、权限复杂扣 22 | support_ticket_classifier 的渠道扩展 | needs_license_review | read_only_mock | Atlassian 条款、工单隐私、禁止写入 | mock issues -> category/SLA | 否 | 否 | 是 |
| 38 | `quality_sprint02_gorgias_ecommerce_support_candidate` | Gorgias API | https://developers.gorgias.com/ | Support API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 电商客服 | 电商售后工单摘要、退款/物流意图分类 | 82 | 客户隐私和回复发送边界扣 18 | 电商客服来源补强 | needs_license_review | read_only_mock | Gorgias API 条款、scope、禁止回复 | mock tickets -> triage | 否 | 否 | 是 |
| 39 | `quality_sprint02_helpscout_mailbox_summary_candidate` | Help Scout API | https://developer.helpscout.com/ | Support API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服主管 | 邮箱客服批量摘要、培训案例抽取 | 81 | 邮箱隐私、回复写入边界扣 19 | Zendesk/Freshdesk 替代来源 | needs_license_review | read_only_mock | Help Scout 条款、mailbox scope、禁止发送 | mock conversations -> summary | 否 | 否 | 是 |
| 40 | `quality_sprint02_crisp_livechat_summary_candidate` | Crisp API | https://docs.crisp.chat/ | Support API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 在线客服 | 在线咨询摘要、满意度风险、转人工 | 79 | 平台条款和写消息边界需核扣 21 | 客服渠道补充 | needs_license_review | read_only_mock | Crisp API 条款、消息读取、禁止发送 | mock chat -> escalation summary | 否 | 否 | 是 |
| 41 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | Zoho Books API | https://www.zoho.com/books/api/v3/ | Finance API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 财务/行政 | 费用分类、重复报销线索、应收提醒 | 82 | 财务数据敏感，不能做审计/税务结论扣 18 | QuickBooks/Xero 替代来源 | needs_license_review | read_only_mock | Zoho Books 条款、财务数据隐私、非审计声明 | mock expenses -> reconcile hints | 否 | 否 | 是 |
| 42 | `quality_sprint02_wave_receipt_expense_candidate` | Wave API / Apps | https://www.waveapps.com/ | Finance SaaS | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 财务/行政 | 小微费用和收款摘要 | 74 | API 开放性和地区适配不清扣 26 | market lead | market_lead | mock_only | API 是否开放、商用和数据条款 | mock transactions -> summary | 否 | 否 | 是 |
| 43 | `quality_sprint02_odoo_invoice_inventory_candidate` | Odoo API | https://www.odoo.com/documentation/ | ERP API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 店长/财务 | 订单、库存、发票摘要和异常提示 | 81 | ERP 配置复杂，版本差异扣 19 | 订单/库存候选补充 | needs_license_review | read_only_mock | Odoo license/API、权限、禁止写单据 | mock records -> exception summary | 否 | 否 | 是 |
| 44 | `quality_sprint02_square_pos_daily_report_candidate` | Square API | https://developer.squareup.com/ | POS API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | POS 销售日报、退款异常和热销品 | 83 | 地区、支付数据、scope 风险扣 17 | 门店经营数据补强 | needs_license_review | read_only_mock | Square API 条款、支付数据隐私、read-only | mock POS sales -> daily report | 否 | 否 | 是 |
| 45 | `quality_sprint02_lightspeed_inventory_alert_candidate` | Lightspeed API | https://developers.lightspeedhq.com/ | Retail API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | 零售库存预警、滞销品和缺货提醒 | 79 | 地区和平台适配度有限扣 21 | 库存候选补充 | needs_license_review | read_only_mock | API 条款、库存数据隐私、禁止写库存 | mock inventory -> alert | 否 | 否 | 是 |
| 46 | `quality_sprint02_shopline_order_digest_candidate` | SHOPLINE Open API | https://open.shopline.io/ | Ecommerce API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | SHOPLINE 订单摘要、售后原因、商品表现 | 82 | 平台条款、地区和写入边界扣 18 | Shopify/WooCommerce 补充来源 | needs_license_review | read_only_mock | SHOPLINE API 条款、订单隐私、禁止写入 | mock orders -> ops digest | 否 | 否 | 是 |
| 47 | `quality_sprint02_bigcommerce_listing_review_candidate` | BigCommerce API | https://developer.bigcommerce.com/ | Ecommerce API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | 商品标题/描述/图片字段优化建议 | 80 | 平台普及度和 scope 风险扣 20 | 商品 listing 候选补充 | needs_license_review | read_only_mock | BigCommerce 条款、catalog scope、禁止写商品 | mock products -> listing review | 否 | 否 | 是 |
| 48 | `quality_sprint02_magento_order_snapshot_candidate` | Adobe Commerce / Magento APIs | https://developer.adobe.com/commerce/webapi/rest/ | Ecommerce API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | 订单异常、库存和退款趋势摘要 | 76 | 系统复杂、部署成本高扣 24 | 只作中大型电商线索 | market_lead | read_only_mock | API/license、版本、权限 | mock orders -> snapshot | 否 | 否 | 是 |
| 49 | `quality_sprint02_autogen_sales_roleplay_candidate` | Microsoft AutoGen | https://github.com/microsoft/autogen | Agent workflow | no | no | workflow_adapter | openai_compatible_possible | no | 销售 | 销售主管 | 销售异议处理和角色扮演训练 mock | 80 | 框架偏重、需抽轻量 workflow 扣 20 | Agent workflow 来源，不直接当 Skill | needs_license_review | mock_only | AutoGen license、依赖、工具调用边界 | mock lead -> roleplay script/eval | 否 | 否 | 否 |
| 50 | `quality_sprint02_crewai_market_research_candidate` | CrewAI | https://github.com/crewAIInc/crewAI | Agent workflow | no | no | workflow_adapter | openai_compatible_possible | no | 销售 | 销售/市场 | 潜客/竞品调研 crew 的本地 mock 流程 | 79 | 框架化较重，license/商业版本需核扣 21 | workflow 来源，不直接当 Skill | needs_license_review | mock_only | CrewAI license、依赖、工具禁用 | mock company -> research brief | 否 | 否 | 否 |
| 51 | `quality_sprint02_semantic_kernel_policy_agent_candidate` | Semantic Kernel | https://github.com/microsoft/semantic-kernel | Agent workflow | no | no | workflow_adapter | openai_compatible_possible | no | 行政/财务/HR | HR/行政 | 制度问答、流程路由、结构化输出 | 80 | 框架需拆为轻量 callable skill 扣 20 | workflow 来源 | needs_license_review | mock_only | Semantic Kernel license、provider adapter | mock policy -> answer + route | 否 | 否 | 否 |
| 52 | `quality_sprint02_haystack_faq_rag_candidate` | Haystack | https://github.com/deepset-ai/haystack | RAG framework | no | no | workflow_adapter | openai_compatible_possible | no | 客服 | 客服主管 | FAQ/RAG 引用回答的替代底层 | 81 | 与稳交付 FAQ 部分重复，只作替代来源扣 19 | stable `faq_answer_with_citations` 替代来源 | needs_license_review | mock_only | Haystack license、依赖、RAG 本地化 | mock docs -> cited answer | 否 | 否 | 否 |
| 53 | `quality_sprint02_guardrailsai_output_policy_candidate` | Guardrails AI | https://github.com/guardrails-ai/guardrails | Output guardrail | no | no | component_adapter | openai_compatible | no | 客服 | 客服/合规 | 客服回复格式、禁语和风险输出校验 | 79 | 更像底层组件，独立业务价值有限扣 21 | stable guardrail 类能力补充 | component_only | mock_only | license、validators 许可、依赖 | mock reply -> validation report | 否 | 否 | 否 |
| 54 | `quality_sprint02_instructor_schema_extraction_candidate` | Instructor | https://github.com/567-labs/instructor | Structured extraction | no | no | component_adapter | openai_compatible | no | 行政/财务/HR | 行政/财务 | 合同/票据/表单结构化抽取 schema | 80 | 组件型，需业务模板包裹扣 20 | expense/parser 类稳定能力补充 | needs_license_review | mock_only | license、provider adapter、schema 输出 | mock text -> typed JSON | 否 | 否 | 否 |
| 55 | `quality_sprint02_dspy_prompt_optimization_candidate` | DSPy | https://github.com/stanfordnlp/dspy | Prompt optimization framework | no | no | component_adapter | openai_compatible_possible | no | 经营报表 | 运营/平台内部 | 优化客服/营销 prompt 的离线实验 | 72 | 偏研发，不是 SMB 直接 Skill 扣 28 | 组件/内部工具 | component_only | mock_only | license、评测数据隐私 | prompt examples -> optimizer plan | 否 | 否 | 否 |
| 56 | `quality_sprint02_promptfoo_support_regression_candidate` | promptfoo | https://github.com/promptfoo/promptfoo | Eval framework | no | no | component_adapter | openai_compatible | no | 客服 | 客服主管/平台测试 | 客服回复回归测试、禁语和引用质量测试 | 82 | 偏测试组件，需封装为质检 Skill 扣 18 | support eval 路线补强 | needs_license_review | mock_only | license、eval 数据隐私、CLI/服务边界 | 3 mock cases -> eval report | 否 | 否 | 否 |
| 57 | `quality_sprint02_langfuse_prompt_trace_candidate` | Langfuse | https://github.com/langfuse/langfuse | Observability | no | no | component_adapter | openai_compatible | no | 经营报表 | 平台运营 | Skill 调用质量和成本观测 | 74 | 平台内部组件，非 SMB 直接场景扣 26 | component only | component_only | mock_metadata_only | license、云服务/自部署条款、数据隐私 | mock trace -> cost report | 否 | 否 | 否 |
| 58 | `quality_sprint02_open_agent_skills_email_child_candidate` | Open Agent Skills registry | https://github.com/ | Agent Skill registry lead | possible | possible | skill_adapter_possible | openai_compatible_possible | unknown | 销售 | 销售代表 | 邮件草稿/跟进类 Agent Skill 子项定位 | 77 | 需定位具体上游子目录和许可证扣 23 | Sprint01 registry lead 的具体方向补充 | needs_license_review | metadata_review_only | 具体 SKILL.md/skill.yaml、license、输入输出 | mock lead -> email skill spec | 否 | 否 | 视实现 |
| 59 | `quality_sprint02_skillsmd_support_child_candidate` | SkillsMD support skill lead | https://skillsmd.ai/ | Agent Skill registry lead | possible | possible | skill_adapter_possible | openai_compatible_possible | unknown | 客服 | 客服主管 | 客服知识库/转人工 Skill 子项定位 | 76 | 来源需复核，可能只是目录线索扣 24 | Sprint01 SkillsMD lead 延伸 | needs_license_review | metadata_review_only | 具体技能包、license、是否可商用 | mock support case -> spec mapping | 否 | 否 | 视实现 |
| 60 | `quality_sprint02_mdskills_finance_admin_child_candidate` | mdskills.ai finance/admin lead | https://mdskills.ai/ | Agent Skill registry lead | possible | possible | skill_adapter_possible | openai_compatible_possible | unknown | 行政/财务/HR | 财务/行政 | 财务报销/行政文档 Skill 子项定位 | 75 | 需要具体上游和许可证扣 25 | Sprint01 mdskills lead 延伸 | needs_license_review | metadata_review_only | 具体技能包、license、权限 | mock invoice text -> spec mapping | 否 | 否 | 视实现 |
| 61 | `quality_sprint02_openclaw_design_banner_child_candidate` | OpenClaw-like design skill lead | https://github.com/ | OpenClaw-like skill pack lead | possible | possible | skill_adapter_possible | openai_compatible_possible | unknown | 营销 | 市场/设计 | 海报/banner 子 skill 定位和迁移 | 76 | 需要具体仓库/manifest，不能直接客户调用扣 24 | OpenClaw 来源补充 | needs_license_review | metadata_review_only | 具体子目录、license、是否写文件/API | campaign brief -> child skill map | 是 | 可能 | 视实现 |
| 62 | `quality_sprint02_hermes_crm_followup_skill_candidate` | Hermes/爱马仕 CRM skill lead | https://github.com/ | Hermes-like skill lead | possible | possible | skill_adapter_possible | openai_compatible_possible | unknown | 销售 | 销售代表 | CRM 跟进/客户画像子 skill 定位 | 75 | 需要真实上游和许可证扣 25 | Hermes 来源补充 | needs_license_review | metadata_review_only | 具体 manifest、license、权限 | mock CRM note -> skill IO spec | 否 | 否 | 视实现 |
| 63 | `quality_sprint02_omniskill_store_ops_child_candidate` | OmniSkill store ops lead | https://github.com/ | Agent Skill registry lead | possible | possible | skill_adapter_possible | openai_compatible_possible | unknown | 电商/门店 | 门店店长 | 门店运营/库存/活动子 skill 定位 | 74 | 来源线索未具体化扣 26 | Sprint01 OmniSkill lead 延伸 | market_lead | metadata_review_only | 真实仓库、license、可调用格式 | mock store issue -> child skill spec | 否 | 否 | 视实现 |
| 64 | `quality_sprint02_open_design_menu_poster_child_candidate` | open-design child skill lead | https://github.com/nexu-io/open-design | Open design skill pack | possible | possible | skill_adapter_possible | openai_compatible_possible | possible | 电商/门店 | 门店运营/设计 | 菜单海报、价目表、门店公告设计子 skill | 79 | 需定位子 skill、外部 API 和 license 扣 21 | Sprint01 open-design 海报候选的细分来源 | needs_license_review | dry_run_metadata_only | 子目录 license、是否生成/写文件、API 依赖 | 菜单 brief -> child payload | 是 | 可能 | 可能 |
| 65 | `quality_sprint02_open_design_product_detail_banner_candidate` | open-design product detail lead | https://github.com/nexu-io/open-design | Open design skill pack | possible | possible | skill_adapter_possible | openai_compatible_possible | possible | 电商/门店 | 电商运营 | 商品详情页 banner/主图规范 | 78 | 与商品图能力重叠，需定位子项扣 22 | open-design 细分来源 | needs_license_review | dry_run_metadata_only | 子 skill、license、API/文件写入 | product info -> banner spec | 是 | 可能 | 可能 |
| 66 | `quality_sprint02_agency_wechat_private_ops_role_candidate` | agency-agents-zh private traffic role | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 客服 | 私域/客服 | 企业微信/微信群运营话术和风险提醒 | 76 | 角色库非 callable Skill，需要模板化扣 24 | agency role 补充，不重复稳交付 | needs_license_review | role_smoke_mock | MIT/上游 license、角色内容授权 | mock group issue -> reply plan | 否 | 否 | 否 |
| 67 | `quality_sprint02_agency_tmall_store_ops_role_candidate` | agency-agents-zh ecommerce role | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 电商/门店 | 电商运营 | 天猫/淘宝店铺运营日常检查清单 | 75 | 角色非 Skill，平台规则风险需补扣 25 | agency role 补充 | needs_license_review | role_smoke_mock | license、平台规则、非自动发布 | mock shop status -> ops checklist | 否 | 否 | 否 |
| 68 | `quality_sprint02_agency_customer_success_trainer_candidate` | agency-agents-zh customer success role | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 客服 | 客服主管 | 客服培训案例、话术评分和改进建议 | 77 | 与客服质检类重叠，角色需模板化扣 23 | support quality 路线补充 | needs_license_review | role_smoke_mock | license、角色授权、质检非惩戒声明 | mock dialogue -> coaching plan | 否 | 否 | 否 |
| 69 | `quality_sprint02_agency_finance_admin_assistant_candidate` | agency-agents-zh finance/admin role | https://github.com/jnMetaCode/agency-agents-zh | Chinese role library | no | no | prompt_role_adapter | openai_compatible | no | 行政/财务/HR | 行政/财务 | 报销材料检查、制度问答、提醒草稿 | 76 | 角色非 Skill，财务结论边界需控扣 24 | expense/parser 稳交付补充 | needs_license_review | role_smoke_mock | license、非税务/审计结论、隐私 | mock reimbursement -> checklist | 否 | 否 | 否 |
| 70 | `quality_sprint02_douyin_live_script_template_candidate` | Douyin live commerce template lead | https://www.douyin.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 营销 | 直播/门店运营 | 直播带货脚本、互动话术、风险词提醒 | 73 | 平台规则和来源开放性不清扣 27 | 与短视频脚本候选部分重叠 | market_lead | mock_only | 平台规则、来源授权、禁止自动发布 | mock product -> live script | 否 | 否 | 否 |
| 71 | `quality_sprint02_wechat_official_account_editor_candidate` | WeChat official account editor template | https://mp.weixin.qq.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 营销 | 新媒体运营 | 公众号文章选题、摘要和改写 | 74 | 平台规则和发布边界扣 26 | marketing copy 稳交付补充 | market_lead | mock_only | 平台规则、版权、禁止发布 | brief -> article outline | 否 | 否 | 否 |
| 72 | `quality_sprint02_kuaishou_shop_video_script_candidate` | Kuaishou shop script template | https://www.kuaishou.com/ | Chinese business template | no | no | prompt_template_adapter | openai_compatible | no | 营销 | 短视频运营 | 快手小店短视频脚本和标题 | 72 | 平台规则、来源不开放、重复度较高扣 28 | 短视频脚本补充 | market_lead | mock_only | 平台规则、禁止发布、素材版权 | product -> script/title | 否 | 否 | 否 |
| 73 | `quality_sprint02_feishu_bitable_ops_tracker_candidate` | Feishu Bitable API | https://open.feishu.cn/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 运营/行政 | 多门店活动/库存/客服指标跟踪摘要 | 81 | 权限和表格隐私需核扣 19 | Lark/Feishu 数据源补强 | needs_license_review | read_only_mock | Bitable API 条款、read-only、禁止写表 | mock rows -> ops tracker summary | 否 | 否 | 是 |
| 74 | `quality_sprint02_wps_doc_template_admin_candidate` | WPS / Kingsoft office template lead | https://open.wps.cn/ | Office SaaS / template lead | no | no | tool_adapter_possible | n/a_model_via_deepagents | possible | 行政/财务/HR | 行政 | 通知、制度、会议纪要模板生成/检查 | 72 | API/开放性、商用和国内账号权限需核扣 28 | 行政文档 market lead | market_lead | mock_only | API 是否开放、模板版权、账号权限 | mock notice -> doc outline | 否 | 否 | 可能 |
| 75 | `quality_sprint02_docuseal_contract_form_candidate` | DocuSeal | https://github.com/docusealco/docuseal | Document workflow | no | no | tool_adapter | n/a_model_via_deepagents | no | 行政/财务/HR | 行政/销售 | 合同/表单签署前字段检查，不发起签署 | 78 | 完整产品，需只取字段检查/模板线索扣 22 | 合同/表单候选补充 | needs_license_review | mock_form_only | license、签署动作禁用、文件隐私 | mock contract form -> missing fields | 否 | 否 | 否 |
| 76 | `quality_sprint02_formbricks_feedback_analysis_candidate` | Formbricks | https://github.com/formbricks/formbricks | Survey tool / API | no | no | tool_adapter | n/a_model_via_deepagents | optional | 客服 | 客服/运营 | 客户反馈表单摘要、差评主题聚类 | 80 | 完整产品，需作为数据源/组件扣 20 | survey analysis 候选补充 | needs_license_review | mock_rows_only | license、数据隐私、是否可作为 connector | mock survey rows -> themes | 否 | 否 | 可选 |
| 77 | `quality_sprint02_typebot_lead_qualification_candidate` | Typebot | https://github.com/baptisteArno/typebot.io | Chat/form workflow | no | no | tool_adapter | openai_compatible_possible | optional | 销售 | 销售/客服 | 线索问卷结构化和分层建议 | 77 | 完整产品，需避免当 Skill 直接推荐扣 23 | lead form 候选补充 | needs_license_review | mock_transcript_only | license、数据隐私、发送/写入禁用 | mock form transcript -> lead score | 否 | 否 | 可选 |
| 78 | `quality_sprint02_calendly_booking_brief_candidate` | Calendly API | https://developer.calendly.com/ | SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售/行政 | 预约记录摘要、会前准备和改期风险 | 80 | OAuth/日程隐私、写入边界扣 20 | Sprint01 Cal.com 的商业替代 | needs_license_review | read_only_mock | API terms、read-only、禁止创建预约 | mock events -> prep brief | 否 | 否 | 是 |
| 79 | `quality_sprint02_mailchimp_campaign_report_candidate` | Mailchimp Marketing API | https://mailchimp.com/developer/marketing/api/ | Marketing SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场运营 | 邮件营销数据摘要、下次活动建议 | 81 | 邮件联系人隐私和发送边界扣 19 | 营销报表补充 | needs_license_review | read_only_mock | API terms、audience privacy、禁止发送 | mock campaign stats -> report | 否 | 否 | 是 |
| 80 | `quality_sprint02_brevo_email_campaign_brief_candidate` | Brevo API | https://developers.brevo.com/ | Marketing SaaS connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场运营 | 邮件/短信活动摘要和草稿，不发送 | 79 | 联系人隐私、短信/邮件发送风险扣 21 | email marketing 来源补充 | needs_license_review | read_only_or_draft_only | API terms、发送禁用、联系人隐私 | mock stats -> next campaign brief | 否 | 否 | 是 |

## 30 个优先入库候选

| priority | candidate_id | quality_score | business_package | source_type | recommended_state | trial_mode | media | real_generation | BYOK | 主要理由 |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | `quality_sprint02_microsoft_excel_report_agent_candidate` | 87 | 经营报表 | SaaS connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 中小微高频表格周报，作为 Google Sheets 路线替代，read-only 可控 |
| P0 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | 86 | 销售 | SaaS connector | `needs_license_review` | `read_only_or_draft_only` | 否 | 否 | 是 | 邮件跟进是销售高频场景，禁止发送即可进入 dry-run |
| P0 | `quality_sprint02_stability_product_scene_candidate` | 85 | 电商/门店 | Image API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 商品图/场景图价值高，Provider route 清楚 |
| P0 | `quality_sprint02_adobe_firefly_product_ad_image_candidate` | 84 | 营销 | Image API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 广告图和海报场景强，需优先核商用条款 |
| P0 | `quality_sprint02_fal_flux_product_photo_candidate` | 84 | 电商/门店 | Image API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 多模型路线适合商品图试跑，需逐模型核 license |
| P0 | `quality_sprint02_runway_gen4_short_ad_candidate` | 84 | 营销 | Video API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 短视频广告高价值，先做 payload 和政策核验 |
| P0 | `quality_sprint02_gmail_customer_email_triage_candidate` | 84 | 客服 | SaaS connector | `needs_license_review` | `read_only_or_draft_only` | 否 | 否 | 是 | 邮件客服分类/草稿适配稳定 13 能力扩展 |
| P0 | `quality_sprint02_zoho_crm_followup_candidate` | 84 | 销售 | CRM API connector | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | Zoho CRM 中小微适配好，作为 HubSpot 替代 |
| P0 | `quality_sprint02_lark_docs_meeting_action_candidate` | 84 | 行政/财务/HR | SaaS connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 飞书文档/会议纪要在中文 SMB 场景高频 |
| P0 | `quality_sprint02_recraft_brand_banner_candidate` | 83 | 营销 | Image API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 品牌 banner/图标/海报能力强，需核 API 和商用 |
| P0 | `quality_sprint02_pipedrive_deal_next_step_candidate` | 83 | 销售 | CRM API connector | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | 销售管道 next action 易做结构化输入输出 |
| P0 | `quality_sprint02_square_pos_daily_report_candidate` | 83 | 电商/门店 | POS API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 门店 POS 日报高价值，read-only 可控 |
| P1 | `quality_sprint02_ideogram_poster_text_candidate` | 82 | 营销 | Image API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 海报文字能力值得核验，但中文稳定性待测 |
| P1 | `quality_sprint02_fal_kontext_image_edit_candidate` | 82 | 电商/门店 | Image edit API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 商品图局部编辑价值高，需核模型 license |
| P1 | `quality_sprint02_removebg_cutout_candidate` | 82 | 电商/门店 | Image edit API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 单点明确，适合快速 L1，但能力较窄 |
| P1 | `quality_sprint02_luma_dream_machine_store_video_candidate` | 82 | 营销 | Video API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 门店/商品短视频价值高，API 条款需核 |
| P1 | `quality_sprint02_wecom_customer_group_summary_candidate` | 82 | 客服 | SaaS connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 中文私域客服高频，权限边界必须严格 |
| P1 | `quality_sprint02_gorgias_ecommerce_support_candidate` | 82 | 客服 | Support API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 电商客服工单适配好，禁止回复即可 mock |
| P1 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | 82 | 行政/财务/HR | Finance API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 小微财务费用核对高频，但需非审计声明 |
| P1 | `quality_sprint02_google_veo_store_campaign_candidate` | 81 | 营销 | Video API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 视频质量潜力高，地区/route/商用需核 |
| P1 | `quality_sprint02_heygen_training_avatar_cn_candidate` | 83 | 行政/财务/HR | Avatar Video API | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | 培训口播和客服培训价值高，肖像/声音授权需核 |
| P1 | `quality_sprint02_haystack_faq_rag_candidate` | 81 | 客服 | RAG framework | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 稳交付 FAQ 的替代底层，适合作 L1 替代来源 |
| P1 | `quality_sprint02_shopline_order_digest_candidate` | 82 | 电商/门店 | Ecommerce API connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 中文/跨境电商场景补强，订单 read-only 可控 |
| P1 | `quality_sprint02_feishu_bitable_ops_tracker_candidate` | 81 | 经营报表 | SaaS connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 多门店运营表格摘要，中文 SMB 适配好 |
| P1 | `quality_sprint02_mailchimp_campaign_report_candidate` | 81 | 营销 | Marketing SaaS connector | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 营销活动复盘高频，禁止发送即可控 |
| P1 | `quality_sprint02_open_design_menu_poster_child_candidate` | 79 | 电商/门店 | Open design skill pack | `needs_license_review` | `dry_run_metadata_only` | 是 | 可能 | 可能 | 菜单海报高频，但需定位子 skill 和 API |
| P1 | `quality_sprint02_autogen_sales_roleplay_candidate` | 80 | 销售 | Agent workflow | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 销售训练 workflow 可迁移，但需轻量化 |
| P1 | `quality_sprint02_crewai_market_research_candidate` | 79 | 销售 | Agent workflow | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 潜客/竞品调研价值高，需限制外部抓取 |
| P1 | `quality_sprint02_instructor_schema_extraction_candidate` | 80 | 行政/财务/HR | Structured extraction | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 结构化抽取能力强，可包裹进合同/票据/表单 |
| P1 | `quality_sprint02_promptfoo_support_regression_candidate` | 82 | 客服 | Eval framework | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 客服回复回归测试适合质检流水线 |

## P0 清单

1. `quality_sprint02_microsoft_excel_report_agent_candidate`
2. `quality_sprint02_microsoft_graph_outlook_followup_candidate`
3. `quality_sprint02_stability_product_scene_candidate`
4. `quality_sprint02_adobe_firefly_product_ad_image_candidate`
5. `quality_sprint02_fal_flux_product_photo_candidate`
6. `quality_sprint02_runway_gen4_short_ad_candidate`
7. `quality_sprint02_gmail_customer_email_triage_candidate`
8. `quality_sprint02_zoho_crm_followup_candidate`
9. `quality_sprint02_lark_docs_meeting_action_candidate`
10. `quality_sprint02_recraft_brand_banner_candidate`
11. `quality_sprint02_pipedrive_deal_next_step_candidate`
12. `quality_sprint02_square_pos_daily_report_candidate`

## P1 清单

1. `quality_sprint02_ideogram_poster_text_candidate`
2. `quality_sprint02_fal_kontext_image_edit_candidate`
3. `quality_sprint02_removebg_cutout_candidate`
4. `quality_sprint02_luma_dream_machine_store_video_candidate`
5. `quality_sprint02_wecom_customer_group_summary_candidate`
6. `quality_sprint02_gorgias_ecommerce_support_candidate`
7. `quality_sprint02_zoho_books_expense_reconcile_candidate`
8. `quality_sprint02_google_veo_store_campaign_candidate`
9. `quality_sprint02_heygen_training_avatar_cn_candidate`
10. `quality_sprint02_haystack_faq_rag_candidate`
11. `quality_sprint02_shopline_order_digest_candidate`
12. `quality_sprint02_feishu_bitable_ops_tracker_candidate`
13. `quality_sprint02_mailchimp_campaign_report_candidate`
14. `quality_sprint02_open_design_menu_poster_child_candidate`
15. `quality_sprint02_autogen_sales_roleplay_candidate`
16. `quality_sprint02_crewai_market_research_candidate`
17. `quality_sprint02_instructor_schema_extraction_candidate`
18. `quality_sprint02_promptfoo_support_regression_candidate`
## 许可证窗口建议

- 优先核 P0 12 个：重点看 Provider/API 条款、OAuth scope、素材上传/存储、生成内容商用权利、是否可 BYOK。
- 媒体类候选在 L1 前只允许 `dry_run_payload_only`，不允许真实生成。
- SaaS/MCP/API 类候选在 L1 前只允许 mock/read-only/dry-run，不允许连接真实账号，不允许写入、发送、上传或发布。
- Agent workflow/framework 类候选只作为可迁移 workflow 来源，L1 需确认 license、依赖体积、是否能抽成轻量 callable Skill。
- 中文角色库/业务模板类候选不能直接写成标准 Skill，必须先模板化为稳定输入输出，并标注平台规则/版权边界。

## 禁止动作

- 不真实调用 API。
- 不生成图片、视频、音频或真实文件。
- 不写 API key。
- 不写稳交付库。
- 不把 market lead 宣称为可调用 Skill。
- 不把完整产品、大型 WebUI、重框架直接作为 Skill 入库。
