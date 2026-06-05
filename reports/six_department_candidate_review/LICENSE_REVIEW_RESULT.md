# L1 许可证复核结果

回传来源：许可证与商用风险复核窗口  
回传时间：2026-06-03  
状态：产品筛选阶段 L1 初筛完成，不替代正式法务意见

## 总体结论

六部门候选池共有 57 个唯一链接：14 个 GitHub、43 个 ClawHub。

| 分组 | 数量 | 当前结论 |
| --- | ---: | --- |
| GitHub 总复核 | 14 | 已完成 L1 初筛 |
| L2 优先队列 | 8 | 5 个可送正式 mock L2，3 个需补资料 |
| ClawHub 初筛 | 43 | 全部许可证/商用条款不可核验，不得送正式 L2 |
| 当前新增客户可调用 Skill | 0 | 可客户调用仍只认已验收 13 个 Skill |

## 可送正式 L2 simulated 的 5 个候选

以下候选只允许进入 mock/dry-run L2，不得触发真实外部动作。

| 候选 Skill ID | 来源 | LICENSE/SPDX | 维护状态 | 可测边界 | 风险等级 | L1 建议动作 |
| --- | --- | --- | --- | --- | --- | --- |
| `visual_prompt_brief_candidate` | `https://github.com/eachlabs/skills` | MIT | 一般 | 只做视觉提示词 brief，不生成图片，不调用 Eachlabs API | 中 | 送 L2 mock |
| `sales_followup_draft_candidate` | `https://github.com/coreyhaines31/marketingskills` | MIT | 活跃 | 只生成销售跟进草稿，不发送邮件/短信，不写 CRM | 中 | 送 L2 mock |
| `sales_meeting_task_brief_candidate` | `https://github.com/googleworkspace/cli` | Apache-2.0 | 活跃 | 只输出会议任务草案和 dry-run payload，不做 OAuth，不写 Workspace | 中高 | 送 L2 mock |
| `lead_research_brief_candidate` | `https://github.com/tavily-ai/skills` | MIT | 一般 | 只用 mock 页面文本，不调用 Tavily API，不搜索，不 crawl | 中 | 送 L2 mock |
| `competitor_product_snapshot_candidate` | `https://github.com/apify/agent-skills` | Apache-2.0 | 活跃 | 只用 mock HTML/快照文本，不真实抓取，不代理，不绕 robots/ToS | 高 | 送 L2 mock |

## L2 优先但未通过 L1 的 3 个候选

| 候选 Skill ID | 来源 | L1 问题 | 当前动作 |
| --- | --- | --- | --- |
| `order_inventory_exception_candidate` | `https://github.com/claude-office-skills/skills` | 总体 MIT 但子 skill 许可证可能不同；需定位具体订单/库存子 skill 或真实上游项目 | 补资料，不送 L2 |
| `support_quality_eval_candidate` | `https://github.com/github/awesome-copilot` | awesome 索引集合，不是可执行 Skill；第三方资源需逐项核验 | 补资料，不送 L2 |
| `hr_resume_privacy_masker_candidate` | `https://github.com/anthropics/skills` | 整仓无统一根 LICENSE；子目录授权不一致；文档技能 source-available，第三方 notices 复杂 | 补资料，不送 L2 |

补充建议：如需推进 HR 脱敏方向，优先复用已测 Microsoft Presidio / `hr_resume_privacy_masker` 路线，而不是从 `anthropics/skills` 整仓推进。

## 14 个 GitHub 链接总复核结果

| 项目名 | 链接 | LICENSE/SPDX | 维护状态 | 商用限制 | 依赖/API/模型风险 | 可封装性 | 评分 | 建议动作 | L2 队列 |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| eachlabs/skills | `https://github.com/eachlabs/skills` | MIT | 一般 | 无明显代码限制 | Eachlabs API、图片/视频生成、素材版权 | 只可封装视觉提示词 brief，不生成图片 | 62 | 送 L2 mock | L2 优先队列 |
| runcomfy-agent-skills | `https://github.com/agentspace-so/runcomfy-agent-skills` | MIT | 一般 | 无明显代码限制 | Comfy/RunComfy、图片视频模型权重 | 生成类高风险 | 40 | 暂缓 | 非优先 |
| Marketing Skills | `https://github.com/coreyhaines31/marketingskills` | MIT | 活跃 | 无明显限制 | 广告合规、文案素材来源 | 可封装草稿类 Skill | 82 | 送 L2 mock | L2 优先队列 |
| anthropics/skills | `https://github.com/anthropics/skills` | 整仓不统一；部分 Apache-2.0 / source-available | 活跃 | 子 skill 授权不一 | HR/文档/Office/PDF 依赖复杂 | 不可整仓封装 | 45 | 补资料 | L2 优先但未通过 |
| googleworkspace/cli | `https://github.com/googleworkspace/cli` | Apache-2.0 | 活跃 | 无代码商用限制 | Google OAuth、Gmail/Drive/Calendar 写入 | 只能 dry-run/mock，不写 Workspace | 60 | 送 L2 mock | L2 优先队列 |
| tavily-ai/skills | `https://github.com/tavily-ai/skills` | MIT | 一般 | 无明显限制 | Tavily API、搜索、extract/crawl | 只用 mock 页面文本，不调 API | 65 | 送 L2 mock | L2 优先队列 |
| apify/agent-skills | `https://github.com/apify/agent-skills` | Apache-2.0 | 活跃 | 无代码限制 | Apify 平台、Actor、抓取 ToS/robots | 只用 mock HTML，不真实抓取 | 55 | 送 L2 mock | L2 优先队列 |
| claude-seo | `https://github.com/agricidaniel/claude-seo` | MIT | 活跃 | 无明显限制 | DataForSEO、Firecrawl、Google API、SEO 承诺 | 电商文案可拆，但大多已有 Skill 覆盖 | 55 | 补资料 | 非优先 |
| claude-office-skills/skills | `https://github.com/claude-office-skills/skills` | 总体 MIT；子 skill 可能不同 | 一般 | 子 skill 授权不清 | Office/MCP、文件读写、库存/表格 | 需定位订单库存子 skill | 50 | 补资料 | L2 优先但未通过 |
| astronomer/agents | `https://github.com/astronomer/agents` | Apache-2.0 | 活跃 | 无明显限制 | Airflow/MCP/数据工作流部署 | 大型框架/底层组件 | 55 | 组件观察 | 非优先 |
| asgard-ai-platform/skills | `https://github.com/asgard-ai-platform/skills` | MIT | 一般 | 无明显限制 | 301 skills，需逐项拆分 | 与现有客服包重叠 | 60 | 组件观察 | 非优先 |
| anthropics/knowledge-work-plugins | `https://github.com/anthropics/knowledge-work-plugins` | Apache-2.0 | 活跃 | 无明显限制 | 插件运行依赖、投诉/回访高风险 | 可作客诉摘要线索 | 65 | 补资料 | 非优先 |
| github/awesome-copilot | `https://github.com/github/awesome-copilot` | MIT | 活跃 | 第三方资源需逐项核验 | awesome 索引，不是可执行 Skill | 只能找真实上游 | 50 | 补资料 | L2 优先但未通过 |
| alirezarezvani/claude-skills | `https://github.com/alirezarezvani/claude-skills` | MIT | 活跃 | 无明显限制 | 大合集，含财务/合同/合规 | 需拆采购后勤子 skill | 60 | 补资料 | 非优先 |

## ClawHub 43 个候选暂缓原因

ClawHub 43 个链接全部存在以下至少一项缺口：

- LICENSE/SPDX 不明。
- 维护状态不明。
- 作者授权不明。
- 商用条款不可核验。
- 依赖/API/模型条款不可核验。
- 部分候选涉及高风险动作或高敏数据。

因此当前统一处理为：仅作线索或暂缓，不送正式 L2，不封装，不客户调用。

| 风险分组 | 涉及候选 | 当前动作 |
| --- | --- | --- |
| 图片/视频生成 | `image-marketing-brochure`, `image-social-media`, `dlazy-image-generate`, `dlazy-recraft-v3`, `video-storyboard-generate` | 暂缓 |
| 内容/品牌线索 | `brand`, `content-calendar`, `content-adapter`, `wechat-rewrite`, `gzh-explosive-content-detector`, `wechat-10w-hot`, `text-storyboard-script` | 补资料，许可证清楚前不送 L2 |
| 用户反馈/画像 | `persona-docs`, `customer-feedback` | 补资料，需 PII 边界 |
| 数据/BI/抓取 | `data-harvester`, `finebi-skills` | 暂缓 |
| 外呼/邮件发送 | `clawcall-dev`, `sendgrid`, `resend-send-native-node`, `email-sequence-pack`, `active-campaign`, `agentcall`, `getresponse` | 暂缓 |
| 日历/任务写入 | `calendar-scheduling`, `cal-com`, `opentask`, `sunsama` | 暂缓 |
| 电商/广告平台 | `woocommerce`, `clawshop-pro`, `linkfox-amazon-ads-entity`, `ad-copy-gen` | 暂缓；文案项仅作线索 |
| RAG/搜索/文档库 | `swarmvault`, `knowledge-rag`, `anysearch`, `safe-shrink`, `cms-docdb` | 暂缓或补资料 |
| HR/薪酬 | `zoho-people`, `diting-compensation-expert` | 暂缓 |
| 财务/票据 | `fl-invoice-tracker`, `simple-ledger`, `expense-invoice-ocr` | 暂缓 |
| 合同/法务 | `contract-reviewer` | 暂缓 |

## 指挥中心当前判定

- 本轮 L1 已产生 5 个可送正式 L2 simulated 的候选。
- 3 个 L2 优先候选需补资料，不送测。
- ClawHub 43 个候选全部暂缓或仅作线索。
- 六部门候选池不新增客户可调用 Skill。
- 下一步由测试台对 5 个候选执行正式 L2 simulated。
