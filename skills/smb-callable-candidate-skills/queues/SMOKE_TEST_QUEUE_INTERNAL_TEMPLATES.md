# 内部模板候选 Smoke Test 队列

来源：`SUPPORT_QUALITY_EVAL_TEMPLATE_PREPLAN.md`

更新时间：2026-06-03

## 待 Smoke Test

| candidate_id | 定位 | smoke 目标 | 下一步 |
| --- | --- | --- | --- |
| `support_quality_eval_candidate` | 内部客服质检评测模板候选 | 验证 mock 客服对话是否能稳定输出评分、失败项、风险标签、培训建议、人工复核触发，并且不保留未脱敏 PII | smoke 通过后再决定是否正式 L2 |

## 边界

- 不写质检系统。
- 不联系客户。
- 不自动处罚客服人员。
- 不保留未脱敏 PII。
- 优先复用现有客服稳交付包能力。
