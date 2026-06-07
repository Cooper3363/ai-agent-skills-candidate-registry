# DEEPAGENTS_SMOKE_QUALITY_SPRINT_07_RESULT

回传日期：2026-06-07

本轮性质：Quality Sprint 07 DeepAgents candidate-level metadata/mock/dry-run/route-check smoke。  
测试范围：仅处理 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_07_QUEUE.md` 内 16 个 L1 放行候选；排除 5 个 `needs_more_license_info` 与 4 个 `component_only` / role/component 候选。  
重要声明：按 2026-06-06 新规则，stable 仓库正式 Skill 已扩容为 55 个；本轮 candidate smoke passed 只代表候选库可继续试跑，不代表 L2 通过，不代表可封装，不代表自动进入 stable 或客户正式可调用。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_07_RESULT.md`。
- 已读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_07_QUEUE.md`。
- 已对 smoke 队列内 16 个候选完成 candidate-level metadata/mock/dry-run/route-check smoke。
- 已为每个候选记录中文六部门 mock/route-check 场景、输入输出 schema、callable 表达、中文可用性、权限边界、人工复核触发、禁止动作和 smoke_status。
- 已生成 Top8 正式 L2 simulated 队列建议：`queues/L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_07_QUEUE.md`。

## 2. 当前问题

- 11 个 SaaS/API read-only 候选仅完成 mock/read-only smoke，未连接真实账号，未验证真实 OAuth scope、分页、限流或错误码。
- 5 个媒体/provider 候选仅完成 route/config/payload schema check，未调用 OpenAI Images、OpenAI TTS、Runway、fal 或 HeyGen，未生成图片、视频或音频，不能写成真实 provider 通过。
- 5 个 `needs_more_license_info` 与 4 个 `component_only` / role/component 项仍不得进入普通 candidate smoke、正式 L2 或封装队列。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- `blocked` 数量为 0。
- 本轮未触发任何外网、真实 API/provider、真实账号、真实客户文件、上传、发送、写系统、媒体生成或依赖安装。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Top8 队列进入正式 L2 simulated。
- 是否将 5 个媒体/provider route-check passed 候选转入独立真实 provider smoke 审批链路，并要求补齐费用上限、素材授权、内容安全、输出权属和审计日志。
- 是否将 Workable、Greenhouse、HubSpot 等未入 Top8 的 passed 候选放入后续招聘/CRM 专题 L2 队列。
- 是否要求研究/许可证窗口继续补齐 5 个 `needs_more_license_info` 标准 Skill/registry 候选的具体 repo/subdir、LICENSE、manifest、外部抓取/API/key、文件写入与输出边界。

## 5. 建议下一步

- 将 Top8 非媒体、低真实动作风险、文本/结构化/read-only 候选送正式 L2 simulated。
- 媒体/provider 候选只保留 route-check passed，不进入正式 L2 通过或封装判断；如继续推进，另走真实 provider smoke 审批。
- 后续真实 Harness 前，所有 read-only 候选必须提供最小只读 scope manifest，并保留 `read_only=true`、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 16 |
| `failed` | 0 |
| `needs_fix` | 0 |
| `blocked` | 0 |

| smoke_type | 数量 |
| --- | ---: |
| SaaS/API `read_only_mock` | 11 |
| 媒体/provider `route_check` / `dry_run_payload_only` | 5 |

## 7. Read-only / Route-check 硬断言

| 检查项 | 结果 |
| --- | --- |
| read-only 候选 `read_only=true` | 通过，11 个 read-only mock 候选均仅使用 synthetic/mock rows |
| read-only 候选最小只读 scope | 通过，后续真实 Harness 需平台化落 scope manifest |
| read-only 候选 `write_allowed=false` | 通过 |
| read-only 候选 `send_allowed=false` | 通过 |
| read-only 候选 `upload_allowed=false` | 通过 |
| read-only 候选 `external_action_blocked=true` | 通过 |
| route-check `provider_call_allowed=false` | 通过，5 个媒体/provider 均未调用 provider |
| route-check `real_media_generation_allowed=false` | 通过，未生成图片/视频/音频/HTML/PDF/PPT/文件 |
| key 读取/打印/写入 | 未发生 |

## 8. Top8 正式 L2 队列建议

| 排名 | candidate_id | 推荐原因 | 正式 L2 重点 |
| ---: | --- | --- | --- |
| 1 | `quality_sprint07_intercom_article_decay_readonly_candidate` | 客服知识库衰减/缺口高频，read-only 风险低 | mock articles/conversations 到 decay/gap report、来源证据和复核触发 |
| 2 | `quality_sprint07_shopify_return_product_quality_candidate` | 售后退货与商品质量聚类高价值，read-only 可控 | mock returns/products 到 quality issue clusters、禁止退款/改商品 |
| 3 | `quality_sprint07_metabase_executive_digest_candidate` | 经营仪表盘摘要高频，mock dashboard cards 风险低 | mock dashboard cards 到 executive digest、数据质量和人工复核 |
| 4 | `quality_sprint07_docusign_missing_signature_readonly_candidate` | 合同缺签状态只读价值高，写入边界清晰 | mock envelopes 到 missing signature report、禁止发送/签署/改 envelope |
| 5 | `quality_sprint07_mailchimp_deliverability_qc_candidate` | 邮件送达 QC 高频，read-only 报表可控 | mock campaign reports 到 deliverability QC、禁止发送/改 audience |
| 6 | `quality_sprint07_helpscout_saved_reply_gap_candidate` | 客服 saved reply 缺口高频，与知识库助手包适配 | mock conversations/saved replies 到 gap report、禁止回复/写 saved reply |
| 7 | `quality_sprint07_front_account_handoff_candidate` | 客户交接场景高频，read-only handoff 可控 | mock account conversations 到 handoff brief、禁止发送/分派 |
| 8 | `quality_sprint07_amplitude_activation_dropoff_candidate` | 激活漏斗掉点分析高频，read-only analytics 风险低 | mock activation metrics 到 dropoff report、数据质量和因果边界 |

## 9. 媒体 Provider Route-check 清单

| candidate_id | route-check 状态 | 主要检查 | 后续建议 |
| --- | --- | --- | --- |
| `quality_sprint07_openai_image_review_to_product_scene_candidate` | passed | review themes + product metadata image payload、asset policy、cost_cap、content_safety | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | passed | roleplay script TTS payload、voice rights、cost_cap、content_safety | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint07_runway_customer_story_clip_candidate` | passed | customer story video payload、story rights、cost_cap、content_safety | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint07_fal_packshot_to_lifestyle_candidate` | passed | packshot-to-lifestyle route payload、product asset rights、model license、cost_cap | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint07_heygen_new_employee_avatar_candidate` | passed | avatar payload、likeness/voice consent、onboarding content safety、cost_cap | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |

## 10. 16 个候选 smoke 明细

| # | candidate_id | smoke_type | 中文 smoke 场景 | expected_inputs | expected_outputs | 权限边界 | 人工复核触发 | 禁止动作 | smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint07_intercom_article_decay_readonly_candidate` | read-only mock | 模拟 Intercom articles/conversations，输出文章衰减和缺口报告 | `mock_articles`, `mock_conversations`, `decay_rules` | `decay_report`, `article_gaps`, `source_rows`, `manual_review_required` | 不连 Intercom；`read_only=true`; `write_allowed=false`; `external_action_blocked=true` | 高频投诉、政策冲突、账号安全 | 写文章、发消息、改 conversation |
| 2 | `quality_sprint07_workable_interview_question_bank_candidate` | read-only mock | 模拟 JD 和候选人画像，输出面试题库草案 | `mock_job_description`, `mock_candidate_profile`, `fairness_rules` | `question_bank`, `fairness_flags`, `manual_review_required`, `not_hiring_decision=true` | 不连 Workable；不写候选人；不录用/拒绝 | 候选人 PII、歧视风险、敏感问题 | 录用/拒绝、写 candidate、发邮件 |
| 3 | `quality_sprint07_shopify_return_product_quality_candidate` | read-only mock | 模拟 Shopify returns/products，聚类商品质量问题 | `mock_returns`, `mock_products`, `quality_rules` | `quality_clusters`, `return_reasons`, `risk_flags`, `source_rows` | 不连 Shopify；不退款；不改商品/库存 | 高退货率、质量安全、退款敏感 | 退款、改商品、改库存、发通知 |
| 4 | `quality_sprint07_metabase_executive_digest_candidate` | read-only mock | 模拟 Metabase dashboard cards，生成经营摘要 | `mock_dashboard_cards`, `metric_rules`, `period` | `executive_digest`, `metric_highlights`, `data_quality_flags`, `source_cards` | 不连 Metabase/DB；不写 query/dashboard | 指标异常、样本缺失、财务敏感 | 写 query、改 dashboard、连真实 DB |
| 5 | `quality_sprint07_openai_image_review_to_product_scene_candidate` | route-check | 模拟评论主题和商品元数据，生成 image payload schema | `mock_review_themes`, `mock_product_metadata`, `asset_policy`, `cost_limit` | `image_payload`, `rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 OpenAI Images；不上传素材；不出图 | 评论隐私、商品/商标/版权、费用 | 调 provider、上传素材、生成图片 |
| 6 | `quality_sprint07_docusign_missing_signature_readonly_candidate` | read-only mock | 模拟 DocuSign envelopes，输出缺签报告 | `mock_envelopes`, `signature_rules`, `risk_rules` | `missing_signature_report`, `stalled_envelopes`, `risk_flags`, `source_rows` | 不连 DocuSign；不发送/签署/改 envelope | 合同金额、签署方异常、期限临近 | 发送合同、签署、修改 envelope |
| 7 | `quality_sprint07_mailchimp_deliverability_qc_candidate` | read-only mock | 模拟 Mailchimp campaign reports，输出送达 QC | `mock_campaign_reports`, `deliverability_rules`, `audience_rules` | `deliverability_qc`, `bounce_flags`, `unsubscribe_flags`, `send_allowed=false` | 不连 Mailchimp；不发送；不改 audience/contact | 投诉/退订异常、隐私风险、送达异常 | 发邮件、改 audience/contact |
| 8 | `quality_sprint07_helpscout_saved_reply_gap_candidate` | read-only mock | 模拟 Help Scout conversations/saved replies，输出回复模板缺口 | `mock_conversations`, `mock_saved_replies`, `support_rules` | `saved_reply_gaps`, `reply_briefs`, `source_rows`, `manual_review_required` | 不连 Help Scout；不回复；不写 saved reply | 政策冲突、退款、账号安全 | 回复客户、写 saved reply、打 tag |
| 9 | `quality_sprint07_front_account_handoff_candidate` | read-only mock | 模拟 Front account conversations，生成客户交接 brief | `mock_account_conversations`, `account_rules`, `handoff_rules` | `handoff_brief`, `open_items`, `risk_tags`, `source_rows` | 不连 Front；不发送；不分派 | VIP、承诺日期、未处理投诉 | 发消息、分派、评论、改 inbox |
| 10 | `quality_sprint07_greenhouse_offer_risk_readonly_candidate` | read-only mock | 模拟 Greenhouse offers/candidates，输出 offer 风险 checklist | `mock_offers`, `mock_candidates`, `fairness_rules` | `offer_risk_checklist`, `privacy_flags`, `manual_review_required`, `not_hiring_decision=true` | 不连 Greenhouse；不发 offer；不录用/拒绝 | 候选人 PII、薪酬敏感、歧视风险 | 发 offer、写候选人、录用/拒绝 |
| 11 | `quality_sprint07_amplitude_activation_dropoff_candidate` | read-only mock | 模拟 Amplitude activation metrics，输出激活掉点报告 | `mock_activation_metrics`, `event_schema`, `quality_rules` | `dropoff_report`, `activation_risks`, `data_quality_flags`, `source_rows` | 不连 Amplitude；不写 cohorts/charts | 样本低、事件缺失、隐私维度 | 写 cohorts/charts、读真实用户明细 |
| 12 | `quality_sprint07_hubspot_lead_source_quality_candidate` | read-only mock | 模拟 HubSpot contacts/deals，输出线索来源质量报告 | `mock_contacts`, `mock_deals`, `source_rules` | `source_quality_report`, `low_quality_sources`, `privacy_flags`, `source_rows` | 不连 HubSpot；不写联系人/任务 | PII、来源归因异常、大额商机 | 写联系人、建任务、发邮件 |
| 13 | `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | route-check | 模拟销售角色扮演脚本，生成 TTS payload schema | `mock_roleplay_script`, `voice_policy`, `cost_limit`, `safety_policy` | `tts_payload`, `voice_rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 TTS；不生成音频；不克隆声音 | 声音授权、销售承诺、费用 | 调 provider、生成音频、上传声音样本 |
| 14 | `quality_sprint07_runway_customer_story_clip_candidate` | route-check | 模拟客户故事 brief，生成 Runway video payload schema | `mock_customer_story_brief`, `asset_policy`, `cost_limit`, `safety_policy` | `video_payload`, `story_rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 Runway；不生成视频；不上传素材 | 客户授权、肖像/商标、费用 | 调 provider、上传素材、生成视频 |
| 15 | `quality_sprint07_fal_packshot_to_lifestyle_candidate` | route-check | 模拟商品 packshot 元数据，生成 fal lifestyle route payload | `mock_product_metadata`, `style_brief`, `rights_policy`, `cost_limit` | `lifestyle_payload`, `asset_rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 fal；不上传商品图；不生成图片 | 商品素材授权、商标、模型许可 | 调 provider、上传素材、出图 |
| 16 | `quality_sprint07_heygen_new_employee_avatar_candidate` | route-check | 模拟新员工培训脚本，生成 HeyGen avatar payload | `mock_onboarding_script`, `avatar_policy`, `voice_policy`, `cost_limit` | `avatar_payload`, `consent_required`, `content_safety`, `real_provider_smoke_required=true` | 不调用 HeyGen；不上传人脸/声音；不生成视频 | 肖像/声音授权、HR 内容、费用 | 调 provider、上传素材、生成视频 |

## 11. 排除项确认

| candidate_id | 状态 | 本轮处理 |
| --- | --- | --- |
| `quality_sprint07_last30days_market_signal_brief_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint07_baoyu_wechat_summary_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint07_graphify_kb_structure_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint07_fireworks_tech_graph_process_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint07_guizang_ppt_sales_training_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint07_agency_sales_ops_forecast_role_candidate` | component_only | 未处理 |
| `quality_sprint07_agency_finance_ap_ar_clerk_role_candidate` | component_only | 未处理 |
| `quality_sprint07_promptfoo_recruiting_fairness_regression_candidate` | component_only | 未处理 |
| `quality_sprint07_instructor_refund_case_schema_candidate` | component_only | 未处理 |

## 12. 权限边界确认

- 未安装依赖。
- 未访问外网或真实账号。
- 未调用真实 API/provider。
- 未读取、打印或写入 key。
- 未读取客户真实文件。
- 未上传素材。
- 未发送邮件、短信、微信、Slack、Outlook、Gmail 或其他消息。
- 未写任何业务系统。
- 未抓取真实网页。
- 未生成真实图片、视频、音频、HTML、PDF、PPT 或任何文件。
- 未退款、未赔偿、未扣款、未改库存、未改订阅、未写账、未报税、未创建任务、未共享文件。
- 未修改 stable 仓库；stable 正式 Skill 仍为 55。
