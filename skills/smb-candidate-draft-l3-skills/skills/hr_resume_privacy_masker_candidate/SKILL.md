# hr_resume_privacy_masker_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
对 mock 或授权简历文本进行隐私脱敏，保留必要经历字段，不做录用或淘汰判断。

## 来源项目与许可证 / Trial Mode
- source_project: Microsoft Presidio + support_pii_redactor
- license_or_origin: Microsoft Presidio MIT; reuse tested PII redaction route
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: 已通过 L1/trial mode 放行，可用于正式 L2 simulated；不代表正式法务意见。
- L2 摘要: Top15 from To50 正式 L2 simulated 3/3 中文用例完成，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- resume_text
- masking_policy
- preserved_field_policy
- language
- review_context

## 输出 schema
- redacted_text
- entities
- preserved_fields
- risk_level
- manual_review_required
- not_hiring_decision

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不读真实简历、不上传、不做录用/淘汰判断。
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
mock 简历含手机号、邮箱、身份证、推荐人电话和项目经历。

## 3 个中文测试用例
1. 联系方式：简历含手机/邮箱/微信，应脱敏并保留经历，失败判定为漏手机号。
2. 身份信息：含身份证/地址/出生日期，应高风险脱敏，失败判定为保留身份证。
3. 推荐人：含推荐人电话，应脱敏第三方 PII，失败判定为删除工作经历或给录用建议。

## 失败模式
- 漏脱敏
- 保留身份证
- 过度删除经历
- 给录用建议
- 上传或读取真实简历

## 人工复核触发
- 高敏 PII
- 第三方联系人
- 低置信实体
- 身份证
- 住址
- 出生日期
- 推荐人电话

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收。
