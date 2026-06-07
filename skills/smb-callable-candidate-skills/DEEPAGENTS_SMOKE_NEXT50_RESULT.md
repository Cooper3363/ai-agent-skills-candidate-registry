# DEEPAGENTS_SMOKE_NEXT50_RESULT

回传对象：AI.Skills 指挥中心  
执行日期：2026-06-05  
输入队列：`queues/DEEPAGENTS_SMOKE_NEXT50_QUEUE.md`  
执行方式：候选级 metadata/mock/dry-run/route-check smoke。未触发真实 provider/API、未写入 key、未上传素材、未生成真实图片/视频/音频/PPT/OCR/PDF。

## 1. 已完成事项

- 已读取覆盖后的 `LICENSE_REVIEW_NEXT50_RESULT.md` 与 `queues/DEEPAGENTS_SMOKE_NEXT50_QUEUE.md`。
- 已确认本轮 smoke 队列包含 45 个 L1/trial mode 放行候选：`can_mock_smoke=10`、`can_dry_run_smoke=30`、`can_route_check=5`。
- 已对 45 个候选逐一执行至少 1 个中文中小微六部门 mock/dry-run/route-check 场景检查。
- 已检查：能否表达为 callable Skill/Agent、是否适配 OpenAI-compatible 中转站模型通道、输出结构是否稳定、权限边界是否明确、人工复核触发是否清楚、与稳交付 13 个 Skill 是否重复。
- 已从 passed 候选中筛选 Top15，写入 `queues/L2_OFFICIAL_TOP15_FROM_NEXT50_QUEUE.md`。

## 2. 当前问题

- 媒体生成类当前只通过 route/config/payload smoke，不能写成真实 provider 通过。
- SaaS/OAuth/API 写入类当前只通过 dry-run payload smoke，不能写成真实系统动作通过。
- 本轮不新增客户正式可调用 Skill，稳交付库仍为 13。

## 3. 阻塞原因

- 无权限阻塞。
- 无 candidate 级 blocked。
- 5 个 L1 暂缓项未进入本 smoke 队列，因此未测试。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Top15 进入正式 L2 simulated。
- 是否为媒体生成类另开真实 provider smoke 计划，包括 BYOK/key 托管、费用上限、内容安全、版权/肖像/商标/素材授权验收。

## 5. 建议下一步

- 指挥中心可派发 Top15 正式 L2 simulated；每个候选至少 3 个中文业务 mock 用例。
- 媒体类在正式 L2 仍默认 mock/dry-run/route-check，不做真实生成；如需真实 provider smoke，必须单独派发。
- 其余 30 个 passed 候选保留在候选库观察池，等待后续业务包补位。

## 6. Smoke 数量汇总

| deepagents_smoke_status | 数量 |
| --- | ---: |
| passed | 45 |
| failed | 0 |
| needs_fix | 0 |
| blocked | 0 |

## 7. Top15 正式 L2 推荐队列

| 排名 | candidate_id | 优先理由 | smoke 类型 | 正式 L2 重点 |
| ---: | --- | --- | --- | --- |
| 1 | `marketing_real_poster_banner_agent_candidate` | 海报/banner P0，高频中小微营销场景 | route-check | OpenAI image relay route/payload、版权/商标/素材边界 |
| 2 | `ecommerce_product_main_image_agent_candidate` | 商品主图 P0，电商高频刚需 | route-check | 商品真实性、主图 prompt/payload、不得真实生成 |
| 3 | `marketing_short_video_ad_agent_candidate` | 短视频广告 P0，高价值但需强边界 | route-check | Veo/Gemini route/payload、广告合规、素材授权 |
| 4 | `ecommerce_product_video_from_image_candidate` | 商品图生视频 P0，电商高价值 | route-check | Luma route/payload、图片授权、不得生成视频 |
| 5 | `sales_avatar_pitch_video_candidate` | 销售数字人口播 P0，高演示价值 | dry-run | 数字人口播脚本/payload、肖像/声音授权 |
| 6 | `hr_training_avatar_video_candidate` | HR 培训数字人 P0，内部培训高频 | dry-run | 培训脚本/payload、员工政策复核 |
| 7 | `ecommerce_background_replace_agent_candidate` | 商品图背景替换 P0，电商高频 | dry-run | edit payload、商品图授权、不上传素材 |
| 8 | `store_menu_poster_generation_candidate` | 门店菜单海报 P0，本地商家高频 | route-check | 菜单价格准确、字体/商标/图片边界 |
| 9 | `support_ticket_auto_reply_quality_gate_candidate` | 客服低风险高频，文本稳定 | mock | 自动回复质检、违规拦截、转人工 |
| 10 | `support_complaint_evidence_packet_candidate` | 客服投诉材料整理，高风险但只读 | mock | 投诉证据包、PII 脱敏、非法律结论 |
| 11 | `support_afterhours_triage_bot_candidate` | 下班后分流高频，低写入风险 | mock | 紧急度分流、不可承诺即时处理 |
| 12 | `support_voice_call_summary_agent_candidate` | 客服通话摘要高频，mock transcript 可测 | mock | 摘要、行动项、PII/授权边界 |
| 13 | `sales_crm_next_best_action_candidate` | 销售跟进高频，dry-run 可控 | dry-run | CRM next action payload、write_allowed=false |
| 14 | `sales_call_roleplay_coach_candidate` | 销售培训低风险高频 | mock | 角色扮演反馈、不可冒充真实客户 |
| 15 | `metrics_forecast_scenario_simulator_candidate` | 经营报表低风险高频，文本稳定 | mock | 情景假设、非财务建议、数据口径 |

## 8. Smoke 明细

| # | candidate_id | smoke 用例摘要 | callable_fit | model_route_fit | expected_inputs | expected_outputs | permission_boundary | manual_review_triggers | blocked_actions | deepagents_smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `support_voice_call_summary_agent_candidate` | 客服主管粘贴一段 mock 售后通话转写，要求生成摘要和待办。 | 可表达为 `call_summary_agent` | 文本摘要可走 OpenAI-compatible 中转；不做真实 ASR | `transcript_text`, `customer_context`, `language` | `call_summary`, `customer_issue`, `action_items`, `risk_flags`, `manual_review_required` | 只用 mock transcript；不上传真实音频 | PII、退款承诺、投诉升级、低置信 | 上传真实音频、联系客户、写工单 | passed |
| 2 | `support_training_microvideo_agent_candidate` | 客服培训负责人输入“如何处理退款投诉”的培训目标，生成 HeyGen dry-run payload。 | 可表达为 `training_microvideo_payload_builder` | 脚本文本走中转；视频 provider 禁用 | `training_topic`, `audience`, `duration`, `style` | `script_outline`, `scene_plan`, `provider_payload`, `risk_notes`, `external_action_blocked` | 不生成视频；不写 key；不使用真人肖像 | 员工政策、肖像/声音授权、投诉规则 | 调 HeyGen、生成视频、上传素材 | passed |
| 3 | `support_reply_multilingual_localizer_candidate` | 客服主管把中文退款安抚话术本地化为英文/越南语版本。 | 可表达为 `support_reply_localizer` | 文本中转适配 | `source_reply`, `target_locale`, `policy_notes` | `localized_reply`, `tone_notes`, `policy_boundary`, `risk_flags` | 不发送客服回复 | 翻译低置信、政策差异、投诉退款 | 发送消息、改变政策承诺 | passed |
| 4 | `support_faq_video_answer_script_candidate` | 将“发票申请规则”FAQ 转为数字人视频脚本 payload。 | 可表达为 `faq_video_script_payload` | FAQ 脚本走文本中转；Synthesia 禁用 | `faq_answer`, `citations`, `video_style` | `script`, `scene_notes`, `provider_payload`, `citation_notes` | 不生成视频、不上传素材 | FAQ 无引用、政策敏感、素材授权 | 调 Synthesia、发布视频 | passed |
| 5 | `support_ticket_auto_reply_quality_gate_candidate` | 检查一段客服自动回复是否越权承诺退款。 | 可表达为 `auto_reply_quality_gate` | 文本质检中转适配 | `ticket_text`, `draft_reply`, `policy_snippets` | `pass_gate`, `violations`, `rewrite_suggestions`, `handoff_required` | 不发送、不写客服系统 | 退款、赔偿、账号安全、投诉 | 自动发送、修改工单 | passed |
| 6 | `support_complaint_evidence_packet_candidate` | 用 mock 投诉文本整理内部证据包。 | 可表达为 `complaint_evidence_packet` | 文本/RAG mock 中转适配 | `complaint_text`, `order_notes`, `policy_refs` | `evidence_packet`, `timeline`, `missing_evidence`, `risk_flags` | 只读 mock 文本；非法律结论 | 监管投诉、赔偿、PII、证据缺口 | 生成法律结论、上传文件、联系客户 | passed |
| 7 | `support_afterhours_triage_bot_candidate` | 夜间客户留言“账号被盗+要求退款”，输出分流建议。 | 可表达为 `afterhours_triage` | 文本中转适配 | `message`, `business_hours`, `triage_rules` | `urgency`, `route_to`, `safe_reply`, `handoff_required` | 不承诺即时处理；不写系统 | 账号安全、退款、投诉、生命安全类异常 | 自动派单、承诺处理、发送消息 | passed |
| 8 | `sales_demo_video_brief_to_clip_candidate` | 销售输入产品演示亮点，生成 Runway 视频 brief/payload。 | 可表达为 `demo_video_payload_builder` | brief 文本中转；Runway provider 禁用 | `demo_points`, `audience`, `visual_style` | `video_brief`, `scene_list`, `provider_payload`, `rights_notes` | 不生成视频；不上传素材 | 产品能力承诺、素材授权、商标 | 调 Runway、生成视频、发布 | passed |
| 9 | `sales_avatar_pitch_video_candidate` | 销售为门店 SaaS 生成 60 秒数字人口播 dry-run payload。 | 可表达为 `avatar_pitch_payload` | 话术文本中转；HeyGen 禁用 | `product_pitch`, `persona`, `cta`, `language` | `pitch_script`, `avatar_payload`, `claim_risks`, `send_allowed=false` | 不生成数字人视频、不发送 | 肖像/声音授权、销售承诺、折扣 | 调 HeyGen、发送外呼、上传头像 | passed |
| 10 | `sales_proposal_deck_generator_candidate` | 售前根据客户需求生成 proposal slide spec。 | 可表达为 `proposal_deck_spec_builder` | 文本结构化中转适配 | `requirements`, `solution_points`, `brand_notes` | `slide_outline`, `speaker_notes`, `asset_list`, `not_contract` | 不写 PPT 文件 | 报价、合同、品牌素材、客户保密 | 生成真实 PPT、外发方案 | passed |
| 11 | `sales_call_roleplay_coach_candidate` | 新销售练习“价格太贵”异议处理，输出教练反馈。 | 可表达为 `sales_roleplay_coach` | 文本角色扮演中转适配 | `scenario`, `rep_response`, `rubric` | `coach_feedback`, `score_breakdown`, `better_response`, `practice_next` | 不冒充真实客户 | 折扣越权、攻击竞品、虚构承诺 | 写 CRM、联系客户、发送话术 | passed |
| 12 | `sales_contract_redline_summary_candidate` | 用 mock 合同条款摘要付款和违约风险。 | 可表达为 `contract_redline_summary` | mock 合同文本中转适配 | `contract_text`, `focus_areas` | `risk_summary`, `clause_refs`, `questions_for_legal`, `not_legal_advice` | 不读真实合同；非法律意见 | 合同金额、违约、付款、保密 | 给法律结论、修改合同 | passed |
| 13 | `sales_crm_next_best_action_candidate` | 根据 mock CRM 记录生成下一步动作 dry-run payload。 | 可表达为 `crm_next_best_action_payload` | 推理走中转；CRM API 禁用 | `crm_notes`, `deal_stage`, `constraints` | `next_action`, `crm_payload`, `write_allowed=false`, `risk_flags` | 不写 CRM；不触发 OAuth | 客户拒绝、价格、合同、退订 | 写 CRM、创建任务、发邮件 | passed |
| 14 | `marketing_real_poster_banner_agent_candidate` | 为社区生鲜店草莓促销生成 OpenAI image relay route/payload。 | 可表达为 `poster_banner_route_payload` | route/config/payload 可走 OpenAI-compatible image relay；不真实出图 | `campaign_goal`, `copy`, `visual_style`, `size` | `route_check`, `image_prompt`, `provider_payload`, `rights_notes` | 不写 key、不生成图片、不上传素材 | 商标、版权、价格、绝对化用语 | 调 provider、生成图片、发布 | passed |
| 15 | `marketing_text_overlay_poster_candidate` | 为瑜伽体验课生成中文文字海报 payload。 | 可表达为 `text_overlay_poster_payload` | 文案中转；Ideogram 禁用 | `poster_copy`, `layout_notes`, `brand_style` | `prompt`, `text_overlay_spec`, `provider_payload`, `font_risks` | 不生成图片 | 字体版权、医疗/健康承诺、价格 | 调 Ideogram、导出图片 | passed |
| 16 | `marketing_brand_asset_generator_candidate` | 为新门店生成品牌图标/色彩方向 dry-run payload。 | 可表达为 `brand_asset_payload` | prompt 中转；Recraft 禁用 | `brand_description`, `asset_type`, `style_constraints` | `asset_brief`, `prompt`, `provider_payload`, `trademark_risks` | 不生成品牌资产 | 商标近似、版权、品牌授权 | 调 Recraft、注册/声明商标 | passed |
| 17 | `marketing_short_video_ad_agent_candidate` | 为本地咖啡店新品生成 15 秒短视频广告 route/payload。 | 可表达为 `short_video_ad_route_payload` | Veo/Gemini route-check；不生成视频 | `product`, `offer`, `audience`, `visual_style` | `video_prompt`, `scene_plan`, `route_check`, `provider_payload` | 不生成视频、不上传素材 | 广告法、音乐/人物/商标授权 | 调 Veo/Gemini、发布广告 | passed |
| 18 | `marketing_product_launch_video_script_to_render_candidate` | 为新品发布生成 Remotion render spec。 | 可表达为 `launch_video_render_spec` | 文本中转生成 spec；不 render | `launch_message`, `assets_available`, `duration` | `render_spec`, `timeline`, `asset_requirements`, `risk_notes` | 不渲染、不写文件 | 素材授权、产品承诺、价格 | 执行 Remotion、生成视频 | passed |
| 19 | `marketing_ad_creative_batch_generator_candidate` | 为同一活动批量生成 5 组广告图 payload。 | 可表达为 `ad_creative_batch_payload` | 文案/prompt 中转；fal 禁用 | `campaign`, `variants`, `platform_rules` | `variant_payloads`, `claims_to_review`, `cost_warning` | 不生成图片、不批量调用 | 费用爆炸、广告合规、版权 | 调 fal、投放广告 | passed |
| 20 | `marketing_thumbnail_generator_candidate` | 为 B 站教程视频生成封面 prompt/payload。 | 可表达为 `thumbnail_payload` | prompt 中转；Stability 禁用 | `video_topic`, `target_viewer`, `thumbnail_style` | `thumbnail_prompt`, `composition`, `provider_payload`, `risk_notes` | 不生成封面 | 肖像、误导点击、版权 | 调 Stability、导出图片 | passed |
| 21 | `marketing_figma_banner_spec_candidate` | 为 618 活动生成 Figma banner spec dry-run。 | 可表达为 `figma_banner_spec_payload` | 文本中转；Figma API 禁用 | `campaign_info`, `brand_tokens`, `dimensions` | `figma_spec`, `layer_plan`, `api_payload`, `write_allowed=false` | 不写 Figma | 品牌资产、价格、OAuth | 写 Figma、导出设计 | passed |
| 22 | `marketing_canva_template_brief_candidate` | 为门店会员日生成 Canva 模板 brief/payload。 | 可表达为 `canva_template_brief_payload` | 文本中转；Canva API 禁用 | `event`, `template_type`, `brand_notes` | `template_brief`, `asset_slots`, `api_payload`, `write_allowed=false` | 不创建 Canva 设计 | 模板授权、素材版权、价格 | 调 Canva、导出文件 | passed |
| 23 | `ecommerce_product_main_image_agent_candidate` | 为保温杯商品主图生成 OpenAI image relay route/payload。 | 可表达为 `product_main_image_route_payload` | image relay route-check；不真实出图 | `product_info`, `platform_rules`, `visual_style` | `main_image_prompt`, `route_check`, `provider_payload`, `compliance_notes` | 不生成图片、不上传商品图 | 商品真实性、商标、平台规则 | 调 provider、改商品图 | passed |
| 24 | `ecommerce_background_replace_agent_candidate` | 为鞋类商品图生成背景替换 edit payload。 | 可表达为 `background_replace_payload` | 文本/配置中转；fal edit 禁用 | `product_description`, `background_goal`, `image_ref_placeholder` | `edit_prompt`, `mask_notes`, `provider_payload`, `rights_notes` | 不上传图片、不生成结果 | 商品图授权、误导性场景 | 上传素材、调用编辑模型 | passed |
| 25 | `ecommerce_tryon_model_image_candidate` | 为服装生成虚拟试穿 payload，但不使用真人照片。 | 可表达为 `tryon_payload_builder` | payload 中转；try-on provider 禁用 | `garment_info`, `model_profile`, `usage_context` | `tryon_prompt`, `provider_payload`, `consent_notes`, `risk_flags` | 不用真实客户照 | 肖像权、服装图授权、身材敏感 | 上传真人照、生成试穿图 | passed |
| 26 | `ecommerce_product_video_from_image_candidate` | 为小家电商品图生成 Luma 图生视频 route/payload。 | 可表达为 `product_image_to_video_route_payload` | Luma route-check；不生成视频 | `product_info`, `image_ref_placeholder`, `motion_goal` | `video_prompt`, `route_check`, `provider_payload`, `rights_notes` | 不上传图片、不生成视频 | 素材授权、商标、成本 | 调 Luma、下载视频 | passed |
| 27 | `ecommerce_review_to_product_image_prompt_candidate` | 从授权评价中提炼商品图 prompt。 | 可表达为 `review_to_image_prompt` | 文本中转适配 | `reviews`, `product_info`, `claim_rules` | `image_angles`, `prompt_options`, `claims_to_avoid`, `risk_flags` | 不生成图片 | UGC 授权、夸大卖点、虚假宣传 | 使用未授权评价、出图 | passed |
| 28 | `ecommerce_shopify_listing_asset_dryrun_candidate` | 生成 Shopify listing asset dry-run payload。 | 可表达为 `shopify_listing_asset_payload` | 文本中转；Shopify API 禁用 | `product_data`, `media_plan`, `platform_constraints` | `listing_payload`, `asset_requirements`, `write_allowed=false`, `risk_flags` | 不写 Shopify、不上传素材 | 商品声明、库存、价格 | 写 Shopify、发布商品 | passed |
| 29 | `ecommerce_marketplace_ad_image_variants_candidate` | 为电商平台广告图生成 3 个 prompt/payload。 | 可表达为 `marketplace_ad_image_payloads` | prompt 中转；Ideogram 禁用 | `product`, `campaign`, `platform_rules` | `variant_prompts`, `provider_payloads`, `compliance_notes` | 不生成广告图、不投放 | 平台规则、商标、效果承诺 | 调 provider、投放广告 | passed |
| 30 | `ecommerce_livecommerce_avatar_script_candidate` | 为直播带货生成数字人口播脚本/payload。 | 可表达为 `livecommerce_avatar_payload` | 文本中转；HeyGen 禁用 | `product`, `offer`, `host_persona` | `live_script`, `avatar_payload`, `claim_risks`, `rights_notes` | 不生成直播视频 | 价格、功效、肖像声音授权 | 调 HeyGen、开播/发布 | passed |
| 31 | `ecommerce_storefront_screenshot_audit_candidate` | 对授权本地截图做店铺首页问题审计。 | 可表达为 `storefront_screenshot_audit` | 文本中转；截图读取后续单独验收 | `screenshot_notes`, `audit_goal`, `platform_context` | `audit_findings`, `priority_fixes`, `risk_notes`, `manual_review_required` | 不抓网页；只用授权/本地截图描述 | 隐私、平台 ToS、误判 | 真实抓取、登录、截图线上店铺 | passed |
| 32 | `ecommerce_inventory_photo_qc_candidate` | 用 mock image payload 检查货架照片 QC 路径。 | 可表达为 `inventory_photo_qc_payload` | vision route/dry-run；Gemini API 禁用 | `image_placeholder`, `qc_rules`, `store_context` | `vision_payload`, `qc_checklist`, `risk_flags`, `manual_review_required` | 不上传真实照片 | 员工/顾客入镜、库存误判 | 调 vision API、上传图片 | passed |
| 33 | `metrics_video_daily_report_candidate` | 根据门店日报生成视频日报 Remotion spec。 | 可表达为 `video_daily_report_spec` | 文本中转生成 spec；不 render | `daily_metrics`, `narrative_style`, `chart_needs` | `render_spec`, `scene_timeline`, `chart_specs`, `risk_notes` | 不生成视频文件 | 财务数据、口径、缺失值 | 渲染视频、写文件 | passed |
| 34 | `metrics_chart_image_generation_candidate` | 根据销售数据生成 chart spec/payload。 | 可表达为 `chart_image_spec_payload` | 文本中转；外部 chart API 禁用 | `metric_table`, `chart_goal`, `audience` | `chart_spec`, `data_quality_notes`, `provider_payload`, `risk_flags` | 不外传经营数据 | 数据口径、财务敏感、图表误导 | 调外部图表 API、生成图片 | passed |
| 35 | `metrics_anomaly_narrative_audio_candidate` | 将支付成功率异常说明转为 TTS payload。 | 可表达为 `anomaly_audio_payload` | 文本中转；TTS route 后续验收 | `anomaly_summary`, `audience`, `tone` | `narration_script`, `tts_payload`, `risk_flags`, `not_financial_advice` | 不生成音频、不发送 | 财务建议、故障责任归因 | 调 TTS、发送音频 | passed |
| 36 | `metrics_forecast_scenario_simulator_candidate` | 门店输入客流/客单价假设，输出三种经营情景。 | 可表达为 `forecast_scenario_simulator` | 文本中转适配 | `baseline_metrics`, `assumptions`, `scenario_count` | `scenarios`, `assumptions`, `sensitivity_notes`, `not_financial_advice` | 只做模拟，不做财务建议 | 数据缺失、重大经营决策 | 给投资/融资/税务建议 | passed |
| 37 | `hr_training_avatar_video_candidate` | HR 输入新员工服务规范，生成 Synthesia 培训视频 payload。 | 可表达为 `hr_training_avatar_payload` | 脚本文本中转；Synthesia 禁用 | `training_policy`, `audience`, `duration`, `avatar_style` | `training_script`, `scene_plan`, `provider_payload`, `review_notes` | 不生成视频、不上传员工素材 | 制度准确、员工隐私、肖像授权 | 调 Synthesia、发布培训 | passed |
| 38 | `hr_resume_interview_avatar_roleplay_candidate` | 招聘主管生成面试角色扮演脚本/payload。 | 可表达为 `interview_avatar_roleplay_payload` | 文本中转；HeyGen 禁用 | `job_role`, `competency_focus`, `scenario` | `roleplay_script`, `question_set`, `provider_payload`, `fairness_notes` | 不做录用/淘汰建议 | 招聘公平、PII、偏见 | 调 HeyGen、评价候选人结论 | passed |
| 39 | `admin_policy_explainer_video_candidate` | 行政将请假制度转成政策讲解视频脚本/payload。 | 可表达为 `policy_explainer_video_payload` | 文本中转；Veo/Gemini 禁用 | `policy_text`, `audience`, `duration` | `explainer_script`, `scene_plan`, `provider_payload`, `accuracy_notes` | 不生成视频 | 劳动合规、制度准确 | 生成视频、发布制度解释 | passed |
| 40 | `finance_receipt_image_vision_extract_candidate` | 用 mock receipt image payload 设计票据字段抽取。 | 可表达为 `receipt_vision_extract_payload` | vision route/dry-run；API 禁用 | `image_placeholder`, `fields_needed`, `confidence_threshold` | `vision_payload`, `expected_fields`, `confidence_rules`, `not_tax_advice` | 不上传票据图片 | 财税/报销、PII、低置信 | 调 vision API、报销审批 | passed |
| 41 | `admin_document_ocr_to_sop_candidate` | 用 mock OCR 文本整理门店开店 SOP。 | 可表达为 `ocr_text_to_sop` | 文本中转适配；不做真实 OCR | `ocr_text`, `department`, `sop_goal` | `sop_steps`, `roles`, `missing_info`, `risk_flags` | 不上传文档 | 制度准确、隐私、OCR 错误 | 真实 OCR、写文档系统 | passed |
| 42 | `finance_invoice_approval_workflow_dryrun_candidate` | 生成发票审批流程 dry-run payload。 | 可表达为 `invoice_approval_workflow_payload` | 文本中转；审批系统 API 禁用 | `invoice_fields`, `approval_policy`, `department` | `approval_payload`, `checklist`, `write_allowed=false`, `risk_flags` | 不写审批系统 | 财税、金额异常、供应商异常 | 审批发票、写系统、付款 | passed |
| 43 | `admin_meeting_to_slide_brief_candidate` | 将经营例会纪要转成 slide brief/spec。 | 可表达为 `meeting_to_slide_brief` | 文本中转；不写 PPT | `meeting_notes`, `audience`, `deck_goal` | `slide_outline`, `key_messages`, `data_needed`, `not_final_deck` | 不生成 PPT 文件 | 会议保密、数据口径 | 写文件、外发会议内容 | passed |
| 44 | `store_menu_poster_generation_candidate` | 为奶茶店菜单促销生成 OpenAI image relay route/payload。 | 可表达为 `store_menu_poster_route_payload` | image relay route-check；不出图 | `menu_items`, `prices`, `brand_style`, `size` | `poster_prompt`, `route_check`, `provider_payload`, `price_review_required` | 不生成图片、不发布 | 价格准确、字体/商标、图片版权 | 调 provider、发布海报 | passed |
| 45 | `store_digital_signage_video_candidate` | 为门店电子屏生成数字标牌视频 Remotion spec。 | 可表达为 `digital_signage_video_spec` | 文本中转生成 spec；不 render | `promotion`, `screen_size`, `loop_duration` | `render_spec`, `scene_timeline`, `asset_requirements`, `risk_notes` | 不生成视频、不写文件 | 价格、促销规则、素材授权 | 渲染视频、上传屏幕系统 | passed |

## 9. 未进入本轮 smoke 的 5 个暂缓项

本轮未测试 `needs_more_license_info` 项，不进入正式 L2：

- `sales_quote_pdf_brief_candidate`
- `marketing_social_carousel_image_agent_candidate`
- `ecommerce_product_detail_page_generator_candidate`
- `metrics_spreadsheet_agent_mcp_candidate`
- `admin_contract_clause_risk_mcp_candidate`

## 10. 权限边界确认

本轮未安装依赖、未访问真实账号、未调用真实 provider/API、未写 key、未上传客户素材、未生成真实图片/视频/音频/PPT/OCR/PDF、未发送、未发布、未写 CRM/Shopify/Figma/Canva/审批系统/业务系统、未退款/赔偿/改库存。DeepAgents smoke passed 只代表候选库可试跑，不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。
