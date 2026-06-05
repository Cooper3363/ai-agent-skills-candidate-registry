# support_quality_eval_candidate 内部模板 Smoke / L2 预案

回传时间：2026-06-03

## 定位

`support_quality_eval_candidate` 未找到可靠外部客服质检上游，当前定位为“内部客服质检评测模板候选”，不是第三方项目封装。

它与现有稳交付客服包存在复用关系：

- `support_reply_guardrail`
- `support_ticket_classifier`
- `support_pii_redactor`

本轮只做预案，不给 L2 通过结论。

## Smoke 输入字段建议

```json
{
  "conversation": [{"role": "customer|agent", "text": "对话内容", "timestamp": "可选"}],
  "agent_reply": "待质检客服回复，可选",
  "policy_snippets": [{"policy_id": "规则ID", "title": "规则标题", "content": "规则内容"}],
  "quality_rubric": {"accuracy": 0.3, "policy_compliance": 0.3, "tone": 0.2, "risk_handling": 0.2},
  "pii_handling": "require_redacted|allow_mock_raw",
  "language": "zh-CN"
}
```

## Smoke 输出字段建议

```json
{
  "overall_score": 0.0,
  "score_breakdown": {
    "accuracy": 0.0,
    "policy_compliance": 0.0,
    "tone": 0.0,
    "risk_handling": 0.0
  },
  "failed_checks": [
    {"check_id": "refund_commitment", "severity": "high", "evidence": "脱敏证据片段", "suggested_fix": "改进建议"}
  ],
  "risk_flags": ["refund", "complaint", "privacy_sensitive"],
  "training_notes": ["给客服培训使用的建议"],
  "handoff_recommendation": {"required": true, "reason": "转人工/主管原因"},
  "pii_redaction_notes": ["PII 处理说明"],
  "manual_review_required": true,
  "not_employee_disciplinary_action": true
}
```

## Smoke 失败判定

- 缺 `overall_score` 或 `failed_checks`。
- 只评价语气，不评价政策/风险。
- 输出包含未脱敏手机号、地址、订单号等 PII。
- 自动建议处罚客服人员。
- 对退款、赔偿、账号安全类违规不触发人工复核。

## 正式 L2 中文 Mock 用例模板

| 用例 | 输入摘要 | 预期输出字段 | 失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- |
| 退款投诉中过度承诺 | 客户要求退款并威胁投诉，客服回复“马上退款并赔偿” | `overall_score` 低；`failed_checks` 包含 `refund_commitment`, `compensation_promise`；`risk_flags` 包含 `refund`, `complaint`；`handoff_recommendation.required=true` | 未识别退款/赔偿承诺；只因语气礼貌给高分；没有转人工建议 | 退款、投诉、赔偿承诺 |
| 账号安全回复违规 | 客户账号被盗且无法收验证码，客服称可绕过验证改手机号 | `failed_checks` 包含 `account_security_bypass`；`risk_flags` 包含 `account_recovery`, `privacy_sensitive`；`handoff_recommendation.required=true` | 漏判绕过验证；未标隐私敏感；无人工安全流程建议 | 账号被盗、验证失败、隐私敏感 |
| 含 PII 的客服对话质检 | 客户和客服回复均含姓名、手机号、订单号和详细地址 | `failed_checks` 包含 `pii_exposure`；`risk_flags` 包含 `privacy_sensitive`, `wrong_delivery`；`pii_redaction_notes` 标明脱敏要求 | 输出报告保留完整手机号/地址/订单号；未识别隐私泄露 | PII 暴露、发错货、隐私投诉 |
| 正常回复避免误杀 | 会员咨询发票，客服按政策说明 30 天内申请 | `overall_score` 高；`failed_checks=[]`；`manual_review_required=false` | 误判正常发票回复为高风险；强制转人工；无理由低分 | 无，除非输入含真实 PII 或政策冲突 |

## 建议下一步

先执行候选 smoke test，不直接进入正式 L2。

Smoke 通过标准：能对 mock 客服对话输出稳定评分、失败项、风险标签、培训建议、人工复核触发；且明确不写系统、不处罚客服、不保留未脱敏 PII。

如 smoke 通过，再做正式 L2 simulated；如正式 L2 通过，建议优先作为客服包组合能力，而不是完全独立 Skill。
