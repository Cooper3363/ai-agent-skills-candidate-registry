# DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_RESULT

回传日期：2026-06-05

本轮性质：DeepAgents candidate-level metadata/mock/dry-run/route-check smoke。  
结论边界：DeepAgents smoke passed 只代表候选库可继续试跑，不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_03_RESULT.md` 与 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_QUEUE.md`。
- 已确认 smoke 队列包含 16 个 L1/trial mode 放行候选；4 个 needs_more_license_info 候选未进入本轮。
- 已对 16 个候选完成 candidate-level metadata/mock/dry-run/route-check smoke。
- 已为每个候选记录中文六部门 mock/dry-run/route-check 场景、callable 表达、输入输出 schema、中文可用性、人工复核触发、禁止动作和 smoke_status。
- 已从 passed 候选中筛选 Top8，生成正式 L2 simulated 队列建议。

## 2. 当前问题

- OpenAI Images/TTS 3 个 provider 项仅完成 route/config/payload check，未真实生成图片、音频、视频或文件，不得写成真实 provider 通过。
- DeepAgents workflow 示例仅做 mock tools 适配验证，未浏览、未抓取、未调用外部工具，不应直接作为客户 callable Skill。
- SaaS/API/MCP connector 类仅完成 mock/read-only/dry-run smoke，未连接真实账号，未写业务系统。
- 4 个 needs_more_license_info 候选仍需补齐具体上游子目录、`SKILL.md`、LICENSE、manifest、provider/API/文件写入边界。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 本轮未触发外部网络、真实账号、真实 API/provider、真实客户文件、上传、发送、抓取、退款/赔偿、库存修改或写业务系统动作。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 Top8 进入正式 L2 simulated，每个候选至少 3 个中文业务 mock/dry-run 用例。
- 是否将 OpenAI Images/TTS 三个 route-check passed 候选并入真实媒体/provider smoke 审批链路；审批前不得真实生成。
- 是否要求研究窗口继续补齐 4 个 needs_more_license_info 候选的上游证据与边界。

## 5. 建议下一步

- 将 Top8 非媒体、低真实动作风险、可形成 callable 业务入口的候选送正式 L2 simulated。
- OpenAI Images/TTS 候选仅保留 route-check passed，暂不进入正式 L2 通过或封装判断。
- 所有 dry-run/SaaS/API 候选后续继续强制 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 16 |
| `failed` | 0 |
| `needs_fix` | 0 |
| `blocked` | 0 |

| smoke_type | 数量 |
| --- | ---: |
| `can_mock_smoke` | 12 |
| `can_dry_run_smoke` | 1 |
| `can_route_check` | 3 |

## 7. Dry-run / Route-check 硬断言结果

| 检查项 | 结果 |
| --- | --- |
| `send_allowed=false` | 通过；HubSpot dry-run 禁止发送邮件/通知 |
| `write_allowed=false` | 通过；HubSpot dry-run 禁止写联系人、deal、任务 |
| `upload_allowed=false` | 通过；dry-run 与 provider route-check 均禁止上传素材/文件 |
| `external_action_blocked=true` | 通过；所有 dry-run、route-check 与 mock connector 均阻断外部动作 |
| OpenAI Images/TTS 真实调用 | 未发生 |
| 图片/音频/视频/文件真实生成 | 未发生 |
| key 读取/打印/写入 | 未发生 |

## 8. Top8 正式 L2 队列建议

| 排名 | candidate_id | 推荐原因 | 正式 L2 重点 |
| ---: | --- | --- | --- |
| 1 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | 电商商品目录高频，mock catalog 可稳定测试，真实动作风险低 | 商品目录 QC、缺字段、异常库存/图片字段，只读边界 |
| 2 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | 订阅健康/收入风险高频，mock subscription 可稳定测试 | 订阅健康摘要、失败扣款风险、非财务/审计结论 |
| 3 | `quality_sprint03_mcp_notion_policy_gap_candidate` | 政策知识库缺口高频，可与 KB 能力互补 | mock pages 到政策缺口、冲突、过期提示 |
| 4 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | 库存/运营表高频，Airtable read-only adapter 清晰 | mock rows 到库存预警、补货核查、禁止写表 |
| 5 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | 客服频道 FAQ 缺口识别高频，低动作风险 | mock messages 到 FAQ gaps、风险主题，send blocked |
| 6 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | 文档分类高频，mock metadata 可稳定验证 | 文件元数据分类、敏感类型提示，不读真实文件内容 |
| 7 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | CRM 数据健康高频，dry-run payload 可控 | 联系人健康评分、重复/缺字段、write/send/upload blocked |
| 8 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | 现金流预警高频，mock accounts 低风险 | 现金流风险、异常费用、非审计/非税务声明 |

## 9. 16 个候选 smoke 明细

| # | candidate_id | smoke_type | 中文 smoke 场景 | callable_fit | expected_inputs | expected_outputs | 权限边界 | 人工复核触发 | 禁止动作 | deepagents_smoke_status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | mock | 模拟 Shopify 商品目录 rows，生成商品信息 QC 报告 | 可表达为只读商品目录 QC agent | `mock_products`, `catalog_rules`, `qc_scope` | `catalog_summary`, `missing_fields`, `risk_flags`, `source_rows` | 不连真实店铺；不写商品/库存 | 价格缺失、库存异常、图片/标题不合规 | 写商品、改库存、上传图片、发布商品 | passed |
| 2 | `quality_sprint03_openai_image_product_variant_candidate` | route-check | 模拟商品变体图需求，生成 OpenAI Images payload | 可表达为 image route candidate，需另行真实 provider 审批 | `mock_product_brief`, `asset_policy`, `prompt_brief`, `cost_limit` | `image_payload`, `route_config`, `content_safety`, `real_media_generation_requires_approval=true` | 不调用 OpenAI Images；不上传商品图 | 商标/版权/肖像/素材授权、费用 | 真实出图、上传素材、发布图片、写 key | passed |
| 3 | `quality_sprint03_openai_image_poster_layout_candidate` | route-check | 模拟门店活动海报需求，生成 poster layout payload | 可表达为 image route candidate，需另行真实 provider 审批 | `mock_campaign_brief`, `brand_rules`, `layout_goal`, `cost_limit` | `poster_payload`, `layout_notes`, `content_safety`, `real_media_generation_requires_approval=true` | 不生成海报；不上传品牌素材 | 中文文字表现、商标/版权、优惠合规 | 真实出图、上传素材、发布海报 | passed |
| 4 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | mock | 模拟 Stripe 订阅/扣款 rows，生成订阅健康摘要 | 可表达为只读订阅健康 agent | `mock_subscriptions`, `mock_charges`, `health_rules` | `health_summary`, `at_risk_accounts`, `failed_payment_notes`, `not_financial_advice=true` | 不连 Stripe；不处理付款/退款/订阅 | 失败扣款、高价值客户、流失风险 | 退款、改订阅、扣款、财务/审计结论 | passed |
| 5 | `quality_sprint03_mcp_notion_policy_gap_candidate` | mock | 模拟 Notion 政策页，输出政策缺口和冲突 | 可表达为只读政策 gap agent | `mock_pages`, `policy_scope`, `version_notes` | `policy_gaps`, `conflicts`, `stale_items`, `source_notes` | 不连 Notion；不写页面/权限 | 退款、赔偿、账号安全、政策冲突 | 写页面、发布政策、改权限 | passed |
| 6 | `quality_sprint03_deepagents_customer_ops_example_candidate` | mock | 模拟客户运营 case，输出 mock tools workflow plan | 仅 workflow example 适配，不是客户正式 Skill | `mock_case`, `mock_tools`, `policy_snippets` | `workflow_plan`, `tool_plan`, `blocked_steps`, `manual_review_required` | 只用 mock tools；不接客服系统 | 工具越权、退款/赔偿、账号安全 | 真实工具调用、外部 API、客户调用 | passed |
| 7 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | mock | 模拟 Airtable 库存 rows，生成库存预警 | 可表达为只读库存运营 agent | `mock_inventory_rows`, `inventory_rules`, `date_range` | `inventory_alerts`, `reorder_checks`, `stale_rows`, `source_rows` | 不连 Airtable；不写行、不改库存 | 缺货、高库存、责任人缺失 | 写表、改库存、创建任务 | passed |
| 8 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | mock | 模拟 Slack 客服频道消息，识别 FAQ 缺口 | 可表达为只读 FAQ gap agent | `mock_channel_messages`, `faq_scope`, `policy_snippets` | `faq_gaps`, `frequent_topics`, `risk_tags`, `source_messages` | 不连 Slack；不发消息/邀人/改频道 | 投诉、退款、账号安全、PII | 发消息、改频道、读取真实 workspace | passed |
| 9 | `quality_sprint03_deepagents_research_report_example_candidate` | mock | 模拟用户提供公司资料，生成调研 brief | 仅 workflow example 适配，不是客户正式 Skill | `mock_company_docs`, `research_scope`, `source_notes` | `research_brief`, `assumptions`, `open_questions`, `manual_review_required` | 不联网、不搜索、不抓取、不调用外部工具 | 来源不足、竞品结论过度、版权引用 | 浏览网页、抓取、调用搜索/API | passed |
| 10 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | mock | 模拟 Google Drive 文件元数据，生成文档分类 | 可表达为只读文件分类 agent | `mock_file_metadata`, `classification_rules`, `privacy_rules` | `classified_files`, `sensitive_flags`, `routing_suggestions`, `manual_review_required` | 不读真实文件内容；不移动/删除/共享 | 合同/票据/HR 文档、权限敏感 | 读真实文件、移动、删除、共享文件 | passed |
| 11 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | dry-run | 模拟 HubSpot 联系人列表，生成数据健康 dry-run 报告 | 可表达为 CRM data health dry-run agent | `mock_contacts`, `health_rules`, `dedupe_policy` | `health_report`, `duplicate_candidates`, `missing_fields`, `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | 不连 HubSpot；不写联系人/任务/deal | PII、重复合并、高价值客户 | 写 CRM、发邮件、建任务、上传联系人 | passed |
| 12 | `quality_sprint03_mcp_xero_ar_followup_candidate` | mock | 模拟 Xero 应收 invoices，生成催收跟进建议 | 可表达为只读 AR follow-up agent | `mock_invoices`, `customer_notes`, `ar_rules` | `ar_summary`, `overdue_accounts`, `followup_suggestions`, `not_audit_or_tax_advice=true` | 不连 Xero；不发催收、不改 invoice | 高金额逾期、争议账款、客户关系风险 | 发催收、改 invoice、审计/税务结论 | passed |
| 13 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | mock | 模拟 QuickBooks 账户/费用 rows，生成现金流预警 | 可表达为只读 cashflow warning agent | `mock_accounts`, `mock_expenses`, `cashflow_rules` | `cashflow_summary`, `warning_flags`, `runway_estimate`, `not_audit_or_tax_advice=true` | 不连 QuickBooks；不写账、不报税 | 现金余额低、异常费用、税务敏感 | 写账、报税、审计/税务结论 | passed |
| 14 | `quality_sprint03_openai_tts_training_microcourse_candidate` | route-check | 模拟 HR 培训微课文本，生成 TTS payload | 可表达为 audio route candidate，需另行真实 provider 审批 | `mock_training_text`, `voice_policy`, `content_policy`, `cost_limit` | `tts_payload`, `voice_rights_notes`, `content_safety`, `real_media_generation_requires_approval=true` | 不调用 TTS；不生成音频；不上传样本 | 声音权利、培训内容合规、费用 | 生成音频、克隆声音、上传样本、写 key | passed |
| 15 | `quality_sprint03_canva_connect_brand_kit_qc_candidate` | mock | 模拟 Canva brand kit JSON，输出品牌一致性 QC | 可表达为只读品牌 QC agent | `mock_brand_kit_json`, `design_rules`, `qc_scope` | `brand_qc_findings`, `severity`, `fix_suggestions`, `manual_review_required` | 不连 Canva；不导出/写设计/上传素材 | 商标、品牌色/字体不一致、版权素材 | 写设计、导出、上传素材、发布 | passed |
| 16 | `quality_sprint03_mcp_google_merchant_feed_qc_candidate` | mock | 模拟 Google Merchant feed rows，生成商品 feed QC | 可表达为只读 feed QC agent | `mock_feed_rows`, `merchant_rules`, `qc_scope` | `feed_qc_findings`, `missing_attributes`, `policy_risks`, `source_rows` | 不连 Merchant；不写 feed/价格/库存 | 违规商品、价格/库存错误、图片缺失 | 写 feed、改价格/图片/库存、发布 | passed |

## 10. 未进入 smoke 的候选

| candidate_id | 状态 | 原因 |
| --- | --- | --- |
| `quality_sprint03_openagentskills_drawio_process_candidate` | needs_more_license_info | 需定位具体上游子目录、`SKILL.md`、LICENSE、manifest、drawio 输出/写入边界 |
| `quality_sprint03_mdskills_file_processing_excel_candidate` | needs_more_license_info | 需定位具体 spreadsheet/file 子 skill、LICENSE、依赖、文件读取边界 |
| `quality_sprint03_openagentskills_social_card_candidate` | needs_more_license_info | 需定位具体 social card 子 skill、LICENSE、是否调用图像 provider、素材上传边界 |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | needs_more_license_info | 需定位具体 data-report child skill、LICENSE、manifest、依赖和业务适配边界 |

## 11. 权限边界确认

- 未安装依赖。
- 未访问真实账号。
- 未调用真实 API/provider。
- 未写 key、未打印 key、未读取密钥文件。
- 未读取客户文件。
- 未上传素材或文件。
- 未发送邮件、短信、微信、Slack 或平台消息。
- 未写 CRM、POS、Sheets、Notion、Slack、HubSpot 或其他业务系统。
- 未抓取真实网页。
- 未生成图片、音频、视频或文件。
- 未退款、未赔偿、未改库存。
- 未修改稳交付库；客户正式可调用 Skill 仍为 13。
