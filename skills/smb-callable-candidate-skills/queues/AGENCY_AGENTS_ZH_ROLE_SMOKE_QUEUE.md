# Agency Agents ZH Role Smoke Queue

生成日期：2026-06-05

来源：`AGENCY_AGENTS_ZH_LICENSE_REVIEW_RESULT.md`

本队列只包含 L1 放行的 `can_role_smoke` 角色。`role_component_only`、`needs_more_license_info`、`blocked` 不得进入本队列。

统一边界：

- 不执行真实安装脚本。
- 不写 OpenClaw/Hermes/Codex/Claude/Copilot 等用户目录。
- 不调用真实业务 API。
- 不读取真实客户文件。
- 不客户调用。
- Role smoke 只验证角色说明能否产生稳定岗位输出，不等同 L2 通过。
- 稳交付库仍为 13。

## Queue

| rank | department | role | upstream_agent_file | final_trial_mode | l1_result | role smoke 边界 |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | 创意设计部门 | 美工/视觉设计 | `design/design-image-prompt-engineer.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不生成真实图片 |
| 2 | 创意设计部门 | 品牌设计 | `design/design-brand-guardian.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 只用用户提供品牌规范 |
| 3 | 创意设计部门 | 视觉设计 | `design/design-ui-designer.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改页面或文件 |
| 4 | 创意设计部门 | 用户研究 | `design/design-ux-researcher.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 只处理 mock 或授权反馈 |
| 5 | 创意设计部门 | 视觉叙事 | `design/design-visual-storyteller.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不生成媒体 |
| 6 | 运营部门 | 内容运营 | `marketing/marketing-content-creator.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不发布 |
| 7 | 运营部门 | 内容运营 | `marketing/marketing-daily-news-briefing.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不抓取新闻 |
| 8 | 运营部门 | 增长运营 | `marketing/marketing-carousel-growth-engine.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不发布、不投放 |
| 9 | 运营部门 | 中国市场运营 | `marketing/marketing-china-market-localization-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 合规人工复核 |
| 10 | 运营部门 | SEO/搜索运营 | `marketing/marketing-baidu-seo-specialist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不承诺排名 |
| 11 | 运营部门 | AI 搜索运营 | `marketing/marketing-ai-citation-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不调用搜索 API |
| 12 | 运营部门 | 应用运营 | `marketing/marketing-app-store-optimizer.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改应用商店 |
| 13 | 销售部门 | 业务员 | `sales/sales-outbound-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不外呼、不发送 |
| 14 | 销售部门 | 销售教练 | `sales/sales-coach.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不做绩效结论 |
| 15 | 销售部门 | 商机策略 | `sales/sales-deal-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不写 CRM |
| 16 | 销售部门 | 需求发现 | `sales/sales-discovery-coach.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 只输出问题清单 |
| 17 | 销售部门 | 售前方案 | `sales/sales-engineer.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不承诺技术交付 |
| 18 | 销售部门 | 销售运营 | `sales/sales-pipeline-analyst.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不写 CRM |
| 19 | 销售部门 | 方案撰写 | `sales/sales-proposal-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不构成合同 |
| 20 | 电商部门 | 商品运营 | `marketing/marketing-china-ecommerce-operator.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不写店铺 |
| 21 | 电商部门 | 跨境电商 | `marketing/marketing-cross-border-ecommerce.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 跨境合规人工复核 |
| 22 | 电商部门 | 小红书运营 | `marketing/marketing-xiaohongshu-operator.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不发布 |
| 23 | 电商部门 | B站运营 | `marketing/marketing-bilibili-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不发布 |
| 24 | 电商部门 | 推广投放 | `paid-media/paid-media-creative-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不投放 |
| 25 | 电商部门 | 搜索投放 | `paid-media/paid-media-ppc-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改预算或账户 |
| 26 | 电商部门 | 投放分析 | `paid-media/paid-media-search-query-analyst.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不读真实广告账户 |
| 27 | 电商部门 | 库存预测 | `supply-chain/supply-chain-inventory-forecaster.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改库存 |
| 29 | 客服部门 | 售前客服 | `support/support-support-responder.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不发送回复 |
| 30 | 客服部门 | 客服主管 | `support/support-executive-summary-generator.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | mock 工单摘要 |
| 31 | 客服部门 | 数据分析 | `support/support-analytics-reporter.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | mock 指标 |
| 45 | 管理部门 | 项目管理 | `project-management/project-management-project-shepherd.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不写任务系统 |
| 46 | 管理部门 | 流程管理 | `project-management/project-management-jira-workflow-steward.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不写 Jira |
| 47 | 管理部门 | 实验管理 | `project-management/project-management-experiment-tracker.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改实验系统 |
| 48 | 管理部门 | 采购供应 | `supply-chain/supply-chain-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不做采购决策 |
| 49 | 管理部门 | 路线/配送 | `supply-chain/supply-chain-route-optimizer.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不调用地图 API |
| 50 | 管理部门 | 生产计划 | `supply-chain/supply-chain-garment-factory-planning-engineer.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改生产计划 |
| 51 | 运营部门 | 产品运营 | `product/product-growth-pm.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改线上产品 |
| 52 | 运营部门 | 产品经理 | `product/product-manager.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 只做需求草稿 |
| 53 | 运营部门 | 用户体验 | `product/product-ux-researcher.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | mock 或授权反馈 |
| 54 | 运营部门 | 市场策略 | `strategy/strategy-growth-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不执行投放 |
| 55 | 运营部门 | 商业策略 | `strategy/strategy-business-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 仅讨论稿 |
| 56 | 运营部门 | 数据策略 | `strategy/strategy-data-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不接真实数据源 |
| 57 | 创意设计部门 | 社媒设计 | `marketing/marketing-social-media-manager.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不发布 |
| 58 | 销售部门 | 客户策略 | `sales/sales-account-strategist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不写 CRM |
| 59 | 电商部门 | 广告审计 | `paid-media/paid-media-auditor.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不登录广告账户 |
| 60 | 电商部门 | 追踪分析 | `paid-media/paid-media-tracking-specialist.md` | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` | 不改站点或像素 |
