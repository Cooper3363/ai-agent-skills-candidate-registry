from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SmokeCase:
    skill_id: str
    title: str
    prompt: str
    expected_fields: list[str] = field(default_factory=list)


STABLE_CASES: list[SmokeCase] = [
    SmokeCase("marketing_copy_pack", "营销文案包", "为社区生鲜店写一组周末草莓促销文案，禁止承诺全网最低。"),
    SmokeCase("daily_weekly_metrics_reporter", "日报周报", "根据 mock 指标生成门店本周经营摘要：营收下降、客单价上升、复购率下降。"),
    SmokeCase("metric_exception_classifier", "指标异常分类", "判断 mock 指标异常：支付成功率从 96% 降到 82%，给出异常类型和复核建议。"),
    SmokeCase("faq_answer_with_citations", "FAQ 引用回复", "基于 mock 知识库回答客户如何开发票，必须引用知识库条目。"),
    SmokeCase("support_ticket_classifier", "工单分类", "分类客户问题：商品损坏要求退款并威胁投诉。"),
    SmokeCase("structured_campaign_brief", "活动 brief", "把瑜伽馆体验课活动目标、渠道、人群整理成结构化 campaign brief。"),
    SmokeCase("structured_metric_summary", "指标摘要", "总结 mock 电商订单、退款、转化率指标，标注缺失口径。"),
    SmokeCase("crm_note_structurer", "CRM 记录", "把销售跟进记录整理为 CRM note 草稿，不写入 CRM。"),
    SmokeCase("support_reply_guardrail", "客服回复防护", "检查客服回复是否越权承诺退款或赔偿。"),
    SmokeCase("marketing_compliance_guard", "营销合规检查", "检查食品低糖饼干文案是否包含医疗功效承诺。"),
    SmokeCase("support_pii_redactor", "客服 PII 脱敏", "脱敏 mock 客服对话中的手机号、地址和订单号。"),
    SmokeCase("support_kb_doc_cleaner", "知识库清洗", "把一段混乱客服政策文本整理为可引用知识库条目。"),
    SmokeCase("expense_invoice_parser", "票据字段抽取", "从 mock OCR 发票文本中抽取金额、税号、发票日期，并标注不是税务建议。"),
]


DRAFT_CASES: list[SmokeCase] = [
    SmokeCase(
        "visual_prompt_brief_candidate",
        "生鲜海报视觉 brief",
        "为社区生鲜店草莓 19.9 元朋友圈海报生成视觉 prompt brief，只输出 brief，不生成图片。",
        ["prompt_brief", "asset_requirements", "risk_notes", "manual_review_required"],
    ),
    SmokeCase(
        "visual_prompt_brief_candidate",
        "瑜伽馆小红书封面 brief",
        "为肩颈放松体验课生成小红书封面视觉 brief，禁止医疗疗效承诺。",
        ["prompt_brief", "style_constraints", "negative_prompts", "manual_review_required"],
    ),
    SmokeCase(
        "visual_prompt_brief_candidate",
        "电商主图 brief",
        "为 316 不锈钢保温杯生成白底电商主图 brief，标注平台和商标边界。",
        ["asset_requirements", "channel_specs", "risk_notes"],
    ),
    SmokeCase(
        "sales_followup_draft_candidate",
        "试用后微信跟进",
        "客户试用排课提醒 3 天后，生成微信跟进草稿，send_allowed 必须为 false。",
        ["message_draft", "send_allowed", "risk_notes", "manual_review_required"],
    ),
    SmokeCase(
        "sales_followup_draft_candidate",
        "报价后价格异议邮件",
        "客户说价格贵，生成报价后跟进邮件草稿，不能承诺超权限折扣。",
        ["message_draft", "subject_options", "risk_notes", "send_allowed"],
    ),
    SmokeCase(
        "sales_followup_draft_candidate",
        "沉睡线索唤醒短信",
        "客户 30 天未回复，生成低打扰短信草稿，不能假设短信授权。",
        ["message_draft", "risk_notes", "send_allowed"],
    ),
    SmokeCase(
        "complaint_escalation_summary_candidate",
        "退款投诉升级",
        "总结客户投诉：商品坏了、一天未回复、要求退款、不然投诉。只做内部摘要，不承诺退款。",
        ["complaint_type", "severity", "risk_flags", "handoff_required"],
    ),
    SmokeCase(
        "complaint_escalation_summary_candidate",
        "赔偿和监管威胁",
        "总结客户说虚假宣传、要求三倍赔偿、要向市场监管举报，必须升级主管。",
        ["severity", "handoff_reason", "next_safe_action", "risk_flags"],
    ),
    SmokeCase(
        "complaint_escalation_summary_candidate",
        "隐私投诉摘要",
        "总结含手机号和订单号的发错地址投诉，摘要必须脱敏。",
        ["summary", "privacy_notes", "risk_flags", "confidence"],
    ),
    SmokeCase(
        "product_listing_copy_candidate",
        "普通商品页",
        "为 316 不锈钢保温杯生成淘宝商品标题、卖点和详情页草稿，不承诺销量排名。",
        ["title_options", "bullet_points", "description", "not_seo_guarantee"],
    ),
    SmokeCase(
        "product_listing_copy_candidate",
        "食品商品风险",
        "为低糖燕麦饼干生成抖音小店文案，禁止治疗糖尿病等医疗功效承诺。",
        ["platform_warnings", "compliance_notes", "manual_review_required"],
    ),
    SmokeCase(
        "product_listing_copy_candidate",
        "教育资料风险",
        "为三年级数学练习册生成拼多多商品文案，禁止保证提分或考试结果。",
        ["title_options", "compliance_notes", "not_seo_guarantee"],
    ),
]


ALL_CASES = STABLE_CASES + DRAFT_CASES
