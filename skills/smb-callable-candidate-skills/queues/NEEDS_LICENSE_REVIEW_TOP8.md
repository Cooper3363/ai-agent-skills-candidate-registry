# 待许可证复核 Top 8

来源：`RESEARCH_TOP18_RESULT.md`

更新时间：2026-06-03

## 复核队列

| candidate_id | source_type | source_url | 复核重点 | 默认 trial mode 建议 |
| --- | --- | --- | --- | --- |
| `support_quality_eval_candidate` | GitHub | `https://github.com/github/awesome-copilot` | 是否只是索引；可封装上游；LICENSE/SPDX | `mock_only` |
| `complaint_escalation_summary_candidate` | GitHub | `https://github.com/anthropics/knowledge-work-plugins` | LICENSE、插件依赖、投诉/知识工作边界 | `mock_only` |
| `support_reply_flow_candidate` | GitHub | `https://github.com/asgard-ai-platform/skills` | LICENSE、是否可独立封装、与客服稳交付包重叠 | `mock_only` |
| `product_listing_copy_candidate` | GitHub | `https://github.com/agricidaniel/claude-seo --skill` | 链接纠错、LICENSE、SEO 承诺风险 | `mock_only` |
| `order_inventory_exception_candidate` | GitHub | `https://github.com/claude-office-skills/skills` | LICENSE、文件读写权限、订单/库存 Skill 粒度 | `read_only` |
| `operations_metric_brief_candidate` | GitHub | `https://github.com/anthropics/skills` | LICENSE、与稳交付报表包重叠、是否仅示例 | `mock_only` |
| `ecommerce_metric_brief_candidate` | GitHub | `https://github.com/astronomer/agents` | LICENSE、是否大型框架、可裁剪性 | `mock_only` |
| `hr_resume_privacy_masker_candidate` | GitHub | `https://github.com/anthropics/skills` | LICENSE、HR PII、脱敏能力是否可独立封装 | `mock_only` |

## 统一边界

- 不直接送正式 L2。
- 许可证窗口先给 L1 结论和 trial mode。
- 大合集、索引、聚合项目必须定位具体子 skill 或真实上游。
- 与 13 个稳交付 Skill 高度重复的候选，优先记录复用关系，不重复封装。
