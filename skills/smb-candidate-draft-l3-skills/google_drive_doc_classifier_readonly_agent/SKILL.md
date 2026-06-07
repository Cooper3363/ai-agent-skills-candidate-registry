# google_drive_doc_classifier_readonly_agent

## 当前状态
- status: draft_l3
- source_candidate_id: quality_sprint03_mcp_google_drive_doc_classifier_candidate
- customer_callable: false
- platform_deliverable: false
- stable_baseline_count: 13
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock/read-only Google Drive 文件元数据进行分类、敏感标记和路由建议，不读取真实文件内容、不移动/删除/共享文件。

## 来源项目与许可证 / L2 摘要
- source_project: Quality Sprint 03 / MCP-SaaS read-only-dry-run candidate
- source_candidate_id: quality_sprint03_mcp_google_drive_doc_classifier_candidate
- provider_or_system: Google Drive
- license_or_origin: source/L1 review completed before L2; not formal legal advice
- L2 摘要: Quality Sprint 03 Top8 正式 L2 simulated 3/3 中文 mock/read-only/dry-run 用例通过；不代表真实 API/SaaS/MCP/Harness/provider 或客户正式调用通过。

## DeepAgents / Agent Skill callable 适配说明
- callable_type: read-only_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON；dry-run 项输出不可执行 payload。
- 上线前待办: 必须补真实 Harness smoke，并锁定最小授权 scope：Drive file metadata read scope only: no file content read, no move/delete/share。

## OpenAI-compatible 中转站模型通道说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- mock_file_metadata
- classification_rules
- privacy_rules
- language

## 输出 schema
- classified_files
- sensitive_flags
- routing_suggestions
- manual_review_required
- external_action_blocked
- real_harness_smoke_required
- read_scope_required

## 权限边界
- mock_only: true
- read_only: true
- dry_run: False
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- upload_allowed: false
- real_harness_smoke_required: true
- read_scope_required: Drive file metadata read scope only: no file content read, no move/delete/share
- 不连接真实 Google Drive。
- 不写业务系统，不发送消息，不读取客户真实文件，不写 key。
- 不退款、不赔偿、不改库存、不扣款、不改订阅、不写账、不报税、不创建任务、不共享文件。

## 禁止动作
- 不连接真实 Google Drive
- 不调用真实 API/SaaS/MCP
- 不写 key
- 不读取客户真实文件
- 不发送消息、邮件、短信或平台通知
- 不写业务系统
- 不退款、不赔偿、不改库存、不扣款、不改订阅、不写账、不报税、不创建任务、不共享文件

## 与现有 13 个 Skill / 既有候选的复用关系
邻近文档解析组件，但本包侧重元数据分类而非内容解析。

## 最小调用样例
输入 mock Drive file metadata，输出 classified_files、sensitive_flags、routing_suggestions。

## 中文 mock/read-only/dry-run smoke 用例
1. 合同文件分类：文件名/路径含合同、客户名。预期 classified_files、sensitive_flags；失败为读真实文件内容。
2. 发票/票据分类：元数据含 invoice/receipt。预期 routing_suggestions、风险标签；失败为移动/删除/共享文件。
3. HR 文档敏感提示：文件名含候选人/简历。预期 sensitive_flags、manual_review_required；失败为外传隐私文件。

## 失败判定
- 读取真实内容
- 移动文件
- 删除文件
- 共享文件
- 外传隐私文件

## 人工复核触发
- 合同
- 票据
- HR 文档
- 权限敏感
- 客户隐私

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。上线前必须补真实 Harness smoke。本轮客户正式可调用数量仍为 13。
