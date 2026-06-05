# L2 Official Top15 From To100 Queue

回传对象：AI.Skills 指挥中心  
来源：`DEEPAGENTS_SMOKE_TO_100_RESULT.md`  
说明：本队列来自第二阶段 To100 DeepAgents candidate smoke passed 候选筛选。进入本队列不代表正式 L2 通过，不代表可封装，不代表客户正式可调用。

## 1. 队列口径

- 只进入正式 L2 simulated，不做真实工具调用。
- 每个候选正式 L2 至少覆盖 3 个中文业务 mock 用例。
- 必须检查固定输入/输出 schema、中文可用性、权限边界、人工复核触发、失败判定、与稳交付 13 个 Skill / To50 候选重复关系、是否仅组件。
- 结论只能为：`L2 通过可封装`、`需补测`、`暂缓`、`未通过`、`仅组件`。
- dry-run 候选必须断言：`external_action_blocked=true`、`send_allowed=false`、`write_allowed=false`。

## 2. 统一禁止动作

- 不安装额外业务依赖。
- 不访问真实账号。
- 不读取真实客户文件。
- 不调用真实业务 API。
- 不发送邮件、短信或微信。
- 不写 CRM、日历、任务或业务系统。
- 不真实抓取网页。
- 不上传文件。
- 不退款、不赔偿、不改库存。
- 不生成真实图片、视频、音频、OCR 或 PDF 结果。
- 不改稳交付 13 个包。

## 3. Top 15 正式 L2 simulated 队列

| 排名 | candidate_id | 业务包 | role | trial_mode | 正式 L2 重点 | 推荐中文用例方向 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | support_ticket_autotag_router_candidate | 客服知识库助手包 | 客服运营 | can_mock_smoke | 工单标签、优先级、路由、风险字段、转人工 | 退款投诉、账号安全、普通物流咨询 |
| 2 | support_refund_evidence_request_candidate | 客服知识库助手包 | 售后客服 | can_dry_run_smoke | 退款证据补充请求、隐私最小化、不得承诺退款 | 商品破损退款、服务不满意退款、监管威胁 |
| 3 | support_policy_conflict_detector_candidate | 客服知识库助手包 | 知识库运营 | can_mock_smoke | 政策冲突识别、冲突条款定位、人工修订建议 | 退款时限冲突、保修规则冲突、配送承诺冲突 |
| 4 | support_ticket_batch_summary_candidate | 客服知识库助手包 | 客服主管 | can_mock_smoke | 批量工单摘要、聚类、升级项、PII 脱敏提示 | 班次交接、投诉集中、物流异常集中 |
| 5 | support_vip_customer_handoff_candidate | 客服知识库助手包 | 大客户支持 | can_mock_smoke | VIP 转人工原因、安全下一步、高风险标记 | VIP 投诉、合同客户售后、舆情风险 |
| 6 | pricing_terms_risk_summary_candidate | 销售跟进助手包 | 销售主管 | can_mock_smoke | 价格/账期/折扣/付款条款风险，不做审批 | 长账期、超权限折扣、验收后付款 |
| 7 | demo_script_builder_candidate | 销售跟进助手包 | 售前顾问 | can_mock_smoke | 演示流程、话术、提问、能力承诺边界 | 库存系统演示、教育课程演示、门店报表演示 |
| 8 | lost_deal_followup_draft_candidate | 销售跟进助手包 | 销售代表 | can_dry_run_smoke | 丢单复联草稿，禁止发送/写 CRM | 预算原因丢单、竞品原因丢单、时机原因丢单 |
| 9 | customer_reference_brief_candidate | 销售跟进助手包 | 销售支持 | can_mock_smoke | 授权案例匹配、适配理由、不得伪造效果 | 连锁门店案例、培训机构案例、餐饮案例 |
| 10 | promo_bundle_copy_matrix_candidate | 营销内容生产包 | 营销运营 | can_mock_smoke | 促销套装文案矩阵、禁用承诺、渠道差异 | 满减套装、节日套装、清库存套装 |
| 11 | influencer_brief_draft_candidate | 营销内容生产包 | 达人合作运营 | can_dry_run_smoke | 达人合作 brief、广告披露、授权边界 | 探店 brief、开箱 brief、课程体验 brief |
| 12 | brand_forbidden_words_checker_candidate | 营销内容生产包 | 品牌合规 | can_mock_smoke | 禁词检查、替代表达、复核触发 | 品牌禁词、广告法高危词、竞品商标词 |
| 13 | product_attribute_gap_checker_candidate | 营销内容生产包 | 电商运营 | can_mock_smoke | 商品属性缺口、平台风险、补充问题 | 服饰属性、食品属性、3C 配件属性 |
| 14 | supplier_delivery_risk_brief_candidate | 经营报表分析包 | 采购/运营 | can_mock_smoke | 供应商交付风险证据和跟进问题，不做采购决策 | 延迟交付、缺货涨价、质量退货 |
| 15 | gross_margin_bridge_summary_candidate | 经营报表分析包 | 财务/经营 | can_mock_smoke | 毛利变化驱动拆解、数据质量和口径提示 | 折扣导致毛利降、成本上涨、品类结构变化 |

## 4. Dry-run 候选专项要求

| candidate_id | L2 必须断言 |
| --- | --- |
| support_refund_evidence_request_candidate | `external_action_blocked=true`; `send_allowed=false`; `write_allowed=false`; 不承诺退款/赔偿 |
| lost_deal_followup_draft_candidate | `external_action_blocked=true`; `send_allowed=false`; `write_allowed=false`; 不发送复联消息、不写 CRM |
| influencer_brief_draft_candidate | `external_action_blocked=true`; `send_allowed=false`; `write_allowed=false`; 不联系达人、不创建投放或付款动作 |

## 5. 建议下一步

测试台下一轮可按本队列执行正式 L2 simulated。每个候选至少 3 个中文业务 mock 用例，完成后再由指挥中心决定是否送入 draft L3 封装队列。
