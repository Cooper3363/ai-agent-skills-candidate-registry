# QUALITY_SOURCE_SPRINT_03 许可证复核队列

更新日期: 2026-06-05

## 来源

- 研究文件: `../QUALITY_SOURCE_SPRINT_03_RESULT.md`
- 优质线索: 60
- 本队列只收 20 个优先入库候选。
- 不送 L2，不封装，不客户调用。

## 队列摘要

| 分类 | 数量 |
| --- | ---: |
| P0 | 8 |
| P1 | 12 |
| 媒体生成/编辑类 | 6 |
| SaaS/MCP/API connector 类 | 9 |
| 标准 Skill 包 / SKILL.md 来源类 | 5 |
| DeepAgents workflow 来源类 | 2 |

## 20 个优先入库候选复核表

| priority | candidate_id | source_name | source_url | source_type | has_skill_md | has_skill_yaml | deepagents_fit | openai_compatible_route_fit | external_provider_dependency | business_package | six_department_role | smb_use_case | quality_score | recommended_state | trial_mode | media | real_generation | BYOK | dedupe_relation | license_review_focus | route / provider focus | test_smoke_focus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | `quality_sprint03_mcp_shopify_readonly_product_catalog_candidate` | Shopify product catalog API/MCP | https://shopify.dev/docs/api | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | 商品目录只读审查：标题、属性、缺图、库存提示 | 86 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Sprint01 order ops 的细分只读补充 | Shopify read-only catalog scope、禁止写商品、商品数据隐私 | read-only/mock catalog only | mock products -> catalog review |
| P0 | `quality_sprint03_openai_image_product_variant_candidate` | OpenAI Images API | https://platform.openai.com/docs/guides/images | Image API | no | no | payload_adapter | native_openai_route | yes | 电商/门店 | 电商运营 | 商品图变体、背景替换 prompt/payload | 86 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Next50 OpenAI image 路线细分 | Images API 条款、素材上传、商用输出、中转站 image route | no real generation in L1 | product brief -> image payload |
| P0 | `quality_sprint03_openai_image_poster_layout_candidate` | OpenAI Images API | https://platform.openai.com/docs/guides/images | Image API | no | no | payload_adapter | native_openai_route | yes | 营销 | 市场/设计 | 门店海报/优惠券视觉 prompt/payload | 85 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | OpenAI image 路线细分 | image route、商用、上传素材、中文文字表现 | no real generation in L1 | campaign brief -> poster payload |
| P0 | `quality_sprint03_mcp_stripe_subscription_health_candidate` | Stripe API | https://docs.stripe.com/api | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 经营/财务 | 订阅/收款健康度、失败支付摘要，不处理付款 | 84 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Sprint01 Stripe invoice 补充 | Stripe API 条款、read-only、PCI/隐私、非财务/审计结论 | read-only/mock charges only | mock charges/subscriptions -> health summary |
| P0 | `quality_sprint03_openagentskills_drawio_process_candidate` | Open Agent Skills drawio skill | https://openagentskills.dev/ | Agent Skill registry | yes_possible | no | skill_adapter_possible | openai_compatible | no | 行政/财务/HR | 行政/运营 | SOP 流程图、售后流程图、培训图示 | 84 | `needs_license_review` | `dry_run_metadata_only` | 否 | 否 | 否 | 新增标准 Skill 包方向 | 具体 SKILL.md、repo license、drawio 文件输出边界 | local spec only; no file write unless approved | 售后流程 -> Mermaid/drawio spec |
| P0 | `quality_sprint03_mcp_notion_policy_gap_candidate` | Notion API | https://developers.notion.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服/行政 | 知识库政策缺口、冲突和过期提醒 | 84 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Sprint01 Notion 知识库细分 | Notion API terms、read-only pages、页面权限和隐私 | read-only/mock pages | mock docs -> gap/conflict report |
| P0 | `quality_sprint03_deepagents_customer_ops_example_candidate` | DeepAgents examples | https://github.com/langchain-ai/deepagents | DeepAgents workflow/examples | possible | no | native_like | openai_compatible | no | 客服 | 客服主管 | 客服处理 workflow 的本地可迁移样例 | 83 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | 本地底座适配性强 | repo license、example path、工具调用边界 | mock tools only | mock support case -> agent plan |
| P0 | `quality_sprint03_mcp_airtable_inventory_ops_candidate` | Airtable API | https://airtable.com/developers/web/api/introduction | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 门店店长 | Airtable 库存/活动表异常摘要，只读 | 83 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Sprint01 Airtable ops 细分 | Airtable API terms、read-only base scope、表格隐私 | mock/read-only rows | mock base rows -> inventory alerts |
| P1 | `quality_sprint03_mdskills_file_processing_excel_candidate` | mdskills.ai spreadsheet/file skills | https://www.mdskills.ai/ | Agent Skill marketplace | yes_possible | no | skill_adapter_possible | openai_compatible | possible | 经营报表 | 经营/财务 | 表格清洗、指标口径检查、周报结构化 | 83 | `needs_license_review` | `metadata_review_only` | 否 | 否 | 可能 | 稳交付报表类补充来源 | 具体 SKILL.md、license、依赖、文件读取权限 | metadata only | mock rows -> clean/report spec |
| P1 | `quality_sprint03_mcp_slack_channel_faq_gap_candidate` | Slack API | https://api.slack.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 客服 | 客服主管 | 从支持频道摘要 FAQ 缺口，不发消息 | 83 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Sprint01 Slack triage 细分 | Slack history scope、频道隐私、禁止发送 | read-only/mock messages | mock channel messages -> FAQ gaps |
| P1 | `quality_sprint03_deepagents_research_report_example_candidate` | DeepAgents research examples | https://github.com/langchain-ai/deepagents | DeepAgents workflow/examples | possible | no | native_like | openai_compatible | no | 销售 | 销售/市场 | 潜客/竞品 research report workflow，本地 mock | 82 | `needs_license_review` | `mock_only` | 否 | 否 | 否 | lead research 补充 | repo license、外部搜索禁用、工具边界 | user-provided docs only | mock company docs -> research brief |
| P1 | `quality_sprint03_mcp_google_drive_doc_classifier_candidate` | Google Drive API | https://developers.google.com/drive/api | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 行政 | 文档分类、制度/合同/票据归档建议，不移动文件 | 82 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | 行政文档补充 | Drive read-only scope、文件隐私、禁止移动/删除 | read-only/mock file metadata | mock file metadata -> classify |
| P1 | `quality_sprint03_mcp_hubspot_contact_health_candidate` | HubSpot CRM API | https://developers.hubspot.com/ | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 销售 | 销售主管 | 联系人资料完整度、跟进风险、下一步建议 | 82 | `needs_license_review` | `dry_run_only` | 否 | 否 | 是 | Sprint01 HubSpot 能力补充 | HubSpot API scope、禁止写联系人、联系人隐私 | `write_allowed=false` | mock contacts -> data health report |
| P1 | `quality_sprint03_mcp_xero_ar_followup_candidate` | Xero API | https://developer.xero.com/documentation/api/accounting/overview | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 行政/财务/HR | 财务 | 应收账款提醒建议，不发送、不做审计 | 82 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Sprint01 Xero 补充 | API terms、read-only、非审计税务声明、财务隐私 | read-only/mock invoices | mock invoices -> AR followup plan |
| P1 | `quality_sprint03_mcp_quickbooks_cashflow_warning_candidate` | QuickBooks API | https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 经营报表 | 财务/管理 | 现金流风险提示、费用趋势，不给税务结论 | 82 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | QuickBooks 摘要补充 | API terms、privacy、非税务/审计 | read-only/mock accounts | mock accounts -> cashflow warning |
| P1 | `quality_sprint03_openagentskills_social_card_candidate` | Open Agent Skills social card skill | https://openagentskills.dev/ | Agent Skill registry | yes_possible | no | skill_adapter_possible | openai_compatible | possible | 营销 | 市场/设计 | 社媒卡片/活动封面生成规范和素材 brief | 82 | `needs_license_review` | `metadata_review_only` | 是 | 可能 | 可能 | Sprint01/02 海报类补充，偏标准包 | 具体 SKILL.md、repo license、是否调用外部图像 provider | metadata only | 活动 brief -> social card spec |
| P1 | `quality_sprint03_vercel_agent_skills_data_report_candidate` | vercel-labs/skills | https://github.com/vercel-labs/skills | Agent Skill repository | yes | no | skill_adapter_possible | openai_compatible | possible | 经营报表 | 运营/管理 | 从标准 SKILL.md 模板抽数据报告 skill 规范 | 82 | `needs_license_review` | `metadata_review_only` | 否 | 否 | 可能 | 标准 SKILL.md 来源补强 | repo license、子 skill、依赖、是否面向业务 | metadata only | mock metrics -> skill trigger/spec |
| P1 | `quality_sprint03_openai_tts_training_microcourse_candidate` | OpenAI Audio/TTS route | https://platform.openai.com/docs/guides/text-to-speech | Audio API | no | no | payload_adapter | native_openai_route | yes | 行政/财务/HR | HR/培训 | SOP/制度培训音频脚本和 TTS payload | 82 | `needs_license_review` | `dry_run_payload_only` | 是 | 是 | 是 | Sprint01 TTS 培训补充 | TTS 条款、声音权利、内容政策、中转站 audio route | no real audio generation | training text -> TTS payload |
| P1 | `quality_sprint03_canva_connect_brand_kit_qc_candidate` | Canva Connect APIs | https://www.canva.dev/docs/ | Design SaaS/API | no | no | tool_adapter | n/a_model_via_deepagents | yes | 营销 | 市场/设计 | 品牌套件一致性检查，不导出、不写设计 | 81 | `needs_license_review` | `read_only_mock` | 是 | 否 | 是 | Sprint02 Canva export 的低风险细分 | Canva API terms、read-only、no export、素材隐私 | mock/read-only design JSON | mock brand kit -> QC report |
| P1 | `quality_sprint03_mcp_google_merchant_feed_qc_candidate` | Google Merchant API | https://developers.google.com/shopping-content | SaaS/API connector | no | no | tool_adapter | n/a_model_via_deepagents | yes | 电商/门店 | 电商运营 | 商品 feed 缺字段、标题/图片/价格风险检查 | 81 | `needs_license_review` | `read_only_mock` | 否 | 否 | 是 | Merchant feed 候选细分 | API terms、商品数据隐私、禁止改 feed | read-only/mock feed | mock feed rows -> QC report |

## P0 / P1 处理建议

- P0 8 个优先 L1：更容易进入 read-only/mock/payload smoke。
- P1 12 个作为第二批：重点补充具体 SKILL.md、API 条款、Provider route、隐私和 BYOK 条件。
- 媒体类候选在 L1 前不得真实生成。
- SaaS/MCP/API connector 在 L1 前不得连接真实账号或写系统。
- 标准 Skill 包候选必须先定位具体子目录和 LICENSE，不能只凭 marketplace 页面入库。

## 禁止动作

- 不真实调用 API。
- 不生成图片、视频、音频或真实文件。
- 不写 API key。
- 不写稳交付库。
- 不把 market lead 宣称为可调用 Skill。
