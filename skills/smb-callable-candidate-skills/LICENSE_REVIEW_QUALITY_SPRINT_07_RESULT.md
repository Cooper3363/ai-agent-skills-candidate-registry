# LICENSE_REVIEW_QUALITY_SPRINT_07_RESULT

回传日期：2026-06-05

## 1. 已完成事项

- 已读取 `QUALITY_SOURCE_SPRINT_07_RESULT.md` 与 `queues/LICENSE_REVIEW_QUALITY_SPRINT_07_QUEUE.md`。
- 已对队列中的 25 个优先候选完成轻量 L1 / trial mode 复核。
- 已生成 DeepAgents candidate smoke 队列：`queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_07_QUEUE.md`。
- 本轮未安装依赖、未调用真实 API/provider、未生成图片/视频/音频/PPT/PDF/真实文件、未读取/打印/写入 key、未访问真实账号、未读取客户文件、未上传素材、未修改稳交付库。

## 2. 当前问题

- SaaS/API connector 候选只能进入 `read_only_mock`，不连接真实账号、不写系统、不发送、不上传。
- 媒体/provider 候选只能进入 `route_check` 或 `dry_run_payload_only`，不真实生成图片、视频、音频或文件。
- 标准 SKILL.md 包必须补齐 LICENSE / 商用条款 / manifest 或 frontmatter / 文件写入边界；本轮 5 个标准包均暂缓，不进入普通 smoke。
- role/component/template 只能作组件或角色资产，不声明客户正式可调用，不进入 draft L3。
- 客户正式可调用 Skill 仍为 13。

## 3. 阻塞原因

- 无权限阻塞。
- `blocked_by_license` 数量为 0。
- `needs_more_license_info` 数量为 5：标准 SKILL.md / registry 候选缺 LICENSE、具体 repo/subdir 或文件输出边界。
- `component_only` 数量为 4：2 个 agency role、promptfoo eval component、Instructor schema component。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 16 个 `allow_smoke` 项进入 DeepAgents candidate smoke，仅限 read-only/mock 或 route/payload check。
- 是否要求研究窗口补齐 5 个标准 Skill 包的 LICENSE、manifest、依赖和文件写入/外部抓取边界。
- 是否将 role/component 项转交 role/component smoke 专线，而非普通 candidate smoke。

## 5. 建议下一步

- 测试台读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_07_QUEUE.md`，只处理 16 个放行项。
- 媒体项进入 route/config/payload check；真实 provider smoke 另走审批。
- SaaS/API 项仅用 mock rows/messages/reports；不得 OAuth 真实租户或写系统。
- 暂缓项补证后再开补充 L1，不送 L2、不封装、不客户调用。

## 6. 数量汇总

| L1 结论 | 数量 |
| --- | ---: |
| `allow_smoke` | 16 |
| `needs_more_license_info` | 5 |
| `blocked_by_license` | 0 |
| `component_only` | 4 |
| `market_lead_or_retire` | 0 |

| trial mode | 数量 |
| --- | ---: |
| `read_only_mock` | 11 |
| `dry_run_payload_only` / `route_check` | 5 |
| `metadata_only` 暂缓 | 5 |
| `role_smoke_mock` / `component_mock` | 4 |

## 7. 暂缓 / 组件清单

| candidate_id | L1 结论 | 缺口 / 原因 |
| --- | --- | --- |
| `quality_sprint07_last30days_market_signal_brief_candidate` | `needs_more_license_info` | 已有 repo/subdir 线索，但需核 LICENSE、脚本、外网搜索/抓取源、API key、保存目录；真实抓取必须禁用或改为用户提供素材 |
| `quality_sprint07_baoyu_wechat_summary_candidate` | `needs_more_license_info` | 需核 repo LICENSE、`wx-cli` 依赖、微信账号权限、群聊隐私、本地历史数据存储边界 |
| `quality_sprint07_graphify_kb_structure_candidate` | `needs_more_license_info` | 缺 concrete GitHub repo、LICENSE、subdir、脚本和文件写入/clone repo 边界 |
| `quality_sprint07_fireworks_tech_graph_process_candidate` | `needs_more_license_info` | 缺 concrete repo、LICENSE、diagram 输出和文件写入/导出边界 |
| `quality_sprint07_guizang_ppt_sales_training_candidate` | `needs_more_license_info` | 需确认 LICENSE、assets/references、HTML/PPT 生成、截图/导出边界；本轮不得生成真实 deck |
| `quality_sprint07_agency_sales_ops_forecast_role_candidate` | `component_only` | role asset；需具体角色文件/许可证归属，不客户调用 |
| `quality_sprint07_agency_finance_ap_ar_clerk_role_candidate` | `component_only` | role asset；财务/税务边界敏感，不自动催收、不做财务结论 |
| `quality_sprint07_promptfoo_recruiting_fairness_regression_candidate` | `component_only` | eval component；只可 mock 招聘文案/问题，不处理真实候选人数据 |
| `quality_sprint07_instructor_refund_case_schema_candidate` | `component_only` | schema component；只可 mock 售后案例，不处理真实客户隐私 |

## 8. 媒体 / Provider 边界

| 候选 | trial_mode | smoke 允许范围 |
| --- | --- | --- |
| `quality_sprint07_openai_image_review_to_product_scene_candidate` | `dry_run_payload_only` | review themes + product metadata -> image payload；不上传素材、不出图 |
| `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | `dry_run_payload_only` | roleplay script -> TTS payload；不生成音频、不克隆声音 |
| `quality_sprint07_runway_customer_story_clip_candidate` | `dry_run_payload_only` | customer story brief -> video payload；不生成视频 |
| `quality_sprint07_fal_packshot_to_lifestyle_candidate` | `route_check` | product metadata -> fal route payload；不上传商品图、不出图 |
| `quality_sprint07_heygen_new_employee_avatar_candidate` | `dry_run_payload_only` | onboarding script -> avatar payload；不上传人脸/声音、不生成视频 |

统一禁止：真实生成、素材上传、读取 key、调用 provider、下载产物、声明商用输出已通过。

## 9. SaaS / Read-only 边界

| 候选 | trial_mode | smoke 允许范围 |
| --- | --- | --- |
| `quality_sprint07_intercom_article_decay_readonly_candidate` | `read_only_mock` | mock articles/conversations -> decay/gap report |
| `quality_sprint07_workable_interview_question_bank_candidate` | `read_only_mock` | mock JD/candidate profile -> question bank |
| `quality_sprint07_shopify_return_product_quality_candidate` | `read_only_mock` | mock returns/products -> quality issue clusters |
| `quality_sprint07_metabase_executive_digest_candidate` | `read_only_mock` | mock dashboard cards -> executive digest |
| `quality_sprint07_docusign_missing_signature_readonly_candidate` | `read_only_mock` | mock envelopes -> missing signature report |
| `quality_sprint07_mailchimp_deliverability_qc_candidate` | `read_only_mock` | mock campaign reports -> deliverability QC |
| `quality_sprint07_helpscout_saved_reply_gap_candidate` | `read_only_mock` | mock conversations/saved replies -> gap report |
| `quality_sprint07_front_account_handoff_candidate` | `read_only_mock` | mock account conversations -> handoff brief |
| `quality_sprint07_greenhouse_offer_risk_readonly_candidate` | `read_only_mock` | mock offers/candidates -> risk checklist |
| `quality_sprint07_amplitude_activation_dropoff_candidate` | `read_only_mock` | mock activation metrics -> dropoff report |
| `quality_sprint07_hubspot_lead_source_quality_candidate` | `read_only_mock` | mock contacts/deals -> source quality report |

统一禁止：连接真实账号、OAuth 真实租户、写入/发送/分派/改状态/改联系人/发 offer/发签署/改商品/退款。

## 10. L1 复核表

| # | priority | candidate_id | L1 结论 | trial_mode | smoke | 许可证/条款关注点 | 上游证据 | 外部依赖/API/provider | 禁止动作 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint07_last30days_market_signal_brief_candidate` | `needs_more_license_info` | `metadata_only` | no | repo LICENSE、外网内容源、API key、保存目录 | 有 repo/subdir/SKILL.md 线索，LICENSE 未核 | 外网搜索/抓取、可能 API key | 不抓取网页，不保存外部内容 |
| 2 | P0 | `quality_sprint07_baoyu_wechat_summary_candidate` | `needs_more_license_info` | `metadata_only` | no | repo LICENSE、微信数据隐私、账号权限 | 有 repo/subdir/SKILL.md 线索，LICENSE 未核 | `wx-cli`、微信账号/本地聊天记录 | 不接真实微信、不读群聊 |
| 3 | P0 | `quality_sprint07_intercom_article_decay_readonly_candidate` | `allow_smoke` | `read_only_mock` | yes | Intercom API terms、article/conversation privacy | 官方 API docs | Intercom API，BYOK 未来需要 | 不写文章、不发消息 |
| 4 | P0 | `quality_sprint07_workable_interview_question_bank_candidate` | `allow_smoke` | `read_only_mock` | yes | Workable terms、候选人 PII、反歧视 | 官方 API docs | Workable API，BYOK 未来需要 | 不录用/拒绝、不写候选人 |
| 5 | P0 | `quality_sprint07_shopify_return_product_quality_candidate` | `allow_smoke` | `read_only_mock` | yes | Shopify terms、orders/returns privacy | 官方 API docs | Shopify API，BYOK 未来需要 | 不退款、不改商品 |
| 6 | P0 | `quality_sprint07_metabase_executive_digest_candidate` | `allow_smoke` | `read_only_mock` | yes | Metabase license/API、dashboard privacy | 官方 API docs | Metabase API/read-only cards | 不写 query，不连真实 DB |
| 7 | P0 | `quality_sprint07_openai_image_review_to_product_scene_candidate` | `allow_smoke` | `dry_run_payload_only` | yes | OpenAI Images terms、评论/商品素材权利、费用 | 官方 API docs | OpenAI Images route | 不生成图片、不上传素材 |
| 8 | P0 | `quality_sprint07_graphify_kb_structure_candidate` | `needs_more_license_info` | `metadata_only` | no | concrete repo、LICENSE、脚本/文件写入 | marketplace lead，不足 | 可能文件/diagram 工具 | 不生成图、不 clone repo |
| 9 | P0 | `quality_sprint07_docusign_missing_signature_readonly_candidate` | `allow_smoke` | `read_only_mock` | yes | DocuSign terms、contract privacy | 官方 API docs | DocuSign API，BYOK 未来需要 | 不签署、不发送、不改 envelope |
| 10 | P0 | `quality_sprint07_mailchimp_deliverability_qc_candidate` | `allow_smoke` | `read_only_mock` | yes | Mailchimp terms、audience privacy | 官方 API docs | Mailchimp API，BYOK 未来需要 | 不发送、不改 audience |
| 11 | P1 | `quality_sprint07_fireworks_tech_graph_process_candidate` | `needs_more_license_info` | `metadata_only` | no | concrete repo、LICENSE、diagram output | marketplace lead，不足 | 可能图形/文件导出工具 | 不生成图、不写文件 |
| 12 | P1 | `quality_sprint07_guizang_ppt_sales_training_candidate` | `needs_more_license_info` | `metadata_only` | no | LICENSE、assets、HTML/PPT 输出 | repo/root SKILL.md 线索，仍需补 license/asset 边界 | 可能 HTML/PPT/截图导出 | 不生成 PPT/HTML |
| 13 | P1 | `quality_sprint07_helpscout_saved_reply_gap_candidate` | `allow_smoke` | `read_only_mock` | yes | Help Scout terms、mailbox privacy | 官方 API docs | Help Scout API，BYOK 未来需要 | 不发回复、不写 saved reply |
| 14 | P1 | `quality_sprint07_front_account_handoff_candidate` | `allow_smoke` | `read_only_mock` | yes | Front terms、inbox/account privacy | 官方 API docs | Front API，BYOK 未来需要 | 不发送、不分派 |
| 15 | P1 | `quality_sprint07_greenhouse_offer_risk_readonly_candidate` | `allow_smoke` | `read_only_mock` | yes | Greenhouse terms、candidate/offer PII | 官方 API docs | Greenhouse API，BYOK 未来需要 | 不发 offer、不录用/拒绝 |
| 16 | P1 | `quality_sprint07_amplitude_activation_dropoff_candidate` | `allow_smoke` | `read_only_mock` | yes | Amplitude terms、analytics privacy | 官方 API docs | Amplitude API，BYOK 未来需要 | 不写 cohorts/charts |
| 17 | P1 | `quality_sprint07_hubspot_lead_source_quality_candidate` | `allow_smoke` | `read_only_mock` | yes | HubSpot terms、contact/deal privacy | 官方 API docs | HubSpot API，BYOK 未来需要 | 不写联系人/任务 |
| 18 | P1 | `quality_sprint07_openai_tts_sales_roleplay_audio_candidate` | `allow_smoke` | `dry_run_payload_only` | yes | TTS terms、声音权利、内容政策 | 官方 API docs | OpenAI TTS route | 不生成音频、不克隆声音 |
| 19 | P1 | `quality_sprint07_runway_customer_story_clip_candidate` | `allow_smoke` | `dry_run_payload_only` | yes | Runway terms、素材上传、输出权利、费用 | 官方 API docs | Runway provider route | 不生成视频、不上传素材 |
| 20 | P1 | `quality_sprint07_fal_packshot_to_lifestyle_candidate` | `allow_smoke` | `route_check` | yes | fal terms、model license、商品图上传/存储 | provider docs lead | fal provider route | 不上传商品图、不生成图片 |
| 21 | P1 | `quality_sprint07_heygen_new_employee_avatar_candidate` | `allow_smoke` | `dry_run_payload_only` | yes | HeyGen terms、avatar/voice/likeness rights | 官方 API docs | HeyGen provider route | 不上传人脸/声音、不生成视频 |
| 22 | P1 | `quality_sprint07_agency_sales_ops_forecast_role_candidate` | `component_only` | `role_smoke_mock` | no | role repo license、具体角色文件 | role mapping TBD | 无 provider | 不做销售决策、不客户调用 |
| 23 | P1 | `quality_sprint07_agency_finance_ap_ar_clerk_role_candidate` | `component_only` | `role_smoke_mock` | no | role repo license、财务/税务边界 | role mapping TBD | 无 provider | 不催收、不做财务结论 |
| 24 | P1 | `quality_sprint07_promptfoo_recruiting_fairness_regression_candidate` | `component_only` | `component_mock` | no | promptfoo license、eval 数据隐私、反歧视 | package/config component | eval component | 不处理真实候选人数据 |
| 25 | P1 | `quality_sprint07_instructor_refund_case_schema_candidate` | `component_only` | `component_mock` | no | Instructor license、provider adapter、客户隐私 | package/docs component | schema component | 不处理真实售后数据 |

