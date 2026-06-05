# L1 许可证复核队列

本文件是六部门候选池的 L1 队列。未完成 L1 的候选不得送 L2，不得封装，不得进入客户调用。

## 复核规则

| 检查项 | 要求 |
| --- | --- |
| LICENSE | 仓库根目录或包目录必须有明确 LICENSE |
| SPDX | 尽量记录 SPDX 标识，如 MIT、Apache-2.0、BSD-3-Clause |
| 商用限制 | README、docs、model card、terms 中不得出现不明商用限制 |
| 维护状态 | 最近提交、issue 状态、是否归档、README 是否可用 |
| 依赖风险 | 第三方 API、模型、浏览器、OAuth、云 OCR、外部账号需标出 |
| 动作权限 | 发送邮件、写 CRM、建日历、抓取网页、财务/法务/HR 决策默认高风险 |

## GitHub 链接优先复核队列

| # | 链接 | 文档部门/角色 | 初始建议 | 复核重点 | 当前状态 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `https://github.com/eachlabs/skills` | 创意设计/美工视觉 | 可能作为视觉提示词或素材简报线索 | LICENSE、是否依赖图片生成 API、商用素材版权 | 待 L1 |
| 2 | `https://github.com/agentspace-so/runcomfy-agent-skills` | 创意设计/短视频剪辑 | 可能作为视频/工作流线索 | LICENSE、Comfy/图片视频模型依赖、模型商用限制 | 待 L1，高风险 |
| 3 | `https://github.com/coreyhaines31/marketingskills` | 创意设计/文案，运营/用户，销售/业务，电商/投放 | 文案/营销候选，与现有 `marketing_copy_pack` 重叠 | LICENSE、内容是否可抽成轻量 callable Skill | 待 L1 |
| 4 | `https://github.com/anthropics/skills` | 运营/数据，管理/行政人事 | 通用 skills 候选，与现有报表/HR PII 方向相关 | LICENSE、技能目录粒度、是否仅示例 | 待 L1 |
| 5 | `https://github.com/googleworkspace/cli` | 销售/销售助理，销售运营 | Workspace 操作线索 | LICENSE、OAuth、Google API、写入权限 | 待 L1，高风险 |
| 6 | `https://github.com/tavily-ai/skills` | 销售/商务支持 | 公开线索调研候选 | LICENSE、Tavily API、网页读取/事实引用 | 待 L1，中高风险 |
| 7 | `https://github.com/apify/agent-skills` | 电商/店铺运营 | 竞品/页面快照线索 | LICENSE、Apify 平台条款、抓取 ToS/robots | 待 L1，高风险 |
| 8 | `https://github.com/agricidaniel/claude-seo --skill` | 电商/商品运营 | SEO/商品描述候选 | 链接需纠错，LICENSE、SEO 承诺风险 | 待 L1，链接异常 |
| 9 | `https://github.com/claude-office-skills/skills` | 电商/订单库存 | 表格/办公技能线索 | LICENSE、文件读写权限、是否完整技能包 | 待 L1 |
| 10 | `https://github.com/astronomer/agents` | 电商/数据分析 | 数据/工作流线索 | LICENSE、是否偏大型框架、部署复杂度 | 待 L1 |
| 11 | `https://github.com/asgard-ai-platform/skills` | 客服/售前售后 | 客服标准回复/流程候选 | LICENSE、是否可独立封装、与现有客服包重叠 | 待 L1 |
| 12 | `https://github.com/anthropics/knowledge-work-plugins` | 客服/客诉 | 投诉/知识工作线索 | LICENSE、插件运行依赖、是否有明确商用边界 | 待 L1 |
| 13 | `https://github.com/github/awesome-copilot` | 客服/质检培训 | 质检/评测线索 | awesome 清单通常不是可封装项目，需找真实上游 | 待 L1，可能仅作索引 |
| 14 | `https://github.com/alirezarezvani/claude-skills` | 管理/采购后勤 | 采购/通用技能线索 | LICENSE、技能粒度、是否能映射轻量采购比较 | 待 L1 |

## ClawHub 来源初筛队列

ClawHub 43 个链接先做来源与商用条款可核验性初筛。许可证、作者授权、依赖、运行边界不清时，不得送 L2。

| 分组 | 链接 | 初始处理 |
| --- | --- | --- |
| 图片/视觉 | `image-marketing-brochure`, `image-social-media`, `dlazy-image-generate`, `dlazy-recraft-v3` | 暂缓，需查生成依赖、版权和商用条款 |
| 品牌/内容 | `brand`, `content-calendar`, `content-adapter`, `wechat-rewrite`, `gzh-explosive-content-detector`, `wechat-10w-hot` | 仅作线索，许可证清楚后可设计 mock L2 |
| 视频/脚本 | `video-storyboard-generate`, `text-storyboard-script` | 文本分镜可观察，视频生成暂缓 |
| 用户/反馈 | `persona-docs`, `customer-feedback` | 可观察为反馈聚类/画像组件，需 PII 边界 |
| 数据/BI | `data-harvester`, `finebi-skills` | 抓取/BI 接入风险高，暂缓 |
| 销售触达 | `clawcall-dev`, `sendgrid`, `resend-send-native-node`, `email-sequence-pack`, `active-campaign` | 只允许 dry-run/草稿，真实外呼和邮件发送暂缓 |
| 日历/任务 | `calendar-scheduling`, `cal-com`, `opentask`, `sunsama` | 只允许 mock 计划，不写日历/任务系统 |
| 电商/广告 | `woocommerce`, `clawshop-pro`, `linkfox-amazon-ads-entity`, `ad-copy-gen`, `getresponse` | API/店铺/广告平台风险高，先暂缓；文案类可作为线索 |
| 客服/RAG/搜索 | `swarmvault`, `agentcall`, `knowledge-rag`, `anysearch`, `safe-shrink`, `cms-docdb` | RAG/搜索/外呼边界需核验，默认暂缓 |
| HR/薪酬 | `zoho-people`, `diting-compensation-expert` | 高敏 HR/薪酬，暂缓 |
| 财务/票据 | `fl-invoice-tracker`, `simple-ledger`, `expense-invoice-ocr` | 只允许字段抽取线索，不输出财税/报销结论 |
| 合同/法务 | `contract-reviewer` | 法务高风险，暂缓；只能做条款分区/风险提示候选 |

## L1 输出格式

许可证复核窗口回传时按以下格式输出：

| 字段 | 内容 |
| --- | --- |
| 项目名 | 仓库或页面名 |
| 链接 | 原始链接和纠错后链接 |
| 来源类型 | GitHub 或 ClawHub |
| LICENSE/SPDX | 明确许可证或“不明” |
| 维护状态 | 活跃、一般、停更、归档、不明 |
| README 商用限制 | 无明显限制、有附加限制、不明 |
| 依赖/API/模型风险 | 外部 API、OAuth、模型、浏览器、云 OCR、网页抓取等 |
| 可封装性 | 直接 Skill、组件、线索、完整产品/大型框架、暂缓 |
| 初始评分 | 0-100 |
| 建议动作 | 送 L2、组件观察、补资料、暂缓、淘汰 |

## 当前状态

L1 初筛已完成，结果见 `LICENSE_REVIEW_RESULT.md`。

| 队列 | 状态 |
| --- | --- |
| GitHub 14 个链接 | 已完成 L1 初筛 |
| 可送正式 L2 simulated | `visual_prompt_brief_candidate`, `sales_followup_draft_candidate`, `sales_meeting_task_brief_candidate`, `lead_research_brief_candidate`, `competitor_product_snapshot_candidate` |
| L2 优先但需补资料 | `order_inventory_exception_candidate`, `support_quality_eval_candidate`, `hr_resume_privacy_masker_candidate` |
| ClawHub 43 个链接 | 许可证/SPDX、维护状态、作者授权、依赖/API/模型条款不可核验，全部暂缓或仅作线索 |
| 客户可调用 | 不新增；仍只认已验收 13 个 Skill |
