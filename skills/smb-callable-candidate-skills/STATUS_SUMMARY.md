# 候选调用库状态汇总

更新日期: 2026-06-05

## 当前结论

- 稳交付库客户正式可调用数量: 13。
- To50 与 To100 已完成，累计 100 张候选卡。
- To150 已新增 50 张 Agent Skill 来源候选卡，统一待 L1/source verification。
- agency-agents-zh 已新增 1 张角色库源候选卡。
- 当前总候选卡: 167。
- 本轮新增客户正式可调用 Skill: 0。

## 状态数量

| 状态 | 数量 |
| --- | ---: |
| draft_l3 | 4 |
| mock_callable | 73 |
| dry_run_callable | 17 |
| component_only | 6 |
| needs_license_review | 67 |
| total_candidate_cards | 167 |
| To150 native_agent_skill | 45 |
| To150 agent_skill_compatible | 5 |
| agency-agents-zh agent_role_library | 1 |
| media real_generation_provider_agent | 16 |
| 客户正式可调用新增 | 0 |

## 最新流水线

1. To150: 50 个 `SKILL.md` / Agent Skill 兼容来源候选已落盘。
2. open-design: 已完成只读初扫并派发外部 API 依赖复核。
3. agency-agents-zh: 已作为六部门 Agent 角色库候选源入库，并生成 Top60 子角色筛选队列。
4. 媒体智能体: 已新增图片/视频制作候选梳理、`MEDIA_AGENT_INTAKE_QUEUE.md` 与 `MEDIA_REAL_GENERATION_PROVIDER_REVIEW_QUEUE.md`，目标包含真实出图、真实出视频。
5. 媒体真实生成扩展: 新增 16 个 provider / open-source / self-host / programmatic video 候选卡，并生成 `MEDIA_REAL_GENERATION_LICENSE_REVIEW_QUEUE.md`。
6. 许可证窗口是当前关键路径: 先做 L1/source verification。

## 下一步

- 许可证窗口复核 agency-agents-zh 的 MIT、上游英文版版权边界、convert/install 脚本行为和商用限制。
- 研究窗口可继续按六部门补 agency-agents-zh Top60 子角色。
- 测试台等待 L1 后做 role smoke，不做 Skill L2。
- 测试台优先对媒体 P0 队列做 role/mock smoke；P1 做 dry-run；P2 先由许可证窗口做 API/依赖复核和中转站 route check，通过后做 sandbox 内真实生成 smoke。
- 许可证窗口优先处理 16 个媒体真实生成候选，输出 can_route_check / provider_key_required / model_level_review_required / infrastructure_required / blocked。

## 不变边界

DeepAgents smoke 通过不等于正式 L2 通过；role smoke 通过不等于正式 L2 通过；候选卡落盘不等于客户正式可调用；稳交付库仍为 13 个客户正式可调用 Skill。
