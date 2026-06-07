# REAL_MEDIA_PROVIDER_SMOKE_QUEUE

生成日期：2026-06-05

来源：`../REAL_MEDIA_PROVIDER_SMOKE_PRECHECK.md`

状态：真实 provider smoke 预备队列。当前只允许 route/config/terms 准备，不代表允许真实 provider 调用。

硬边界：

- 不写 key。
- 不直接调用 provider。
- 不生成图片、视频或数字人。
- 不上传真实客户/员工/候选人/未授权商品素材。
- 不发布、不外发、不客户调用。
- 输出只允许进入 runner sandbox。
- 真实最小样例必须等待指挥中心后续批准。

## Queue

| priority | candidate_id | provider/API | smoke_stage | required_before_real_generation | max_real_sample_if_approved | manual_review_trigger | queue_status |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | `marketing_real_poster_banner_agent_candidate` | OpenAI image relay | route/config/terms check | OpenAI image terms, key托管, 费用上限, 内容安全, 输出审计 | 1 张 mock 活动海报 | 品牌/商标、人物、价格促销、版权或政策命中 | `route_check_ready` |
| 2 | `ecommerce_product_main_image_agent_candidate` | OpenAI image relay | route/config/terms check | OpenAI image terms, 商品真实性边界, 商标/素材授权, 输出审计 | 1 张 mock 商品主图 | 商品失真、商标/包装风险、虚假卖点、规格不确定 | `route_check_ready` |
| 3 | `store_menu_poster_generation_candidate` | OpenAI image relay | route/config/terms check | OpenAI image terms, 菜单/价格人工确认, 字体/商标边界, 输出审计 | 1 张 mock 菜单海报 | 价格/菜单不确定、商标/字体风险、食品图片授权、促销承诺 | `route_check_ready` |
| 4 | `marketing_short_video_ad_agent_candidate` | Google Veo/Gemini | terms + route check | Google/Veo terms, route轮询/下载, 费用上限, 广告内容安全 | 1 个 5-8 秒 mock 视频 | 人物/肖像、音乐、竞品/商标、夸大宣传、违规广告 | `needs_terms_and_route_check` |
| 5 | `ecommerce_product_video_from_image_candidate` | Luma API | terms + route check | Luma terms, 输入图授权, 下载/存储边界, 费用上限 | 1 个 5 秒以内 mock 商品视频 | 输入图授权不明、商品失真、商标/包装风险、下载/存储条款不清 | `needs_terms_and_route_check` |
| 6 | `sales_avatar_pitch_video_candidate` | HeyGen API | terms + avatar rights check | HeyGen terms, stock/授权 avatar, 声音/肖像权, 不外发 | 1 个 15-30 秒 stock avatar mock pitch | 真人肖像/声音、外发意图、价格/合同承诺、夸大产品效果 | `needs_terms_avatar_rights_check` |
| 7 | `hr_training_avatar_video_candidate` | Synthesia API | terms + avatar rights check | Synthesia terms, stock/授权 avatar, 员工制度人工审核, 不发布 | 1 个 15-30 秒 stock avatar 培训片段 | HR/劳动制度争议、员工隐私、肖像/声音、政策文本未经确认 | `needs_terms_avatar_rights_check` |
| 8 | `ecommerce_background_replace_agent_candidate` | fal image edit | model terms + upload check | fal terms, 具体模型条款, 输入素材授权, 上传/存储边界 | 1 张 mock 商品背景替换图 | 具体模型条款不清、上传/存储不清、商品/商标授权不明、背景误导 | `needs_model_terms_and_upload_check` |

