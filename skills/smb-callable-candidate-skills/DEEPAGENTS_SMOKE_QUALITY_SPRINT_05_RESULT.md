# DEEPAGENTS_SMOKE_QUALITY_SPRINT_05_RESULT

回传日期：2026-06-05

本轮性质：Quality Sprint 05 DeepAgents candidate-level metadata/mock/dry-run/route-check smoke。  
测试范围：仅处理 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_05_QUEUE.md` 内 20 个 L1/trial mode 放行候选；排除 4 个 `needs_more_license_info` 与 1 个 `component_only`。  
重要声明：DeepAgents smoke passed 只代表候选库可继续试跑，不代表 L2 通过，不代表可封装，不代表客户正式可调用；客户正式可调用 Skill 仍为 13。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_05_RESULT.md`。
- 已读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_05_QUEUE.md`。
- 已对 smoke 队列内 20 个候选完成 candidate-level metadata/mock/dry-run/route-check smoke。
- 已为每个候选记录中文六部门 mock/dry-run/route-check 场景、输入输出 schema、callable 表达、中文可用性、权限边界、人工复核触发、禁止动作和 smoke_status。
- 已生成 Top10 正式 L2 simulated 队列建议：`queues/L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_05_QUEUE.md`。

## 2. 当前问题

- 16 个 SaaS/API read-only 候选仅完成 mock/read-only smoke，未连接真实账号，未验证真实 OAuth scope 或平台分页/限流/错误码。
- Canva 仅完成 dry-run payload/spec，未创建设计、未上传素材、未导出文件。
- 3 个媒体/provider 候选仅完成 route/config/payload schema check，未调用 OpenAI TTS、fal 或 Replicate，未生成音频或图片，不能写成真实 provider 通过。
- 4 个 `needs_more_license_info` 与 1 个 `component_only` 项仍不得进入普通 candidate smoke、正式 L2 或封装队列。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- `blocked` 数量为 0。
- 本轮未触发任何外网、真实 API/provider、真实账号、真实客户文件、上传、发送、写系统、媒体生成或依赖安装。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Top10 队列进入正式 L2 simulated。
- 是否将 3 个媒体/provider route-check passed 候选转入独立真实 provider smoke 审批链路，并要求补齐费用上限、素材授权、内容安全、输出权属和审计日志。
- 是否将未入 Top10 的 Figma/Asana/Trello/Jira/Confluence/BambooHR/Greenhouse/DocuSign 放入后续协作/HR/签约专题 L2 队列。
- 是否要求研究/许可证窗口继续补齐 Pika、OpenClaw、guizang PPT、open-design design brief 的具体 repo/subdir/SKILL.md/LICENSE/manifest 与文件写入边界。

## 5. 建议下一步

- 将 Top10 非媒体、低真实动作风险、文本/结构化/read-only/dry-run 候选送正式 L2 simulated。
- 媒体/provider 候选只保留 route-check passed，不进入正式 L2 通过或封装判断；如继续推进，另走真实 provider smoke 审批。
- 后续真实 Harness 前，所有 read-only 候选必须提供最小只读 scope manifest；dry-run 候选必须保留 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 20 |
| `failed` | 0 |
| `needs_fix` | 0 |
| `blocked` | 0 |

| smoke_type | 数量 |
| --- | ---: |
| `can_mock_smoke` / `read_only_mock` | 16 |
| `can_dry_run_smoke` / `dry_run_only` | 1 |
| `can_route_check` / `route_check` | 3 |

## 7. Dry-run / Read-only / Route-check 硬断言

| 检查项 | 结果 |
| --- | --- |
| read-only 候选 `read_only=true` | 通过，16 个 read-only mock 候选均仅使用 synthetic/mock rows |
| read-only 候选最小只读 scope | 通过，后续真实 Harness 需平台化落 scope manifest |
| read-only 候选 `write_allowed=false` | 通过 |
| read-only 候选 `send_allowed=false` | 通过，营销/客服/协作候选均禁止发送 |
| read-only 候选 `upload_allowed=false` | 通过 |
| read-only 候选 `external_action_blocked=true` | 通过 |
| Canva dry-run `send_allowed=false` | 通过 |
| Canva dry-run `write_allowed=false` | 通过 |
| Canva dry-run `upload_allowed=false` | 通过 |
| Canva dry-run `external_action_blocked=true` | 通过 |
| route-check `provider_call_allowed=false` | 通过，3 个媒体/provider 均未调用 provider |
| route-check `real_media_generation_allowed=false` | 通过，未生成音频/图片/视频/HTML/PDF/PPT/文件 |
| key 读取/打印/写入 | 未发生 |

## 8. Top10 正式 L2 队列建议

| 排名 | candidate_id | 推荐原因 | 正式 L2 重点 |
| ---: | --- | --- | --- |
| 1 | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | 客服对话与宏缺口高频，read-only 风险低 | mock conversations/articles/macros 到 macro gap、升级建议、人工复核 |
| 2 | `quality_sprint05_helpscout_article_gap_readonly_candidate` | 客服知识库缺口高频，结构化输出清楚 | mailbox/docs mock rows 到 article gaps、handoff notes |
| 3 | `quality_sprint05_front_inbox_handoff_readonly_candidate` | 共享 inbox 交接场景高频，禁止写入边界清楚 | inbox messages 到 handoff summary、owner gap、risk tags |
| 4 | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | 营销活动健康高频，read-only 可控 | campaign metrics 到 health summary、unsubscribe/complaint flags |
| 5 | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | 电商商品目录 QC 高频，低真实动作风险 | products 到 missing fields、price/image/compliance risks |
| 6 | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | 与 WooCommerce 形成电商平台 adapter 组合 | catalog/variants 到 gap report、listing readiness |
| 7 | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | 广告预算与素材异常高价值，read-only 报表可控 | campaign report 到 budget/creative anomalies、no optimization action |
| 8 | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | 落地页掉点分析高频，适合经营/营销包 | GA4 report rows 到 dropoff summary、data quality flags |
| 9 | `quality_sprint05_canva_design_brief_dryrun_candidate` | 设计 brief dry-run 可封装，真实动作可硬阻断 | mock campaign brief 到 design brief、dry-run export spec、四个硬断言 |
| 10 | `quality_sprint05_jira_service_sla_readonly_candidate` | 服务台 SLA 与客服协同高频，read-only 风险低 | JSM requests/SLA 到 risk report、escalation suggestions |

## 9. 媒体 Provider Route-check 清单

| candidate_id | route-check 状态 | 主要检查 | 后续建议 |
| --- | --- | --- | --- |
| `quality_sprint05_openai_tts_support_voiceover_payload_candidate` | passed | TTS payload schema、voice/speaker rights、cost_cap、content_safety、audit_fields | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint05_fal_flux_product_image_payload_candidate` | passed | image payload schema、asset_policy、model_license_notes、cost_cap、content_safety | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint05_replicate_background_replace_payload_candidate` | passed | background replace payload、asset rights、model/output rights、cost_cap、content_safety | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |

## 10. 20 个候选 smoke 明细

| # | candidate_id | smoke_type | 中文 smoke 场景 | expected_inputs | expected_outputs | 权限边界 | 人工复核触发 | 禁止动作 | smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | read-only mock | 模拟 Intercom 对话、文章和宏，识别客服回复宏缺口 | `mock_conversations`, `mock_articles`, `mock_macros`, `policy_rules` | `macro_gaps`, `conversation_themes`, `handoff_suggestions`, `source_rows` | 不连 Intercom；`read_only=true`; `write_allowed=false`; `external_action_blocked=true` | 退款、账号安全、投诉升级、PII | 回复对话、更新工单、写宏、发消息 | passed |
| 2 | `quality_sprint05_helpscout_article_gap_readonly_candidate` | read-only mock | 模拟 Help Scout mailbox/docs，输出知识库文章缺口 | `mock_mailbox_rows`, `mock_docs`, `support_rules` | `article_gaps`, `faq_candidates`, `handoff_notes`, `source_rows` | 不连 Help Scout；只读；不写 docs/tag | 高投诉频次、政策冲突、敏感客户 | 回复客户、打 tag、写文档 | passed |
| 3 | `quality_sprint05_front_inbox_handoff_readonly_candidate` | read-only mock | 模拟 Front inbox messages，生成跨班次交接摘要 | `mock_messages`, `team_roster`, `handoff_rules` | `handoff_summary`, `owner_gaps`, `risk_tags`, `manual_review_required` | 不连 Front；不分配、不评论、不发消息 | VIP、未处理投诉、承诺日期 | 发送、分配、评论、写 inbox | passed |
| 4 | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | read-only mock | 模拟 Klaviyo campaign metrics，输出活动健康摘要 | `mock_campaign_metrics`, `audience_rules`, `benchmark_rules` | `campaign_health`, `open_click_notes`, `unsubscribe_flags`, `send_allowed=false` | 不连 Klaviyo；不发邮件；不改联系人 | 投诉/退订异常、隐私风险、样本过低 | 发送邮件、改联系人、改 campaign | passed |
| 5 | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | read-only mock | 模拟 WooCommerce 商品行，输出目录 QC | `mock_products`, `catalog_rules`, `qc_scope` | `catalog_qc`, `missing_fields`, `price_image_risks`, `source_rows` | 不连 WooCommerce；不改商品/订单/库存/价格 | 价格异常、禁售词、侵权素材 | 写商品、改库存、改价格、上下架 | passed |
| 6 | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | read-only mock | 模拟 BigCommerce catalog/variants，输出上架缺口 | `mock_catalog_rows`, `variant_rows`, `listing_rules` | `catalog_gaps`, `variant_issues`, `readiness_score`, `source_rows` | 不连 BigCommerce；只读；不写商品 | 变体缺失、库存敏感、合规词 | 写商品、改变体、改库存、发布 | passed |
| 7 | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | read-only mock | 模拟 Google Ads campaign report，识别预算/素材异常 | `mock_campaign_report`, `creative_rows`, `budget_rules` | `budget_anomalies`, `creative_flags`, `risk_notes`, `blocked_actions` | 不连 Google Ads；不改预算/出价/广告 | 花费异常、违规素材、ROAS 承诺 | 改 budget/bid/ad、自动优化投放 | passed |
| 8 | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | read-only mock | 模拟 GA4 landing page rows，输出掉点报告 | `mock_ga4_rows`, `funnel_rules`, `quality_rules` | `dropoff_summary`, `page_risks`, `data_quality_flags`, `source_rows` | 不连 GA4；不改 property/config | 样本过低、事件缺失、隐私维度 | 改 GA4 配置、读取真实用户明细 | passed |
| 9 | `quality_sprint05_canva_design_brief_dryrun_candidate` | dry-run | 模拟活动 brief，生成 Canva 设计 brief 与不可执行导出 spec | `mock_campaign_brief`, `brand_rules`, `asset_policy` | `design_brief`, `dry_run_export_spec`, `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | 不连 Canva；不创建/上传/导出 | 品牌/版权/商标/费用风险 | 创建设计、上传素材、导出、写 Canva | passed |
| 10 | `quality_sprint05_openai_tts_support_voiceover_payload_candidate` | route-check | 模拟客服培训脚本，生成 TTS payload schema | `mock_script`, `voice_policy`, `cost_limit`, `safety_policy` | `tts_payload`, `voice_rights_notes`, `cost_cap`, `content_safety`, `real_provider_smoke_required=true` | 不调用 TTS；不生成音频；不克隆声音 | 声音授权、敏感内容、费用上限 | 调 provider、生成音频、上传声音样本 | passed |
| 11 | `quality_sprint05_fal_flux_product_image_payload_candidate` | route-check | 模拟商品主图 brief，生成 fal FLUX image payload schema | `mock_product_brief`, `asset_policy`, `model_policy`, `cost_limit` | `image_payload`, `asset_rights_notes`, `cost_cap`, `content_safety`, `real_provider_smoke_required=true` | 不调用 fal；不生成图片；不上传素材 | 商品/商标/版权/费用风险 | 调 provider、上传素材、出图 | passed |
| 12 | `quality_sprint05_replicate_background_replace_payload_candidate` | route-check | 模拟商品图背景替换需求，生成 Replicate payload schema | `mock_asset_metadata`, `background_brief`, `rights_policy`, `cost_limit` | `background_replace_payload`, `rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 Replicate；不上传真实素材；不生成图片 | 素材授权、模型许可、输出权属 | 调 provider、上传素材、生成图片 | passed |
| 13 | `quality_sprint05_figma_design_token_audit_readonly_candidate` | read-only mock | 模拟 Figma nodes/tokens，输出设计 token 审计 | `mock_figma_nodes`, `token_rules`, `brand_rules` | `token_audit`, `inconsistencies`, `source_nodes`, `manual_review_required` | 不连 Figma；不编辑/导出文件 | 品牌规范冲突、设计系统变更 | 编辑文件、导出设计、上传素材 | passed |
| 14 | `quality_sprint05_asana_project_risk_readonly_candidate` | read-only mock | 模拟 Asana tasks，输出项目风险摘要 | `mock_tasks`, `dependency_rules`, `owner_rules` | `project_risks`, `blocked_tasks`, `owner_gaps`, `source_task_ids` | 不连 Asana；不写任务/评论/状态 | 高优先级逾期、负责人缺失 | 写任务、评论、改负责人/状态 | passed |
| 15 | `quality_sprint05_trello_board_handoff_readonly_candidate` | read-only mock | 模拟 Trello cards，输出交接摘要 | `mock_cards`, `list_rules`, `handoff_rules` | `handoff_summary`, `stale_cards`, `owner_notes`, `blocked_actions` | 不连 Trello；不写卡片/评论/列表 | 客户承诺、逾期、责任不清 | 移动卡片、评论、改列表 | passed |
| 16 | `quality_sprint05_jira_service_sla_readonly_candidate` | read-only mock | 模拟 JSM requests/SLA，输出服务 SLA 风险 | `mock_requests`, `sla_rows`, `service_rules` | `sla_risks`, `escalation_suggestions`, `impact_notes`, `source_rows` | 不连 Jira；不写 request/issue/comment | SLA 超时、重大客户、服务中断 | 写 issue、评论、改状态 | passed |
| 17 | `quality_sprint05_confluence_policy_gap_readonly_candidate` | read-only mock | 模拟 Confluence pages，识别政策文档缺口 | `mock_pages`, `policy_topics`, `freshness_rules` | `policy_gaps`, `outdated_pages`, `article_briefs`, `source_pages` | 不连 Confluence；不写页面/评论/权限 | 过期政策、合规冲突、HR/财务敏感 | 写页面、评论、改权限 | passed |
| 18 | `quality_sprint05_bamboohr_onboarding_gap_readonly_candidate` | read-only mock | 模拟 BambooHR onboarding rows，输出入职缺口 | `mock_onboarding_rows`, `checklist_rules`, `privacy_rules` | `onboarding_gaps`, `missing_steps`, `privacy_flags`, `manual_review_required` | 不连 BambooHR；不写员工记录 | 员工 PII、入职合规、薪酬敏感 | 写员工记录、做 HR 决策 | passed |
| 19 | `quality_sprint05_greenhouse_candidate_packet_readonly_candidate` | read-only mock | 模拟 Greenhouse candidate rows，生成候选人 packet 摘要 | `mock_candidate_rows`, `job_rows`, `privacy_rules` | `candidate_packet`, `privacy_flags`, `missing_materials`, `not_hiring_decision=true` | 不连 Greenhouse；不写 note；不做录用/淘汰判断 | PII、歧视风险、录用判断 | 写候选人记录、录用/淘汰、发送邮件 | passed |
| 20 | `quality_sprint05_docusign_contract_status_readonly_candidate` | read-only mock | 模拟 DocuSign envelopes，输出合同签署状态摘要 | `mock_envelopes`, `contract_rules`, `risk_rules` | `contract_status_summary`, `stalled_envelopes`, `risk_flags`, `source_rows` | 不连 DocuSign；不发送/签署/写 envelope | 合同逾期、金额条款、签署方异常 | 发送合同、签署、修改 envelope | passed |

## 11. 排除项确认

| candidate_id | 状态 | 本轮处理 |
| --- | --- | --- |
| `quality_sprint05_pika_video_ad_payload_route_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint05_openclaw_ui_ux_pro_max_skill_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint05_openagentskills_guizang_ppt_brief_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint05_open_design_design_brief_child_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint05_agency_agents_zh_hr_recruiting_role_component_candidate` | component_only / role component | 未处理 |

## 12. 权限边界确认

- 未安装依赖。
- 未访问外网或真实账号。
- 未调用真实 API/provider。
- 未读取、打印或写入 key。
- 未读取客户真实文件。
- 未上传素材。
- 未发送邮件、短信、微信、Slack、Outlook、Gmail 或其他消息。
- 未写 CRM/POS/财务/HR/协作/电商/广告/签约系统。
- 未抓取真实网页。
- 未生成真实图片、视频、音频、HTML、PDF、PPT 或任何文件。
- 未退款、未赔偿、未扣款、未改库存、未改订阅、未写账、未报税、未创建任务、未共享文件。
- 未修改稳交付库；客户正式可调用 Skill 仍为 13。
