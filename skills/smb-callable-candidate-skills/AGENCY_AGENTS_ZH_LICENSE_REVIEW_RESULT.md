# agency-agents-zh L1 / Source / License Review Result

回传日期：2026-06-05

## 1. 已完成事项

- 已完成 `agency_agents_zh_role_library_candidate` 的 L1/source/license 复核。
- 已按 `AGENCY_AGENTS_ZH_INTAKE_QUEUE.md` 对 Top60 子角色给出 L1 结论。
- 已核验来源定位：`jnMetaCode/agency-agents-zh`，上游项目为 `msitarzewski/agency-agents`。
- 已按产品筛选阶段边界复核 MIT 许可证、上游版权边界、中文本地化声明、脚本写入风险、外部 API/业务动作风险。
- 已生成测试台 role smoke 队列：`queues/AGENCY_AGENTS_ZH_ROLE_SMOKE_QUEUE.md`。
- 本轮未执行脚本、未安装依赖、未写入 OpenClaw/Hermes/Codex/Claude/Copilot 等用户目录、未调用 API、未读取客户文件、未做客户调用；稳交付仍为 13。

## 2. 当前问题

- `agency-agents-zh` 是角色库，不是标准 `SKILL.md` / `skill.yaml` Skill；只能按 role library / role component 进入 smoke，不得直接当作客户可调用 Skill。
- `convert.*` / `install.*` 类脚本存在写入本地工具目录的行为风险，role smoke 阶段必须禁止执行。
- Top60 中采购决策、法律、税务、财务、HR、合同、绩效、反欺诈等 14 个角色属于高风险专业建议方向，建议仅作为 `role_component_only`，不进入 role smoke 队列。
- 角色文件本身是 Markdown 指令，不应触发真实 API；测试台只能验证角色说明在 mock 场景下是否能产生稳定岗位输出。

## 3. 阻塞原因

- 无权限阻塞。
- 无文件写入阻塞。
- 未访问外网；本轮基于已落盘候选卡、队列资料和指挥中心既有来源信息完成产品筛选阶段 L1 复核。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否采纳本轮分流：46 个 `can_role_smoke` 进入 role smoke；14 个 `role_component_only` 不进入 role smoke。
- 是否确认 role smoke 仅验证岗位角色说明稳定性，不等同 L2 通过、不得封装为客户可调用 Skill。
- 是否后续由研究/封装窗口按部门优先级从 46 个放行角色中继续拆分候选卡，而不是一次性纳入全量角色库。

## 5. 建议下一步

- 测试台只读取 `queues/AGENCY_AGENTS_ZH_ROLE_SMOKE_QUEUE.md` 中 46 个 `can_role_smoke` 项。
- 所有 role smoke 使用中文六部门 mock 场景，不读取真实客户文件。
- 禁止执行 `convert.sh` / `install.sh` / `convert.ps1` / `install.ps1`。
- `role_component_only` 角色仅保留为组件线索或人工辅助提示，不进入测试台 role smoke。

## Source / License / Script Review

| 字段 | 复核结论 |
| --- | --- |
| source_project | `jnMetaCode/agency-agents-zh` |
| source_url | `https://github.com/jnMetaCode/agency-agents-zh` |
| upstream_project | `msitarzewski/agency-agents` |
| license_status | MIT；产品筛选阶段可接受，但需保留原作者与中文本地化版权声明 |
| upstream copyright boundary | 上游英文角色库版权归 `msitarzewski/agency-agents` 原作者；中文本地化与中国市场新增角色归 `jnMetaCode/agency-agents-zh` 维护方声明 |
| Chinese localization | 中文社区/本地化版本，包含上游角色翻译/映射及中国市场原创角色；复用时需保留 MIT 许可证与版权声明 |
| commercial_use_notes | MIT 通常允许商用、复制、修改、分发、再许可和销售；但本项目在本平台当前阶段只允许 role smoke，不得客户调用、不得直接 L2、不得封装为正式 Skill |
| upstream_agent_file_verified | Top60 中每项均按队列给出的 `upstream_agent_file` 做来源路径登记；本地未执行角色文件 |
| convert script behavior | `convert.sh` / `convert.ps1` 属于格式转换脚本，预期会将 Markdown 角色转成 OpenClaw/Hermes/Codex/Claude/Copilot 等工具格式；测试阶段禁止执行 |
| install script behavior | `install.sh` / `install.ps1` 存在写入用户或项目工具目录风险，包括 `.claude/agents`、`.github`、`.copilot`、`.openclaw`、`.codex/agents`、`.hermes/skills`、`.cursor/rules`、`.opencode/agents` 等；可能调用 `openclaw agents add`；测试阶段禁止执行 |
| dependency install risk | 本轮不安装；角色库本身不应需要依赖安装。README 若引导安装外部 orchestrator 或 CLI，不纳入 role smoke |
| external_api_risk | 角色 Markdown 本身不调用 API；凡涉及邮件、CRM、广告平台、地图、任务系统、财务、合同、HR、税务等真实动作，统一 `external_action_blocked` |
| final_trial_mode | `mock_only`, `read_only`, `external_action_blocked` |

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_role_smoke` | 46 |
| `role_component_only` | 14 |
| `needs_more_license_info` | 0 |
| `blocked` | 0 |

## Top60 L1 Review Table

| rank | department | role | upstream_agent_file | license_status | commercial_use_notes | upstream_agent_file_verified | script_write_risk | external_api_risk | final_trial_mode | l1_result |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 创意设计部门 | 美工/视觉设计 | `design/design-image-prompt-engineer.md` | MIT | 仅做视觉提示词/素材构思，不生成真实图片 | true | install scripts write tool dirs; execution forbidden | image generation provider risk if used beyond mock | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 2 | 创意设计部门 | 品牌设计 | `design/design-brand-guardian.md` | MIT | 品牌一致性检查需使用用户自有品牌规范 | true | install scripts write tool dirs; execution forbidden | brand/trademark review only; no external API | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 3 | 创意设计部门 | 视觉设计 | `design/design-ui-designer.md` | MIT | UI/页面视觉评审只输出建议，不改文件 | true | install scripts write tool dirs; execution forbidden | design artifact/write risk blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 4 | 创意设计部门 | 用户研究 | `design/design-ux-researcher.md` | MIT | 只处理 mock 或已授权反馈，不读取真实访谈资料 | true | install scripts write tool dirs; execution forbidden | research PII risk; no real interview data | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 5 | 创意设计部门 | 视觉叙事 | `design/design-visual-storyteller.md` | MIT | 仅做活动视觉故事线 brief，不生成媒体 | true | install scripts write tool dirs; execution forbidden | no media generation | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 6 | 运营部门 | 内容运营 | `marketing/marketing-content-creator.md` | MIT | 内容初稿不发布、不保证营销效果 | true | install scripts write tool dirs; execution forbidden | platform publishing blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 7 | 运营部门 | 内容运营 | `marketing/marketing-daily-news-briefing.md` | MIT | 行业资讯摘要需用户提供素材，不抓取新闻 | true | install scripts write tool dirs; execution forbidden | no web fetch/news API in smoke | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 8 | 运营部门 | 增长运营 | `marketing/marketing-carousel-growth-engine.md` | MIT | 轮播内容增长策略不发布、不投放 | true | install scripts write tool dirs; execution forbidden | social platform action blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 9 | 运营部门 | 中国市场运营 | `marketing/marketing-china-market-localization-strategist.md` | MIT | 本地化营销策略需合规人工复核 | true | install scripts write tool dirs; execution forbidden | regulated industries risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 10 | 运营部门 | SEO/搜索运营 | `marketing/marketing-baidu-seo-specialist.md` | MIT | SEO 策略不承诺排名，不调用搜索 API | true | install scripts write tool dirs; execution forbidden | no search crawl/API | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 11 | 运营部门 | AI 搜索运营 | `marketing/marketing-ai-citation-strategist.md` | MIT | AI 引用策略不保证被收录 | true | install scripts write tool dirs; execution forbidden | no external search/API | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 12 | 运营部门 | 应用运营 | `marketing/marketing-app-store-optimizer.md` | MIT | ASO 建议不修改应用商店资料 | true | install scripts write tool dirs; execution forbidden | app store API/action blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 13 | 销售部门 | 业务员 | `sales/sales-outbound-strategist.md` | MIT | 外联策略只生成草稿，不发送、不外呼 | true | install scripts write tool dirs; execution forbidden | email/call/CRM blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 14 | 销售部门 | 销售教练 | `sales/sales-coach.md` | MIT | 销售训练建议不替代绩效评估 | true | install scripts write tool dirs; execution forbidden | no external API | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 15 | 销售部门 | 商机策略 | `sales/sales-deal-strategist.md` | MIT | 商机推进不承诺折扣、合同或成交 | true | install scripts write tool dirs; execution forbidden | CRM/deal write blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 16 | 销售部门 | 需求发现 | `sales/sales-discovery-coach.md` | MIT | 只输出发现问题清单草稿 | true | install scripts write tool dirs; execution forbidden | no external API | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 17 | 销售部门 | 售前方案 | `sales/sales-engineer.md` | MIT | 售前技术方案需人工确认能力边界 | true | install scripts write tool dirs; execution forbidden | technical claims risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 18 | 销售部门 | 销售运营 | `sales/sales-pipeline-analyst.md` | MIT | 管道分析只读 mock 数据，不写 CRM | true | install scripts write tool dirs; execution forbidden | CRM/API blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 19 | 销售部门 | 方案撰写 | `sales/sales-proposal-strategist.md` | MIT | 提案策略草稿不构成合同或承诺 | true | install scripts write tool dirs; execution forbidden | contract/proposal commitment risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 20 | 电商部门 | 商品运营 | `marketing/marketing-china-ecommerce-operator.md` | MIT | 电商运营建议不写店铺、不改商品 | true | install scripts write tool dirs; execution forbidden | store/API action blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 21 | 电商部门 | 跨境电商 | `marketing/marketing-cross-border-ecommerce.md` | MIT | 跨境电商建议需合规/关务/税务人工复核 | true | install scripts write tool dirs; execution forbidden | marketplace/customs/tax risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 22 | 电商部门 | 小红书运营 | `marketing/marketing-xiaohongshu-operator.md` | MIT | 种草策略不发布、不登录平台 | true | install scripts write tool dirs; execution forbidden | platform rule/content risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 23 | 电商部门 | B站运营 | `marketing/marketing-bilibili-strategist.md` | MIT | B站内容策略不发布、不上传 | true | install scripts write tool dirs; execution forbidden | platform publishing blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 24 | 电商部门 | 推广投放 | `paid-media/paid-media-creative-strategist.md` | MIT | 投放创意策略不投放广告 | true | install scripts write tool dirs; execution forbidden | ad platform/API blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 25 | 电商部门 | 搜索投放 | `paid-media/paid-media-ppc-strategist.md` | MIT | PPC 策略不改预算、不写广告账户 | true | install scripts write tool dirs; execution forbidden | ad account/API blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 26 | 电商部门 | 投放分析 | `paid-media/paid-media-search-query-analyst.md` | MIT | 搜索词分析只读 mock 数据，不读取真实广告账户 | true | install scripts write tool dirs; execution forbidden | ad data/API blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 27 | 电商部门 | 库存预测 | `supply-chain/supply-chain-inventory-forecaster.md` | MIT | 库存预测草稿不改库存、不触发补货 | true | install scripts write tool dirs; execution forbidden | inventory/write risk blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 28 | 电商部门 | 供应商评估 | `supply-chain/supply-chain-vendor-evaluator.md` | MIT | 供应商对比涉及采购/合同风险，仅可作为组件线索 | true | install scripts write tool dirs; execution forbidden | procurement/contract high risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 29 | 客服部门 | 售前客服 | `support/support-support-responder.md` | MIT | 客服回复建议不发送、不承诺退款 | true | install scripts write tool dirs; execution forbidden | customer PII/refund risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 30 | 客服部门 | 客服主管 | `support/support-executive-summary-generator.md` | MIT | 客服周报仅为 mock 工单摘要 | true | install scripts write tool dirs; execution forbidden | ticket PII risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 31 | 客服部门 | 数据分析 | `support/support-analytics-reporter.md` | MIT | 客服指标摘要不做自动经营决策 | true | install scripts write tool dirs; execution forbidden | data quality risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 32 | 客服部门 | 法务合规协作 | `support/support-legal-compliance-checker.md` | MIT | 合规检查仅作提示，非法律意见 | true | install scripts write tool dirs; execution forbidden | legal/compliance high risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 33 | 客服部门 | 财务协作 | `support/support-finance-tracker.md` | MIT | 退款/费用跟踪仅作草稿，非财务结论 | true | install scripts write tool dirs; execution forbidden | finance/refund high risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 34 | 管理部门 | 财务 | `finance/finance-bookkeeper-controller.md` | MIT | 记账/往来检查不做客户可调用结论 | true | install scripts write tool dirs; execution forbidden | bookkeeping/accounting high risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 35 | 管理部门 | 财务分析 | `finance/finance-financial-analyst.md` | MIT | 财务分析摘要非财务建议 | true | install scripts write tool dirs; execution forbidden | financial advice risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 36 | 管理部门 | 经营预测 | `finance/finance-financial-forecaster.md` | MIT | 经营预测草稿不可作为决策依据 | true | install scripts write tool dirs; execution forbidden | forecast/finance risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 37 | 管理部门 | FP&A | `finance/finance-fpa-analyst.md` | MIT | 预算/经营分析非审计或财务意见 | true | install scripts write tool dirs; execution forbidden | FP&A/high-stakes finance | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 38 | 管理部门 | 反欺诈 | `finance/finance-fraud-detector.md` | MIT | 仅作异常线索，不做欺诈判定 | true | install scripts write tool dirs; execution forbidden | fraud/false positive risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 39 | 管理部门 | 票据 | `finance/finance-invoice-manager.md` | MIT | 发票/单据管理不做报销、税务或审计结论 | true | install scripts write tool dirs; execution forbidden | invoice/tax/audit risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 40 | 管理部门 | 税务 | `finance/finance-tax-strategist.md` | MIT | 税务事项仅提示专业复核，非税务意见 | true | install scripts write tool dirs; execution forbidden | tax advice high risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 41 | 管理部门 | 招聘 | `hr/hr-recruiter.md` | MIT | 招聘支持不得输出录用/淘汰结论 | true | install scripts write tool dirs; execution forbidden | HR PII/bias risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 42 | 管理部门 | 绩效 | `hr/hr-performance-reviewer.md` | MIT | 绩效草稿不得用于自动处罚或正式评定 | true | install scripts write tool dirs; execution forbidden | HR/performance high risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 43 | 管理部门 | 合同 | `legal/legal-contract-reviewer.md` | MIT | 合同风险提示非法律意见 | true | install scripts write tool dirs; execution forbidden | legal advice high risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 44 | 管理部门 | 政策制度 | `legal/legal-policy-writer.md` | MIT | 公司制度草稿需法务/HR 审核 | true | install scripts write tool dirs; execution forbidden | legal/HR policy risk | `mock_only`, `read_only`, `external_action_blocked` | `role_component_only` |
| 45 | 管理部门 | 项目管理 | `project-management/project-management-project-shepherd.md` | MIT | 项目推进只做风险清单，不写任务系统 | true | install scripts write tool dirs; execution forbidden | no external API | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 46 | 管理部门 | 流程管理 | `project-management/project-management-jira-workflow-steward.md` | MIT | 任务流转规则不写 Jira 或任务系统 | true | install scripts write tool dirs; execution forbidden | Jira/API/write risk blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 47 | 管理部门 | 实验管理 | `project-management/project-management-experiment-tracker.md` | MIT | 实验追踪不改真实实验系统 | true | install scripts write tool dirs; execution forbidden | analytics/project write blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 48 | 管理部门 | 采购供应 | `supply-chain/supply-chain-strategist.md` | MIT | 供应链策略为草稿，需人工决策 | true | install scripts write tool dirs; execution forbidden | procurement/logistics risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 49 | 管理部门 | 路线/配送 | `supply-chain/supply-chain-route-optimizer.md` | MIT | 路线建议不调用地图、调度或物流 API | true | install scripts write tool dirs; execution forbidden | routing/map/API risk blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 50 | 管理部门 | 生产计划 | `supply-chain/supply-chain-garment-factory-planning-engineer.md` | MIT | 生产排程草稿需人工确认，不写生产系统 | true | install scripts write tool dirs; execution forbidden | production planning risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 51 | 运营部门 | 产品运营 | `product/product-growth-pm.md` | MIT | 产品增长假设不改线上产品 | true | install scripts write tool dirs; execution forbidden | experiment/product write blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 52 | 运营部门 | 产品经理 | `product/product-manager.md` | MIT | 产品需求梳理为草稿，不写项目系统 | true | install scripts write tool dirs; execution forbidden | roadmap/customer data risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 53 | 运营部门 | 用户体验 | `product/product-ux-researcher.md` | MIT | 用户体验研究只处理 mock 或授权反馈 | true | install scripts write tool dirs; execution forbidden | user PII/interview risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 54 | 运营部门 | 市场策略 | `strategy/strategy-growth-strategist.md` | MIT | 增长策略不做预算、投放或真实执行 | true | install scripts write tool dirs; execution forbidden | strategy/financial implication | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 55 | 运营部门 | 商业策略 | `strategy/strategy-business-strategist.md` | MIT | 商业策略仅为讨论稿，不作正式决策 | true | install scripts write tool dirs; execution forbidden | business decision risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 56 | 运营部门 | 数据策略 | `strategy/strategy-data-strategist.md` | MIT | 数据策略不连接真实数据源 | true | install scripts write tool dirs; execution forbidden | data governance/privacy risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 57 | 创意设计部门 | 社媒设计 | `marketing/marketing-social-media-manager.md` | MIT | 社媒排期不发布内容 | true | install scripts write tool dirs; execution forbidden | social platform/API blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 58 | 销售部门 | 客户策略 | `sales/sales-account-strategist.md` | MIT | 客户经营策略不写 CRM、不触达客户 | true | install scripts write tool dirs; execution forbidden | CRM/customer data risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 59 | 电商部门 | 广告审计 | `paid-media/paid-media-auditor.md` | MIT | 投放账户审计草稿不登录广告账户 | true | install scripts write tool dirs; execution forbidden | ad account/API risk | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
| 60 | 电商部门 | 追踪分析 | `paid-media/paid-media-tracking-specialist.md` | MIT | 追踪检查不改站点、不写像素 | true | install scripts write tool dirs; execution forbidden | tracking/pixel/site write blocked | `mock_only`, `read_only`, `external_action_blocked` | `can_role_smoke` |
