# 中小微候选库研究 Top 18 回传

回传时间：2026-06-03

## 研究边界

本轮只读候选调用库治理文件，未访问外网、未安装依赖、未登录账号、未提交表单、未写入外部系统、未请求权限。

稳交付库仍只有 13 个客户可调用 Skill，不扩容。

## 当前结论

| 分类 | 数量 | 说明 |
| --- | ---: | --- |
| 已存在候选 | 5 | 2 个 `draft_l3`，3 个 `component_only` |
| 可送许可证复核 | 8 | GitHub 或明确来源候选，需 L1 |
| 市场线索 | 5 | 主要为 ClawHub/文档来源，许可证和商用条款不清 |
| 客户可调用新增 | 0 | 不改变稳交付 13 个基线 |

## 六大业务包 Top 18

| candidate_id | business_package | target_role | job_to_be_done | source_type | source_url | covered_by_stable_13 | suggested_status | risk_hint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `support_quality_eval_candidate` | 客服 | 客服主管 / 质检培训 | 对客服对话做质检评分、失败项标注、培训建议 | GitHub | `https://github.com/github/awesome-copilot` | 部分覆盖：`support_reply_guardrail` | `needs_license_review` | awesome 清单可能只是索引，需找真实上游；只做评分建议 |
| `complaint_escalation_summary_candidate` | 客服 | 客诉专员 | 投诉内容摘要、风险等级、转人工原因 | GitHub | `https://github.com/anthropics/knowledge-work-plugins` | 部分覆盖：`support_ticket_classifier`, `support_reply_guardrail` | `needs_license_review` | 投诉、退款、赔偿必须人工复核 |
| `support_reply_flow_candidate` | 客服 | 售前/售后客服 | 标准回复流程、知识依据、转人工判断 | GitHub | `https://github.com/asgard-ai-platform/skills` | 已覆盖：`faq_answer_with_citations`, `support_ticket_classifier` | `needs_license_review` | 与稳交付客服包重叠，需找增量点 |
| `sales_followup_draft_candidate` | 销售 | 业务员 / 销售运营 | 生成销售跟进草稿，不发送、不写 CRM | GitHub | `https://github.com/coreyhaines31/marketingskills` | 部分覆盖：`crm_note_structurer` | 已存在：`draft_l3` | 固定 `send_allowed=false` |
| `sales_meeting_task_brief_candidate` | 销售 | 销售助理 | 会议纪要、行动项、dry-run 日历/任务 payload | GitHub | `https://github.com/googleworkspace/cli` | 否 | 已存在：`component_only` | OAuth/日历写入禁止，只 dry-run |
| `lead_research_brief_candidate` | 销售 | 商务支持 / 业务员 | 基于已提供页面文本生成潜客简报和跟进角度 | GitHub | `https://github.com/tavily-ai/skills` | 否 | 已存在：`component_only` | 不搜索、不抓取、不调用 Tavily，需来源引用 |
| `visual_prompt_brief_candidate` | 营销 | 美工 / 视觉设计 | 输出视觉 prompt brief、素材需求、品牌约束 | GitHub | `https://github.com/eachlabs/skills` | 部分覆盖：`structured_campaign_brief` | 已存在：`draft_l3` | 不生成图片，不声明素材授权 |
| `content_calendar_planner_candidate` | 营销 | 内容运营 / 活动运营 | 生成内容日历、发布主题、渠道计划 | 文档来源 / ClawHub | `https://clawhub.ai/clawdssen/content-calendar` | 部分覆盖：`structured_campaign_brief` | `market_lead` | ClawHub 条款不清；不写日历 |
| `brand_consistency_check_candidate` | 营销 | 品牌设计 / 文案策划 | 检查品牌语气、禁用表达、修改建议 | 文档来源 / ClawHub | `https://clawhub.ai/skills/brand` | 部分覆盖：`marketing_compliance_guard` | `market_lead` | 来源条款不清，需品牌规范输入 |
| `product_listing_copy_candidate` | 电商/门店 | 商品运营 | 商品标题、卖点、详情页文案草稿 | GitHub | `https://github.com/agricidaniel/claude-seo --skill` | 部分覆盖：`marketing_copy_pack` | `needs_license_review` | 链接格式异常；SEO 排名承诺风险 |
| `competitor_product_snapshot_candidate` | 电商/门店 | 店铺运营 | 基于 mock/授权页面快照输出竞品对比 | GitHub | `https://github.com/apify/agent-skills` | 否 | 已存在：`component_only` | 不真实抓取；ToS/robots 风险 |
| `order_inventory_exception_candidate` | 电商/门店 | 订单/库存运营 | 根据订单/库存表识别异常和核查步骤 | GitHub | `https://github.com/claude-office-skills/skills` | 否 | `needs_license_review` | 不写库存系统；只输出建议 |
| `operations_metric_brief_candidate` | 经营报表 | 数据运营 / 老板 | 运营指标摘要、变化解释、下一步检查 | GitHub | `https://github.com/anthropics/skills` | 已覆盖：`daily_weekly_metrics_reporter`, `structured_metric_summary` | `needs_license_review` | 与稳交付报表包重叠，避免重复封装 |
| `ecommerce_metric_brief_candidate` | 经营报表 | 电商数据分析 | 商品表现、活动效果、转化摘要 | GitHub | `https://github.com/astronomer/agents` | 已覆盖：`structured_metric_summary`, `metric_exception_classifier` | `needs_license_review` | 可能偏大型框架；只取轻量摘要任务 |
| `data_harvester_metric_lead` | 经营报表 | 数据运营 | 数据采集/报表线索 | 文档来源 / ClawHub | `https://clawhub.ai/dxg852621787/data-harvester` | 已覆盖：经营报表 3 Skill | `market_lead` | 抓取/BI 接入风险高，暂不 L2 |
| `hr_resume_privacy_masker_candidate` | 行政/财务/HR | 行政人事 / HR | 简历和人事材料脱敏 | GitHub | `https://github.com/anthropics/skills` | 部分复用：`support_pii_redactor` | `needs_license_review` | HR PII 高敏；必须人工复核 |
| `invoice_receipt_review_candidate` | 行政/财务/HR | 财务 | 票据字段复核、金额一致性提示 | 文档来源 / ClawHub | `https://clawhub.ai/skills/expense-invoice-ocr` | 已覆盖：`expense_invoice_parser` | `market_lead` | 不能输出税务/审计/报销结论 |
| `contract_section_review_candidate` | 行政/财务/HR | 法务/合同 | 合同条款分区、风险提示 | 文档来源 / ClawHub | `https://clawhub.ai/1kalin/contract-reviewer` | 否 | `market_lead` | 法律意见风险，必须 `not_legal_advice=true` |

## 可送许可证窗口

| candidate_id | source_type | source_url | 复核重点 |
| --- | --- | --- | --- |
| `support_quality_eval_candidate` | GitHub | `https://github.com/github/awesome-copilot` | 是否只是索引；可封装上游；LICENSE/SPDX |
| `complaint_escalation_summary_candidate` | GitHub | `https://github.com/anthropics/knowledge-work-plugins` | LICENSE、插件依赖、投诉/知识工作边界 |
| `support_reply_flow_candidate` | GitHub | `https://github.com/asgard-ai-platform/skills` | LICENSE、是否可独立封装、与客服稳交付包重叠 |
| `product_listing_copy_candidate` | GitHub | `https://github.com/agricidaniel/claude-seo --skill` | 链接纠错、LICENSE、SEO 承诺风险 |
| `order_inventory_exception_candidate` | GitHub | `https://github.com/claude-office-skills/skills` | LICENSE、文件读写权限、订单/库存 Skill 粒度 |
| `operations_metric_brief_candidate` | GitHub | `https://github.com/anthropics/skills` | LICENSE、与稳交付报表包重叠、是否仅示例 |
| `ecommerce_metric_brief_candidate` | GitHub | `https://github.com/astronomer/agents` | LICENSE、是否大型框架、可裁剪性 |
| `hr_resume_privacy_masker_candidate` | GitHub | `https://github.com/anthropics/skills` | LICENSE、HR PII、脱敏能力是否可独立封装 |

## 暂不送许可证窗口

以下候选先保留为 `market_lead`：

- `content_calendar_planner_candidate`
- `brand_consistency_check_candidate`
- `data_harvester_metric_lead`
- `invoice_receipt_review_candidate`
- `contract_section_review_candidate`

原因：来源为 ClawHub/文档来源，许可证和商用条款不清；先做来源可核验性初筛。
