# 候选分类与优先级

本文件用于把六部门文档中的 57 个唯一链接拆成可复核、可测试、可封装的候选。当前结论只用于内部调度，不代表 L1/L2/L3 通过。

## 分类口径

| 分类 | 含义 | 是否可送 L2 | 是否可客户调用 |
| --- | --- | --- | --- |
| 已有 13 个可交付 Skill 覆盖 | 业务需求已经可由已验收 13 个 Skill 承接，文档链接不需要重复占名额 | 不需要重复送测 | 可调用的是现有 13 个对应 Skill，不是新候选 |
| 可进入许可证复核 | 链接可能对应轻量 callable Skill 或可借鉴实现，先做 L1 | L1 通过后才可送 | 否 |
| 仅作线索/组件 | 适合作为上游工具、组件、参考流程或内容素材，不宜独立 Skill | 需要组件定位和 L1 通过 | 否 |
| 暂缓/高风险 | 涉及发送、写入、账号、抓取、财务、合同、薪酬、图片/视频生成或许可证不清 | 不送 L2，除非边界补齐 | 否 |

## 已有 13 个 Skill 覆盖关系

| 部门/角色 | 文档需求 | 已有 Skill 覆盖 | 处理建议 |
| --- | --- | --- | --- |
| 创意设计/文案策划 | 广告文案、活动文案、海报文案、卖点表达 | `marketing_copy_pack`, `structured_campaign_brief`, `marketing_compliance_guard` | 先用已验收营销包覆盖，不重复立项 |
| 运营/内容运营 | 内容初稿、分发文案、内容改写 | `marketing_copy_pack`, `structured_campaign_brief`, `marketing_compliance_guard` | 文档链接只作扩展线索 |
| 运营/活动运营 | 活动排期、流程推进、活动文案 | `structured_campaign_brief`, `marketing_copy_pack` | 日历/提醒动作暂缓 |
| 运营/数据运营 | 数据分析、日报周报、数据备注 | `daily_weekly_metrics_reporter`, `structured_metric_summary`, `metric_exception_classifier` | 可直接使用现有经营报表包 |
| 销售/业务员 | 跟进话术、客户介绍、成交跟进 | `crm_note_structurer`, `marketing_copy_pack` | 外呼/邮件发送暂缓 |
| 销售/销售运营 | 销售数据、过程管理、资料支持 | `crm_note_structurer`, `structured_metric_summary`, `daily_weekly_metrics_reporter` | CRM 写入动作暂缓 |
| 电商/推广投放 | 广告文案、投放思路、广告优化 | `marketing_copy_pack`, `structured_campaign_brief`, `marketing_compliance_guard` | 广告平台 API 暂缓 |
| 电商/数据分析 | 转化、商品表现、活动效果 | `structured_metric_summary`, `daily_weekly_metrics_reporter`, `metric_exception_classifier` | 可直接使用现有经营报表包 |
| 客服/售前客服 | 标准回复、话术、客服流程 | `faq_answer_with_citations`, `support_reply_guardrail`, `support_ticket_classifier` | 可直接使用现有客服包 |
| 客服/售后客服 | 售后归类、统计、FAQ 总结 | `support_ticket_classifier`, `faq_answer_with_citations`, `support_kb_doc_cleaner` | 可直接使用现有客服包 |
| 客服/客诉专员 | 投诉、升级、回访 | `support_reply_guardrail`, `support_ticket_classifier`, `faq_answer_with_citations` | 回访动作暂缓，只保留分类和转人工 |
| 客服/质检培训 | 对话质量检查、培训材料 | `support_reply_guardrail`, `support_kb_doc_cleaner` | 新评测候选需另走 L1/L2 |
| 管理/财务 | 单据、报表、费用核对 | `expense_invoice_parser`, `daily_weekly_metrics_reporter`, `structured_metric_summary` | 财务结论和报销合规不可自动输出 |

## 每部门 Top 3 内部候选

说明：Top 3 是优先复核队列，不是通过结论。优先选择轻量、mock 可测、可封装成 callable Skill 的方向；高风险候选只保留观察，不直接送测。

| 部门 | Top 候选方向 | 建议 Skill ID | 来源链接 | 初始分类 | 主要风险 |
| --- | --- | --- | --- | --- | --- |
| 创意设计部门 | 视觉需求提示词/资产简报 | `visual_prompt_brief_candidate` | `https://github.com/eachlabs/skills` | 可进入许可证复核 | 图片生成依赖、素材版权、不可直接生成商业图 |
| 创意设计部门 | 短视频脚本/分镜文本 | `storyboard_script_brief_candidate` | `https://clawhub.ai/skills/text-storyboard-script` | 仅作线索/组件 | ClawHub 许可证不清，不能送 L2 |
| 创意设计部门 | 品牌一致性检查 | `brand_consistency_check_candidate` | `https://clawhub.ai/skills/brand` | 仅作线索/组件 | 品牌规范输入缺失、来源条款不清 |
| 运营部门 | 内容日历规划 | `content_calendar_planner_candidate` | `https://clawhub.ai/clawdssen/content-calendar` | 仅作线索/组件 | ClawHub 许可证不清，日历写入动作暂缓 |
| 运营部门 | 用户反馈聚类摘要 | `feedback_cluster_insights_candidate` | `https://clawhub.ai/jk-0001/customer-feedback` | 仅作线索/组件 | 可能含 PII，需脱敏和人工复核 |
| 运营部门 | 数据运营周报增强 | `operations_metric_brief_candidate` | `https://github.com/anthropics/skills` | 可进入许可证复核 | 与现有报表 Skill 重叠，避免重复封装 |
| 销售部门 | 销售跟进邮件草稿 | `sales_followup_draft_candidate` | `https://github.com/coreyhaines31/marketingskills` | 可进入许可证复核 | 只生成草稿，不发送邮件 |
| 销售部门 | 会议/任务资料整理 | `sales_meeting_task_brief_candidate` | `https://github.com/googleworkspace/cli` | 可进入许可证复核 | Google Workspace 权限、日历/文档写入默认暂缓 |
| 销售部门 | 公开线索调研简报 | `lead_research_brief_candidate` | `https://github.com/tavily-ai/skills` | 可进入许可证复核 | 外部搜索/API、网页事实准确性 |
| 电商部门 | 商品标题和描述优化 | `product_listing_copy_candidate` | `https://github.com/agricidaniel/claude-seo --skill` | 可进入许可证复核 | 链接格式异常，SEO 承诺风险 |
| 电商部门 | 店铺/竞品快照 | `competitor_product_snapshot_candidate` | `https://github.com/apify/agent-skills` | 可进入许可证复核 | 网页抓取、ToS/robots、真实页面访问暂缓 |
| 电商部门 | 订单库存异常分类 | `order_inventory_exception_candidate` | `https://github.com/claude-office-skills/skills` | 可进入许可证复核 | 文件/表格权限，不能写入库存系统 |
| 客服部门 | 客服标准回复/流程 | `support_reply_flow_candidate` | `https://github.com/asgard-ai-platform/skills` | 可进入许可证复核 | 与现有客服包重叠，需找增量点 |
| 客服部门 | 客诉升级和摘要 | `complaint_escalation_summary_candidate` | `https://github.com/anthropics/knowledge-work-plugins` | 可进入许可证复核 | 投诉/退款必须转人工 |
| 客服部门 | 对话质检评测 | `support_quality_eval_candidate` | `https://github.com/github/awesome-copilot` | 可进入许可证复核 | awesome 清单可能只是索引，不一定有可封装代码 |
| 管理部门 | 简历/人事材料脱敏 | `hr_resume_privacy_masker_candidate` | `https://github.com/anthropics/skills` | 可进入许可证复核 | HR PII，高敏隐私 |
| 管理部门 | 票据字段抽取扩展 | `invoice_receipt_review_candidate` | `https://clawhub.ai/skills/expense-invoice-ocr` | 仅作线索/组件 | ClawHub 许可证不清，真实 OCR/税务结论暂缓 |
| 管理部门 | 合同条款分区/风险提示 | `contract_section_review_candidate` | `https://clawhub.ai/1kalin/contract-reviewer` | 暂缓/高风险 | 法律意见风险、许可证不清、需法务边界 |

## 暂缓/高风险清单

| 风险类型 | 涉及链接举例 | 当前动作 |
| --- | --- | --- |
| 邮件发送/API 投递 | `sendgrid`, `resend-send-native-node`, `email-sequence-pack`, `active-campaign`, `getresponse` | 只允许草稿或 dry-run payload，真实发送暂缓 |
| 日历/任务写入 | `cal-com`, `calendar-scheduling`, `opentask`, `sunsama` | 只允许 mock 任务建议，真实创建暂缓 |
| 网页抓取/竞品监控 | `apify/agent-skills`, `data-harvester`, `anysearch`, `woocommerce`, `clawshop-pro` | 只允许 mock HTML/文本，真实抓取需 ToS/robots/URL 审批 |
| 图片/视频生成 | `dlazy-image-generate`, `dlazy-recraft-v3`, `runcomfy-agent-skills`, `video-storyboard-generate` | 生成类依赖和版权未清前暂缓 |
| 财务/票据/报销 | `fl-invoice-tracker`, `simple-ledger`, `expense-invoice-ocr` | 不输出税务、报销、审计结论 |
| 合同/法务 | `contract-reviewer` | 不输出法律意见，需法务边界 |
| 薪酬/人事 | `zoho-people`, `diting-compensation-expert` | 高敏 HR 数据和薪酬决策暂缓 |

## 指挥中心当前判定

- 不从该文档直接新增客户可调用 Skill。
- 研究窗口先补全结构化候选池和每部门 Top 3。
- 许可证窗口先查 14 个 GitHub 链接，ClawHub 只做可核验性初筛。
- 测试台只设计模板，不测试未通过 L1 的候选。
- 封装专员和平台调用验收暂时待命。
