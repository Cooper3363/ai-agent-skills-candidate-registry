# agency-agents-zh 六部门 Top60 角色库研究细化

更新日期: 2026-06-05

## 1. 已完成事项

- 已读取 `AGENCY_AGENTS_ZH_INTAKE_RESULT.md` 与 `queues/AGENCY_AGENTS_ZH_INTAKE_QUEUE.md`。
- 已按六部门角色表复核 Top60 子角色：创意设计、运营、销售、电商、客服、管理。
- 已为每个子角色补充：部门、岗位、上游 agent 文件、业务场景、推荐使用方式、与现有 13 稳交付 Skill / 151 候选重复关系、角色类型。
- 已明确 `agency-agents-zh` 是 Markdown Agent 角色库来源，不是标准 `SKILL.md` / `skill.yaml` Skill，不直接写成平台标准 Skill。

## 2. 当前问题

- `agency-agents-zh` 仍需许可证窗口确认 MIT、上游英文版版权边界、convert/install 脚本行为和商用限制。
- Top60 子角色目前只能作为“角色库来源 / role smoke 候选”，不能直接进入 Skill L2 或客户调用。
- 部分角色涉及投放、税务、财务、法律、绩效、招聘、库存、路线等高风险领域，必须保留 mock / read-only / dry-run / human_review_required 边界。

## 3. 阻塞原因

无权限阻塞。未安装脚本、未执行 convert/install、未调用真实 API、未访问真实账号、未改稳交付库。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否允许 `role_ready` 子角色在 L1/source verification 通过后进入 role smoke。
- 是否将 `role_component_only` 子角色仅作为现有候选能力的角色提示词补充，不单独落候选卡。
- 是否要求许可证窗口先统一复核 `agency-agents-zh` 源级候选，再对子角色分批放行。

## 5. 建议下一步

- 许可证窗口先做源级 L1：LICENSE、上游版权、脚本行为、商用边界。
- 研究窗口建议优先送 role smoke 的批次：创意设计 1-5、运营 6-12、销售 13-19、客服 29-32。
- 管理部门中的税务、法律、绩效、反欺诈、路线优化、生产计划先保守处理，不进入客户可调用。

## 6. 角色类型口径

| 角色类型 | 含义 | 下一步 |
| --- | --- | --- |
| `role_ready` | 中小微岗位场景清楚，适合 L1 后做 role smoke | 许可证通过后送 role smoke |
| `needs_license_review` | 场景有价值，但涉及外部动作、高风险专业领域或来源边界 | 先做 L1/source verification |
| `role_component_only` | 与现有 13 稳交付 Skill 或 151 候选高度重叠，只适合作提示词/角色组件 | 不单独作为 Skill |
| `not_smb_fit` | 对中小微不够通用，或风险/复杂度超过本阶段 | 暂缓 |

## 7. Top60 子角色细化表

| rank | 部门 | 岗位 | 上游 agent 文件 | 业务场景 | 推荐使用方式 | 与现有 13 稳交付 Skill / 151 候选重复关系 | 角色类型 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | 创意设计 | 美工/视觉设计 | `design/design-image-prompt-engineer.md` | 海报、商品图、活动图的视觉提示词和素材构思 | 只做视觉 brief / prompt 草稿，不生成真实图片，不声明素材授权 | 与 To50 `visual_prompt_brief_candidate`、To150 `native_visual_prompt_brief_skill_candidate` 高度相邻 | `role_component_only` |
| 2 | 创意设计 | 品牌设计 | `design/design-brand-guardian.md` | 品牌语气、视觉规范、禁用表达检查 | 作为品牌一致性 role smoke，输入品牌规范和物料草稿 | 与 `marketing_compliance_guard`、To100 `brand_forbidden_words_checker_candidate` 部分重复 | `role_ready` |
| 3 | 创意设计 | 视觉设计 | `design/design-ui-designer.md` | 页面、落地页、后台界面视觉评审 | 只做 read-only 评审和修改建议，不改设计文件 | 与 To150 `compatible_design_system_review_skill_candidate` 相邻 | `role_ready` |
| 4 | 创意设计 | 用户研究 | `design/design-ux-researcher.md` | 用户访谈问题、反馈归纳、体验痛点 | 只处理 mock/脱敏访谈文本，输出洞察和待验证假设 | 与 To150 `native_customer_research_skill_candidate` 相邻 | `role_component_only` |
| 5 | 创意设计 | 视觉叙事 | `design/design-visual-storyteller.md` | 活动视觉故事线、短视频分镜、品牌叙事 | 作为营销视觉策划角色，不生成媒体 | 与 `structured_campaign_brief`、To100 视频/视觉 brief 候选相邻 | `role_ready` |
| 6 | 运营 | 内容运营 | `marketing/marketing-content-creator.md` | 公众号、社媒、活动内容初稿 | 只输出文案草稿和渠道建议，不发布 | 与 `marketing_copy_pack` 高度重叠 | `role_component_only` |
| 7 | 运营 | 内容运营 | `marketing/marketing-daily-news-briefing.md` | 行业资讯摘要、门店/电商晨会 brief | 仅基于用户提供素材做摘要，不抓新闻 | 与 To100 `support_ticket_batch_summary_candidate`、报表摘要类部分相邻 | `role_ready` |
| 8 | 运营 | 增长运营 | `marketing/marketing-carousel-growth-engine.md` | 小红书/LinkedIn/朋友圈轮播内容增长策略 | 输出轮播结构和文案草稿，不发布 | 与 To100 `social_content`、To150 `native_social_content_skill_candidate` 相邻 | `role_ready` |
| 9 | 运营 | 中国市场运营 | `marketing/marketing-china-market-localization-strategist.md` | 中国市场本地化文案、渠道和表达调整 | 用作本地化策略 role smoke，禁止声称真实市场效果 | 与 To100 本地活动、营销策略候选相邻 | `role_ready` |
| 10 | 运营 | SEO/搜索运营 | `marketing/marketing-baidu-seo-specialist.md` | 百度 SEO 内容方向、页面标题和 FAQ 建议 | 只基于用户提供页面文本输出 SEO 建议，不抓网页、不承诺排名 | 与 To150 `native_seo_audit_skill_candidate`、`native_ai_seo_skill_candidate` 相邻 | `role_component_only` |
| 11 | 运营 | AI 搜索运营 | `marketing/marketing-ai-citation-strategist.md` | AI 搜索引用可见性、答案片段策略 | 只输出结构化内容建议，不承诺被引用 | 与 To100 `ai_search_answer_snippet_candidate`、To150 GEO/AI SEO 候选相邻 | `role_component_only` |
| 12 | 运营 | 应用运营 | `marketing/marketing-app-store-optimizer.md` | 应用商店标题、描述、关键词优化 | 只处理 mock app listing，不承诺排名 | 与 To150 `native_aso_listing_skill_candidate` 相邻 | `role_component_only` |
| 13 | 销售 | 业务员 | `sales/sales-outbound-strategist.md` | 外呼、外联、陌拜策略和话术草稿 | dry-run，仅生成话术和节奏，不发送、不写 CRM | 与 To100 `outbound_message_personalizer_candidate`、`native_cold_email_skill_candidate` 相邻 | `role_ready` |
| 14 | 销售 | 销售教练 | `sales/sales-coach.md` | 销售话术训练、异议处理演练 | 用作训练角色，输入 mock 对话，输出改进建议 | 与 To50 `quote_objection_response_candidate` 相邻 | `role_ready` |
| 15 | 销售 | 商机策略 | `sales/sales-deal-strategist.md` | 商机推进策略、风险和下一步建议 | 只输出建议，不推进 CRM 阶段 | 与 To50 `deal_risk_flagger_candidate`、To100 销售阶段候选相邻 | `role_component_only` |
| 16 | 销售 | 需求发现 | `sales/sales-discovery-coach.md` | 销售发现问题、客户需求澄清 | 生成 discovery 问题清单和访谈结构 | 与 To100 `proposal_requirement_gap_checker_candidate` 相邻 | `role_ready` |
| 17 | 销售 | 售前方案 | `sales/sales-engineer.md` | 售前技术方案、客户需求到功能映射 | 只输出方案 brief，不承诺实施/价格 | 与 To50 `proposal_outline_candidate` 相邻 | `role_component_only` |
| 18 | 销售 | 销售运营 | `sales/sales-pipeline-analyst.md` | 销售漏斗、商机阶段、转化异常分析 | 只处理 mock CRM 表，不写 CRM | 与 `crm_note_structurer`、To100 `crm_pipeline_summary_candidate` 相邻 | `role_component_only` |
| 19 | 销售 | 方案撰写 | `sales/sales-proposal-strategist.md` | 提案策略、大纲、差异化卖点 | 只生成提案草稿和风险提示 | 与 To50 `proposal_outline_candidate`、To100 `quote_scope_change_summary_candidate` 相邻 | `role_ready` |
| 20 | 电商 | 商品运营 | `marketing/marketing-china-ecommerce-operator.md` | 中国电商商品、活动、平台运营策略 | 只做运营建议和 mock 商品策略，不登录平台 | 与 To50 `product_listing_copy_candidate`、To100 电商候选相邻 | `role_ready` |
| 21 | 电商 | 跨境电商 | `marketing/marketing-cross-border-ecommerce.md` | 跨境商品文案、渠道和合规提示 | 只输出策略草稿，不做平台发布和物流承诺 | 与商品文案、投放、供应链候选相邻 | `role_ready` |
| 22 | 电商 | 小红书运营 | `marketing/marketing-xiaohongshu-operator.md` | 小红书种草、笔记结构、话题策略 | 只输出笔记草稿，不发布、不刷量 | 与 To100 社媒/UGC 广告角度候选相邻 | `role_ready` |
| 23 | 电商 | B 站运营 | `marketing/marketing-bilibili-strategist.md` | B 站视频选题、脚本和投放策略 | 只输出脚本/brief，不生成或发布视频 | 与 To150 `native_video_brief_skill_candidate` 相邻 | `role_ready` |
| 24 | 电商 | 推广投放 | `paid-media/paid-media-creative-strategist.md` | 投放创意策略和素材 brief | dry-run，不投放、不改预算、不承诺转化 | 与 To150 `native_ads_planning_skill_candidate`、`native_ad_creative_skill_candidate` 相邻 | `needs_license_review` |
| 25 | 电商 | 搜索投放 | `paid-media/paid-media-ppc-strategist.md` | PPC 账户策略和关键词投放建议 | dry-run，不登录广告账户、不改预算 | 与 paid ads native 候选相邻 | `needs_license_review` |
| 26 | 电商 | 投放分析 | `paid-media/paid-media-search-query-analyst.md` | 搜索词报告分析、否词建议 | 只处理用户提供报表，不写广告账户 | 与 To100 经营报表/投放追踪候选相邻 | `needs_license_review` |
| 27 | 电商 | 库存预测 | `supply-chain/supply-chain-inventory-forecaster.md` | 库存预测、补货建议、缺货预警 | 只用 mock 库存销量表，不生成采购单 | 与 To50 `order_inventory_exception_candidate`、库存周转候选相邻 | `role_component_only` |
| 28 | 电商 | 供应商评估 | `supply-chain/supply-chain-vendor-evaluator.md` | 供应商评分、报价、交期对比 | 只输出对比建议，不能自动选择供应商 | 与 To50 `purchase_quote_compare_candidate`、To100 供应商风险候选相邻 | `role_ready` |
| 29 | 客服 | 售前客服 | `support/support-support-responder.md` | 售前/售后回复建议 | 只输出客服回复草稿，不发送、不承诺赔偿 | 与 `faq_answer_with_citations`、`support_reply_guardrail` 高度重叠 | `role_component_only` |
| 30 | 客服 | 客服主管 | `support/support-executive-summary-generator.md` | 客服周报、班次摘要、升级事项 | 作为客服主管摘要角色，输入工单/对话 mock | 与 To100 `support_ticket_batch_summary_candidate` 相邻 | `role_ready` |
| 31 | 客服 | 数据分析 | `support/support-analytics-reporter.md` | 客服指标摘要、趋势和异常 | 只处理 mock 指标表，不写系统 | 与报表稳交付 3 件套、To100 客服摘要候选相邻 | `role_component_only` |
| 32 | 客服 | 法务合规协作 | `support/support-legal-compliance-checker.md` | 客服回复中的合规/法律风险提示 | 只输出风险提示和转人工，不给法律意见 | 与 `support_reply_guardrail`、合同/法律候选相邻 | `needs_license_review` |
| 33 | 客服 | 财务协作 | `support/support-finance-tracker.md` | 退款、费用、补偿跟踪草稿 | 只做记录草稿，不退款、不赔偿、不写财务系统 | 与 `expense_invoice_parser`、退款回复候选相邻 | `needs_license_review` |
| 34 | 管理 | 财务 | `finance/finance-bookkeeper-controller.md` | 记账、往来、费用分类检查 | 只能做 mock/read-only 检查，不给审计结论 | 与 `expense_invoice_parser`、费用异常候选相邻 | `needs_license_review` |
| 35 | 管理 | 财务分析 | `finance/finance-financial-analyst.md` | 财务分析摘要、收入成本结构 | 只输出摘要和核查建议，不给投资/融资建议 | 与报表稳交付和现金流候选相邻 | `role_component_only` |
| 36 | 管理 | 经营预测 | `finance/finance-financial-forecaster.md` | 收入、成本、现金流预测草稿 | 只做假设草稿，不作财务建议 | 与 To100 现金流、盈亏平衡、目标进度候选相邻 | `needs_license_review` |
| 37 | 管理 | FP&A | `finance/finance-fpa-analyst.md` | 预算、经营分析、差异解释 | 只输出预算差异解释，不改预算 | 与 To100 `budget_variance_explainer_candidate` 相邻 | `role_component_only` |
| 38 | 管理 | 反欺诈 | `finance/finance-fraud-detector.md` | 异常交易、重复报销、风险线索 | 只输出人工复核线索，不做欺诈定性 | 与重复票据、费用异常候选相邻 | `needs_license_review` |
| 39 | 管理 | 票据 | `finance/finance-invoice-manager.md` | 发票/单据字段、金额、状态整理 | 只处理 mock OCR/文本，不做税务/报销结论 | 与 `expense_invoice_parser`、票据一致性组件高度重叠 | `role_component_only` |
| 40 | 管理 | 税务 | `finance/finance-tax-strategist.md` | 税务事项提示和资料准备 | 不给税务意见，只输出“需专业复核”的材料清单 | 高风险，To100 已将税务表述 guard 暂缓 | `not_smb_fit` |
| 41 | 管理 | 招聘 | `hr/hr-recruiter.md` | JD、候选人追问、面试流程支持 | 只输出 JD/问题，不自动录用或淘汰 | 与 To100 HR 简历、面试问题候选相邻 | `role_ready` |
| 42 | 管理 | 绩效 | `hr/hr-performance-reviewer.md` | 绩效评估草稿、反馈结构化 | 只输出反馈草稿，不用于处罚/薪酬决策 | 与员工产能快照候选相邻，高风险 | `needs_license_review` |
| 43 | 管理 | 合同 | `legal/legal-contract-reviewer.md` | 合同条款摘要、风险提示 | 只输出非法律意见和人工复核点 | 与 To50 合同条款候选相邻，高风险 | `needs_license_review` |
| 44 | 管理 | 政策制度 | `legal/legal-policy-writer.md` | 公司制度、通知、内部政策草稿 | 只做制度草稿，必须人工审核 | 与 To100 政策通知候选相邻 | `role_ready` |
| 45 | 管理 | 项目管理 | `project-management/project-management-project-shepherd.md` | 项目推进、里程碑、风险清单 | 只输出计划和风险，不写任务系统 | 与 To100 会议/任务 dry-run 候选相邻 | `role_ready` |
| 46 | 管理 | 流程管理 | `project-management/project-management-jira-workflow-steward.md` | 任务流转、看板状态、流程规则 | 只输出流程建议，不写 Jira/任务系统 | 偏工具流程，SMB 可用但需 dry-run | `needs_license_review` |
| 47 | 管理 | 实验管理 | `project-management/project-management-experiment-tracker.md` | 增长实验进度、假设和指标追踪 | 只输出实验看板摘要，不改系统 | 与 To150 `native_ab_testing_skill_candidate` 相邻 | `role_component_only` |
| 48 | 管理 | 采购供应 | `supply-chain/supply-chain-strategist.md` | 供应链策略、采购计划、风险 | 只输出策略和核查清单，不下单 | 与采购报价、供应商风险候选相邻 | `role_ready` |
| 49 | 管理 | 路线/配送 | `supply-chain/supply-chain-route-optimizer.md` | 配送路线和调度建议 | 涉及路线优化和真实配送，先只做 mock，不接真实地图/API | 对多数 SMB 平台客户复杂度偏高 | `not_smb_fit` |
| 50 | 管理 | 生产计划 | `supply-chain/supply-chain-garment-factory-planning-engineer.md` | 服装工厂生产排程 | 垂直行业强，先作为制造业线索，不进入通用 SMB | 与通用六部门不够贴合 | `not_smb_fit` |
| 51 | 运营 | 产品运营 | `product/product-growth-pm.md` | 产品增长假设、功能转化路径 | 只输出增长假设和实验建议 | 与 To150 增长、AB testing 候选相邻 | `role_ready` |
| 52 | 运营 | 产品经理 | `product/product-manager.md` | 需求梳理、PRD、功能优先级 | 只输出 PRD 草稿和需求澄清，不写开发系统 | 与项目管理/运营候选相邻 | `role_ready` |
| 53 | 运营 | 用户体验 | `product/product-ux-researcher.md` | UX 研究、反馈归纳、问题假设 | 只处理脱敏反馈，不抓用户数据 | 与 `native_customer_research_skill_candidate`、设计 UX 角色重复 | `role_component_only` |
| 54 | 运营 | 市场策略 | `strategy/strategy-growth-strategist.md` | 增长策略、渠道、目标和实验 | 只输出策略草稿，不改预算 | 与营销计划/增长候选相邻 | `role_ready` |
| 55 | 运营 | 商业策略 | `strategy/strategy-business-strategist.md` | 商业模式、定价、市场进入策略 | 只输出分析框架和假设，不作投资/财务结论 | 与定价、经营策略候选相邻 | `needs_license_review` |
| 56 | 运营 | 数据策略 | `strategy/strategy-data-strategist.md` | 指标体系、数据口径、分析路线 | 只输出指标和口径建议，不接真实数据源 | 与报表稳交付和数据质量候选相邻 | `role_component_only` |
| 57 | 创意设计 | 社媒设计 | `marketing/marketing-social-media-manager.md` | 社媒内容排期、视觉和文案方向 | 只输出排期/文案/视觉 brief，不发布 | 与内容日历、社媒内容候选高度相邻 | `role_component_only` |
| 58 | 销售 | 客户策略 | `sales/sales-account-strategist.md` | 重点客户经营策略、续约/扩展路径 | 只输出账户计划，不写 CRM、不承诺价格 | 与客户成功、续费、商机策略候选相邻 | `role_ready` |
| 59 | 电商 | 广告审计 | `paid-media/paid-media-auditor.md` | 投放账户审计草稿和问题清单 | 只用用户提供报表，不登录广告账户 | 高风险外部账户场景，需 L1 和 dry-run | `needs_license_review` |
| 60 | 电商 | 追踪分析 | `paid-media/paid-media-tracking-specialist.md` | 转化追踪、埋点、UTM 检查 | 只输出检查清单，不改 GTM/广告账户 | 与 To150 `native_analytics_tracking_skill_candidate` 相邻 | `role_component_only` |

## 8. 类型汇总

| 角色类型 | 数量 |
| --- | ---: |
| `role_ready` | 24 |
| `needs_license_review` | 16 |
| `role_component_only` | 17 |
| `not_smb_fit` | 3 |
| 合计 | 60 |

## 9. 优先进入 role smoke 建议

| 优先级 | 子角色 | 原因 |
| --- | --- | --- |
| P0 | `design/design-brand-guardian.md`、`design/design-ui-designer.md`、`design/design-visual-storyteller.md` | 低权限、适合 mock、与中小微营销设计高频匹配 |
| P0 | `marketing/marketing-daily-news-briefing.md`、`marketing/marketing-carousel-growth-engine.md`、`marketing/marketing-china-market-localization-strategist.md` | 输出稳定，外部动作少，可用用户提供素材 |
| P0 | `sales/sales-outbound-strategist.md`、`sales/sales-coach.md`、`sales/sales-discovery-coach.md`、`sales/sales-proposal-strategist.md` | 销售高频岗位场景清楚，dry-run 边界可控 |
| P0 | `support/support-executive-summary-generator.md` | 客服主管摘要适合 role smoke，低权限 |
| P1 | 电商内容/供应商评估类角色 | 适合中小微，但需避免真实平台账号和采购决策 |
| 暂缓 | 税务、路线优化、服装生产计划 | 专业风险或垂直行业过强 |

## 10. 边界声明

- `agency-agents-zh` 的 Markdown agent 只作为角色库来源，不是标准 Skill。
- 本文件不生成 `SKILL.md`、`skill.yaml`，不把任何子角色宣称为客户可调用。
- 本轮不安装脚本、不调用真实 API、不改稳交付库。
- 客户正式可调用 Skill 仍为 13。
