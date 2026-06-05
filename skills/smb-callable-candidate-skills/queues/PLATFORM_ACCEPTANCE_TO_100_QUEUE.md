# 平台验收窗口任务：To100 候选调用边界复核

## 输入

请读取：

- `PACKAGING_TO_100_RESULT.md`
- `DEEPAGENTS_SMOKE_TO_100_RESULT.md`
- `LICENSE_REVIEW_TO_100_RESULT.md`
- `L2_OFFICIAL_TOP15_FROM_TO100_RESULT.md`
- `COMPONENT_POOL_TO100_ADDITIONS.md`
- `candidates/mock_callable/`
- `candidates/dry_run_callable/`
- `candidates/component_only/`
- `candidates/draft_l3/`

## 任务

对 To100 第二阶段新增的 50 张候选卡做候选调用边界复核。

本轮只验收候选卡是否适合内部/受控试跑，不验收稳交付客户调用，不把任何候选迁入稳交付库。

## 必查项

- 50 张 To100 候选卡是否均存在 `CANDIDATE.md` 与 `candidate.yaml`。
- Top15 候选是否只标记 `formal_l2_status: pending_or_queued`，没有误写成 L2 通过。
- 所有候选是否保留 `customer_callable=false` 与 `platform_deliverable=false`。
- 9 个 dry-run 候选是否全部保留：
  - `external_action_blocked=true`
  - `send_allowed=false`
  - `write_allowed=false`
- 是否没有为 To100 候选卡生成 `SKILL.md` / `skill.yaml`。
- 是否没有修改稳交付 13 个 Skill。
- `support_ticket_batch_summary_candidate` 与 `brand_forbidden_words_checker_candidate` 是否只作为组件池对象，不进入独立 L3。

## 验收结论枚举

- `candidate_trial_accepted`
- `candidate_trial_needs_fix`
- `component_only`
- `blocked`

## 输出

请落盘：

- `PLATFORM_ACCEPTANCE_TO_100_RESULT.md`

输出需要包含：

- 50 张候选卡复核数量。
- accepted / needs_fix / component_only / blocked 数量。
- dry-run 硬断言检查结果。
- Top15 pending 标记检查结果。
- 是否发现误生成 L3 文件。
- 是否发现客户正式可调用或平台可交付字段误置 true。
- 明确说明稳交付库客户正式可调用数量仍为 13。

## 禁止

- 不验收 To100 13 个 draft L3，因为它们还未由封装窗口落盘。
- 不把 DeepAgents smoke passed 或候选卡验收通过写成正式 L2 通过。
- 不把候选调用验收通过写成客户正式可调用。
- 不修改 13 个稳交付 Skill 原包。
