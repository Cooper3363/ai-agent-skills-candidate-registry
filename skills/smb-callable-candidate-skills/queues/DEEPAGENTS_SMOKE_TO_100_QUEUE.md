# 测试台任务：第二阶段 50 个候选 DeepAgents Candidate Smoke

## 输入

- `RESEARCH_TO_100_RESULT.md`
- `LICENSE_REVIEW_TO_100_RESULT.md`

## 任务

对许可证窗口第二阶段 L1 / trial mode 放行的 50 个候选执行 DeepAgents candidate smoke。

本轮目标是判断这些候选是否可进入候选库继续试跑，不是正式 L2，不决定封装，不改变客户可调用状态。

## 当前 L1 / Trial Mode 数量

- `can_mock_smoke`: 41
- `can_dry_run_smoke`: 9
- `component_only`: 0
- `needs_more_license_info`: 0
- `blocked`: 0

## Smoke 要求

每个候选至少覆盖 1 个中文 mock / dry-run 用例，并检查：

- Candidate ID 是否稳定
- 业务包、角色、场景是否清楚
- trial mode 是否明确
- 输入 / 输出字段是否可表达为候选调用
- 禁止动作是否明确
- 人工复核触发是否合理
- 是否与当前 13 个稳交付 Skill 或 To50 候选重复
- 是否只能作为组件

## dry-run 硬断言

9 个 `can_dry_run_smoke` 候选必须断言：

- `external_action_blocked=true`
- `send_allowed=false`
- `write_allowed=false`

## 禁止动作

- 不安装依赖
- 不访问真实账号
- 不读取真实客户文件
- 不调用真实业务 API
- 不发送邮件、短信或微信
- 不写 CRM、日历、任务或业务系统
- 不真实抓取网页
- 不上传文件
- 不退款、不赔偿、不改库存
- 不生成真实图片、视频、音频、OCR 或 PDF 结果
- 不改稳交付 13 个包

## 输出文件

- `DEEPAGENTS_SMOKE_TO_100_RESULT.md`
- `queues/L2_OFFICIAL_TOP15_FROM_TO100_QUEUE.md`

## Smoke 结论枚举

- `passed`
- `failed`
- `needs_fix`
- `blocked`

## Top 15 队列要求

从 smoke passed 候选中筛选最适合进入正式 L2 simulated 的 Top 15，并写入 `queues/L2_OFFICIAL_TOP15_FROM_TO100_QUEUE.md`。

正式 L2 队列只排优先候选，不代表 L2 通过，不代表可封装，不代表客户可调用。
