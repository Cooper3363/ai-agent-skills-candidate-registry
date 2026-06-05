# contract_renewal_date_extractor_candidate

## 当前状态
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_queued
- deepagents_smoke_status: passed
- count_towards_100: true

## 业务包、角色、场景
- business_package: 采购行政包
- roles: 行政/法务支持
- scenario: 合同续约日期抽取

## 来源与许可证 / Trial Mode
- source_project: GitHub: dateparser/dateparser 或内部日期规则模板
- license_or_origin: dateparser 为 BSD-3-Clause；也可改内部规则实现规避依赖
- trial_mode: mock_only, read_only, external_action_blocked
- l1_result: can_mock_smoke
- deepagents_trial_fit: mock_candidate_smoke_fit

## 中文 smoke 用例
- 输入摘要: mock 合同片段含到期日、自动续约条款
- 预期输出字段: renewal_dates, confidence, source_spans, not_legal_advice, review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy

## 输出字段
- renewal_dates
- confidence
- source_spans
- not_legal_advice
- review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不写日历/任务
- 不做法律意见

## 人工复核触发
- 日期解析错误
- 合同敏感

## 复用 / 重复关系
可试跑，L3 前需锁定实现依赖

## 下一步动作
保留在候选库继续试跑或等待后续业务包补位。
