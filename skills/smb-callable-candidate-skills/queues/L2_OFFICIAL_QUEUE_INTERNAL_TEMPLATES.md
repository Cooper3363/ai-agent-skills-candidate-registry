# 内部模板正式 L2 队列

来源：`SUPPORT_QUALITY_EVAL_SMOKE_RESULT.md`

更新时间：2026-06-03

## 待正式 L2 simulated

| candidate_id | 定位 | L2 边界 | 默认封装方向 |
| --- | --- | --- | --- |
| `support_quality_eval_candidate` | 客服质检组合模板 | 只评测 mock 客服对话、客服回复和 policy snippets；不写系统、不处罚客服、不保留未脱敏 PII | 组件或组合能力，不作为独立第三方 Skill |

## 必测用例

- 退款/赔偿承诺。
- 账号安全绕验证。
- PII 暴露。
- 正常回复避免误杀。

## 统一禁止

- 不写质检系统。
- 不联系客户。
- 不自动处罚客服人员。
- 不保留未脱敏 PII。
- 不安装依赖。
- 不访问外网。
- 不调用真实 API。
