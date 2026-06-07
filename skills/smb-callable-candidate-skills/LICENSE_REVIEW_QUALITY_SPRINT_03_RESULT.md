# LICENSE_REVIEW_QUALITY_SPRINT_03_RESULT

回传日期：2026-06-05

## 1. 已完成事项

- 已读取 `QUALITY_SOURCE_SPRINT_03_RESULT.md` 与 `queues/LICENSE_REVIEW_QUALITY_SPRINT_03_QUEUE.md`。
- 已对队列中的 20 个优先候选完成轻量 L1 / provider / trial mode 复核。
- 已生成 DeepAgents candidate smoke 队列：`queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_QUEUE.md`。
- 本轮未调用真实 API/provider，未安装依赖，未写 key，未读取客户文件，未上传素材，未生成图片/音频/视频，未连接真实账号，未写 CRM/POS/Sheets/Notion/Slack/HubSpot/业务系统，未修改稳交付库。

## 2. 当前问题

- SaaS/MCP/API connector 候选只能按 mock/read-only/dry-run 进入 smoke；不允许连接真实账号，不允许写入、发送、发布、上传或改业务系统。
- 媒体/provider 候选在 L1 阶段只允许 route-check 或 dry-run payload；不允许真实生成图片、音频或视频。
- 标准 Skill 包 / marketplace 来源候选必须定位具体 `SKILL.md`、子目录、manifest 和 LICENSE；只凭 marketplace/registry 页面不能放行为 callable，也不进入 smoke。
- DeepAgents workflow 示例可做 mock workflow 适配验证，但不得直接宣称为客户正式可调用 Skill。
- 客户正式可调用 Skill 仍为 13；本轮不送正式 L2、不封装、不新增客户可调用项。

## 3. 阻塞原因

- 无权限阻塞。
- `blocked` 数量为 0。
- `needs_more_license_info` 数量为 4，原因均为具体上游子 skill / LICENSE / manifest / 依赖边界未定位完整。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 16 个 L1 放行项进入 DeepAgents candidate smoke，仅限 mock/dry-run/route-check。
- 是否要求研究窗口继续补齐 4 个标准 Skill 包候选的具体上游子目录、`SKILL.md`、LICENSE、manifest、外部 API/provider 和文件写入边界。
- 是否将 OpenAI Images / TTS 三个 provider route-check 项并入真实媒体 provider smoke 预检链路；在批准前仍不得真实生成。

## 5. 建议下一步

- 测试台读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_QUEUE.md`，只处理 L1 放行的 16 个候选。
- SaaS/API 项统一设置 `write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`read_only/mock only`。
- 媒体/provider 项统一设置 `BYOK_required`、`provider_api_required`、`real_media_generation_requires_approval`，并补费用上限、素材授权、生成物权属和内容安全审计。
- 暂缓项不得送正式 L2、不得封装、不得客户调用；补齐具体上游证据后再开新一轮 L1。

## 6. 数量汇总

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 12 |
| `can_dry_run_smoke` | 1 |
| `can_route_check` | 3 |
| `component_only` | 0 |
| `needs_more_license_info` | 4 |
| `blocked` | 0 |

| 回传口径 | 数量 |
| --- | ---: |
| 可送 smoke | 16 |
| needs_more_license_info | 4 |
| blocked | 0 |
| 可直接送正式 L2 | 0 |
| 客户正式可调用 Skill | 13 |

## 7. 媒体 / Provider 边界

| 分流 | 数量 | 候选 |
| --- | ---: | --- |
| `can_route_check` | 3 | `quality_sprint03_openai_image_product_variant_candidate`, `quality_sprint03_openai_image_poster_layout_candidate`, `quality_sprint03_openai_tts_training_microcourse_candidate` |
| 只读设计/API mock | 1 | `quality_sprint03_canva_connect_brand_kit_qc_candidate` |
| 需补具体 Skill 包 | 1 | `quality_sprint03_openagentskills_social_card_candidate` |

媒体类 L1 禁止动作：不真实生成图片/音频/视频，不上传商品图、品牌素材、人物肖像或声音样本，不写 key，不确认 provider 商用通过，不声明生成物可商用交付。

## 8. P0 / P1 清单

### P0 放行 smoke

1. `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate`
2. `quality_sprint03_openai_image_product_variant_candidate`
3. `quality_sprint03_openai_image_poster_layout_candidate`
4. `quality_sprint03_mcp_stripe_subscription_health_candidate`
5. `quality_sprint03_mcp_notion_policy_gap_candidate`
6. `quality_sprint03_deepagents_customer_ops_example_candidate`
7. `quality_sprint03_mcp_airtable_inventory_ops_candidate`

### P0 需补资料

1. `quality_sprint03_openagentskills_drawio_process_candidate`

### P1 放行 smoke

1. `quality_sprint03_mcp_slack_channel_faq_gap_candidate`
2. `quality_sprint03_deepagents_research_report_example_candidate`
3. `quality_sprint03_mcp_google_drive_doc_classifier_candidate`
4. `quality_sprint03_mcp_hubspot_contact_health_candidate`
5. `quality_sprint03_mcp_xero_ar_followup_candidate`
6. `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate`
7. `quality_sprint03_openai_tts_training_microcourse_candidate`
8. `quality_sprint03_canva_connect_brand_kit_qc_candidate`
9. `quality_sprint03_mcp_google_merchant_feed_qc_candidate`

### P1 需补资料

1. `quality_sprint03_mdskills_file_processing_excel_candidate`
2. `quality_sprint03_openagentskills_social_card_candidate`
3. `quality_sprint03_vercel_agent_skills_data_report_candidate`

## 9. L1 / Provider / Trial Mode 复核表

| # | priority | candidate_id | source / provider | license / terms | 维护状态或来源可信度 | 依赖/API/provider/模型风险 | BYOK / route 要求 | trial_mode | 是否可送 smoke | 禁止动作 | l1_result |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | Shopify product catalog API/MCP | Shopify API terms；非开源库许可证问题，按 API 条款和 OAuth scope 管控 | 官方 API 来源，可信度高 | 商品目录、库存、图片等店铺数据隐私；禁止写商品、改库存、发布商品 | BYOK；只读 catalog scope；DeepAgents 侧用 mock rows | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不连接真实店铺，不写商品/库存，不上传图片 | `can_mock_smoke` |
| 2 | P0 | `quality_sprint03_openai_image_product_variant_candidate` | OpenAI Images API | OpenAI API / Images terms；需遵守商用输出、素材上传和内容政策 | 官方 provider route，可信度高 | 商品图上传、品牌素材、商标、肖像、生成内容权属和费用 | BYOK 或平台中转站 route；L1 仅 payload/route check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | 不上传商品图，不真实出图，不声明商用素材通过 | `can_route_check` |
| 3 | P0 | `quality_sprint03_openai_image_poster_layout_candidate` | OpenAI Images API | OpenAI API / Images terms；需补生成物权属和中文文字表现验收 | 官方 provider route，可信度高 | 活动素材、门店海报、优惠券文案、商标和版权风险 | BYOK 或中转站 image route；L1 仅 payload/route check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | 不真实生成海报，不上传品牌素材，不发布 | `can_route_check` |
| 4 | P0 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | Stripe API | Stripe API terms；支付/订阅数据按只读和隐私边界管控 | 官方 API 来源，可信度高 | 支付、订阅、失败扣款等敏感财务数据；不得处理付款或给审计结论 | BYOK；read-only/mock charges/subscriptions | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不处理付款，不退款，不改订阅，不做财务/审计结论 | `can_mock_smoke` |
| 5 | P0 | `quality_sprint03_openagentskills_drawio_process_candidate` | Open Agent Skills registry / drawio lead | 仅有 registry 线索；具体 repo、`SKILL.md`、LICENSE 未定位完整 | 来源可信度待核验 | 可能写 drawio/diagram 文件；需确认是否调用外部工具或写文件 | 暂不进入 smoke；需补具体 child skill 和输出边界 | `dry_run_only`, `external_action_blocked` | no | 不写文件，不生成真实 drawio 文件，不按 marketplace 页面放行 | `needs_more_license_info` |
| 6 | P0 | `quality_sprint03_mcp_notion_policy_gap_candidate` | Notion API | Notion API terms；按页面 read-only scope 管控 | 官方 API 来源，可信度高 | 知识库页面、客户政策、权限继承和隐私 | BYOK；read-only/mock pages | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不连接真实 workspace，不写页面，不改权限 | `can_mock_smoke` |
| 7 | P0 | `quality_sprint03_deepagents_customer_ops_example_candidate` | langchain-ai/deepagents examples | 源仓库许可证需在正式封装前复核；L1 仅作为 workflow example mock | GitHub 示例来源，适合底座适配验证 | 示例工具调用需全部替换为 mock；不得真实工单/检索/外呼 | OpenAI-compatible route 可适配；mock tools only | `mock_only`, `read_only`, `external_action_blocked` | yes | 不调用真实工具，不连接客服系统，不客户调用 | `can_mock_smoke` |
| 8 | P0 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | Airtable API | Airtable API terms；按 base/table read-only scope 管控 | 官方 API 来源，可信度高 | 库存、活动表、门店运营数据隐私；禁止写表 | BYOK；read-only/mock rows | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不连接真实 base，不写行，不改库存 | `can_mock_smoke` |
| 9 | P1 | `quality_sprint03_mdskills_file_processing_excel_candidate` | mdskills.ai spreadsheet/file skills | marketplace 线索；具体 `SKILL.md`、LICENSE、依赖未定位 | 来源可信度待核验 | 文件读取、表格清洗、财务数据隐私；可能依赖外部文件工具 | 暂不进入 smoke；需补真实上游 | `mock_only`, `read_only`, `external_action_blocked` | no | 不读取客户文件，不按 marketplace 页面放行 | `needs_more_license_info` |
| 10 | P1 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | Slack API | Slack API terms；按 history read-only scope 管控 | 官方 API 来源，可信度高 | 频道消息、客户/员工隐私；禁止发消息 | BYOK；read-only/mock messages | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不连接真实 workspace，不发消息，不邀请/改频道 | `can_mock_smoke` |
| 11 | P1 | `quality_sprint03_deepagents_research_report_example_candidate` | langchain-ai/deepagents research examples | 源仓库许可证需在正式封装前复核；L1 仅 workflow mock | GitHub 示例来源，适合底座适配验证 | 外部搜索/抓取工具必须禁用；仅用户提供材料 | OpenAI-compatible route 可适配；mock docs only | `mock_only`, `read_only`, `external_action_blocked` | yes | 不联网搜索，不抓取网页，不调用外部工具 | `can_mock_smoke` |
| 12 | P1 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | Google Drive API | Google Drive API terms；按 file metadata/read-only scope 管控 | 官方 API 来源，可信度高 | 文档隐私、合同/票据/制度文件；禁止移动、删除、共享或写文件 | BYOK；read-only/mock file metadata | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不读真实文件内容，不移动/删除/共享文件 | `can_mock_smoke` |
| 13 | P1 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | HubSpot CRM API | HubSpot API terms；CRM scopes 需最小化 | 官方 API 来源，可信度高 | 联系人 PII、销售跟进记录、CRM 写入风险 | BYOK；dry-run only；`write_allowed=false` | `dry_run_only`, `BYOK_required`, `external_action_blocked` | yes | 不写联系人，不建任务，不发送邮件，不改 deal | `can_dry_run_smoke` |
| 14 | P1 | `quality_sprint03_mcp_xero_ar_followup_candidate` | Xero API | Xero API terms；财务数据按只读与非审计声明管控 | 官方 API 来源，可信度高 | 应收账款、客户财务隐私；税务/审计结论风险 | BYOK；read-only/mock invoices | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不发送催收，不改 invoice，不做审计/税务结论 | `can_mock_smoke` |
| 15 | P1 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | QuickBooks API | Intuit/QuickBooks API terms；财务数据需严格只读 | 官方 API 来源，可信度高 | 账户、费用、现金流敏感数据；地区会计/税务差异 | BYOK；read-only/mock accounts | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不写账，不报税，不给审计结论，不改业务数据 | `can_mock_smoke` |
| 16 | P1 | `quality_sprint03_openagentskills_social_card_candidate` | Open Agent Skills registry / social card lead | 仅有 registry 线索；具体 repo、`SKILL.md`、LICENSE 未定位完整 | 来源可信度待核验 | 可能调用图像 provider 或写素材文件；需确认外部依赖 | 暂不进入 smoke；需补 child skill、LICENSE、provider 边界 | `dry_run_only`, `external_action_blocked` | no | 不生成图片，不上传素材，不按 marketplace 页面放行 | `needs_more_license_info` |
| 17 | P1 | `quality_sprint03_vercel_agent_skills_data_report_candidate` | vercel-labs/skills | GitHub 仓库线索；需定位具体 data-report child skill、LICENSE、依赖 | GitHub 来源较可信，但子 skill 未明确 | 标准 Skill 包适配、数据文件读取、是否面向业务场景待核验 | 暂不进入 smoke；需补具体 child skill/manifest | `mock_only`, `read_only`, `external_action_blocked` | no | 不读取文件，不封装，不按整仓放行 | `needs_more_license_info` |
| 18 | P1 | `quality_sprint03_openai_tts_training_microcourse_candidate` | OpenAI Audio/TTS route | OpenAI API / TTS terms；需遵守声音权利、内容政策和费用 | 官方 provider route，可信度高 | 培训音频、声音/配音权利、内容安全、费用 | BYOK 或中转站 audio route；L1 仅 payload/route check | `dry_run_only`, `BYOK_required`, `provider_api_required`, `real_media_generation_requires_approval`, `external_action_blocked` | yes | 不生成音频，不克隆声音，不上传音频样本 | `can_route_check` |
| 19 | P1 | `quality_sprint03_canva_connect_brand_kit_qc_candidate` | Canva Connect APIs | Canva API terms；read-only brand/design JSON 边界 | 官方 API 来源，可信度高 | 品牌素材、设计文件隐私、导出/写设计风险 | BYOK；read-only/mock design JSON；no export | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不导出设计，不写设计，不上传素材 | `can_mock_smoke` |
| 20 | P1 | `quality_sprint03_mcp_google_merchant_feed_qc_candidate` | Google Merchant API | Google Merchant / Shopping Content API terms；商品数据只读 | 官方 API 来源，可信度高 | 商品 feed、价格、图片、库存数据隐私；禁止改 feed | BYOK；read-only/mock feed rows | `mock_only`, `read_only`, `BYOK_required`, `external_action_blocked` | yes | 不写 feed，不改价格/图片/库存，不发布 | `can_mock_smoke` |

