# 中小微 AI.Skills 候选调用库

更新日期: 2026-06-05

## 定位

本目录是 AI.Skills 指挥中心的候选调用库，用于收纳适合中小微企业业务场景的可评估、可 mock、可 dry-run 或可受控试点候选。进入本目录不等于客户正式可调用。

当前稳交付客户正式可调用库仍为:

`X:\codexwork\ai-agent-skills-registry\skills\p0-first-13-platform-callable-skills`

当前客户正式可调用 Skill 数量仍为 13；本候选库新增客户正式可调用数量为 0。

## 当前状态

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| draft_l3 | 4 | 早期六部门 draft L3 候选区 |
| mock_callable | 73 | 可用 mock/read-only 输入试跑的候选卡 |
| dry_run_callable | 17 | 只生成 dry-run 草稿或 payload，不触发外部动作 |
| component_only | 6 | 只作组合组件，不独立客户调用 |
| needs_license_review | 67 | 50 个 To150 Agent Skill 来源候选 + 1 个 agency-agents-zh 角色库源候选 + 16 个媒体真实生成候选 |
| total_candidate_cards | 167 | 当前实际落盘候选卡总数 |
| 客户正式可调用新增 | 0 | 稳交付库仍为 13 |

## 最新新增

- To150: 新增 50 个 `SKILL.md` / Agent Skill 兼容来源候选。
- open-design: 已建外部 API 依赖复核队列，尚未收入子 skill。
- agency-agents-zh: 已作为六部门 Agent 角色库候选源入库，candidate_id 为 `agency_agents_zh_role_library_candidate`。
- 媒体智能体: 已新增图片/视频制作候选梳理、intake 队列和真实生成 provider review 队列；目标包含真实出图、真实出视频，但先做中转站 route check 与 sandbox smoke。
- 媒体真实生成扩展: 新增 16 个 `needs_license_review` 候选，覆盖 OpenAI/Google/fal/Runway/Luma/FLUX/Ideogram/Recraft/Replicate/Stability/ComfyUI/Remotion/HeyGen/Synthesia/open-design。

## 角色库口径

`agency-agents-zh` 不是标准 `SKILL.md / skill.yaml` 技能库，而是 Markdown Agent 角色库。它适合补充六部门岗位角色层，后续按 Top60 子角色筛选、许可证复核和 role smoke 推进。

## 底座适配口径

候选库允许收纳 Skill、AI Agent、Agent Role、工作流包装和内部模板。准入重点是：能适配本平台底座或 DeepAgents，本轮模型调用可走 OpenAI-compatible 中转站，并能服务创意设计、运营、销售、电商、客服、管理六部门场景。

中转站只解决模型调用，不自动放行真实业务动作。图片/视频/音频生成可以在 provider route check 通过后做 sandbox 内真实 smoke；Figma/PPT/文件导出、平台上传发布、广告投放等仍默认 `external_action_blocked=true`，需单独复核。

## 不变边界

候选库扩容不等于客户正式可调用；DeepAgents smoke passed 不等于正式 L2 通过；role smoke 不等于 L2 通过；稳交付扩容必须完成 L1、L2、L3 和平台正式验收。
