# 封装窗口任务：第一阶段候选卡落盘

## 输入

等待测试台输出 `DEEPAGENTS_SMOKE_TO_50_RESULT.md`。

## 任务

对 smoke 通过或明确可组件化的候选生成候选卡：

- `CANDIDATE.md`
- `candidate.yaml`

落盘目录按状态选择：

- `candidates/mock_callable/`
- `candidates/dry_run_callable/`
- `candidates/deepagents_smoke_passed/`
- `candidates/component_only/`

每张候选卡必须包含：

- 业务包、角色、场景
- 来源与许可证/trial mode 结论
- 输入/输出字段
- DeepAgents smoke 用例
- 权限边界
- 禁止动作
- 人工复核触发
- 是否计入 100 个可试跑候选

## 禁止

- 不修改 13 个稳交付 Skill 原包。
- 不把组件项封成独立 L3。
- 不把 smoke 通过写成正式 L2 通过。
