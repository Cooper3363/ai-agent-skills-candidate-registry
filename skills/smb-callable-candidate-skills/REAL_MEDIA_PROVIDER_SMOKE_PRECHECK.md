# REAL_MEDIA_PROVIDER_SMOKE_PRECHECK

回传日期：2026-06-05

## 1. 已完成事项

- 已完成 8 个真实图片/视频/数字人候选的 provider smoke 前置复核预案。
- 已明确这些候选在 Next50 Top15 L2 中属于“真实 provider smoke 后再定”，不是失败，但不得进入 draft_l3。
- 已生成真实 provider smoke 预备队列：`queues/REAL_MEDIA_PROVIDER_SMOKE_QUEUE.md`。
- 本轮未调用真实 provider/API，未写 key，未生成图片/视频，未上传素材。

## 2. 当前问题

- 真实媒体 smoke 前必须先完成 provider/API 条款、BYOK/key 托管、费用上限、内容权属、素材授权、内容安全、日志审计和失败重试方案。
- 当前任何 route/config/payload smoke 都不能写成“真实 provider 通过”。
- 数字人、试穿、背景替换、商品图和广告视频类均有额外的肖像、声音、商标、版权、素材授权和客户隐私风险。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 真实生成被流程边界阻塞：需要指挥中心/平台验收后才能执行最小真实样例。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准后续测试台创建“真实 provider smoke 最小样例”专项。
- 是否要求所有真实 provider smoke 统一走平台中转站 route，不允许测试台直接持有 provider key。
- 是否先放行 3 个 OpenAI image relay `route_check_ready` 项做 route/config 验收，再推进视频和数字人 provider。

## 5. 建议下一步

- 测试台先做 route/config/terms 准备，不做真实生成。
- 平台侧准备 key 托管、费用限额、输出 sandbox、审计日志和内容安全检查。
- 指挥中心确认 provider 商用条款与生成内容权属后，再批准每项最多 1 个最小真实样例。
- 所有真实输出只进 runner sandbox，不进稳交付库，不客户调用，不发布。

## 6. 统一前置要求

| 维度 | 要求 |
| --- | --- |
| provider/API 条款 | 记录 provider terms、commercial use、content ownership、prohibited use、retention/logging 条款来源。 |
| BYOK/key 托管 | key 不入库；测试台不可明文持有；优先平台中转站或 secrets manager；日志不得打印 key。 |
| 中转站 route | 优先 OpenAI-compatible route 或平台 provider adapter；不得绕过平台审计直连 provider。 |
| 费用上限 | 图片最多 1 张；视频/数字人最多 1 个极短样例；禁止批量生成；每项设单次预算上限。 |
| 生成内容权属 | 输出只能标记为“provider terms 下生成内容”；不得承诺版权完全清白或可无限制转授权。 |
| 素材授权 | 只能使用 mock/自有/明确授权素材；不得上传真实客户、员工、候选人或未授权商品/人物素材。 |
| 肖像/声音 | 数字人必须使用 provider stock avatar 或明确授权 avatar/voice；不得用真实员工、客户、候选人照片或声音。 |
| 商标/品牌 | 不生成仿冒品牌、受保护商标、竞品 logo；品牌素材必须由用户确认授权。 |
| 内容安全 | 生成前做 prompt policy check；生成后做 output review；失败或命中风险时进入人工审核。 |
| 日志/审计 | 记录 candidate_id、provider、route、request id、成本、输入摘要、输出路径、审核结果；不记录敏感素材正文。 |
| 失败重试 | 默认 0 次自动重试；如需重试最多 1 次，必须记录失败原因；不得循环生成。 |
| 输出存储 | 仅 runner sandbox；不得上传客户空间、不得发布、不得写稳交付库。 |

## 7. 候选复核表

| candidate_id | provider/API | 是否可走中转站 route | 是否 BYOK | key 托管建议 | 费用上限建议 | 最小真实样例是否允许 | 生成内容权属 | 内容安全 | 版权/肖像/商标/素材授权 | 日志/审计 | 失败重试 | 人工审核触发 | precheck_result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `marketing_real_poster_banner_agent_candidate` | OpenAI image API / platform image relay | 是，优先走 OpenAI-compatible image relay | 是，或平台统一 provider key | key 只进平台 secrets manager；测试台只拿 route id | 1 张图，固定尺寸，单次预算上限 | 暂不允许；route/config/terms 通过后可申请 1 张 mock 海报 | 按 OpenAI/API terms 标记，不承诺版权完全清白 | prompt + output 双审核；禁止仿冒品牌和违规营销 | 活动文案、字体、商标、品牌素材必须 mock/自有/授权 | 记录 prompt 摘要、route id、request id、成本、输出 sandbox 路径 | 默认 0 次；最多人工批准后 1 次 | 出现品牌/商标、人物、医疗金融承诺、价格促销、政策命中 | `route_check_ready` |
| `ecommerce_product_main_image_agent_candidate` | OpenAI image API / platform image relay | 是，优先走 OpenAI-compatible image relay | 是，或平台统一 provider key | key 只进平台 secrets manager；不入库 | 1 张图，单次预算上限 | 暂不允许；route/config/terms 通过后可申请 1 张 mock 商品主图 | 按 provider terms 标记；不得承诺独占版权 | 商品真实性审核；禁止虚假功能、虚假包装、仿冒品牌 | 商品、包装、logo、商标和背景素材必须授权；不上传真实客户素材 | 记录商品输入摘要、route id、request id、成本、输出路径 | 默认 0 次；最多人工批准后 1 次 | 商品与实物不符、商标/包装风险、虚假卖点、价格/规格不确定 | `route_check_ready` |
| `marketing_short_video_ad_agent_candidate` | Google Veo/Gemini video via relay/provider adapter | 理论可走平台 adapter；需先 route/config check | 是 | Google/Veo key 仅平台托管；测试台不可直连 | 1 个 5-8 秒 mock 视频，单次预算上限 | 暂不允许；terms + route 通过后可申请 1 个极短 mock 广告视频 | 按 Google/Veo terms 标记；不得承诺完全版权清白 | prompt、视频输出、广告文案三重审核 | 广告素材、人物肖像、音乐/声音、商标必须授权 | 记录 request id、轮询状态、下载 URL、成本、输出路径、审核结果 | 默认 0 次；最多人工批准后 1 次 | 人物/肖像、音乐、竞品/商标、夸大宣传、违规广告、下载失败 | `needs_terms_and_route_check` |
| `ecommerce_product_video_from_image_candidate` | Luma API / relay | 可走平台 provider adapter；需 route/config check | 是 | Luma key 仅平台托管；不写入队列或日志 | 1 个 5 秒以内 mock 商品视频，单次预算上限 | 暂不允许；terms + 素材授权 + route 通过后可申请 1 个样例 | 按 Luma terms 标记；输入图与输出视频权属需一并记录 | 输入图审核 + 输出视频审核 | 输入商品图必须 mock/自有/授权；不得上传真实客户素材 | 记录素材授权状态、request id、轮询/下载、成本、输出路径 | 默认 0 次；最多人工批准后 1 次 | 输入图授权不明、商品失真、商标/包装风险、下载/存储条款不清 | `needs_terms_and_route_check` |
| `sales_avatar_pitch_video_candidate` | HeyGen API | 可走平台 provider adapter；不建议测试台直连 | 是 | HeyGen key 仅平台托管；avatar id 不含敏感身份 | 1 个 15-30 秒 stock avatar mock pitch | 暂不允许；terms + avatar/voice rights 通过后可申请 1 个样例 | 按 HeyGen terms 标记；不得承诺可无限制商用或转授权 | 脚本审核 + avatar/voice 审核 + 输出审核 | 只用 stock avatar 或授权 avatar/voice；不得使用真实销售/客户肖像或声音 | 记录脚本摘要、avatar id、request id、成本、输出路径 | 默认 0 次；最多人工批准后 1 次 | 使用真人肖像/声音、外发意图、价格/合同承诺、夸大产品效果 | `needs_terms_avatar_rights_check` |
| `hr_training_avatar_video_candidate` | Synthesia API | 可走平台 provider adapter；不建议测试台直连 | 是 | Synthesia key 仅平台托管；avatar id 走白名单 | 1 个 15-30 秒 stock avatar 培训片段 | 暂不允许；terms + HR 内容审核 + avatar rights 通过后可申请 1 个样例 | 按 Synthesia terms 标记；员工制度内容仍归业务方审核 | HR 制度脚本人工审核 + 输出审核 | 只用 stock avatar；不得上传员工照片/声音；制度素材需公司授权 | 记录制度版本、脚本摘要、avatar id、request id、成本、输出路径 | 默认 0 次；最多人工批准后 1 次 | HR/劳动制度争议、员工隐私、肖像/声音、政策文本未经确认 | `needs_terms_avatar_rights_check` |
| `ecommerce_background_replace_agent_candidate` | fal image edit / provider relay | 可走 fal/provider route；需具体 model id | 是 | fal key 仅平台托管；model id 和版本必须入审计 | 1 张 mock 商品背景替换图 | 暂不允许；model terms + 上传/存储边界通过后可申请 1 张样例 | 按 fal 和具体模型 terms 标记；输入图权属单独记录 | 输入图审核 + 输出图审核 | 商品图必须 mock/自有/授权；不得上传真实客户或未授权商品图 | 记录 model id、素材授权状态、request id、成本、输出路径 | 默认 0 次；最多人工批准后 1 次 | 具体模型条款不清、上传/存储不清、商品/商标授权不明、背景误导 | `needs_model_terms_and_upload_check` |
| `store_menu_poster_generation_candidate` | OpenAI image API / platform image relay | 是，优先走 OpenAI-compatible image relay | 是，或平台统一 provider key | key 只进平台 secrets manager；测试台只拿 route id | 1 张图，固定尺寸，单次预算上限 | 暂不允许；route/config/terms 通过后可申请 1 张 mock 菜单海报 | 按 OpenAI/API terms 标记；价格和菜单信息不由模型背书 | 菜单/价格人工确认 + output review | 食品图片、字体、商标、门店品牌素材必须授权；不得虚假促销 | 记录菜单输入摘要、route id、request id、成本、输出路径 | 默认 0 次；最多人工批准后 1 次 | 价格/菜单不确定、商标/字体风险、食品图片授权、促销承诺 | `route_check_ready` |

## 8. 结论

| 状态 | 数量 |
| --- | ---: |
| `route_check_ready` | 3 |
| `needs_terms_and_route_check` | 2 |
| `needs_terms_avatar_rights_check` | 2 |
| `needs_model_terms_and_upload_check` | 1 |
| 允许立即真实生成 | 0 |
| 进入真实 provider smoke 预备队列 | 8 |
| 可送 draft_l3 | 0 |
| 可送正式 L2 | 0 |

