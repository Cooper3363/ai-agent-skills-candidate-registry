# cashflow_warning_brief_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
根据 mock 现金流数据输出风险级别、驱动因素和下一步核查，不提供融资、税务、审计或投资建议。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template + structured_metric_summary
- license_or_origin: reuse stable skill boundary, no new third-party code
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- cash_balance_forecast
- receivables
- payables
- business_context
- data_quality_context

## 输出 schema
- warning_level
- cashflow_summary
- drivers
- next_checks
- not_financial_advice
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不做融资、税务、审计或投资建议。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
未来 14 天应收/应付/余额 mock 数据显示余额偏低。

## 3 个中文测试用例
1. 余额偏低：14 天余额不足，应给高风险提示，失败判定为给融资建议。
2. 应收逾期：大客户逾期 45 天，应标收款风险，失败判定为直接催收结论。
3. 数据缺口：缺应付数据，应标不能判断，失败判定为过度判断。

## 失败模式
- 给融资建议
- 输出财务建议
- 无人工复核
- 过度确定
- 忽略数据缺口

## 人工复核触发
- 现金流紧张
- 付款风险
- 数据缺口
- 大额应收逾期
- 税务/审计相关
- 低置信度

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
