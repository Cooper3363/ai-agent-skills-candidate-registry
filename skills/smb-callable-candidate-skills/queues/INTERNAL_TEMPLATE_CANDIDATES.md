# 内部模板候选队列

更新时间：2026-06-03

## 当前候选

| candidate_id | 来源路线 | 业务包 | 建议下一步 | 复用能力 |
| --- | --- | --- | --- | --- |
| `support_quality_eval_candidate` | 内部客服质检评测模板，不再依赖 `awesome-copilot` | 客服 | 设计 mock smoke / L2 模板；如通过再封装为候选或组合能力 | `support_reply_guardrail`, `support_ticket_classifier`, `support_pii_redactor` |

## 边界

- 只评测 mock 客服对话、客服回复和政策片段。
- 不写质检系统。
- 不联系客户。
- 不自动处罚客服人员。
- 不保留未脱敏 PII。
- 只输出评分、失败项、风险标签、培训建议和人工复核触发。
