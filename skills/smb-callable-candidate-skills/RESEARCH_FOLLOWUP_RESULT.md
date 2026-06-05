# Top 8 补资料研究结果

回传时间：2026-06-03

## 总结

本轮针对 L1 标为“需补资料”的 3 个候选做了具体上游/子 skill 定位：

| candidate_id | 补资料结论 | 建议下一步 |
| --- | --- | --- |
| `support_quality_eval_candidate` | 未在 `github/awesome-copilot` 定位到客服质检子 Skill；仅找到偏代码质量的 `quality-playbook` | 改为内部客服质检评测模板候选，或复用客服稳交付包 |
| `order_inventory_exception_candidate` | 找到 `claude-office-skills/skills` 下的 `shopify-automation` 子 Skill | 以具体子 Skill 重走 L1；只允许 mock/dry-run/read-only |
| `hr_resume_privacy_masker_candidate` | 未在 `anthropics/skills` 定位到 HR/PII 子 Skill | 放弃 Anthropic 上游，改走 Presidio / `support_pii_redactor` 复用路线 |

## 详细结果

| candidate_id | 找到的具体上游/子 skill | source_url | license 线索 | 业务价值 | 权限边界 | 是否建议重走 L1 | 是否建议复用稳交付 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `support_quality_eval_candidate` | 未找到客服质检子 Skill；仅找到 `quality-playbook`，偏代码质量审计，不是客服场景 | `https://github.com/github/awesome-copilot`, `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/quality-playbook/SKILL.md` | 总仓库 MIT，但具体客服质检上游缺失 | 客服对话质检、培训建议、风险标注 | 只读客服对话文本；不联系客户、不写工单、不保留 PII | 以 awesome-copilot 来源不建议；以内部模板建议 | 是，复用 `support_reply_guardrail`、`support_ticket_classifier`、`support_pii_redactor` |
| `order_inventory_exception_candidate` | 找到 `shopify-automation`；可补充参考 `woocommerce-automation`、`amazon-seller` | `https://raw.githubusercontent.com/claude-office-skills/skills/main/shopify-automation/SKILL.md` | repo MIT；`shopify-automation` frontmatter 标 MIT | 低库存、缺货、订单异常、库存周转提醒 | mock/dry-run；禁用真实 API、库存更新、采购单、Slack/邮件通知 | 建议，以 `shopify-automation` 具体子 Skill 重走 L1 | 部分复用报表 3 件套，但库存/订单异常是新增能力 |
| `hr_resume_privacy_masker_candidate` | `anthropics/skills` 未找到 HR/PII 子 Skill；建议改用 Microsoft Presidio | `https://github.com/anthropics/skills`, `https://github.com/microsoft/presidio` | Anthropic skills 授权不统一，部分 source-available；Presidio 为 MIT | 简历/候选人材料脱敏，降低 HR PII 外泄 | 只处理 mock 或授权文本；不上传真实简历；不做录用/淘汰判断 | 以 Anthropic 来源不建议；以 Presidio 路线建议 | 强烈建议复用 `support_pii_redactor`，做 HR 场景包装 |

## 指挥中心处理

- `support_quality_eval_candidate`：进入内部模板路线，先做候选 smoke/L2 模板，不再依赖 awesome-copilot 上游。
- `order_inventory_exception_candidate`：进入补充 L1 队列，来源改为具体 `shopify-automation` 子 Skill。
- `hr_resume_privacy_masker_candidate`：进入补充 L1 队列，来源改为 Microsoft Presidio / 已有 PII 脱敏路线。
