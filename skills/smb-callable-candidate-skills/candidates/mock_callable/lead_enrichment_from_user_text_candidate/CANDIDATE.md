# lead_enrichment_from_user_text_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 销售跟进助手包
- roles: 销售代表
- scenario: 基于用户提供文本补全线索

## 来源与许可证 / Trial Mode
- source_project: internal_template
- license_or_origin: internal_template，无第三方代码
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: 用户粘贴客户简介和沟通记录
- 预期输出字段: enriched_lead_profile, inferred_needs, confidence, missing_info

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- enriched_lead_profile
- inferred_needs
- confidence
- missing_info

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不搜索
- 不调用 enrichment API

## 人工复核触发
- 低置信推断
- 隐私信息

## 复用 / 重复关系
与 lead research 相邻但无外网，适合作为组件

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
