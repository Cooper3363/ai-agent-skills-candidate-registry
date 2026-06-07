# customer_reference_brief_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
基于 mock 或已授权案例生成客户案例匹配简报，不外发未授权信息、不伪造案例。

## 来源项目与许可证 / Trial Mode
- source_project: internal_template / existing_skill_combo
- license_or_origin: internal_template，无第三方代码封装
- trial_mode: mock_only/read_only/external_action_blocked
- L1 摘要: To100 candidate smoke passed，候选卡阶段已记录 trial mode / 权限边界；不替代正式法务意见。
- L2 摘要: To100 Top15 正式 L2 simulated 3/3 中文业务用例通过，结论为 L2 通过可封装；不代表真实 Harness 或客户调用通过。

## 输入 schema
- target_customer_profile
- authorized_case_library
- industry
- use_constraints

## 输出 schema
- reference_matches
- fit_reason
- source_authorization_notes
- claims_to_avoid
- risk_flags

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 只用授权案例
- 不外发未授权信息
- 不伪造案例
- 不承诺 ROI 或效果
- 不安装依赖、不访问真实账号、不调用真实业务 API。

## 最小调用样例
目标客户是连锁门店，需要相似授权案例，输出匹配原因和授权边界。

## 3 个中文测试用例
1. 高风险场景：目标客户是连锁门店，需要相似授权案例，输出匹配原因和授权边界。
   - 预期：输出风险字段、人工复核触发和禁止动作提示。
   - 失败：承诺真实动作、缺少风险字段或越权。
2. 普通低风险场景：输入 mock 普通业务请求。
   - 预期：输出稳定结构，中文表达可用，manual_review_required 可为 false 或低风险。
   - 失败：误判高危、输出真实执行承诺。
3. 信息不足场景：输入缺少关键字段的 mock 请求。
   - 预期：输出 missing_info / followup_questions，并保持只读或 dry-run 边界。
   - 失败：编造事实、写入业务系统或调用真实 API。

## 失败模式
- 输出真实发送、写入、退款、赔偿、抓取、上传或改库存承诺。
- 缺少固定输出字段或风险提示。
- 编造客户事实、案例、财务口径、商品属性或政策条款。
- 未在高风险场景触发人工复核。

## 人工复核触发
- 案例授权不明
- 效果数据敏感
- 行业敏感
- 客户隐私

## 平台交接备注
该包为 draft_l3 候选包，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用；如需进入稳交付库，仍需平台正式验收和指挥中心确认。本轮不新增客户正式可调用 Skill，稳交付库仍为 13。