# OpenClow/Hermes 可调用轻量 Skills 目录

核验日期：2026-06-02。

定位：本目录只收“可被 OpenClow/Hermes 这类 Agent 运行时调用的轻量 Skill”。重产品、完整平台和大型 WebUI 不直接作为岗位适配项，只能作为可选底层依赖或延期线索。

## Skill 包约定

每个 Skill 建议是一个小目录：

```text
skill-id/
  SKILL.md
  skill.yaml
  prompts/
  tools/
  tests/
```

最小调用协议：

- `id`：稳定 Skill ID。
- `intent`：一句话说明什么时候调用。
- `inputs`：JSON schema 或字段列表。
- `outputs`：JSON schema 或字段列表。
- `permissions`：需要访问的文件、网络、浏览器、OCR、邮件、CRM 等权限。
- `source_refs`：真实开源来源和许可证。
- `adapter_targets`：`openclow`、`openclaw`、`hermes`、`mcp`、`generic_agent`。

## Callable Skills

| Skill ID | 调用意图 | 输入 | 输出 | 开源来源 |
| --- | --- | --- | --- | --- |
| `visual_prompt_brief` | 为主图、海报、详情页生成视觉创意 brief 和图像提示词 | 产品信息、卖点、品牌语气、尺寸 | 视觉 brief、提示词、负面词、构图建议 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `image_asset_cutout_plan` | 生成商品/人物抠图、背景替换、素材分层执行方案 | 图片说明、目标用途、尺寸 | 抠图步骤、素材层级、质检项 | [Segment Anything](https://github.com/facebookresearch/segment-anything) `Apache-2.0` |
| `visual_asset_variation_brief` | 为同一商品生成多版本物料方案 | 原始物料、活动主题、渠道 | 多版本方向、颜色/构图建议、尺寸清单 | [MMagic](https://github.com/open-mmlab/mmagic) `Apache-2.0` |
| `brand_consistency_checker` | 检查文案和物料是否符合品牌语气 | 品牌规范、待检查内容 | 不一致点、修改建议、风险等级 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `storyboard_script_generator` | 生成短视频脚本、分镜和拍摄清单 | 产品、受众、时长、平台 | 脚本、分镜、镜头清单、口播 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `subtitle_transcription` | 将音视频转成字幕或口播稿 | 音视频文件/URL、语言 | 字幕、时间戳、转写文本 | [Whisper](https://github.com/openai/whisper) `MIT`、[WhisperX](https://github.com/m-bain/whisperX) `BSD-2-Clause` |
| `short_video_asset_digest` | 从视频素材中提取标题、看点、封面建议 | 视频文本、转写稿、素材说明 | 标题、封面文案、爆点摘要 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) `Unlicense`、[Whisper](https://github.com/openai/whisper) `MIT` |
| `marketing_copy_pack` | 生成广告、海报、活动、私域等文案包 | 产品、受众、渠道、目标 | 多版本文案、卖点、CTA | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `ad_copy_ab_generator` | 生成 A/B 广告文案和变量说明 | 产品、投放目标、人群 | A/B 文案、变量、假设 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT`、[DSPy](https://github.com/stanfordnlp/dspy) `MIT` |
| `content_calendar_planner` | 生成内容选题日历 | 行业、产品、周期、渠道 | 周/月选题表、发布建议 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `content_repurpose_distributor` | 将一份内容改写成多平台版本 | 原文、平台、目标受众 | 小红书/公众号/短视频/社群版本 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `web_page_to_brief` | 把网页转成业务摘要 | URL、关注点 | 摘要、关键信息、引用 | [Jina Reader](https://github.com/jina-ai/reader) `Apache-2.0` |
| `activity_plan_scheduler` | 生成活动排期、任务拆解和提醒节点 | 活动目标、时间、人员 | 排期表、任务清单、风险点 | [CrewAI](https://github.com/crewAIInc/crewAI) `MIT` |
| `feedback_cluster_insights` | 聚类用户反馈并提炼需求 | 用户反馈、渠道、时间 | 分类、频次、需求洞察 | [Instructor](https://github.com/567-labs/instructor) `MIT`、[DSPy](https://github.com/stanfordnlp/dspy) `MIT` |
| `user_profile_segmenter` | 生成用户画像和分层标签 | 用户行为、订单、反馈 | 标签、画像、触达建议 | [mem0](https://github.com/mem0ai/mem0) `Apache-2.0`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `daily_weekly_metrics_reporter` | 生成日报、周报和异常说明 | 指标表、目标、口径 | 报告、异常、行动建议 | [Instructor](https://github.com/567-labs/instructor) `MIT`、[Marvin](https://github.com/PrefectHQ/marvin) `Apache-2.0` |
| `spreadsheet_cleaning_notes` | 清洗表格并生成备注 | CSV/XLSX 文本、字段口径 | 清洗结果、备注、异常行 | [claude-office-skills/skills](https://github.com/claude-office-skills/skills) `MIT`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `lead_research_brief` | 调研潜在客户并生成线索摘要 | 公司名/URL/关键词 | 客户画像、痛点、切入话术 | [browser-use](https://github.com/browser-use/browser-use) `MIT`、[Jina Reader](https://github.com/jina-ai/reader) `Apache-2.0` |
| `sales_pitch_generator` | 生成产品介绍和销售话术 | 产品、客户画像、痛点 | 开场白、介绍话术、异议处理 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `followup_email_sequence` | 生成销售跟进邮件/企微话术 | 客户阶段、沟通记录、目标 | 跟进话术、下一步动作 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT`、[Composio](https://github.com/ComposioHQ/composio) `MIT` |
| `meeting_minutes_tasks` | 整理会议纪要和待办 | 会议转写、参会人、主题 | 纪要、待办、负责人、截止时间 | [Whisper](https://github.com/openai/whisper) `MIT`、[claude-office-skills/skills](https://github.com/claude-office-skills/skills) `MIT` |
| `partner_research_brief` | 调研合作方和渠道机会 | 合作方 URL/关键词 | 背景、合作点、风险、邮件草稿 | [Scrapy](https://github.com/scrapy/scrapy) `BSD-3-Clause`、[Jina Reader](https://github.com/jina-ai/reader) `Apache-2.0` |
| `sales_pipeline_summary` | 汇总销售过程和漏斗问题 | CRM/表格数据、阶段定义 | 漏斗摘要、卡点、改进建议 | [Instructor](https://github.com/567-labs/instructor) `MIT` |
| `competitor_product_snapshot` | 抓取竞品页面并生成对比 | URL、字段、关注点 | 竞品表、卖点、价格、风险 | [Crawlee](https://github.com/apify/crawlee) `Apache-2.0`、[Scrapy](https://github.com/scrapy/scrapy) `BSD-3-Clause` |
| `product_listing_seo_optimizer` | 优化商品标题、描述和属性 | 商品信息、关键词、竞品 | 标题、描述、属性、SEO 建议 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `ad_campaign_brief` | 生成推广投放 brief 和测试变量 | 产品、预算、人群、渠道 | 广告 brief、素材需求、测试变量 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) `MIT` |
| `order_exception_classifier` | 分类订单异常并给处理建议 | 订单记录、规则、备注 | 异常类型、优先级、建议动作 | [Instructor](https://github.com/567-labs/instructor) `MIT`、[Robocorp](https://github.com/robocorp/robocorp) `Apache-2.0` |
| `inventory_reorder_assistant` | 生成库存预警和补货建议 | 销量、库存、周期、阈值 | 预警、补货建议、缺货风险 | [Robocorp](https://github.com/robocorp/robocorp) `Apache-2.0` |
| `ecommerce_funnel_report` | 生成转化、商品、活动效果分析 | 指标表、活动信息 | 漏斗报告、异常、建议 | [Instructor](https://github.com/567-labs/instructor) `MIT` |
| `faq_answer_with_citations` | 基于知识库回答客服问题并给引用 | 问题、知识文档、客户上下文 | 回复、引用、转人工判断 | [Haystack](https://github.com/deepset-ai/haystack) `Apache-2.0`、[LlamaIndex](https://github.com/run-llama/llama_index) `MIT` |
| `customer_intent_classifier` | 识别客服意图和槽位 | 客户消息、意图列表 | 意图、槽位、置信度 | [Rasa](https://github.com/RasaHQ/rasa) `Apache-2.0`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `return_refund_flow_assistant` | 处理退换货流程并判断转人工 | 客户问题、政策、订单 | 处理步骤、回复、转人工原因 | [LangGraph](https://github.com/langchain-ai/langgraph) `MIT`、[Rasa](https://github.com/RasaHQ/rasa) `Apache-2.0` |
| `complaint_risk_escalation` | 识别投诉风险并生成升级建议 | 投诉内容、历史记录、规则 | 风险等级、安抚回复、升级路径 | [Guardrails](https://github.com/guardrails-ai/guardrails) `Apache-2.0`、[mem0](https://github.com/mem0ai/mem0) `Apache-2.0` |
| `service_quality_audit` | 对客服对话做质检评分 | 对话记录、质检标准 | 分数、问题、培训建议 | [Guardrails](https://github.com/guardrails-ai/guardrails) `Apache-2.0`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `training_case_extractor` | 从对话中提取培训案例 | 对话记录、培训主题 | 好/坏案例、点评、改进话术 | [Rasa](https://github.com/RasaHQ/rasa) `Apache-2.0`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `job_description_generator` | 生成招聘 JD 和面试题 | 岗位、职责、要求、公司信息 | JD、面试题、评分表 | [claude-office-skills/skills](https://github.com/claude-office-skills/skills) `MIT` |
| `resume_screening_extractor` | 抽取简历字段并初筛 | 简历文本、岗位要求 | 候选人字段、匹配度、疑点 | [MarkItDown](https://github.com/microsoft/markitdown) `MIT`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `onboarding_offboarding_checklist` | 生成入离职流程清单 | 员工信息、岗位、日期 | 清单、通知、资料项 | [claude-office-skills/skills](https://github.com/claude-office-skills/skills) `MIT` |
| `invoice_receipt_extractor` | 从票据/发票中抽取字段 | 图片/PDF、字段口径 | 发票字段、置信度、异常 | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) `Apache-2.0`、[invoice2data](https://github.com/invoice-x/invoice2data) `MIT` |
| `expense_reconciliation_checker` | 核对费用、报销和往来 | 报销表、票据字段、规则 | 差异、风险、处理建议 | [invoice2data](https://github.com/invoice-x/invoice2data) `MIT`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `contract_risk_review` | 审查合同风险并输出摘要 | 合同文本、审查规则 | 摘要、风险条款、建议 | [Unstructured](https://github.com/Unstructured-IO/unstructured) `Apache-2.0`、[Guardrails](https://github.com/guardrails-ai/guardrails) `Apache-2.0` |
| `contract_clause_compare` | 对比两个合同或条款版本 | 合同 A、合同 B、关注点 | 差异、风险、建议 | [LlamaIndex](https://github.com/run-llama/llama_index) `MIT`、[Instructor](https://github.com/567-labs/instructor) `MIT` |
| `purchase_quote_compare` | 对比供应商报价并生成建议 | 报价单、需求、评分口径 | 比价表、推荐、风险 | [MarkItDown](https://github.com/microsoft/markitdown) `MIT`、[Instructor](https://github.com/567-labs/instructor) `MIT` |

## 不直接作为 Skill 推荐的类型

- 完整产品或 WebUI：例如 InvokeAI、LibreChat、AnythingLLM、Langflow。
- 过重底层框架：例如直接把 Diffusers 当岗位 Skill 推荐。
- 许可证未自动确认：例如 GitHub API 返回 `NOASSERTION` 的 skills 仓库。
- 强 copyleft 或服务端传染风险项目：例如 AGPL-3.0。

