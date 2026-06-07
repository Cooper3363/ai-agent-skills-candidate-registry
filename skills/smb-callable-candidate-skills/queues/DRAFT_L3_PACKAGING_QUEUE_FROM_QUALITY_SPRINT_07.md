# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_07

生成日期：2026-06-07

来源：`../L2_OFFICIAL_TOP8_FROM_QUALITY_SPRINT_07_RESULT.md`

队列性质：Quality Sprint 07 正式 L2 simulated 后的 draft L3 封装准备队列。  
重要边界：进入本队列不代表真实 SaaS/API/Harness/provider 通过，不代表自动进入 stable 或客户正式可调用；stable 仓库正式 Skill 仍为 55，promotion/platform acceptance 需另行决策。

## 1. 入队标准

- L2 结论为：`L2 通过可封装`。
- 可表达为 DeepAgents/通用 Agent Skill callable candidate。
- 当前仅允许 mock/read-only 语义。
- SaaS/API connector 必须保留最小只读 scope 和 read-only 硬断言。
- 后续封装必须补齐真实 Harness smoke 计划、审计日志、错误回退、权限声明和人工复核触发。

## 2. 封装队列

| 排名 | draft_skill_id | source_candidate_id | 业务包 | trial mode | 封装目标 | 必须保留的权限边界 | 最小平台 smoke 输入 | 后续真实 Harness 要求 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `intercom_article_decay_readonly_agent` | `quality_sprint07_intercom_article_decay_readonly_candidate` | 客服知识库助手包 | `read_only_mock` | Intercom 文章衰减与缺口只读分析 | `read_only=true`, 最小 articles/conversations 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox articles/conversations | 禁止写文章、发消息、改 conversation |
| 2 | `shopify_return_product_quality_readonly_agent` | `quality_sprint07_shopify_return_product_quality_candidate` | 电商售后质量包 | `read_only_mock` | Shopify 退货商品质量问题聚类 | `read_only=true`, 最小 returns/products 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox returns/products | 禁止退款、改商品、改库存、发通知 |
| 3 | `metabase_executive_digest_readonly_agent` | `quality_sprint07_metabase_executive_digest_candidate` | 经营报表摘要包 | `read_only_mock` | Metabase dashboard 经营摘要只读分析 | `read_only=true`, 最小 dashboard/card 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox dashboard cards | 禁止写 query/dashboard、连接真实 DB |
| 4 | `docusign_missing_signature_readonly_agent` | `quality_sprint07_docusign_missing_signature_readonly_candidate` | 合同签署状态包 | `read_only_mock` | DocuSign 缺签和停滞报告只读分析 | `read_only=true`, 最小 envelopes/status 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox envelopes | 禁止发送、签署、修改 envelope |
| 5 | `mailchimp_deliverability_qc_readonly_agent` | `quality_sprint07_mailchimp_deliverability_qc_candidate` | 邮件营销健康包 | `read_only_mock` | Mailchimp deliverability QC 只读分析 | `read_only=true`, 最小 campaign/audience report 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox campaign reports | 禁止发送邮件、改 audience/contact |
| 6 | `helpscout_saved_reply_gap_readonly_agent` | `quality_sprint07_helpscout_saved_reply_gap_candidate` | 客服回复模板包 | `read_only_mock` | Help Scout saved reply 缺口只读分析 | `read_only=true`, 最小 conversations/saved replies 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox conversations/saved replies | 禁止回复客户、写 saved reply、打 tag |
| 7 | `front_account_handoff_readonly_agent` | `quality_sprint07_front_account_handoff_candidate` | 客户交接包 | `read_only_mock` | Front account 交接 brief 只读分析 | `read_only=true`, 最小 account conversations 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox account conversations | 禁止发送、分派、评论、改 inbox |
| 8 | `amplitude_activation_dropoff_readonly_agent` | `quality_sprint07_amplitude_activation_dropoff_candidate` | 产品/增长分析包 | `read_only_mock` | Amplitude activation dropoff 只读分析 | `read_only=true`, 最小 activation/report 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox activation metrics | 禁止写 cohorts/charts、读取真实用户明细 |

## 3. 封装窗口统一要求

- 每个 draft Skill 必须声明 `customer_callable=false`，直到真实 Harness、权限、安全和验收流程完成。
- 每个 read-only Skill 必须声明 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- 输出必须保留 `source_rows`、`source_ids` 或等价证据字段。
- 输出必须保留 `manual_review_required` 和 `manual_review_triggers`。
- 禁止自动发送、发布、上传、写任何业务系统、扣款、退款、改库存、改订阅、创建任务、共享文件。
- 后续如需真实平台 smoke，必须由指挥中心另行批准并使用沙盒账号、最小权限和审计日志。

## 4. 未纳入本封装队列的项

- 5 个媒体/provider route-check passed 候选未纳入本队列；如继续推进，必须走独立真实 provider smoke 审批链路。
- Workable/Greenhouse/HubSpot passed 候选未纳入本队列；建议后续按 HR/CRM 专题补做正式 L2。
- `needs_more_license_info` 与 `component_only` 项未处理，不能进入本队列。
