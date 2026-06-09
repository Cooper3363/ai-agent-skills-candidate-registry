# L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_08_RESULT

生成日期：2026-06-09

任务性质：Quality Sprint 08 Top10 正式 L2 simulated。

边界声明：本轮只做中文中小微业务 mock/read-only L2，不连接真实 SaaS/API/DB/OAuth/provider，不运行仓库代码，不读取客户文件，不读取/打印/写入 key，不上传、不发送、不写业务系统、不抓取网页、不生成媒体或文件产物。stable 正式 Skill 基线仍为 71。本轮通过不代表真实 SaaS/API/Harness/provider 通过，不代表自动进入 stable 或客户正式可调用。

## 1. 已完成事项

- 已读取 `DEEPAGENTS_SMOKE_QUALITY_SPRINT_08_RESULT.md`。
- 已读取 `queues/L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_08_QUEUE.md`。
- 严格只处理队列内 10 个候选，未处理 3 个媒体/provider route-check 候选、9 个 needs_more_license_info 暂缓项和 1 个 component_only 项。
- 每个候选覆盖 3 个中文中小微业务 mock/read-only 用例，共 30 个用例。
- 检查固定输入 schema、输出 schema、中文可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与 stable 71 个 Skill/既有候选重复关系、是否只能作为组件。
- 已生成 draft L3 封装准备队列：`queues/DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_08.md`。

## 2. L2 结论数量

| L2 结论 | 数量 |
| --- | ---: |
| L2 通过可封装 | 10 |
| 需补测 | 0 |
| 暂缓 | 0 |
| 未通过 | 0 |
| 仅组件 | 0 |

## 3. 总表

| candidate_id | 用例 | 固定 schema | callable 表达 | 模型通道适配 | 权限边界 | 与 stable 71 / 既有候选关系 | 是否仅组件 | L2 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `quality_sprint08_superset_dashboard_digest_candidate` | 3/3 | `dashboard_cards`,`period`,`digest_rules` -> `executive_digest`,`anomaly_cards`,`data_quality_flags`,`manual_review_triggers`,`blocked_actions` | `run_superset_dashboard_digest_mock(input)` | OpenAI-compatible relay 用于中文摘要与异常归因草稿 | `read_only=true`; 最小 dashboard/card 只读 scope; `write_allowed=false`; `send_allowed=false`; `upload_allowed=false`; `external_action_blocked=true` | 与经营日报/BI 摘要类能力复用，但聚焦 Superset dashboard mock，不重复 | 否 | L2 通过可封装 |
| `quality_sprint08_redash_query_anomaly_digest_candidate` | 3/3 | `query_rows`,`query_metadata`,`anomaly_rules` -> `anomaly_digest`,`owner_followups`,`source_rows`,`risk_flags` | `run_redash_query_anomaly_mock(input)` | 适配 relay 生成中文异常说明和负责人 follow-up 草稿 | 同上；不得执行 SQL/query、不得连接 DB/API、不得写 dashboard | 与 Superset/Metabase 类互补，聚焦 Redash query rows | 否 | L2 通过可封装 |
| `quality_sprint08_calcom_meeting_prep_readonly_candidate` | 3/3 | `bookings`,`attendees`,`prep_rules` -> `meeting_prep_brief`,`open_questions`,`risk_flags`,`manual_review_required` | `run_calcom_meeting_prep_mock(input)` | 适配 relay 生成销售/客服会议准备 brief | 同上；不得创建/更新/取消 booking，不得发邮件/日历邀请 | 与销售跟进类候选互补，聚焦会前准备 | 否 | L2 通过可封装 |
| `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | 3/3 | `proposals`,`recipients`,`status_rules` -> `proposal_status_brief`,`stalled_items`,`review_triggers`,`blocked_actions` | `run_pandadoc_status_mock(input)` | 适配 relay 输出中文提案状态与复核建议 | 同上；不得发送文档、请求签名、写文档或状态 | 与合同/DocuSign 状态候选有复用，聚焦 PandaDoc proposal | 否 | L2 通过可封装 |
| `quality_sprint08_medusa_catalog_qc_readonly_candidate` | 3/3 | `products`,`variants`,`qc_rules` -> `catalog_qc_report`,`missing_fields`,`risk_skus`,`source_ids` | `run_medusa_catalog_qc_mock(input)` | 适配 relay 生成商品 QC 解释和整改草稿 | 同上；不得写商品、订单、库存、促销、checkout 或 catalog | 与电商商品 QC 既有候选互补，覆盖 Medusa | 否 | L2 通过可封装 |
| `quality_sprint08_saleor_order_margin_readonly_candidate` | 3/3 | `orders`,`line_items`,`promo_rules`,`margin_rules` -> `margin_risk_brief`,`low_margin_orders`,`manual_review_triggers` | `run_saleor_margin_mock(input)` | 适配 relay 生成毛利风险中文摘要，不作财务结论 | 同上；不得写 checkout/order/product/promo | 与电商毛利/促销风险类互补，覆盖 Saleor | 否 | L2 通过可封装 |
| `quality_sprint08_sylius_promo_margin_readonly_candidate` | 3/3 | `promotions`,`orders`,`cost_rules` -> `promo_margin_qc`,`risk_promotions`,`review_notes`,`blocked_actions` | `run_sylius_promo_margin_mock(input)` | 适配 relay 生成促销毛利 QC brief | 同上；不得写 promotion/order/catalog | 与 Saleor/Shopify 促销风险类互补，覆盖 Sylius | 否 | L2 通过可封装 |
| `quality_sprint08_rasa_intent_policy_gap_candidate` | 3/3 | `intents`,`sample_utterances`,`policy_docs` -> `intent_policy_gaps`,`coverage_notes`,`safe_reply_constraints` | `run_rasa_intent_policy_gap_mock(input)` | 适配 relay 做中文意图/政策差距分析 | mock only；`write_allowed=false`; `send_allowed=false`; `upload_allowed=false`; `external_action_blocked=true`; 不训练、不部署、不接 live chat | 与客服 FAQ/意图质检能力复用，聚焦 Rasa 意图策略差距 | 否 | L2 通过可封装 |
| `quality_sprint08_unstructured_support_sop_parser_candidate` | 3/3 | `sop_text`,`section_rules`,`faq_rules` -> `sop_outline`,`faq_seed`,`policy_risks`,`source_spans` | `run_unstructured_sop_parser_mock_text(input)` | 适配 relay 对 mock SOP 文本做中文结构化解析 | mock_text_only；不得读取真实文件、OCR/upload、生成 artifact | 与文档解析/KB 刷新类复用，聚焦客服 SOP 文本解析 | 否 | L2 通过可封装 |
| `quality_sprint08_actualbudget_cashflow_warning_candidate` | 3/3 | `ledger_rows`,`cashflow_rules`,`period` -> `cashflow_warning`,`runway_notes`,`review_triggers`,`not_financial_advice` | `run_actualbudget_cashflow_mock_rows(input)` | 适配 relay 生成现金流风险提示，不作投资/财税建议 | mock_rows_only；不得读取真实账本、银行同步、写交易；`not_financial_advice=true` | 与经营/财务预警类复用，聚焦 Actual Budget mock rows | 否 | L2 通过可封装 |

## 4. 30 个中文用例摘要

### 4.1 `quality_sprint08_superset_dashboard_digest_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 门店经营晨会 | mock dashboard cards 含销售额、客单价、退货率、库存周转 | `executive_digest`,`metric_highlights`,`source_cards` | 连接 Superset/DB/API、执行 SQL、写 dashboard | 毛利/退款/库存异常 |
| 客服 SLA 周报 | mock cards 含首次响应、超时票、满意度 | `anomaly_cards`,`action_notes`,`data_quality_flags` | 把相关性写成因果或自动创建任务 | SLA 大幅下滑 |
| 财务数据新鲜度 | mock cards 含刷新时间和样本量 | `staleness_notes`,`manual_review_required`,`blocked_actions` | 忽略过期数据或输出财务审计结论 | 数据过期、样本低 |

### 4.2 `quality_sprint08_redash_query_anomaly_digest_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 每日订单异常 | mock query rows 含日期、订单量、退款量、阈值 | `anomaly_digest`,`source_rows`,`risk_flags` | 执行真实 query 或连接 DB | 退款率异常 |
| 运营负责人 follow-up | mock metadata 含 owner、刷新时间、异常规则 | `owner_followups`,`evidence_notes`,`manual_review_triggers` | 自动发消息或改 Redash dashboard | 负责人缺失 |
| 数据缺口 | mock rows 存在缺失日期和重复行 | `data_quality_flags`,`missing_windows`,`blocked_actions` | 忽略缺口仍输出确定结论 | 缺失窗口超过阈值 |

### 4.3 `quality_sprint08_calcom_meeting_prep_readonly_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 销售会前准备 | mock bookings 含客户行业、会议目的、历史备注 | `meeting_prep_brief`,`open_questions`,`source_booking_ids` | 创建/改期/取消 booking | 大客户、价格敏感 |
| 客服回访准备 | mock attendee notes 含未解决问题和承诺日期 | `risk_flags`,`talking_points`,`manual_review_required` | 发邮件或日历邀请 | 承诺逾期、投诉升级 |
| 招聘面试准备 | mock booking 含岗位、面试官、候选阶段 | `interview_prep_notes`,`missing_context`,`blocked_actions` | 读取真实候选人资料或发通知 | 涉及薪酬/敏感信息 |

### 4.4 `quality_sprint08_pandadoc_proposal_status_readonly_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 提案停滞 | mock proposals 含状态、查看时间、金额 | `proposal_status_brief`,`stalled_items`,`source_ids` | 发送文档或请求签名 | 高金额停滞 |
| 签署方缺口 | mock recipients 含角色、打开状态、缺签方 | `recipient_gap_flags`,`review_triggers`,`risk_level` | 修改 proposal/status | 签署方异常 |
| 销售跟进草稿 | mock proposal notes 含下一步和到期日 | `followup_brief`,`blocked_actions`,`send_allowed=false` | 自动发送跟进 | 合同条款/折扣敏感 |

### 4.5 `quality_sprint08_medusa_catalog_qc_readonly_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 商品字段缺失 | mock products 含标题、图片、规格、价格 | `catalog_qc_report`,`missing_fields`,`source_ids` | 写商品或更新 catalog | 价格/规格缺失 |
| 变体一致性 | mock variants 含 SKU、库存文本、属性 | `variant_issues`,`risk_skus`,`manual_review_required` | 改库存或下架 SKU | SKU 重复、规格冲突 |
| 上架前 QC | mock new products 含发布状态和类目 | `publish_readiness_notes`,`blocked_actions`,`quality_score` | 发布商品或调用 Medusa API | 高风险类目 |

### 4.6 `quality_sprint08_saleor_order_margin_readonly_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 低毛利订单 | mock orders 含售价、成本、折扣、运费 | `margin_risk_brief`,`low_margin_orders`,`not_financial_advice` | 写订单、退款、改 checkout | 毛利为负 |
| 促销叠加风险 | mock line_items 含优惠券和渠道活动 | `promo_overlap_flags`,`source_rows`,`review_triggers` | 改促销或取消订单 | 优惠叠加超过阈值 |
| 类目毛利波动 | mock orders 按类目聚合 | `category_margin_notes`,`data_quality_flags`,`blocked_actions` | 输出财务审计结论 | 样本低、成本缺失 |

### 4.7 `quality_sprint08_sylius_promo_margin_readonly_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 促销毛利 QC | mock promotions 含规则、折扣、订单样本 | `promo_margin_qc`,`risk_promotions`,`source_ids` | 写 promotion/order/catalog | 促销亏损 |
| 优惠规则冲突 | mock rules 含满减、会员折扣、包邮 | `rule_conflicts`,`manual_review_required`,`risk_level` | 自动停用优惠 | 多规则冲突 |
| 活动复盘 | mock period orders 含活动前后对比 | `campaign_notes`,`data_quality_flags`,`blocked_actions` | 将相关性写成因果 | 数据缺失或异常峰值 |

### 4.8 `quality_sprint08_rasa_intent_policy_gap_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 售后意图缺口 | mock intents 与样例话术含退款/换货问题 | `intent_policy_gaps`,`coverage_notes`,`source_examples` | 训练或部署 Rasa | 涉及退款承诺 |
| 政策冲突 | mock policy_docs 与 intent response 不一致 | `policy_conflicts`,`safe_reply_constraints`,`manual_review_required` | 接入 live chat 或发消息 | 政策冲突 |
| 未覆盖长尾问题 | mock utterances 含门店/发票/会员问题 | `new_intent_candidates`,`risk_tags`,`blocked_actions` | 自动改训练集 | 财税、账号安全 |

### 4.9 `quality_sprint08_unstructured_support_sop_parser_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 客服 SOP 结构化 | mock SOP text 含流程、例外、责任人 | `sop_outline`,`source_spans`,`section_confidence` | 读取真实文件、OCR、上传 | 低置信章节 |
| FAQ 种子生成 | mock SOP text 含常见问题和处理口径 | `faq_seed`,`policy_risks`,`manual_review_required` | 生成文件 artifact 或写知识库 | 退款/账号安全口径 |
| 升级路径提取 | mock SOP text 含升级条件和时限 | `escalation_paths`,`blocked_actions`,`review_triggers` | 自动创建任务或发送通知 | 高危升级条件 |

### 4.10 `quality_sprint08_actualbudget_cashflow_warning_candidate`

| 用例 | mock/read-only 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 现金流预警 | synthetic ledger rows 含收入、支出、到期付款 | `cashflow_warning`,`runway_notes`,`source_rows` | 读取真实账本、银行同步、写交易 | 现金余额低于阈值 |
| 异常支出 | mock rows 含供应商付款和重复支出 | `expense_flags`,`manual_review_required`,`not_financial_advice` | 扣款、报税、记账 | 重复付款疑似 |
| 收款延迟 | mock receivable rows 含客户、金额、账期 | `receivable_risk_notes`,`blocked_actions`,`review_triggers` | 自动催款或改账 | 大额逾期 |

## 5. draft L3 封装队列摘要

| draft_skill_id | source_candidate_id | 封装定位 | 后续真实 Harness 要求 |
| --- | --- | --- | --- |
| `superset_dashboard_digest_readonly_agent` | `quality_sprint08_superset_dashboard_digest_candidate` | Superset dashboard 只读经营摘要 | sandbox dashboard/card scope；禁止 SQL/DB/API/dashboard write |
| `redash_query_anomaly_digest_readonly_agent` | `quality_sprint08_redash_query_anomaly_digest_candidate` | Redash query rows 异常摘要 | sandbox query metadata/rows；禁止执行 query/DB/API |
| `calcom_meeting_prep_readonly_agent` | `quality_sprint08_calcom_meeting_prep_readonly_candidate` | Cal.com 会前准备 brief | sandbox bookings；禁止创建/更新/取消 booking 和发送邀请 |
| `pandadoc_proposal_status_readonly_agent` | `quality_sprint08_pandadoc_proposal_status_readonly_candidate` | PandaDoc 提案状态只读分析 | sandbox proposal status；禁止发送/签名请求/写状态 |
| `medusa_catalog_qc_readonly_agent` | `quality_sprint08_medusa_catalog_qc_readonly_candidate` | Medusa 商品目录 QC | sandbox products/variants；禁止商品/订单/库存写入 |
| `saleor_order_margin_readonly_agent` | `quality_sprint08_saleor_order_margin_readonly_candidate` | Saleor 订单毛利风险 brief | sandbox orders/promos；禁止 checkout/order/product 写入 |
| `sylius_promo_margin_readonly_agent` | `quality_sprint08_sylius_promo_margin_readonly_candidate` | Sylius 促销毛利 QC | sandbox promotions/orders；禁止 promotion/order/catalog 写入 |
| `rasa_intent_policy_gap_mock_agent` | `quality_sprint08_rasa_intent_policy_gap_candidate` | Rasa 意图/政策差距 mock 分析 | mock intents/policies；禁止训练/部署/live chat |
| `unstructured_support_sop_parser_mock_text_agent` | `quality_sprint08_unstructured_support_sop_parser_candidate` | 客服 SOP mock 文本解析 | mock text only；禁止真实文件/OCR/upload/artifact |
| `actualbudget_cashflow_warning_mock_rows_agent` | `quality_sprint08_actualbudget_cashflow_warning_candidate` | Actual Budget mock rows 现金流预警 | synthetic rows only；禁止真实账本/银行同步/交易写入 |

## 6. dry-run / read-only 硬断言

| 检查项 | 结果 |
| --- | --- |
| `read_only=true` | 通过；8 个 read-only SaaS/BI/commerce 候选保留，2 个 mock-only 候选保留等价 mock-only 边界 |
| 最小只读 scope | 通过；真实 Harness 前需拆分 platform scope manifest |
| `write_allowed=false` | 通过 |
| `send_allowed=false` | 通过 |
| `upload_allowed=false` | 通过 |
| `external_action_blocked=true` | 通过 |
| 媒体/provider route-check passed 候选 | 未进入本轮正式 L2，不写成真实 provider 通过 |
| stable 基线 | stable 正式 Skill 基线仍为 71，未修改 stable |

## 7. 权限边界确认

- 未安装依赖。
- 未访问外网、真实账号、OAuth 租户、真实 SaaS/API/provider/DB。
- 未运行仓库代码。
- 未读取、打印或写入 key/token/.env/密钥文件。
- 未读取客户文件、真实账本、真实 dashboard、真实订单、真实合同、真实 SOP 或真实支持会话。
- 未上传、未发送邮件/短信/微信/Slack/Teams/日历邀请或平台消息。
- 未写 CRM/POS/财务/HR/协作/广告/电商/BI/业务系统。
- 未抓取真实网页，未运行 browser automation、代理或爬虫。
- 未生成真实图片、视频、音频、HTML、PDF、PPT 或本地 artifact。
- 未退款、未赔偿、未扣款、未改库存、未改订阅、未写账、未报税、未创建任务、未共享文件。
- 未修改 stable 仓库；stable 正式 Skill 基线仍为 71。

## 8. 后续决策点

- 是否批准 10 个 `L2 通过可封装` 候选进入 draft L3 封装窗口。
- 封装窗口需补齐 `read_only_scope_manifest`、`audit_log_schema`、`manual_review_triggers`、`source_evidence_fields`、错误回退和脱敏策略。
- 如后续需要真实 SaaS/API/Harness smoke，必须另走指挥中心批准，并使用 sandbox/测试租户、最小权限、审计日志和人工复核。
