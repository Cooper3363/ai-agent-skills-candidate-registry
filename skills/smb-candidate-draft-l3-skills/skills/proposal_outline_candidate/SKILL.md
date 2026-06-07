# proposal_outline_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
根据客户需求生成售前方案书大纲、章节、假设和缺失信息，不生成合同或承诺报价交付。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template, no third-party code
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- customer_needs
- business_context
- solution_context
- constraints
- language

## 输出 schema
- outline
- sections
- assumptions
- missing_info
- risk_notes
- not_contract

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不生成合同、不承诺报价/交付。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
教培客户需要排课、签到、学员管理方案，要求输出方案书大纲。

## 3 个中文测试用例
1. 教培方案：排课、签到、学员管理，应输出方案书章节，失败判定为写成合同。
2. 批发进销存：库存、欠款、老板日报，应输出业务方案大纲，失败判定为承诺价格。
3. 装修 CRM：客户跟进、阶段管理，应标缺失信息，失败判定为过度承诺实施周期。

## 失败模式
- 把大纲写成合同
- 承诺价格
- 过度承诺实施周期
- 遗漏关键缺失信息
- 输出签署建议

## 人工复核触发
- 合同
- 报价
- 实施周期
- 定制开发
- 交付承诺
- 信息缺失

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
