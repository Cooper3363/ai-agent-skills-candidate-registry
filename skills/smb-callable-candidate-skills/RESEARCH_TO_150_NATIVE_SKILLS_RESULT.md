# To150 Native / Compatible Agent Skill Research Result

更新日期: 2026-06-03

## Summary

本轮新增 50 个候选，口径从内部业务模板切换为已有 SKILL.md 或接近 Agent Skill 结构的可迁移候选。

- 新增候选卡: 50
- native_agent_skill: 45，本机已验证存在 SKILL.md。
- agent_skill_compatible: 5，来自公开 Agent Skill/Claude Skill 仓库线索，需许可证窗口核验具体子目录和 manifest。
- 新增候选统一状态: needs_license_review。
- 本轮不执行 L2，不生成 draft L3，不进入客户正式调用。
- 稳交付库客户正式可调用数量仍为 13。

## Selection Rules

- 优先选择已有 SKILL.md 的目录型 Agent Skill。
- 能映射到中小微高频业务包。
- 进入 DeepAgents 前必须完成 L1/source verification。
- OpenClaw/Hermes 兼容性暂记为 adapter_pending，不默认宣称已可直接安装。
- 已有 100 个候选不改状态；本轮新增只计入 To150 Agent Skill 来源候选。

## New 50 Candidates

| candidate_id | skill_source_class | business_package | source_project | current_status | recommended_trial_mode | deepagents_trial_fit |
|---|---|---|---|---|---|---|
| native_ab_testing_skill_candidate | native_agent_skill | 经营报表与增长实验包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_ad_creative_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_ads_planning_skill_candidate | native_agent_skill | 营销投放包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_ai_seo_skill_candidate | native_agent_skill | 营销与搜索包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_analytics_tracking_skill_candidate | native_agent_skill | 经营报表包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_aso_listing_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_churn_prevention_skill_candidate | native_agent_skill | 销售与客户成功包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_co_marketing_skill_candidate | native_agent_skill | 营销与合作包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_cold_email_skill_candidate | native_agent_skill | 销售获客包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_community_marketing_skill_candidate | native_agent_skill | 营销与客户运营包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_competitor_profiling_skill_candidate | native_agent_skill | 营销与销售情报包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| native_competitor_comparison_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_content_strategy_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_copy_editing_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_copywriting_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_cro_skill_candidate | native_agent_skill | 经营增长包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_customer_research_skill_candidate | native_agent_skill | 客服与经营洞察包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_directory_submissions_skill_candidate | native_agent_skill | 营销获客包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_email_sequence_skill_candidate | native_agent_skill | 销售与客户运营包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_free_tool_planner_skill_candidate | native_agent_skill | 营销获客包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_geo_citation_audit_skill_candidate | native_agent_skill | 营销与搜索包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| native_image_marketing_skill_candidate | native_agent_skill | 营销视觉包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_launch_planning_skill_candidate | native_agent_skill | 营销与运营包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_lead_magnet_skill_candidate | native_agent_skill | 营销获客包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_marketing_ideas_skill_candidate | native_agent_skill | 营销策略包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_marketing_plan_skill_candidate | native_agent_skill | 营销策略包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_marketing_psychology_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_onboarding_skill_candidate | native_agent_skill | 销售与客户成功包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_paywall_optimization_skill_candidate | native_agent_skill | 经营增长包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_popup_optimization_skill_candidate | native_agent_skill | 营销与转化包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_pricing_strategy_skill_candidate | native_agent_skill | 经营策略包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_product_marketing_context_skill_candidate | native_agent_skill | 营销策略包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_programmatic_seo_skill_candidate | native_agent_skill | 营销与搜索包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| native_prospecting_skill_candidate | native_agent_skill | 销售获客包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| native_referral_program_skill_candidate | native_agent_skill | 销售与客户成功包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_revops_skill_candidate | native_agent_skill | 销售运营包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_sales_enablement_skill_candidate | native_agent_skill | 销售赋能包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_schema_markup_skill_candidate | native_agent_skill | 营销与搜索包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_seo_audit_skill_candidate | native_agent_skill | 营销与搜索包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| native_signup_optimization_skill_candidate | native_agent_skill | 经营增长包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_site_architecture_skill_candidate | native_agent_skill | 营销与搜索包 | local_codex_user_skill | needs_license_review | mock_only/read_only/external_action_blocked | skill_ready |
| native_sms_campaign_skill_candidate | native_agent_skill | 销售与客户运营包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_social_content_skill_candidate | native_agent_skill | 营销内容包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_video_brief_skill_candidate | native_agent_skill | 营销视频包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| native_visual_prompt_brief_skill_candidate | native_agent_skill | 营销视觉包 | local_codex_user_skill | needs_license_review | dry_run_only/read_only/external_action_blocked | dry_run_only |
| compatible_office_financial_model_skill_candidate | agent_skill_compatible | 行政财务 HR 包 | fivetaku/claude-office-skills | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| compatible_office_deck_refresh_skill_candidate | agent_skill_compatible | 行政与销售赋能包 | fivetaku/claude-office-skills | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| compatible_design_system_review_skill_candidate | agent_skill_compatible | 营销视觉包 | bergside/awesome-design-skills | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| compatible_agent_skill_packager_candidate | agent_skill_compatible | 平台运营包 | FrancyJGLisboa/agent-skill-creator | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |
| compatible_office_comps_summary_skill_candidate | agent_skill_compatible | 经营报表包 | fivetaku/claude-office-skills | needs_license_review | mock_only/read_only/external_action_blocked | mock_only |

## Window Decision

研究窗口结论: 50 个候选可以进入许可证窗口，不得直接 smoke、不得直接 L2、不得直接封装 L3。
