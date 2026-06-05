# 中小微 AI.Skills 候选调用库索引

更新时间: 2026-06-05

## 当前总数

| 分类 | 数量 | 说明 |
| --- | ---: | --- |
| draft_l3 | 4 | 早期已形成 draft L3 的候选 |
| component_only | 6 | 组合组件，不独立客户调用 |
| mock_callable | 73 | 可 mock/read-only 试跑 |
| dry_run_callable | 17 | 可 dry-run 试跑 |
| needs_license_review | 67 | To150 50 个来源候选 + agency-agents-zh 角色库源候选 + 16 个媒体真实生成候选 |
| total_candidate_cards | 167 | 当前实际落盘候选卡 |
| 客户正式可调用新增 | 0 | 稳交付库仍为 13 |

## 当前目录

- `candidates/draft_l3/`
- `candidates/mock_callable/`
- `candidates/dry_run_callable/`
- `candidates/component_only/`
- `candidates/needs_license_review/`
- `candidates/deepagents_smoke_passed/`

## 最新文件

- `AGENCY_AGENTS_ZH_INTAKE_RESULT.md`
- `queues/AGENCY_AGENTS_ZH_INTAKE_QUEUE.md`
- `OPEN_DESIGN_PRELIMINARY_API_SCAN.md`
- `queues/OPEN_DESIGN_EXTERNAL_API_DEPENDENCY_REVIEW_QUEUE.md`
- `MEDIA_REAL_GENERATION_RESEARCH_EXPANSION_RESULT.md`
- `queues/MEDIA_REAL_GENERATION_LICENSE_REVIEW_QUEUE.md`

## 来源类型

| source_type / skill_source_class | 用途 |
| --- | --- |
| native_agent_skill | 已有本地或上游 SKILL.md 的技能来源 |
| agent_skill_compatible | 接近 Agent Skill 结构，需要迁移或 manifest 适配 |
| agent_role_library / agent_role_compatible | Markdown Agent 角色库，进入角色层筛选，不直接当 Skill |
| real_generation_provider_agent | 真实图片/视频/头像生成 provider 候选，先做 L1 和 route check |
| self_hosted_media_engine / programmatic_video_agent | 自托管或本地渲染媒体候选，先做基础设施和依赖复核 |

客户正式可调用 Skill 仍为 13。
