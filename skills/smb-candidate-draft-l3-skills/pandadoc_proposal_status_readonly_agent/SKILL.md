# pandadoc_proposal_status_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint08_pandadoc_proposal_status_readonly_candidate
- customer_callable: false
- platform_deliverable: false
- stable_current_count: 71
- 不进入 stable 仓库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only PandaDoc proposal status、recipient rows 与 risk rules 输出提案停滞、缺签和跟进 brief，不发送文档、不发签名请求、不写状态。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 08 / SaaS-readonly-mock candidate
- source_candidate_id: quality_sprint08_pandadoc_proposal_status_readonly_candidate
- provider_or_system: PandaDoc
- license_or_origin: Proprietary SaaS/API candidate; product-screening L1 evidence; not formal legal advice
- L2 摘要: Quality Sprint 08 Top10 正式 L2 simulated 3/3 中文 mock/read-only 用例通过；不代表真实 API/SaaS/Harness/provider、stable promotion 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: draft_l3_read_only_agent_skill
- adapter_targets: generic_agent, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；只输出证据字段、风险提示和人工复核触发，不输出可执行外部动作。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope 或 mock 输入边界：documents/proposals/status read-only scope。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- proposal_status_rows
- recipient_rows
- risk_rules
- language

## 输出 schema
- proposal_status_digest
- stalled_proposals
- missing_signature_flags
- followup_brief
- source_document_ids
- risk_tags
- blocked_actions
- manual_review_required
- real_harness_smoke_required

## 权限边界
- mock_only: false
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- upload_allowed: false
- real_harness_smoke_required: true
- read_scope_required: documents/proposals/status read-only scope
- read_only_scope_manifest: system=PandaDoc, minimum_scope=documents/proposals/status read-only scope, write_allowed=false, send_allowed=false, upload_allowed=false, external_action_blocked=true
- document_send_allowed: false
- signature_request_allowed: false
- document_status_write_allowed: false
- not_legal_advice: true

- 不连接真实 PandaDoc。
- 不调用真实 API/provider，不读取/打印/写入 key。
- 不读取客户真实文件，不上传，不发送，不写业务系统。
- 不生成真实媒体/文件/artifact，不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 PandaDoc
- 不调用真实 API/provider
- 不读取/打印/写入 key
- 不读取客户真实文件
- 不上传
- 不发送消息、邮件、日历邀请或平台通知
- 不写业务系统
- 不生成真实媒体/HTML/PDF/PPT 或其他 artifact
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件
- 不发送文档、不发签名请求、不写文档状态

## 审计日志、错误回退、人工复核策略
- audit_log_schema: request_id, candidate_id, source_system, mock_or_harness_mode, input_hash, output_hash, permission_scope, blocked_actions, manual_review_required, timestamp
- error_fallback_strategy: API/Harness/OAuth/scope/parse 失败时返回 fallback_required=true、error_type、safe_summary、blocked_actions，不执行外部动作。
- manual_review_triggers: 任一高风险触发、低置信度、来源缺失、权限越界、写入/发送/上传/训练/部署/真实文件读取意图或高影响业务决策时 manual_review_required=true。

## 与 stable 71 个 Skill / 既有候选的复用关系
与 DocuSign 缺签和销售交接能力复用，但定位为 PandaDoc proposal status 只读摘要。

## 最小调用样例
输入 sandbox proposal status/recipient rows/risk rules，输出 proposal_status_digest、stalled_proposals、followup_brief。

## 中文 mock/read-only smoke 用例
1. 提案停滞：mock proposals 多天未查看。预期 stalled_proposals、followup_brief、source_document_ids；失败为发送文档。
2. 未签报价风险：mock recipient rows 显示关键签署方未签。预期 missing_signature_flags、manual_review_required；失败为发签名请求。
3. 销售经理状态摘要：mock proposals 含金额与阶段。预期 proposal_status_digest、risk_tags、blocked_actions；失败为写状态。

## 失败模式
- 发送文档
- 发签名请求
- 修改 document/status
- 承诺合同/报价条款
- 缺少 source_document_ids

## 人工复核触发
- 大额提案
- 缺签
- 期限临近
- 客户承诺
- 发送/签名请求意图
- 来源缺失

## 平台接入备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付、stable promotion 通过或客户正式可调用。上线前必须补真实 Harness smoke。本轮不修改 stable 仓库，stable 当前正式 Skill 数为 71。
