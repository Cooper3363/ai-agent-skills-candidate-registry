# Open Design External API Dependency Review Result

回传时间：2026-06-04

## 已完成事项

已按 `OPEN_DESIGN_EXTERNAL_API_DEPENDENCY_REVIEW_QUEUE.md` 与 `OPEN_DESIGN_PRELIMINARY_API_SCAN.md`，对 `nexu-io/open-design` 的优先 13 个子 skill 做 read-only L1 / external API dependency 复核。

本轮只做公开 GitHub / raw `SKILL.md` / README / LICENSE 只读核验；未安装依赖，未调用 fal、Figma、OpenAI、Venice、browser automation、upload/export/download、image/video/audio generation、PPT/PDF generation 或任何真实 API。

## 仓库许可证与商用边界

| 项目 | 结论 |
| --- | --- |
| source_project | `nexu-io/open-design` |
| source_url | https://github.com/nexu-io/open-design |
| repo license | Apache-2.0；GitHub 与根目录 `LICENSE` 均显示 Apache-2.0 |
| bundled template notes | README / repo 摘要说明 `skills/guizang-ppt/` 保留原 MIT 与作者归属，`skills/html-ppt/` 保留原 MIT 与作者归属 |
| commercial boundary | 仓库主许可宽松；但 README 明确含 BYOK、MCP、CLI adapters、Model Router、image/video/deck/export 等能力。不能整仓作为可调用库收入，必须按子 skill 限定 trial mode |
| customer-callable | 否。本轮不得标记任何 open-design skill 为 customer-callable；稳交付库仍为 13 |

## 子 Skill 复核表

| child skill | upstream_skill_md_verified | requires_external_api | dependency families | BYOK_required | l1_result | final_trial_mode | 建议加入 `candidates/needs_license_review` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad-creative` | true；`skills/ad-creative/SKILL.md` verified，catalog wrapper 指向 `coreyhaines31/marketingskills` | no for wrapper; upstream full workflow需另核 | model provider risk if used with agent; ad platform risk; no fal/Figma/browser in wrapper | false | `can_mock_smoke` | `mock_only`, `read_only`, `external_action_blocked` | 是，作为 open-design child candidate；仅输出广告创意 brief/copy，不投放、不调用广告 API |
| `brand-guidelines` | true；`skills/brand-guidelines/SKILL.md` verified，指向 Anthropic brand-guidelines | no direct API | brand/trademark; upstream Anthropic skill license/brand usage boundary; no fal/Figma/browser in wrapper | false | `needs_more_license_info` | `mock_only`, `read_only`, `external_action_blocked` | 否；需确认不得复用 Anthropic 官方品牌资产，可改为内部“品牌规范检查模板” |
| `design-brief` | true；`skills/design-brief/SKILL.md` verified | no external API, but writes artifacts | file_write, HTML preview, design-system generation; no fal/Figma/model provider required by skill text | false | `can_dry_run_smoke` | `dry_run_only`, `read_only`, `external_action_blocked` | 是；只输出 DESIGN.md/brief-preview 草案文本，不真实写文件 |
| `design-review` | true；`skills/design-review/SKILL.md` verified，catalog wrapper 指向 `garrytan/gstack` | likely yes in upstream; wrapper itself no | browser/screenshot, repo edits, atomic commits, before/after screenshots; upstream license and exact workflow未核 | unknown | `needs_more_license_info` | `dry_run_only`, `read_only`, `external_action_blocked` | 否；需定位 `gstack` 上游许可证和具体 workflow，当前不得 smoke |
| `faq-page` | true；`skills/faq-page/SKILL.md` verified | no external API | HTML/JS artifact generation, possible export/download if used in full OD; no model provider/fal/Figma required by skill text | false | `can_dry_run_smoke` | `dry_run_only`, `read_only`, `external_action_blocked` | 是；仅输出 FAQ 页面结构/HTML 草案，不写文件、不导出 |
| `data-report` | true；`skills/data-report/SKILL.md` verified | no direct API, but CDN/chart dependency noted | CSV/Excel/JSON parsing, Chart.js/ECharts via jsdelivr CDN, HTML report generation, file/export risk | false for mock; BYOK not needed | `can_dry_run_smoke` | `dry_run_only`, `read_only`, `external_action_blocked` | 是；仅 mock 数据摘要/报告结构，不读真实文件、不加载 CDN、不导出 |
| `finance-report` | true；`skills/finance-report/SKILL.md` verified | no external API | finance report HTML, inline charts, financial data sensitivity; no tax/audit/investment conclusions | false | `can_mock_smoke` | `mock_only`, `read_only`, `external_action_blocked` | 是；只用 mock 财务摘要，必须 `not_financial_advice=true` |
| `hr-onboarding` | true；`skills/hr-onboarding/SKILL.md` verified | no external API | HR onboarding HTML, employee PII, handbook/payroll references; no system writes | false | `can_mock_smoke` | `mock_only`, `read_only`, `external_action_blocked` | 是；只用 mock 入职信息，不读真实员工文件、不写 HR 系统 |
| `frontend-design` | true；`skills/frontend-design/SKILL.md` verified; folder claims `LICENSE.txt` upstream Apache-2.0 terms | no external API required by skill text | code/file write, frontend artifact generation, possible browser preview/export; no fal/Figma required | false | `can_dry_run_smoke` | `dry_run_only`, `read_only`, `external_action_blocked` | 是；只输出前端设计 brief / UI spec，不写代码文件、不预览浏览器 |
| `card-xiaohongshu` | true；`skills/card-xiaohongshu/SKILL.md` verified | no external API | HTML card artifact, screenshot/export/social publishing risk, image/card generation semantics | false | `can_dry_run_smoke` | `dry_run_only`, `read_only`, `external_action_blocked` | 是；只输出卡片 brief/文案结构，不截图、不生成图片、不发布 |
| `card-twitter` | true；`skills/card-twitter/SKILL.md` verified | no external API | HTML card artifact, screenshot/export/social publishing risk, Twitter/X brand/platform risk | false | `can_dry_run_smoke` | `dry_run_only`, `read_only`, `external_action_blocked` | 是；只输出分享卡 brief/文案结构，不截图、不发布 |
| `pptx` | true；`skills/pptx/SKILL.md` verified，catalog wrapper 指向 Anthropic `pptx` skill | likely yes/tooling in upstream; wrapper itself no | PPTX generation/editing, file read/write, possible Python/Office tooling, upstream license details not pinned in wrapper | unknown | `needs_more_license_info` | `dry_run_only`, `read_only`, `external_action_blocked` | 否；需核 Anthropic `pptx` 具体 LICENSE / dependencies，当前不得 smoke |
| `slides` | true；`skills/slides/SKILL.md` verified，catalog wrapper 指向 `openai/skills` | likely yes/tooling in upstream; wrapper itself no | PptxGenJS, deck generation/editing, file export, OpenAI skills upstream license/dependency未核 | unknown | `needs_more_license_info` | `dry_run_only`, `read_only`, `external_action_blocked` | 否；需核 `openai/skills` slides 子目录许可证和依赖，当前不得 smoke |

## 分类汇总

| l1_result | 数量 | child skills |
| --- | ---: | --- |
| `can_mock_smoke` | 3 | `ad-creative`, `finance-report`, `hr-onboarding` |
| `can_dry_run_smoke` | 6 | `design-brief`, `faq-page`, `data-report`, `frontend-design`, `card-xiaohongshu`, `card-twitter` |
| `needs_more_license_info` | 4 | `brand-guidelines`, `design-review`, `pptx`, `slides` |
| `blocked` | 0 | 无 |

## 当前问题

- `open-design` 根仓库 Apache-2.0 可接受，但 155 个 skill 中 152 个带外部依赖关键词，不能整仓收入候选库。
- `brand-guidelines` 使用 Anthropic 官方品牌规范语义，存在商标/品牌授权边界，不建议按原子 skill 进入 smoke。
- `design-review`、`pptx`、`slides` 均为 catalog wrapper 指向上游完整 workflow；wrapper 可见，但上游许可证、依赖和 manifest 未闭合。
- `data-report`、`card-*`、`frontend-design` 等即使不需要外部 API，也涉及 HTML/file/export/browser preview 类动作，必须 dry-run。

## 需要 AI.Skills 指挥中心决策的问题

- 是否允许将 9 个 `can_mock_smoke` / `can_dry_run_smoke` 子 skill 作为 open-design child candidate 加入 `candidates/needs_license_review`，但仅用于 DeepAgents smoke，不进入正式 L2。
- 是否将 `brand-guidelines` 改写为内部模板候选，避免 Anthropic 官方品牌资产/商标复用。
- 是否要求研究窗口对 `design-review` 的 `garrytan/gstack`、`pptx` 的 Anthropic upstream、`slides` 的 `openai/skills` upstream 做单独 L1。

## 建议下一步

1. 可进入候选库 child candidate / DeepAgents smoke 预备队列：`ad-creative`, `design-brief`, `faq-page`, `data-report`, `finance-report`, `hr-onboarding`, `frontend-design`, `card-xiaohongshu`, `card-twitter`。
2. 暂不进入 smoke：`brand-guidelines`, `design-review`, `pptx`, `slides`。
3. 所有 open-design child candidate 必须默认：
   - `customer_callable=false`
   - `external_action_blocked=true`
   - `send_allowed=false`
   - `write_allowed=false`
   - 不调用 fal / Figma / OpenAI / model provider / browser automation / upload / export / download / image/video/audio/PPT/PDF generation。
4. 稳交付库仍为 13。
