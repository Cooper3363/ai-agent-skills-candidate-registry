# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_01

生成日期：2026-06-05

来源：`../L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_RESULT.md`

本队列性质：Quality Sprint 01 正式 L2 simulated 后，进入 draft L3 封装窗口的候选队列。  
重要边界：进入 draft L3 不代表客户正式可调用，不代表稳交付库扩容；封装后仍需平台调用验收和必要真实 Harness smoke。

## 1. 数量汇总

| 状态 | 数量 |
| --- | ---: |
| L2 通过可封装 | 4 |
| 仅组件，不进入本队列 | 6 |

## 2. Draft L3 封装候选

| 排名 | candidate_id | 建议 draft Skill ID | 业务包 | 封装定位 | 必须保留的权限边界 | 平台调用验收重点 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint01_google_sheets_mcp_report_agent_candidate` | `sheets_metrics_report_dryrun_agent` | 经营报表分析包 | mock/read-only rows 到经营摘要、异常字段、source rows | 不连接真实 Google Sheets；不写表；上线前真实 Harness 仅允许 read-only scope | schema 稳定、source_rows 可追溯、异常不编造、字段缺失能回退 |
| 2 | `quality_sprint01_notion_ops_knowledge_agent_candidate` | `notion_kb_gap_review_dryrun_agent` | 客服知识库助手包 | mock/read-only pages 到 FAQ 缺口、过期条款、冲突提示 | 不连接真实 Notion；不写页面；上线前真实 Harness 仅允许授权 read-only page scope | source_notes 稳定、政策冲突触发人工复核、不自动发布 |
| 3 | `quality_sprint01_slack_support_triage_agent_candidate` | `slack_support_triage_dryrun_agent` | 客服知识库助手包 | mock channel messages 到交接摘要、风险标签、dry-run payload | `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`；不连 Slack，不发消息 | 投诉/退款/账号安全/PII 风险触发准确，dry-run payload 不可执行 |
| 4 | `quality_sprint01_hubspot_crm_followup_agent_candidate` | `hubspot_crm_followup_dryrun_agent` | 销售跟进助手包 | mock deal/notes 到线索摘要、下一步动作、CRM dry-run payload | `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`；不连 HubSpot，不写 CRM | 下一步动作有依据，折扣/合同/PII 触发人工复核，payload 明确 dry-run |

## 3. 不进入本封装队列的组件项

| candidate_id | L2 结论 | 推荐去向 | 原因 |
| --- | --- | --- | --- |
| `quality_sprint01_openai_agents_customer_ops_workflow_candidate` | 仅组件 | Agent workflow 编排组件池 | 通用编排底座，不是单一业务 callable Skill |
| `quality_sprint01_langgraph_sales_pipeline_workflow_candidate` | 仅组件 | 销售 pipeline 状态机组件池 | 更适合作为销售流程 Skill 的内部状态机 |
| `quality_sprint01_microsoft_presidio_hr_pii_candidate` | 仅组件 | PII 脱敏组件池 | 与既有 PII 能力邻近，HR 中文规则需继续增强 |
| `quality_sprint01_llamaindex_kb_refresh_agent_candidate` | 仅组件 | KB refresh 组件池 | 适合作为 FAQ/KB 能力内部组件 |
| `quality_sprint01_pydantic_ai_structured_tool_candidate` | 仅组件 | 结构化输出组件池 | schema/校验底座，不是独立业务 Skill |
| `quality_sprint01_unstructured_contract_invoice_agent_candidate` | 仅组件 | 文档解析组件池 | 需组合到合同/票据具体业务 Skill，不能输出法律/审计/税务结论 |

## 4. 封装窗口固定要求

- 不得把本轮 simulated L2 写成真实 API/provider 通过。
- SaaS/OAuth/API/MCP 类候选必须默认 `dry_run=true`。
- 所有 dry-run payload 必须包含 `send_allowed=false`、`write_allowed=false`、`external_action_blocked=true`。
- 不得写入 Sheets、Notion、Slack、HubSpot、CRM 或其他业务系统。
- 不得发送消息、邮件、短信或平台通知。
- 不得读取客户真实文件或连接真实账号。
- 不得把候选封装后直接加入稳交付库；稳交付库仍为 13，需平台调用验收后再由指挥中心决策。

## 5. 建议平台验收 smoke

| draft Skill ID | 最小中文 smoke 输入 | 预期输出字段 | 失败判定 |
| --- | --- | --- | --- |
| `sheets_metrics_report_dryrun_agent` | 7 行门店销售 mock rows | `summary`, `metric_changes`, `anomalies`, `source_rows`, `manual_review_required` | 编造数据、无 source_rows、异常无解释 |
| `notion_kb_gap_review_dryrun_agent` | 3 段售后政策 mock pages | `page_summary`, `faq_gaps`, `stale_items`, `conflicts`, `source_notes` | 自动裁决政策、无来源、写 Notion |
| `slack_support_triage_dryrun_agent` | 5 条投诉/账号安全 mock channel messages | `handoff_summary`, `risk_tags`, `priority`, `dry_run_payload`, `send_allowed=false` | 自动发送、风险漏判、缺 dry-run 字段 |
| `hubspot_crm_followup_dryrun_agent` | mock deal + 3 条跟进备注 | `lead_summary`, `next_action`, `risk_flags`, `crm_payload`, `write_allowed=false` | 自动写 CRM、自动发邮件、折扣承诺 |
