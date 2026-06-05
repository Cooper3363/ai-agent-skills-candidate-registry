# 双库入库与晋级规则

## 基本判断

候选优先级不由来源决定，而由中小微企业业务价值决定。OpenClaw、Hermes、MCP、GitHub 或其他来源都必须先回答三个问题：

1. 是否解决中小微企业高频工作。
2. 是否能用清晰输入输出表达成 callable Skill 或组件。
3. 是否能在权限、许可证和人工复核边界内试跑。

## 2026-06-05 新口径：底座适配优先

候选库不再只收标准 `SKILL.md / skill.yaml`。只要满足以下三点，就可以进入候选库的研究、许可证复核或 smoke 队列：

1. 能适配本平台底座或 DeepAgents 本地 runner。
2. 能通过 OpenAI-compatible 中转站模型通道调用，或只依赖本地 prompt/role/schema 包装。
3. 能服务六部门中小微场景：创意设计、运营、销售、电商、客服、管理。

允许进入候选库的能力单元包括：

- 标准 Agent Skill：已有 `SKILL.md`、`skill.yaml` 或接近该结构。
- 兼容型 Skill：目录结构、说明文档、schema 接近 Agent Skill，可迁移。
- Agent 角色库：Markdown 角色、岗位提示词、部门角色包，可做 role smoke。
- 工作流/工具包装：需要外部 API、浏览器、Figma、媒体生成、PPT/文件导出的工具流，只能先进入 `dry_run_only` 或 `needs_license_review`。
- 内部模板：没有可靠上游，但能稳定服务中小微高频场景的 mock/read-only 模板。

模型中转站只解决“模型调用口”问题，不自动放行业务外部动作。凡涉及真实发送、写入、上传、抓取、出图、出视频、广告投放、库存修改、退款、CRM/OAuth、日历/任务写入，都必须单独标注权限边界，并默认 `external_action_blocked=true`。

## 进入候选调用库

满足以下任一条件可进入候选调用库：

- 已有明确中小微业务场景，但许可证待复核。
- 可用 mock 输入做 smoke test。
- 可生成 dry-run payload，但不能真实发送或写入。
- 只能作为组合流程组件，但业务价值明确。
- 已通过正式 L2 simulated，但尚未平台验收。
- 可作为 DeepAgents / OpenClaw / Hermes / MCP / Codex 等底座的可适配 Agent、Role 或 Skill 候选。

进入候选调用库必须写清：

- `candidate_id`
- 业务包与适配角色
- 来源项目或来源文档
- 当前状态
- 调用模式
- 权限边界
- 风险标签
- 是否客户可调用
- 下一步动作

## 进入稳交付库

候选晋级稳交付库必须全部满足：

- L1：许可证、商用限制、依赖/API/模型条款可核验。
- L2：至少 3 个中文业务用例通过，输出结构稳定。
- L3：完成 `SKILL.md`、`skill.yaml`、输入输出、权限边界、测试用例、平台交接备注。
- 平台调用验收：Skill ID、intent、adapter target、schema、失败模式、人工复核触发、最小调用样例通过。

稳交付库可以比早期口径适当宽松：标准来源不必只限已内置的 13 个 Skill，也可以来自已完成迁移的 Agent、Role 或工作流包装。但“可客户调用”仍必须有明确运行边界、最小调用样例、失败模式和人工复核触发；不能仅凭来源项目知名度或 smoke passed 晋级。

## 默认暂缓或降级

以下场景不得直接进入客户正式调用：

- 许可证或商用条款不清。
- 需要真实 OAuth、CRM、邮箱、短信、日历或任务写入。
- 需要真实网页抓取、代理、登录、绕过 robots/ToS。
- 需要真实财务、合同、薪酬、法律或税务判断。
- 需要真实图片、视频、音频、OCR、PDF 处理但 Harness 未通过。
- 无法稳定输出结构化 schema。

这些候选可以留在候选库，但必须标为 `market_lead`、`needs_license_review`、`mock_callable`、`dry_run_callable` 或 `component_only`。
