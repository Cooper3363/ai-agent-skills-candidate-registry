# 封装窗口任务：第二阶段 To100 候选卡落盘

## 输入

请读取：

- `DEEPAGENTS_SMOKE_TO_100_RESULT.md`
- `LICENSE_REVIEW_TO_100_RESULT.md`
- `queues/L2_OFFICIAL_TOP15_FROM_TO100_QUEUE.md`

## 任务

对第二阶段 50 个 DeepAgents candidate smoke passed 候选生成候选卡：

- `CANDIDATE.md`
- `candidate.yaml`

落盘目录按 trial mode 和候选定位选择：

- `candidates/mock_callable/`
- `candidates/dry_run_callable/`
- `candidates/deepagents_smoke_passed/`
- `candidates/component_only/`

本轮是候选卡封装，不是 L3 封装。即使候选进入 Top15 正式 L2 队列，也只能在候选卡中记录 `formal_l2_status: pending_or_queued`，不得写成 L2 通过。

## 每张候选卡必须包含

- candidate_id
- 业务包
- 角色
- 使用场景
- 来源与许可证/trial mode 结论
- `deepagents_trial_fit`
- DeepAgents smoke status
- 中文 smoke 用例
- 输入字段
- 输出字段
- 权限边界
- 禁止动作
- 人工复核触发
- 与稳交付 13 个 Skill 或 To50 候选的复用/重复关系
- 是否计入候选池目标对象
- 下一步动作

## dry-run 硬边界

对所有 dry-run 候选必须写入：

- `external_action_blocked: true`
- `send_allowed: false`
- `write_allowed: false`

并明确禁止：

- 发送邮件、短信、微信或私信
- 写 CRM、日历、任务、工单或业务系统
- 调用真实业务 API 或 OAuth
- 上传文件
- 退款、赔偿或改库存
- 真实抓取网页
- 生成真实图片、视频、音频、OCR 或 PDF 结果

## 输出

请落盘：

- `PACKAGING_TO_100_RESULT.md`
- 50 个候选目录及其 `CANDIDATE.md` / `candidate.yaml`

输出结果需要包含：

- 落盘总数
- mock_callable 数量
- dry_run_callable 数量
- component_only 数量
- deepagents_smoke_passed 数量
- Top15 候选是否只标记为 `formal_l2_status: pending_or_queued`
- 稳交付库客户正式可调用数量仍为 13

## 禁止

- 不修改 13 个稳交付 Skill 原包。
- 不生成 `SKILL.md` 或 `skill.yaml`。
- 不把 smoke 通过写成正式 L2 通过。
- 不把候选卡落盘写成平台验收通过。
- 不新增客户正式可调用 Skill。
