# LICENSE_REVIEW_QUALITY_SPRINT_04_RESULT

更新日期: 2026-06-05

## Summary

本文件为 Quality Sprint 04 的轻量 L1 / trial mode 复核结果。许可证窗口已完成分类判断但长时间未落盘；指挥中心根据许可证窗口已回传的判断补落本文件，供测试台继续执行 candidate smoke。

本轮不代表正式法务意见，不代表 DeepAgents smoke 通过，不代表 L2 通过，不代表可封装，不代表客户正式可调用。客户正式可调用 Skill 仍为 13。

## Counts

| L1 结论 | 数量 |
| --- | ---: |
| `can_mock_smoke` | 11 |
| `can_dry_run_smoke` | 1 |
| `can_route_check` | 7 |
| `component_only` | 1 |
| `needs_more_license_info` | 5 |
| `blocked` | 0 |
| 可送 DeepAgents candidate smoke | 19 |

## L1 Result Table

| candidate_id | L1 结论 | trial_mode | 许可证/条款状态 | 主要风险 | 是否入 smoke |
| --- | --- | --- | --- | --- | --- |
| `quality_sprint04_zendesk_sla_macro_gap_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Zendesk API 条款需后续真实 Harness 前复核；本轮可 mock | 工单隐私、macro/help-center 只读 scope、不得写入/回复 | yes |
| `quality_sprint04_freshdesk_ticket_sla_risk_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Freshdesk API 条款需后续真实 Harness 前复核；本轮可 mock | 工单隐私、SLA 只读 scope、不得回复/更新状态 | yes |
| `quality_sprint04_salesforce_opportunity_hygiene_dryrun_candidate` | `can_dry_run_smoke` | `dry_run_only` | Salesforce API/OAuth 条款需后续真实 Harness 前复核；本轮可 dry-run | CRM 隐私、不得写商机/联系人/任务/邮件 | yes |
| `quality_sprint04_shopline_catalog_qc_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Shopline Open API 条款需后续真实 Harness 前复核；本轮可 mock | 商品数据隐私、不得写商品/库存/价格 | yes |
| `quality_sprint04_lightspeed_pos_shift_anomaly_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Lightspeed API 条款需后续真实 Harness 前复核；本轮可 mock | POS/订单/支付数据敏感、不得退款/改库存 | yes |
| `quality_sprint04_xero_bank_reconcile_exception_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Xero API 条款需后续真实 Harness 前复核；本轮可 mock | 财务隐私、非审计/非税务结论、不得写账/付款 | yes |
| `quality_sprint04_posthog_funnel_dropoff_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | PostHog API 条款需后续真实 Harness 前复核；本轮可 mock | 用户行为数据隐私、不得改 tracking 配置 | yes |
| `quality_sprint04_linear_customer_bug_triage_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Linear API 条款需后续真实 Harness 前复核；本轮可 mock | issue 隐私、不得改状态/评论/创建任务 | yes |
| `quality_sprint04_runway_video_ad_payload_candidate` | `can_route_check` | `route_check` | Runway provider/API 条款需真实 provider smoke 前复核；本轮只查 route/payload | 商用输出权、素材上传/存储、费用上限、内容安全 | yes |
| `quality_sprint04_heygen_avatar_training_payload_candidate` | `can_route_check` | `route_check` | HeyGen provider/API 条款需真实 provider smoke 前复核；本轮只查 route/payload | 肖像/声音授权、数字人素材、费用上限、内容安全 | yes |
| `quality_sprint04_synthesia_hr_training_video_payload_candidate` | `can_route_check` | `route_check` | Synthesia provider/API 条款需真实 provider smoke 前复核；本轮只查 route/payload | avatar 权利、商用输出、费用上限、内容安全 | yes |
| `quality_sprint04_recraft_brand_asset_payload_candidate` | `can_route_check` | `route_check` | Recraft provider/API 条款需真实 provider smoke 前复核；本轮只查 route/payload | 商用输出权、品牌素材、费用上限、内容安全 | yes |
| `quality_sprint04_ideogram_poster_copy_image_payload_candidate` | `can_route_check` | `route_check` | Ideogram provider/API 条款需真实 provider smoke 前复核；本轮只查 route/payload | 文字海报输出权、商标/版权/素材授权、费用上限 | yes |
| `quality_sprint04_pika_short_video_payload_candidate` | `needs_more_license_info` | `metadata_or_route_check` | route/API 与商用条款未充分定位 | provider route 不清、商用输出/费用/素材上传边界不清 | no |
| `quality_sprint04_tavus_sales_avatar_payload_candidate` | `can_route_check` | `route_check` | Tavus provider/API 条款需真实 provider smoke 前复核；本轮只查 route/payload | 肖像/声音同意、不得外发、费用上限、内容安全 | yes |
| `quality_sprint04_did_avatar_support_script_payload_candidate` | `can_route_check` | `route_check` | D-ID provider/API 条款需真实 provider smoke 前复核；本轮只查 route/payload | face/voice rights、上传/存储、费用上限、内容安全 | yes |
| `quality_sprint04_omniskill_support_qa_child_locator_candidate` | `needs_more_license_info` | `metadata_only` | 缺具体 repo/subdir/SKILL.md/LICENSE | 只凭 registry 页面不能放行 callable smoke | no |
| `quality_sprint04_openagentskills_ui_ux_pro_max_candidate` | `needs_more_license_info` | `metadata_only` | 缺具体 GitHub repo/subdir/LICENSE/工具边界 | 只凭 marketplace 页面不能放行 callable smoke | no |
| `quality_sprint04_openagentskills_guizang_ppt_candidate` | `needs_more_license_info` | `metadata_only` | 缺具体 repo/subdir/LICENSE；需确认 PPT/HTML artifact 写入边界 | 文件生成/导出边界不清 | no |
| `quality_sprint04_wondelai_skill_pack_locator_candidate` | `needs_more_license_info` | `metadata_only` | 缺子目录清单、LICENSE 与可商用证据 | 需先定位具体 child skill | no |
| `quality_sprint04_monday_board_health_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | monday.com API 条款需后续真实 Harness 前复核；本轮可 mock | board 隐私、不得写 item/comment/status | yes |
| `quality_sprint04_clickup_task_risk_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | ClickUp API 条款需后续真实 Harness 前复核；本轮可 mock | task 隐私、不得写任务/评论 | yes |
| `quality_sprint04_mailchimp_campaign_health_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Mailchimp API 条款需后续真实 Harness 前复核；本轮可 mock | audience 隐私、不得发送/改名单 | yes |
| `quality_sprint04_brevo_email_campaign_health_readonly_candidate` | `can_mock_smoke` | `read_only_mock` | Brevo API 条款需后续真实 Harness 前复核；本轮可 mock | 联系人隐私、不得发送/改联系人 | yes |
| `quality_sprint04_agency_agents_zh_sales_ops_role_component_candidate` | `component_only` | `role_smoke_component` | 需继续确认角色库 LICENSE 与内容边界 | 仅 role/component，不作为普通 candidate smoke 或 draft L3 | no |

## Smoke Queue Policy

可送 smoke 的 19 个候选包括：

- 11 个 `can_mock_smoke`：SaaS/API read-only mock。
- 1 个 `can_dry_run_smoke`：Salesforce dry-run。
- 7 个 `can_route_check`：媒体/provider route/config/payload check。

不送普通 candidate smoke：

- `quality_sprint04_pika_short_video_payload_candidate`：暂缓，provider route/API/条款不清。
- 4 个标准 Skill/registry locator：暂缓，缺具体 child skill / repo / LICENSE / manifest。
- `quality_sprint04_agency_agents_zh_sales_ops_role_component_candidate`：组件/角色资产，不进入普通 candidate smoke。

## Hard Boundaries

- 不安装依赖。
- 不调用真实 API/provider。
- 不访问真实账号。
- 不读取、打印或写入 key。
- 不读取客户真实文件。
- 不上传素材。
- 不发送邮件、短信、微信、Slack、CRM 消息或平台通知。
- 不写 CRM/POS/财务/HR/协作系统。
- 不生成真实图片、视频、音频、HTML、PDF、PPT 或文件。
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。
- 不修改稳交付库。
- 客户正式可调用 Skill 仍为 13。

