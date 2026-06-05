# L2 中文业务测试队列

本文件是 L2 模板预案，不代表正式测试结果。测试台不得测试未通过许可证复核的新增候选。

## 执行边界

- 只做 mock/simulated L2。
- 每个候选至少 3 个中文业务用例。
- 不安装依赖。
- 不访问真实账号。
- 不发送邮件。
- 不写 CRM、日历、任务、店铺、广告平台。
- 不跑真实网页抓取、OCR、视频生成、图片生成或音频处理。
- 不读取真实合同、简历、票据、客户隐私文件。

## 可测试条件

候选进入本队列前必须满足：

1. L1 许可证和商用风险通过。
2. 适合表达为轻量 callable Skill 或明确组件。
3. 输入输出 schema 可固定。
4. 权限边界和人工复核触发可写清。
5. 不依赖真实外部动作完成核心验收。

## 每部门 Top 候选 L2 模板

| 部门 | 建议 Skill ID | Mock 输入 | 预期输出字段 | 重点失败判定 | 人工复核触发 |
| --- | --- | --- | --- | --- | --- |
| 创意设计 | `visual_prompt_brief_candidate` | 商品卖点、品牌色、渠道、禁用词、目标风格 | `prompt_brief`, `asset_requirements`, `style_constraints`, `risk_notes`, `manual_review_required` | 虚构素材授权；输出直接生成承诺；忽略品牌限制 | 涉及肖像、商标、医疗/金融宣传、版权不明 |
| 创意设计 | `storyboard_script_brief_candidate` | 短视频主题、目标人群、时长、产品卖点 | `storyboard`, `shot_list`, `voiceover`, `caption_notes`, `risk_notes` | 分镜缺结构；生成夸大承诺；把视频生成当已完成 | 医疗/教育/金融承诺、素材版权不明 |
| 创意设计 | `brand_consistency_check_candidate` | 品牌规范、待检查文案/视觉描述 | `passed`, `violations`, `suggested_fixes`, `brand_terms`, `manual_review_required` | 未识别品牌禁用表达；无修改建议 | 品牌规范冲突、法律/商标风险 |
| 运营 | `content_calendar_planner_candidate` | 业务目标、活动日期、渠道、素材能力 | `calendar_items`, `content_topics`, `channel_plan`, `missing_inputs`, `manual_review_required` | 虚构节日/库存；自动写日历；未标缺失信息 | 价格/库存/合规行业不清 |
| 运营 | `feedback_cluster_insights_candidate` | mock 用户反馈列表 | `clusters`, `top_pain_points`, `representative_quotes`, `pii_redaction_notes`, `actions` | 暴露 PII；把少量反馈当确定结论 | 投诉、退款、隐私、样本量过低 |
| 运营 | `operations_metric_brief_candidate` | mock 运营指标和备注 | `metric_summary`, `changes`, `possible_factors`, `data_quality_notes`, `next_checks` | 算错变化；确定归因；缺数据质量提示 | 财务决策、严重缺失、口径冲突 |
| 销售 | `sales_followup_draft_candidate` | 客户背景、上次沟通、异议、下一步目标 | `message_draft`, `talking_points`, `risk_notes`, `send_allowed=false`, `manual_review_required` | 直接发送；虚构客户事实；超权限折扣承诺 | 折扣、合同、投诉、个人信息 |
| 销售 | `sales_meeting_task_brief_candidate` | mock 会议记录、参会角色、待办 | `summary`, `action_items`, `owners`, `due_dates`, `permission_notes` | 真实建日历/任务；行动项归属错误 | 合同条款、价格承诺、客户隐私 |
| 销售 | `lead_research_brief_candidate` | mock 公司主页文本、产品页文本 | `company_summary`, `business_signals`, `follow_up_angle`, `source_notes`, `confidence` | 把 mock 内容当尽调事实；无来源说明 | 对外沟通前、低置信、页面过期 |
| 电商 | `product_listing_copy_candidate` | 商品参数、目标关键词、平台规则 | `title_options`, `bullet_points`, `description`, `seo_terms`, `compliance_notes` | 夸大疗效/绝对化；承诺排名；违反平台规则 | 医疗、食品、金融、教育、平台禁词 |
| 电商 | `competitor_product_snapshot_candidate` | mock_old_html、mock_new_html、产品字段 | `product_name`, `price_change`, `evidence_snippets`, `availability`, `risk_notes` | 把划线价当现价；无证据片段；真实抓取 | ToS/robots 不清、页面过期、动态内容 |
| 电商 | `order_inventory_exception_candidate` | mock 订单和库存表 | `exception_detected`, `exception_type`, `affected_items`, `verification_steps`, `manual_review_required` | 直接改库存；误判补货；缺核查步骤 | 大额订单、库存为负、供应商冲突 |
| 客服 | `support_reply_flow_candidate` | 客户问题、知识库片段、客服回复 | `reply_draft`, `citations`, `risk_flags`, `handoff_required`, `confidence` | 编造知识库外答案；退款/账号安全不转人工 | 投诉、退款、账号、隐私、低置信 |
| 客服 | `complaint_escalation_summary_candidate` | mock 投诉对话 | `complaint_type`, `severity`, `summary`, `handoff_reason`, `next_safe_action` | 自动承诺赔偿；未升级；泄露隐私 | 投诉、退款、赔偿、监管威胁 |
| 客服 | `support_quality_eval_candidate` | mock 客服对话和质检规则 | `score`, `failed_checks`, `risk_flags`, `training_notes`, `manual_review_required` | 只看语气不看政策；漏账号安全 | 低分、高风险、隐私、退款承诺 |
| 管理 | `hr_resume_privacy_masker_candidate` | mock 简历文本 | `redacted_text`, `entities`, `preserved_fields`, `risk_level`, `manual_review_required` | 漏身份证/手机号；过度删除经历 | 高敏 PII、第三方联系人、低置信实体 |
| 管理 | `invoice_receipt_review_candidate` | mock 发票/小票 OCR 文本 | `invoice_type`, `fields`, `amount_validation`, `missing_fields`, `not_tax_advice=true` | 输出税务/报销结论；金额不一致未提示 | 金额异常、税号缺失、低置信 |
| 管理 | `contract_section_review_candidate` | mock 合同文本 | `sections`, `clause_types`, `risky_sections`, `quality_warnings`, `not_legal_advice=true` | 输出法律意见；漏自动续费/违约 | 自动续费、违约、保密、争议解决 |

## 当前测试状态

| 队列 | 状态 |
| --- | --- |
| 六部门新增候选正式 L2 | 未开始 |
| 可直接测试候选 | 5 |
| 等待 L1 通过候选 | 3 个 L2 优先候选需补资料；ClawHub 43 个暂缓 |
| 已可客户调用基线 | 13 个已验收 Skill，不属于本队列 |

补充状态：测试台已完成 18 个候选方向的 L2 模板预案，结果见 `L2_TEMPLATE_PREPLAN_RESULT.md`。L1 初筛结果见 `LICENSE_REVIEW_RESULT.md`。当前可送正式 L2 simulated 的候选为：`visual_prompt_brief_candidate`、`sales_followup_draft_candidate`、`sales_meeting_task_brief_candidate`、`lead_research_brief_candidate`、`competitor_product_snapshot_candidate`。所有候选仅允许 mock/dry-run，不得执行真实外部动作。

## 最新状态：5 个候选正式 L2 simulated 已完成

正式 L2 结果见 `L2_OFFICIAL_RESULT.md`。

| 结果 | 候选 |
| --- | --- |
| L2 通过可封装 | `visual_prompt_brief_candidate`, `sales_followup_draft_candidate` |
| 仅组件 | `sales_meeting_task_brief_candidate`, `lead_research_brief_candidate`, `competitor_product_snapshot_candidate` |
| 新增客户可调用 Skill | 0 |

后续要求：

- `visual_prompt_brief_candidate` 封装时必须强制“不生成图片、不调用 Eachlabs API、不声明素材授权”。
- `sales_followup_draft_candidate` 封装时必须强制 `send_allowed=false`，不发邮件/短信，不写 CRM，并建议与 `crm_note_structurer` 组合。
- 3 个组件候选不独立封装、不进入平台调用验收、不计入客户可调用 Skill。

## 测试台回传格式

| 字段 | 内容 |
| --- | --- |
| 候选 | 项目名 / Skill ID |
| 来源 | GitHub/ClawHub 链接 |
| L1 依据 | 许可证通过摘要 |
| 中文用例 | 至少 3 个 |
| 输出结构稳定性 | 高/中/低 |
| 中文可用性 | 高/中/低 |
| 权限边界 | 只读、mock、dry-run、禁止动作 |
| 人工复核触发 | 枚举 |
| L2 结论 | 通过、组件、需补测、暂缓、淘汰 |
| 建议下一步 | 送封装、补规则、补真实 Harness、暂缓 |
