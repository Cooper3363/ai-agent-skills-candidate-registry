# 研究补资料队列

来源：`LICENSE_REVIEW_TOP8_RESULT.md`

更新时间：2026-06-03

## 需补资料候选

| candidate_id | 来源项目 | 当前问题 | 研究窗口下一步 |
| --- | --- | --- | --- |
| `support_quality_eval_candidate` | `github/awesome-copilot` | awesome 索引，不是具体可封装 Skill | 定位具体客服质检上游资源，或建议自研评测模板后重走 L1 |
| `order_inventory_exception_candidate` | `claude-office-skills/skills` | 大合集，子 skill 许可证可能不同 | 定位具体订单/库存子 skill，确认权限边界后重走 L1 |
| `hr_resume_privacy_masker_candidate` | `anthropics/skills` | 整仓授权不统一，HR PII 高敏 | 拆到具体 HR/PII 子 skill，或建议复用 Presidio / support_pii_redactor 路线 |

## 统一要求

- 不送正式 L2。
- 不封装。
- 不客户调用。
- 定位不到真实上游或具体子 skill 时，保留为 `market_lead` 或复用稳交付能力。
