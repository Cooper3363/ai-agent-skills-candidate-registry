# Media Agent Intake Queue

生成日期: 2026-06-05

## 目标

把图片/视频制作相关的 Skill、Agent、Role、工作流包装统一纳入候选库推进。prompt / brief / role smoke 是前置层，真实图片/视频生成是最终目标之一。

模型通道口径：平台使用 OpenAI-compatible 多路由中转站。中转站可用于 prompt、brief、脚本、分镜、评审、风险提示；如果中转站支持图片/视频模型 route，也可以进入真实生成 route check 和 sandbox smoke。

客户正式可调用 Skill 数量仍为 13。

## P0 Role / Mock Smoke Queue

| rank | source | candidate_or_role | department | scenario | trial_mode | smoke boundary |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | existing candidate | `visual_prompt_brief_candidate` | 创意设计 | 海报/商品图/活动图视觉 brief | `mock_only`, `read_only` | 不生成图片 |
| 2 | native skill | `native_visual_prompt_brief_skill_candidate` | 创意设计 | 视觉提示词 brief | `dry_run_only`, `read_only` | 不调用图片 API |
| 3 | native skill | `native_image_marketing_skill_candidate` | 创意设计/运营 | 营销图片 brief、素材清单 | `dry_run_only`, `read_only` | 不生成图片 |
| 4 | native skill | `native_video_brief_skill_candidate` | 创意设计/运营 | 短视频脚本、分镜、素材清单 | `dry_run_only`, `read_only` | 不生成视频 |
| 5 | agency-agents-zh | `design/design-image-prompt-engineer.md` | 创意设计 | 视觉提示词、素材构思 | `mock_only`, `read_only` | 不生成图片 |
| 6 | agency-agents-zh | `design/design-visual-storyteller.md` | 创意设计 | 活动视觉故事线、短视频分镜 | `mock_only`, `read_only` | 不生成媒体 |
| 7 | agency-agents-zh | `design/design-brand-guardian.md` | 创意设计 | 品牌视觉规范检查 | `mock_only`, `read_only` | 只用用户提供品牌规范 |
| 8 | agency-agents-zh | `design/design-ui-designer.md` | 创意设计 | 页面/落地页视觉评审 | `mock_only`, `read_only` | 不改页面或文件 |
| 9 | agency-agents-zh | `marketing/marketing-xiaohongshu-operator.md` | 电商/运营 | 小红书图文与封面方向 | `mock_only`, `read_only` | 不发布 |
| 10 | agency-agents-zh | `marketing/marketing-bilibili-strategist.md` | 电商/运营 | B站视频选题和脚本策略 | `mock_only`, `read_only` | 不上传视频 |
| 11 | agency-agents-zh | `paid-media/paid-media-creative-strategist.md` | 电商/运营 | 广告素材 brief | `mock_only`, `read_only` | 不投放广告 |

## P1 Dry-run Candidate Queue

| rank | source | child_skill | scenario | current_l1_status | next_step |
| ---: | --- | --- | --- | --- | --- |
| 1 | open-design | `design-brief` | 活动物料/品牌视觉 brief | `can_dry_run_smoke` | 测试台做 dry-run smoke |
| 2 | open-design | `card-xiaohongshu` | 小红书卡片图结构 | `can_dry_run_smoke` | 测试台做 dry-run smoke |
| 3 | open-design | `card-twitter` | 社媒分享卡结构 | `can_dry_run_smoke` | 测试台做 dry-run smoke |
| 4 | open-design | `frontend-design` | 活动页/落地页视觉设计 brief | `can_dry_run_smoke` | 测试台做 dry-run smoke |
| 5 | open-design | `poster-hero` | 活动主视觉方向 | `needs_l1_media_dependency_review` | 许可证窗口复核 |
| 6 | open-design | `canvas-design` | 画布设计方案 | `needs_l1_media_dependency_review` | 许可证窗口复核 |
| 7 | open-design | `ecommerce-image-workflow` | 商品主图/详情图工作流 | `needs_l1_media_dependency_review` | 许可证窗口复核 |
| 8 | open-design | `mockup-device-3d` | 产品样机/设备展示图方案 | `needs_l1_media_dependency_review` | 许可证窗口复核 |
| 9 | open-design | `gif-sticker-maker` | GIF/贴纸方案 | `needs_l1_media_dependency_review` | 许可证窗口复核 |
| 10 | open-design | `image-enhancer` | 图片优化建议 | `needs_l1_media_dependency_review` | 许可证窗口复核 |

## P2 External API / Real Generation Review Queue

| rank | source | child_skill_family | dependency_family | default_trial_mode | review_focus |
| ---: | --- | --- | --- | --- | --- |
| 1 | open-design | `imagegen`, `imagen` | image generation provider | `BYOK_required`, `dry_run_only`, `external_action_blocked` | 是否支持中转站 base_url，是否真实调用图片模型 |
| 2 | open-design | `venice-image-*` | Venice image API | `BYOK_required`, `dry_run_only`, `external_action_blocked` | provider key、上传/下载、授权边界 |
| 3 | open-design | `fal-*` image skills | fal image/video API | `BYOK_required`, `dry_run_only`, `external_action_blocked` | fal key、模型费用、真实生成动作 |
| 4 | open-design | `sora` | video generation | `sunset_watchlist`, `dry_run_only`, `external_action_blocked` | Sora API 停止服务窗口内只作迁移观察，不作长期主路线 |
| 5 | open-design | `venice-video` | Venice video API | `BYOK_required`, `dry_run_only`, `external_action_blocked` | provider key、真实生成动作 |
| 6 | open-design | `fal-kling-o3`, `fal-video-edit`, `fal-lip-sync` | video generation/edit/lip sync | `BYOK_required`, `dry_run_only`, `external_action_blocked` | 肖像、声音、版权、上传风险 |
| 7 | open-design | `remotion`, `video-hyperframes` | local/programmatic video render | `dry_run_only`, `external_action_blocked` | 文件写入、渲染、导出目录 |
| 8 | open-design | `figma-*` | Figma API / MCP / file write | `BYOK_required`, `dry_run_only`, `external_action_blocked` | 不写 Figma、不创建文件 |
| 9 | open-design | `pptx*`, `ppt-keynote`, `nanobanana-ppt` | PPT generation/export | `dry_run_only`, `external_action_blocked` | 不读真实文件、不导出 PPT |

真实生成 provider route check 另见 `MEDIA_REAL_GENERATION_PROVIDER_REVIEW_QUEUE.md`。

## 测试台 smoke 输出字段

| 字段 | 说明 |
| --- | --- |
| candidate_or_role | Skill、Agent role 或 child skill 名称 |
| source | existing / native skill / agency-agents-zh / open-design |
| media_type | image / video / design / social-card / deck |
| model_channel_fit | relay_supported / adapter_pending / BYOK_required / not_suitable |
| trial_mode | mock_only / dry_run_only / BYOK_required / read_only / external_action_blocked |
| expected_outputs | brief、prompt、script、shot_list、asset_requirements、risk_notes 等 |
| forbidden_actions_present | 是否出现真实生成、上传、发布、导出、API 调用等禁止动作 |
| smoke_result | passed / needs_fix / blocked |

## 硬边界

- 未完成 route check 前，不生成真实图片、视频、音频、GIF、PPT、PDF。
- 未完成 route check 前，不调用 fal、Veo、Runway、Luma、Venice、Figma、OpenAI 图片/视频接口或其他媒体 API；Sora 只作遗留迁移观察。
- 完成 route check 后，只允许 sandbox 内最小真实生成 smoke。
- 不上传、不发布、不导出、不写文件、不写平台。
- 不声明素材授权、肖像授权、商标授权、版权清白。
- 不承诺播放量、转化率、销量、广告效果或排名。
