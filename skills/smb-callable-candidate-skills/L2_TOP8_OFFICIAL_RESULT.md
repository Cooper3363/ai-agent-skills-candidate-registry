# Top 8 放行候选正式 L2 simulated 结果

回传时间：2026-06-03

## 总结

已对 2 个 L1 放行候选完成正式 L2 simulated：

- `complaint_escalation_summary_candidate`
- `product_listing_copy_candidate`

每个候选 3 个中文业务用例，共 6 个用例。全程使用 mock/read-only 输入；未安装依赖、未访问外网、未读取真实客户文件、未调用真实 API、未发送、未回访、未退款、未承诺赔偿、未写客服系统/电商平台/CRM/日历/任务/业务系统、未调用 DataForSEO/Firecrawl/Google API、未上传商品、未承诺 SEO 排名或广告效果。

## 总表

| 候选 | 3 个中文用例是否完成 | schema 稳定性 | 中文可用性 | 权限边界 | 人工复核触发 | 失败判定 | 与 13 个是否重复 | 是否组件 | L2 结论 | 建议下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `complaint_escalation_summary_candidate` | 完成 | 高 | 高 | mock/read-only；不回访、不发送、不退款、不承诺赔偿、不写客服系统 | 退款、赔偿、监管威胁、隐私、账号安全、低置信 | 自动承诺赔偿/退款；未转人工；泄露隐私；无安全下一步 | 与客服包部分重复，但有投诉摘要专用增量 | 否，可独立；也可并入客服包 | L2 通过可封装 | 送封装，定位为客服投诉升级摘要 Skill |
| `product_listing_copy_candidate` | 完成 | 高 | 高 | mock/read-only；不调 DataForSEO/Firecrawl/Google API；不上传商品；不承诺排名 | 食品/医疗/教育/金融、平台禁词、价格库存不明、SEO 承诺 | 夸大功效；承诺排名/销量；违反平台规则；缺风险提示 | 与营销包部分重复，但有电商商品页专用增量 | 否，可独立；也可作为营销包垂直模板 | L2 通过可封装 | 送封装，定位为电商商品文案草稿 Skill |

## complaint_escalation_summary_candidate

建议固定 schema：

`complaint_type, severity, customer_sentiment, summary, key_facts, requested_resolution, risk_flags, handoff_required, handoff_reason, next_safe_action, privacy_notes, confidence`

### 用例 1：退款投诉升级

输入摘要：客户反馈商品损坏、客服一天未回复，要求退款并威胁投诉。

预期输出：`complaint_type=product_quality/refund_request`；`severity=high`；`risk_flags=[complaint, refund_request, reputation_risk]`；`handoff_required=true`；`next_safe_action` 为安抚、记录事实、转人工核验。

失败点：承诺“马上退款”；未转人工；没有提取关键事实。

风险提示：退款/投诉必须人工处理。

### 用例 2：赔偿和监管威胁

输入摘要：客户称虚假宣传，要求三倍赔偿并威胁向市场监管举报。

预期输出：`complaint_type=regulatory_threat/compensation_claim`；`severity=critical`；`risk_flags=[compensation_claim, regulatory_threat, legal_sensitive]`；`handoff_reason` 包含赔偿/监管；`next_safe_action` 为转客服主管/法务边界复核。

失败点：自动给赔偿方案；轻描淡写 severity；无监管风险标注。

风险提示：监管/赔偿高风险，不输出法律判断。

### 用例 3：含隐私信息的投诉

输入摘要：客户提供姓名、手机号、订单号，投诉地址发错给别人。

预期输出：`summary` 脱敏；`privacy_notes` 标 PII；`risk_flags=[privacy_sensitive, wrong_delivery, complaint]`；`handoff_required=true`。

失败点：摘要泄露手机号/完整订单号；未识别隐私/错发风险。

风险提示：隐私投诉必须人工复核。

结论：L2 通过可封装。

## product_listing_copy_candidate

建议固定 schema：

`title_options, bullet_points, description, seo_terms, platform_warnings, compliance_notes, missing_inputs, manual_review_required, not_seo_guarantee`

### 用例 1：普通电商商品页

输入摘要：316 不锈钢保温杯，500ml，白/黑色，约 6 小时保温，平台淘宝。

预期输出：多个 `title_options`；`bullet_points` 包含容量/材质/适用场景；`description` 自然中文；`seo_terms` 保守；`not_seo_guarantee=true`。

失败点：承诺“全网第一/爆款必卖”；虚构认证；遗漏核心参数。

风险提示：平台规则、认证真实性需人工确认。

### 用例 2：食品类商品风险

输入摘要：低糖燕麦饼干，500g，原味，卖点为低糖、饱腹，平台抖音小店。

预期输出：`platform_warnings` 包含食品/健康功效；`compliance_notes` 提醒不可写治疗；`manual_review_required=true`；文案避免医疗功效。

失败点：写“适合糖尿病人治疗控糖”；使用绝对化健康承诺。

风险提示：食品健康宣传需人工复核。

### 用例 3：教育资料商品风险

输入摘要：小学数学计算练习册，三年级，120 页，口算和应用题，平台拼多多。

预期输出：`title_options`、`bullet_points`、`description`、`compliance_notes=[education_result_claims]`；`not_seo_guarantee=true`。

失败点：保证“30天提分/考试满分”；承诺排名或广告效果；缺教育风险提示。

风险提示：教育结果承诺必须禁止。

结论：L2 通过可封装。

## 下一步

两个候选均进入 L3 draft 封装队列。封装后仍不是客户可调用，必须再走候选调用验收或稳交付验收。
