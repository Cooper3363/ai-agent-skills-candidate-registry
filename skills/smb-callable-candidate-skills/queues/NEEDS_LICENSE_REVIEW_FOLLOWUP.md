# 补资料后待 L1 复核队列

来源：`RESEARCH_FOLLOWUP_RESULT.md`

更新时间：2026-06-03

## 待复核对象

| candidate_id | source_project | source_url | 复核重点 | 默认 trial mode |
| --- | --- | --- | --- | --- |
| `order_inventory_exception_candidate` | `claude-office-skills/skills/shopify-automation` | `https://raw.githubusercontent.com/claude-office-skills/skills/main/shopify-automation/SKILL.md` | 子 Skill 许可证、Shopify API/库存更新/通知动作风险、是否可 mock/dry-run | `mock_only`, `read_only`, `external_action_blocked` |
| `hr_resume_privacy_masker_candidate` | `microsoft/presidio` + existing `support_pii_redactor` route | `https://github.com/microsoft/presidio` | Presidio 许可证、中文 HR PII 规则、与已测 PII 脱敏能力复用关系 | `mock_only`, `read_only`, `external_action_blocked` |

## 不再按原上游推进

| candidate_id | 原上游 | 处理 |
| --- | --- | --- |
| `support_quality_eval_candidate` | `github/awesome-copilot` | 未定位到客服质检上游；改为内部模板/客服稳交付组合路线 |
| `hr_resume_privacy_masker_candidate` | `anthropics/skills` | 未定位到 HR/PII 子 Skill；不再按 Anthropic 整仓推进 |

## 统一边界

- 不安装依赖。
- 不运行真实工具。
- 不读取真实客户文件。
- 不写库存系统。
- 不上传真实简历。
- 不做招聘录用/淘汰判断。
- 不输出财务、法务或 HR 决策结论。
