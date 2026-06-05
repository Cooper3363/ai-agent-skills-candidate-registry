# Top 8 放行后的正式 L2 队列

来源：`LICENSE_REVIEW_TOP8_RESULT.md`

更新时间：2026-06-03

## 可送正式 L2 simulated

| candidate_id | business_package | trial_mode | L2 边界 | 禁止动作 |
| --- | --- | --- | --- | --- |
| `complaint_escalation_summary_candidate` | 客服 | `mock_only`, `read_only`, `external_action_blocked` | 只处理 mock 投诉文本，输出投诉摘要、风险等级、转人工原因和下一步安全建议 | 不回访、不发送、不退款、不承诺赔偿、不写客服系统 |
| `product_listing_copy_candidate` | 电商/门店 | `mock_only`, `read_only`, `external_action_blocked`, `BYOK_required` | 只生成商品标题、卖点、详情页文案草稿和平台/SEO 风险提示 | 不调用 DataForSEO、Firecrawl、Google API，不上传商品，不承诺排名 |

## 正式 L2 要求

- 每个候选至少 3 个中文业务用例。
- 固定输入输出 schema。
- 明确失败判定、权限边界、人工复核触发。
- 结论只能为：L2 通过可封装、需补测、暂缓、未通过、仅组件。
- 本轮不安装依赖、不访问外网、不读取真实客户文件、不调用真实 API、不发送、不写入、不抓取、不生成真实媒体/OCR/PDF/音频结果。
