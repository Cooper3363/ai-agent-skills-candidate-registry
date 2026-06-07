# DRAFT_L3_PACKAGING_QUEUE_FROM_QUALITY_SPRINT_05

生成日期：2026-06-05

来源：`../L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_05_RESULT.md`

队列性质：Quality Sprint 05 正式 L2 simulated 后的 draft L3 封装准备队列。  
重要边界：进入本队列不代表真实 SaaS/API/Harness/provider 通过，不代表客户正式可调用，不进入稳交付库；客户正式可调用 Skill 仍为 13。

## 1. 入队标准

- L2 结论为：`L2 通过可封装`。
- 可表达为 DeepAgents/通用 Agent Skill callable candidate。
- 当前仅允许 mock/read-only/dry-run 语义。
- SaaS/API connector 必须保留最小只读 scope 或 dry-run 硬断言。
- 后续封装必须补齐真实 Harness smoke 计划、审计日志、错误回退、权限声明和人工复核触发。

## 2. 封装队列

| 排名 | draft_skill_id | source_candidate_id | 业务包 | trial mode | 封装目标 | 必须保留的权限边界 | 最小平台 smoke 输入 | 后续真实 Harness 要求 |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `intercom_conversation_macro_gap_readonly_agent` | `quality_sprint05_intercom_conversation_macro_gap_readonly_candidate` | 客服知识库助手包 | `read_only_mock` | Intercom 对话宏缺口和升级建议只读分析 | `read_only=true`, 最小 conversations/articles/macros 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox conversations/articles/macros rows | 只读 OAuth scope、来源行、禁止回复/更新/写宏 |
| 2 | `helpscout_article_gap_readonly_agent` | `quality_sprint05_helpscout_article_gap_readonly_candidate` | 客服知识库助手包 | `read_only_mock` | Help Scout 知识库文章缺口只读分析 | `read_only=true`, 最小 mailbox/docs 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox mailbox/docs rows | 禁止回复/打 tag/写 docs，政策冲突强制复核 |
| 3 | `front_inbox_handoff_readonly_agent` | `quality_sprint05_front_inbox_handoff_readonly_candidate` | 客服/运营交接包 | `read_only_mock` | Front inbox 交接摘要和 owner gap 只读分析 | `read_only=true`, 最小 inbox/messages 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox inbox messages/team roster | 禁止发送/分配/评论，VIP 和承诺日期强制复核 |
| 4 | `klaviyo_campaign_health_readonly_agent` | `quality_sprint05_klaviyo_campaign_health_readonly_candidate` | 营销活动健康包 | `read_only_mock` | Klaviyo campaign 健康和退订/投诉风险只读分析 | `read_only=true`, 最小 campaign/metrics 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox campaign metrics | 禁止发送/改联系人/campaign，不承诺营销效果 |
| 5 | `woocommerce_catalog_qc_readonly_agent` | `quality_sprint05_woocommerce_catalog_qc_readonly_candidate` | 电商运营包 | `read_only_mock` | WooCommerce 商品目录 QC 只读分析 | `read_only=true`, 最小 products/catalog 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox product rows | 禁止改商品/订单/库存/价格/上下架 |
| 6 | `bigcommerce_catalog_gap_readonly_agent` | `quality_sprint05_bigcommerce_catalog_gap_readonly_candidate` | 电商运营包 | `read_only_mock` | BigCommerce 目录和变体缺口只读分析 | `read_only=true`, 最小 catalog/variants 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox catalog/variant rows | 禁止写商品/改变体/改库存/发布 |
| 7 | `google_ads_creative_budget_anomaly_readonly_agent` | `quality_sprint05_google_ads_creative_budget_anomaly_readonly_candidate` | 营销投放分析包 | `read_only_mock` | Google Ads 素材/预算异常只读分析 | `read_only=true`, 最小 reports/campaign metrics 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox campaign/creative reports | 禁止改 budget/bid/ad，不承诺排名或广告效果 |
| 8 | `ga4_landing_page_dropoff_readonly_agent` | `quality_sprint05_ga4_landing_page_dropoff_readonly_candidate` | 营销/经营分析包 | `read_only_mock` | GA4 落地页掉点和数据质量只读分析 | `read_only=true`, 最小 report rows 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox GA4 report rows | 禁止改 property/config，不读取真实用户明细 |
| 9 | `canva_design_brief_dryrun_agent` | `quality_sprint05_canva_design_brief_dryrun_candidate` | 营销设计 brief 包 | `dry_run_only` | Canva 设计 brief 和不可执行导出 spec | `send_allowed=false`, `write_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox campaign brief/brand rules/asset policy | 禁止创建/上传/导出/写 Canva，素材授权强制复核 |
| 10 | `jira_service_sla_readonly_agent` | `quality_sprint05_jira_service_sla_readonly_candidate` | 客服/服务台 SLA 包 | `read_only_mock` | Jira Service Management SLA 风险只读分析 | `read_only=true`, 最小 requests/SLA 只读 scope, `write_allowed=false`, `send_allowed=false`, `upload_allowed=false`, `external_action_blocked=true` | sandbox JSM requests/SLA rows | 禁止写 request/issue/comment/status，服务中断强制升级复核 |

## 3. 封装窗口统一要求

- 每个 draft Skill 必须声明 `customer_callable=false`，直到真实 Harness、权限、安全和验收流程完成。
- 每个 read-only Skill 必须声明 `read_only=true`、最小只读 scope、`write_allowed=false`、`send_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- Canva dry-run Skill 必须声明 `send_allowed=false`、`write_allowed=false`、`upload_allowed=false`、`external_action_blocked=true`。
- 输出必须保留 `source_rows`、`source_ids` 或等价证据字段。
- 输出必须保留 `manual_review_required` 和 `manual_review_triggers`。
- 禁止自动发送、发布、上传、写客服/营销/电商/广告/分析/设计/服务台系统、改库存、扣款、退款、创建任务、共享文件。
- 后续如需真实平台 smoke，必须由指挥中心另行批准并使用沙盒账号、最小权限和审计日志。

## 4. 未纳入本封装队列的项

- 媒体/provider route-check passed 候选未纳入本队列；如继续推进，必须走独立真实 provider smoke 审批链路。
- Figma/Asana/Trello/Confluence/BambooHR/Greenhouse/DocuSign passed 候选未纳入本队列；建议后续按协作/HR/签约专题补做正式 L2。
- `needs_more_license_info` 与 `component_only` 项未处理，不能进入本队列。
