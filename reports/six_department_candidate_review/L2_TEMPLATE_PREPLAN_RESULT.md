# L2 模板预案回传

回传来源：测试台窗口  
回传时间：2026-06-03  
状态：模板预案完成，不是正式 L2 结论

## 总体结论

测试台已读取内部资料包：

- `README.md`
- `SOURCE_DOC_EXTRACT.md`
- `CANDIDATE_CLASSIFICATION.md`
- `L2_TEST_QUEUE.md`

已为六部门每部门 Top 3 候选设计 L2 中文业务用例模板预案，共 18 个候选方向。每个候选均给出 3 个中文 mock 用例方向、预期输出字段、失败判定、权限边界、人工复核触发和是否需要真实 Harness 补测。

本轮只做模板预案：

- 不做正式 L2 测试
- 不给 L2 通过或未通过结论
- 不安装依赖
- 不访问外网
- 不访问真实账号
- 不发送邮件
- 不写 CRM、日历或任务
- 不跑真实抓取、OCR、图片、视频或音频处理

## 当前限制

| 问题 | 处理 |
| --- | --- |
| 新增文档候选均未完成许可证复核 | 等待 L1，通过后才能正式进入 L2 |
| 部分候选已由 13 个可交付 Skill 覆盖 | 避免重复占用 L2 资源 |
| ClawHub 来源许可证不清 | 只能保留模板或组件线索，不正式送测 |
| 高风险动作不清 | 真实账号、发送、写入、抓取、生成、法律、财务动作统一不得执行 |

## 需要指挥中心决策

| 决策点 | 当前建议 |
| --- | --- |
| 哪些候选可以从模板转为正式 L2 | 等 L1/许可证复核窗口回传后决定 |
| 已由 13 个 Skill 覆盖的场景是否重复送测 | 只保留映射，不作为新候选送测 |
| ClawHub 来源候选如何处理 | 许可证无法确认时统一暂缓 |
| 高风险动作候选如何测试 | 只允许 dry-run 或 mock L2 |

## 18 个候选模板摘要

| 部门 | 候选 / Skill ID | 当前处理 | L2 模板状态 | 主要边界 |
| --- | --- | --- | --- | --- |
| 创意设计 | `visual_prompt_brief_candidate` | 等待 L1，通过后可 mock L2 | 已完成 | 只生成提示词 brief，不生成图片，不调用图片模型 |
| 创意设计 | `storyboard_script_brief_candidate` | ClawHub 线索/组件，许可证不清前不正式 L2 | 已完成 | 只输出脚本/分镜，不生成视频/字幕文件 |
| 创意设计 | `brand_consistency_check_candidate` | ClawHub 线索/组件，许可证不清前不正式 L2 | 已完成 | 只检查 mock 文案/视觉描述，不读真实设计文件 |
| 运营 | `content_calendar_planner_candidate` | 许可证不清，部分被现有 Skill 覆盖 | 已完成 | 只输出日历草案，不写日历/任务/发布平台 |
| 运营 | `feedback_cluster_insights_candidate` | 许可证不清，可作新候选模板 | 已完成 | 只处理 mock 反馈，不读取真实用户数据 |
| 运营 | `operations_metric_brief_candidate` | 无需重复测试，可使用现有已验收 Skill | 已完成 | 复用 `structured_metric_summary`、`daily_weekly_metrics_reporter`、`metric_exception_classifier` |
| 销售 | `sales_followup_draft_candidate` | 等待 L1，可 mock L2，不能真实发送 | 已完成 | 只生成草稿，不发邮件/短信，不写 CRM |
| 销售 | `sales_meeting_task_brief_candidate` | 等待 L1，Google Workspace 写入动作暂缓 | 已完成 | 只输出任务草案，不写日历/任务/文档 |
| 销售 | `lead_research_brief_candidate` | 等待 L1，外部搜索/API 暂缓 | 已完成 | 只用 mock 页面文本，不搜索、不抓网页、不调用 API |
| 电商 | `product_listing_copy_candidate` | 大部分由现有营销 Skill 覆盖，电商专用需 L1 | 已完成 | 只生成草稿，不上传电商平台 |
| 电商 | `competitor_product_snapshot_candidate` | 等待 L1，真实抓取暂缓 | 已完成 | 只用 mock HTML，不访问网页、不代理、不绕 robots/ToS |
| 电商 | `order_inventory_exception_candidate` | 等待 L1，不写库存系统 | 已完成 | 只读 mock 订单/库存表，不写系统 |
| 客服 | `support_reply_flow_candidate` | 无需重复测试，可使用现有已验收 Skill | 已完成 | 复用 `faq_answer_with_citations`、`support_reply_guardrail`、`support_ticket_classifier` |
| 客服 | `complaint_escalation_summary_candidate` | 大部分由现有客服 Skill 覆盖，摘要新候选需 L1 | 已完成 | 只总结 mock 对话，不回访、不发消息 |
| 客服 | `support_quality_eval_candidate` | 等待 L1，可作为评测候选 | 已完成 | 只评测 mock 对话，不写质检系统 |
| 管理 | `hr_resume_privacy_masker_candidate` | 等待 L1，与已测 HR 脱敏方向一致 | 已完成 | 只用 mock 简历，不读真实文件、不上传 |
| 管理 | `invoice_receipt_review_candidate` | 无需重复测试，可使用现有 `expense_invoice_parser` | 已完成 | 只用 mock OCR 文本，不跑 OCR/上传票据 |
| 管理 | `contract_section_review_candidate` | 暂缓/高风险，许可证与法律边界不清 | 已完成 | 只用 mock 合同文本，不读真实合同、不做法律意见 |

## 测试台建议

| 类型 | 候选 |
| --- | --- |
| 无需重复 L2，可使用现有已验收 Skill | `operations_metric_brief_candidate`, `support_reply_flow_candidate`, `invoice_receipt_review_candidate` |
| 可优先由现有 Skill 组合覆盖 | `product_listing_copy_candidate`, `complaint_escalation_summary_candidate` |
| 等待 L1 后可进入模板化 mock L2 | `visual_prompt_brief_candidate`, `sales_followup_draft_candidate`, `sales_meeting_task_brief_candidate`, `lead_research_brief_candidate`, `competitor_product_snapshot_candidate`, `order_inventory_exception_candidate`, `support_quality_eval_candidate`, `hr_resume_privacy_masker_candidate` |
| 仅作线索/组件或暂缓 | `storyboard_script_brief_candidate`, `brand_consistency_check_candidate`, `content_calendar_planner_candidate`, `feedback_cluster_insights_candidate`, `contract_section_review_candidate` |

## 指挥中心判定

- 本回传已收录为模板预案结果。
- 不是正式 L2 测试结果。
- 不新增客户可调用 Skill。
- 下一步等待许可证复核窗口回传 L1 结果，再决定哪些候选进入正式 L2 simulated。
