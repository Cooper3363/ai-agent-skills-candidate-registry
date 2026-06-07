# LICENSE_REVIEW_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_RESULT

回传日期：2026-06-05

## 1. 已完成事项

- 已读取 `QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP.md`。
- 已按指挥中心范围，仅对 2 个建议重新送 L1 的候选完成轻量 L1 / trial mode 复核：
  - `quality_sprint03_openagentskills_drawio_process_candidate`
  - `quality_sprint03_mdskills_file_processing_excel_candidate`
- 已记录另外 2 个不重审候选的保留状态：
  - `quality_sprint03_openagentskills_social_card_candidate`
  - `quality_sprint03_vercel_agent_skills_data_report_candidate`
- 已生成 DeepAgents candidate smoke 队列：`queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_QUEUE.md`。
- 本轮未安装依赖、未访问外网、未调用 API/provider、未写 key、未读取客户文件、未写或生成本地文件、未上传、未发送、未写业务系统、未修改稳交付库。

## 2. 当前问题

- `drawio` 候选虽为 MIT，但上游完整能力会生成 `.drawio` XML 并可导出 PNG/SVG/PDF/JPG，还可能依赖 draw.io desktop CLI；本轮只能保留 metadata/mock，不允许真实文件生成或导出。
- `spreadsheet` 候选虽为 Apache-2.0，但上游完整能力涉及读取/写入 `.xlsx/.csv/.tsv`、生成图表和输出文件；本轮只能使用 synthetic rows，不读取真实文件，不写任何输出。
- `social_card` 已定位到具体仓库但许可证为 AGPL-3.0，按当前低风险商用优先口径不得送 smoke。
- `vercel_agent_skills_data_report` 未定位到对应 `data-report` child skill，不应按经营报表候选继续推进。

## 3. 阻塞原因

- 无权限阻塞。
- 本轮重审 2 项均非 `blocked`，但均禁止真实执行。
- 不重审 2 项中：
  - `social_card` 为许可证阻塞：AGPL-3.0。
  - `vercel data-report` 为来源定位阻塞：未找到匹配 child skill。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 2 个重审候选进入 DeepAgents candidate smoke，仅限 metadata/mock。
- 是否将 `openagentskills_social_card_candidate` 固定标记为 `blocked_by_license`，除非法务另行批准 AGPL-3.0。
- 是否淘汰 `vercel_agent_skills_data_report_candidate`，或改名为面向技术/网站运维的独立 market lead 后另行研究。

## 5. 建议下一步

- 测试台读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_QUEUE.md`。
- `drawio` smoke 只输出流程图 metadata、节点/边结构、Mermaid/drawio XML 计划文本；不得写 `.drawio`、PNG、SVG、PDF、JPG，不调用 draw.io CLI。
- `spreadsheet` smoke 只使用 synthetic rows；不得读取真实 Excel/CSV/TSV，不写 workbook、CSV、图表或报告文件。
- 两项均不得进入正式 L2、不得封装、不得客户调用；如未来要真实文件读写，需另开文件权限/沙箱输出审批链路。
- 客户正式可调用 Skill 仍为 13。

## 6. 数量汇总

| 分类 | 数量 |
| --- | ---: |
| 重审候选 | 2 |
| `can_mock_smoke` | 2 |
| `can_dry_run_smoke` | 0 |
| `can_route_check` | 0 |
| `component_only` | 0 |
| `needs_more_license_info` | 0 |
| `blocked` | 0 |
| 可送 smoke | 2 |
| 可送正式 L2 | 0 |
| 不重审保留项 | 2 |
| 客户正式可调用 Skill | 13 |

## 7. 两个重审候选 L1 结论

| candidate_id | source repo / subdir | LICENSE / 条款 | DeepAgents / 通用 Agent Skill 适配 | 中转站模型通道适配 | 六部门业务场景 | 依赖/API/文件写入风险 | trial mode | 是否可送 smoke | 禁止动作 | l1_result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `quality_sprint03_openagentskills_drawio_process_candidate` | `https://github.com/Agents365-ai/drawio-skill`; `skills/drawio-skill/SKILL.md` | MIT；产品筛选阶段可接受 | 可抽成流程图/SOP 图 metadata skill：输入流程说明，输出节点、边、泳道、布局建议 | 文本规划可走 OpenAI-compatible 中转站；视觉自检不在本轮 | 行政/运营、客服、培训：SOP、售后升级流程、门店操作流程 | 上游真实能力会写 `.drawio` XML 并导出 PNG/SVG/PDF/JPG，可能调用 draw.io desktop CLI | `metadata_only`, `mock_only`, `read_only`, `external_action_blocked` | yes | 不生成 `.drawio`、PNG、SVG、PDF、JPG；不调用 draw.io CLI；不写文件 | `can_mock_smoke` |
| `quality_sprint03_mdskills_file_processing_excel_candidate` | `https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet`; `skills/.curated/spreadsheet/SKILL.md` | Apache-2.0；产品筛选阶段可接受 | 可抽成表格清洗/指标口径/周报结构化 mock skill：输入 synthetic rows，输出规则和摘要 | 文本解释、规则生成、结构化摘要可走 OpenAI-compatible 中转站 | 经营报表/财务/行政：表格清洗、指标口径、周报结构化 | 上游真实能力涉及 `openpyxl`/`pandas`、可选 `matplotlib`/LibreOffice/Poppler；真实文件读写和图表输出风险高 | `mock_only`, `read_only`, `external_action_blocked` | yes | 不读取真实 Excel/CSV/TSV；不写 workbook/CSV/图表/报告文件；不处理客户财务文件 | `can_mock_smoke` |

## 8. 不重审候选保留状态

| candidate_id | 定位结果 | license / 状态 | 保留结论 | 不送 smoke 原因 |
| --- | --- | --- | --- | --- |
| `quality_sprint03_openagentskills_social_card_candidate` | 已定位到 `https://github.com/op7418/guizang-social-card-skill`，root `SKILL.md` | AGPL-3.0 | `blocked_by_license` | AGPL-3.0 不符合当前低风险商用优先口径；且会生成 HTML/PNG、使用 Playwright/browser screenshot、写输出目录 |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | 未定位到 `data-report` child skill；实际 Vercel skills 偏前端/部署/网站优化 | MIT 线索不等于原候选可用 | `market_lead_or_retire` | 与 SMB 经营报表方向不匹配；缺目标 child skill、manifest、业务适配证据 |

## 9. 硬边界

- 不安装依赖。
- 不访问外网。
- 不调用 API/provider。
- 不写 key。
- 不读取客户文件。
- 不生成或写入本地文件。
- 不上传、不发送、不写业务系统。
- 不调用 draw.io CLI、Playwright、browser screenshot、LibreOffice、Poppler 或真实文件处理工具。
- 不把本轮任何项送正式 L2、封装或客户调用。

