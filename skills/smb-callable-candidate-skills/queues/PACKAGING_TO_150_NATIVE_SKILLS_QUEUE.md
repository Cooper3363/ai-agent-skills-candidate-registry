# Packaging To150 Native Skills Queue

更新日期: 2026-06-03

## Current Status

candidate_card_packaging_done。50 个候选卡已落盘到 candidates/needs_license_review/。

## Next Packaging Gate

L1 放行后可补 DeepAgents staging 信息；smoke passed 后可移动到 mock_callable 或 dry_run_callable；正式 L2 通过后才允许生成 draft L3。组件项不得封独立 L3。

## Candidate Cards

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
