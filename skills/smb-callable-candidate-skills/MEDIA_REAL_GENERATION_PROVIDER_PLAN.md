# 真实图片/视频生成智能体接入计划

更新日期: 2026-06-05

## 结论

媒体类智能体的目标不是停留在 prompt / brief，而是要能真实出图片、真实出视频。prompt、分镜、脚本只是生成前置层；真正可用的媒体智能体必须最终完成受控真实生成 smoke。

当前平台模型通道采用 OpenAI-compatible 多路由中转站。后续接入策略是：

1. 先验证中转站是否支持目标模型的生成 endpoint、参数、文件返回格式和计费。
2. 中转站支持的 provider/model，直接作为本平台媒体生成候选。
3. 中转站不支持但市场认可度高的 provider，进入 `provider_key_required` 或 `adapter_required`，由平台决定是否单独接入。
4. 真实生成只允许写入 runner 的 sandbox 输出目录，不允许上传、发布、投放或写业务系统。

客户正式可调用 Skill 数量仍为 13；真实生成 smoke 通过也只代表候选调用通过，不自动进入稳交付。

## 市场认可 Provider 优先级

| 优先级 | provider / route | 适合能力 | 候选定位 | 关键复核点 |
| --- | --- | --- | --- | --- |
| P0 | OpenAI GPT Image | 通用图片生成、图片编辑 | 若中转站支持，优先做真实出图 smoke | endpoint 是否兼容、组织/安全验证、返回文件格式 |
| P0 | Google Imagen / Veo via Gemini API or relay | 商品图、短视频、9:16 社媒视频 | 若中转站支持，优先做真实生成 smoke | relay 是否支持 Gemini/Veo 参数、视频轮询和文件下载 |
| P0 | fal.ai multi-model route | FLUX、Kling、Seedance、Veo、Sora、Topaz、抠图、upscale | 很适合做多模型媒体代理 | 是否可用同一中转站 key；否则 BYOK/provider key |
| P1 | Runway API | 高质量视频、图生视频、广告素材 | 视频生成候选 | 账号/API key、模型参数、费用、时长限制 |
| P1 | Luma Ray / Dream Machine API | 文生视频、图生视频、镜头运动 | 视频生成候选 | API key、下载 URL、图生视频素材 URL 要求 |
| P1 | Stability / Stable Diffusion / SDXL / SD3 | 图片生成、品牌图、商品图 | 可作为低成本图片路线 | 商用条款、模型托管方式、内容安全 |
| P1 | Replicate | 开源模型托管、FLUX/Wan/Hunyuan 等 | 多模型候选 | 模型许可证差异大，需逐模型 L1 |
| P1 | Sora legacy API | 短期遗留视频生成 | 不作为长期主路线 | OpenAI Help Center 显示 Sora API 将于 2026-09-24 停止，若中转站仍支持也只做迁移窗口验证 |
| P2 | ComfyUI / self-hosted Wan / Hunyuan / Flux | 自托管可控生成 | 长期路线 | GPU、模型许可证、运维、队列和内容安全 |
| P2 | HeyGen / Synthesia / avatar tools | 口播、培训、销售视频 | 头像视频候选 | 肖像/声音授权、企业条款、上传素材 |
| P2 | Figma / Canva / Remotion / Hyperframes | 设计文件、模板化视频和导出 | 生产工作流候选 | 写文件/导出/上传边界 |

## 真实生成候选类型

| candidate_type | 说明 | 允许进入候选库 | 进入稳交付前置 |
| --- | --- | --- | --- |
| `real_image_generation_agent` | 能真实生成图片、海报、商品图、社媒图 | 是 | 真实生成 smoke + 内容安全 + 成本/日志 |
| `real_image_edit_agent` | 能编辑、抠图、upscale、换背景 | 是 | 输入素材授权、文件处理边界、结果存储 |
| `real_video_generation_agent` | 能生成短视频、图生视频、广告视频 | 是 | 真实生成 smoke + 轮询/下载 + 安全水印/审核 |
| `real_video_edit_agent` | 剪辑、口型、upscale、背景移除 | 是 | 肖像/声音授权、上传素材、输出审核 |
| `programmatic_video_agent` | Remotion/Hyperframes 等模板化视频 | 是 | 本地渲染 sandbox、依赖锁定、文件输出审计 |

## 最小真实生成 smoke

第一批真实生成 smoke 不追求复杂效果，只验证“能跑通、能落文件、能审计、不会越权”。

| smoke | 输入 | 预期输出 | 失败判定 |
| --- | --- | --- | --- |
| 图片文生图 | 一条中文商品海报 prompt，指定 1:1 或 4:5 | 1 张图片文件 + metadata JSON | 未生成文件、调用非批准模型、无费用/模型记录 |
| 图片编辑/变体 | 使用 mock 或平台自有测试图 | 1 张编辑结果 + 授权说明字段 | 读取客户真实图、未记录素材来源 |
| 视频文生视频 | 5-8 秒中文场景 prompt，9:16 | 1 个短视频文件 + metadata JSON | 未轮询完成、未保存文件、费用/模型不明 |
| 图生视频 | 使用平台自有测试图 + 动作 prompt | 1 个短视频文件 + metadata JSON | 使用外部未授权素材、上传位置不明 |
| 程序化视频 | mock 数据生成 10 秒竖版运营日报视频 | 1 个本地 mp4 + render log | 写出 sandbox 之外、依赖未锁定 |

## 真实生成运行边界

允许：

- 调用已批准的中转站模型 route 或已批准 provider API。
- 将生成结果写入 runner sandbox 输出目录。
- 记录 model、provider、prompt hash、尺寸、时长、费用、job id、输出文件路径、审核状态。

不允许：

- 上传客户真实素材，除非后续明确授权。
- 发布到小红书、抖音、B站、视频号、广告平台或网盘。
- 把生成结果直接写 CRM、店铺、CMS、素材库或客户系统。
- 声明肖像、商标、字体、音乐、图片或视频素材授权已经自动解决。
- 自动使用真人肖像、员工照片、客户照片、名人、商标或版权角色。
- 承诺播放量、转化率、销量、排名或广告效果。

## 各窗口任务

| 窗口 | 任务 |
| --- | --- |
| 研究窗口 | 从 open-design、agency-agents-zh、native skills、fal/Runway/Luma/Google/OpenAI 等来源整理真实生成候选，优先短视频、商品图、海报、社媒卡、广告素材 |
| 许可证窗口 | 复核 provider 条款、模型商用边界、内容政策、素材上传/存储、计费、BYOK 或中转站支持情况 |
| 测试台窗口 | 先做 route check，再做 1 张图/1 段短视频的真实生成 smoke；所有输出进 sandbox |
| 封装窗口 | 为通过真实 smoke 的候选生成 `CANDIDATE.md` / `candidate.yaml`，字段必须包含 provider route、成本、输出路径、安全审核 |
| 平台验收窗口 | 做候选调用验收；只有通过正式平台验收后，才可进入稳交付扩容 |

## 本轮已落地真实生成候选

本轮已新增 16 个 `needs_license_review` 候选卡，详见 `MEDIA_REAL_GENERATION_RESEARCH_EXPANSION_RESULT.md` 与 `queues/MEDIA_REAL_GENERATION_LICENSE_REVIEW_QUEUE.md`。

| rank | candidate_id | source | target_capability | preferred_route |
| ---: | --- | --- | --- | --- |
| 1 | `openai_gpt_image_real_generation_agent_candidate` | OpenAI API | 图片生成/编辑 | relay route check |
| 2 | `google_imagen_real_image_agent_candidate` | Google Imagen/Gemini | 图片生成 | relay/provider adapter |
| 3 | `google_veo_real_video_agent_candidate` | Google Veo/Gemini | 短视频/图生视频 | relay/provider adapter |
| 4 | `fal_multi_model_media_router_candidate` | fal.ai | 多模型图片/视频/音频/3D | relay or BYOK |
| 5 | `runway_real_video_generation_agent_candidate` | Runway API | 高质量视频/图生视频 | provider key or relay |
| 6 | `luma_ray_video_generation_agent_candidate` | Luma API | 图生视频/镜头运动短片 | provider key or relay |
| 7 | `bfl_flux_real_image_agent_candidate` | BFL FLUX | 高质量图片 | provider/hosted route |
| 8 | `ideogram_typography_image_agent_candidate` | Ideogram API | 带字海报/社媒卡图 | provider key or relay |
| 9 | `recraft_brand_asset_image_agent_candidate` | Recraft API | 品牌资产/插画/设计图 | provider key or relay |
| 10 | `replicate_media_model_router_candidate` | Replicate | 开源模型托管路由 | model-level review |
| 11 | `stability_image_generation_agent_candidate` | Stability AI | Stable Diffusion 图片 | provider key or relay |
| 12 | `comfyui_self_host_media_engine_candidate` | ComfyUI | 自托管媒体工作流 | infrastructure required |
| 13 | `remotion_programmatic_video_agent_candidate` | Remotion | 程序化视频渲染 | local sandbox |
| 14 | `heygen_avatar_video_agent_candidate` | HeyGen API | 数字人口播视频 | provider key |
| 15 | `synthesia_avatar_video_agent_candidate` | Synthesia API | 企业数字人视频 | provider key |
| 16 | `open_design_real_media_skill_pack_candidate` | open-design | 媒体子 skill 源级包 | child skill review |
