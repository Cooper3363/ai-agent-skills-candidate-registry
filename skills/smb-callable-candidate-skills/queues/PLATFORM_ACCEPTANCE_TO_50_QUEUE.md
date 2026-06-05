# 平台验收窗口任务：第一阶段候选调用边界复核

## 输入

等待封装窗口完成候选卡落盘，并等待测试台 smoke 结果。

## 任务

复核第一阶段候选调用边界：

- Skill/Candidate ID 是否稳定
- 业务包和角色是否清楚
- trial mode 是否明确
- 输入/输出字段是否可调用
- 禁止动作是否明确
- 人工复核触发是否合理
- DeepAgents smoke 是否真实完成

## 验收结论

每个候选只允许输出：

- `candidate_trial_accepted`
- `candidate_trial_needs_fix`
- `component_only`
- `blocked`

## 不变边界

- 候选调用验收通过不进入稳交付库。
- 稳交付库仍为 13 个客户正式可调用 Skill。
- 稳交付扩容必须另走正式平台验收。
