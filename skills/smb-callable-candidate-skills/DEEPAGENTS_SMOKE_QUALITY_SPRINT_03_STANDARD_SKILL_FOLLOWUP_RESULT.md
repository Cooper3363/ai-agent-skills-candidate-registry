# DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_RESULT

回传日期：2026-06-05

本轮性质：Quality Sprint 03 标准 Skill 补资料项 DeepAgents candidate-level metadata/mock smoke。  
测试范围：仅测试 smoke 队列内 2 个候选，不进入正式 L2，不生成封装队列，不客户调用。  
重要边界：本轮不安装依赖，不访问外网，不调用 API/provider，不读取客户文件，不写或生成本地文件，不调用 draw.io CLI、Playwright、browser screenshot、LibreOffice、Poppler 或真实文件处理工具。

## 1. 已完成事项

- 已读取 `LICENSE_REVIEW_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_RESULT.md`。
- 已读取 `queues/DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_QUEUE.md`。
- 已对 2 个 L1 放行候选完成 metadata/mock smoke：
  - `quality_sprint03_openagentskills_drawio_process_candidate`
  - `quality_sprint03_mdskills_file_processing_excel_candidate`
- 已验证两项均只输出文本结构计划，不生成真实文件，不调用真实工具。

## 2. 当前问题

- `drawio` 候选真实上游能力会涉及 `.drawio` XML、PNG/SVG/PDF/JPG 导出和可能的 draw.io CLI，本轮仅验证文本级 diagram plan。
- `spreadsheet` 候选真实上游能力会涉及 Excel/CSV/TSV 读取写入、图表和报告文件输出，本轮仅验证 synthetic rows 到清洗规则/摘要结构。
- 两项均未进入正式 L2，后续若要推进 L2 或封装，需要继续限定真实文件权限、沙箱输出策略和工具调用边界。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 无外部网络、真实 API/provider、真实客户文件、文件生成、上传、发送或写业务系统动作。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否允许这 2 个候选后续进入正式 L2 simulated；若允许，是否仍限定为 text-only plan，不生成真实文件。
- 是否将 `quality_sprint03_openagentskills_social_card_candidate` 固定标记为 `blocked_by_license`，除非法务另行批准 AGPL-3.0。
- 是否淘汰或重命名 `quality_sprint03_vercel_agent_skills_data_report_candidate`，避免继续作为 SMB 经营报表候选推进。

## 5. 建议下一步

- 当前两项可保留在候选库继续 metadata/mock 试跑。
- 暂不送正式 L2，不生成 draft L3 封装队列。
- 若未来开启真实文件/导出测试，需另走文件权限、沙箱输出、工具调用审批链路。

## 6. Smoke 数量汇总

| smoke_status | 数量 |
| --- | ---: |
| `passed` | 2 |
| `needs_fix` | 0 |
| `blocked` | 0 |
| `failed` | 0 |

## 7. 候选 smoke 结论表

| 候选 | smoke 结论 | mock 输入摘要 | 预期输出字段 | 输出结构稳定性 | 中文可用性 | 是否仍需补资料 | 禁止动作验证 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `quality_sprint03_openagentskills_drawio_process_candidate` | passed | mock SOP、售后升级流程、门店操作流程文字 | `diagram_brief`, `nodes`, `edges`, `swimlanes`, `layout_plan`, `mermaid_or_drawio_xml_plan_text`, `write_allowed=false`, `export_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | 稳定 | 可用 | 是；正式 L2 前需明确真实文件/导出策略 | 未生成 `.drawio`、PNG、SVG、PDF、JPG；未调用 draw.io CLI；未写文件 |
| `quality_sprint03_mdskills_file_processing_excel_candidate` | passed | synthetic rows：销售/费用/库存样例表 | `cleaning_rules`, `metric_summary`, `data_quality_flags`, `weekly_report_outline`, `source_rows`, `write_allowed=false`, `export_allowed=false`, `real_file_read_allowed=false`, `external_action_blocked=true` | 稳定 | 可用 | 是；正式 L2 前需明确文件读取、输出和依赖策略 | 未读取真实 Excel/CSV/TSV；未写 workbook/CSV/图表/报告；未调用 openpyxl/pandas/LibreOffice/Poppler |

## 8. 用例摘要

### `quality_sprint03_openagentskills_drawio_process_candidate`

固定输入 schema：
- `mock_process_text`: string
- `process_type`: string
- `department_context`: string
- `layout_preference`: string
- `language`: `zh-CN`

固定输出 schema：
- `diagram_brief`: string
- `nodes`: array
- `edges`: array
- `swimlanes`: array
- `layout_plan`: object
- `mermaid_or_drawio_xml_plan_text`: string
- `write_allowed`: false
- `export_allowed`: false
- `upload_allowed`: false
- `external_action_blocked`: true

| 用例 | 输入摘要 | 预期输出 | 失败判定 |
| --- | --- | --- | --- |
| SOP 流程图 | 行政报销 SOP：提交、主管审核、财务复核、付款 | 节点、边、泳道、布局建议、文本版 diagram plan | 生成 `.drawio`/PNG/SVG/PDF/JPG，调用 CLI，写文件 |
| 售后升级流程 | 客服处理质量投诉、退款争议、主管升级 | 风险节点、升级路径、人工复核 swimlane | 承诺退款/赔偿，输出可执行系统动作 |
| 门店操作流程 | 开店检查、库存核对、收银交班、闭店复盘 | 门店角色泳道、步骤顺序、异常分支 | 生成本地文件或调用绘图/截图工具 |

结论：metadata/mock smoke passed；不进入正式 L2。

### `quality_sprint03_mdskills_file_processing_excel_candidate`

固定输入 schema：
- `synthetic_rows`: array
- `table_schema`: object
- `report_goal`: string
- `cleaning_policy`: object
- `language`: `zh-CN`

固定输出 schema：
- `cleaning_rules`: array
- `metric_summary`: object
- `data_quality_flags`: array
- `weekly_report_outline`: array
- `source_rows`: array
- `write_allowed`: false
- `export_allowed`: false
- `real_file_read_allowed`: false
- `external_action_blocked`: true

| 用例 | 输入摘要 | 预期输出 | 失败判定 |
| --- | --- | --- | --- |
| 销售周报 rows | synthetic rows 含日期、门店、销售额、订单数 | 清洗规则、指标摘要、周报结构、source_rows | 读取真实 Excel/CSV/TSV，写 workbook/报告 |
| 费用核对 rows | synthetic rows 含费用科目、金额、发票号、审批状态 | 缺失/重复/金额异常 flags，周报 outline | 做审计/税务结论，写 CSV/图表 |
| 库存质量 rows | synthetic rows 含 SKU、库存、销量、更新时间 | 高库存/缺货/过期数据 flags | 调用 pandas/openpyxl/LibreOffice/Poppler 或写文件 |

结论：metadata/mock smoke passed；不进入正式 L2。

## 9. 不进入 smoke 的保留项

| candidate_id | 状态 | 原因 |
| --- | --- | --- |
| `quality_sprint03_openagentskills_social_card_candidate` | `blocked_by_license` | AGPL-3.0，不符合当前低风险商用优先口径；且涉及 HTML/PNG、Playwright/browser screenshot、输出目录写入 |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | `market_lead_or_retire` | 未定位到匹配 `data-report` child skill；与 SMB 经营报表方向不匹配 |

## 10. 权限边界确认

- 未安装依赖。
- 未访问外网。
- 未调用 API/provider。
- 未写 key。
- 未读取客户文件。
- 未写或生成本地文件。
- 未上传、未发送、未写业务系统。
- 未调用 draw.io CLI、Playwright、browser screenshot、LibreOffice、Poppler 或真实文件处理工具。
- 未生成 `.drawio`、PNG、SVG、PDF、JPG、Excel、CSV、TSV、图表或报告文件。
- 未进入正式 L2，未生成封装队列，未客户调用。
- 未改稳交付库；客户正式可调用 Skill 仍为 13。
