# LICENSE_REVIEW_QUALITY_SPRINT_02_RESULT

回传日期：2026-06-05

## 1. 已完成事项

- 已读取 `QUALITY_SOURCE_SPRINT_02_RESULT.md` 与 `queues/LICENSE_REVIEW_QUALITY_SPRINT_02_QUEUE.md`。
- 已对队列中的 30 个唯一候选完成 L1 / provider / trial mode 复核。
- 已生成 DeepAgents smoke 队列：`queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_02_QUEUE.md`。
- 本轮未调用真实 API/provider，未安装，未写 key，未读取客户文件，未生成图片/视频/音频/PDF，未写 SaaS/CRM/日历/任务/业务系统，未改稳交付库。

## 2. 当前问题

- 媒体/provider 类候选全部只能进入 route/payload smoke，不能真实生成，不能写作 provider 通过。
- SaaS/API/CRM/POS/日历/邮件类候选全部只能 read-only mock 或 dry-run，不得连接真实账号、发送邮件、写 CRM、写表格、创建任务或读取客户文件。
- Agent workflow / framework 类可以 mock smoke，但不能直接当作 Skill；后续需要抽成轻量 callable workflow。
- `open-design menu poster child` 仍需定位具体子 skill、manifest/API/文件写入边界，暂缓。

## 3. 阻塞原因

- 无权限阻塞。
- 候选项级 blocked 为 0。
- 需补资料项 1 个：`quality_sprint02_open_design_menu_poster_child_candidate`。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 29 个 L1 放行项进入 DeepAgents mock/dry-run/route-check smoke。
- 是否将 13 个媒体/provider 类统一并入真实媒体 provider 预检链路，先 route/config/terms，不做真实生成。
- 是否要求研究窗口补齐 `open-design menu poster child` 的具体子目录、LICENSE、manifest、API/导出/文件写入依赖。

## 5. 建议下一步

- 测试台读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_02_QUEUE.md`。
- 连接器类统一 `write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`read_only/mock only`。
- 媒体/provider 类统一 `BYOK_required`、`provider_api_required`、`real_media_generation_requires_approval`、费用上限和素材授权检查。
- 暂缓项不得送正式 L2、不得封装、不得客户调用。

## 6. 数量汇总

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 8 |
| `can_dry_run_smoke` | 8 |
| `can_route_check` | 13 |
| `can_real_provider_smoke_later` | 0 |
| `component_only` | 0 |
| `needs_more_license_info` | 1 |
| `blocked` | 0 |

| 回传口径 | 数量 |
| --- | ---: |
| 放行 smoke | 29 |
| needs_more_license_info | 1 |
| blocked | 0 |
| 可直接送正式 L2 | 0 |

## 7. 媒体 / Provider 类分流

| 分流 | 数量 | 候选 |
| --- | ---: | --- |
| `can_route_check` image provider/edit | 8 | Stability, Adobe Firefly, fal FLUX, Recraft, Ideogram, fal Kontext, remove.bg, Cloudinary |
| `can_route_check` video/avatar provider | 5 | Runway, Luma, Google Veo, HeyGen, Shotstack |
| `can_real_provider_smoke_later` | 0 | 真实生成需另走 provider smoke 预检批准 |

## 8. P0 / P1 清单

### P0 放行 smoke

1. `quality_sprint02_microsoft_excel_report_agent_candidate`
2. `quality_sprint02_microsoft_graph_outlook_followup_candidate`
3. `quality_sprint02_stability_product_scene_candidate`
4. `quality_sprint02_adobe_firefly_product_ad_image_candidate`
5. `quality_sprint02_fal_flux_product_photo_candidate`
6. `quality_sprint02_runway_gen4_short_ad_candidate`
7. `quality_sprint02_gmail_customer_email_triage_candidate`
8. `quality_sprint02_zoho_crm_followup_candidate`
9. `quality_sprint02_lark_docs_meeting_action_candidate`
10. `quality_sprint02_recraft_brand_banner_candidate`
11. `quality_sprint02_pipedrive_deal_next_step_candidate`
12. `quality_sprint02_square_pos_daily_report_candidate`

### P1 放行 smoke

`quality_sprint02_ideogram_poster_text_candidate`, `quality_sprint02_fal_kontext_image_edit_candidate`, `quality_sprint02_removebg_cutout_candidate`, `quality_sprint02_luma_dream_machine_store_video_candidate`, `quality_sprint02_wecom_customer_group_summary_candidate`, `quality_sprint02_gorgias_ecommerce_support_candidate`, `quality_sprint02_zoho_books_expense_reconcile_candidate`, `quality_sprint02_google_veo_store_campaign_candidate`, `quality_sprint02_heygen_training_avatar_cn_candidate`, `quality_sprint02_haystack_faq_rag_candidate`, `quality_sprint02_shopline_order_digest_candidate`, `quality_sprint02_feishu_bitable_ops_tracker_candidate`, `quality_sprint02_mailchimp_campaign_report_candidate`, `quality_sprint02_autogen_sales_roleplay_candidate`, `quality_sprint02_crewai_market_research_candidate`, `quality_sprint02_instructor_schema_extraction_candidate`, `quality_sprint02_promptfoo_support_regression_candidate`

### P1 暂缓补资料

`quality_sprint02_open_design_menu_poster_child_candidate`

## 9. L1 / Provider / Trial Mode 复核表

| # | priority | candidate_id | source / provider | license / terms | platform_fit | relay_fit | dependency_risk | BYOK / cost / rights | dedupe_relation | trial_mode | smoke_allowed | formal_l2 | l1_result |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint02_microsoft_excel_report_agent_candidate` | Microsoft Graph Excel | Microsoft Graph API terms；Files.Read/read-only scope | 适合经营报表 read-only mock | 文本中转分析 mock rows | 文件/表格隐私、OAuth、禁止写 workbook | BYOK；read-only；不读真实文件 | Sprint01 Sheets 替代 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 2 | P0 | `quality_sprint02_microsoft_graph_outlook_followup_candidate` | Microsoft Graph Mail | Microsoft Graph terms；Mail.Read；禁止发送 | 适合销售/客服邮件跟进草稿 | 文本中转生成摘要/草稿 | 邮箱隐私、发送风险、OAuth | BYOK；send_allowed=false；local draft only | Microsoft 路线新增 | `dry_run_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 3 | P0 | `quality_sprint02_stability_product_scene_candidate` | Stability AI API | Stability API/model terms 需复核 | 适合商品场景图 payload | provider route；文本中转生成 prompt | 图片上传、模型条款、商标/素材授权 | BYOK；单图费用上限；不真实生成 | Sprint01 product photo 替代 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 4 | P0 | `quality_sprint02_adobe_firefly_product_ad_image_candidate` | Adobe Firefly Services | Firefly API/commercial terms 需核 | 适合广告图/海报 payload | provider route | 素材上传、生成图权利、费用、商标 | BYOK；单图费用上限；不真实生成 | 高质量媒体替代来源 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 5 | P0 | `quality_sprint02_fal_flux_product_photo_candidate` | fal.ai FLUX routes | fal terms + per-model license | 适合商品图风格化 payload | fal/provider route | 多模型许可证、上传存储、费用 | BYOK；model id 审计；不真实生成 | fal 媒体补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 6 | P0 | `quality_sprint02_runway_gen4_short_ad_candidate` | Runway API | Runway API terms/content policy | 适合短广告视频 payload | provider route | 视频素材授权、输出权利、费用 | BYOK；单视频预算；不渲染 | 视频候选补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 7 | P0 | `quality_sprint02_gmail_customer_email_triage_candidate` | Gmail API | Gmail API terms；read-only/draft boundary | 适合客服邮件分流/草稿 | 文本中转分析 mock emails | 邮箱隐私、发送风险、OAuth scope | BYOK；send_allowed=false | support classifier 渠道补充 | `dry_run_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 8 | P0 | `quality_sprint02_zoho_crm_followup_candidate` | Zoho CRM API | Zoho API terms；CRM scopes | 适合 CRM next action dry-run | 文本中转生成 payload | CRM 写入、联系人隐私、OAuth | BYOK；write_allowed=false | HubSpot 替代 | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 9 | P0 | `quality_sprint02_lark_docs_meeting_action_candidate` | Lark Open Platform | Lark API terms；docs read-only | 适合会议纪要/待办 dry-run | 文本中转可用 | 文档隐私、任务创建风险 | BYOK；task/write blocked | 国内协作工具补充 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 10 | P0 | `quality_sprint02_recraft_brand_banner_candidate` | Recraft API | Recraft API terms；商用授权需核 | 适合品牌 banner payload | provider route | 品牌素材上传、商标、版权声明 | BYOK；单图费用上限；不生成 | 视觉候选补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 11 | P0 | `quality_sprint02_pipedrive_deal_next_step_candidate` | Pipedrive API | Pipedrive API terms/scopes | 适合 deal next-step dry-run | 文本中转生成报告 | CRM 写入、联系人隐私、OAuth | BYOK；write_allowed=false | CRM 补充来源 | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_dry_run_smoke` |
| 12 | P0 | `quality_sprint02_square_pos_daily_report_candidate` | Square API | Square developer/API terms；read-only | 适合门店 POS 日报 mock | 文本中转分析 mock POS rows | 支付/销售数据隐私、权限 | BYOK；read-only/mock | 门店经营数据补强 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 13 | P1 | `quality_sprint02_ideogram_poster_text_candidate` | Ideogram API | API/commercial terms 需核 | 适合海报文字 payload | provider route | 中文文字、字体、商标、素材授权 | BYOK；单图费用上限；不生成 | 海报能力补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 14 | P1 | `quality_sprint02_fal_kontext_image_edit_candidate` | fal Kontext image edit | fal terms + model license | 适合商品局部编辑 payload | provider route | 上传/删除策略、模型条款、商品授权 | BYOK；model id 审计；不生成 | image edit 补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 15 | P1 | `quality_sprint02_removebg_cutout_candidate` | remove.bg API | remove.bg API terms 需核 | 适合商品白底图 payload | provider route | 上传素材、员工/证件照片隐私、商用权利 | BYOK；单图费用上限；不上传 | 轻量替代来源 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 16 | P1 | `quality_sprint02_luma_dream_machine_store_video_candidate` | Luma AI API | Luma API/commercial terms 需核 | 适合门店/商品短视频 payload | provider route | 素材授权、下载/存储、费用 | BYOK；单视频预算；不渲染 | 视频来源补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 17 | P1 | `quality_sprint02_wecom_customer_group_summary_candidate` | WeCom API | 企业微信 API terms；read-only/mock | 适合中文私域客服摘要 | 文本中转可用 | 群消息隐私、发送风险、权限 | BYOK；send_allowed=false | 中文客服渠道补充 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 18 | P1 | `quality_sprint02_gorgias_ecommerce_support_candidate` | Gorgias API | Gorgias API terms/scopes | 适合电商客服工单摘要 | 文本中转分析 mock tickets | 工单隐私、回复/退款风险 | BYOK；reply/write blocked | 电商客服补强 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 19 | P1 | `quality_sprint02_zoho_books_expense_reconcile_candidate` | Zoho Books API | Zoho Books terms；finance read-only | 适合费用核对提示 | 文本中转分析 mock rows | 财务数据隐私、非审计/税务结论 | BYOK；read-only/mock | 财务 API 替代 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 20 | P1 | `quality_sprint02_google_veo_store_campaign_candidate` | Google Veo/Gemini | Google/Veo terms, region, cost 需核 | 适合视频 payload | provider route possible | 地区可用性、素材授权、费用、内容政策 | BYOK；不生成视频 | Next50 Veo 补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 21 | P1 | `quality_sprint02_heygen_training_avatar_cn_candidate` | HeyGen API | HeyGen terms/avatar/voice rights | 适合培训数字人 payload | provider route | 肖像/声音授权、HR 内容、费用 | BYOK；stock avatar only；不生成 | Avatar 补充 | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | no | `can_route_check` |
| 22 | P1 | `quality_sprint02_haystack_faq_rag_candidate` | Haystack | Apache-2.0；产品筛选可接受 | 适合 FAQ/RAG 底层替代 | OpenAI-compatible possible | 框架较重、真实文档隐私 | 无 BYOK；mock docs only | stable FAQ 替代来源 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 23 | P1 | `quality_sprint02_shopline_order_digest_candidate` | SHOPLINE Open API | SHOPLINE API terms；orders read-only | 适合中文/跨境电商订单摘要 | 文本中转可用 | 订单隐私、写入边界 | BYOK；read-only/mock | Shopify/WooCommerce 补充 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 24 | P1 | `quality_sprint02_feishu_bitable_ops_tracker_candidate` | Feishu Bitable API | Feishu API terms；read-only | 适合运营表格摘要 | 文本中转可用 | 表格隐私、写表风险 | BYOK；write blocked | Lark/Feishu 数据源补强 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 25 | P1 | `quality_sprint02_mailchimp_campaign_report_candidate` | Mailchimp Marketing API | Mailchimp API terms；audience privacy | 适合营销活动复盘 read-only | 文本中转可用 | 联系人隐私、发送风险 | BYOK；send_allowed=false | 营销报表补充 | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 26 | P1 | `quality_sprint02_open_design_menu_poster_child_candidate` | open-design child skill lead | 仓库 Apache-2.0；子 skill 未定位 | 需定位具体 child skill 后评估 | possible | 聚合仓库、API/文件写入/导出风险 | BYOK 待定 | Sprint01 open-design 细分来源 | `dry_run_only`, `external_action_blocked` | no | no | `needs_more_license_info` |
| 27 | P1 | `quality_sprint02_autogen_sales_roleplay_candidate` | Microsoft AutoGen | MIT；产品筛选可接受 | 适合销售 roleplay workflow mock | OpenAI-compatible possible | 依赖较重；不得真实工具调用 | 无 BYOK；mock only | Agent workflow 来源 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 28 | P1 | `quality_sprint02_crewai_market_research_candidate` | CrewAI | MIT；产品筛选可接受 | 适合市场调研 workflow mock | OpenAI-compatible possible | 不得浏览/抓取/API；工具禁用 | 无 BYOK；mock company only | workflow 来源 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 29 | P1 | `quality_sprint02_instructor_schema_extraction_candidate` | Instructor | MIT；产品筛选可接受 | 适合结构化抽取组件 | OpenAI-compatible | provider adapter；真实文件隐私 | 无 BYOK；mock text only | 稳定结构化能力补充 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
| 30 | P1 | `quality_sprint02_promptfoo_support_regression_candidate` | promptfoo | MIT；产品筛选可接受 | 适合客服回归测试组件 | OpenAI-compatible | eval 数据隐私，偏测试组件 | 无 BYOK；mock eval only | support eval 路线补强 | `mock_only`, `read_only`, `external_action_blocked` | yes | no | `can_mock_smoke` |
