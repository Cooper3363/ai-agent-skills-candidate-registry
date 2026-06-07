# Next50 高质量候选研究结果

更新日期: 2026-06-05

## Summary

本轮按新口径补充 50 个候选：只要能适配本地 DeepAgents / 通用 Agent Skill 运行方式、可通过 OpenAI-compatible 中转站模型通道或明确 provider/API adapter 接入、能服务中小微六部门场景，即可进入候选调用库研究队列。

- 新增候选线索: 50
- 媒体生成 / 媒体制作候选: 24
- 依赖外部 API / provider 的候选: 30
- 可仅用中转站文本模型 mock/dry-run 的候选: 20
- 本轮只做研究和入队，不真实调用 API，不生成图片/视频，不写稳交付库，不写 key。
- 客户正式可调用 Skill 仍为 13。

## 业务包分布

| 业务包 | 数量 |
| --- | ---: |
| 客服 | 7 |
| 销售 | 7 |
| 营销 | 14 |
| 电商/门店 | 10 |
| 经营报表 | 5 |
| 行政/财务/HR | 7 |
| 合计 | 50 |

## 外部 API 依赖分类

| 依赖分类 | 数量 | 说明 |
| --- | ---: | --- |
| `relay_text_only` | 20 | 仅需 OpenAI-compatible 文本模型中转站，可 mock/dry-run |
| `relay_image_route_check` | 8 | 优先通过中转站图片生成/编辑 route，需验证 endpoint、返回文件、计费 |
| `relay_video_route_check` | 5 | 优先通过中转站视频 route，需验证轮询、下载、成本 |
| `provider_key_required` | 8 | 需要 HeyGen/Synthesia/Runway/Luma/Canva/Figma/Shopify/Ads 等独立 key |
| `mcp_or_saas_adapter_required` | 5 | 需要 MCP 或 SaaS adapter；本轮只 dry-run |
| `self_host_or_local_runtime` | 4 | ComfyUI/Remotion/FFmpeg/Playwright 等本地运行或自托管，需基础设施复核 |

## Next50 候选总表

| # | candidate_id | 名称 | 来源链接 | 来源类型 | 是否已有 SKILL.md/skill.yaml | 是否可适配 DeepAgents / 通用 Agent Skill | 模型通道适配性 | 是否依赖外部 API | 业务包 | 角色 | 使用场景 | 与稳交付 13 个 Skill 的复用关系 | 建议状态 | deepagents_trial_fit | 建议 trial mode | 风险标签 | 下一步交给许可证窗口的核验点 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `support_voice_call_summary_agent_candidate` | 客服电话录音摘要候选 | https://github.com/openai/whisper | GitHub model/tool | 否 | 是，可封装为转写后摘要 Agent Skill | 文本中转站可摘要；音频转写需 adapter | 是，ASR/API 或本地模型 | 客服 | 客服主管 | 客服电话转文字摘要、风险点、转人工原因 | 复用 `support_ticket_classifier`, `support_reply_guardrail` | `needs_license_review` | `dry_run_only` | `mock_audio_text_only` | audio_upload, pii, consent_required | Whisper/ASR 许可证、音频上传/存储、客户授权、中文识别质量 |
| 2 | `support_training_microvideo_agent_candidate` | 客服培训微视频生成候选 | https://docs.heygen.com/ | real_generation_provider_agent | 否 | 是，先以脚本+provider payload 运行 | 文本中转站生成脚本；视频需 provider key | 是，HeyGen API | 客服 | 客服培训 | 根据低分对话生成 30 秒培训口播视频 | 复用 `support_reply_guardrail`, `support_quality_eval_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | avatar_rights, video_generation, pii | HeyGen 条款、头像/声音授权、不得上传真实客服录音、费用 |
| 3 | `support_reply_multilingual_localizer_candidate` | 多语客服回复本地化候选 | https://github.com/openai/openai-agents-python | GitHub Agent | 否 | 是，轻量 callable text skill | 中转站文本模型直接可用 | 否 | 客服 | 跨境客服 | 将中文客服回复改写成英文/日文/东南亚语气版本 | 复用 `support_reply_guardrail` | `mock_callable` | `skill_ready` | `mock_only` | translation_accuracy, policy_conflict | OpenAI Agents SDK 许可证、输出需保留原政策边界 |
| 4 | `support_faq_video_answer_script_candidate` | FAQ 视频回答脚本候选 | https://docs.synthesia.io/ | real_generation_provider_agent | 否 | 是，先脚本，后数字人 adapter | 文本中转站生成脚本；视频需 provider | 是，Synthesia API | 客服 | 客服运营 | 把高频 FAQ 生成短视频口播脚本和数字人 payload | 复用 `faq_answer_with_citations` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | citation_required, avatar_rights | Synthesia 条款、FAQ 引用保真、不得真实生成/发布 |
| 5 | `support_ticket_auto_reply_quality_gate_candidate` | 客服自动回复质检闸门候选 | https://github.com/langchain-ai/langgraph | GitHub Agent/workflow | 否 | 是，可作为 guardrail workflow | 中转站文本模型直接可用 | 否 | 客服 | 客服主管 | 在回复草稿发送前检查政策、PII、承诺、转人工 | 复用 `support_reply_guardrail`, `support_pii_redactor` | `mock_callable` | `skill_ready` | `mock_only` | false_negative, escalation | LangGraph 许可证、是否只作为 workflow 依赖、不发送消息 |
| 6 | `support_complaint_evidence_packet_candidate` | 客诉证据包整理候选 | https://github.com/run-llama/llama_index | GitHub RAG/tool | 否 | 是，可做只读文档整理 skill | 中转站文本模型可用；RAG 可本地 mock | 否 | 客服 | 客诉专员 | 整理客户投诉、订单、聊天记录成证据包摘要 | 复用 `complaint_escalation_summary_candidate` | `needs_license_review` | `mock_only` | `read_only_mock` | pii, legal_escalation | LlamaIndex 许可证、不得读真实客户文件、法律/赔偿人工复核 |
| 7 | `support_afterhours_triage_bot_candidate` | 非工作时间客服分流候选 | https://github.com/crewAIInc/crewAI | GitHub Agent | 否 | 是，可做多步骤 Agent | 文本中转站可用 | 否 | 客服 | 值班客服 | 非工作时间自动分类紧急度和次日处理建议 | 复用 `support_ticket_classifier` | `needs_license_review` | `mock_only` | `mock_only` | availability, emergency_misroute | crewAI 许可证、不得承诺即时处理、紧急事项转人工 |
| 8 | `sales_demo_video_brief_to_clip_candidate` | 销售演示短视频生成候选 | https://docs.dev.runwayml.com/ | real_generation_provider_agent | 否 | 是，先 brief/payload，后 provider route | 文本中转站生成脚本；视频需 Runway/provider | 是，Runway API | 销售 | 售前顾问 | 根据客户场景生成产品演示短视频脚本和生成 payload | 复用 `proposal_outline_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | video_generation, claims | Runway 条款、素材授权、不得承诺产品效果 |
| 9 | `sales_avatar_pitch_video_candidate` | 销售数字人口播候选 | https://docs.heygen.com/ | real_generation_provider_agent | 否 | 是，数字人口播 payload skill | 文本中转站生成话术；视频需 HeyGen | 是，HeyGen API | 销售 | 销售代表 | 生成 60 秒客户邀约/产品介绍数字人口播 payload | 复用 `sales_followup_draft_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | avatar_rights, outbound | HeyGen 条款、不得真实发送、肖像/声音授权 |
| 10 | `sales_proposal_deck_generator_candidate` | 销售提案 PPT 草稿候选 | https://python-pptx.readthedocs.io/ | GitHub/library | 否 | 是，可作为文档生成 Agent Skill | 文本中转站生成结构；PPT 生成需本地库 | 否，本地 runtime | 销售 | 商务支持 | 根据方案大纲生成 PPT 结构和 dry-run slide spec | 复用 `proposal_outline_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_slide_spec` | file_write, brand_asset | python-pptx 许可证、只输出 spec 不写真实 PPT |
| 11 | `sales_call_roleplay_coach_candidate` | 销售通话角色扮演教练候选 | https://github.com/openai/openai-agents-python | GitHub Agent | 否 | 是，文本对话 Agent | 中转站文本模型直接可用 | 否 | 销售 | 销售教练 | 模拟客户异议并给销售复盘建议 | 复用 `quote_objection_response_candidate` | `mock_callable` | `skill_ready` | `mock_only` | hallucinated_customer, training_only | SDK 许可证、训练用途声明、不得当真实客户反馈 |
| 12 | `sales_contract_redline_summary_candidate` | 销售合同红线摘要候选 | https://github.com/Unstructured-IO/unstructured | GitHub document tool | 否 | 是，文档解析+摘要 Agent | 文本中转站可摘要；文档解析可 mock | 否/可本地 | 销售 | 销售经理 | 提取合同中付款、违约、续约、交付风险 | 复用 `contract_clause_partitioner_candidate` | `needs_license_review` | `mock_only` | `mock_doc_text_only` | legal, contract | Unstructured 许可证、非法律意见、真实合同读取边界 |
| 13 | `sales_crm_next_best_action_candidate` | CRM 下一步动作候选 | https://github.com/ComposioHQ/composio | MCP/SaaS connector | 否 | 是，先 dry-run connector payload | 文本中转站可推理；CRM 需 adapter | 是，CRM/SaaS API | 销售 | 销售运营 | 从 CRM 记录生成下一步动作，不写 CRM | 复用 `crm_note_structurer` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | crm_write, oauth | Composio 许可证、OAuth、write_allowed=false |
| 14 | `sales_quote_pdf_brief_candidate` | 报价单 PDF 摘要候选 | https://github.com/pymupdf/PyMuPDF | GitHub document library | 否 | 是，可做 PDF 文本解析候选 | 文本中转站摘要；PDF 解析本地 | 否/可本地 | 销售 | 商务支持 | 将报价 PDF 转成价格、条款、有效期摘要 | 复用 `quote_scope_change_summary_candidate` | `needs_license_review` | `mock_only` | `mock_pdf_text_only` | document_license, pricing | PyMuPDF 许可证、真实文件读取、报价不自动发送 |
| 15 | `marketing_real_poster_banner_agent_candidate` | 海报/banner 真实出图候选 | https://platform.openai.com/docs/guides/image-generation | real_generation_provider_agent | 否 | 是，作为 image generation Agent Skill | 优先中转站图片 route check | 是，OpenAI/relay image API | 营销 | 美工/运营 | 生成活动海报、banner、社媒封面 | 复用 `visual_prompt_brief_candidate`, `marketing_copy_pack` | `needs_license_review` | `dry_run_only` | `route_check_then_1_image_smoke` | image_generation, copyright | 中转站图片 endpoint、内容政策、费用、输出文件审计 |
| 16 | `marketing_text_overlay_poster_candidate` | 带字海报生成候选 | https://developer.ideogram.ai/ | real_generation_provider_agent | 否 | 是，poster agent + provider adapter | 中转站可生成 prompt；出图需 Ideogram/relay | 是，Ideogram API | 营销 | 设计/运营 | 生成带中文卖点文字的海报/卡片 | 复用 `local_event_poster_copy_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | text_rendering, brand_rights | Ideogram API 条款、中文文字质量、商标/字体授权 |
| 17 | `marketing_brand_asset_generator_candidate` | 品牌资产/插画生成候选 | https://www.recraft.ai/docs | real_generation_provider_agent | 否 | 是，品牌资产 Agent | 中转站 prompt；Recraft/provider 出图 | 是，Recraft API | 营销 | 品牌设计 | 生成品牌插画、图标、社媒模板方向 | 复用 `brand_forbidden_words_checker_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | brand_ip, vector_asset | Recraft 条款、品牌资产授权、不得声明版权清白 |
| 18 | `marketing_short_video_ad_agent_candidate` | 短视频广告生成候选 | https://ai.google.dev/gemini-api/docs/video | real_generation_provider_agent | 否 | 是，video generation Agent | 中转站/Google Veo route check | 是，Veo/Gemini API | 营销 | 短视频运营 | 生成 5-8 秒活动短视频广告 | 复用 `native_video_brief_skill_candidate` | `needs_license_review` | `dry_run_only` | `route_check_then_short_video_smoke` | video_generation, cost | Veo route、轮询下载、费用、内容安全 |
| 19 | `marketing_social_carousel_image_agent_candidate` | 社媒轮播图生成候选 | https://github.com/nexu-io/open-design | OpenClaw/OpenClaw-like skill pack | 可能有子 skill | 是，需子 skill 映射 | 中转站文本+图片 route；open-design 子技能 | 是/视子 skill | 营销 | 内容运营 | 生成小红书/朋友圈轮播图结构和图片 payload | 复用 `content_calendar_mock_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_metadata_only` | export, image_api | open-design 子目录、许可证、是否写文件/截图 |
| 20 | `marketing_product_launch_video_script_to_render_candidate` | 新品发布视频渲染候选 | https://www.remotion.dev/docs/ | programmatic_video_agent | 否 | 是，本地程序化视频 spec | 文本中转站生成脚本；Remotion 本地渲染 | 否/本地 runtime | 营销 | 活动运营 | 把新品发布脚本转成 Remotion 渲染 spec | 复用 `structured_campaign_brief` | `needs_license_review` | `dry_run_only` | `dry_run_render_spec` | file_write, local_runtime | Remotion 许可证、sandbox 输出、依赖锁定 |
| 21 | `marketing_ad_creative_batch_generator_candidate` | 广告素材批量生成候选 | https://docs.fal.ai/model-apis | real_generation_provider_agent | 否 | 是，多模型媒体路由 Agent | 中转站或 fal route check | 是，fal API | 营销 | 投放运营 | 批量生成广告图/短视频素材 payload | 复用 `ad_variant_brief_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | bulk_generation, ad_claims | fal 条款、多模型许可证、费用上限、不得投放 |
| 22 | `marketing_thumbnail_generator_candidate` | 视频封面/缩略图生成候选 | https://platform.stability.ai/docs | real_generation_provider_agent | 否 | 是，image agent | 中转站 prompt；Stability/provider 出图 | 是，Stability API | 营销 | 视频运营 | 为短视频/B站/课程生成封面图 | 复用 `native_image_marketing_skill_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | copyright, thumbnail_claims | Stability 条款、模型商用、素材授权 |
| 23 | `marketing_figma_banner_spec_candidate` | Figma banner 设计 spec 候选 | https://www.figma.com/developers/api | SaaS/API design adapter | 否 | 是，先输出 Figma dry-run payload | 文本中转站可生成 spec；Figma 需 OAuth/API | 是，Figma API | 营销 | 设计 | 生成 Figma banner frame spec，不写 Figma | 复用 `compatible_design_system_review_skill_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | oauth, design_write | Figma API 条款、write_allowed=false、品牌资源 |
| 24 | `marketing_canva_template_brief_candidate` | Canva 模板 brief 候选 | https://www.canva.dev/docs/ | SaaS/API design adapter | 否 | 是，先模板 brief/payload | 文本中转站可用；Canva 需 API | 是，Canva API | 营销 | 运营设计 | 生成 Canva 模板 brief 和素材清单 | 复用 `visual_prompt_brief_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | saas_terms, export | Canva 条款、不得创建/导出真实设计 |
| 25 | `ecommerce_product_main_image_agent_candidate` | 商品主图真实生成候选 | https://platform.openai.com/docs/guides/image-generation | real_generation_provider_agent | 否 | 是，商品图 Agent Skill | 中转站图片 route check | 是，OpenAI/relay image API | 电商/门店 | 商品运营 | 根据商品信息生成主图/场景图 | 复用 `product_listing_copy_candidate`, `visual_prompt_brief_candidate` | `needs_license_review` | `dry_run_only` | `route_check_then_1_image_smoke` | product_accuracy, trademark | 商品真实性、品牌/商标、图片 route、成本 |
| 26 | `ecommerce_background_replace_agent_candidate` | 商品图背景替换候选 | https://docs.fal.ai/model-apis | real_image_edit_agent | 否 | 是，image edit Agent | 中转站/Provider 图片编辑 route | 是，fal/relay image edit | 电商/门店 | 商品运营 | 给 mock 商品图换纯色/场景背景 | 复用 `open_design_real_media_skill_pack_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | image_upload, rights | 输入素材授权、上传/存储、编辑模型条款 |
| 27 | `ecommerce_tryon_model_image_candidate` | 服饰试穿图候选 | https://docs.fal.ai/model-apis | real_image_generation_agent | 否 | 是，provider adapter | fal/provider route required | 是，fal try-on/API | 电商/门店 | 服饰商家 | 用 mock 模特/服装生成试穿图 payload | 复用商品图候选 | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | biometric, likeness, apparel | 肖像授权、服装图授权、不得用真实客户照片 |
| 28 | `ecommerce_product_video_from_image_candidate` | 商品图生短视频候选 | https://lumalabs.ai/api | real_video_generation_agent | 否 | 是，video adapter | 中转站或 Luma route check | 是，Luma API | 电商/门店 | 商品运营 | 把商品图转成 5 秒动效展示视频 | 复用 `google_veo_real_video_agent_candidate` | `needs_license_review` | `dry_run_only` | `route_check_then_short_video_smoke` | image_to_video, rights | Luma 条款、素材授权、下载 URL、成本 |
| 29 | `ecommerce_review_to_product_image_prompt_candidate` | 评价转商品图 prompt 候选 | https://github.com/openai/openai-agents-python | GitHub Agent | 否 | 是，text Agent | 中转站文本模型直接可用 | 否 | 电商/门店 | 商品运营 | 从用户评价提炼商品图卖点和 prompt | 复用 `review_sentiment_cluster_candidate` | `mock_callable` | `skill_ready` | `mock_only` | review_bias | SDK 许可证、评价脱敏、不得生成虚假卖点 |
| 30 | `ecommerce_shopify_listing_asset_dryrun_candidate` | Shopify 素材上架 dry-run 候选 | https://shopify.dev/docs/api | SaaS/API connector | 否 | 是，connector payload skill | 文本中转站生成 payload；Shopify 需 API | 是，Shopify API | 电商/门店 | 店铺运营 | 生成商品图/标题/描述上架 dry-run payload | 复用 `product_listing_copy_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | ecommerce_write, oauth | Shopify API 条款、write_allowed=false、不上传素材 |
| 31 | `ecommerce_marketplace_ad_image_variants_candidate` | 电商广告图变体候选 | https://developer.ideogram.ai/ | real_generation_provider_agent | 否 | 是，image variant Agent | 中转站 prompt；Ideogram/provider | 是，Ideogram/API | 电商/门店 | 投放运营 | 生成电商广告图变体 payload | 复用 `ad_variant_brief_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | ad_claims, image_rights | 广告合规、图片生成条款、不得投放 |
| 32 | `ecommerce_livecommerce_avatar_script_candidate` | 直播带货数字人口播候选 | https://docs.heygen.com/ | avatar_video_agent | 否 | 是，avatar payload skill | 文本中转站脚本；HeyGen 需 provider | 是，HeyGen API | 电商/门店 | 直播运营 | 生成直播带货数字人口播脚本和 payload | 复用 `livecommerce_script_outline_candidate` 旧线索/营销文案 | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | avatar_rights, sales_claims | 肖像授权、价格承诺、不得直播/发布 |
| 33 | `ecommerce_storefront_screenshot_audit_candidate` | 店铺页面截图审阅候选 | https://github.com/microsoft/playwright | GitHub/browser tool | 否 | 是，browser tool adapter | 文本模型可分析；截图需本地 browser | 否/本地 tool | 电商/门店 | 店铺运营 | 对用户提供或本地页面截图做布局/转化审阅 | 复用 `native_cro_skill_candidate` | `needs_license_review` | `dry_run_only` | `local_screenshot_only` | screenshot, browser | Playwright 许可证、只本地/授权页面、不得抓网页 |
| 34 | `ecommerce_inventory_photo_qc_candidate` | 库存/货架照片质检候选 | https://ai.google.dev/gemini-api/docs/image-understanding | vision_model_agent | 否 | 是，vision adapter | 需视觉模型 route check | 是，vision API | 电商/门店 | 门店店长 | 用 mock 货架图识别缺货/陈列问题 | 复用 `order_inventory_exception_candidate` | `needs_license_review` | `dry_run_only` | `mock_image_payload_only` | image_upload, privacy | 视觉模型条款、图片上传、员工/顾客隐私 |
| 35 | `ecommerce_product_detail_page_generator_candidate` | 商品详情页生成候选 | https://github.com/nexu-io/open-design | OpenClaw/OpenClaw-like skill pack | 可能有子 skill | 是，需子 skill manifest | 文本中转站+设计 dry-run | 否/视子 skill | 电商/门店 | 商品运营 | 生成商品详情页结构、文案和视觉模块 spec | 复用 `product_listing_copy_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_metadata_only` | file_write, product_claims | open-design 子 skill、是否写代码/截图、商品声明 |
| 36 | `metrics_video_daily_report_candidate` | 经营日报视频生成候选 | https://www.remotion.dev/docs/ | programmatic_video_agent | 否 | 是，本地程序化视频 spec | 文本中转站生成脚本；Remotion 本地渲染 | 否/本地 runtime | 经营报表 | 老板/店长 | 把日报指标转成 30 秒竖版汇报视频 spec | 复用 `daily_weekly_metrics_reporter` | `needs_license_review` | `dry_run_only` | `dry_run_render_spec` | file_write, chart_accuracy | Remotion 许可证、图表准确性、sandbox 输出 |
| 37 | `metrics_chart_image_generation_candidate` | 指标图表卡片生成候选 | https://quickchart.io/documentation/ | SaaS/API chart tool | 否 | 是，可作为 chart image agent | 文本中转站生成 chart spec；QuickChart/API 可选 | 是/可本地替代 | 经营报表 | 数据运营 | 生成老板周报图表卡片 spec 或图片 | 复用 `structured_metric_summary` | `needs_license_review` | `dry_run_only` | `dry_run_chart_spec` | data_accuracy, external_api | QuickChart 条款、是否外传数据、可否本地渲染 |
| 38 | `metrics_anomaly_narrative_audio_candidate` | 异常指标语音播报候选 | https://platform.openai.com/docs/guides/text-to-speech | audio_generation_agent | 否 | 是，TTS adapter | 文本中转站生成稿；TTS route check | 是，TTS API | 经营报表 | 老板 | 把异常指标解释成语音播报脚本和 TTS payload | 复用 `metric_exception_classifier` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | audio_generation, financial_advice | TTS 条款、不得真实生成/发送、非财务建议 |
| 39 | `metrics_spreadsheet_agent_mcp_candidate` | 表格分析 MCP 候选 | https://github.com/modelcontextprotocol/servers | MCP/tool | 否 | 是，MCP adapter | 文本中转站可用；MCP 需本地 adapter | 否/本地 MCP | 经营报表 | 数据运营 | 对 mock 表格做字段清洗、指标摘要和异常提示 | 复用报表 3 件套 | `needs_license_review` | `mock_only` | `mock_spreadsheet_only` | file_read, data_quality | MCP server 许可证、文件读取边界、只 mock 表格 |
| 40 | `metrics_forecast_scenario_simulator_candidate` | 经营情景模拟候选 | https://github.com/langchain-ai/langgraph | GitHub Agent/workflow | 否 | 是，多步骤 workflow | 中转站文本模型可用 | 否 | 经营报表 | 老板/财务 | 输入销量/毛利/费用假设，输出情景模拟摘要 | 复用 `structured_metric_summary` | `mock_callable` | `skill_ready` | `mock_only` | financial_advice, assumptions | LangGraph 许可证、非财务建议、假设透明 |
| 41 | `hr_training_avatar_video_candidate` | 员工培训数字人视频候选 | https://docs.synthesia.io/ | avatar_video_agent | 否 | 是，avatar payload skill | 文本中转站脚本；Synthesia 需 provider | 是，Synthesia API | 行政/财务/HR | HR/培训 | 根据 SOP 生成入职/制度培训数字人视频 payload | 复用 `sop_step_extractor_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | avatar_rights, employee_policy | Synthesia 条款、员工制度人工审核、不得真实生成 |
| 42 | `hr_resume_interview_avatar_roleplay_candidate` | 面试模拟数字人候选 | https://docs.heygen.com/ | avatar_video_agent | 否 | 是，先 roleplay script/payload | 文本中转站脚本；HeyGen 需 provider | 是，HeyGen API | 行政/财务/HR | HR | 根据岗位生成面试模拟口播 payload | 复用 `resume_screening_question_pack_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | hiring_bias, avatar_rights | 不做录用建议、HeyGen 条款、候选人隐私 |
| 43 | `admin_policy_explainer_video_candidate` | 制度解读短视频候选 | https://ai.google.dev/gemini-api/docs/video | real_video_generation_agent | 否 | 是，video payload skill | 中转站/Veo route check | 是，Veo/Gemini API | 行政/财务/HR | 行政 | 将公司制度改成 5-8 秒说明视频 payload | 复用 `policy_notice_draft_candidate` 旧线索 | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | policy_accuracy, video_generation | 制度人工审核、视频 route、不得发布 |
| 44 | `finance_receipt_image_vision_extract_candidate` | 票据图片视觉抽取候选 | https://ai.google.dev/gemini-api/docs/image-understanding | vision_model_agent | 否 | 是，vision adapter | 需视觉模型 route check | 是，vision API | 行政/财务/HR | 财务 | 从 mock 发票/小票图片抽取字段并标异常 | 复用 `expense_invoice_parser` | `needs_license_review` | `dry_run_only` | `mock_image_payload_only` | pii, tax, image_upload | 视觉模型条款、税务/报销非结论、图片存储 |
| 45 | `admin_document_ocr_to_sop_candidate` | 文档 OCR 转 SOP 候选 | https://github.com/PaddlePaddle/PaddleOCR | GitHub OCR/tool | 否 | 是，OCR + text Agent | OCR 需本地/adapter；文本中转站可整理 | 是/可本地 | 行政/财务/HR | 行政 | 将扫描制度/手册转成 SOP 步骤 | 复用 `sop_step_extractor_candidate` | `needs_license_review` | `mock_only` | `mock_ocr_text_only` | document_upload, pii | PaddleOCR 许可证、文档上传、只 mock OCR 文本 |
| 46 | `finance_invoice_approval_workflow_dryrun_candidate` | 报销审批流程 dry-run 候选 | https://github.com/ComposioHQ/composio | MCP/SaaS connector | 否 | 是，workflow payload | 文本中转站可判断；审批系统需 adapter | 是，SaaS/OAuth | 行政/财务/HR | 财务 | 根据票据信息生成审批建议和 dry-run payload | 复用 `expense_invoice_parser` | `needs_license_review` | `dry_run_only` | `dry_run_payload_only` | finance_write, audit | Composio/OAuth、write_allowed=false、非审计结论 |
| 47 | `admin_meeting_to_slide_brief_candidate` | 会议纪要转汇报页候选 | https://python-pptx.readthedocs.io/ | document_generation_tool | 否 | 是，slide spec Agent | 文本中转站生成 slide spec；本地库可选 | 否/本地 runtime | 行政/财务/HR | 行政 | 把会议纪要转成管理汇报 PPT 大纲 | 复用 `meeting_minutes_action_candidate` | `needs_license_review` | `dry_run_only` | `dry_run_slide_spec` | file_write, confidentiality | python-pptx 许可证、会议信息保密、不写真实 PPT |
| 48 | `admin_contract_clause_risk_mcp_candidate` | 合同条款风险 MCP 候选 | https://github.com/modelcontextprotocol/servers | MCP/tool | 否 | 是，MCP adapter + text Agent | 文本中转站可用；MCP read-only | 否/本地 MCP | 行政/财务/HR | 合同经办 | 从 mock 合同文本提取风险条款和复核问题 | 复用 `contract_clause_partitioner_candidate` | `needs_license_review` | `mock_only` | `mock_doc_text_only` | legal, file_read | MCP 许可证、非法律意见、真实文件读取边界 |
| 49 | `store_menu_poster_generation_candidate` | 门店菜单/价目表海报候选 | https://platform.openai.com/docs/guides/image-generation | real_generation_provider_agent | 否 | 是，image generation Agent | 中转站图片 route check | 是，OpenAI/relay image API | 电商/门店 | 门店店长 | 生成菜单、价目表、到店活动海报 | 复用 `marketing_copy_pack`, `local_event_poster_copy_candidate` | `needs_license_review` | `dry_run_only` | `route_check_then_1_image_smoke` | price_accuracy, image_generation | 价格准确性、字体/商标、图片 route 和费用 |
| 50 | `store_digital_signage_video_candidate` | 门店电子屏短视频候选 | https://www.remotion.dev/docs/ | programmatic_video_agent | 否 | 是，本地渲染 spec | 文本中转站脚本；Remotion/local render | 否/本地 runtime | 电商/门店 | 门店运营 | 生成 10 秒门店电子屏促销视频 spec | 复用 `structured_campaign_brief` | `needs_license_review` | `dry_run_only` | `dry_run_render_spec` | file_write, price_claims | Remotion 许可证、价格/促销人工审核、sandbox 输出 |

## 媒体生成候选清单

本轮 24 个媒体生成 / 媒体制作候选：

`support_training_microvideo_agent_candidate`, `support_faq_video_answer_script_candidate`, `sales_demo_video_brief_to_clip_candidate`, `sales_avatar_pitch_video_candidate`, `marketing_real_poster_banner_agent_candidate`, `marketing_text_overlay_poster_candidate`, `marketing_brand_asset_generator_candidate`, `marketing_short_video_ad_agent_candidate`, `marketing_social_carousel_image_agent_candidate`, `marketing_product_launch_video_script_to_render_candidate`, `marketing_ad_creative_batch_generator_candidate`, `marketing_thumbnail_generator_candidate`, `marketing_figma_banner_spec_candidate`, `marketing_canva_template_brief_candidate`, `ecommerce_product_main_image_agent_candidate`, `ecommerce_background_replace_agent_candidate`, `ecommerce_tryon_model_image_candidate`, `ecommerce_product_video_from_image_candidate`, `ecommerce_marketplace_ad_image_variants_candidate`, `ecommerce_livecommerce_avatar_script_candidate`, `metrics_video_daily_report_candidate`, `hr_training_avatar_video_candidate`, `admin_policy_explainer_video_candidate`, `store_menu_poster_generation_candidate`, `store_digital_signage_video_candidate`。

说明：其中 `support_faq_video_answer_script_candidate` 先是脚本/payload 候选，真实生成需 Synthesia route；`marketing_figma_banner_spec_candidate` 与 `marketing_canva_template_brief_candidate` 属于设计 SaaS 生产流，不直接生成图片但有外部设计 API 风险。

## 优先许可证复核建议

| 优先级 | candidate_id | 原因 |
| --- | --- | --- |
| P0 | `marketing_real_poster_banner_agent_candidate` | 中小微高频海报/banner，若中转站支持图片 route，可最快做 1 张图 smoke |
| P0 | `ecommerce_product_main_image_agent_candidate` | 商品主图是电商/门店高价值场景，需优先核图片 route 和商品真实性 |
| P0 | `marketing_short_video_ad_agent_candidate` | 短视频广告是重点新增方向，需优先核 Veo/relay 轮询和成本 |
| P0 | `ecommerce_product_video_from_image_candidate` | 商品图生视频高价值，需核素材授权和 Luma/relay route |
| P0 | `sales_avatar_pitch_video_candidate` | 数字人口播销售场景明确，需核 HeyGen 肖像/声音授权 |
| P0 | `hr_training_avatar_video_candidate` | 培训数字人适合企业内部使用，需核 Synthesia 条款 |
| P1 | `marketing_ad_creative_batch_generator_candidate` | fal 多模型可扩展，但多模型许可证和费用复杂 |
| P1 | `finance_receipt_image_vision_extract_candidate` | 票据视觉抽取业务价值高，但涉及 PII/财税边界 |
| P1 | `metrics_video_daily_report_candidate` | 程序化视频可本地 sandbox，但需核 Remotion 许可证和文件输出 |
| P1 | `ecommerce_shopify_listing_asset_dryrun_candidate` | 电商 SaaS connector 风险高，先确认 write_allowed=false |

## 边界

- 不写入稳交付库。
- 不写真实 API key。
- 不真实调用外部生成、发送、写入、抓取。
- 不生成图片、视频、音频、PPT 或真实文件。
- 所有外部 Provider / API 候选必须先进入许可证窗口和 route check。
