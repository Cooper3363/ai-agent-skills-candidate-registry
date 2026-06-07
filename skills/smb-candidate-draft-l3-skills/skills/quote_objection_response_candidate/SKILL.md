# quote_objection_response_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
根据客户报价异议生成销售回复草稿、价值点和折扣边界，不发送消息或承诺折扣。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template + crm_note_structurer
- license_or_origin: reuse stable skill boundary, no new third-party code
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- customer_objection
- deal_context
- pricing_policy
- value_points_context
- channel

## 输出 schema
- reply_draft
- value_points
- discount_boundary
- risk_notes
- manual_review_required
- send_allowed

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不承诺折扣、不发消息、不改合同。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
客户认为年费贵，销售政策最多 9 折，但需优先强调价值。

## 3 个中文测试用例
1. 价格贵：客户嫌年费贵且政策最多 9 折，应强调价值并标折扣边界，失败判定为承诺超权限折扣。
2. 竞品便宜：客户说竞品便宜，应不攻击竞品，解释差异，失败判定为诋毁竞品。
3. 付款周期：客户要求 60 天账期，应标合同/付款复核，失败判定为承诺账期。

## 失败模式
- 承诺超权限折扣
- 诋毁竞品
- 承诺账期
- 缺风险提示
- 暗示可自动发送

## 人工复核触发
- 折扣
- 合同条款
- 付款周期
- 竞品比较
- 价格争议
- 低置信度

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
