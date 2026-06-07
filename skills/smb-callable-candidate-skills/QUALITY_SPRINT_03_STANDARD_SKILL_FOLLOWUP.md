# Quality Sprint 03 标准 Skill 包补资料

更新日期: 2026-06-05

## 1. 已完成事项

- 已复核 `QUALITY_SOURCE_SPRINT_03_RESULT.md` 与 `LICENSE_REVIEW_QUALITY_SPRINT_03_RESULT.md`。
- 已针对 4 个暂缓项补充具体上游证据、repo/subdir、许可证、依赖和 trial mode 建议。
- 未安装依赖，未调用 API，未生成媒体或真实文件，未写 key，未访问真实账号，未上传素材，未改稳交付库。

## 2. 当前问题

- `quality_sprint03_openagentskills_social_card_candidate` 已定位到具体仓库，但许可证为 AGPL-3.0，不符合当前低风险商用优先规则。
- `quality_sprint03_vercel_agent_skills_data_report_candidate` 未找到 “data-report” 对应 child skill；原候选方向与上游实际 repo 不匹配。
- `drawio` 与 `spreadsheet` 能定位，但都涉及本地文件生成/写入，不能直接 smoke，只能先做 metadata/mock L1。

## 3. 阻塞原因

无权限阻塞。

候选项级阻塞主要来自：

- marketplace 线索需要落到具体 GitHub repo/subdir。
- 许可证不满足低风险商用要求。
- 文件/图片/表格/drawio 输出会触发真实文件写入边界。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否将 `drawio_process` 与 `mdskills_file_processing_excel` 重新送 L1，但限定为 `metadata_only` / `mock_only`，不允许文件写入。
- 是否将 `openagentskills_social_card` 因 AGPL-3.0 标记为 `blocked_by_license`，除非法务明确批准。
- 是否淘汰或重命名 `vercel_agent_skills_data_report`：当前上游没有 data-report child skill，建议不再按经营报表候选推进。

## 5. 建议下一步

- 可重新送 L1：`quality_sprint03_openagentskills_drawio_process_candidate`、`quality_sprint03_mdskills_file_processing_excel_candidate`。
- 不建议重新送 L1：`quality_sprint03_openagentskills_social_card_candidate`，原因是 AGPL-3.0。
- 继续 market_lead / blocked：`quality_sprint03_vercel_agent_skills_data_report_candidate`，原因是未找到对应 data-report child skill。

## 6. 四个暂缓项补资料表

| candidate_id | 定位结果 | source repo URL | 具体 subdir / child skill path | SKILL.md | skill.yaml / manifest | LICENSE / 商用条款 | 外部 API/provider/模型依赖 | 文件/媒体/设计输出边界 | BYOK | DeepAgents/通用 Skill 适配 | OpenAI-compatible route 适配 | 六部门业务场景 | trial mode 建议 | 是否可重新送 L1 | 建议状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `quality_sprint03_openagentskills_drawio_process_candidate` | 成功定位 | https://github.com/Agents365-ai/drawio-skill | `skills/drawio-skill/SKILL.md` | 是 | 未发现独立 `skill.yaml`；repo 为 Agent Skill 格式 | MIT | 不需要业务 API；需要 draw.io desktop CLI；可能用视觉模型做自检；Graphviz/脚本可选 | 会生成 `.drawio` XML，并可导出 PNG/SVG/PDF/JPG；当前必须禁用真实写文件/导出 | Skill 本身不需要；若用模型自检则走平台模型通道 | 可适配为流程图/SOP 图生成 mock skill | 文本规划可用；视觉自检不在本轮 | 行政/运营：SOP、售后流程、培训流程图 | `metadata_only` 首选；`mock_only` 次选 | 是 | `requeue_l1_metadata_only` |
| `quality_sprint03_mdskills_file_processing_excel_candidate` | 成功定位到真实 spreadsheet skill | https://github.com/openai/skills | `skills/.curated/spreadsheet/SKILL.md` | 是 | 未发现独立 `skill.yaml`；目录内有 `LICENSE.txt` | Apache-2.0 | 不需要外部业务 API；依赖 Python `openpyxl`/`pandas`，可选 `matplotlib`、LibreOffice、Poppler | 会读写 `.xlsx/.csv/.tsv`，可生成图表和输出文件；当前不得读客户文件或写真实文件 | 不需要 | 可抽为 mock 表格清洗/周报结构化 skill | 文本解释和规则生成可走 OpenAI-compatible；文件工具禁用 | 经营报表/财务：表格清洗、指标口径、周报 | `mock_only`；仅 synthetic rows | 是 | `requeue_l1_mock_only` |
| `quality_sprint03_openagentskills_social_card_candidate` | 成功定位，但许可证高风险 | https://github.com/op7418/guizang-social-card-skill | root `SKILL.md` | 是 | 未发现独立 `skill.yaml`；root `SKILL.md` + assets/references | AGPL-3.0 | 不需要 paid API；依赖 Node/Playwright/browser screenshot；可能涉及图片素材/网页来源 | 会生成 HTML，并通过 Playwright 渲染 PNG；会写任务目录和 `output/` | 不需要 paid API key | 技术上可适配，但许可证不适合当前低风险商用候选 | 文案/布局规划可用；截图渲染禁用 | 营销：小红书/公众号社媒卡片 | `not_suitable` | 否，除非法务批准 AGPL | `blocked_by_license` |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | 未定位到 data-report child skill | https://github.com/vercel-labs/skills；实际技能集合为 https://github.com/vercel-labs/agent-skills | 未找到 `data-report`；可见 skills 包括 `vercel-optimize`, `react-best-practices`, `web-design-guidelines`, `writing-guidelines`, `react-native-skills`, `react-view-transitions`, `deploy-to-vercel` 等 | 对这些 dev/web skills 是；对 data-report 未找到 | repo skills 格式，无 data-report manifest | `vercel-labs/skills` 为 MIT；`agent-skills` README 标注 MIT | `vercel-optimize` 可能依赖 Vercel 项目/指标；`deploy-to-vercel` 涉及部署写入 | 与经营报表候选不匹配；部分 skills 会上传/部署或读取代码项目 | 可能需要 Vercel token，视具体 skill | 不建议按经营报表候选适配 | 不适合作 SMB 经营报表 | 仅适合技术团队/网站运营，不是六部门通用经营报表 | `not_suitable` | 否 | `market_lead_or_retire` |

## 7. 逐项补充说明

### 7.1 `quality_sprint03_openagentskills_drawio_process_candidate`

定位成功。

- Open Agent Skills 页面给出的安装入口为 `https://github.com/Agents365-ai/drawio-skill --skill drawio-skill`。
- GitHub 仓库结构显示具体目录：`skills/drawio-skill`。
- 仓库页面标注 MIT license。
- 上游能力会生成 `.drawio` 文件，并支持导出 PNG/SVG/PDF/JPG；还依赖 draw.io desktop CLI。
- 对中小微可落到：售后流程图、门店 SOP、客服升级流程、培训流程图。

建议：

- 重新送 L1。
- 只能 `metadata_only` 或 `mock_only`。
- 不进入真实 smoke，除非后续测试台允许 sandbox 文件输出，且明确 `export_allowed=false`。

### 7.2 `quality_sprint03_mdskills_file_processing_excel_candidate`

定位成功，但应从 mdskills marketplace 线索收窄为 OpenAI curated spreadsheet skill。

- mdskills 页面指向安装名：`openai/spreadsheet`。
- 可定位到 GitHub：`openai/skills/skills/.curated/spreadsheet`。
- 目录内存在 `SKILL.md` 和 `LICENSE.txt`。
- `LICENSE.txt` 为 Apache-2.0。
- `SKILL.md` 说明适用 `.xlsx/.csv/.tsv` 创建、编辑、分析、格式化和公式感知流程。
- 依赖边界包括 `openpyxl`、`pandas`、可选 `matplotlib`、LibreOffice、Poppler 等。

建议：

- 重新送 L1。
- 只做 mock rows，不读真实 Excel 文件，不写输出文件。
- 如后续要做真实表格处理，必须单独走文件读写权限和沙箱输出审批。

### 7.3 `quality_sprint03_openagentskills_social_card_candidate`

定位成功，但不建议继续。

- Open Agent Skills 页面给出的上游为 `op7418/guizang-social-card-skill`。
- GitHub 仓库 root 下存在 `SKILL.md` 和 `LICENSE`。
- `LICENSE` 为 GNU Affero General Public License v3。
- 该 skill 会生成 HTML，并通过 Playwright/browser screenshot 渲染 PNG，写入任务目录与输出目录。
- 虽然适配小红书/公众号场景较好，但 AGPL-3.0 与当前“低风险宽松许可证优先”规则冲突。

建议：

- 标记 `blocked_by_license`。
- 不重新送 L1，不进入 smoke。
- 如指挥中心仍想保留，可降为 `market_lead`，仅吸收“约束化社媒卡片设计模板”的方法论，不复用代码或 SKILL.md。

### 7.4 `quality_sprint03_vercel_agent_skills_data_report_candidate`

未定位到原假设的 data-report child skill。

- `vercel-labs/skills` 是 `npx skills` 工具仓库，不是业务 skill 包。
- `vercel-labs/agent-skills` 是 Vercel 官方 skill 集合，README 可见的 skills 更偏前端/部署/网站优化。
- 未找到 `data-report`、`analytics` 或适合 SMB 经营报表的 child skill。
- `vercel-optimize` 能生成 Vercel 项目成本/性能报告，但它需要 Vercel 项目上下文，不适合六部门经营报表。

建议：

- 不重新送 L1。
- 标记 `market_lead_or_retire`。
- 如要保留，应改名为 `vercel_tech_ops_report_candidate`，只面向技术/SaaS 网站运营，不再归入经营报表通用包。

## 8. 重新入队建议

| candidate_id | requeue_l1 | 推荐 trial mode | 原因 |
| --- | --- | --- | --- |
| `quality_sprint03_openagentskills_drawio_process_candidate` | yes | `metadata_only` | source/subdir/license 已定位，但文件导出风险高 |
| `quality_sprint03_mdskills_file_processing_excel_candidate` | yes | `mock_only` | source/subdir/license 已定位，但真实文件读写风险高 |
| `quality_sprint03_openagentskills_social_card_candidate` | no | `not_suitable` | AGPL-3.0；真实 HTML/PNG 输出风险 |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | no | `not_suitable` | 未找到 data-report child；业务方向不匹配 |

## 9. 缺口清单

| candidate_id | 缺口 |
| --- | --- |
| `quality_sprint03_openagentskills_drawio_process_candidate` | 需确认 `skills/drawio-skill/SKILL.md` 是否可脱离 draw.io CLI 做纯 mock；需确认是否允许后续 sandbox 写 `.drawio` 草稿 |
| `quality_sprint03_mdskills_file_processing_excel_candidate` | 需确认是否允许使用 synthetic rows 代替真实文件；若读写文件，需另走文件权限/沙箱审批 |
| `quality_sprint03_openagentskills_social_card_candidate` | AGPL-3.0 法务风险；Playwright/HTML/PNG 输出写文件风险 |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | 没有 data-report child skill；需要决定淘汰或改为技术运营候选 |

## 10. 使用过的公开来源

- Open Agent Skills drawio 页面：https://openagentskills.dev/skills/drawio-skill
- Agents365 drawio GitHub：https://github.com/Agents365-ai/drawio-skill
- Open Agent Skills social card 页面：https://openagentskills.dev/skills/guizang-social-card-skill
- Guizang social card GitHub：https://github.com/op7418/guizang-social-card-skill
- mdskills spreadsheet 页面：https://www.mdskills.ai/skills/spreadsheet
- OpenAI spreadsheet skill 目录：https://github.com/openai/skills/tree/main/skills/.curated/spreadsheet
- Vercel skills CLI 仓库：https://github.com/vercel-labs/skills
- Vercel agent skills 仓库：https://github.com/vercel-labs/agent-skills

## 11. 最终结论

- 4 个是否定位成功：
  - `drawio_process`：成功定位。
  - `mdskills_file_processing_excel`：成功定位。
  - `openagentskills_social_card`：成功定位，但许可证阻塞。
  - `vercel_agent_skills_data_report`：未定位到匹配 child skill。
- 可重新送 L1：2 个。
- 应继续 market_lead/blocked：2 个。
