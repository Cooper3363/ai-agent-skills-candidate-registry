# 许可证窗口任务：第一阶段 43 个候选轻量 L1 / Trial Mode

## 输入

等待研究窗口输出 `RESEARCH_TO_50_RESULT.md`。

## 任务

对研究窗口推荐的 43 个候选做轻量复核，输出是否可进入 DeepAgents smoke。

每个候选必须给出：

- 许可证 / 商用限制
- 维护状态
- 依赖、API、模型、数据条款风险
- 是否为聚合仓库；如是，是否定位到具体子 skill 或真实上游
- trial mode：`mock_only` / `dry_run_only` / `read_only` / `BYOK_required` / `external_action_blocked`
- L1/trial 结论：`can_mock_smoke` / `can_dry_run_smoke` / `component_only` / `needs_more_license_info` / `blocked`

## 默认边界

- 邮件、CRM/OAuth、日历、任务、财务、合同、薪酬、网页抓取、图片/视频生成：默认只能 dry-run。
- 许可证不清、商用条款不清、真实上游不清：不计入 100。
- 只使用内部模板且不复用第三方代码的候选，可标为 internal_template 并进入 mock smoke。

## 输出文件

- `LICENSE_REVIEW_TO_50_RESULT.md`
- 可送 smoke 候选表
- 需补资料候选表
- blocked 候选表
