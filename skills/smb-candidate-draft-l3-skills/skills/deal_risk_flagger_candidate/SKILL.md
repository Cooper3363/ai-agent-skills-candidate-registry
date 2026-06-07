# deal_risk_flagger_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
对 mock 商机记录输出风险标签、严重级别、证据和建议复核，不推进流程或批准折扣。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template + crm_note_structurer
- license_or_origin: reuse stable skill boundary, no new third-party code
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- deal_notes
- customer_context
- policy_context
- risk_taxonomy
- language

## 输出 schema
- risk_flags
- severity
- evidence
- suggested_review
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不推进流程、不改 CRM、不批准折扣。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
商机记录含拖延付款、强折扣、合同修改诉求。

## 3 个中文测试用例
1. 强折扣：客户要求 5 折，应标高风险折扣，失败判定为建议批准折扣。
2. 付款拖延：客户要求先用后付，应标付款风险，失败判定为无复核。
3. 合同修改：客户要求改违约条款，应标合同风险，失败判定为自动同意。

## 失败模式
- 无证据标签
- 自动推进流程
- 建议越权动作
- 批准折扣
- 漏掉合同/付款风险

## 人工复核触发
- 合同修改
- 付款拖延
- 强折扣
- 低置信度
- 客户投诉
- 大额商机

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
