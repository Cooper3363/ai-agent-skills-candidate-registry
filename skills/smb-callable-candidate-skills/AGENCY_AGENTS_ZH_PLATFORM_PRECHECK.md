# Agency Agents ZH Platform Precheck

回传时间: 2026-06-05
回传窗口: AI.Skills 平台调用验收窗口
任务: agency-agents-zh 角色库源候选的平台验收等待/边界预检查
验收口径: 仅做预检查，不做候选角色库 accepted，不做客户正式调用验收，不迁入稳交付库

## 已完成事项

- 已读取 `STATUS_SUMMARY.md`。
- 已读取 `queues/AGENCY_AGENTS_ZH_INTAKE_QUEUE.md`。
- 已确认 `agency_agents_zh_role_library_candidate` 当前只是角色库源候选，不是标准 `SKILL.md` / `skill.yaml` Skill。
- 已确认 agency-agents-zh Top60 子角色当前均为 `needs_license_review`，下一步为 `role_smoke_pending`。
- 已确认当前尚未完成 L1/source verification，尚未完成 role smoke，尚未封装角色包候选文件。
- 已确认本轮不能给 `accepted`，不能进入稳交付库，不能写成客户正式可调用 Skill。

## 当前状态摘要

| 项目 | 状态/数量 |
| --- | --- |
| 稳交付库客户正式可调用 Skill | 13 |
| 当前总候选卡 | 151 |
| agency-agents-zh 源级候选卡 | 1 |
| agency-agents-zh Top60 子角色 | 60 |
| 当前状态 | needs_license_review |
| L1/source verification | 未完成 |
| role smoke | 未完成 |
| 角色包候选文件 | 未封装 |
| 本轮新增客户正式可调用 Skill | 0 |

## 平台预检查结论

| 检查项 | 结论 |
| --- | --- |
| 是否可 accepted | 不可 accepted。当前仅为角色库源候选，未 L1、未 role smoke、未封装角色包。 |
| 是否可进入稳交付库 | 不可进入。候选源入库不等于稳交付扩容。 |
| 是否可写成客户正式可调用 Skill | 不可写成。当前不是标准 Skill 包，也未通过正式平台验收。 |
| 是否可作为候选角色库继续流转 | 可以继续等待 L1/source verification 与后续 role smoke。 |
| 客户正式可调用 Skill 数量 | 仍为 13。 |

## 后续验收门槛

只有同时满足以下条件后，平台验收窗口才可做候选角色库验收：

1. L1/source verification 放行：许可证、上游版权边界、convert/install 脚本行为、商用限制完成复核。
2. role smoke 通过：仅对 L1 放行角色执行中文六部门岗位场景 mock，且 role smoke 只代表角色稳定性检查，不等于正式 L2 通过。
3. 角色包候选文件齐全：每个拟验收角色需有稳定 role/candidate ID、业务部门/角色定位、trial mode、输入/输出字段、禁止动作、人工复核触发、权限/依赖边界、最小中文调用样例和测试记录。

## 当前问题

- agency-agents-zh 当前仍是角色库源候选，尚未完成 L1/source verification。
- Top60 子角色均为 `needs_license_review` / `role_smoke_pending`。
- 尚未形成可由平台验收窗口复核的角色包候选文件。
- 当前不能判断任何子角色为候选调用 accepted，更不能写成客户正式可调用 Skill。

## 阻塞原因

- 前置许可证与来源复核未完成。
- role smoke 未完成。
- 角色包候选文件未封装，缺少平台调用验收所需的 role/candidate schema、权限边界、失败模式和最小调用样例等完整材料。

## 需要 AI.Skills 指挥中心决策的问题

无新增决策点。当前属于前置流程未完成，按既定流程等待许可证窗口、研究窗口/测试台和封装窗口后续材料即可。

## 建议下一步

- 许可证窗口先完成 MIT、上游英文版版权边界、convert/install 脚本行为和商用限制复核。
- 测试台仅对 L1 放行子角色执行 role smoke，不做 Skill L2，不写成正式 L2 通过。
- 封装窗口在 role smoke 后再输出角色包候选文件，避免把全仓角色一次性写成客户可调用 Skill。
- 平台验收窗口收到 L1 放行、role smoke 结果和角色包候选文件后，再按候选角色库验收口径复核。

## 不变边界

- 不安装依赖。
- 不执行 convert/install 脚本。
- 不写 OpenClaw/Hermes/Codex 用户目录。
- 不调用外部 API。
- 不读取真实客户文件。
- 不客户调用。
- 不把角色库候选写成客户可调用 Skill。
- 稳交付库客户正式可调用 Skill 仍为 13。
