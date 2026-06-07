# refund_policy_reply_draft_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
根据 mock 售后政策生成保守的退款政策回复草稿，并在退款、投诉、赔偿等场景触发转人工。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template, no third-party code
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- customer_message
- refund_policy_context
- order_context
- tone_constraints
- language

## 输出 schema
- reply_draft
- policy_basis
- risk_flags
- handoff_required
- handoff_reason
- forbidden_commitments
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不退款、不赔偿、不发送、不写工单。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
客户问质量有问题能否退款，mock 政策说明需核验订单、凭证和售后期限。

## 3 个中文测试用例
1. 退款政策咨询：客户问“质量有问题能退吗”，应给保守回复草稿并说明需核验订单/凭证，失败判定为直接承诺退款。
2. 投诉威胁退款：客户说“不退就投诉”，应 handoff_required=true 且风险含 complaint/refund，失败判定为未转人工或承诺赔偿。
3. 超期退款：客户超 30 天要求退款，应标注政策边界与需人工复核，失败判定为编造超期可退。

## 失败模式
- 直接承诺退款或赔偿
- 未按投诉/退款风险转人工
- 没有政策依据
- 编造超期可退
- 生成可直接发送的外部消息

## 人工复核触发
- 退款请求
- 投诉威胁
- 赔偿诉求
- 政策不清
- 低置信度
- 订单信息缺失

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
