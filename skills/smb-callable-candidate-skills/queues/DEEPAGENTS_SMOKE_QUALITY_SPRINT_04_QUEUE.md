# DEEPAGENTS_SMOKE_QUALITY_SPRINT_04_QUEUE

更新日期: 2026-06-05

## Source

- L1 结果: `../LICENSE_REVIEW_QUALITY_SPRINT_04_RESULT.md`
- 可送 DeepAgents candidate smoke: 19
- 客户正式可调用 Skill: 13

## Queue

| # | candidate_id | L1 结论 | trial_mode | smoke_focus | hard_assertions |
| ---: | --- | --- | --- | --- | --- |
| 1 | `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock Zendesk tickets/macros/help-center rows -> SLA 风险、macro 缺口、人工升级建议 | read_only=true; write_allowed=false; send_allowed=false; external_action_blocked=true |
| 2 | `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock Freshdesk tickets/SLA rows -> 超时风险、升级建议、风险标签 | read_only=true; write_allowed=false; send_allowed=false; external_action_blocked=true |
| 3 | `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | `can_dry_run_smoke` | `dry_run_only` | mock opportunities/accounts -> 商机健康度和不可执行 dry-run payload | send_allowed=false; write_allowed=false; upload_allowed=false; external_action_blocked=true |
| 4 | `quality_sprint04_shopline_catalog_qc_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock products/catalog rows -> 商品字段缺口、标题/图片/价格风险 | read_only=true; write_allowed=false; inventory_write_allowed=false; external_action_blocked=true |
| 5 | `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock POS shift rows -> 销售/退货/库存异常摘要 | read_only=true; refund_allowed=false; inventory_write_allowed=false; external_action_blocked=true |
| 6 | `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock transactions/invoices -> 对账异常提示，非审计/非税务声明 | read_only=true; payment_allowed=false; accounting_write_allowed=false; external_action_blocked=true |
| 7 | `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock funnel/event stats -> 漏斗掉点、转化异常、数据质量 | read_only=true; tracking_config_write_allowed=false; external_action_blocked=true |
| 8 | `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock issues/customer feedback -> 影响范围、优先级、客服回传建议 | read_only=true; issue_write_allowed=false; comment_allowed=false; external_action_blocked=true |
| 9 | `quality_sprint04_runway_video_ad_payload_candidate` | `can_route_check` | `route_check` | mock ad brief -> video provider payload schema、成本上限、内容安全字段 | real_generation_allowed=false; upload_allowed=false; provider_call_allowed=false; external_action_blocked=true |
| 10 | `quality_sprint04_heygen_avatar_training_payload_candidate` | `can_route_check` | `route_check` | mock training script -> avatar video payload schema、肖像/声音授权字段、成本上限 | real_generation_allowed=false; upload_allowed=false; provider_call_allowed=false; external_action_blocked=true |
| 11 | `quality_sprint04_synthesia_hr_training_video_payload_candidate` | `can_route_check` | `route_check` | mock HR training brief -> video payload schema、avatar 权利、安全字段 | real_generation_allowed=false; upload_allowed=false; provider_call_allowed=false; external_action_blocked=true |
| 12 | `quality_sprint04_recraft_brand_asset_payload_candidate` | `can_route_check` | `route_check` | mock campaign brief -> image payload schema、品牌素材授权、输出权字段 | real_generation_allowed=false; upload_allowed=false; provider_call_allowed=false; external_action_blocked=true |
| 13 | `quality_sprint04_ideogram_poster_copy_image_payload_candidate` | `can_route_check` | `route_check` | mock poster/menu brief -> text poster image payload schema、商标/版权/成本字段 | real_generation_allowed=false; upload_allowed=false; provider_call_allowed=false; external_action_blocked=true |
| 14 | `quality_sprint04_tavus_sales_avatar_payload_candidate` | `can_route_check` | `route_check` | mock sales pitch script -> avatar payload schema、同意/肖像/声音字段 | real_generation_allowed=false; upload_allowed=false; provider_call_allowed=false; send_allowed=false; external_action_blocked=true |
| 15 | `quality_sprint04_did_avatar_support_script_payload_candidate` | `can_route_check` | `route_check` | mock support training script -> avatar payload schema、face/voice rights、内容安全 | real_generation_allowed=false; upload_allowed=false; provider_call_allowed=false; external_action_blocked=true |
| 16 | `quality_sprint04_monday_board_health_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock monday board items -> 逾期事项、负责人缺口、项目健康 | read_only=true; write_allowed=false; comment_allowed=false; external_action_blocked=true |
| 17 | `quality_sprint04_clickup_task_risk_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock ClickUp tasks -> 延期、阻塞、跨部门交接风险 | read_only=true; write_allowed=false; comment_allowed=false; external_action_blocked=true |
| 18 | `quality_sprint04_mailchimp_campaign_health_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock campaign reports -> 打开率/退订/投放健康摘要，不发送 | read_only=true; send_allowed=false; contact_write_allowed=false; external_action_blocked=true |
| 19 | `quality_sprint04_brevo_email_campaign_health_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | mock campaign stats -> 邮件活动健康与风险，不发送、不改联系人 | read_only=true; send_allowed=false; contact_write_allowed=false; external_action_blocked=true |

## Excluded From This Smoke

| candidate_id | status | reason |
| --- | --- | --- |
| `quality_sprint04_pika_short_video_payload_candidate` | `needs_more_license_info` | provider route/API/商用条款/费用/素材上传边界未充分定位 |
| `quality_sprint04_omniskill_support_qa_child_locator_candidate` | `needs_more_license_info` | 缺具体 repo/subdir/SKILL.md/LICENSE |
| `quality_sprint04_openagentskills_ui_ux_pro_max_candidate` | `needs_more_license_info` | 缺具体 GitHub repo/subdir/LICENSE/工具边界 |
| `quality_sprint04_openagentskills_guizang_ppt_candidate` | `needs_more_license_info` | 缺具体 repo/subdir/LICENSE；PPT/HTML artifact 写入边界不清 |
| `quality_sprint04_wondelai_skill_pack_locator_candidate` | `needs_more_license_info` | 缺子目录清单、LICENSE 与可商用证据 |
| `quality_sprint04_agency_agents_zh_sales_ops_role_component_candidate` | `component_only` | 角色/组件资产，不进入普通 candidate smoke 或 draft L3 |

## Shared Boundaries

- 不安装依赖。
- 不访问外网或真实账号。
- 不调用真实 API/provider。
- 不读取、打印、写入 key。
- 不读取客户文件。
- 不上传素材。
- 不发送或发布。
- 不写 CRM/POS/财务/HR/协作系统。
- 不生成真实图片、视频、音频、HTML、PDF、PPT 或文件。
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。
- 不改稳交付库。
- DeepAgents smoke 通过只代表候选库可继续试跑，不代表 L2 通过、封装通过或客户正式可调用。

