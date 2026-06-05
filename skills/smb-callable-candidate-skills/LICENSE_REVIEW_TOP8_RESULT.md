# Top 8 L1 许可证与 Trial Mode 复核结果

回传时间：2026-06-03

## 总结

| 结论 | 数量 | 候选 |
| --- | ---: | --- |
| 可送正式 L2 simulated | 2 | `complaint_escalation_summary_candidate`, `product_listing_copy_candidate` |
| 需补资料 | 3 | `support_quality_eval_candidate`, `order_inventory_exception_candidate`, `hr_resume_privacy_masker_candidate` |
| 只作线索 / 复用稳交付 | 3 | `support_reply_flow_candidate`, `operations_metric_brief_candidate`, `ecommerce_metric_brief_candidate` |

## 复核结果表

| candidate_id | source_project | license | commercial_use_notes | maintenance_status | dependency_risks | trial_mode | l1_result | 建议动作 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `support_quality_eval_candidate` | `github/awesome-copilot` | MIT；仓库本体 MIT，但 README 提醒资源来自第三方开发者，需逐项检查 | 社区索引/合集，不等于具体可封装 Skill 授权 | 活跃 | 第三方 skills/plugins/MCP 上游不统一；质检评测上游未定位 | `mock_only`, `read_only`, `external_action_blocked` | 需补资料 | 定位具体上游或自研评测模板后重走 L1；当前不得送正式 L2 |
| `complaint_escalation_summary_candidate` | `anthropics/knowledge-work-plugins` | Apache-2.0 | README 无额外商用限制；投诉/退款/赔偿必须人工复核 | 活跃 | 插件形态，可能依赖 Claude/Cowork 工作流；不得回访、不得发送、不得退款处理 | `mock_only`, `read_only`, `external_action_blocked` | 可送 L2 | 送正式 L2 simulated；只处理 mock 投诉文本并输出摘要/转人工原因 |
| `support_reply_flow_candidate` | `asgard-ai-platform/skills` | MIT | 无明显商用限制；但 301 skills 大合集，需拆具体客服 skill | 一般/活跃 | 与 `faq_answer_with_citations`、`support_ticket_classifier` 高度重叠；部分脚本/领域方法需逐项看 | `mock_only`, `read_only`, `external_action_blocked` | 只作线索 | 优先复用稳交付客服包，不重复封装 |
| `product_listing_copy_candidate` | `agricidaniel/claude-seo` | MIT；原链接需纠错为 `https://github.com/agricidaniel/claude-seo` | 无明显商用限制；不得承诺 SEO 排名或广告效果 | 活跃 | DataForSEO、Firecrawl、Google APIs、PDF/Excel 报告、图片扩展；L2 必须禁用外部 API | `mock_only`, `read_only`, `external_action_blocked`, `BYOK_required` | 可送 L2 | 送正式 L2 simulated；只生成商品标题/卖点草稿，不调用 SEO/API |
| `order_inventory_exception_candidate` | `claude-office-skills/skills` | 总体 MIT；README 明确 individual skills may have different licenses | 子 skill 许可证可能不同，不能整仓通过 | 一般 | Office MCP、Excel 读写、库存/表格权限；真实写库存系统必须禁止 | `mock_only`, `read_only`, `external_action_blocked` | 需补资料 | 研究窗口需定位具体订单/库存子 skill；补齐后重走 L1 |
| `operations_metric_brief_candidate` | `anthropics/skills` | 不宜整仓通过；README 称很多 skills Apache-2.0，但 docx/pdf/pptx/xlsx 为 source-available | 官方说明部分内容仅示例/教育用途；与稳交付报表包重叠 | 活跃 | 文档/报表 skills 授权不统一；经营数据敏感 | `mock_only`, `read_only`, `external_action_blocked` | 只作线索 | 复用 `daily_weekly_metrics_reporter`、`structured_metric_summary`、`metric_exception_classifier` |
| `ecommerce_metric_brief_candidate` | `astronomer/agents` | Apache-2.0 | 无明显商用限制 | 活跃 | Airflow/MCP/数据仓库连接，偏大型数据工程框架；真实数据源连接禁止 | `mock_only`, `read_only`, `external_action_blocked`, `BYOK_required` | 只作线索 | 复用稳交付经营报表包；Astronomer 仅组件观察 |
| `hr_resume_privacy_masker_candidate` | `anthropics/skills` | 不宜整仓通过；部分 Apache-2.0、部分 source-available | HR PII 高敏；需确认具体脱敏子 skill 授权 | 活跃 | 简历/人事材料隐私；不得上传真实简历，不得做招聘录用判断 | `mock_only`, `read_only`, `external_action_blocked` | 需补资料 | 研究窗口需拆到具体 HR/PII 子 skill；当前优先复用 `support_pii_redactor` 方向 |

## 指挥中心下一步

- 正式 L2 simulated 队列：`complaint_escalation_summary_candidate`, `product_listing_copy_candidate`。
- 研究补资料队列：`support_quality_eval_candidate`, `order_inventory_exception_candidate`, `hr_resume_privacy_masker_candidate`。
- 复用/线索队列：`support_reply_flow_candidate`, `operations_metric_brief_candidate`, `ecommerce_metric_brief_candidate`。
