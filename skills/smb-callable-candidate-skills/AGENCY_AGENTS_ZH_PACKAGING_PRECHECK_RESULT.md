# Agency Agents ZH Packaging Precheck Result

回传时间: 2026-06-05
回传窗口: AI.Skills 封装专员窗口
任务: agency-agents-zh 角色包封装预检查

## 1. 已完成事项

- 已读取 `candidates/needs_license_review/agency_agents_zh_role_library_candidate/CANDIDATE.md`。
- 已读取 `candidates/needs_license_review/agency_agents_zh_role_library_candidate/candidate.yaml`。
- 已读取 `queues/AGENCY_AGENTS_ZH_INTAKE_QUEUE.md`。
- 已完成角色库源级候选卡完整性检查。
- 已确认当前未生成 `SKILL.md` / `skill.yaml`。
- 已确认该对象当前只作为角色库候选源，不作为独立客户可调用 Skill。

## 2. 当前问题

- 当前状态仍为 `needs_license_review`，许可证窗口尚未给出 L1/source verification 放行。
- role smoke 尚未开始，`role_smoke_status: not_started`。
- formal L2 当前为 `not_applicable_yet`，不得写成 L2 通过。
- 后续即使 role smoke 通过，也只能考虑封装为“角色包候选”或平台角色库/组合编排候选，不应作为独立客户可调用 Skill。

## 3. 阻塞原因

- 无权限阻塞。
- 无候选卡字段缺失阻塞。
- 当前流程阻塞为正常阶段门禁：等待许可证 L1/source verification 与后续 role smoke 结果。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否将 `agency_agents_zh_role_library_candidate` 送许可证窗口做 L1/source verification。
- L1 放行后，是否按 intake 队列的 Top60 子角色进入 role smoke，而不是展开全仓角色。
- role smoke 通过后，是否按“角色包候选”路径封装，避免误进入独立 L3 Skill。

## 5. 建议下一步

- 许可证窗口先核验 MIT 许可证、上游英文版版权边界、中文本地化边界、仓库脚本行为和商用限制。
- 测试台仅对 L1 放行的 Top60 子角色做 role smoke，每个角色至少 1 个中文六部门岗位 mock 场景。
- role smoke 只验证角色说明是否能产生稳定岗位输出，不得标记为正式 L2 通过。
- 封装窗口后续只按角色包候选或组合编排候选处理，不生成独立客户可调用 Skill。
- 本轮不生成 `SKILL.md` / `skill.yaml`，不改稳交付库，客户正式可调用 Skill 仍为 13。

## 6. 预检查明细

| 检查项 | 预期 | 实际 | 结论 |
| --- | --- | --- | --- |
| `CANDIDATE.md` | 存在 | 存在 | pass |
| `candidate.yaml` | 存在 | 存在 | pass |
| `SKILL.md` | 不应生成 | 未生成 | pass |
| `skill.yaml` | 不应生成 | 未生成 | pass |
| `source_type` | `agent_role_library` | `agent_role_library` | pass |
| `skill_source_class` | `agent_role_compatible` | `agent_role_compatible` | pass |
| `customer_callable` | `false` | `false` | pass |
| `platform_deliverable` | `false` | `false` | pass |
| `not_l2_passed` | `true` | `true` | pass |
| `role_smoke_status` | `not_started` | `not_started` | pass |
| `formal_l2_status` | 不应为 L2 passed | `not_applicable_yet` | pass |
| 禁止 install/convert 脚本 | 必须写清 | 已写清 `install_allowed: false`，并禁止执行真实 convert/install 脚本写入用户工具目录 | pass |
| 权限边界 | read-only / external action blocked | 已写清 | pass |
| 人工复核触发 | 必须写清 | 已写清 | pass |

## 7. 封装结论

结论：预检查通过，但当前仅可保持为 `needs_license_review` 的角色库源级候选卡。

不得生成 L3，不得生成 `SKILL.md` / `skill.yaml`，不得把 role smoke 写成 L2，通过后也应优先按“角色包候选”或组合编排候选处理。

## 8. 平台交接备注

- 该对象是角色库源，不是标准 callable Skill。
- 角色库内 Top60 子角色可以作为后续 role smoke 队列，但每个子角色仍需单独风险边界与人工复核触发。
- 高风险角色包括法律、税务、财务、HR、供应链、投放、客服合规等方向，role smoke 后仍需人工复核策略。
- 不执行安装脚本、不执行 convert 脚本、不写 OpenClaw/Hermes/Codex 用户目录。
- 稳交付库仍为 13，本轮不新增客户正式可调用 Skill。

