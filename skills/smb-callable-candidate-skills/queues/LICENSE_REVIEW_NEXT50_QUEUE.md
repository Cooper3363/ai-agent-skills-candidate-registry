# Next50 许可证 / Provider / Trial Mode 复核队列

更新日期: 2026-06-05

## 来源

- 研究结果: `../RESEARCH_NEXT50_RESULT.md`
- 候选数量: 50
- 媒体生成 / 媒体制作候选: 24
- 本队列只用于 L1 / provider / route check，不送 L2，不封装，不客户调用。

## 统一 L1 复核要求

每个候选至少输出：

- source license / terms
- commercial use notes
- 是否有 `SKILL.md` / `skill.yaml`
- DeepAgents / 通用 Agent Skill 适配方式
- OpenAI-compatible 中转站适配方式
- 外部 API / provider / OAuth / MCP / 本地 runtime 依赖
- trial mode: `mock_only` / `dry_run_only` / `route_check_required` / `provider_key_required` / `local_runtime_required`
- blocked actions: 发送、发布、写 CRM/店铺/日历/任务、真实抓取、真实生成、上传素材、写稳交付库
- L1 结论: `can_mock_smoke` / `can_dry_run_smoke` / `can_route_check` / `needs_provider_terms_review` / `component_only` / `blocked`

## Provider/API 依赖分类

| 分类 | 候选 |
| --- | --- |
| `relay_text_only` | `support_reply_multilingual_localizer_candidate`, `support_ticket_auto_reply_quality_gate_candidate`, `support_complaint_evidence_packet_candidate`, `support_afterhours_triage_bot_candidate`, `sales_call_roleplay_coach_candidate`, `sales_contract_redline_summary_candidate`, `sales_quote_pdf_brief_candidate`, `ecommerce_review_to_product_image_prompt_candidate`, `metrics_forecast_scenario_simulator_candidate`, `admin_document_ocr_to_sop_candidate`, `admin_contract_clause_risk_mcp_candidate` |
| `relay_image_route_check` | `marketing_real_poster_banner_agent_candidate`, `marketing_text_overlay_poster_candidate`, `marketing_brand_asset_generator_candidate`, `marketing_thumbnail_generator_candidate`, `ecommerce_product_main_image_agent_candidate`, `ecommerce_background_replace_agent_candidate`, `ecommerce_marketplace_ad_image_variants_candidate`, `store_menu_poster_generation_candidate` |
| `relay_video_route_check` | `marketing_short_video_ad_agent_candidate`, `ecommerce_product_video_from_image_candidate`, `admin_policy_explainer_video_candidate` |
| `provider_key_required` | `support_training_microvideo_agent_candidate`, `support_faq_video_answer_script_candidate`, `sales_demo_video_brief_to_clip_candidate`, `sales_avatar_pitch_video_candidate`, `ecommerce_tryon_model_image_candidate`, `ecommerce_livecommerce_avatar_script_candidate`, `hr_training_avatar_video_candidate`, `hr_resume_interview_avatar_roleplay_candidate`, `finance_receipt_image_vision_extract_candidate` |
| `mcp_or_saas_adapter_required` | `sales_crm_next_best_action_candidate`, `ecommerce_shopify_listing_asset_dryrun_candidate`, `marketing_figma_banner_spec_candidate`, `marketing_canva_template_brief_candidate`, `finance_invoice_approval_workflow_dryrun_candidate`, `metrics_spreadsheet_agent_mcp_candidate` |
| `self_host_or_local_runtime` | `sales_proposal_deck_generator_candidate`, `marketing_product_launch_video_script_to_render_candidate`, `metrics_video_daily_report_candidate`, `store_digital_signage_video_candidate`, `metrics_chart_image_generation_candidate`, `ecommerce_storefront_screenshot_audit_candidate` |
| `multi_model_provider_router` | `marketing_ad_creative_batch_generator_candidate` |

## 50 个候选复核队列

| # | candidate_id | 来源链接 | 来源类型 | 业务包 | 外部依赖 | 建议 trial mode | deepagents_trial_fit | 优先级 | 许可证窗口核验点 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `support_voice_call_summary_agent_candidate` | https://github.com/openai/whisper | GitHub model/tool | 客服 | ASR/API 或本地模型 | `mock_audio_text_only` | `dry_run_only` | P1 | Whisper 许可证、音频上传/存储、客户授权、PII |
| 2 | `support_training_microvideo_agent_candidate` | https://docs.heygen.com/ | real_generation_provider_agent | 客服 | HeyGen API | `dry_run_payload_only` | `dry_run_only` | P1 | HeyGen 条款、头像/声音授权、客服 PII、费用 |
| 3 | `support_reply_multilingual_localizer_candidate` | https://github.com/openai/openai-agents-python | GitHub Agent | 客服 | 无 | `mock_only` | `skill_ready` | P2 | SDK 许可证、翻译准确性、政策边界保留 |
| 4 | `support_faq_video_answer_script_candidate` | https://docs.synthesia.io/ | real_generation_provider_agent | 客服 | Synthesia API | `dry_run_payload_only` | `dry_run_only` | P1 | Synthesia 条款、FAQ 引用保真、不得生成/发布 |
| 5 | `support_ticket_auto_reply_quality_gate_candidate` | https://github.com/langchain-ai/langgraph | GitHub Agent/workflow | 客服 | 无 | `mock_only` | `skill_ready` | P2 | LangGraph 许可证、只做闸门不发送、false negative |
| 6 | `support_complaint_evidence_packet_candidate` | https://github.com/run-llama/llama_index | GitHub RAG/tool | 客服 | 无/本地 RAG | `read_only_mock` | `mock_only` | P2 | LlamaIndex 许可证、真实客户文件读取边界、法律/赔偿复核 |
| 7 | `support_afterhours_triage_bot_candidate` | https://github.com/crewAIInc/crewAI | GitHub Agent | 客服 | 无 | `mock_only` | `mock_only` | P2 | crewAI 许可证、非工作时间承诺、紧急事项转人工 |
| 8 | `sales_demo_video_brief_to_clip_candidate` | https://docs.dev.runwayml.com/ | real_generation_provider_agent | 销售 | Runway API | `dry_run_payload_only` | `dry_run_only` | P1 | Runway 条款、素材授权、不得承诺产品效果 |
| 9 | `sales_avatar_pitch_video_candidate` | https://docs.heygen.com/ | avatar_video_agent | 销售 | HeyGen API | `dry_run_payload_only` | `dry_run_only` | P0 | HeyGen 条款、肖像/声音授权、不得发送 |
| 10 | `sales_proposal_deck_generator_candidate` | https://python-pptx.readthedocs.io/ | document_generation_tool | 销售 | 本地 runtime | `dry_run_slide_spec` | `dry_run_only` | P2 | python-pptx 许可证、只输出 slide spec、不写真实 PPT |
| 11 | `sales_call_roleplay_coach_candidate` | https://github.com/openai/openai-agents-python | GitHub Agent | 销售 | 无 | `mock_only` | `skill_ready` | P2 | SDK 许可证、训练用途声明、不得当真实客户反馈 |
| 12 | `sales_contract_redline_summary_candidate` | https://github.com/Unstructured-IO/unstructured | GitHub document tool | 销售 | 文档解析 | `mock_doc_text_only` | `mock_only` | P2 | Unstructured 许可证、非法律意见、真实合同读取边界 |
| 13 | `sales_crm_next_best_action_candidate` | https://github.com/ComposioHQ/composio | MCP/SaaS connector | 销售 | CRM/OAuth | `dry_run_payload_only` | `dry_run_only` | P1 | Composio 许可证、OAuth、write_allowed=false |
| 14 | `sales_quote_pdf_brief_candidate` | https://github.com/pymupdf/PyMuPDF | document library | 销售 | 本地 PDF 解析 | `mock_pdf_text_only` | `mock_only` | P2 | PyMuPDF 许可证、真实文件读取、报价不发送 |
| 15 | `marketing_real_poster_banner_agent_candidate` | https://platform.openai.com/docs/guides/image-generation | real_generation_provider_agent | 营销 | OpenAI/relay image API | `route_check_then_1_image_smoke` | `dry_run_only` | P0 | 中转站图片 endpoint、内容政策、费用、输出文件审计 |
| 16 | `marketing_text_overlay_poster_candidate` | https://developer.ideogram.ai/ | real_generation_provider_agent | 营销 | Ideogram API | `dry_run_payload_only` | `dry_run_only` | P0 | Ideogram 条款、中文文字质量、商标/字体授权 |
| 17 | `marketing_brand_asset_generator_candidate` | https://www.recraft.ai/docs | real_generation_provider_agent | 营销 | Recraft API | `dry_run_payload_only` | `dry_run_only` | P1 | Recraft 条款、品牌资产授权、不得声明版权清白 |
| 18 | `marketing_short_video_ad_agent_candidate` | https://ai.google.dev/gemini-api/docs/video | real_generation_provider_agent | 营销 | Veo/Gemini API | `route_check_then_short_video_smoke` | `dry_run_only` | P0 | Veo/relay route、轮询下载、费用、内容安全 |
| 19 | `marketing_social_carousel_image_agent_candidate` | https://github.com/nexu-io/open-design | OpenClaw-like skill pack | 营销 | open-design 子 skill/API | `dry_run_metadata_only` | `dry_run_only` | P1 | 子目录、许可证、是否写文件/截图/导出 |
| 20 | `marketing_product_launch_video_script_to_render_candidate` | https://www.remotion.dev/docs/ | programmatic_video_agent | 营销 | Remotion 本地 runtime | `dry_run_render_spec` | `dry_run_only` | P2 | Remotion 许可证、sandbox 输出、依赖锁定 |
| 21 | `marketing_ad_creative_batch_generator_candidate` | https://docs.fal.ai/model-apis | real_generation_provider_agent | 营销 | fal API | `dry_run_payload_only` | `dry_run_only` | P1 | fal 条款、多模型许可证、费用上限、不得投放 |
| 22 | `marketing_thumbnail_generator_candidate` | https://platform.stability.ai/docs | real_generation_provider_agent | 营销 | Stability API | `dry_run_payload_only` | `dry_run_only` | P1 | Stability 条款、模型商用、素材授权 |
| 23 | `marketing_figma_banner_spec_candidate` | https://www.figma.com/developers/api | SaaS/API design adapter | 营销 | Figma API/OAuth | `dry_run_payload_only` | `dry_run_only` | P1 | Figma 条款、write_allowed=false、品牌资源 |
| 24 | `marketing_canva_template_brief_candidate` | https://www.canva.dev/docs/ | SaaS/API design adapter | 营销 | Canva API | `dry_run_payload_only` | `dry_run_only` | P1 | Canva 条款、不得创建/导出真实设计 |
| 25 | `ecommerce_product_main_image_agent_candidate` | https://platform.openai.com/docs/guides/image-generation | real_generation_provider_agent | 电商/门店 | OpenAI/relay image API | `route_check_then_1_image_smoke` | `dry_run_only` | P0 | 商品真实性、品牌/商标、图片 route、成本 |
| 26 | `ecommerce_background_replace_agent_candidate` | https://docs.fal.ai/model-apis | real_image_edit_agent | 电商/门店 | fal/relay image edit | `dry_run_payload_only` | `dry_run_only` | P0 | 输入素材授权、上传/存储、编辑模型条款 |
| 27 | `ecommerce_tryon_model_image_candidate` | https://docs.fal.ai/model-apis | real_image_generation_agent | 电商/门店 | fal try-on/API | `dry_run_payload_only` | `dry_run_only` | P1 | 肖像授权、服装图授权、不得用真实客户照片 |
| 28 | `ecommerce_product_video_from_image_candidate` | https://lumalabs.ai/api | real_video_generation_agent | 电商/门店 | Luma API | `route_check_then_short_video_smoke` | `dry_run_only` | P0 | Luma 条款、素材授权、下载 URL、成本 |
| 29 | `ecommerce_review_to_product_image_prompt_candidate` | https://github.com/openai/openai-agents-python | GitHub Agent | 电商/门店 | 无 | `mock_only` | `skill_ready` | P2 | SDK 许可证、评价脱敏、不得生成虚假卖点 |
| 30 | `ecommerce_shopify_listing_asset_dryrun_candidate` | https://shopify.dev/docs/api | SaaS/API connector | 电商/门店 | Shopify API/OAuth | `dry_run_payload_only` | `dry_run_only` | P1 | Shopify 条款、write_allowed=false、不上传素材 |
| 31 | `ecommerce_marketplace_ad_image_variants_candidate` | https://developer.ideogram.ai/ | real_generation_provider_agent | 电商/门店 | Ideogram API | `dry_run_payload_only` | `dry_run_only` | P1 | 广告合规、图片生成条款、不得投放 |
| 32 | `ecommerce_livecommerce_avatar_script_candidate` | https://docs.heygen.com/ | avatar_video_agent | 电商/门店 | HeyGen API | `dry_run_payload_only` | `dry_run_only` | P1 | 肖像授权、销售承诺、不得直播/发布 |
| 33 | `ecommerce_storefront_screenshot_audit_candidate` | https://github.com/microsoft/playwright | browser tool | 电商/门店 | 本地 browser | `local_screenshot_only` | `dry_run_only` | P2 | Playwright 许可证、只本地/授权页面、不得抓网页 |
| 34 | `ecommerce_inventory_photo_qc_candidate` | https://ai.google.dev/gemini-api/docs/image-understanding | vision_model_agent | 电商/门店 | vision API | `mock_image_payload_only` | `dry_run_only` | P1 | 视觉模型条款、图片上传、员工/顾客隐私 |
| 35 | `ecommerce_product_detail_page_generator_candidate` | https://github.com/nexu-io/open-design | OpenClaw-like skill pack | 电商/门店 | open-design 子 skill | `dry_run_metadata_only` | `dry_run_only` | P1 | 子 skill、是否写代码/截图、商品声明 |
| 36 | `metrics_video_daily_report_candidate` | https://www.remotion.dev/docs/ | programmatic_video_agent | 经营报表 | Remotion 本地 runtime | `dry_run_render_spec` | `dry_run_only` | P1 | Remotion 许可证、图表准确性、sandbox 输出 |
| 37 | `metrics_chart_image_generation_candidate` | https://quickchart.io/documentation/ | chart API/tool | 经营报表 | QuickChart/API 或本地替代 | `dry_run_chart_spec` | `dry_run_only` | P2 | QuickChart 条款、是否外传数据、可否本地渲染 |
| 38 | `metrics_anomaly_narrative_audio_candidate` | https://platform.openai.com/docs/guides/text-to-speech | audio_generation_agent | 经营报表 | TTS API | `dry_run_payload_only` | `dry_run_only` | P2 | TTS 条款、不得真实生成/发送、非财务建议 |
| 39 | `metrics_spreadsheet_agent_mcp_candidate` | https://github.com/modelcontextprotocol/servers | MCP/tool | 经营报表 | 本地 MCP | `mock_spreadsheet_only` | `mock_only` | P2 | MCP server 许可证、文件读取边界、只 mock 表格 |
| 40 | `metrics_forecast_scenario_simulator_candidate` | https://github.com/langchain-ai/langgraph | GitHub Agent/workflow | 经营报表 | 无 | `mock_only` | `skill_ready` | P2 | LangGraph 许可证、非财务建议、假设透明 |
| 41 | `hr_training_avatar_video_candidate` | https://docs.synthesia.io/ | avatar_video_agent | 行政/财务/HR | Synthesia API | `dry_run_payload_only` | `dry_run_only` | P0 | Synthesia 条款、员工制度人工审核、不得真实生成 |
| 42 | `hr_resume_interview_avatar_roleplay_candidate` | https://docs.heygen.com/ | avatar_video_agent | 行政/财务/HR | HeyGen API | `dry_run_payload_only` | `dry_run_only` | P1 | 不做录用建议、HeyGen 条款、候选人隐私 |
| 43 | `admin_policy_explainer_video_candidate` | https://ai.google.dev/gemini-api/docs/video | real_video_generation_agent | 行政/财务/HR | Veo/Gemini API | `dry_run_payload_only` | `dry_run_only` | P1 | 制度人工审核、视频 route、不得发布 |
| 44 | `finance_receipt_image_vision_extract_candidate` | https://ai.google.dev/gemini-api/docs/image-understanding | vision_model_agent | 行政/财务/HR | vision API | `mock_image_payload_only` | `dry_run_only` | P1 | 视觉模型条款、税务/报销非结论、图片存储 |
| 45 | `admin_document_ocr_to_sop_candidate` | https://github.com/PaddlePaddle/PaddleOCR | OCR/tool | 行政/财务/HR | OCR 本地/adapter | `mock_ocr_text_only` | `mock_only` | P2 | PaddleOCR 许可证、文档上传、只 mock OCR 文本 |
| 46 | `finance_invoice_approval_workflow_dryrun_candidate` | https://github.com/ComposioHQ/composio | MCP/SaaS connector | 行政/财务/HR | SaaS/OAuth | `dry_run_payload_only` | `dry_run_only` | P1 | Composio/OAuth、write_allowed=false、非审计结论 |
| 47 | `admin_meeting_to_slide_brief_candidate` | https://python-pptx.readthedocs.io/ | document_generation_tool | 行政/财务/HR | 本地 runtime | `dry_run_slide_spec` | `dry_run_only` | P2 | python-pptx 许可证、会议信息保密、不写真实 PPT |
| 48 | `admin_contract_clause_risk_mcp_candidate` | https://github.com/modelcontextprotocol/servers | MCP/tool | 行政/财务/HR | 本地 MCP | `mock_doc_text_only` | `mock_only` | P2 | MCP 许可证、非法律意见、真实文件读取边界 |
| 49 | `store_menu_poster_generation_candidate` | https://platform.openai.com/docs/guides/image-generation | real_generation_provider_agent | 电商/门店 | OpenAI/relay image API | `route_check_then_1_image_smoke` | `dry_run_only` | P0 | 价格准确性、字体/商标、图片 route 和费用 |
| 50 | `store_digital_signage_video_candidate` | https://www.remotion.dev/docs/ | programmatic_video_agent | 电商/门店 | Remotion 本地 runtime | `dry_run_render_spec` | `dry_run_only` | P1 | Remotion 许可证、价格/促销人工审核、sandbox 输出 |

## P0 优先复核清单

1. `marketing_real_poster_banner_agent_candidate`
2. `ecommerce_product_main_image_agent_candidate`
3. `marketing_short_video_ad_agent_candidate`
4. `ecommerce_product_video_from_image_candidate`
5. `sales_avatar_pitch_video_candidate`
6. `hr_training_avatar_video_candidate`
7. `ecommerce_background_replace_agent_candidate`
8. `store_menu_poster_generation_candidate`

## 禁止动作

- 不写稳交付库。
- 不写真实 API key。
- 不真实调用外部生成、发送、写入、抓取。
- 不生成真实图片、视频、音频、PPT。
- 不上传客户素材，不发布到任何平台，不写 CRM/店铺/广告/财务/HR 系统。
