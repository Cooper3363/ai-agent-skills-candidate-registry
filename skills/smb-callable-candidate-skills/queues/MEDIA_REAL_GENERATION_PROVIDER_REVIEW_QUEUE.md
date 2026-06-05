# Media Real Generation Provider Review Queue

生成日期: 2026-06-05

## 目标

验证图片/视频智能体是否可以通过平台 OpenAI-compatible 多路由中转站或批准的 provider API 完成真实生成。

本队列不是 prompt/brief 队列；目标是进入真实出图、真实出视频候选 smoke。

## Provider Route Review

| rank | provider_or_route | media_type | market_role | route_check | default_status |
| ---: | --- | --- | --- | --- | --- |
| 1 | OpenAI GPT Image via relay | image | 通用高质量图片生成/编辑 | 测 `/images` 或 Responses image tool 是否被中转站支持 | `route_check_required` |
| 2 | Google Imagen / Veo via relay | image/video | 商品图、9:16 社媒短视频 | 测 Gemini/Veo route、视频 operation 轮询、文件返回 | `route_check_required` |
| 3 | fal.ai via relay or provider key | image/video/audio | 多模型媒体生成聚合 | 确认中转站是否代理 fal；否则 BYOK | `route_or_byok_required` |
| 4 | Runway API | video/image-to-video | 高质量视频和广告素材 | 确认是否走中转站；否则 provider key | `provider_key_required` |
| 5 | Luma Ray / Dream Machine API | video/image-to-video | 镜头运动、图生视频 | 确认是否走中转站；否则 provider key | `provider_key_required` |
| 6 | OpenAI Sora legacy via relay | video | 短期遗留视频生成 | 仅确认迁移窗口；不作为长期主路线 | `sunset_watchlist` |
| 7 | Stability / Stable Diffusion provider | image | 低成本图片生成 | 确认模型许可证和 route | `route_or_byok_required` |
| 8 | Replicate | image/video/open models | 开源模型托管 | 逐模型许可证复核 | `provider_key_required` |
| 9 | ComfyUI self-hosted | image/video | 自托管可控生成 | GPU、模型许可、队列、隔离 | `infrastructure_required` |
| 10 | Remotion / Hyperframes local | video | 模板化视频 | 本地 sandbox 渲染 | `local_sandbox_required` |

## Route Check 输出字段

| 字段 | 说明 |
| --- | --- |
| provider_or_route | 中转站 route 或 provider 名称 |
| endpoint_family | image_generation / image_edit / text_to_video / image_to_video / video_edit / programmatic_render |
| model_id_tested | 实测模型 ID |
| relay_supported | true / false / partial |
| auth_mode | relay_key / provider_key / service_account / local |
| output_format | png / webp / mp4 / gif / url / base64 / file_id |
| polling_required | true / false |
| sandbox_write_ok | true / false |
| cost_logged | true / false |
| content_safety_notes | 内容安全与水印/审核说明 |
| route_result | can_real_smoke / needs_adapter / needs_provider_key / blocked |

## 第一批真实生成 smoke 候选

| rank | candidate_id | media_type | use_case | min_smoke |
| ---: | --- | --- | --- | --- |
| 1 | `real_product_poster_image_agent_candidate` | image | 茶饮店新品海报 | 生成 1 张 4:5 图片 |
| 2 | `real_social_card_image_agent_candidate` | image | 小红书活动卡图 | 生成 1 张 3:4 或 4:5 图片 |
| 3 | `real_ecommerce_main_image_agent_candidate` | image | 商品主图 | 生成 1 张 1:1 商品图 |
| 4 | `real_image_edit_background_agent_candidate` | image_edit | 平台自有测试图换背景 | 输出 1 张编辑图 |
| 5 | `real_short_video_generation_agent_candidate` | video | 门店活动 5-8 秒短视频 | 输出 1 个 9:16 mp4 |
| 6 | `real_product_image_to_video_agent_candidate` | image_to_video | 商品图动效短视频 | 输出 1 个 5-8 秒 mp4 |
| 7 | `real_ad_video_clip_agent_candidate` | video | 电商促销广告片 | 输出 1 个短视频 |
| 8 | `real_programmatic_report_video_agent_candidate` | video_render | 运营日报短视频 | 本地渲染 1 个 mp4 |

## 硬边界

- 只使用平台批准的测试 prompt 和平台自有测试素材。
- 生成结果只能写入 DeepAgents runner / media smoke sandbox 输出目录。
- 禁止上传、发布、投放、写业务系统。
- 禁止读取客户真实素材或客户文件。
- 禁止真人肖像、名人、商标、版权角色、音乐和声音克隆，除非后续有明确授权。
- 每次真实生成必须记录 provider、model、job id、费用或用量、输出路径、审核状态。
