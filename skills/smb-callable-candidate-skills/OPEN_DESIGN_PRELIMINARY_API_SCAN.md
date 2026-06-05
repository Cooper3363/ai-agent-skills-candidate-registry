# Open Design External API Dependency Review Queue

更新日期: 2026-06-04

## Source

- source_project: nexu-io/open-design
- source_url: https://github.com/nexu-io/open-design
- local_scan_mode: read-only zip scan, no dependency install, no API call
- scan_result: 155 skill directories with SKILL.md; 152 showed at least one external dependency hint keyword.

## Preliminary Conclusion

open-design 可以作为候选来源项目进入研究/许可证复核，但不能整仓直接收入可调用库。必须按子 skill 做 L1/source/API 依赖复核。

High-risk external dependency families found by keyword scan:

| dependency_family | examples from scan | default trial mode before L1 |
|---|---|---|
| fal / image-video generation | fal-generate, fal-kling-o3, fal-upscale, fal-video-edit, fal-train, ecommerce-image-workflow | dry_run_only, BYOK_required, external_action_blocked |
| Figma / MCP / design file write | figma-use, figma-generate-design, figma-create-new-file, figma-implement-design | dry_run_only, BYOK_required, external_action_blocked |
| browser / upload / export / download | agent-browser, export-download-debugging, frontend-design, youtube-clipper | dry_run_only, external_action_blocked |
| OpenAI / model provider / token | imagegen, sora, speech, slides, screenshot | BYOK_required, dry_run_only |
| PPTX / PDF / document generation | pptx, pptx-generator, slides, pdf, minimax-pdf, pptx-html-fidelity-audit | mock_only or dry_run_only; no real file upload/export |
| video/audio generation | sora, venice-video, fal-lip-sync, remotion, speech, venice-audio-speech | dry_run_only, BYOK_required |

## Priority Low-Permission Candidates For Manual L1

These may fit SMB workflows if their SKILL.md does not require real API execution:

| skill | expected business package | L1 focus |
|---|---|---|
| ad-creative | 营销内容包 | 是否只输出创意 brief/copy，是否调用图片/广告 API |
| brand-guidelines | 营销品牌包 | 是否纯文本规范，是否引用外部品牌/设计系统 API |
| design-brief | 营销视觉包 | 是否只生成 brief，是否触发 fal/image provider |
| design-review | 营销视觉包 | 是否需要截图/浏览器/上传 |
| faq-page | 客服/官网内容包 | 是否只是页面文案/结构，是否浏览器导出 |
| data-report | 经营报表包 | 是否只总结 mock 数据，是否生成文件/图像 |
| finance-report | 经营报表/财务包 | 是否含财务建议或真实文件处理 |
| hr-onboarding | 行政 HR 包 | 是否纯文本 checklist，是否涉及员工 PII |
| frontend-design | 营销网页包 | 是否仅设计 brief，是否写文件/导出 |
| card-xiaohongshu | 营销社媒包 | 是否只输出设计 brief，是否调用 fal/image |
| card-twitter | 营销社媒包 | 是否只输出社媒卡 brief，是否调用 fal/image |
| pptx / slides | 销售赋能/汇报包 | 是否生成真实文件，是否依赖 OpenAI/PPTX 工具 |

## License Window Task

Please produce `OPEN_DESIGN_EXTERNAL_API_DEPENDENCY_REVIEW_RESULT.md` with:

- repo license and any bundled template license notes
- per-skill dependency classification for the priority list above
- whether the skill requires external API, model provider, browser, upload/export, Figma, fal, image/video/audio, PPT/PDF tooling
- suggested l1_result: can_mock_smoke / can_dry_run_smoke / needs_more_license_info / blocked
- final trial_mode: mock_only / dry_run_only / BYOK_required / read_only / external_action_blocked
- whether it can be added to `candidates/needs_license_review` as an open-design child candidate

## Hard Boundary

- Do not install open-design dependencies.
- Do not call fal, Figma, OpenAI, Venice, browser automation, upload/export/download, image/video/audio generation, PPT/PDF generation, or any real API.
- Do not read customer files or upload files.
- Do not mark any open-design skill as customer-callable.
- Stable customer-callable Skill count remains 13.