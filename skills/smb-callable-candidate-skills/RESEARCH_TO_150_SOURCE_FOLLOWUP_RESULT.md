# To150 Agent Skill 来源补充研究结果

回传时间：2026-06-03

## 1. 已完成事项

- 已读取 `RESEARCH_TO_150_NATIVE_SKILLS_RESULT.md`、`queues/RESEARCH_TO_150_NATIVE_SKILLS_QUEUE.md`。
- 已读取并核对 `candidates/needs_license_review/` 下 50 张新增候选卡。
- 已确认 45 个 `native_agent_skill` 候选的本地 `SKILL.md` 均存在。
- 已确认 5 个 `agent_skill_compatible` 候选仍需要许可证窗口 / 研究窗口继续定位具体公开上游子目录、许可证和 manifest。
- 已确认候选目录下未发现上游 `skill.yaml`，当前均依赖 registry 自己生成 `candidate.yaml`，后续如进入平台适配需再生成 OpenClaw/Hermes/DeepAgents manifest 映射。

## 2. 当前问题

- 45 个 native 候选来自本机 Codex skills，已验证 `SKILL.md` 文件存在，但尚未完成商用授权、再分发边界、平台迁移边界复核。
- 5 个 compatible 候选只有公开 GitHub / Agent Skill 兼容线索，尚未确认具体子目录、是否存在 `SKILL.md`、许可证和商用边界。
- 当前没有可直接声明为 OpenClaw/OpenClow 或 Hermes 已原生兼容的证据，只能标为 `adapter_pending`。

## 3. 阻塞原因

无权限阻塞。未安装依赖、未运行项目、未调用真实业务 API、未访问真实账号、未写外部系统、未请求权限。

两个 Windows 通配路径查询出现路径语法错误，属于本地命令写法问题，不影响已完成的候选卡读取和统计结论。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否允许 45 个本地 Codex `SKILL.md` 来源候选继续作为 `native_agent_skill` 路线推进 L1，但在许可证窗口重点检查“是否可迁移/再分发/平台商用”。
- 是否要求 OpenClaw/OpenClow、Hermes 适配窗口先提供标准 manifest/schema；否则本轮只能输出 `candidate.yaml` 和 `adapter_pending`，不能宣称已可导入。
- 5 个 compatible 候选是否继续投入公开来源定位；若无法定位具体 `SKILL.md` 子目录，建议保持 `needs_more_source_info`，不送 smoke。

## 5. 建议下一步

- 许可证窗口先处理 45 个已验证本地 `SKILL.md` 存在的 native 候选，重点看授权、迁移和外部动作边界。
- 研究窗口或许可证窗口对 5 个 compatible 候选逐项定位公开仓库具体子目录、LICENSE、README、`SKILL.md` / manifest。
- 平台适配窗口等待 OpenClaw/Hermes schema 后，再把 `candidate.yaml` 映射为平台调用 manifest。

## 6. 总体统计

| 分类 | 数量 | 来源证据结论 | 建议动作 |
| --- | ---: | --- | --- |
| `native_agent_skill` | 45 | 本地 `SKILL.md` 已验证存在 | 可送 L1/source verification，不可直接客户调用 |
| `agent_skill_compatible` | 5 | 公开来源线索存在，但具体子目录 / manifest 未核实 | 需补上游定位后再决定是否 L1 |
| 已发现上游 `skill.yaml` | 0 | 候选目录未发现上游 `skill.yaml` | registry 需自行维护 `candidate.yaml` / manifest 映射 |
| OpenClaw/OpenClow 已导入证据 | 0 | 未见真实导入日志或 manifest | 标记 `adapter_pending` |
| Hermes 已导入证据 | 0 | 未见真实导入日志或 manifest | 标记 `adapter_pending` |
| DeepAgents 可迁移证据 | 45 | 本地 `SKILL.md` 结构可作为迁移输入 | 需 L1 后再 smoke |

## 7. 45 个 native_agent_skill 来源证据表

统一结论：

- `native_agent_skill`：已验证本地存在 `SKILL.md`。
- `skill.yaml / manifest`：未发现上游 `skill.yaml`，当前候选卡已由 registry 生成 `candidate.yaml`。
- OpenClaw/OpenClow：`adapter_pending`，需平台 schema。
- Hermes：`adapter_pending`，需平台 schema。
- DeepAgents：`migratable_after_L1`，但不得跳过许可证 / source verification。

| candidate_id | 本地 SKILL.md 路径 | native_agent_skill 是否已验证 | skill.yaml / manifest 状态 | 与稳交付 13 / 既有 100 关系 | 复核建议 |
| --- | --- | --- | --- | --- | --- |
| `native_ab_testing_skill_candidate` | `C:/Users/Administrator/.codex/skills/ab-testing/SKILL.md` | 是 | 需 registry 生成 manifest | 与经营报表/增长候选相邻 | L1 检查实验建议边界，不得输出确定因果 |
| `native_ad_creative_skill_candidate` | `C:/Users/Administrator/.codex/skills/ad-creative/SKILL.md` | 是 | 需 registry 生成 manifest | 部分重叠 `marketing_copy_pack` | L1 检查广告承诺、禁词和外部投放禁止 |
| `native_ads_planning_skill_candidate` | `C:/Users/Administrator/.codex/skills/ads/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销投放候选相邻 | 仅 dry-run，禁止真实投放和预算调整 |
| `native_ai_seo_skill_candidate` | `C:/Users/Administrator/.codex/skills/ai-seo/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销/SEO 候选相邻 | 禁止承诺排名或 AI 引用结果 |
| `native_analytics_tracking_skill_candidate` | `C:/Users/Administrator/.codex/skills/analytics/SKILL.md` | 是 | 需 registry 生成 manifest | 与经营报表和数据质量候选相邻 | 只输出埋点/口径建议，不写 GTM/系统 |
| `native_aso_listing_skill_candidate` | `C:/Users/Administrator/.codex/skills/aso/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销内容候选相邻 | 只处理 mock 应用商店文案，不承诺排名 |
| `native_churn_prevention_skill_candidate` | `C:/Users/Administrator/.codex/skills/churn-prevention/SKILL.md` | 是 | 需 registry 生成 manifest | 与销售/客户成功候选相邻 | 禁止自动发优惠或改订阅 |
| `native_co_marketing_skill_candidate` | `C:/Users/Administrator/.codex/skills/co-marketing/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销合作候选相邻 | 只输出合作 brief，不联系外部伙伴 |
| `native_cold_email_skill_candidate` | `C:/Users/Administrator/.codex/skills/cold-email/SKILL.md` | 是 | 需 registry 生成 manifest | 与销售邮件候选相邻 | dry-run，禁止发送邮件 |
| `native_community_marketing_skill_candidate` | `C:/Users/Administrator/.codex/skills/community-marketing/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销/客户运营候选相邻 | 禁止真实发帖或社群操作 |
| `native_competitor_profiling_skill_candidate` | `C:/Users/Administrator/.codex/skills/competitor-profiling/SKILL.md` | 是 | 需 registry 生成 manifest | 与竞品快照组件相邻 | 仅用用户提供文本，不抓网页 |
| `native_competitor_comparison_skill_candidate` | `C:/Users/Administrator/.codex/skills/competitors/SKILL.md` | 是 | 需 registry 生成 manifest | 与竞品/营销内容候选相邻 | 禁止诋毁竞品，需证据字段 |
| `native_content_strategy_skill_candidate` | `C:/Users/Administrator/.codex/skills/content-strategy/SKILL.md` | 是 | 需 registry 生成 manifest | 部分重叠内容日历候选 | 可 L1，定位为内容策略 mock 输出 |
| `native_copy_editing_skill_candidate` | `C:/Users/Administrator/.codex/skills/copy-editing/SKILL.md` | 是 | 需 registry 生成 manifest | 部分重叠 `marketing_copy_pack` | 适合作为文案润色组件 |
| `native_copywriting_skill_candidate` | `C:/Users/Administrator/.codex/skills/copywriting/SKILL.md` | 是 | 需 registry 生成 manifest | 高度相邻 `marketing_copy_pack` | 建议组件化，避免重复稳交付 |
| `native_cro_skill_candidate` | `C:/Users/Administrator/.codex/skills/cro/SKILL.md` | 是 | 需 registry 生成 manifest | 与增长/落地页候选相邻 | 只输出优化建议，不改页面 |
| `native_customer_research_skill_candidate` | `C:/Users/Administrator/.codex/skills/customer-research/SKILL.md` | 是 | 需 registry 生成 manifest | 与客服洞察和评价聚类相邻 | 需 PII 脱敏和样本量提示 |
| `native_directory_submissions_skill_candidate` | `C:/Users/Administrator/.codex/skills/directory-submissions/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销获客相邻 | dry-run，禁止提交目录表单 |
| `native_email_sequence_skill_candidate` | `C:/Users/Administrator/.codex/skills/emails/SKILL.md` | 是 | 需 registry 生成 manifest | 与销售邮件/私域候选相邻 | dry-run，禁止发送和写营销平台 |
| `native_free_tool_planner_skill_candidate` | `C:/Users/Administrator/.codex/skills/free-tools/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销获客相邻 | 只输出工具方案，不开发/发布 |
| `native_geo_citation_audit_skill_candidate` | `C:/Users/Administrator/.codex/skills/geo-citation-agent/SKILL.md` | 是 | 需 registry 生成 manifest | 与 AI SEO 候选相邻 | 禁止承诺被引用；需来源证据 |
| `native_image_marketing_skill_candidate` | `C:/Users/Administrator/.codex/skills/image/SKILL.md` | 是 | 需 registry 生成 manifest | 与视觉 brief 候选相邻 | dry-run，仅生成 brief，不生成真实图片 |
| `native_launch_planning_skill_candidate` | `C:/Users/Administrator/.codex/skills/launch/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销运营候选相邻 | 可 mock，用于活动/新品发布计划 |
| `native_lead_magnet_skill_candidate` | `C:/Users/Administrator/.codex/skills/lead-magnets/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销获客候选相邻 | 只输出 lead magnet 方案 |
| `native_marketing_ideas_skill_candidate` | `C:/Users/Administrator/.codex/skills/marketing-ideas/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销策略候选相邻 | 适合作策略灵感，不作为执行动作 |
| `native_marketing_plan_skill_candidate` | `C:/Users/Administrator/.codex/skills/marketing-plan/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销策略候选相邻 | 输出计划，不改预算或投放 |
| `native_marketing_psychology_skill_candidate` | `C:/Users/Administrator/.codex/skills/marketing-psychology/SKILL.md` | 是 | 需 registry 生成 manifest | 与文案风险/营销内容相邻 | 避免操纵性或敏感人群建议 |
| `native_onboarding_skill_candidate` | `C:/Users/Administrator/.codex/skills/onboarding/SKILL.md` | 是 | 需 registry 生成 manifest | 与客户成功/入职概念相邻 | 明确是用户 onboarding，不是 HR 入职 |
| `native_paywall_optimization_skill_candidate` | `C:/Users/Administrator/.codex/skills/paywalls/SKILL.md` | 是 | 需 registry 生成 manifest | 与增长候选相邻 | 只输出建议，不改付费墙 |
| `native_popup_optimization_skill_candidate` | `C:/Users/Administrator/.codex/skills/popups/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销转化候选相邻 | 只输出弹窗策略，不改站点 |
| `native_pricing_strategy_skill_candidate` | `C:/Users/Administrator/.codex/skills/pricing/SKILL.md` | 是 | 需 registry 生成 manifest | 与销售报价/经营策略相邻 | 价格建议需人工复核，不作财务结论 |
| `native_product_marketing_context_skill_candidate` | `C:/Users/Administrator/.codex/skills/product-marketing/SKILL.md` | 是 | 需 registry 生成 manifest | 与营销策略候选相邻 | 适合作上下文整理组件 |
| `native_programmatic_seo_skill_candidate` | `C:/Users/Administrator/.codex/skills/programmatic-seo/SKILL.md` | 是 | 需 registry 生成 manifest | 与 SEO 候选相邻 | 禁止承诺排名；不生成真实站点 |
| `native_prospecting_skill_candidate` | `C:/Users/Administrator/.codex/skills/prospecting/SKILL.md` | 是 | 需 registry 生成 manifest | 与销售获客候选相邻 | 仅用户提供资料，不抓取真实线索 |
| `native_referral_program_skill_candidate` | `C:/Users/Administrator/.codex/skills/referrals/SKILL.md` | 是 | 需 registry 生成 manifest | 与客户成功/营销候选相邻 | 只输出推荐计划，不改奖励系统 |
| `native_revops_skill_candidate` | `C:/Users/Administrator/.codex/skills/revops/SKILL.md` | 是 | 需 registry 生成 manifest | 与销售运营候选相邻 | 不写 CRM，不做自动路由 |
| `native_sales_enablement_skill_candidate` | `C:/Users/Administrator/.codex/skills/sales-enablement/SKILL.md` | 是 | 需 registry 生成 manifest | 与销售赋能候选相邻 | 可作为销售资料 brief 能力 |
| `native_schema_markup_skill_candidate` | `C:/Users/Administrator/.codex/skills/schema/SKILL.md` | 是 | 需 registry 生成 manifest | 与 SEO/落地页候选相邻 | 只输出 schema 建议，不改站点 |
| `native_seo_audit_skill_candidate` | `C:/Users/Administrator/.codex/skills/seo-audit/SKILL.md` | 是 | 需 registry 生成 manifest | 与 SEO 候选相邻 | 仅用户提供页面文本，不抓网页 |
| `native_signup_optimization_skill_candidate` | `C:/Users/Administrator/.codex/skills/signup/SKILL.md` | 是 | 需 registry 生成 manifest | 与增长候选相邻 | 只输出注册流程建议 |
| `native_site_architecture_skill_candidate` | `C:/Users/Administrator/.codex/skills/site-architecture/SKILL.md` | 是 | 需 registry 生成 manifest | 与 SEO/官网候选相邻 | 只输出站点结构建议 |
| `native_sms_campaign_skill_candidate` | `C:/Users/Administrator/.codex/skills/sms/SKILL.md` | 是 | 需 registry 生成 manifest | 与私域营销候选相邻 | dry-run，禁止发送短信 |
| `native_social_content_skill_candidate` | `C:/Users/Administrator/.codex/skills/social/SKILL.md` | 是 | 需 registry 生成 manifest | 与社媒内容候选相邻 | dry-run，禁止真实发布 |
| `native_video_brief_skill_candidate` | `C:/Users/Administrator/.codex/skills/video/SKILL.md` | 是 | 需 registry 生成 manifest | 与短视频 brief 候选相邻 | dry-run，只输出脚本/brief，不生成视频 |
| `native_visual_prompt_brief_skill_candidate` | `C:/Users/Administrator/.codex/skills/visual_prompt_brief/SKILL.md` | 是 | 需 registry 生成 manifest | 与 To50 `visual_prompt_brief_candidate` 高度相邻 | 建议作为视觉 prompt 组件或替代来源 |

## 8. 5 个 agent_skill_compatible 补资料表

| candidate_id | 来源线索 | native_agent_skill 是否已验证本地 SKILL.md | agent_skill_compatible 是否需定位具体上游子目录 | skill.yaml / manifest 状态 | 与稳交付 13 / 既有 100 关系 | 建议动作 |
| --- | --- | --- | --- | --- | --- | --- |
| `compatible_office_financial_model_skill_candidate` | `https://github.com/fivetaku/claude-office-skills` | 否 | 是 | 未知，需定位具体子目录 | 与财务/经营报表候选相邻，高风险 | 先找具体 `SKILL.md`、LICENSE；若只做三表/DCF，必须 mock/read-only |
| `compatible_office_deck_refresh_skill_candidate` | `https://github.com/fivetaku/claude-office-skills` | 否 | 是 | 未知，需定位具体子目录 | 与销售赋能/营销视觉候选相邻 | 只做 PPT refresh brief，不生成或改真实 PPT |
| `compatible_design_system_review_skill_candidate` | `https://github.com/bergside/awesome-design-skills` | 否 | 是 | 未知，可能是 awesome 索引 | 与视觉 prompt/营销设计相邻 | 若为 awesome 清单，不得直接 L1，需拆真实上游 |
| `compatible_agent_skill_packager_candidate` | `https://github.com/FrancyJGLisboa/agent-skill-creator` | 否 | 是 | 未知，需确认是否有可复用 manifest | 与平台运营/封装工具相邻，不是客户业务 Skill | 建议仅作内部平台组件线索，不作为客户候选 |
| `compatible_office_comps_summary_skill_candidate` | `https://github.com/fivetaku/claude-office-skills` | 否 | 是 | 未知，需定位具体子目录 | 与竞品快照/经营报表相邻 | 只允许用户提供表格文本，不做抓取或财务结论 |

## 9. OpenClaw / OpenClow、Hermes、DeepAgents 迁移判断

| 平台 / 运行环境 | 当前证据 | 可否宣称已兼容 | 建议标签 |
| --- | --- | --- | --- |
| DeepAgents | 45 个 native 候选存在本地 `SKILL.md`；候选库已有 `candidate.yaml` | 只能说“可迁移候选”，不能说已 smoke | `migratable_after_L1` |
| OpenClaw / OpenClow | 未提供标准 manifest/schema；候选卡标注 adapter pending | 否 | `adapter_pending` |
| Hermes / 爱马仕 | 未提供标准 manifest/schema；候选卡标注 adapter pending | 否 | `adapter_pending` |
| Registry 自生成 candidate.yaml | 50 张候选卡均已有 `candidate.yaml` | 可作为候选库内部元数据 | `registry_candidate_yaml_generated` |

## 10. 不推荐直接送 smoke 的项

| candidate_id | 原因 |
| --- | --- |
| 5 个 `compatible_*` 候选 | 未定位具体上游子目录 / `SKILL.md` / manifest / LICENSE，不应直接 smoke。 |
| `native_directory_submissions_skill_candidate` | 目录提交属于外部表单动作，必须 dry-run 且明确禁止提交。 |
| `native_cold_email_skill_candidate` | 邮件发送高风险，必须 dry-run 且 `send_allowed=false`。 |
| `native_sms_campaign_skill_candidate` | 短信触达高风险，必须 dry-run 且 `send_allowed=false`。 |
| `native_image_marketing_skill_candidate`、`native_video_brief_skill_candidate` | 只能输出 brief，不能生成真实图片/视频或声明素材授权。 |
| 高度重叠营销文案类 native 候选 | 与稳交付 `marketing_copy_pack` 或 To100 营销候选重叠，建议先组件化。 |

## 11. 回传结论

- To150 的 50 个新增候选卡已完成来源证据补充研究。
- 45 个 native 候选已验证本地 `SKILL.md` 存在，可进入许可证窗口做 L1/source verification。
- 5 个 compatible 候选仍需定位具体公开上游子目录，不建议直接 smoke。
- 当前没有 OpenClaw/OpenClow 或 Hermes 真实导入证据；全部保持 `adapter_pending`。
- 本轮不改稳交付 13 个包、不送 L2、不封 L3、不客户调用。
