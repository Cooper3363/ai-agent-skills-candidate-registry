# Platform Acceptance Quality Sprint 07 Result

回传时间: 2026-06-07
回传窗口: AI.Skills 平台调用验收窗口
任务: Quality Sprint 07 平台候选调用验收复验
验收口径: 候选库本地可试跑 / 平台候选调用边界验收；不代表客户正式可调用，不进入 stable 仓库

## 已完成事项

- 已读取 `PACKAGING_QUALITY_SPRINT_07_RESULT.md`。
- 已读取 `queues/PLATFORM_ACCEPTANCE_QUALITY_SPRINT_07_QUEUE.md`。
- 已逐一读取 8 个指定 draft_l3 包的 `SKILL.md` 与 `skill.yaml`。
- 已核查 `status=draft_l3`、`customer_callable=false`、`platform_deliverable=false`、`stable_current_count=63`。
- 已核查 8 个 read-only 包保留 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`、`real_harness_smoke_required=true`。
- 已核查 `read_only_scope_manifest`、`audit_log_schema`、`error_fallback_strategy`、`manual_review_triggers`、`failure_modes`。
- 已核查 OpenAI-compatible 中转站模型通道说明，且 key/base_url/model 由平台 runtime 注入，repo 不写 key。
- 已核查未将 simulated L2 误写为真实 API/SaaS/Harness/provider passed。
- 已核查未写成 stable promotion passed。
- 未安装依赖，未访问真实账号，未调用真实 API/provider。
- 未读取/打印/写入 key，未读取 `.env`，未读取客户真实文件。
- 未发送，未上传，未写业务系统，未修改 stable 仓库。

## 当前问题

无。

## 阻塞原因

无阻塞。

## 需要 AI.Skills 指挥中心决策的问题

- 是否批准 8 个 accepted 候选进入 stable promotion queue。
- 是否后续对 Workable/Greenhouse/HubSpot passed 候选单独进入 HR/CRM 专题 L2 队列。

## 数量汇总

| 项目 | 数量 |
| --- | ---: |
| 本轮验收 draft_l3 包 | 8 |
| accepted | 8 |
| needs_fix | 0 |
| blocked | 0 |
| failed | 0 |
| 字段缺失对象 | 0 |
| 可保持 candidate/local trial | 8 |
| 本轮修改 stable 仓库 | 0 |
| 当前 stable 正式 Skill 数 | 63 |

## 逐包验收结论

| draft_skill_id | 结论 | 候选调用边界 |
| --- | --- | --- |
| `intercom_article_decay_readonly_agent` | accepted | 只基于 mock/read-only Intercom articles、conversations 与 decay rules 输出文章衰减、过期内容和知识缺口；不写文章、不发消息、不改 conversation。 |
| `shopify_return_product_quality_readonly_agent` | accepted | 只基于 mock/read-only Shopify returns、products 与 quality rules 输出退货原因聚类、商品质量风险和退款边界提示；不退款、不改商品、不改库存、不发通知。 |
| `metabase_executive_digest_readonly_agent` | accepted | 只基于 mock/read-only Metabase dashboard cards、metric rules 与 period 输出经营摘要、异常提示和数据质量 flags；不写 query/dashboard、不连接真实 DB、不输出审计结论。 |
| `docusign_missing_signature_readonly_agent` | accepted | 只基于 mock/read-only DocuSign envelopes、signature rules 与 risk rules 输出缺签、停滞和期限风险报告；不发送合同、不签署、不修改 envelope。 |
| `mailchimp_deliverability_qc_readonly_agent` | accepted | 只基于 mock/read-only Mailchimp campaign reports、deliverability rules 与 audience rules 输出送达质量、bounce/投诉/退订风险和受众健康提示；不发邮件、不改 audience/contact、不承诺营销效果。 |
| `helpscout_saved_reply_gap_readonly_agent` | accepted | 只基于 mock/read-only Help Scout conversations、saved replies 与 support rules 输出 saved reply 缺口、回复 brief 和政策冲突；不回复客户、不写 saved reply、不打 tag。 |
| `front_account_handoff_readonly_agent` | accepted | 只基于 mock/read-only Front account conversations、account rules 与 handoff rules 输出客户交接 brief、未闭环事项和风险提示；不发消息、不分派、不评论、不改 inbox。 |
| `amplitude_activation_dropoff_readonly_agent` | accepted | 只基于 mock/read-only Amplitude activation metrics、event schema 与 quality rules 输出激活掉点、事件缺失和样本质量提示；不写 cohorts/charts、不读真实用户明细、不把相关性写成因果。 |

## 字段缺失清单

无。

## 字段与边界核查

| 检查项 | 结果 |
| --- | --- |
| `SKILL.md` 与 `skill.yaml` 均存在 | 8/8 通过 |
| `status=draft_l3` | 8/8 通过 |
| `customer_callable=false` | 8/8 通过 |
| `platform_deliverable=false` | 8/8 通过 |
| `stable_current_count=63` | 8/8 通过 |
| `read_only=true` | 8/8 通过 |
| `write_allowed=false` | 8/8 通过 |
| `send_allowed=false` | 8/8 通过 |
| `upload_allowed=false` | 8/8 通过 |
| `external_action_blocked=true` | 8/8 通过 |
| `real_harness_smoke_required=true` | 8/8 通过 |
| `read_only_scope_manifest` | 8/8 通过 |
| `audit_log_schema` | 8/8 通过 |
| `error_fallback_strategy` | 8/8 通过 |
| `manual_review_triggers` | 8/8 通过 |
| `failure_modes` | 8/8 通过 |
| OpenAI-compatible 中转站模型通道说明 | 8/8 通过 |
| key/base_url/model 由平台 runtime 注入，repo 不写 key | 8/8 通过 |
| 未误写真实 API/SaaS/Harness/provider passed | 8/8 通过 |
| 未写成 stable promotion passed | 8/8 通过 |

## 真实 Harness 待办

- 为每个 SaaS connector 单独配置最小 read-only scope。
- 验证 OAuth/Token/key 托管不写入 repo。
- 验证沙盒账号、速率限制、审计日志和错误回退。
- 验证真实 Harness 不执行写入、发送、上传、扣款、退款、库存修改、订阅修改、写账、报税、任务创建或文件共享。
- 验证失败时返回 `fallback_required=true` 与人工复核触发。
- 验证日志与审计不泄露 access token、refresh token、客户文件内容、客户隐私或业务敏感数据。
- 真实 Harness smoke 通过前，不得申请客户正式可调用或 stable promotion。

## 硬边界确认

- 不安装依赖。
- 不访问真实账号。
- 不调用真实 API/provider。
- 不读取/打印/写入 key。
- 不读取 `.env`。
- 不读取客户真实文件。
- 不发送、不上传、不写业务系统。
- 不退款、不赔偿、不扣款、不改库存、不改订阅、不写账、不报税、不创建任务、不共享文件。
- 不修改 stable 仓库。

## Stable Promotion Queue 建议

因 8 个候选均为 `accepted`，建议允许进入 stable promotion queue 做后续评审，但不得直接改 stable 仓库。

建议进入 stable promotion queue 的对象：

1. `intercom_article_decay_readonly_agent`
2. `shopify_return_product_quality_readonly_agent`
3. `metabase_executive_digest_readonly_agent`
4. `docusign_missing_signature_readonly_agent`
5. `mailchimp_deliverability_qc_readonly_agent`
6. `helpscout_saved_reply_gap_readonly_agent`
7. `front_account_handoff_readonly_agent`
8. `amplitude_activation_dropoff_readonly_agent`

进入 promotion queue 前置说明：

- 仍需真实 Harness smoke。
- 仍需平台确认最小 read-only scope、OAuth/key 托管、审计日志、失败回退与人工复核策略。
- 仍需指挥中心显式 promotion 决策。
- 当前结果不等于客户正式可调用。

## 退回建议

- 退回封装窗口：无。
- 退回测试台：无。
- 退回许可证复核窗口：无。
- 拒绝对象：无。

## 稳交付边界

本轮结果只代表 `platform_candidate_acceptance accepted`。未修改 stable 仓库，未新增客户正式可调用 Skill，当前 stable 正式 Skill 数仍为 63。
