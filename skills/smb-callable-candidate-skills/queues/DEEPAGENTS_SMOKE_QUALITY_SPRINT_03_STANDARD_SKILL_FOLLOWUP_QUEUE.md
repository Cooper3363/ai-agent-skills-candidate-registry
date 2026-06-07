# DEEPAGENTS_SMOKE_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_QUEUE

生成日期：2026-06-05

来源：`../LICENSE_REVIEW_QUALITY_SPRINT_03_STANDARD_SKILL_FOLLOWUP_RESULT.md`

本队列只包含 Sprint03 标准 Skill 补资料后 L1 放行项。只允许 metadata/mock smoke，不允许真实执行上游工具。

## Hard Boundaries

- 不安装依赖。
- 不访问外网。
- 不调用 API/provider。
- 不写 key。
- 不读取客户文件。
- 不写或生成本地文件。
- 不上传、不发送、不写业务系统。
- 不调用 draw.io CLI、Playwright、browser screenshot、LibreOffice、Poppler 或真实文件处理工具。
- 不送正式 L2，不封装，不客户调用。

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 2 |
| smoke queue total | 2 |

## Queue

| # | candidate_id | source_repo | source_subdir | smoke_type | trial_mode | write_allowed | export_allowed | upload_allowed | real_file_read_allowed | smoke_focus |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint03_openagentskills_drawio_process_candidate` | `Agents365-ai/drawio-skill` | `skills/drawio-skill/SKILL.md` | metadata/mock | `metadata_only`, `mock_only`, `read_only`, `external_action_blocked` | false | false | false | false | mock SOP/support process text -> diagram metadata, nodes/edges, layout plan |
| 2 | `quality_sprint03_mdskills_file_processing_excel_candidate` | `openai/skills` | `skills/.curated/spreadsheet/SKILL.md` | mock | `mock_only`, `read_only`, `external_action_blocked` | false | false | false | false | synthetic rows -> cleaning rules, metric summary, weekly report structure |

## Excluded From Smoke

| candidate_id | reason |
| --- | --- |
| `quality_sprint03_openagentskills_social_card_candidate` | `blocked_by_license`: AGPL-3.0；除非法务或指挥中心另行批准，不送 smoke |
| `quality_sprint03_vercel_agent_skills_data_report_candidate` | `market_lead_or_retire`: 未找到 `data-report` child skill；不按经营报表候选推进 |

