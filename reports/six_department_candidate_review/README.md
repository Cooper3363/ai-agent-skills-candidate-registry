# 六部门候选池审查包

来源文档：`C:\Users\Administrator\Downloads\六部门角色与Skill适配方案(1).docx`

生成时间：2026-06-03

## 定位

本目录是 AI.Skills 指挥中心的内部候选池审查包，不是客户可调用 Skill 包，也不是安装包。

当前平台客户可调用基线仍只认 13 个已通过平台调用验收的 Skill：

1. `marketing_copy_pack`
2. `daily_weekly_metrics_reporter`
3. `metric_exception_classifier`
4. `faq_answer_with_citations`
5. `support_ticket_classifier`
6. `structured_campaign_brief`
7. `structured_metric_summary`
8. `crm_note_structurer`
9. `support_reply_guardrail`
10. `marketing_compliance_guard`
11. `support_pii_redactor`
12. `support_kb_doc_cleaner`
13. `expense_invoice_parser`

六部门文档中的新候选默认状态为：内部候选，未复核，未测试，不可客户调用。

## 提取结果

| 项目 | 数量 |
| --- | ---: |
| Word 表格行数 | 63 |
| 唯一链接 | 57 |
| GitHub 链接 | 14 |
| ClawHub 链接 | 43 |
| 部门 | 6 |
| 角色 | 24 |

## 文件说明

| 文件 | 用途 |
| --- | --- |
| `SOURCE_DOC_EXTRACT.md` | Word 表格提取后的结构化清单，保留部门、角色、工作内容、来源类型和链接 |
| `CANDIDATE_CLASSIFICATION.md` | 候选分类、每部门 Top 3、与已通过 13 个 Skill 的覆盖关系 |
| `LICENSE_REVIEW_QUEUE.md` | L1 许可证和商用风险复核队列 |
| `LICENSE_REVIEW_RESULT.md` | 许可证窗口回传的 L1 初筛结果，含 5 个可送正式 L2、3 个补资料、ClawHub 暂缓 |
| `L2_TEST_QUEUE.md` | L2 中文业务用例模板队列，仅许可证通过后执行 |
| `L2_TEMPLATE_PREPLAN_RESULT.md` | 测试台回传的 18 个候选 L2 模板预案结果，不代表正式 L2 通过 |
| `L2_OFFICIAL_RESULT.md` | 测试台回传的 5 个 L1 放行候选正式 L2 simulated 结果 |
| `COMPONENT_POOL_ADDITIONS.md` | 六部门新增 3 个组件候选记录，不独立 L3，不客户调用 |

## 验收门槛

新候选必须逐项通过以下流程后，才能进入平台客户调用：

| 阶段 | 要求 | 失败处理 |
| --- | --- | --- |
| L1 许可证复核 | LICENSE、SPDX、商用限制、依赖/API/模型风险清楚 | 许可证不清、商用限制不清、依赖高风险时暂缓 |
| L2 中文业务测试 | 至少 3 个中文业务用例，输出结构稳定，权限边界清楚 | 低于 70 分、结构不稳、高风险动作不清时不送封装 |
| L3 标准封装 | 产出 `SKILL.md`、`skill.yaml`、输入输出、权限边界、测试用例、平台交接备注 | 缺关键字段或边界不清时退回 |
| 平台调用验收 | Skill ID、intent、adapter target、schema、失败模式、人工复核触发、最小调用样例通过 | 未通过则不可客户调用 |

## 当前结论

- 可直接给平台客户调用：仍为已验收 13 个 Skill。
- 六部门文档候选：全部进入内部候选池，不新增客户可调用 Skill。
- GitHub 14 个链接：L1 初筛已完成；5 个候选可进入正式 mock L2，3 个 L2 优先候选需补资料，其余为组件观察或暂缓。
- ClawHub 43 个链接：许可证/SPDX、维护状态、作者授权、依赖/API/模型条款不可核验，全部不得送正式 L2。
- 邮件发送、CRM/OAuth、日历、财务、合同、薪酬、网页抓取、图片/视频生成默认高风险，未明确权限和真实依赖边界前暂缓。
- 测试台已完成 18 个 Top 候选的 L2 模板预案；当前仅 5 个 L1 放行候选可进入正式 L2 simulated。

## 最新状态：正式 L2 已完成

- 测试台已完成 5 个 L1 放行候选的正式 L2 simulated，结果见 `L2_OFFICIAL_RESULT.md`。
- `visual_prompt_brief_candidate`、`sales_followup_draft_candidate`：L2 通过可封装，下一步进入 `draft_l3` 封装队列。
- `sales_meeting_task_brief_candidate`、`lead_research_brief_candidate`、`competitor_product_snapshot_candidate`：仅进入六部门组件池，见 `COMPONENT_POOL_ADDITIONS.md`。
- 六部门候选池当前新增客户可调用 Skill 仍为 0。
