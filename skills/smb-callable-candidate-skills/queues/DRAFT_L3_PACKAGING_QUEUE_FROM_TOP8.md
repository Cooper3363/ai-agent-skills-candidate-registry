# Top 8 L2 通过候选 L3 Draft 封装队列

来源：`L2_TOP8_OFFICIAL_RESULT.md`

更新时间：2026-06-03

## 待封装对象

| candidate_id | 推荐定位 | L2 结论 | 强边界 |
| --- | --- | --- | --- |
| `complaint_escalation_summary_candidate` | 客服投诉升级摘要 Skill | L2 通过可封装 | 只摘要、分级、转人工建议；不回访、不发消息、不退款、不承诺赔偿 |
| `product_listing_copy_candidate` | 电商商品文案草稿 Skill | L2 通过可封装 | 只输出草稿和风险提示；不调用 SEO/API；不上传商品；不承诺 SEO 排名、销量或广告效果 |

## 封装要求

- 状态使用 `draft_l3`。
- 不进入稳交付库。
- 不标记客户可调用。
- 每个候选必须有 `SKILL.md`、`skill.yaml`、输入输出 schema、权限边界、L2 摘要、3 个中文测试用例、失败模式、人工复核触发和最小调用样例。
