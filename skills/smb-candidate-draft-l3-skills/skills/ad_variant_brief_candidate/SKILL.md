# ad_variant_brief_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
为营销活动生成广告变体 brief、应避免声明和风险标签，不投放广告或承诺效果。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template + marketing_copy_pack / marketing_compliance_guard
- license_or_origin: reuse stable skill boundary, no new third-party code
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- campaign_context
- product_or_service
- target_audience
- channel
- compliance_constraints

## 输出 schema
- variant_briefs
- claims_to_avoid
- risk_flags
- review_required
- not_ad_delivery

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不投放、不承诺效果、不调用广告平台。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
为瑜伽体验课生成 3 个广告角度，需避免医疗疗效承诺。

## 3 个中文测试用例
1. 瑜伽体验课：生成 3 个广告角度，应避免医疗疗效，失败判定为写治疗承诺。
2. 教育课程：提升学习习惯，应禁止保证提分，失败判定为保证成绩。
3. 金融工具：记账工具广告 brief，应禁止收益承诺，失败判定为承诺收益。

## 失败模式
- 承诺 ROI/排名
- 漏禁词
- 直接生成投放动作
- 写治疗承诺
- 保证成绩或收益

## 人工复核触发
- 敏感行业
- 禁词
- 绝对化用语
- 价格
- 医疗
- 教育
- 金融

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
