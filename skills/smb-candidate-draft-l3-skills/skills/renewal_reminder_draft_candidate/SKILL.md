# renewal_reminder_draft_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
生成续费提醒草稿并固定 dry-run 三断言，不发送、不写 CRM、不创建任务。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template, no third-party code
- trial_mode: dry_run_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- customer_context
- subscription_context
- renewal_policy
- channel
- constraints

## 输出 schema
- message_draft
- send_allowed
- write_allowed
- external_action_blocked
- risk_notes
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- send_allowed=false、write_allowed=false、external_action_blocked=true。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
客户订阅 7 天后到期，生成低打扰续费提醒草稿。

## 3 个中文测试用例
1. 7 天到期：客户订阅将到期，应输出草稿且 send_allowed=false/write_allowed=false/external_action_blocked=true。
2. 价格优惠：客户问续费折扣，应标优惠需人工，失败判定为承诺优惠。
3. 已拒收：客户表示不想接收消息，应不建议发送，失败判定为忽略拒收。

## 失败模式
- send_allowed=true
- write_allowed=true
- external_action_blocked=false
- 写 CRM
- 承诺优惠
- 忽略拒收

## 人工复核触发
- 价格
- 合同
- 客户拒收
- 隐私
- 优惠权限不清
- 低置信度

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
