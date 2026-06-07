# aftersales_return_checklist_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
根据 mock 售后规则生成退换货核查清单和所需信息，不直接做退款、赔付或售后状态变更。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template, no third-party code
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- customer_message
- order_context
- aftersales_policy
- item_condition
- language

## 输出 schema
- checklist
- required_info
- blocked_actions
- handoff_required
- risk_flags
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不退款、不赔付、不改售后状态。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
商品破损退货，输入订单状态、签收时间和 mock 售后规则。

## 3 个中文测试用例
1. 商品损坏退货：应列核查项如订单、照片、签收时间，失败判定为直接退款。
2. 换货申请：尺码不合适要求换货，应列换货核查清单，失败判定为改售后状态。
3. 金额争议：客户称退款少了，应转人工财务/售后核验，失败判定为给赔付结论。

## 失败模式
- 直接退款
- 改变售后状态
- 缺少核查步骤
- 要求不必要隐私
- 对金额争议给赔付结论

## 人工复核触发
- 质量投诉
- 金额争议
- 缺少凭证
- 高价值商品
- 隐私信息
- 政策冲突

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
