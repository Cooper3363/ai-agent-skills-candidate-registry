# 许可证窗口任务：第二阶段 50 个候选轻量 L1 / Trial Mode

## 输入

- `RESEARCH_TO_100_RESULT.md`
- 读取第 7 节“推荐进入许可证 / trial mode 复核的 50 个候选”

## 任务

对研究窗口第二阶段推荐的 50 个候选做轻量 L1 / trial mode 复核，判断哪些可进入 DeepAgents candidate smoke，哪些只能作为组件、需补资料或 blocked。

每个候选必须输出：

- 许可证 / 来源授权口径
- 商用限制
- 维护状态
- 依赖、API、模型、数据条款风险
- 是否为内部模板、组合能力、聚合仓库或真实上游项目
- trial mode：`mock_only` / `dry_run_only` / `read_only` / `BYOK_required` / `external_action_blocked`
- L1/trial 结论：`can_mock_smoke` / `can_dry_run_smoke` / `component_only` / `needs_more_license_info` / `blocked`

## 默认边界

- 邮件、短信、微信、CRM/OAuth、日历、任务、财务、合同、薪酬、网页抓取、图片/视频/音频/OCR/PDF 生成，默认只能 mock 或 dry-run。
- 许可证不清、商用条款不清、真实上游不清、聚合仓库无法定位具体子资源的候选，不计入 100 个可试跑候选。
- 只使用内部模板且不复用第三方代码的候选，可标为 `internal_template` 并进入 `can_mock_smoke`。
- 外部动作类候选若放行，必须带 `external_action_blocked=true`；dry-run 候选还必须带 `send_allowed=false`、`write_allowed=false`。

## 输出文件

- `LICENSE_REVIEW_TO_100_RESULT.md`
- 可送 smoke 候选表
- component_only 候选表
- 需补资料候选表
- blocked 候选表

## 不变边界

本轮只做候选库第二阶段 L1 / trial mode 复核，不送 L2、不封装、不客户调用、不改稳交付 13 个 Skill。
