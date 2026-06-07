# DEEPAGENTS_SMOKE_QUALITY_SPRINT_04_RESULT

回传日期：2026-06-05

本轮性质：Quality Sprint 04 DeepAgents candidate-level metadata/mock/dry-run/route-check smoke。  
测试范围：仅测试 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_04_QUEUE.md` 内 19 个候选；排除 5 个 needs_more_license_info 与 1 个 component_only。  
结论边界：DeepAgents smoke passed 只代表候选库可继续试跑，不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_04_RESULT.md`。
- 已读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_04_QUEUE.md`。
- 已对 smoke 队列内 19 个候选完成 metadata/mock/dry-run/route-check smoke。
- 已为每个候选记录中文六部门 mock/dry-run/route-check 场景、callable 表达、输入输出 schema、中文可用性、人工复核触发、禁止动作与 smoke_status。
- 已生成 Top10 正式 L2 simulated 队列建议：`queues/L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_04_QUEUE.md`。

## 2. 当前问题

- 7 个媒体/provider 候选仅完成 route/config/payload schema check，未真实调用 provider，未生成图片/视频/音频/HTML/PDF/PPT/文件，不得写成真实 provider 通过。
- SaaS/API connector 类仅完成 mock/read-only/dry-run smoke，未连接真实账号，未写 CRM/POS/财务/HR/协作系统。
- Mailchimp/Brevo 两个营销活动健康候选 smoke passed，但本轮 Top10 优先客服、销售、电商、POS、财务、产品运营和项目协同高频项，暂列候补。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 无外部网络、真实账号、真实 API/provider、真实客户文件、上传、发送、抓取、退款/赔偿/扣款、库存修改、订阅修改、写账/报税或写业务系统动作。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Sprint04 Top10 进入正式 L2 simulated。
- 是否为 7 个媒体/provider route-check passed 候选另建真实 provider smoke 审批队列。
- 是否要求研究/许可证窗口继续补齐 5 个 needs_more_license_info 候选的具体 child skill / repo / LICENSE / manifest / provider 边界。
- 是否将 `quality_sprint04_agency_agents_zh_sales_ops_role_component_candidate` 继续固定为 component_only，不进入普通 candidate smoke。

## 5. 建议下一步

- 将 Top10 非媒体、低真实动作风险、read-only/dry-run 候选送正式 L2 simulated。
- 媒体/provider 项仅保留 route-check passed，不进入正式 L2 通过或封装判断。
- 真实 Harness 前继续要求所有 read-only 候选提供最小授权 scope；dry-run 候选必须保留 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 19 |
| `failed` | 0 |
| `needs_fix` | 0 |
| `blocked` | 0 |

| smoke_type | 数量 |
| --- | ---: |
| `can_mock_smoke` / `read_only_mock` | 11 |
| `can_dry_run_smoke` / `dry_run_only` | 1 |
| `can_route_check` / `route_check` | 7 |

## 7. Dry-run / Read-only / Route-check 硬断言

| 检查项 | 结果 |
| --- | --- |
| read-only 候选 `read_only=true` | 通过；所有 SaaS/API mock 候选均仅使用 mock rows |
| dry-run `send_allowed=false` | 通过；Salesforce dry-run 禁止发送 |
| dry-run `write_allowed=false` | 通过；Salesforce dry-run 禁止写商机、联系人、任务、邮件 |
| dry-run `upload_allowed=false` | 通过；Salesforce dry-run 禁止上传 |
| route-check `provider_call_allowed=false` | 通过；7 个媒体/provider 均未调用 provider |
| route-check `real_generation_allowed=false` | 通过；未生成图片/视频/音频/HTML/PDF/PPT/文件 |
| `external_action_blocked=true` | 通过；所有 19 个候选均阻断外部动作 |
| key 读取/打印/写入 | 未发生 |

## 8. Top10 正式 L2 队列建议

| 排名 | candidate_id | 推荐原因 | 正式 L2 重点 |
| ---: | --- | --- | --- |
| 1 | `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | 客服 SLA 与宏缺口高频，read-only 风险低 | ticket/macro/help-center mock rows 到 SLA 风险、macro 缺口、升级建议 |
| 2 | `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | 客服工单 SLA 风险高频，与 Zendesk 形成渠道 adapter | 超时风险、升级建议、风险标签，不回复/不改状态 |
| 3 | `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | 销售商机卫生高频，dry-run payload 可控 | 商机健康、缺字段、不可执行 payload，四个硬断言 |
| 4 | `quality_sprint04_shopline_catalog_qc_readonly_candidate` | 电商商品目录 QC 高频，中文/跨境场景补充 | 商品字段缺口、标题/图片/价格风险，不写商品/库存 |
| 5 | `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | 门店 POS 班次异常高频，经营报表价值明显 | 销售/退货/库存异常摘要，不退款/不改库存 |
| 6 | `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | 财务对账异常高频，低动作风险 | 银行/发票/交易异常提示，非审计/非税务声明 |
| 7 | `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | 产品/增长漏斗分析高频，read-only 数据可 mock | funnel dropoff、转化异常、数据质量提示 |
| 8 | `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | 客服反馈到产品 bug 分流高频 | issue 影响范围、优先级、客服回传建议，不写 issue |
| 9 | `quality_sprint04_monday_board_health_readonly_candidate` | 项目协同 board 健康高频 | 逾期事项、负责人缺口、项目健康，不写 item/comment |
| 10 | `quality_sprint04_clickup_task_risk_readonly_candidate` | 任务风险/跨部门交接高频 | 延期、阻塞、跨部门交接风险，不写任务/comment |

## 9. 媒体 Provider Route-check 清单

| candidate_id | route-check 状态 | 主要检查 | 后续建议 |
| --- | --- | --- | --- |
| `quality_sprint04_runway_video_ad_payload_candidate` | passed | video payload schema、cost_cap、content_safety | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint04_heygen_avatar_training_payload_candidate` | passed | avatar payload、肖像/声音授权、cost_cap | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint04_synthesia_hr_training_video_payload_candidate` | passed | HR training video payload、avatar rights、安全字段 | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint04_recraft_brand_asset_payload_candidate` | passed | image payload、品牌素材授权、输出权字段 | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint04_ideogram_poster_copy_image_payload_candidate` | passed | poster/menu image payload、商标/版权/成本字段 | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint04_tavus_sales_avatar_payload_candidate` | passed | sales avatar payload、同意/肖像/声音字段 | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |
| `quality_sprint04_did_avatar_support_script_payload_candidate` | passed | avatar support script payload、face/voice rights、安全字段 | 真实 provider smoke 待审批，`real_provider_smoke_required=true` |

## 10. 19 个候选 smoke 明细

| # | candidate_id | smoke_type | 中文 smoke 场景 | expected_inputs | expected_outputs | 权限边界 | 人工复核触发 | 禁止动作 | smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | read-only mock | 模拟 Zendesk tickets/macros/help-center rows，生成 SLA 风险与 macro 缺口 | `mock_tickets`, `mock_macros`, `help_center_rows`, `sla_rules` | `sla_risks`, `macro_gaps`, `handoff_suggestions`, `source_rows` | 不连 Zendesk；不写回复/状态 | SLA 将超时、投诉、退款、账号安全 | 回复工单、更新状态、写 macro | passed |
| 2 | `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | read-only mock | 模拟 Freshdesk tickets/SLA rows，输出超时风险和升级建议 | `mock_tickets`, `sla_rows`, `support_rules` | `overdue_risks`, `priority`, `risk_tags`, `manual_review_required` | 不连 Freshdesk；不回复/改状态 | 超时、高价值客户、投诉升级 | 回复工单、改状态、写系统 | passed |
| 3 | `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | dry-run | 模拟 Salesforce opportunities/accounts，生成商机健康 dry-run payload | `mock_opportunities`, `mock_accounts`, `hygiene_rules` | `hygiene_report`, `missing_fields`, `dry_run_payload`, `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | 不连 Salesforce；不写 CRM | 大额商机、缺关键字段、PII | 写商机/联系人/任务、发邮件、上传 | passed |
| 4 | `quality_sprint04_shopline_catalog_qc_readonly_candidate` | read-only mock | 模拟 Shopline catalog rows，生成商品字段 QC | `mock_products`, `catalog_rules`, `qc_scope` | `catalog_summary`, `missing_fields`, `price_image_risks`, `source_rows` | 不连 Shopline；不写商品/库存/价格 | 价格缺失、库存异常、图片风险 | 写商品、改库存/价格、发布 | passed |
| 5 | `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | read-only mock | 模拟 Lightspeed POS shift rows，生成班次异常摘要 | `mock_shift_rows`, `pos_rules`, `date_range` | `shift_summary`, `sales_anomalies`, `refund_flags`, `inventory_notes` | 不连 POS；不退款、不改库存 | 退款异常、支付异常、交班差异 | 退款、改库存、写 POS | passed |
| 6 | `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | read-only mock | 模拟 Xero transactions/invoices，输出对账异常 | `mock_transactions`, `mock_invoices`, `reconcile_rules` | `reconcile_exceptions`, `matched_items`, `risk_flags`, `not_audit_or_tax_advice=true` | 不连 Xero；不写账/付款 | 金额不一致、重复交易、税务敏感 | 写账、付款、报税、审计结论 | passed |
| 7 | `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | read-only mock | 模拟 PostHog funnel/event stats，输出漏斗掉点 | `mock_funnel_stats`, `event_schema`, `quality_rules` | `dropoff_summary`, `conversion_anomalies`, `data_quality_flags`, `source_rows` | 不连 PostHog；不改 tracking | 样本量低、事件缺失、转化异常 | 改 tracking 配置、写事件 | passed |
| 8 | `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | read-only mock | 模拟 Linear issues/customer feedback，输出 bug triage | `mock_issues`, `customer_feedback`, `triage_rules` | `impact_summary`, `priority`, `support_notes`, `risk_flags` | 不连 Linear；不写 issue/comment | 关键客户、数据丢失、安全 bug | 写 issue、评论、改状态、创建任务 | passed |
| 9 | `quality_sprint04_runway_video_ad_payload_candidate` | route-check | 模拟短视频广告 brief，生成 Runway payload schema | `mock_ad_brief`, `storyboard`, `asset_policy`, `cost_limit` | `provider_payload`, `cost_cap`, `content_safety`, `real_provider_smoke_required=true` | 不调用 Runway；不生成视频 | 素材授权、费用、内容安全 | provider 调用、上传素材、生成视频 | passed |
| 10 | `quality_sprint04_heygen_avatar_training_payload_candidate` | route-check | 模拟培训脚本，生成 HeyGen avatar payload schema | `mock_training_script`, `avatar_policy`, `voice_policy`, `cost_limit` | `avatar_payload`, `consent_required`, `content_safety`, `real_provider_smoke_required=true` | 不调用 HeyGen；不生成视频 | 肖像/声音授权、HR 内容敏感 | provider 调用、上传素材、生成视频 | passed |
| 11 | `quality_sprint04_synthesia_hr_training_video_payload_candidate` | route-check | 模拟 HR 培训 brief，生成 Synthesia video payload schema | `mock_hr_brief`, `avatar_rights`, `content_policy`, `cost_limit` | `video_payload`, `avatar_rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 Synthesia；不生成视频 | avatar 权利、HR 合规、费用 | provider 调用、生成视频、发布 | passed |
| 12 | `quality_sprint04_recraft_brand_asset_payload_candidate` | route-check | 模拟品牌活动 brief，生成 Recraft image payload schema | `mock_campaign_brief`, `brand_asset_policy`, `cost_limit` | `image_payload`, `rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 Recraft；不生成图片 | 品牌素材授权、商标、版权 | provider 调用、上传素材、出图 | passed |
| 13 | `quality_sprint04_ideogram_poster_copy_image_payload_candidate` | route-check | 模拟菜单/海报 brief，生成 Ideogram payload schema | `mock_poster_brief`, `text_requirements`, `rights_policy`, `cost_limit` | `poster_payload`, `text_render_risks`, `cost_cap`, `real_provider_smoke_required=true` | 不调用 Ideogram；不生成海报 | 中文文字、商标/版权、费用 | provider 调用、出图、发布 | passed |
| 14 | `quality_sprint04_tavus_sales_avatar_payload_candidate` | route-check | 模拟销售口播脚本，生成 Tavus avatar payload schema | `mock_sales_script`, `consent_policy`, `voice_policy`, `cost_limit` | `avatar_payload`, `consent_required`, `send_allowed=false`, `real_provider_smoke_required=true` | 不调用 Tavus；不生成/外发视频 | 肖像/声音同意、销售承诺 | provider 调用、生成视频、发送 | passed |
| 15 | `quality_sprint04_did_avatar_support_script_payload_candidate` | route-check | 模拟客服培训脚本，生成 D-ID avatar payload schema | `mock_support_script`, `face_voice_policy`, `content_policy`, `cost_limit` | `avatar_payload`, `rights_notes`, `content_safety`, `real_provider_smoke_required=true` | 不调用 D-ID；不生成视频 | face/voice rights、内容安全 | provider 调用、上传素材、生成视频 | passed |
| 16 | `quality_sprint04_monday_board_health_readonly_candidate` | read-only mock | 模拟 monday board items，输出项目健康摘要 | `mock_board_items`, `status_rules`, `owner_rules` | `board_health`, `overdue_items`, `owner_gaps`, `risk_flags` | 不连 monday；不写 item/comment/status | 逾期、负责人缺失、高优先级项目 | 写 item、评论、改状态 | passed |
| 17 | `quality_sprint04_clickup_task_risk_readonly_candidate` | read-only mock | 模拟 ClickUp tasks，输出任务风险 | `mock_tasks`, `dependency_rules`, `handoff_rules` | `task_risks`, `blocked_items`, `handoff_notes`, `manual_review_required` | 不连 ClickUp；不写任务/comment | 延期、阻塞、跨部门交接 | 写任务、评论、改状态 | passed |
| 18 | `quality_sprint04_mailchimp_campaign_health_readonly_candidate` | read-only mock | 模拟 Mailchimp campaign reports，输出投放健康摘要 | `mock_campaign_reports`, `audience_rules`, `benchmark_rules` | `campaign_health`, `open_click_notes`, `unsubscribe_flags`, `send_allowed=false` | 不连 Mailchimp；不发邮件/改名单 | 退订异常、隐私、投放承诺 | 发送邮件、改受众、写 campaign | passed |
| 19 | `quality_sprint04_brevo_email_campaign_health_readonly_candidate` | read-only mock | 模拟 Brevo campaign stats，输出邮件活动风险 | `mock_campaign_stats`, `contact_rules`, `benchmark_rules` | `campaign_summary`, `risk_flags`, `contact_health_notes`, `send_allowed=false` | 不连 Brevo；不发邮件/改联系人 | 退订/投诉、联系人隐私、低样本 | 发送邮件、改联系人、写 campaign | passed |

## 11. 排除项确认

| candidate_id | 状态 | 本轮处理 |
| --- | --- | --- |
| `quality_sprint04_pika_short_video_payload_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint04_omniskill_support_qa_child_locator_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint04_openagentskills_ui_ux_pro_max_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint04_openagentskills_guizang_ppt_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint04_wondelai_skill_pack_locator_candidate` | needs_more_license_info | 未处理 |
| `quality_sprint04_agency_agents_zh_sales_ops_role_component_candidate` | component_only | 未处理 |

## 12. 权限边界确认

- 未安装依赖。
- 未访问外网或真实账号。
- 未调用真实 API/provider。
- 未读取、打印或写入 key。
- 未读取客户真实文件。
- 未上传素材。
- 未发送或发布。
- 未写 CRM/POS/财务/HR/协作系统。
- 未抓取真实网页。
- 未生成真实图片、视频、音频、HTML、PDF、PPT 或文件。
- 未退款、未赔偿、未扣款、未改库存、未改订阅、未写账、未报税、未创建任务、未共享文件。
- 未改稳交付库；客户正式可调用 Skill 仍为 13。
