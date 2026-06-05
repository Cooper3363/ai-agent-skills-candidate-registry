# 候选库执行追踪

更新日期: 2026-06-05

## 当前基线

- 稳交付库客户正式可调用 Skill: 13。
- 候选库总候选卡: 167。
- 本轮新增客户正式可调用: 0。

## 已完成流水线

| 阶段 | 状态 | 产物 |
| --- | --- | --- |
| To50 候选扩展 | completed | 50 张候选卡、Top15 L2、11 个 draft L3 候选 |
| To100 候选扩展 | completed | 新增 50 张候选卡、Top15 L2、13 个 draft L3 候选 |
| To150 Agent Skill 来源扩展 | candidate_cards_landed | 新增 50 张 needs_license_review 候选卡 |
| open-design 初扫 | dependency_review_queued | 外部 API 依赖复核队列 |
| agency-agents-zh 入库 | role_library_candidate_landed | 1 张源级候选卡 + Top60 角色筛选队列 |
| 图片/视频媒体智能体梳理 | intake_queued | `MEDIA_IMAGE_VIDEO_AGENT_CANDIDATES.md` + `queues/MEDIA_AGENT_INTAKE_QUEUE.md` |
| 媒体真实生成 Provider 路由 | provider_review_queued | `MEDIA_REAL_GENERATION_PROVIDER_PLAN.md` + `queues/MEDIA_REAL_GENERATION_PROVIDER_REVIEW_QUEUE.md` |
| 媒体真实生成候选扩展 | candidate_cards_landed | 新增 16 张 needs_license_review 候选卡 + `queues/MEDIA_REAL_GENERATION_LICENSE_REVIEW_QUEUE.md` |

## agency-agents-zh 窗口任务

| 窗口 | 当前状态 | 下一步 |
| --- | --- | --- |
| 研究窗口 | queued | 按六部门复核 Top60 子角色，补映射和重复关系 |
| 许可证窗口 | queued | 复核 MIT、上游版权、脚本行为、商用限制 |
| 测试台窗口 | pending_l1 | L1 放行后做 role smoke |
| 封装窗口 | pending_role_smoke | 后续按角色包候选封装，不生成独立 L3 |
| 平台验收窗口 | not_ready | 等 role smoke / 角色包文件齐全后复核 |

## 媒体智能体窗口任务

| 窗口 | 当前状态 | 下一步 |
| --- | --- | --- |
| 研究窗口 | queued | 补齐 agency-agents-zh 中短视频、抖音、快手、小红书、B站、社媒设计等角色 |
| 许可证窗口 | queued | 复核 open-design P1/P2 子 skill 的 fal、Sora、Veo、Runway、Luma、Venice、Figma、Remotion、PPT/export 依赖和中转站 route |
| 测试台窗口 | ready_for_p0 | P0 做 role/mock smoke；P1 dry-run；P2 route check 通过后做 sandbox 真实生成 smoke |
| 封装窗口 | pending_smoke | smoke 通过后生成候选卡；真实生成类记录 provider、model、job id、成本和输出路径 |
| 平台验收窗口 | not_ready | 只验收候选调用边界，不改变稳交付 13 个基线 |

## 边界

agency-agents-zh 是 Agent 角色库，不是标准 `SKILL.md / skill.yaml` Skill 库。它进入角色层候选，不进入稳交付客户可调用库。
