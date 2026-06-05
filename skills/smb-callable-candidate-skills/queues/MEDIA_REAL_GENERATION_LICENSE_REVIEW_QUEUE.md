# Media Real Generation License Review Queue

生成日期: 2026-06-05

来源: `MEDIA_REAL_GENERATION_RESEARCH_EXPANSION_RESULT.md`

## 目标

对 16 个真实图片/视频生成智能体候选做 L1/provider/model review，决定哪些可以进入中转站 route check 和 sandbox 真实生成 smoke。

## Queue

| rank | candidate_id | source | review_focus | expected_trial_mode |
| ---: | --- | --- | --- | --- |
| 1 | `openai_gpt_image_real_generation_agent_candidate` | OpenAI API | 中转站是否支持 GPT Image endpoint、组织验证、输出格式、计费 | `route_check_required`, `real_generation_sandbox_smoke` |
| 2 | `google_imagen_real_image_agent_candidate` | Google Imagen/Gemini | 中转站或 provider adapter、Imagen 商用条款、输出文件 | `route_check_required`, `real_generation_sandbox_smoke` |
| 3 | `google_veo_real_video_agent_candidate` | Google Veo/Gemini | 视频 operation 轮询、下载、费用、内容安全 | `route_check_required`, `real_generation_sandbox_smoke` |
| 4 | `fal_multi_model_media_router_candidate` | fal.ai | 中转站是否代理 fal、模型级许可证、BYOK、费用 | `route_or_BYOK_required`, `real_generation_sandbox_smoke` |
| 5 | `runway_real_video_generation_agent_candidate` | Runway API | provider key、模型、时长限制、费用、商用条款 | `provider_key_required`, `real_generation_sandbox_smoke` |
| 6 | `luma_ray_video_generation_agent_candidate` | Luma API | 图生视频素材 URL、下载、费用、商用边界 | `provider_key_required`, `real_generation_sandbox_smoke` |
| 7 | `bfl_flux_real_image_agent_candidate` | BFL / FLUX | FLUX 模型条款、BFL/fal/Replicate 路由、商用限制 | `route_or_provider_required`, `real_generation_sandbox_smoke` |
| 8 | `ideogram_typography_image_agent_candidate` | Ideogram API | 带字图片质量、API 条款、商用、中文标题风险 | `provider_key_required`, `real_generation_sandbox_smoke` |
| 9 | `recraft_brand_asset_image_agent_candidate` | Recraft API | 品牌资产上传、矢量/插画输出、商用条款 | `provider_key_required`, `real_generation_sandbox_smoke` |
| 10 | `replicate_media_model_router_candidate` | Replicate | 逐模型许可证、模型版本、费用和数据保留 | `model_level_l1_required`, `real_generation_sandbox_smoke` |
| 11 | `stability_image_generation_agent_candidate` | Stability AI | API 条款、模型许可、商用、内容政策 | `provider_key_required`, `real_generation_sandbox_smoke` |
| 12 | `comfyui_self_host_media_engine_candidate` | ComfyUI | repo 许可、模型许可、GPU/依赖、节点安全隔离 | `infrastructure_review_required`, `sandbox_smoke_only` |
| 13 | `remotion_programmatic_video_agent_candidate` | Remotion | 商用许可、依赖锁定、本地 render sandbox | `local_dependency_review_required`, `sandbox_render_smoke` |
| 14 | `heygen_avatar_video_agent_candidate` | HeyGen API | 肖像/声音授权、企业条款、素材上传和存储 | `provider_key_required`, `avatar_rights_review` |
| 15 | `synthesia_avatar_video_agent_candidate` | Synthesia API | avatar/voice 权利、企业条款、素材上传和存储 | `provider_key_required`, `avatar_rights_review` |
| 16 | `open_design_real_media_skill_pack_candidate` | open-design | 子 skill 拆分、整仓安装风险、provider/API 依赖 | `child_skill_l1_required`, `no_repo_install` |

## L1 输出字段

| 字段 | 说明 |
| --- | --- |
| candidate_id | 候选 ID |
| license_status | repo/provider/model 许可证或服务条款结论 |
| commercial_use_notes | 商用限制 |
| provider_key_required | 是否需要单独 provider key |
| relay_route_supported | 中转站是否可直接路由 |
| model_level_review_required | 是否需要逐模型许可证复核 |
| upload_or_storage_risk | 是否上传/存储素材或输出 |
| content_policy_risk | 内容安全、肖像、商标、版权、敏感行业风险 |
| estimated_cost_notes | 费用/用量记录方式 |
| l1_result | can_route_check / provider_key_required / model_level_review_required / infrastructure_required / blocked |
| next_queue | route_check / sandbox_smoke / needs_more_info / blocked |

## 硬边界

- L1 前不调用真实图片/视频/音频/头像 API。
- 不使用用户提供的真实客户素材。
- 不上传、不发布、不投放、不写业务系统。
- 不把 provider docs 可用等同于本平台稳交付可用。
- 稳交付客户正式可调用数量仍为 13。
