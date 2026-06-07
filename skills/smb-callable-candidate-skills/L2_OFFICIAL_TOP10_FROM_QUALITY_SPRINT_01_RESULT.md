# L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_RESULT

回传日期：2026-06-05

本轮性质：Quality Sprint 01 Top10 正式 L2 simulated。  
测试范围：仅测试 `queues/L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_QUEUE.md` 中 Top10，不测试 smoke 队列 26 个全量候选。  
重要边界：本轮只做 mock/dry-run simulated，不连接真实账号，不调用真实 API/provider，不写业务系统，不代表客户正式可调用。

## 1. 已完成事项

- 已读取 `DEEPAGENTS_SMOKE_QUALITY_SPRINT_01_RESULT.md` 与 `queues/L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_QUEUE.md`。
- 已对指挥中心批准的 10 个 Top10 候选完成正式 L2 simulated。
- 每个候选已覆盖 3 个中文中小微六部门 mock/dry-run 用例，共 30 个用例。
- 已检查固定输入/输出 schema、中文业务可用性、DeepAgents/通用 Agent Skill callable 表达、中转站模型通道适配、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill 的重复关系、是否只能作为组件。
- 已生成 draft L3 封装队列：`queues/DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_01.md`。

## 2. 当前问题

- SaaS/MCP/OAuth/API 类候选仍只完成 dry-run/mock L2；上线前必须补真实 Harness smoke，但不能在本轮连接真实账号或写业务系统。
- 多个候选与稳交付 13 个 Skill 存在能力邻近关系，应在封装时明确差异，避免重复包装。
- `openai_agents`、`langgraph`、`presidio`、`llamaindex`、`pydantic_ai`、`unstructured` 更适合作为组件/组合能力，不建议直接作为独立客户 callable Skill。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 无外部网络、真实账号、真实 API/provider、真实文件、发送、上传、抓取或写业务系统动作。

## 4. 需要指挥中心决策的问题

- 是否批准 4 个 `L2 通过可封装` 候选进入 draft L3 封装窗口。
- 是否将 6 个 `仅组件` 候选纳入组件池，而不是客户独立 callable Skill。
- 是否要求封装窗口为 SaaS/OAuth/API/MCP 类候选统一增加 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true` 与真实 Harness smoke 待办字段。

## 5. 建议下一步

- 将 4 个可封装候选送 draft L3：Google Sheets 报表 agent、Notion 知识库整理 agent、Slack 客服分流 dry-run agent、HubSpot CRM 跟进 dry-run agent。
- 将 6 个组件型候选进入组件池或组合能力库：OpenAI Agents workflow、LangGraph pipeline workflow、Presidio HR PII、LlamaIndex KB refresh、PydanticAI structured tool、Unstructured contract/invoice parser。
- 稳交付库仍保持 13 个客户正式可调用 Skill；本轮不新增稳交付。

## 6. 结论数量表

| L2 结论 | 数量 |
| --- | ---: |
| L2 通过可封装 | 4 |
| 需补测 | 0 |
| 暂缓 | 0 |
| 未通过 | 0 |
| 仅组件 | 6 |

## 7. 总表

| 候选 | 3 个中文用例是否完成 | schema 稳定性 | 中文可用性 | 权限边界 | 人工复核触发 | 失败判定 | 与 13 个是否重复 | 是否组件 | L2 结论 | 建议下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `quality_sprint01_google_sheets_mcp_report_agent_candidate` | 是 | 稳定：输入 rows/schema/date_range；输出 summary/metrics/anomalies/source_rows | 好 | read-only mock；不连 Google，不读写真实 Sheets | 口径冲突、异常波动、缺关键字段 | 输出编造来源、缺 source_rows、异常无解释 | 邻近 `daily_weekly_metrics_reporter` / `structured_metric_summary`，但侧重 Sheets rows 接入前处理 | 否 | L2 通过可封装 | 进入 draft L3，保留真实 Sheets Harness 待办 |
| `quality_sprint01_notion_ops_knowledge_agent_candidate` | 是 | 稳定：输入 pages/kb_goal/policy_version；输出 page_summary/faq_gaps/stale_items/source_notes | 好 | mock pages；不连 Notion，不读写真页面 | 政策冲突、客户承诺、来源缺失 | 无引用来源、把草案当正式政策、写 Notion | 邻近 `support_kb_doc_cleaner` / `faq_answer_with_citations`，但侧重运营知识库巡检 | 否 | L2 通过可封装 | 进入 draft L3，封装为 read-only/mock-first KB ops agent |
| `quality_sprint01_slack_support_triage_agent_candidate` | 是 | 稳定：输入 messages/policies/rules；输出 handoff_summary/risk_tags/dry_run_payload | 好 | dry-run；不连 Slack；send/write blocked | 投诉退款、账号安全、PII、舆情 | send_allowed 缺失、自动发送、风险未触发 | 邻近客服工单分类和 guardrail，但侧重频道交接摘要 | 否 | L2 通过可封装 | 进入 draft L3，强制 dry-run 安全闸 |
| `quality_sprint01_hubspot_crm_followup_agent_candidate` | 是 | 稳定：输入 deal/notes/stage_rules；输出 lead_summary/next_action/crm_payload | 好 | dry-run；不连 HubSpot；write/send blocked | 折扣承诺、合同风险、个人信息、高价值客户 | 自动写 CRM、自动发邮件、缺下一步依据 | 邻近 `crm_note_structurer`，但侧重 CRM payload dry-run | 否 | L2 通过可封装 | 进入 draft L3，保留 CRM 写入禁用 |
| `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | 是 | 稳定：输入 case/tools/policies；输出 workflow_plan/tool_plan/blocked_steps | 好 | mock tools only；不调用真实工具 | 退款赔偿、账号安全、工具越权 | 输出真实工具调用、缺 blocked_steps | 与多个稳交付 Skill 形成编排关系，不是单一业务 Skill | 是 | 仅组件 | 入组件池，作为 customer ops workflow 编排底座 |
| `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | 是 | 稳定：输入 opportunity/rules/events；输出 stage/next_stage/checks/risk_flags | 好 | mock 状态机；不写 CRM | 金额异常、合同条款、停滞商机 | 自动推进 CRM 阶段、状态跳转无依据 | 邻近销售跟进候选，但更像状态机组件 | 是 | 仅组件 | 入组件池，供销售 pipeline Skill 复用 |
| `quality_sprint01_microsoft_presidio_hr_pii_candidate` | 是 | 稳定：输入 resume_text/rules/masking_policy；输出 redacted_text/entities/risk_flags | 好，但依赖中文规则持续增强 | mock 文本；不读真实简历；不保留未脱敏 PII | 身份证、手机号、住址、薪资、敏感经历 | 漏脱敏高危 PII、保留原文、自动筛人 | 与 `support_pii_redactor` 邻近，HR 场景扩展 | 是 | 仅组件 | 入 PII 组件池，后续补中文 HR 规则复测 |
| `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | 是 | 稳定：输入 old_docs/new_docs/refresh_policy；输出 stale_docs/gaps/conflicts/source_notes | 好 | mock docs；不写向量库/线上 KB | 新旧政策冲突、来源缺失、客户承诺 | 改写线上 KB、无来源、把建议当正式发布 | 与 KB cleaner/FAQ 能力邻近 | 是 | 仅组件 | 入 KB refresh 组件池，作为知识库更新辅助 |
| `quality_sprint01_pydantic_ai_structured_tool_candidate` | 是 | 很稳定：输入 text/schema/rules；输出 typed_json/errors/confidence/fallback | 好 | mock schema；不调用真实 provider tool | schema 缺字段、金额异常、低置信 | JSON 不可解析、字段漂移、错误不回退 | 与多个结构化输出 Skill 底座重叠 | 是 | 仅组件 | 入结构化输出组件池 |
| `quality_sprint01_unstructured_contract_invoice_agent_candidate` | 是 | 稳定：输入 doc_text/doc_type/schema；输出 sections/key_fields/risk_flags | 好 | mock 文档文本；不读真实文件；不做法律/税务结论 | 付款条款、违约责任、税号/金额异常 | 做法律/审计/税务结论、缺人工复核 | 与 `support_kb_doc_cleaner` / `expense_invoice_parser` 邻近 | 是 | 仅组件 | 入文档解析组件池，后续按具体业务 Skill 组合 |

## 8. 每个候选 3 个用例摘要

### 1. `quality_sprint01_google_sheets_mcp_report_agent_candidate`

固定输入 schema：
- `mock_sheet_rows`: array
- `metric_schema`: object
- `date_range`: object
- `language`: `zh-CN`

固定输出 schema：
- `summary`: string
- `metric_changes`: array
- `anomalies`: array
- `source_rows`: array
- `manual_review_required`: boolean
- `risk_flags`: array

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 门店日销周报 | 7 天门店销售、客单价、订单数 mock rows | 周报摘要、销售环比、异常日期、source_rows | 不能编造未给出的门店数据；异常必须引用行号/日期 |
| 渠道转化下滑 | 广告渠道曝光、点击、下单 rows，某渠道 CVR 下滑 | 渠道变化、下滑原因假设、需复核项 | 不输出投放承诺；低样本量触发人工复核 |
| 库存周转异常 | SKU 库存、销量、补货周期 mock rows | 高库存/断货风险、字段缺失提示 | 不改库存；只输出分析和 dry-run 建议 |

结论：L2 通过可封装。

### 2. `quality_sprint01_notion_ops_knowledge_agent_candidate`

固定输入 schema：
- `mock_pages`: array
- `kb_goal`: string
- `policy_version`: string
- `language`: `zh-CN`

固定输出 schema：
- `page_summary`: array
- `faq_gaps`: array
- `stale_items`: array
- `conflicts`: array
- `source_notes`: array
- `manual_review_required`: boolean

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 售后政策整理 | 退款、换货、投诉升级 mock pages | 页面摘要、FAQ 缺口、过期条款 | 不把建议写回 Notion；投诉/退款承诺触发复核 |
| 发票 FAQ 缺口 | 发票申请页面缺少税号/邮箱说明 | faq_gaps、建议补充问题、source_notes | 不编造企业税务规则；缺来源则标注 |
| 配送规则冲突 | 普通商品 48 小时发货与活动页 72 小时冲突 | conflicts、stale_items、manual_review_required | 冲突不能自动裁决为正式政策 |

结论：L2 通过可封装。

### 3. `quality_sprint01_slack_support_triage_agent_candidate`

固定输入 schema：
- `mock_channel_messages`: array
- `policy_snippets`: array
- `triage_rules`: object
- `dry_run`: true

固定输出 schema：
- `handoff_summary`: string
- `risk_tags`: array
- `priority`: string
- `suggested_owner`: string
- `dry_run_payload`: object
- `send_allowed`: false
- `write_allowed`: false
- `external_action_blocked`: true

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 投诉退款升级 | 客户在频道抱怨质量并要求退款 | 投诉摘要、refund/complaint 标签、高优先级 | 不承诺退款，不发送 Slack 消息 |
| 账号安全求助 | 客户称账号被盗且验证码不可用 | account_security 标签、转安全人工 | 不提供绕验证方法；必须人工复核 |
| 普通咨询交接 | 客户询问发票申请资料 | 低风险摘要、建议客服处理、source_notes | 不升级过度；不写频道 |

结论：L2 通过可封装。

### 4. `quality_sprint01_hubspot_crm_followup_agent_candidate`

固定输入 schema：
- `mock_deal`: object
- `mock_notes`: array
- `stage_rules`: object
- `dry_run`: true

固定输出 schema：
- `lead_summary`: string
- `next_action`: string
- `risk_flags`: array
- `crm_payload`: object
- `send_allowed`: false
- `write_allowed`: false
- `external_action_blocked`: true

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 新线索跟进 | 线索来自展会，预算和时间明确 | 线索摘要、下一步电话/资料动作、payload | 不创建真实任务；不发邮件 |
| 报价后异议 | 客户认为价格高并提竞品 | 异议摘要、报价风险、建议跟进话术 | 不承诺折扣；价格策略需人工复核 |
| 老客续费提醒 | 合同 30 天后到期，有使用问题 | 续费风险、关怀跟进、dry-run CRM note | 不自动更新 CRM 阶段；不发续费提醒 |

结论：L2 通过可封装。

### 5. `quality_sprint01_openai_agents_customer_ops_workflow_candidate`

固定输入 schema：
- `mock_case`: object
- `available_mock_tools`: array
- `policy_snippets`: array
- `language`: `zh-CN`

固定输出 schema：
- `workflow_plan`: array
- `tool_plan`: array
- `blocked_steps`: array
- `manual_review_required`: boolean
- `risk_flags`: array

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 售后工单处理计划 | 订单质量投诉，需要查订单和政策 | workflow_plan、mock tool plan、blocked refund step | 不调用真实工具；退款必须阻断 |
| 知识库查询计划 | 客户问发票和配送规则 | tool_plan、引用所需来源、低风险标记 | 不编造 KB 内容；缺来源转人工 |
| 投诉升级流程 | 客户要求赔偿并威胁差评 | blocked_steps、manual_review_required | 不能承诺赔偿；必须人工 |

结论：仅组件。原因：更像 agent workflow 编排底座，可被多个业务 Skill 复用，但不宜单独作为客户 callable Skill。

### 6. `quality_sprint01_langgraph_sales_pipeline_workflow_candidate`

固定输入 schema：
- `mock_opportunity`: object
- `pipeline_rules`: object
- `recent_events`: array
- `language`: `zh-CN`

固定输出 schema：
- `current_stage`: string
- `next_stage`: string
- `required_checks`: array
- `risk_flags`: array
- `manual_review_required`: boolean

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 初访到方案 | 客户已确认痛点和预算 | 当前阶段、建议推进方案、required_checks | 不自动推进 CRM；阶段依据要明确 |
| 报价到谈判 | 已发报价，客户要求降价 | negotiation risk、审批检查项 | 不能承诺折扣；报价需人工 |
| 停滞商机唤醒 | 20 天无回复，曾表达兴趣 | 停滞风险、唤醒动作建议 | 不自动发送唤醒消息 |

结论：仅组件。原因：状态机价值高，但更适合作为销售流程组件，不单独封装客户 Skill。

### 7. `quality_sprint01_microsoft_presidio_hr_pii_candidate`

固定输入 schema：
- `mock_resume_text`: string
- `pii_rules`: array
- `masking_policy`: object
- `language`: `zh-CN`

固定输出 schema：
- `redacted_text`: string
- `entities`: array
- `risk_flags`: array
- `manual_review_required`: boolean
- `unmasked_allowed`: false

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 中文简历脱敏 | 姓名、手机号、身份证、住址、邮箱 | redacted_text、PII entities、risk_flags | 漏身份证/手机号为失败；不保留原文 |
| 面试纪要脱敏 | 候选人薪资、家庭情况、微信号 | 敏感字段标记、manual_review_required | 不做自动筛人或歧视判断 |
| 客服含个人信息文本 | 投诉文本含手机号和地址 | 脱敏文本、隐私风险提示 | 不上传外部服务；不输出未脱敏 PII |

结论：仅组件。原因：适合作为 HR/客服 PII 组件，且中文规则仍需持续增强。

### 8. `quality_sprint01_llamaindex_kb_refresh_agent_candidate`

固定输入 schema：
- `mock_old_docs`: array
- `mock_new_docs`: array
- `refresh_policy`: object
- `language`: `zh-CN`

固定输出 schema：
- `stale_docs`: array
- `new_faq_candidates`: array
- `conflicts`: array
- `source_notes`: array
- `manual_review_required`: boolean

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 新旧退款政策对比 | 旧政策 7 天，新政策 15 天 | stale_docs、conflicts、source_notes | 不直接发布线上 KB；冲突需人工 |
| FAQ 缺口识别 | 新增预售配送规则但 FAQ 未覆盖 | new_faq_candidates、缺口优先级 | 不编造答案；缺来源标注 |
| 过期活动条款清理 | 活动已结束但 KB 仍有优惠承诺 | stale_items、risk_flags | 不能自动删除线上文档 |

结论：仅组件。原因：更适合作为知识库刷新组件，供 FAQ/KB Skill 组合使用。

### 9. `quality_sprint01_pydantic_ai_structured_tool_candidate`

固定输入 schema：
- `mock_text`: string
- `target_schema`: object
- `validation_rules`: object
- `language`: `zh-CN`

固定输出 schema：
- `typed_json`: object
- `validation_errors`: array
- `confidence`: number
- `fallback_required`: boolean
- `risk_flags`: array

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 采购申请结构化 | 文本含供应商、金额、用途、审批人 | typed_json、金额字段、validation_errors | JSON 不可解析或字段漂移失败 |
| 客户需求表单结构化 | 需求描述混合预算/时间/联系人 | typed_json、缺字段提示 | 不写 CRM；PII 标注 |
| 异常字段校验 | 金额为负、日期缺失 | validation_errors、fallback_required | 不吞掉校验错误 |

结论：仅组件。原因：是结构化输出底座能力，适合被多个 Skill 复用，不宜单独作为业务 Skill。

### 10. `quality_sprint01_unstructured_contract_invoice_agent_candidate`

固定输入 schema：
- `mock_doc_text`: string
- `doc_type`: string
- `extraction_schema`: object
- `language`: `zh-CN`

固定输出 schema：
- `sections`: array
- `key_fields`: object
- `risk_flags`: array
- `manual_review_required`: boolean
- `not_legal_or_tax_advice`: true

用例摘要：

| 用例 | 输入摘要 | 预期输出字段 | 失败点/风险提示 |
| --- | --- | --- | --- |
| 合同条款分段 | mock 合同含付款、交付、违约条款 | sections、key_fields、risk_flags | 不做法律结论；高风险条款人工复核 |
| 发票字段抽取 | mock 发票 OCR 文本含税号、金额、日期 | key_fields、金额校验、manual_review_required | 不做税务/报销合规结论 |
| 付款条款风险提示 | 合同含预付款和逾期罚则 | risk_flags、source_notes | 不给法律建议；只做业务复核提示 |

结论：仅组件。原因：文档解析价值明确，但需要组合到合同/票据具体 Skill，且不能独立输出法律、审计或税务结论。

## 9. 封装队列

已生成 `queues/DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_01.md`，包含 4 个 `L2 通过可封装` 候选：

1. `quality_sprint01_google_sheets_mcp_report_agent_candidate`
2. `quality_sprint01_notion_ops_knowledge_agent_candidate`
3. `quality_sprint01_slack_support_triage_agent_candidate`
4. `quality_sprint01_hubspot_crm_followup_agent_candidate`

## 10. 权限边界确认

- 未安装依赖。
- 未访问外网。
- 未访问真实账号。
- 未调用真实 API/provider。
- 未写 key，未读取或打印 key。
- 未读取客户文件。
- 未发送邮件、短信、微信、Slack 或平台消息。
- 未写 Sheets、Notion、Slack、HubSpot、CRM 或其他业务系统。
- 未抓取真实网页。
- 未上传素材。
- 未生成真实图片、视频、音频、OCR 或 PDF。
- 未改稳交付库；客户正式可调用 Skill 仍为 13。
