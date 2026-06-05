# Platform Acceptance To150 Native Skills Precheck

回传时间: 2026-06-03
回传窗口: AI.Skills 平台调用验收窗口
任务: To150 新增 50 个 Agent Skill 来源候选的等待/边界预审
验收口径: 仅做平台验收门槛预审，不做候选调用 accepted，不做稳交付扩容

## 已完成事项

- 已读取 `queues/PLATFORM_ACCEPTANCE_TO_150_NATIVE_SKILLS_QUEUE.md`。
- 已读取 `STATUS_SUMMARY.md`。
- 已确认 To150 新增 50 个候选当前状态均为 `needs_license_review`。
- 已确认队列状态为 `not_ready`，原因是尚未完成许可证窗口 L1/source verification，也尚未完成 DeepAgents candidate smoke。
- 已检查平台验收门槛表述：候选 smoke 通过只代表内部/受控试跑；draft L3 验收也不等于稳交付扩容；稳交付扩容仍需另走正式平台验收。
- 已确认本轮不应给任何 To150 候选 `candidate_trial_accepted`。

## 当前状态摘要

| 项目 | 数量/状态 |
| --- | --- |
| 稳交付库客户正式可调用 Skill | 13 |
| 当前总候选卡 | 150 |
| To150 新增候选 | 50 |
| To150 native_agent_skill | 45 |
| To150 agent_skill_compatible | 5 |
| To150 当前状态 | needs_license_review |
| L1/source verification | 未完成 |
| DeepAgents candidate smoke | 未完成 |
| 平台候选调用复核 | not_ready |
| 本轮新增客户正式可调用 Skill | 0 |

## 平台验收门槛检查

| 门槛项 | 预审结论 |
| --- | --- |
| candidate smoke passed 的含义是否写清 | 已写清，仅代表候选内部/受控试跑底座检查，不代表客户正式可调用。 |
| draft L3 验收是否等于稳交付扩容 | 已写清，不等于稳交付扩容。 |
| 稳交付扩容是否需另行正式验收 | 已写清，仍需另走平台正式验收。 |
| needs_license_review 候选是否被 accepted | 未发现，本轮不得 accepted。 |
| To150 是否写入稳交付库 | 未发现，本轮不得写入。 |
| 客户正式可调用 Skill 数量 | 仍为 13。 |

## 当前问题

- To150 50 个新增候选仍处于 `needs_license_review`，尚未完成 L1/source verification。
- DeepAgents smoke 队列状态为 `pending_l1`，尚未输出 `DEEPAGENTS_SMOKE_TO_150_NATIVE_SKILLS_RESULT.md`。
- 因缺少 L1 放行与 smoke 结果，平台验收窗口当前不能做候选调用边界复核，也不能给 accepted。

## 阻塞原因

- 前置材料未完成：L1/source verification 未完成。
- 前置测试未完成：DeepAgents candidate smoke 未完成。
- 按候选调用验收规则，未通过 L1 与 smoke 的 To150 候选不能进入平台候选调用 accepted 判断。

## 需要 AI.Skills 指挥中心决策的问题

无新增决策点。当前属于流程前置未完成，不需要改变验收口径。

## 建议下一步

- 等许可证窗口完成 To150 L1/source verification 后，再由测试台执行 DeepAgents candidate smoke。
- 等测试台落盘 `DEEPAGENTS_SMOKE_TO_150_NATIVE_SKILLS_RESULT.md` 后，再由平台验收窗口执行 To150 候选调用边界复核。
- 后续复核仍只对 L1 放行且 smoke passed 的 mock/dry-run 候选做内部/受控试跑判断，不得写成客户正式可调用。
- 继续保持稳交付库客户正式可调用 Skill 数量为 13。

## 预审结论

To150 平台候选调用验收当前处于等待状态。不得给 accepted，不得写入稳交付库，不新增客户正式可调用 Skill。
