# 图片/视频制作智能体候选梳理

更新日期: 2026-06-05

## 结论

有，而且要按“真实生成目标 + 分层准入”推进。

本平台当前模型通道采用 OpenAI-compatible 多路由中转站。它既可以承接 prompt / brief / 分镜 / 脚本，也应该作为真实图片/视频模型的优先路由入口。后续目标是验证中转站能否切换到图片生成、图片编辑、文生视频、图生视频等模型，并完成受控真实生成 smoke。

prompt、分镜、脚本只是媒体生成前置层，不是最终能力边界。真实图片/视频/音频生成、Figma 写入、PPT/HTML 导出、平台上传等动作必须走单独 route/API 依赖复核；通过后可以做 sandbox 内真实生成，但仍不得上传、发布、投放或写业务系统。

客户正式可调用数量仍为 13；本文件只新增媒体类候选推进口径，不新增稳交付 Skill。

## 三层分流

| 层级 | 类型 | 能否先用中转站试跑 | 推荐状态 | 说明 |
| --- | --- | --- | --- | --- |
| P0 | brief / prompt / storyboard / script / review | 可以 | `mock_callable` 或 `role_smoke` | 只调用模型，输出结构化文本，不生成真实媒体 |
| P1 | image/card/poster/design dry-run | 可以做 dry-run | `dry_run_callable` 或 `needs_license_review` | 只输出卡片/海报/商品图方案，不截图、不导出、不调用生成 API |
| P2 | real generation / edit / export | 需要 route check | `real_generation_route_check` 或 `needs_license_review` | fal、Veo、Runway、Luma、Venice、Figma、Remotion、PPTX 等需单独 API/依赖复核；Sora 只作遗留迁移观察 |

新增真实生成路线见 `MEDIA_REAL_GENERATION_PROVIDER_PLAN.md` 与 `queues/MEDIA_REAL_GENERATION_PROVIDER_REVIEW_QUEUE.md`。

## P0：优先送 role/mock smoke

| source | candidate / role | 六部门场景 | 中转站适配 | 下一步 |
| --- | --- | --- | --- | --- |
| existing candidate | `visual_prompt_brief_candidate` | 创意设计、美工、商品图、活动海报 | 可直接输出视觉 brief | 已是 `draft_l3`，等待平台侧候选调用复核 |
| native skill | `native_visual_prompt_brief_skill_candidate` | 创意设计、营销视觉 | 可直接输出 prompt brief | L1 后送 DeepAgents smoke |
| native skill | `native_image_marketing_skill_candidate` | 营销图片、社媒图、商品图 | 可直接输出 image brief | L1 后送 DeepAgents smoke |
| native skill | `native_video_brief_skill_candidate` | 短视频脚本、分镜、素材清单 | 可直接输出 video brief | L1 后送 DeepAgents smoke |
| agency-agents-zh | `design/design-image-prompt-engineer.md` | 视觉提示词、素材构思 | 可 role smoke | 测试台按 role smoke 队列执行 |
| agency-agents-zh | `design/design-visual-storyteller.md` | 活动视觉故事线、短视频分镜 | 可 role smoke | 测试台按 role smoke 队列执行 |
| agency-agents-zh | `design/design-brand-guardian.md` | 品牌视觉规范、禁用表达 | 可 role smoke | 测试台按 role smoke 队列执行 |
| agency-agents-zh | `design/design-ui-designer.md` | 页面/落地页视觉评审 | 可 role smoke | 测试台按 role smoke 队列执行 |
| agency-agents-zh | `marketing/marketing-short-video-editing-coach.md` | 短视频剪辑建议、字幕与节奏 | 可 role smoke，需补 L1 子角色 | 研究窗口补入下一批 role queue |
| agency-agents-zh | `marketing/marketing-video-optimization-specialist.md` | 视频标题、封面、完播率优化 | 可 role smoke，需补 L1 子角色 | 研究窗口补入下一批 role queue |
| agency-agents-zh | `marketing/marketing-douyin-strategist.md` | 抖音内容选题、脚本、发布策略 | 可 role smoke，需补 L1 子角色 | 研究窗口补入下一批 role queue |
| agency-agents-zh | `marketing/marketing-xiaohongshu-operator.md` | 小红书种草图文、封面和内容节奏 | 可 role smoke | 已在 Top60 role queue |
| agency-agents-zh | `marketing/marketing-bilibili-strategist.md` | B 站视频选题、脚本、栏目策略 | 可 role smoke | 已在 Top60 role queue |
| agency-agents-zh | `paid-media/paid-media-creative-strategist.md` | 投放素材 brief、广告创意方向 | 可 role smoke | 已在 Top60 role queue |

## P1：图片/设计 dry-run 候选

| source | child skill | 六部门场景 | 依赖判断 | 下一步 |
| --- | --- | --- | --- | --- |
| open-design | `design-brief` | 创意设计、活动物料 brief | 不需要真实生成 API，但可能写文件 | 已 L1: `can_dry_run_smoke` |
| open-design | `card-xiaohongshu` | 小红书卡片图结构和文案 | 不需要真实生成 API，但有截图/导出风险 | 已 L1: `can_dry_run_smoke` |
| open-design | `card-twitter` | 社媒分享卡结构和文案 | 不需要真实生成 API，但有截图/导出风险 | 已 L1: `can_dry_run_smoke` |
| open-design | `frontend-design` | 落地页/活动页设计 brief | 不需要真实生成 API，但可能写代码/预览 | 已 L1: `can_dry_run_smoke` |
| open-design | `poster-hero` | 活动主视觉/海报方向 | 需补子 skill L1 | 许可证窗口补 API/导出依赖 |
| open-design | `canvas-design` | 画布设计方案 | 需补子 skill L1 | 许可证窗口补 API/导出依赖 |
| open-design | `mockup-device-3d` | 产品截图包装、设备样机 brief | 需补子 skill L1 | 许可证窗口补 3D/导出依赖 |
| open-design | `ecommerce-image-workflow` | 商品图流程、主图/详情图方案 | 可能依赖图片生成/处理 API | 先 `dry_run_only` |
| open-design | `image-enhancer` | 图片优化建议 | 可能依赖图片处理 API | 先 `needs_license_review` |
| open-design | `image-to-code-skill` | 从图到页面结构说明 | 可能涉及 OCR/视觉模型/文件读取 | 先 `needs_license_review` |

## P2：真实图片/视频生成或工具执行候选

| source | child skill | 能力方向 | 默认边界 |
| --- | --- | --- | --- |
| open-design | `imagegen`, `imagen` | 图片生成 | `BYOK_required`, `dry_run_only`, `external_action_blocked` |
| open-design | `venice-image-generate`, `venice-image-edit` | Venice 图片生成/编辑 | `BYOK_required`, `dry_run_only`, `external_action_blocked` |
| open-design | `fal-generate`, `fal-image-edit`, `fal-upscale`, `fal-tryon`, `fal-restore`, `fal-vision`, `fal-3d` | fal 图片/视觉/3D 工具 | `BYOK_required`, `dry_run_only`, `external_action_blocked` |
| open-design | `sora` | 视频生成 | Sora API 已进入停止服务窗口，只作遗留迁移观察，不作为长期主路线 |
| open-design | `venice-video` | Venice 视频生成 | `BYOK_required`, `dry_run_only`, `external_action_blocked` |
| open-design | `fal-kling-o3`, `fal-video-edit`, `fal-lip-sync` | fal/Kling 视频、剪辑、口型 | `BYOK_required`, `dry_run_only`, `external_action_blocked` |
| open-design | `remotion`, `video-hyperframes` | 程序化视频渲染 | 不调用平台 API 也会写文件/渲染，先 dry-run |
| open-design | `gif-sticker-maker`, `slack-gif-creator` | GIF/贴纸生成 | 禁止真实导出/上传 |
| open-design | `figma-*` | Figma 文件读写/设计系统 | `BYOK_required`, 不写 Figma |
| open-design | `pptx`, `pptx-generator`, `ppt-keynote`, `nanobanana-ppt` | PPT/视觉文档生成 | 不读真实文件、不生成真实 PPT |

## 统一禁止动作与允许动作

未完成 provider route check 前：

- 不真实生成图片、视频、音频、GIF、PPT、PDF。
- 不调用 fal、Sora、Veo、Runway、Luma、Venice、Figma、OpenAI 图片/视频接口或其他第三方媒体 API。

完成 provider route check 且进入真实生成 smoke 后，允许：

- 使用批准的中转站 route 或 provider API 生成 1 张测试图或 1 段短测试视频。
- 输出到 runner sandbox。
- 记录 model、provider、job id、用量/费用、输出路径和审核状态。

始终不允许：

- 不上传素材，不发布到小红书、抖音、B 站、广告平台或任何社媒。
- 不写 Figma、Canva、PPT、网页、业务系统或文件导出目录。
- 不声明素材授权、肖像授权、商标授权或版权清白。
- 不承诺播放量、转化率、广告效果或 SEO/平台排名。

## 窗口任务

| 窗口 | 当前任务 |
| --- | --- |
| 研究窗口 | 继续补齐 agency-agents-zh 中短视频、抖音、快手、小红书、B站、社媒设计角色，按六部门场景映射，不一次性全量晋级 |
| 许可证窗口 | 对 P1/P2 open-design 子 skill 做媒体 API 依赖复核，区分中转站可用、BYOK_required、adapter_pending、blocked |
| 测试台窗口 | 先对 P0 做 role/mock smoke；P1 只做 dry-run metadata/mock smoke；P2 不做真实生成 |
| 封装窗口 | smoke 通过后只生成 `CANDIDATE.md` / `candidate.yaml`；真实生成类不得直接封 L3 |
| 平台验收窗口 | 只验收候选调用边界，不把媒体 smoke passed 等同客户正式可调用 |
