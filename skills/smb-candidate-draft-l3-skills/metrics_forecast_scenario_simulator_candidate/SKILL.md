# metrics_forecast_scenario_simulator_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于基线指标和假设生成多情景模拟、敏感性说明和数据质量提示，仅供经营讨论，不构成财务、投资或税务建议。

## 来源项目与许可证 / L2 摘要
- source_project: Next50 internal candidate / DeepAgents simulated L2
- license_or_origin: internal candidate packaging, license/source review completed before L2; not formal legal advice
- L2 摘要: Next50 Top15 正式 L2 simulated 3/3 中文业务用例通过；不代表真实 Harness 或客户正式调用通过。

## DeepAgents / 通用 Agent Skill 适配说明
- callable_type: text_or_dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON，不依赖真实外部 provider/API。

## 中转站模型通道配置说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- baseline_metrics
- assumptions
- scenario_count
- time_window
- language

## 输出 schema
- scenarios
- assumptions
- sensitivity_notes
- data_quality_notes
- not_financial_advice
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 只做情景模拟
- 非财务/投资/税务建议
- 不写财务系统
- 不做融资或经营决策
- 不调用真实 BI/API
- 不调用真实 provider/API。
- 不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 与现有 13 个 Skill 的复用关系
与 daily_weekly_metrics_reporter / structured_metric_summary 相邻，但本 Skill 聚焦多情景假设模拟，不生成完整日报周报。

## 最小调用样例
输入门店客流下降 15%、客单价和成本假设，输出 3 种 scenarios、assumptions 和 not_financial_advice=true。

## 3 个中文测试用例
1. 客流下降：门店客流下降 15%。预期输出三种情景和假设说明，not_financial_advice=true；失败为直接给投资建议。
2. 客单价上升：客单价提升但复购下降。预期输出敏感性分析和口径提示；失败为隐瞒数据缺失。
3. 成本上涨：成本涨 10%。预期输出毛利压力情景，不给税务/融资建议；失败为写成财务建议。

## 失败判定 / 失败模式
- 直接给投资/融资/税务建议
- 隐瞒假设
- 无数据质量提示
- 修改财务数据
- 输出确定性预测

## 人工复核触发
- 数据缺失
- 重大经营决策
- 财务敏感
- 口径不清
- 成本或收入异常
- 低置信度

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。本轮不改变客户正式可调用 13 的状态。
