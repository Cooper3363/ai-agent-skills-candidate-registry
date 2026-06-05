# support_quality_eval_candidate Smoke Test 结果

回传时间：2026-06-03

## 结论

Smoke 结论：仅组件或组合能力。

`support_quality_eval_candidate` 不应作为独立第三方 Skill 直接封装，应定位为客服质检组合模板，复用现有稳交付客服包能力：

- `support_reply_guardrail`
- `support_ticket_classifier`
- `support_pii_redactor`

## Smoke 表

| 候选 | mock 输入摘要 | 预期输出字段 | 输出结构稳定性 | 中文可用性 | 与 13 个稳交付 Skill 是否重复 | 权限边界 | 人工复核触发 | Smoke 结论 | 建议下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `support_quality_eval_candidate` | mock 客服对话、客服回复、政策片段；覆盖退款承诺、账号安全、PII 暴露、正常发票回复 | `overall_score`, `score_breakdown`, `failed_checks`, `risk_flags`, `training_notes`, `handoff_recommendation`, `pii_redaction_notes`, `manual_review_required`, `not_employee_disciplinary_action` | 高 | 高 | 高度依赖现有客服包，但有“评分+培训建议”增量 | 只读 mock 对话；不写质检系统；不联系客户；不处罚客服；不保留未脱敏 PII | 退款、赔偿、投诉、账号安全、隐私暴露、低分、高风险 | 仅组件或组合能力 | 可进入正式 L2 simulated，但按组合模板测试，不作为独立第三方 Skill |

## 关键风险

- 不能只评价客服语气，必须评价政策合规和安全边界。
- 质检报告不得保留完整手机号、地址、订单号、身份证等 PII。
- 输出必须包含 `not_employee_disciplinary_action=true`，不能自动演变为处罚建议。
- 不应替代现有客服包，应作为质检评分和培训建议汇总层。
- 正式 L2 需要保留正常回复用例，避免误杀。

## 下一步

进入正式 L2 simulated，但按“客服质检组合模板”定位测试。即使 L2 通过，默认也进入组件/组合能力池，不直接作为独立客户可调用 Skill。
