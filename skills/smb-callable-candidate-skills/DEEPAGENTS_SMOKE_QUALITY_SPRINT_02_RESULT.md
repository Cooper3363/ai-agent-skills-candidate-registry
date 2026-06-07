# DEEPAGENTS_SMOKE_QUALITY_SPRINT_02_RESULT

回传日期：2026-06-05

本轮性质：DeepAgents candidate-level metadata/mock/dry-run/route-check smoke。  
结论边界：DeepAgents smoke passed 只代表候选库可继续试跑，不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_02_RESULT.md` 与 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_02_QUEUE.md`。
- 已确认 smoke 队列包含 29 个 L1/trial mode 放行候选；`quality_sprint02_open_design_menu_poster_child_candidate` 为 needs_more_license_info，未进入本轮 smoke。
- 已对 29 个候选完成 candidate-level metadata/mock/dry-run/route-check smoke。
- 已为每个候选记录中文 mock/dry-run/route-check 场景、callable 表达、模型通道适配、预期输入输出、权限边界、人工复核触发、禁止动作和 smoke_status。
- 已从 passed 候选中筛选 Top10，生成正式 L2 simulated 队列建议。

## 2. 当前问题

- 13 个媒体/provider 候选仅完成 route/config/payload check，未真实生成图片、视频、音频或 PDF，不得写成真实 provider 通过。
- SaaS/API/CRM/POS/邮件/协作工具类候选仅完成 mock/read-only/dry-run smoke，未连接真实账号，未写业务系统。
- Agent workflow / framework 类候选可 smoke，但后续是否进入正式 L2 需看是否能抽成轻量 callable 业务能力。
- `quality_sprint02_open_design_menu_poster_child_candidate` 仍需研究/许可证窗口补齐具体 child skill、manifest、API/文件写入边界。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 本轮未触发外部网络、真实账号、真实 API/provider、真实客户文件、发送、上传、抓取、退款/赔偿、库存修改或写业务系统动作。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Top10 进入正式 L2 simulated，每个候选至少 3 个中文业务 mock/dry-run 用例。
- 是否为 13 个媒体/provider route-check passed 候选另建真实 provider smoke 预检/审批队列。
- 是否要求研究窗口继续补齐 open-design menu poster child 的具体子目录、许可证和导出/写入边界。

## 5. 建议下一步

- 将 Top10 非媒体、低真实动作风险、callable 表达清楚的候选送正式 L2 simulated。
- 媒体/provider 项只保留为 route-check passed，暂不进入正式 L2 通过或封装判断。
- 所有 dry-run/SaaS/API 候选后续 L2 与封装阶段继续强制 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 29 |
| `failed` | 0 |
| `needs_fix` | 0 |
| `blocked` | 0 |

| smoke_type | 数量 |
| --- | ---: |
| `can_mock_smoke` | 8 |
| `can_dry_run_smoke` | 8 |
| `can_route_check` | 13 |

## 7. Dry-run 硬断言结果

| 检查项 | 结果 |
| --- | --- |
| `send_allowed=false` | 通过；邮件/CRM/协作/营销相关 dry-run 均禁止发送 |
| `write_allowed=false` | 通过；CRM/POS/Docs/Bitable/邮件/业务系统均禁止写入 |
| `external_action_blocked=true` | 通过；所有 dry-run 与 route-check 候选均阻断外部动作 |
| provider/API 真实调用 | 未发生 |
| key 读取/打印/写入 | 未发生 |

## 8. Top10 正式 L2 队列建议

| 排名 | candidate_id | 推荐原因 | 正式 L2 重点 |
| ---: | --- | --- | --- |
| 1 | `quality_sprint02_microsoft_excel_report_agent_candidate` | 经营报表高频，Excel mock rows 与稳交付报表能力互补 | Excel rows 到经营摘要、异常、source rows；read-only 边界 |
| 2 | `quality_sprint02_square_pos_daily_report_candidate` | 门店 POS 日报高频，mock rows 可稳定验证 | POS 销售/退款/客单价摘要，不做收款/退款动作 |
| 3 | `quality_sprint02_gmail_customer_email_triage_candidate` | 客服邮箱分流高频，dry-run 草稿可控 | 邮件分类、回复草稿、风险标签，send_allowed=false |
| 4 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | 销售/客服邮件跟进常见，微软路线补充 | 邮件摘要、跟进草稿、Outlook send blocked |
| 5 | `quality_sprint02_zoho_crm_followup_candidate` | CRM 跟进高频，适合 dry-run payload | 线索摘要、下一步动作、write_allowed=false |
| 6 | `quality_sprint02_pipedrive_deal_next_step_candidate` | 销售商机推进高频，CRM 写入风险可 dry-run 控制 | deal 阶段、风险、下一步建议，不写 Pipedrive |
| 7 | `quality_sprint02_lark_docs_meeting_action_candidate` | 会议纪要/待办高频，国内协作场景补充 | mock 会议文档到行动项，不创建任务 |
| 8 | `quality_sprint02_wecom_customer_group_summary_candidate` | 中文私域客服/社群运营高频 | 群消息摘要、风险标签、send_allowed=false |
| 9 | `quality_sprint02_gorgias_ecommerce_support_candidate` | 电商客服工单高频，mock tickets 可稳定测试 | 工单分类、优先级、退款/投诉风险，不回复工单 |
| 10 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | 财务费用核对高频，mock rows 低风险 | 费用对账提示、异常字段，不做审计/税务结论 |

## 9. 29 个候选 smoke 明细

| # | candidate_id | smoke_type | 中文 smoke 场景 | expected_inputs | expected_outputs | 权限边界 | 人工复核触发 | 禁止动作 | deepagents_smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint02_microsoft_excel_report_agent_candidate` | mock | 模拟 Excel 门店周报 rows，生成经营摘要 | `mock_workbook_rows`, `metric_schema`, `date_range` | `summary`, `metric_changes`, `anomalies`, `source_rows`, `manual_review_required` | 不读真实 Excel/Graph；read-only mock | 口径冲突、缺关键字段、异常波动 | 读取真实文件、写 workbook、分享权限变更 | passed |
| 2 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | dry-run | 模拟 Outlook 客户邮件，生成跟进草稿 | `mock_emails`, `customer_context`, `policy_rules` | `email_summary`, `draft_reply`, `risk_flags`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Outlook；不发邮件 | 投诉、退款、合同承诺、PII | 发送邮件、写草稿箱、读取真实邮箱 | passed |
| 3 | `quality_sprint02_stability_product_scene_candidate` | route-check | 模拟商品资料，生成 Stability 场景图 payload | `mock_product`, `prompt_brief`, `asset_policy`, `cost_limit` | `provider_payload`, `route_config`, `cost_cap`, `content_safety`, `real_media_generation_requires_approval=true` | 不调用 Stability；不生成图片 | 商标、版权、人物、费用超限 | provider 调用、图片生成、素材上传 | passed |
| 4 | `quality_sprint02_adobe_firefly_product_ad_image_candidate` | route-check | 模拟活动 brief，生成 Firefly 广告图 payload | `mock_campaign`, `brand_rules`, `asset_policy`, `cost_limit` | `provider_payload`, `audit_fields`, `content_safety`, `real_media_generation_requires_approval=true` | 不调用 Firefly；不生成图片 | 品牌授权、版权、平台禁词 | provider 调用、图片生成、发布 | passed |
| 5 | `quality_sprint02_fal_flux_product_photo_candidate` | route-check | 模拟商品图风格化需求，生成 fal FLUX payload | `mock_product_metadata`, `model_id`, `style_goal`, `cost_limit` | `route_config`, `provider_payload`, `model_license_note`, `real_media_generation_requires_approval=true` | 不调用 fal；不生成图片 | 模型许可证、商品授权、费用 | provider 调用、图片生成、素材上传 | passed |
| 6 | `quality_sprint02_runway_gen4_short_ad_candidate` | route-check | 模拟短广告脚本，生成 Runway 视频 payload | `mock_campaign_brief`, `storyboard`, `asset_policy`, `cost_limit` | `video_payload`, `duration`, `rights_notes`, `real_media_generation_requires_approval=true` | 不调用 Runway；不渲染视频 | 肖像/版权、预算、内容安全 | 视频生成、上传、发布 | passed |
| 7 | `quality_sprint02_gmail_customer_email_triage_candidate` | dry-run | 模拟 Gmail 客服邮件，生成分流和回复草稿 | `mock_email`, `triage_rules`, `policy_snippets` | `category`, `priority`, `draft_reply`, `risk_flags`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Gmail；不发邮件 | 投诉退款、账号安全、PII、低置信 | 发送邮件、写 Gmail、读取真实邮箱 | passed |
| 8 | `quality_sprint02_zoho_crm_followup_candidate` | dry-run | 模拟 Zoho CRM 线索，生成下一步 payload | `mock_lead`, `mock_notes`, `stage_rules` | `lead_summary`, `next_action`, `crm_payload`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Zoho CRM；不写联系人 | 折扣、合同、PII、高价值客户 | 写 CRM、发邮件、创建任务 | passed |
| 9 | `quality_sprint02_lark_docs_meeting_action_candidate` | mock | 模拟 Lark 会议文档，提取行动项 | `mock_meeting_doc`, `attendees`, `action_rules` | `meeting_summary`, `action_items`, `owners`, `due_date_warnings`, `external_action_blocked=true` | 不连 Lark；不创建任务 | 责任人不清、敏感客户信息、承诺事项 | 写文档、创建任务、通知成员 | passed |
| 10 | `quality_sprint02_recraft_brand_banner_candidate` | route-check | 模拟品牌 banner 需求，生成 Recraft payload | `mock_brand_brief`, `brand_rules`, `asset_policy`, `cost_limit` | `banner_payload`, `brand_safety`, `cost_cap`, `real_media_generation_requires_approval=true` | 不调用 Recraft；不生成图片 | 商标、品牌错用、版权素材 | provider 调用、图片生成、发布 | passed |
| 11 | `quality_sprint02_pipedrive_deal_next_step_candidate` | dry-run | 模拟 Pipedrive deal，生成下一步建议 | `mock_deal`, `activity_history`, `pipeline_rules` | `deal_summary`, `risk_flags`, `next_step`, `send_allowed=false`, `write_allowed=false`, `external_action_blocked=true` | 不连 Pipedrive；不写 deal | 大额折扣、合同条款、停滞商机 | 写 CRM、改阶段、发邮件 | passed |
| 12 | `quality_sprint02_square_pos_daily_report_candidate` | mock | 模拟 Square POS 日销售 rows，生成日报 | `mock_pos_rows`, `store_profile`, `metric_schema` | `daily_summary`, `sales_breakdown`, `refund_notes`, `anomalies` | 不连 Square；不读真实 POS | 退款异常、支付异常、口径缺失 | 退款、收款、写 POS | passed |
| 13 | `quality_sprint02_ideogram_poster_text_candidate` | route-check | 模拟门店海报文案，生成 Ideogram payload | `mock_poster_brief`, `text_requirements`, `brand_rules`, `cost_limit` | `poster_payload`, `text_render_risks`, `real_media_generation_requires_approval=true` | 不调用 Ideogram；不生成海报 | 中文文字渲染、字体、商标、版权 | 图片生成、上传、发布 | passed |
| 14 | `quality_sprint02_fal_kontext_image_edit_candidate` | route-check | 模拟商品局部修图需求，生成 Kontext edit payload | `mock_image_metadata`, `edit_instruction`, `asset_policy` | `edit_payload`, `model_id`, `rights_notes`, `real_media_generation_requires_approval=true` | 不调用 fal；不上传图片 | 商品授权、人物/商标、模型条款 | provider 调用、图片编辑、素材上传 | passed |
| 15 | `quality_sprint02_removebg_cutout_candidate` | route-check | 模拟商品白底图需求，生成 remove.bg cutout payload | `mock_image_metadata`, `cutout_policy`, `cost_limit` | `cutout_payload`, `output_path_schema`, `privacy_notes`, `real_media_generation_requires_approval=true` | 不调用 remove.bg；不上传图片 | 证件照/员工照、商品版权、费用 | 上传图片、抠图生成、发布 | passed |
| 16 | `quality_sprint02_luma_dream_machine_store_video_candidate` | route-check | 模拟门店短视频需求，生成 Luma video payload | `mock_store_brief`, `storyboard`, `asset_policy`, `cost_limit` | `video_payload`, `rights_notes`, `content_safety`, `real_media_generation_requires_approval=true` | 不调用 Luma；不生成视频 | 门店素材授权、肖像、预算 | 视频生成、上传、发布 | passed |
| 17 | `quality_sprint02_wecom_customer_group_summary_candidate` | mock | 模拟企微客户群聊天，生成群摘要和风险标签 | `mock_group_messages`, `summary_rules`, `policy_snippets` | `group_summary`, `customer_intents`, `risk_tags`, `manual_review_required`, `external_action_blocked=true` | 不连企微；不发群消息 | 投诉、退款、PII、舆情 | 发送消息、拉群、读取真实群 | passed |
| 18 | `quality_sprint02_gorgias_ecommerce_support_candidate` | mock | 模拟电商客服工单，生成分流和风险摘要 | `mock_tickets`, `support_rules`, `refund_policy` | `ticket_summaries`, `priority`, `risk_flags`, `handoff_required` | 不连 Gorgias；不回复工单 | 退款、投诉、赔偿、物流争议 | 回复工单、退款、写客服系统 | passed |
| 19 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | mock | 模拟费用和发票 rows，生成核对提示 | `mock_expense_rows`, `mock_invoice_rows`, `reconcile_rules` | `matched_items`, `exceptions`, `risk_flags`, `not_audit_or_tax_advice=true` | 不连 Zoho Books；不读真实财务 | 金额不一致、税号缺失、重复报销 | 审批报销、做税务/审计结论、写账本 | passed |
| 20 | `quality_sprint02_google_veo_store_campaign_candidate` | route-check | 模拟门店活动短视频 brief，生成 Veo payload | `mock_campaign_brief`, `storyboard`, `asset_policy`, `cost_limit` | `video_payload`, `region_terms_note`, `real_media_generation_requires_approval=true` | 不调用 Veo/Gemini；不生成视频 | 地区可用性、版权、费用、内容政策 | 视频生成、上传、发布 | passed |
| 21 | `quality_sprint02_heygen_training_avatar_cn_candidate` | route-check | 模拟 HR 培训脚本，生成 HeyGen 数字人 payload | `mock_training_script`, `avatar_policy`, `voice_policy`, `cost_limit` | `avatar_payload`, `consent_required`, `content_safety`, `real_media_generation_requires_approval=true` | 不调用 HeyGen；不生成视频 | 肖像/声音授权、HR 敏感内容、费用 | 数字人生成、上传、发布 | passed |
| 22 | `quality_sprint02_haystack_faq_rag_candidate` | mock | 模拟 FAQ 文档，生成带引用回答 | `mock_docs`, `question`, `min_confidence` | `answer`, `citations`, `confidence`, `handoff_required`, `risk_flags` | 不读真实文档；不接真实向量库 | 低置信、无引用、退款/账号安全 | 编造引用、写线上 KB | passed |
| 23 | `quality_sprint02_shopline_order_digest_candidate` | mock | 模拟 SHOPLINE 订单 rows，生成运营摘要 | `mock_orders`, `store_rules`, `date_range` | `order_digest`, `exceptions`, `risk_flags`, `source_rows` | 不连 SHOPLINE；不读真实订单 | 异常退款、缺货、隐私字段 | 写订单、退款、改库存 | passed |
| 24 | `quality_sprint02_feishu_bitable_ops_tracker_candidate` | mock | 模拟飞书多维表 rows，生成运营跟踪摘要 | `mock_bitable_rows`, `status_rules`, `date_range` | `ops_summary`, `blocked_items`, `owner_gaps`, `manual_review_required` | 不连飞书；不写表 | 延期、责任人缺失、敏感客户 | 写行、创建任务、通知成员 | passed |
| 25 | `quality_sprint02_mailchimp_campaign_report_candidate` | mock | 模拟邮件活动数据，生成营销复盘摘要 | `mock_campaign_stats`, `audience_notes`, `benchmark_rules` | `campaign_summary`, `metric_changes`, `risk_flags`, `send_allowed=false` | 不连 Mailchimp；不发邮件 | 退订异常、隐私、投放承诺 | 发送邮件、改受众、写 campaign | passed |
| 26 | `quality_sprint02_autogen_sales_roleplay_candidate` | mock | 模拟销售线索，生成角色扮演话术和评分 | `mock_lead_profile`, `scenario_goal`, `rubric` | `roleplay_script`, `objection_paths`, `scorecard`, `risk_notes` | 不调用真实工具；不联系客户 | 价格承诺、医疗/金融敏感、攻击性话术 | 发消息、写 CRM、真实外呼 | passed |
| 27 | `quality_sprint02_crewai_market_research_candidate` | mock | 模拟公司资料，生成市场调研 brief | `mock_company_profile`, `research_scope`, `source_notes` | `research_brief`, `assumptions`, `open_questions`, `manual_review_required` | 不浏览、不搜索、不调用 API | 来源不足、竞品结论过度、版权引用 | 抓网页、调用搜索/API、采集联系人 | passed |
| 28 | `quality_sprint02_instructor_schema_extraction_candidate` | mock | 模拟客户需求文本，抽取 typed JSON | `mock_text`, `target_schema`, `validation_rules` | `typed_json`, `validation_errors`, `confidence`, `fallback_required` | 不读真实文件；不写业务系统 | schema 缺字段、低置信、PII | 调用真实 provider tool、写系统 | passed |
| 29 | `quality_sprint02_promptfoo_support_regression_candidate` | mock | 模拟 3 条客服回归测试 case，输出 eval report | `mock_eval_cases`, `expected_behaviors`, `rubric` | `eval_summary`, `failed_cases`, `risk_flags`, `manual_review_required` | 不接真实 eval 数据；不调用外部模型平台 | 退款承诺、账号安全、PII 漏判 | 上传 eval 数据、调用真实测试平台 | passed |

## 10. 权限边界确认

- 未安装依赖。
- 未访问真实账号。
- 未调用真实 API/provider。
- 未写 key、未打印 key、未读取密钥文件。
- 未读取客户真实文件。
- 未发送邮件、短信、微信、Slack、Outlook、Gmail 或平台消息。
- 未写 CRM、POS、Sheets、Notion、Feishu、Lark、Shopline、Mailchimp 或其他业务系统。
- 未抓取真实网页。
- 未上传文件。
- 未生成真实图片、视频、音频或 PDF。
- 未退款、未赔偿、未改库存。
- 未修改稳交付库 13 个包。
