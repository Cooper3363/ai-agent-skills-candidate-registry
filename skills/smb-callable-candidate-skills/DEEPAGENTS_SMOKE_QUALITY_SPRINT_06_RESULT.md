# DEEPAGENTS_SMOKE_QUALITY_SPRINT_06_RESULT

回传日期：2026-06-05

本轮性质：Quality Sprint 06 DeepAgents candidate-level metadata/mock/dry-run/route-check smoke。  
测试范围：仅处理 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_06_QUEUE.md` 内 18 个 L1/trial mode 放行候选；排除 3 个 `needs_more_license_info` 与 4 个 `component_only`。  
重要声明：DeepAgents smoke passed 只代表候选库可继续试跑，不代表 L2 通过，不代表可封装，不代表客户正式可调用；客户正式可调用 Skill 仍为 13。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_06_RESULT.md`。
- 已读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_06_QUEUE.md`。
- 已对 smoke 队列内 18 个候选完成 candidate-level metadata/mock/dry-run/route-check smoke。
- 已为每个候选记录中文六部门 mock/dry-run/route-check 场景、输入输出 schema、callable 表达、中文可用性、权限边界、人工复核触发、禁止动作和 smoke_status。
- 已生成 Top8 正式 L2 simulated 队列建议：`queues/L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_06_QUEUE.md`。

## 2. 当前问题

- 12 个 SaaS/API read-only 候选仅完成 mock/read-only smoke，未连接真实账号，未验证真实 OAuth scope、分页、限流或错误码。
- HubSpot 仅完成 dry-run payload/spec，未写 deal、note、task 或发送邮件。
- 5 个媒体/provider 候选仅完成 route/config/payload schema check，未调用 OpenAI Images、Runway、OpenAI TTS、fal 或 HeyGen，未生成图片、视频或音频，不能写成真实 provider 通过。
- 3 个 `needs_more_license_info` 与 4 个 `component_only` 项仍不得进入普通 candidate smoke、正式 L2 或封装队列。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- `blocked` 数量为 0。
- 本轮未触发任何外网、真实 API/provider、真实账号、真实客户文件、上传、发送、写系统、媒体生成或依赖安装。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Top8 队列进入正式 L2 simulated。
- 是否将 5 个媒体/provider route-check passed 候选转入独立真实 provider smoke 审批链路，并要求补齐费用上限、素材授权、内容安全、输出权属和审计日志。
- 是否将 Gmail/Freshdesk/Shopify/DocuSign/PostHog/Mailchimp 等未入 Top8 的 passed 候选放入后续专题 L2 队列。
- 是否要求研究/许可证窗口继续补齐 Wondelai、OpenClaw、Guizang PPT 的具体目录、`SKILL.md`、LICENSE、manifest、assets/references 和文件生成边界。

## 5. 建议下一步

- 将 Top8 非媒体、低真实动作风险、文本/结构化/read-only/dry-run 候选送正式 L2 simulated。
- 媒体/provider 候选只保留 route-check passed，不进入正式 L2 通过或封装判断；如继续推进，另走真实 provider smoke 审批。
- 后续真实 Harness 前，所有 read-only 候选必须提供最小只读 scope manifest；HubSpot dry-run 候选必须保留 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 18 |
| `failed` | 0 |
| `needs_fix` | 0 |
| `blocked` | 0 |

| smoke_type | 数量 |
| --- | ---: |
| `can_mock_smoke` / `read_only_mock` | 12 |
| `can_dry_run_smoke` / `dry_run_only` | 1 |
| `can_route_check` / `route_check` | 5 |

## 7. Dry-run / Read-only / Route-check 硬断言

| 检查项 | 结果 |
| --- | --- |
| read-only 候选 `read_only=true` | 通过，12 个 read-only mock 候选均仅使用 synthetic/mock rows |
| read-only 候选最小只读 scope | 通过，后续真实 Harness 需平台化落 scope manifest |
| read-only 候选 `write_allowed=false` | 通过 |
| read-only 候选 `send_allowed=false` | 通过 |
| read-only 候选 `upload_allowed=false` | 通过 |
| read-only 候选 `external_action_blocked=true` | 通过 |
| HubSpot dry-run `send_allowed=false` | 通过 |
| HubSpot dry-run `write_allowed=false` | 通过 |
| HubSpot dry-run `upload_allowed=false` | 通过 |
| HubSpot dry-run `external_action_blocked=true` | 通过 |
| route-check `provider_call_allowed=false` | 通过，5 个媒体/provider 均未调用 provider |
| route-check `real_media_generation_allowed=false` | 通过，未生成图片/视频/音频/HTML/PDF/PPT/文件 |
| key 读取/打印/写入 | 未发生 |

## 8. Top8 正式 L2 队列建议

| 排名 | candidate_id | 推荐原因 | 正式 L2 重点 |
| ---: | --- | --- | --- |
| 1 | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | M365 政策/知识库 QC 高频，read-only 风险低 | mock SharePoint pages 到 policy gap、过期政策、人工复核 |
| 2 | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | Teams 交接摘要高频，禁止写入边界清楚 | mock Teams messages 到 handoff digest、owner gap、risk tags |
| 3 | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | 预算差异分析高价值，read-only rows 可控 | mock budget rows 到 variance report、财务复核提示 |
| 4 | `quality_sprint06_zendesk_answerbot_deflection_candidate` | 客服 deflection 场景高频，可复用知识库能力 | mock tickets/articles 到 deflection opportunities、风险边界 |
| 5 | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | 销售交接质量高频，dry-run payload 可硬阻断 | mock deals/notes 到 handoff quality report、四个硬断言 |
| 6 | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | 失败付款挽回高价值，但必须只读与草稿化 | mock failed payments 到 recovery draft、禁止扣款/退款/发送 |
| 7 | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | HR 请假覆盖高频，read-only 和隐私边界清楚 | mock time-off rows 到 coverage summary、PII/排班复核 |
| 8 | `quality_sprint06_google_workspace_gmail_label_health_candidate` | Gmail label health 高频，元数据只读风险可控 | mock labels/message headers 到 label health report |

## 9. 媒体 Provider Route-check 清单

| candidate_id | route-check 状态 | 主要检查 | 后续建议 |
| --- | --- | --- | --- |
| `quality_sprint06_openai_image_brand_scene_batch_candidate` | passed | image batch payload、brand asset policy、cost_cap、content_safety、audit_fields | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint06_runway_storyboard_to_clip_candidate` | passed | video payload、storyboard schema、asset rights、cost_cap、content_safety | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint06_openai_tts_customer_training_audio_candidate` | passed | TTS payload、voice rights、training content safety、cost_cap | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint06_fal_product_model_tryon_route_candidate` | passed | try-on payload、人像/商品素材授权、model license、cost_cap | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint06_heygen_sales_objection_avatar_candidate` | passed | avatar payload、likeness/voice consent、script safety、cost_cap | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |

## 10. 18 个候选 smoke 明细

| # | candidate_id | smoke_type | 中文 smoke 场景 | expected_inputs | expected_outputs | 权限边界 | 人工复核触发 | 禁止动作 | smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint06_microsoft_graph_sharepoint_policy_qc_candidate` | read-only mock | 模拟 SharePoint 政策页面，输出政策 QC 和缺口 | `mock_pages`, `policy_rules`, `freshness_rules` | `policy_gaps`, `outdated_pages`, `qc_flags`, `source_pages` | 不连 M365；`read_only=true`; `write_allowed=false`; `external_action_blocked=true` | 过期政策、合规冲突、HR/财务敏感 | 写页面/文件、改权限、共享文件 | passed |
| 2 | `quality_sprint06_microsoft_graph_teams_handoff_digest_candidate` | read-only mock | 模拟 Teams 频道消息，生成交接 digest | `mock_messages`, `team_roster`, `handoff_rules` | `handoff_digest`, `open_items`, `owner_gaps`, `risk_tags` | 不连 Teams；不发消息；不建任务 | VIP、承诺日期、未闭环事项 | 发消息、建任务、写频道 | passed |
| 3 | `quality_sprint06_google_sheets_budget_variance_harness_candidate` | read-only mock | 模拟预算表行，输出预算差异报告 | `mock_budget_rows`, `variance_rules`, `period` | `variance_report`, `over_budget_items`, `source_rows`, `manual_review_required` | 不读真实 Sheets；不写单元格；不生成文件 | 超预算、财务敏感、异常分类 | 写表、生成文件、写账/报税 | passed |
| 4 | `quality_sprint06_zendesk_answerbot_deflection_candidate` | read-only mock | 模拟 tickets/articles，识别 answerbot deflection 机会 | `mock_tickets`, `help_center_articles`, `deflection_rules` | `deflection_opportunities`, `article_candidates`, `risk_tags`, `source_rows` | 不连 Zendesk；不回复；不写文章/工单 | 投诉、退款、账号安全、政策冲突 | 回复客户、写文章、改工单 | passed |
| 5 | `quality_sprint06_hubspot_deal_handoff_quality_candidate` | dry-run | 模拟 HubSpot deals/notes，生成交接质量报告和 dry-run payload | `mock_deals`, `mock_notes`, `handoff_rules` | `handoff_quality_report`, `missing_fields`, `dry_run_payload`, `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | 不连 HubSpot；不写 deal/note/task | 大额商机、PII、承诺折扣、下一步缺失 | 写 CRM、建任务、发邮件、上传 | passed |
| 6 | `quality_sprint06_stripe_failed_payment_recovery_draft_candidate` | read-only mock | 模拟 failed payments/invoices，输出挽回草稿 | `mock_failed_payments`, `mock_invoices`, `recovery_policy` | `recovery_drafts`, `payment_risk_flags`, `manual_review_required`, `source_rows` | 不连 Stripe；不扣款/退款/发邮件 | 支付隐私、财务敏感、重复扣款风险 | 扣款、退款、发邮件、财务结论 | passed |
| 7 | `quality_sprint06_bamboohr_timeoff_coverage_candidate` | read-only mock | 模拟请假和排班行，输出覆盖缺口 | `mock_timeoff_rows`, `staffing_rules`, `privacy_rules` | `coverage_summary`, `coverage_gaps`, `privacy_flags`, `manual_review_required` | 不连 BambooHR；不写员工记录 | 员工 PII、排班缺口、薪酬/健康敏感 | 写员工记录、做 HR 决策 | passed |
| 8 | `quality_sprint06_openai_image_brand_scene_batch_candidate` | route-check | 模拟品牌场景批量图 brief，生成 image payload schema | `mock_brand_brief`, `asset_policy`, `cost_limit`, `safety_policy` | `image_batch_payload`, `rights_notes`, `cost_cap`, `content_safety`, `real_provider_smoke_required=true` | 不调用 OpenAI Images；不生成图片；不上传素材 | 品牌/商标/版权/费用/内容安全 | 调 provider、上传素材、出图 | passed |
| 9 | `quality_sprint06_runway_storyboard_to_clip_candidate` | route-check | 模拟 storyboard，生成 Runway video payload schema | `mock_storyboard`, `asset_policy`, `cost_limit`, `safety_policy` | `video_payload`, `asset_rights_notes`, `cost_cap`, `content_safety`, `real_provider_smoke_required=true` | 不调用 Runway；不生成视频；不上传素材 | 视频版权、素材授权、费用 | 调 provider、上传素材、生成视频 | passed |
| 10 | `quality_sprint06_google_workspace_gmail_label_health_candidate` | read-only mock | 模拟 Gmail labels/message headers，输出标签健康报告 | `mock_labels`, `mock_message_headers`, `label_rules` | `label_health`, `mislabel_flags`, `source_rows`, `send_allowed=false` | 不连 Gmail；不读正文；不发邮件/改标签 | 邮件隐私、客户投诉、敏感发件人 | 读真实正文、发邮件、改标签 | passed |
| 11 | `quality_sprint06_freshdesk_agent_workload_balance_candidate` | read-only mock | 模拟 Freshdesk tickets/agents，输出客服工作量平衡 | `mock_tickets`, `mock_agents`, `workload_rules` | `workload_summary`, `overload_flags`, `handoff_suggestions`, `source_rows` | 不连 Freshdesk；不分派/回复/改状态 | 工单过载、投诉升级、绩效敏感 | 分派工单、回复、改状态 | passed |
| 12 | `quality_sprint06_shopify_subscription_order_exception_candidate` | read-only mock | 模拟 Shopify orders/customers，输出订阅订单异常 | `mock_orders`, `mock_customers`, `exception_rules` | `order_exceptions`, `subscription_flags`, `risk_notes`, `source_rows` | 不连 Shopify；不退款；不改订单/订阅/客户 | 退款、订阅变更、库存/配送异常 | 退款、改订单、改订阅、改库存 | passed |
| 13 | `quality_sprint06_docusign_renewal_notice_gap_candidate` | read-only mock | 模拟 DocuSign envelopes，输出续约通知缺口 | `mock_envelopes`, `template_rows`, `renewal_rules` | `renewal_notice_gaps`, `stalled_envelopes`, `risk_flags`, `source_rows` | 不连 DocuSign；不发送/签署/写 envelope | 合同金额、续约期限、签署异常 | 发送合同、签署、改 envelope | passed |
| 14 | `quality_sprint06_posthog_funnel_dropoff_candidate` | read-only mock | 模拟 PostHog funnel metrics，输出掉点报告 | `mock_funnel_metrics`, `event_schema`, `quality_rules` | `dropoff_report`, `conversion_anomalies`, `data_quality_flags`, `source_rows` | 不连 PostHog；不改 tracking | 样本低、事件缺失、隐私维度 | 写 tracking config、读真实用户明细 | passed |
| 15 | `quality_sprint06_mailchimp_audience_health_candidate` | read-only mock | 模拟 Mailchimp audience/campaign 数据，输出受众健康 | `mock_audience_metrics`, `campaign_rows`, `privacy_rules` | `audience_health`, `unsubscribe_flags`, `engagement_segments`, `send_allowed=false` | 不连 Mailchimp；不发送；不改 audience/contact | 退订/投诉异常、隐私风险、低互动分群 | 发送邮件、改联系人、改 audience | passed |
| 16 | `quality_sprint06_openai_tts_customer_training_audio_candidate` | route-check | 模拟客户培训脚本，生成 TTS payload schema | `mock_training_script`, `voice_policy`, `cost_limit`, `safety_policy` | `tts_payload`, `voice_rights_notes`, `cost_cap`, `content_safety`, `real_provider_smoke_required=true` | 不调用 TTS；不生成音频；不克隆声音 | 声音授权、敏感培训内容、费用上限 | 调 provider、生成音频、上传声音样本 | passed |
| 17 | `quality_sprint06_fal_product_model_tryon_route_candidate` | route-check | 模拟商品/模特试穿元数据，生成 fal route payload | `mock_product_metadata`, `model_policy`, `rights_policy`, `cost_limit` | `tryon_payload`, `likeness_rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 fal；不上传人像/商品图；不生成图片 | 人像授权、商品素材、模型许可、费用 | 调 provider、上传素材、出图 | passed |
| 18 | `quality_sprint06_heygen_sales_objection_avatar_candidate` | route-check | 模拟销售异议脚本，生成 HeyGen avatar payload | `mock_objection_script`, `avatar_policy`, `voice_policy`, `cost_limit` | `avatar_payload`, `consent_required`, `content_safety`, `real_provider_smoke_required=true` | 不调用 HeyGen；不上传人脸/声音；不生成视频 | 肖像/声音授权、销售承诺、费用 | 调 provider、上传素材、生成视频 | passed |

## 11. 排除项确认

| candidate_id | 状态 | 本轮处理 |
| --- | --- | --- |
| `quality_sprint06_wondelai_skill_pack_specific_scan_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint06_openclaw_uiux_pro_max_official_path_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint06_guizang_ppt_license_followup_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint06_agency_ops_coordinator_role_candidate` | component_only | 未处理 |
| `quality_sprint06_agency_purchase_admin_role_candidate` | component_only | 未处理 |
| `quality_sprint06_promptfoo_customer_reply_safety_candidate` | component_only | 未处理 |
| `quality_sprint06_instructor_sales_call_schema_candidate` | component_only | 未处理 |

## 12. 权限边界确认

- 未安装依赖。
- 未访问外网或真实账号。
- 未调用真实 API/provider。
- 未读取、打印或写入 key。
- 未读取客户真实文件。
- 未上传素材。
- 未发送邮件、短信、微信、Slack、Outlook、Gmail 或其他消息。
- 未写 M365、Google、Zendesk、HubSpot、Stripe、BambooHR、Gmail、Freshdesk、Shopify、DocuSign、PostHog、Mailchimp 或业务系统。
- 未抓取真实网页。
- 未生成真实图片、视频、音频、HTML、PDF、PPT 或任何文件。
- 未退款、未赔偿、未扣款、未改库存、未改订阅、未写账、未报税、未创建任务、未共享文件。
- 未修改稳交付库；客户正式可调用 Skill 仍为 13。
