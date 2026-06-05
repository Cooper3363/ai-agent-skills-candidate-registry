# 六部门核心角色 OpenClow/Hermes Callable Skills 适配表

来源文件：`C:\Users\Administrator\Downloads\六部门角色与Skill适配方案.docx`

口径纠正：本表不再把完整产品、大型 WebUI 或重框架直接分配给角色。每个核心角色只映射到可被 OpenClow/Hermes 调用的轻量 Skill ID。Skill 的真实开源来源见 `catalog/callable_skill_catalog_openclow_hermes.md`。

## 角色适配表

| 部门 | 核心角色 | 主要工作 | 推荐 Callable Skills |
| --- | --- | --- | --- |
| 创意设计部门 | 美工/视觉设计 | 做主图、海报、详情页配图、活动物料 | `visual_prompt_brief`<br>`image_asset_cutout_plan`<br>`visual_asset_variation_brief`<br>`brand_consistency_checker` |
| 创意设计部门 | 品牌设计 | 统一品牌风格，做品牌规范和视觉延展 | `brand_consistency_checker`<br>`visual_prompt_brief`<br>`visual_asset_variation_brief`<br>`marketing_copy_pack` |
| 创意设计部门 | 短视频/剪辑 | 整理脚本、分镜、字幕、封面和短视频素材 | `storyboard_script_generator`<br>`subtitle_transcription`<br>`short_video_asset_digest`<br>`marketing_copy_pack` |
| 创意设计部门 | 文案策划 | 写广告文案、活动文案、海报文案和卖点表达 | `marketing_copy_pack`<br>`ad_copy_ab_generator`<br>`brand_consistency_checker`<br>`content_repurpose_distributor` |
| 运营部门 | 内容运营 | 内容选题、内容初稿、分发文案 | `content_calendar_planner`<br>`content_repurpose_distributor`<br>`web_page_to_brief`<br>`marketing_copy_pack` |
| 运营部门 | 活动运营 | 活动排期、提醒、流程推进 | `activity_plan_scheduler`<br>`marketing_copy_pack`<br>`daily_weekly_metrics_reporter`<br>`meeting_minutes_tasks` |
| 运营部门 | 用户运营 | 用户反馈整理、用户画像、需求归纳 | `feedback_cluster_insights`<br>`user_profile_segmenter`<br>`daily_weekly_metrics_reporter`<br>`followup_email_sequence` |
| 运营部门 | 数据运营 | 表格处理、日报周报、数据备注 | `daily_weekly_metrics_reporter`<br>`spreadsheet_cleaning_notes`<br>`ecommerce_funnel_report`<br>`feedback_cluster_insights` |
| 销售部门 | 业务员 | 找客户、介绍产品、跟进成交 | `lead_research_brief`<br>`sales_pitch_generator`<br>`followup_email_sequence`<br>`user_profile_segmenter` |
| 销售部门 | 销售助理 | 整理资料、排会议、跟进合同和进度 | `meeting_minutes_tasks`<br>`resume_screening_extractor`<br>`contract_risk_review`<br>`followup_email_sequence` |
| 销售部门 | 商务拓展 | 找合作方、谈合作、维护渠道 | `partner_research_brief`<br>`lead_research_brief`<br>`sales_pitch_generator`<br>`followup_email_sequence` |
| 销售部门 | 销售运营 | 做销售数据、过程管理、资料支持 | `sales_pipeline_summary`<br>`daily_weekly_metrics_reporter`<br>`spreadsheet_cleaning_notes`<br>`meeting_minutes_tasks` |
| 电商部门 | 店铺运营 | 店铺信息抓取、竞品整理 | `competitor_product_snapshot`<br>`web_page_to_brief`<br>`daily_weekly_metrics_reporter`<br>`activity_plan_scheduler` |
| 电商部门 | 商品运营 | 商品标题、商品描述、搜索优化 | `product_listing_seo_optimizer`<br>`competitor_product_snapshot`<br>`visual_prompt_brief`<br>`ad_copy_ab_generator` |
| 电商部门 | 推广投放 | 广告投放文案、投放思路、广告优化 | `ad_campaign_brief`<br>`ad_copy_ab_generator`<br>`marketing_copy_pack`<br>`ecommerce_funnel_report` |
| 电商部门 | 订单/库存 | 跟订单、查库存、做补货和异常处理 | `order_exception_classifier`<br>`inventory_reorder_assistant`<br>`daily_weekly_metrics_reporter`<br>`customer_intent_classifier` |
| 电商部门 | 数据分析 | 看转化、看商品表现、看活动效果 | `ecommerce_funnel_report`<br>`daily_weekly_metrics_reporter`<br>`spreadsheet_cleaning_notes`<br>`product_listing_seo_optimizer` |
| 客服部门 | 售前客服 | 标准回复、话术整理、客服流程 | `faq_answer_with_citations`<br>`customer_intent_classifier`<br>`sales_pitch_generator`<br>`brand_consistency_checker` |
| 客服部门 | 售后客服 | 售后问题归类、问题统计、常见问题总结 | `return_refund_flow_assistant`<br>`customer_intent_classifier`<br>`faq_answer_with_citations`<br>`training_case_extractor` |
| 客服部门 | 客诉专员 | 处理投诉、升级问题、回访客户 | `complaint_risk_escalation`<br>`return_refund_flow_assistant`<br>`service_quality_audit`<br>`followup_email_sequence` |
| 客服部门 | 质检培训 | 检查对话质量，整理培训材料 | `service_quality_audit`<br>`training_case_extractor`<br>`complaint_risk_escalation`<br>`faq_answer_with_citations` |
| 管理部门 | 行政人事 | 做招聘协助、入离职、通知、档案和日常行政 | `job_description_generator`<br>`resume_screening_extractor`<br>`onboarding_offboarding_checklist`<br>`meeting_minutes_tasks` |
| 管理部门 | 财务 | 整理单据、做报表、核对费用和往来 | `invoice_receipt_extractor`<br>`expense_reconciliation_checker`<br>`spreadsheet_cleaning_notes`<br>`daily_weekly_metrics_reporter` |
| 管理部门 | 法务/合同 | 看合同、留痕、提风险、管模板 | `contract_risk_review`<br>`contract_clause_compare`<br>`purchase_quote_compare`<br>`faq_answer_with_citations` |
| 管理部门 | 采购后勤 | 采购办公物资，管后勤和供应协调 | `purchase_quote_compare`<br>`competitor_product_snapshot`<br>`inventory_reorder_assistant`<br>`spreadsheet_cleaning_notes` |

## 第一批建议打包的 12 个 Skills

| 优先级 | Skill ID | 覆盖重点 |
| --- | --- | --- |
| P0 | `marketing_copy_pack` | 文案策划、内容运营、推广投放、售前客服 |
| P0 | `faq_answer_with_citations` | 售前客服、售后客服、质检培训、法务/合同 |
| P0 | `daily_weekly_metrics_reporter` | 数据运营、销售运营、电商数据分析、财务 |
| P0 | `competitor_product_snapshot` | 店铺运营、商品运营、商务拓展、采购后勤 |
| P0 | `invoice_receipt_extractor` | 财务、行政、报销 |
| P0 | `lead_research_brief` | 业务员、商务拓展、用户运营 |
| P1 | `product_listing_seo_optimizer` | 商品运营、推广投放、店铺运营 |
| P1 | `service_quality_audit` | 客服质检、售后、客诉 |
| P1 | `contract_risk_review` | 法务、销售助理、采购 |
| P1 | `subtitle_transcription` | 短视频、内容运营 |
| P1 | `meeting_minutes_tasks` | 销售助理、活动运营、行政人事 |
| P1 | `activity_plan_scheduler` | 活动运营、店铺运营、内容运营 |
