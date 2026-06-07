# LICENSE_REVIEW_NEXT50_RESULT

回传日期：2026-06-05

## 1. 已完成事项

- 已读取 `RESEARCH_NEXT50_RESULT.md` 与 `queues/LICENSE_REVIEW_NEXT50_QUEUE.md`。
- 已对 50 个唯一 `candidate_id` 完成轻量 L1 / provider / trial mode 复核。
- 已覆盖旧的空阻塞结果。
- 已生成 `queues/DEEPAGENTS_SMOKE_NEXT50_QUEUE.md`。
- 本轮未安装、未运行项目、未调用 provider/API、未写 key、未生成图片/视频/音频/PPT、未上传素材、未写稳交付库。

## 2. 当前问题

- 图片/视频/音频/视觉模型类可以进入候选试跑，但真实 provider smoke 前仍需 route check、BYOK/密钥托管、计费、内容安全、版权/肖像/商标/素材授权验收。
- SaaS/OAuth/MCP/浏览器/文档生成类只能 dry-run 或 mock，不得写 CRM、Shopify、Figma、Canva、审批系统、文件系统或真实业务系统。
- `PyMuPDF` 存在 AGPL/商业授权风险；`open-design` 与 `modelcontextprotocol/servers` 属聚合来源，需定位具体子 skill/server 后再放行。

## 3. 阻塞原因

- 无工具/权限阻塞。
- 候选项级阻塞为 0。
- 需补资料项为 5，不进入 smoke，不进入正式 L2。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否将 45 个 L1 放行项交给测试台做 DeepAgents mock/dry-run/route-check smoke。
- 是否为 P0 真实图片/视频候选优先安排 provider route check：OpenAI image relay、Veo/Gemini video、Luma video、HeyGen、Synthesia。
- 是否要求研究窗口补充 5 个暂缓项的具体上游：PyMuPDF 商业授权替代方案、open-design 子 skill、MCP server 子项目。

## 5. 建议下一步

- 测试台只读取 `queues/DEEPAGENTS_SMOKE_NEXT50_QUEUE.md` 中 45 个放行项。
- 当前 smoke 仅允许 mock、dry-run、route check；不得真实生成媒体，除非后续指挥中心明确批准真实 provider smoke。
- 许可证不清或上游不明项不得送正式 L2。
- 本轮不新增稳交付 Skill，稳交付库仍按平台验收另行推进。

## 6. 数量汇总

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 10 |
| `can_dry_run_smoke` | 30 |
| `can_route_check` | 5 |
| `can_real_provider_smoke_later` | 0 |
| `component_only` | 0 |
| `needs_more_license_info` | 5 |
| `blocked` | 0 |

| 回传口径 | 数量 |
| --- | ---: |
| 通过，可进 DeepAgents smoke | 45 |
| 暂缓，需补许可证/上游/provider 条款 | 5 |
| 阻塞 | 0 |
| smoke 队列数量 | 45 |
| 可直接送正式 L2 | 0 |

## 7. 最高优先级

P0 优先做 route/dry-run smoke：

1. `marketing_real_poster_banner_agent_candidate`
2. `ecommerce_product_main_image_agent_candidate`
3. `marketing_short_video_ad_agent_candidate`
4. `ecommerce_product_video_from_image_candidate`
5. `sales_avatar_pitch_video_candidate`
6. `hr_training_avatar_video_candidate`
7. `ecommerce_background_replace_agent_candidate`
8. `store_menu_poster_generation_candidate`

## 8. L1 / Provider / Trial Mode 复核表

| # | candidate_id | source / provider | license / terms | 商用限制与维护状态 | 聚合/上游定位 | Provider/API/BYOK/中转站 | 真实生成与权利风险 | trial_mode | DeepAgents smoke | 正式 L2 | l1_result |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `support_voice_call_summary_agent_candidate` | OpenAI Whisper | MIT；模型/代码产品筛选可接受 | 活跃；音频转写涉及客户授权、存储、PII | 非聚合；上游清楚 | 摘要可走 OpenAI-compatible 文本中转；ASR 可本地/BYOK | 不上传真实录音；只用 mock transcript | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 2 | `support_training_microvideo_agent_candidate` | HeyGen API | 专有 SaaS terms，需 BYOK/条款复核 | 商用取决于 HeyGen 订阅与素材/头像授权 | 非聚合；provider 清楚 | 话术走文本中转；视频需 HeyGen key | 头像/声音/客户录音/费用/肖像权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 3 | `support_reply_multilingual_localizer_candidate` | openai-agents-python | MIT；产品筛选可接受 | 活跃；翻译准确性与政策边界需保留 | 非聚合；上游清楚 | 可直接走 OpenAI-compatible 文本中转 | 不自动发送客服回复 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 4 | `support_faq_video_answer_script_candidate` | Synthesia API | 专有 SaaS terms，需 BYOK/条款复核 | 商用取决于 Synthesia 订阅；FAQ 必须引用保真 | 非聚合；provider 清楚 | 脚本走文本中转；视频需 Synthesia key | 数字人、素材、发布权限、费用 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 5 | `support_ticket_auto_reply_quality_gate_candidate` | LangGraph | MIT；产品筛选可接受 | 活跃；只能做质检闸门，不得自动发送 | 非聚合；上游清楚 | 可走 OpenAI-compatible 文本中转 | false negative、转人工漏判 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 6 | `support_complaint_evidence_packet_candidate` | LlamaIndex | MIT；产品筛选可接受 | 活跃；仅 mock/read-only，非法律结论 | 非聚合；上游清楚 | 文本中转可用；RAG 本地 mock | 投诉资料 PII、法律升级风险 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 7 | `support_afterhours_triage_bot_candidate` | crewAI | MIT；产品筛选可接受 | 活跃；不得承诺即时处理或替代人工值班 | 非聚合；上游清楚 | 可走 OpenAI-compatible 文本中转 | 紧急事项误分流风险 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 8 | `sales_demo_video_brief_to_clip_candidate` | Runway API | 专有 API terms，需 BYOK/条款复核 | 商用取决于 Runway 订阅；产品效果不得夸大 | 非聚合；provider 清楚 | brief 走文本中转；视频需 Runway key | 素材授权、产品声明、费用 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 9 | `sales_avatar_pitch_video_candidate` | HeyGen API | 专有 SaaS terms，需 BYOK/条款复核 | 商用取决于 HeyGen；不得真实外发 | 非聚合；provider 清楚 | 文本中转生成话术；视频需 HeyGen key | 肖像/声音授权、销售承诺、发送风险 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 10 | `sales_proposal_deck_generator_candidate` | python-pptx | MIT；产品筛选可接受 | 维护稳定；本轮只输出 slide spec，不写真实 PPT | 非聚合；上游清楚 | 文本中转生成结构；本地库后续单独验收 | 文件写入、品牌素材、客户方案保密 | `dry_run_only`, `read_only`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 11 | `sales_call_roleplay_coach_candidate` | openai-agents-python | MIT；产品筛选可接受 | 活跃；训练用途，不当作真实客户反馈 | 非聚合；上游清楚 | 可走 OpenAI-compatible 文本中转 | 虚构客户反馈需标明 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 12 | `sales_contract_redline_summary_candidate` | Unstructured | Apache-2.0；产品筛选可接受 | 活跃；非法律意见，不读真实合同 | 非聚合；上游清楚 | 文本中转可摘要；文档解析 mock text | 合同/法律风险、真实文件读取边界 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 13 | `sales_crm_next_best_action_candidate` | Composio | MIT SDK；SaaS/OAuth terms 需边界 | 活跃；write_allowed=false，只能 dry-run | 非聚合；上游清楚 | 文本中转可推理；CRM/OAuth BYOK | CRM 写入、邮件/任务动作风险 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 14 | `sales_quote_pdf_brief_candidate` | PyMuPDF | AGPL/commercial 双轨风险；需商业授权或替代库 | 维护活跃但 AGPL 不适合直接平台托管分发 | 非聚合；上游清楚但许可高风险 | 文本中转可摘要；PDF 解析依赖需替换/授权 | 报价文件保密、自动发送风险 | `mock_only`, `read_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 15 | `marketing_real_poster_banner_agent_candidate` | OpenAI image API / relay | OpenAI API terms；需平台条款与内容政策验收 | provider 活跃；商用取决于平台 API terms 与费用 | 非聚合；provider 清楚 | 优先走 OpenAI-compatible 图片中转 route check | 版权、商标、素材授权、输出审计 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 16 | `marketing_text_overlay_poster_candidate` | Ideogram API | 专有 API terms，需 BYOK/条款复核 | 商用取决于 Ideogram 订阅；中文文字质量需测 | 非聚合；provider 清楚 | 文本中转生成 prompt；出图需 Ideogram/relay | 字体、商标、中文文字、版权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 17 | `marketing_brand_asset_generator_candidate` | Recraft API | 专有 API terms，需 BYOK/条款复核 | 商用取决于 Recraft；不得声明版权清白 | 非聚合；provider 清楚 | 文本中转生成 prompt；出图需 Recraft | 品牌资产、图标、商标、授权证明 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 18 | `marketing_short_video_ad_agent_candidate` | Google Veo/Gemini video | Google API terms；需 route/费用/内容安全验收 | provider 活跃；视频生成费用和下载轮询需测 | 非聚合；provider 清楚 | 走 OpenAI-compatible 或 Gemini relay route check | 广告声明、版权、商标、素材授权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 19 | `marketing_social_carousel_image_agent_candidate` | open-design | Apache-2.0 仓库；子 skill 需单独定位 | open-design 是大型 skill pack，不能整仓放行 | 聚合；具体子目录未定位 | 需定位 child skill/API 依赖后再评估 | 导出、截图、文件写入、图片 provider | `dry_run_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 20 | `marketing_product_launch_video_script_to_render_candidate` | Remotion | Remotion 商用/企业授权需补核；可先只做 render spec | 维护活跃；本轮不安装、不渲染 | 非聚合；上游清楚 | 文本中转生成 spec；本地 runtime 后续验收 | 文件写入、素材授权、渲染成本 | `dry_run_only`, `read_only`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 21 | `marketing_ad_creative_batch_generator_candidate` | fal.ai | 专有 provider terms；多模型许可证需逐模型复核 | provider 活跃；批量生成需费用上限 | 非聚合 provider，但模型级条款复杂 | 文本中转或 fal BYOK；当前只 payload | 多模型商用、广告合规、费用爆发 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 22 | `marketing_thumbnail_generator_candidate` | Stability API | Stability API/model terms 需复核 | provider 活跃；商用取决于模型/API terms | 非聚合；provider 清楚 | 文本中转生成 prompt；出图需 Stability | 素材授权、封面误导、版权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 23 | `marketing_figma_banner_spec_candidate` | Figma API | Figma developer/API terms；需 OAuth/BYOK | SaaS 活跃；write_allowed=false | 非聚合；provider 清楚 | 文本中转生成 spec；Figma API dry-run payload | 品牌资源、设计写入、OAuth | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 24 | `marketing_canva_template_brief_candidate` | Canva API | Canva developer/API terms；需 BYOK/条款复核 | SaaS 活跃；不创建/导出真实设计 | 非聚合；provider 清楚 | 文本中转生成 brief/payload；Canva dry-run | 模板授权、导出、素材版权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 25 | `ecommerce_product_main_image_agent_candidate` | OpenAI image API / relay | OpenAI API terms；需平台条款与内容政策验收 | provider 活跃；商用取决于 API terms 与费用 | 非聚合；provider 清楚 | 优先走 OpenAI-compatible 图片中转 route check | 商品真实性、商标、版权、成本 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 26 | `ecommerce_background_replace_agent_candidate` | fal.ai image edit | fal terms；输入素材上传/存储需复核 | provider 活跃；真实编辑需用户素材授权 | 非聚合；provider 清楚 | 文本中转生成 edit payload；fal/relay 后续 | 商品图授权、上传存储、编辑模型条款 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 27 | `ecommerce_tryon_model_image_candidate` | fal.ai try-on | fal/model terms；肖像/生物特征高风险 | provider 活跃；不得用真实客户照片 | 非聚合；provider 清楚 | 当前只 dry-run payload；后续 BYOK | 肖像权、服装图授权、模特授权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 28 | `ecommerce_product_video_from_image_candidate` | Luma API | Luma API terms；需 BYOK/费用/下载复核 | provider 活跃；图生视频需素材授权 | 非聚合；provider 清楚 | Luma/relay route check | 素材授权、下载 URL、成本、商标 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 29 | `ecommerce_review_to_product_image_prompt_candidate` | openai-agents-python | MIT；产品筛选可接受 | 活跃；评价脱敏，不得生成虚假卖点 | 非聚合；上游清楚 | 可走 OpenAI-compatible 文本中转 | 评论偏差、虚假宣传 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 30 | `ecommerce_shopify_listing_asset_dryrun_candidate` | Shopify API | Shopify developer/API terms；需 OAuth/BYOK | SaaS 活跃；write_allowed=false，不上传素材 | 非聚合；provider 清楚 | 文本中转生成 payload；Shopify dry-run | 店铺写入、OAuth、商品声明 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 31 | `ecommerce_marketplace_ad_image_variants_candidate` | Ideogram API | 专有 API terms，需 BYOK/条款复核 | provider 活跃；不投放广告 | 非聚合；provider 清楚 | 文本中转生成 prompt；出图需 Ideogram | 广告合规、商标、图片权利 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 32 | `ecommerce_livecommerce_avatar_script_candidate` | HeyGen API | HeyGen terms；需 BYOK/肖像授权 | provider 活跃；不得直播/发布 | 非聚合；provider 清楚 | 文本中转脚本；HeyGen payload dry-run | 肖像/声音、价格承诺、销售合规 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 33 | `ecommerce_storefront_screenshot_audit_candidate` | Playwright | Apache-2.0；产品筛选可接受 | 活跃；只可本地/授权页面，不抓取业务网页 | 非聚合；上游清楚 | 文本中转分析；本地 browser 后续验收 | 截图、网站 ToS、隐私 | `dry_run_only`, `read_only`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 34 | `ecommerce_inventory_photo_qc_candidate` | Gemini vision/image understanding | Google API terms；需图片上传/存储复核 | provider 活跃；不得上传真实员工/顾客照片 | 非聚合；provider 清楚 | 视觉 API route/BYOK；当前 mock image payload | 图片隐私、货架/员工/顾客信息 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 35 | `ecommerce_product_detail_page_generator_candidate` | open-design | Apache-2.0 仓库；子 skill 需单独定位 | open-design 是大型 skill pack，不能整仓放行 | 聚合；具体子 skill 未定位 | 需定位 child skill/manifest/API 依赖 | 写代码/截图/导出、商品声明 | `dry_run_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 36 | `metrics_video_daily_report_candidate` | Remotion | Remotion 商用/企业授权需补核；可先 dry-run spec | 维护活跃；不渲染真实视频 | 非聚合；上游清楚 | 文本中转生成 render spec；本地 runtime 后续验收 | 图表准确性、文件输出、指标隐私 | `dry_run_only`, `read_only`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 37 | `metrics_chart_image_generation_candidate` | QuickChart | QuickChart service/open-source terms 需补核；可先 chart spec | 维护可用；优先考虑本地渲染替代 | 非聚合；provider 清楚 | 文本中转生成 chart spec；API/BYOK 后续 | 外传经营数据、图表准确性 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 38 | `metrics_anomaly_narrative_audio_candidate` | OpenAI TTS | OpenAI API terms；需 route/费用/音频输出验收 | provider 活跃；非财务建议，不发送音频 | 非聚合；provider 清楚 | 文本中转生成讲稿；TTS route 后续 | 语音生成、财务建议边界 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 39 | `metrics_spreadsheet_agent_mcp_candidate` | modelcontextprotocol/servers | 聚合仓库，server 许可证需逐项定位 | MCP 服务器众多，不能按整仓放行 | 聚合；具体 server 未定位 | 需定位 spreadsheet/file server 后再复核 | 文件读取、表格隐私、数据质量 | `mock_only`, `read_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 40 | `metrics_forecast_scenario_simulator_candidate` | LangGraph | MIT；产品筛选可接受 | 活跃；非财务建议，假设必须透明 | 非聚合；上游清楚 | 可走 OpenAI-compatible 文本中转 | 预测被误当财务建议 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 41 | `hr_training_avatar_video_candidate` | Synthesia API | Synthesia terms；需 BYOK/条款复核 | provider 活跃；员工制度需人工审核 | 非聚合；provider 清楚 | 文本中转生成脚本；视频需 Synthesia key | 数字人授权、员工政策、费用 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 42 | `hr_resume_interview_avatar_roleplay_candidate` | HeyGen API | HeyGen terms；需 BYOK/条款复核 | provider 活跃；不得做录用/淘汰建议 | 非聚合；provider 清楚 | 文本中转生成脚本；HeyGen payload dry-run | 候选人隐私、招聘偏见、肖像授权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 43 | `admin_policy_explainer_video_candidate` | Google Veo/Gemini video | Google API terms；需 route/费用/内容安全验收 | provider 活跃；制度内容需人工审核 | 非聚合；provider 清楚 | 文本中转生成脚本；Veo/Gemini route 后续 | 政策准确性、视频发布风险 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 44 | `finance_receipt_image_vision_extract_candidate` | Gemini vision/image understanding | Google API terms；图片上传/存储需复核 | provider 活跃；非税务/报销/审计结论 | 非聚合；provider 清楚 | 视觉 API route/BYOK；当前 mock image payload | 票据隐私、财税边界、图片存储 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 45 | `admin_document_ocr_to_sop_candidate` | PaddleOCR | Apache-2.0；模型权重需锁定官方可商用版本 | 活跃；只 mock OCR text，不上传文档 | 非聚合；上游清楚 | 文本中转整理 SOP；OCR 本地后续验收 | 文档隐私、OCR 模型权重 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 46 | `finance_invoice_approval_workflow_dryrun_candidate` | Composio | MIT SDK；SaaS/OAuth terms 需边界 | 活跃；write_allowed=false，非审计结论 | 非聚合；上游清楚 | 文本中转可判断；审批系统 adapter dry-run | 财务写入、审批误导、OAuth | `dry_run_only`, `BYOK_required`, `provider_api_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 47 | `admin_meeting_to_slide_brief_candidate` | python-pptx | MIT；产品筛选可接受 | 维护稳定；只输出 slide spec，不写真实 PPT | 非聚合；上游清楚 | 文本中转生成 slide spec；本地库后续验收 | 会议保密、文件写入 | `dry_run_only`, `read_only`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 48 | `admin_contract_clause_risk_mcp_candidate` | modelcontextprotocol/servers | 聚合仓库，server 许可证需逐项定位 | MCP 服务器众多，不能按整仓放行 | 聚合；具体 server 未定位 | 需定位 file/doc MCP server 后再复核 | 非法律意见、文件读取、合同隐私 | `mock_only`, `read_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 49 | `store_menu_poster_generation_candidate` | OpenAI image API / relay | OpenAI API terms；需平台条款与内容政策验收 | provider 活跃；价格/字体/商标需人工确认 | 非聚合；provider 清楚 | OpenAI-compatible 图片中转 route check | 价格准确性、字体/商标、版权 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 50 | `store_digital_signage_video_candidate` | Remotion | Remotion 商用/企业授权需补核；可先 dry-run spec | 维护活跃；不渲染真实视频 | 非聚合；上游清楚 | 文本中转生成 render spec；本地 runtime 后续验收 | 价格/促销人工审核、文件输出 | `dry_run_only`, `read_only`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
