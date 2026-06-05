# agency_agents_zh_role_library_candidate

## 当前状态
- status: needs_license_review
- source_type: agent_role_library
- skill_source_class: agent_role_compatible
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- role_smoke_status: not_started
- formal_l2_status: not_applicable_yet
- count_towards_candidate_cards: true

## 来源
- source_project: jnMetaCode/agency-agents-zh
- source_url: https://github.com/jnMetaCode/agency-agents-zh
- upstream_project: msitarzewski/agency-agents
- license: MIT, pending license window verification
- upstream_format: Markdown agent role files, not SKILL.md / skill.yaml
- runtime_fit: OpenClaw/Hermes/Codex compatible via repository convert/install scripts, pending verification

## 入库定位

该项目作为“六部门 Agent 角色库候选源”入库，不作为单个客户可调用 Skill。后续需要按子角色拆分、许可证复核、角色 smoke，再决定哪些角色能进入平台角色库或组合 Skill 编排层。

## 六部门适配

- 创意设计部门: design、marketing 视觉/品牌/内容角色
- 运营部门: marketing、product、project-management、strategy 角色
- 销售部门: sales 角色
- 电商部门: marketing、paid-media、supply-chain 角色
- 客服部门: support 角色
- 管理部门: finance、hr、legal、project-management、supply-chain 角色

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- install_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true

## 禁止动作
- 不安装 agency-orchestrator 或仓库脚本到生产环境
- 不执行真实 convert/install 脚本写入用户工具目录
- 不发送消息、不写 CRM/日历/任务/业务系统
- 不读取真实客户文件、不上传文件
- 不调用真实外部 API 或模型供应商
- 不把角色 smoke 通过写成 L2 通过

## 人工复核触发
- 许可证或上游版权边界不清
- 角色包含法律、税务、财务、医疗、招聘、绩效等高风险建议
- 角色需要真实账号、外部 API、安装脚本或文件写入
- 与现有稳交付 13 个 Skill 或候选库重复

## Top60 子角色筛选队列摘要

| rank | 六部门 | 角色 | upstream_agent_file | 适配说明 | 当前状态 | 下一步 |
|---:|---|---|---|---|---|---|
| 1 | 创意设计部门 | 美工/视觉设计 | `design/design-image-prompt-engineer.md` | 视觉提示词/素材构思，需避免真实图片生成 | needs_license_review | role_smoke_pending |
| 2 | 创意设计部门 | 品牌设计 | `design/design-brand-guardian.md` | 品牌一致性与视觉规范检查 | needs_license_review | role_smoke_pending |
| 3 | 创意设计部门 | 视觉设计 | `design/design-ui-designer.md` | UI/页面视觉评审 | needs_license_review | role_smoke_pending |
| 4 | 创意设计部门 | 用户研究 | `design/design-ux-researcher.md` | 用户访谈/反馈研究 | needs_license_review | role_smoke_pending |
| 5 | 创意设计部门 | 视觉叙事 | `design/design-visual-storyteller.md` | 活动视觉故事线 | needs_license_review | role_smoke_pending |
| 6 | 运营部门 | 内容运营 | `marketing/marketing-content-creator.md` | 内容选题与初稿 | needs_license_review | role_smoke_pending |
| 7 | 运营部门 | 内容运营 | `marketing/marketing-daily-news-briefing.md` | 行业资讯摘要 | needs_license_review | role_smoke_pending |
| 8 | 运营部门 | 增长运营 | `marketing/marketing-carousel-growth-engine.md` | 轮播内容增长策略 | needs_license_review | role_smoke_pending |
| 9 | 运营部门 | 中国市场运营 | `marketing/marketing-china-market-localization-strategist.md` | 本地化营销策略 | needs_license_review | role_smoke_pending |
| 10 | 运营部门 | SEO/搜索运营 | `marketing/marketing-baidu-seo-specialist.md` | 百度 SEO 内容策略 | needs_license_review | role_smoke_pending |
| 11 | 运营部门 | AI 搜索运营 | `marketing/marketing-ai-citation-strategist.md` | AI 引用可见性策略 | needs_license_review | role_smoke_pending |
| 12 | 运营部门 | 应用运营 | `marketing/marketing-app-store-optimizer.md` | 应用商店优化 | needs_license_review | role_smoke_pending |
| 13 | 销售部门 | 业务员 | `sales/sales-outbound-strategist.md` | 外呼/外联策略草稿 | needs_license_review | role_smoke_pending |
| 14 | 销售部门 | 销售教练 | `sales/sales-coach.md` | 销售话术训练 | needs_license_review | role_smoke_pending |
| 15 | 销售部门 | 商机策略 | `sales/sales-deal-strategist.md` | 商机推进策略 | needs_license_review | role_smoke_pending |
| 16 | 销售部门 | 需求发现 | `sales/sales-discovery-coach.md` | 销售发现问题清单 | needs_license_review | role_smoke_pending |
| 17 | 销售部门 | 售前方案 | `sales/sales-engineer.md` | 售前技术方案支持 | needs_license_review | role_smoke_pending |
| 18 | 销售部门 | 销售运营 | `sales/sales-pipeline-analyst.md` | 销售管道分析 | needs_license_review | role_smoke_pending |
| 19 | 销售部门 | 方案撰写 | `sales/sales-proposal-strategist.md` | 提案策略草稿 | needs_license_review | role_smoke_pending |
| 20 | 电商部门 | 商品运营 | `marketing/marketing-china-ecommerce-operator.md` | 中国电商运营 | needs_license_review | role_smoke_pending |
| 21 | 电商部门 | 跨境电商 | `marketing/marketing-cross-border-ecommerce.md` | 跨境电商运营 | needs_license_review | role_smoke_pending |
| 22 | 电商部门 | 小红书运营 | `marketing/marketing-xiaohongshu-operator.md` | 小红书种草策略 | needs_license_review | role_smoke_pending |
| 23 | 电商部门 | B 站运营 | `marketing/marketing-bilibili-strategist.md` | B 站内容策略 | needs_license_review | role_smoke_pending |
| 24 | 电商部门 | 推广投放 | `paid-media/paid-media-creative-strategist.md` | 投放创意策略 | needs_license_review | role_smoke_pending |
| 25 | 电商部门 | 搜索投放 | `paid-media/paid-media-ppc-strategist.md` | PPC 策略草稿 | needs_license_review | role_smoke_pending |
| 26 | 电商部门 | 投放分析 | `paid-media/paid-media-search-query-analyst.md` | 搜索词分析 | needs_license_review | role_smoke_pending |
| 27 | 电商部门 | 库存预测 | `supply-chain/supply-chain-inventory-forecaster.md` | 库存预测/补货建议 | needs_license_review | role_smoke_pending |
| 28 | 电商部门 | 供应商评估 | `supply-chain/supply-chain-vendor-evaluator.md` | 供应商对比 | needs_license_review | role_smoke_pending |
| 29 | 客服部门 | 售前客服 | `support/support-support-responder.md` | 客服回复建议 | needs_license_review | role_smoke_pending |
| 30 | 客服部门 | 客服主管 | `support/support-executive-summary-generator.md` | 客服周报/主管摘要 | needs_license_review | role_smoke_pending |
| 31 | 客服部门 | 数据分析 | `support/support-analytics-reporter.md` | 客服指标摘要 | needs_license_review | role_smoke_pending |
| 32 | 客服部门 | 法务合规协作 | `support/support-legal-compliance-checker.md` | 客服合规检查 | needs_license_review | role_smoke_pending |
| 33 | 客服部门 | 财务协作 | `support/support-finance-tracker.md` | 客服退款/费用跟踪草稿 | needs_license_review | role_smoke_pending |
| 34 | 管理部门 | 财务 | `finance/finance-bookkeeper-controller.md` | 记账/往来检查 | needs_license_review | role_smoke_pending |
| 35 | 管理部门 | 财务分析 | `finance/finance-financial-analyst.md` | 财务分析摘要 | needs_license_review | role_smoke_pending |
| 36 | 管理部门 | 经营预测 | `finance/finance-financial-forecaster.md` | 经营预测草稿 | needs_license_review | role_smoke_pending |
| 37 | 管理部门 | FP&A | `finance/finance-fpa-analyst.md` | 预算/经营分析 | needs_license_review | role_smoke_pending |
| 38 | 管理部门 | 反欺诈 | `finance/finance-fraud-detector.md` | 异常交易提示 | needs_license_review | role_smoke_pending |
| 39 | 管理部门 | 票据 | `finance/finance-invoice-manager.md` | 发票/单据管理 | needs_license_review | role_smoke_pending |
| 40 | 管理部门 | 税务 | `finance/finance-tax-strategist.md` | 税务事项提示，非税务意见 | needs_license_review | role_smoke_pending |
| 41 | 管理部门 | 招聘 | `hr/hr-recruiter.md` | 招聘 JD/筛选支持 | needs_license_review | role_smoke_pending |
| 42 | 管理部门 | 绩效 | `hr/hr-performance-reviewer.md` | 绩效评估草稿 | needs_license_review | role_smoke_pending |
| 43 | 管理部门 | 合同 | `legal/legal-contract-reviewer.md` | 合同条款风险提示 | needs_license_review | role_smoke_pending |
| 44 | 管理部门 | 政策制度 | `legal/legal-policy-writer.md` | 公司制度草稿 | needs_license_review | role_smoke_pending |
| 45 | 管理部门 | 项目管理 | `project-management/project-management-project-shepherd.md` | 项目推进和风险清单 | needs_license_review | role_smoke_pending |
| 46 | 管理部门 | 流程管理 | `project-management/project-management-jira-workflow-steward.md` | 任务流转规则 | needs_license_review | role_smoke_pending |
| 47 | 管理部门 | 实验管理 | `project-management/project-management-experiment-tracker.md` | 实验进度追踪 | needs_license_review | role_smoke_pending |
| 48 | 管理部门 | 采购供应 | `supply-chain/supply-chain-strategist.md` | 供应链策略草稿 | needs_license_review | role_smoke_pending |
| 49 | 管理部门 | 路线/配送 | `supply-chain/supply-chain-route-optimizer.md` | 配送路线建议 | needs_license_review | role_smoke_pending |
| 50 | 管理部门 | 生产计划 | `supply-chain/supply-chain-garment-factory-planning-engineer.md` | 生产排程草稿 | needs_license_review | role_smoke_pending |
| 51 | 运营部门 | 产品运营 | `product/product-growth-pm.md` | 产品增长假设 | needs_license_review | role_smoke_pending |
| 52 | 运营部门 | 产品经理 | `product/product-manager.md` | 产品需求梳理 | needs_license_review | role_smoke_pending |
| 53 | 运营部门 | 用户体验 | `product/product-ux-researcher.md` | 用户体验研究 | needs_license_review | role_smoke_pending |
| 54 | 运营部门 | 市场策略 | `strategy/strategy-growth-strategist.md` | 增长策略 | needs_license_review | role_smoke_pending |
| 55 | 运营部门 | 商业策略 | `strategy/strategy-business-strategist.md` | 商业策略 | needs_license_review | role_smoke_pending |
| 56 | 运营部门 | 数据策略 | `strategy/strategy-data-strategist.md` | 数据策略 | needs_license_review | role_smoke_pending |
| 57 | 创意设计部门 | 社媒设计 | `marketing/marketing-social-media-manager.md` | 社媒内容排期 | needs_license_review | role_smoke_pending |
| 58 | 销售部门 | 客户策略 | `sales/sales-account-strategist.md` | 客户经营策略 | needs_license_review | role_smoke_pending |
| 59 | 电商部门 | 广告审计 | `paid-media/paid-media-auditor.md` | 投放账户审计草稿 | needs_license_review | role_smoke_pending |
| 60 | 电商部门 | 追踪分析 | `paid-media/paid-media-tracking-specialist.md` | 投放追踪检查 | needs_license_review | role_smoke_pending |

## 下一步
1. 许可证窗口复核 MIT、上游英文版与中文本地化版权边界、脚本行为和商用限制。
2. 研究窗口按六部门筛 Top60 子角色，不直接展开全仓 215 个。
3. 测试台在 L1 放行后做 role smoke，每个角色至少 1 个中文岗位场景 mock。
4. 封装窗口后续按“角色包候选”封装，不生成独立客户可调用 Skill。
