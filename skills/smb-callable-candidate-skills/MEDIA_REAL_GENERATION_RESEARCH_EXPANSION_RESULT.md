# 媒体真实生成智能体扩展研究结果

更新日期: 2026-06-05

## Summary

已按“先多找，再入库”的口径扩展真实图片/视频生成智能体候选。

- 新增候选卡: 16
- 新增状态: 全部 `needs_license_review`
- 新增方向: 真实出图、真实出视频、图生视频、图片编辑、数字人口播、程序化视频、自托管媒体引擎
- 当前候选库总数: 167
- 当前稳交付客户正式可调用 Skill: 13，未改变

## 入库原则

本轮只收“真实生成目标”的候选，不再只收 prompt/brief。入库条件：

1. 有市场认可度或明确官方 API/开源项目来源。
2. 可映射到六部门场景。
3. 可通过中转站 route check、provider key 或本地 sandbox 接入。
4. 进入候选库后先做 L1/provider/model review，不直接 L2，不直接稳交付。

## 新增 16 个候选

| candidate_id | source | media_type | 六部门主场景 | model_channel_fit | 当前状态 |
| --- | --- | --- | --- | --- | --- |
| `openai_gpt_image_real_generation_agent_candidate` | OpenAI API | image | 商品海报、活动图、社媒图 | relay route check | needs_license_review |
| `google_imagen_real_image_agent_candidate` | Google Imagen/Gemini | image | 品牌图、商品图、社媒图 | relay/provider adapter | needs_license_review |
| `google_veo_real_video_agent_candidate` | Google Veo/Gemini | video | 短视频、商品展示、活动视频 | relay/provider adapter | needs_license_review |
| `fal_multi_model_media_router_candidate` | fal.ai | image/video/audio/3D | 多模型媒体生成、upscale、图生视频 | relay or BYOK | needs_license_review |
| `runway_real_video_generation_agent_candidate` | Runway API | video | 高质量广告短片、商品视频 | provider key or relay | needs_license_review |
| `luma_ray_video_generation_agent_candidate` | Luma Ray/API | video/image-to-video | 商品图生视频、镜头运动短片 | provider key or relay | needs_license_review |
| `bfl_flux_real_image_agent_candidate` | Black Forest Labs FLUX | image | 品牌图、商品场景图 | provider/hosted route | needs_license_review |
| `ideogram_typography_image_agent_candidate` | Ideogram API | image/text | 带字海报、社媒卡图、商品卖点图 | provider key or relay | needs_license_review |
| `recraft_brand_asset_image_agent_candidate` | Recraft API | image/vector/design | 品牌资产、插画、社媒模板 | provider key or relay | needs_license_review |
| `replicate_media_model_router_candidate` | Replicate | image/video/open models | 多模型托管、实验模型 | model-level review | needs_license_review |
| `stability_image_generation_agent_candidate` | Stability AI | image | Stable Diffusion 系列图片 | provider key or relay | needs_license_review |
| `comfyui_self_host_media_engine_candidate` | ComfyUI | image/video workflow | 自托管媒体流水线 | infrastructure required | needs_license_review |
| `remotion_programmatic_video_agent_candidate` | Remotion | programmatic video | 报表视频、活动复盘、销售跟进视频 | local sandbox | needs_license_review |
| `heygen_avatar_video_agent_candidate` | HeyGen API | avatar video | 培训、客服话术、销售口播 | provider key | needs_license_review |
| `synthesia_avatar_video_agent_candidate` | Synthesia API | avatar video | 入职培训、客服 FAQ、产品介绍 | provider key | needs_license_review |
| `open_design_real_media_skill_pack_candidate` | open-design | media skill pack | 图片/视频/设计子 skill 源级包 | child skill review | needs_license_review |

## Sources

- OpenAI image generation docs: https://platform.openai.com/docs/guides/image-generation
- Google Gemini image generation docs: https://ai.google.dev/gemini-api/docs/image-generation
- Google Gemini video generation docs: https://ai.google.dev/gemini-api/docs/video
- fal Model APIs docs: https://docs.fal.ai/model-apis
- Runway API docs: https://docs.dev.runwayml.com/
- Luma API: https://lumalabs.ai/api
- BFL / FLUX docs: https://docs.bfl.ai/
- Ideogram API docs: https://developer.ideogram.ai/
- Recraft docs: https://www.recraft.ai/docs
- Replicate docs: https://replicate.com/docs
- Stability AI docs: https://platform.stability.ai/docs
- ComfyUI GitHub: https://github.com/comfyanonymous/ComfyUI
- Remotion docs: https://www.remotion.dev/docs/
- HeyGen docs: https://docs.heygen.com/
- Synthesia docs: https://docs.synthesia.io/
- open-design GitHub: https://github.com/nexu-io/open-design

## 下一步

许可证窗口优先处理 `queues/MEDIA_REAL_GENERATION_LICENSE_REVIEW_QUEUE.md`。

测试台不得直接调用真实生成 API；必须等待 L1/provider route check 结论。L1 放行后，测试台只做最小真实生成 smoke：1 张图或 1 段短视频，输出到 runner sandbox。
