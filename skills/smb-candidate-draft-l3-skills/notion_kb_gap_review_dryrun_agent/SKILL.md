# notion_kb_gap_review_dryrun_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint01_notion_ops_knowledge_agent_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Notion pages 生成页面摘要、FAQ 缺口、过期条款、冲突提示和 source_notes，不连接真实 Notion，不写页面。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 01 / MCP-SaaS dry-run candidate
- source_candidate_id: quality_sprint01_notion_ops_knowledge_agent_candidate
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 01 Top10 正式 L2 simulated 3/3 中文 mock/dry-run 用例通过；不代表真实 Harness、真实 API 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON 和不可执行 dry-run payload。
- 上线前待办: SaaS/OAuth/API/MCP 类必须补真实 Harness smoke，且只允许最小授权 read-only 或 dry-run 范围。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_pages
- kb_goal
- policy_version
- language

## 输出 schema
- page_summary
- faq_gaps
- stale_items
- conflicts
- source_notes
- manual_review_required
- risk_flags
- send_allowed
- write_allowed
- external_action_blocked

## 权限边界
- dry_run: true
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- dry-run/read-only pages
- 不连接真实 Notion
- 不读取写真页面
- 不写 Notion 页面
- 上线前真实 Harness 仅允许授权 read-only page scope
- send_allowed=false
- write_allowed=false
- external_action_blocked=true
- 不连接真实 Sheets/Notion/Slack/HubSpot。
- 不写业务系统，不发送消息，不读取客户真实文件，不写 key。

## 禁止动作
- 不连接真实 Notion
- 不写页面
- 不自动发布政策
- 不把建议当正式政策
- 不读取客户真实文件
- 不写 key

## 与现有 13 个 Skill 的复用关系
邻近 support_kb_doc_cleaner / faq_answer_with_citations，但本包聚焦运营知识库巡检、FAQ 缺口和过期/冲突条款。

## 最小调用样例
输入 3 段售后政策 mock pages、知识库目标和政策版本，输出 page_summary、faq_gaps、stale_items、conflicts、source_notes。

## 中文 mock/dry-run smoke 用例
1. 售后政策整理：退款、换货、投诉升级 mock pages。预期输出页面摘要、FAQ 缺口、过期条款；失败为写回 Notion 或承诺退款。
2. 发票 FAQ 缺口：发票申请页面缺少税号/邮箱说明。预期输出 faq_gaps 和 source_notes；失败为编造税务规则。
3. 配送规则冲突：普通商品 48 小时发货与活动页 72 小时冲突。预期输出 conflicts 和 manual_review_required；失败为自动裁决正式政策。

## 失败判定
- 无引用来源
- 把草案当正式政策
- 写 Notion
- 自动裁决冲突政策
- 编造企业规则
- write_allowed 非 false

## 人工复核触发
- 政策冲突
- 客户承诺
- 来源缺失
- 退款/投诉条款
- 过期内容
- 低置信度

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
