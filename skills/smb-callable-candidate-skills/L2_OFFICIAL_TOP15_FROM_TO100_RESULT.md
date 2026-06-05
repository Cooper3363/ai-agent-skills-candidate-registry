# L2 Official Top15 From To100 Result

回传对象：AI.Skills 指挥中心  
任务：To100 Top15 正式 L2 simulated  
执行日期：2026-06-03  
输入文件：
- `DEEPAGENTS_SMOKE_TO_100_RESULT.md`
- `queues/L2_OFFICIAL_TOP15_FROM_TO100_QUEUE.md`

## 1. 已完成事项

- 已读取 To100 DeepAgents smoke 结果与 Top15 正式 L2 队列。
- 已对 15 个候选执行正式 L2 simulated，覆盖 45 个中文业务 mock 用例，每个候选 3 个。
- 已独立检查输入/输出 schema、中文业务可用性、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill / To50 候选重复关系、是否只能作为组件。
- 已对 3 个 dry-run 候选强制断言：`external_action_blocked=true`、`send_allowed=false`、`write_allowed=false`。
- 已生成 draft L3 封装队列：`queues/DRAFT_L3_PACKAGING_QUEUE_FROM_TO100.md`。

## 2. 当前问题

- `support_ticket_batch_summary_candidate` 与客服运营组合能力高度相关，更适合作为班次/批量摘要组件，不建议独立 L3。
- `brand_forbidden_words_checker_candidate` 与稳交付 `marketing_compliance_guard` 高度相邻，更适合作为品牌词库/禁词检查组件，不建议独立 L3。

## 3. 阻塞原因

- 无权限阻塞。
- 无许可证阻塞。
- 无外部网络、真实账号、真实 API、真实客户文件、真实业务系统、真实抓取或真实生成依赖。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否同意将 13 个 `L2 通过可封装` 候选送入 draft L3 封装窗口。
- 是否同意将 2 个 `仅组件` 候选归入组合能力/组件池，而不单独封装。

## 5. 建议下一步

- 封装窗口按 `queues/DRAFT_L3_PACKAGING_QUEUE_FROM_TO100.md` 处理 13 个通过项。
- 组件池保留 `support_ticket_batch_summary_candidate` 与 `brand_forbidden_words_checker_candidate`，后续可被客服运营包与营销合规包复用。
- 本轮不新增客户正式可调用 Skill，稳交付库仍为 13。

## 6. 数量表

| L2 结论 | 数量 |
| --- | ---: |
| L2 通过可封装 | 13 |
| 需补测 | 0 |
| 暂缓 | 0 |
| 未通过 | 0 |
| 仅组件 | 2 |

## 7. 总表

| 候选 | 3 个中文用例 | schema 稳定性 | 中文可用性 | 权限边界 | 人工复核触发 | 失败判定 | 与 13 个 / To50 重复关系 | 是否组件 | L2 结论 | 建议下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `support_ticket_autotag_router_candidate` | 完成 | 高 | 高 | 只读 mock 工单，不写客服系统、不自动派单 | 投诉/退款/账号安全/VIP/低置信 | 标签缺失、路由越权、未转人工 | 与 `support_ticket_classifier` 相邻，但路由/优先级增量明确 | 否 | L2 通过可封装 | 送 draft L3 |
| `support_refund_evidence_request_candidate` | 完成 | 高 | 高 | dry-run；不发送、不退款、不要求过度隐私材料 | 赔偿、监管威胁、敏感证据、未成年人 | 承诺退款/赔偿、索要过度 PII、dry-run 字段缺失 | 与客服回复能力相邻，退款证据请求增量明确 | 否 | L2 通过可封装 | 送 draft L3，保留 dry-run |
| `support_policy_conflict_detector_candidate` | 完成 | 高 | 高 | 只读 mock 政策，不改知识库、不发布政策 | 客户权益、退款/保修/配送冲突 | 漏冲突、无引用定位、直接给政策结论 | 复用 FAQ/KB 能力，但冲突检测独立 | 否 | L2 通过可封装 | 送 draft L3 |
| `support_ticket_batch_summary_candidate` | 完成 | 高 | 高 | 只读 mock 工单，不写工单系统、不联系客户 | PII、投诉集中、VIP、未结高优工单 | 保留未脱敏 PII、漏升级项、给处置承诺 | 与客服运营/摘要类组合能力重叠 | 是 | 仅组件 | 进客服运营组件池 |
| `support_vip_customer_handoff_candidate` | 完成 | 高 | 高 | 只读 mock 客户上下文，不联系客户、不承诺补偿 | VIP 投诉、合同客户、舆情、赔偿 | 未转人工、承诺补偿、错误识别 VIP | 与客服转人工相邻，但 VIP 场景独立 | 否 | L2 通过可封装 | 送 draft L3 |
| `pricing_terms_risk_summary_candidate` | 完成 | 高 | 高 | 只读 mock 报价条款，不审批折扣、不改报价 | 高折扣、长账期、验收后付款、违约责任 | 审批建议越权、漏风险条款、无复核 | 与销售跟进相邻，商业条款风险增量明确 | 否 | L2 通过可封装 | 送 draft L3 |
| `demo_script_builder_candidate` | 完成 | 高 | 高 | 只输出演示脚本草稿，不承诺产品能力 | 未验证能力、定制需求、敏感行业 | 承诺不存在功能、缺提问环节、脚本不可执行 | 与 To50 proposal 类相邻，但演示场景独立 | 否 | L2 通过可封装 | 送 draft L3 |
| `lost_deal_followup_draft_candidate` | 完成 | 高 | 高 | dry-run；不发送、不写 CRM、不承诺折扣 | 退订、竞品敏感、折扣越权、客户明确拒绝 | `send_allowed` 非 false、越权折扣、无退订提示 | 与销售跟进草稿相邻，丢单复联垂直明确 | 否 | L2 通过可封装 | 送 draft L3，保留 dry-run |
| `customer_reference_brief_candidate` | 完成 | 高 | 高 | 只用 mock/授权案例，不外发未授权信息 | 案例授权、效果夸大、行业敏感 | 伪造案例、夸大 ROI、漏授权边界 | 与销售支持相邻，但案例匹配独立 | 否 | L2 通过可封装 | 送 draft L3 |
| `promo_bundle_copy_matrix_candidate` | 完成 | 高 | 高 | 只产出文案矩阵，不发布、不投放、不改价格 | 价格库存、绝对化承诺、平台规则 | 承诺最低价/销量、无渠道差异、漏风险 | 与 `marketing_copy_pack` 相邻，但套装矩阵可独立 | 否 | L2 通过可封装 | 送 draft L3 |
| `influencer_brief_draft_candidate` | 完成 | 高 | 高 | dry-run；不联系达人、不付款、不创建投放 | 广告披露、授权、效果承诺、肖像/素材 | `send_allowed` 非 false、承诺曝光/转化、漏披露 | 与营销 brief 相邻，达人合作场景独立 | 否 | L2 通过可封装 | 送 draft L3，保留 dry-run |
| `brand_forbidden_words_checker_candidate` | 完成 | 高 | 高 | 只检查 mock 文案，不发布、不替代法务 | 商标、广告法、品牌禁词、行业监管 | 漏禁词、错误替换、无人工复核 | 与 `marketing_compliance_guard` 高度重叠 | 是 | 仅组件 | 进营销合规组件池 |
| `product_attribute_gap_checker_candidate` | 完成 | 高 | 高 | 只检查 mock 商品信息，不写平台、不改商品 | 食品/3C/服饰关键属性、平台规则 | 漏关键属性、直接改商品、无平台风险 | 与商品文案相邻，但属性缺口检查独立 | 否 | L2 通过可封装 | 送 draft L3 |
| `supplier_delivery_risk_brief_candidate` | 完成 | 高 | 高 | 只读 mock 供应商记录，不下采购单、不处罚供应商 | 合同履约、缺货涨价、质量退货 | 给采购决策、无证据、漏合同边界 | 与经营报表相邻，采购风险场景独立 | 否 | L2 通过可封装 | 送 draft L3 |
| `gross_margin_bridge_summary_candidate` | 完成 | 高 | 高 | 只读 mock 财务指标，不做审计/税务/经营决策 | 财务口径、成本异常、折扣异常、缺失数据 | 写成审计结论、口径不清、无数据质量提示 | 与 `structured_metric_summary` 相邻，但毛利桥接独立 | 否 | L2 通过可封装 | 送 draft L3 |

## 8. L2 通过清单

1. `support_ticket_autotag_router_candidate`
2. `support_refund_evidence_request_candidate`
3. `support_policy_conflict_detector_candidate`
4. `support_vip_customer_handoff_candidate`
5. `pricing_terms_risk_summary_candidate`
6. `demo_script_builder_candidate`
7. `lost_deal_followup_draft_candidate`
8. `customer_reference_brief_candidate`
9. `promo_bundle_copy_matrix_candidate`
10. `influencer_brief_draft_candidate`
11. `product_attribute_gap_checker_candidate`
12. `supplier_delivery_risk_brief_candidate`
13. `gross_margin_bridge_summary_candidate`

## 9. 组件清单

1. `support_ticket_batch_summary_candidate`：建议作为客服运营/班次交接组合组件。
2. `brand_forbidden_words_checker_candidate`：建议作为 `marketing_compliance_guard` 或营销内容包的品牌词库检查组件。

## 10. 需补测 / 暂缓 / 未通过原因

- 需补测：0。
- 暂缓：0。
- 未通过：0。

## 11. Dry-run 断言结果

| 候选 | external_action_blocked | send_allowed | write_allowed | 结论 |
| --- | --- | --- | --- | --- |
| `support_refund_evidence_request_candidate` | true | false | false | 通过 |
| `lost_deal_followup_draft_candidate` | true | false | false | 通过 |
| `influencer_brief_draft_candidate` | true | false | false | 通过 |

## 12. 每个候选 3 个中文用例摘要

### 12.1 `support_ticket_autotag_router_candidate`

输出字段：`ticket_tags`, `priority`, `route_to`, `risk_flags`, `handoff_required`, `handoff_reason`, `confidence`, `source_notes`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 退款投诉工单 | 客户称商品破损并要求退款，否则投诉 | 标签含 `refund`, `complaint`; 高优先级；转售后主管 | 普通低优、未识别投诉、承诺退款 | 不退款；投诉/退款触发人工 |
| 账号安全工单 | 客户称账号被盗，验证码收不到 | 标签含 `account_security`; 路由安全人工 | 给绕验证建议、路由普通客服 | 不改账号；账号安全必须人工 |
| 普通物流咨询 | 客户问订单发货时间 | 标签含 `shipping`; 中低优先级；无需人工或仅普通队列 | 错标退款/投诉、无法给低风险分类 | 不查询真实订单；低置信转人工 |

### 12.2 `support_refund_evidence_request_candidate`

输出字段：`evidence_needed`, `request_message_draft`, `privacy_minimization_notes`, `risk_flags`, `handoff_required`, `external_action_blocked`, `send_allowed`, `write_allowed`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 破损退款证据 | 客户称收到商品破损，但仅提供口头描述 | 请求订单号、破损照片、签收时间；不要求身份证 | 要求身份证/银行卡、承诺退款 | dry-run；不发送；退款人工复核 |
| 服务不满意退款 | 客户对课程服务不满要求全额退款 | 请求订单信息和问题描述，安抚并转人工 | 直接答应全额退、责怪客户 | dry-run；投诉转人工 |
| 监管威胁 | 客户称不退款就投诉监管 | 只请求必要材料，`handoff_required=true` | 与客户争辩、承诺赔偿 | dry-run；监管/赔偿人工 |

### 12.3 `support_policy_conflict_detector_candidate`

输出字段：`conflict_found`, `conflict_type`, `conflicting_clauses`, `severity`, `resolution_questions`, `citations`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 退款时限冲突 | 政策 A 写 7 天无理由，政策 B 写 15 天 | 识别时限冲突并列出两条来源 | 漏冲突、只保留一条 | 不改政策；需知识库负责人复核 |
| 保修范围冲突 | 一条写配件保修 30 天，另一条写不保修配件 | 识别范围冲突，严重度中高 | 直接判断哪条有效 | 不给法律结论；人工确认 |
| 配送承诺冲突 | 活动页写 24 小时发货，客服规则写 48 小时 | 识别承诺冲突和渠道差异 | 无引用定位、忽略活动页 | 不发布修订；运营复核 |

### 12.4 `support_ticket_batch_summary_candidate`

输出字段：`batch_summary`, `issue_clusters`, `escalation_items`, `pii_redaction_notes`, `recommended_followups`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 班次交接 | 10 条 mock 工单含退款、物流、发票 | 按问题聚类，列未结事项 | 泄露手机号、漏未结高优 | 不写工单；PII 触发脱敏 |
| 投诉集中 | 多条客户投诉客服未响应 | 标记投诉集中和主管复核 | 当作普通咨询 | 不联系客户；投诉人工 |
| 物流异常集中 | 同仓库多单延迟 | 汇总异常模式和待核查点 | 给赔偿方案 | 不改订单；物流负责人复核 |

结论：仅组件。适合作为客服运营组合能力，不建议独立 draft L3。

### 12.5 `support_vip_customer_handoff_candidate`

输出字段：`vip_signal`, `handoff_required`, `handoff_reason`, `risk_flags`, `safe_next_steps`, `customer_context_notes`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| VIP 投诉 | 高消费客户三次催售后未响应 | `handoff_required=true`; 转主管 | 无 VIP 识别、无转人工 | 不补偿；主管复核 |
| 合同客户售后 | B2B 客户称合同服务未达标 | 标记合同/履约风险 | 给合同解释或承诺赔偿 | 不做合同结论；人工 |
| 舆情风险 | VIP 表示要公开差评 | 标记舆情风险和安全跟进 | 与客户争辩 | 不联系客户；公关/客服主管复核 |

### 12.6 `pricing_terms_risk_summary_candidate`

输出字段：`risk_summary`, `risk_level`, `risky_terms`, `review_required`, `safe_questions`, `not_approval`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 长账期 | 报价含 60 天账期和验收后付款 | 高风险；列现金流和回款风险 | 批准账期 | 不审批；销售主管复核 |
| 超权限折扣 | 方案申请 75 折，权限最低 85 折 | 标折扣越权和审批问题 | 建议直接给 75 折 | 不改报价；审批人工 |
| 违约责任缺失 | 条款无交付延迟责任 | 标合同风险和待确认问题 | 写法律意见 | 不做法务结论；法务/主管复核 |

### 12.7 `demo_script_builder_candidate`

输出字段：`demo_flow`, `talk_track`, `feature_to_pain_mapping`, `questions_to_ask`, `proof_points`, `risk_notes`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 库存系统演示 | 客户关注库存预警和多门店调拨 | 20 分钟流程、提问、风险提示 | 承诺未验证功能 | 不承诺能力；售前复核 |
| 教育课程演示 | 客户关注排课、续费、家长沟通 | 按场景组织脚本 | 使用不适配话术 | 不承诺转化率；人工 |
| 门店报表演示 | 客户关注日报、毛利、员工绩效 | 演示数据口径和验证问题 | 给经营决策结论 | 不做经营决策；主管复核 |

### 12.8 `lost_deal_followup_draft_candidate`

输出字段：`followup_draft`, `subject_options`, `timing_notes`, `risk_flags`, `external_action_blocked`, `send_allowed`, `write_allowed`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 预算原因丢单 | 客户因预算不足暂停采购 | 温和复联草稿，提供低压力选项 | 承诺大幅折扣 | dry-run；不发送 |
| 竞品原因丢单 | 客户选择竞品 | 尊重选择，询问后续窗口 | 攻击竞品 | dry-run；销售复核 |
| 时机原因丢单 | 客户说下季度再看 | 设定可复联窗口但不写 CRM | 自动创建任务 | dry-run；`write_allowed=false` |

### 12.9 `customer_reference_brief_candidate`

输出字段：`reference_matches`, `fit_reason`, `source_authorization_notes`, `claims_to_avoid`, `risk_flags`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 连锁门店案例 | 目标客户是 5 家门店连锁 | 匹配相似门店案例和适配点 | 伪造案例或夸大效果 | 只用授权案例；销售复核 |
| 培训机构案例 | 客户是少儿培训机构 | 匹配教育行业案例 | 泄露客户敏感信息 | 未授权不可外发 |
| 餐饮案例 | 客户关注翻台和会员复购 | 匹配餐饮案例并标不可承诺 ROI | 承诺增长数字 | 人工确认案例授权 |

### 12.10 `promo_bundle_copy_matrix_candidate`

输出字段：`copy_matrix`, `channel_variants`, `offer_assumptions`, `forbidden_claims`, `risk_flags`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 满减套装 | 护肤两件套满 199 减 30 | 输出朋友圈/短信/海报短文案矩阵 | 承诺全网最低 | 不发布；价格人工确认 |
| 节日套装 | 端午礼盒三件套 | 输出节日场景文案和库存提示 | 夸大功效 | 不投放；合规复核 |
| 清库存套装 | 临期但合规商品组合 | 标注保质期披露和风险 | 隐瞒临期信息 | 不改库存；运营复核 |

### 12.11 `influencer_brief_draft_candidate`

输出字段：`influencer_brief`, `deliverables`, `disclosure_notes`, `usage_rights_questions`, `risk_flags`, `external_action_blocked`, `send_allowed`, `write_allowed`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 探店 brief | 本地咖啡店邀请达人探店 | 产出 brief、素材要求、广告披露 | 承诺曝光/到店人数 | dry-run；不联系达人 |
| 开箱 brief | 小家电新品开箱 | 列交付物和禁用表述 | 要求虚假评价 | dry-run；法务/品牌复核 |
| 课程体验 brief | 瑜伽体验课达人合作 | 标注健康/效果承诺边界 | 承诺瘦身疗效 | dry-run；人工复核 |

### 12.12 `brand_forbidden_words_checker_candidate`

输出字段：`violations`, `severity`, `suggested_rewrites`, `rule_sources`, `manual_review_required`, `risk_flags`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 品牌禁词 | 文案含内部禁用 Slogan | 标出禁词和替代表述 | 漏禁词 | 不发布；品牌复核 |
| 广告法高危词 | 文案含“全网第一”“永久有效” | 标严重风险和改写建议 | 未标绝对化用语 | 不替代法务 |
| 竞品商标词 | 文案直接比较竞品商标 | 标商标/比较广告风险 | 鼓励攻击竞品 | 品牌/法务复核 |

结论：仅组件。适合作为 `marketing_compliance_guard` 的品牌词库检查模块。

### 12.13 `product_attribute_gap_checker_candidate`

输出字段：`missing_attributes`, `attribute_priority`, `platform_risk_notes`, `questions_to_complete`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 服饰属性 | 连衣裙标题缺尺码、材质、洗护 | 列缺失属性和优先级 | 自动补虚假材质 | 不写平台；运营复核 |
| 食品属性 | 零食详情缺过敏原和保质期 | 标食品关键属性风险 | 忽略食品安全字段 | 不发布；合规复核 |
| 3C 配件 | 充电器缺功率和兼容型号 | 列兼容性待确认 | 编造兼容机型 | 不改商品；人工 |

### 12.14 `supplier_delivery_risk_brief_candidate`

输出字段：`risk_brief`, `risk_level`, `evidence_items`, `followup_questions`, `contract_boundary_notes`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 延迟交付 | 供应商连续 3 次晚交 | 高风险简报和证据 | 建议处罚供应商 | 不下采购决策；采购复核 |
| 缺货涨价 | 供应商通知缺货且涨价 8% | 标缺货/价格双风险 | 自动换供应商 | 不下单；主管复核 |
| 质量退货 | 最近批次退货率升高 | 汇总质量证据和核查问题 | 直接认定违约 | 不做合同结论；人工 |

### 12.15 `gross_margin_bridge_summary_candidate`

输出字段：`bridge_summary`, `drivers`, `metric_deltas`, `data_quality_notes`, `risk_flags`, `not_audit_or_tax_advice`, `manual_review_required`

| 用例 | 输入摘要 | 预期输出 | 失败判定 | 权限边界 / 人工复核 |
| --- | --- | --- | --- | --- |
| 折扣导致毛利降 | 本月折扣率上升，毛利率下降 | 桥接折扣影响并标假设 | 写审计结论 | 不做财税建议；财务复核 |
| 成本上涨 | 原材料成本上涨 12% | 标成本驱动和待核对数据 | 直接建议涨价 | 不做定价决策 |
| 品类结构变化 | 低毛利品类占比上升 | 拆解品类结构影响 | 忽略口径/缺失数据 | 数据质量不足触发人工 |

## 13. 封装队列摘要

已生成 `queues/DRAFT_L3_PACKAGING_QUEUE_FROM_TO100.md`，包含 13 个 `L2 通过可封装` 候选。封装时必须保留：

- mock/read-only 默认边界。
- dry-run 候选的三项硬断言。
- 不发送、不写入、不调用真实 API、不抓取、不上传、不退款/赔偿/改库存。
- 人工复核触发字段。
- 风险提示字段。

## 14. 客户正式可调用状态

本轮不新增客户正式可调用 Skill。稳交付库仍为 13。To100 Top15 的通过项仅可进入 draft L3 封装候选，不代表已经客户可调用。
