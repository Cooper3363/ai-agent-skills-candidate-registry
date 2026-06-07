# REAL_MEDIA_ROUTE_CONFIG_CHECK_RESULT

回传对象：AI.Skills 指挥中心  
执行日期：2026-06-05  
输入文件：
- `REAL_MEDIA_PROVIDER_SMOKE_PRECHECK.md`
- `queues/REAL_MEDIA_PROVIDER_SMOKE_QUEUE.md`

执行范围：仅 3 个 `route_check_ready` OpenAI image relay 项。  
执行方式：route/config check only；未调用真实 image endpoint，未写 key，未上传素材，未生成图片，未消耗费用。

## 1. 已完成事项

- 已读取真实媒体 provider smoke precheck 与队列。
- 已确认本轮只处理 3 个 `route_check_ready` 项：
  - `marketing_real_poster_banner_agent_candidate`
  - `ecommerce_product_main_image_agent_candidate`
  - `store_menu_poster_generation_candidate`
- 已检查三项是否可表达为平台 image relay 调用配置。
- 已检查输入 schema、输出路径 schema、成本上限字段、审计字段、内容安全字段、mock prompt、mock asset policy、`manual_review_required` 是否齐全。
- 已生成 `queues/REAL_MEDIA_MINIMAL_SAMPLE_APPROVAL_QUEUE.md`，仅作为“待指挥中心批准真实最小样例”队列。

## 2. 当前问题

- 本轮未批准真实出图，因此不能写成真实 provider 通过。
- 后续若要真实最小样例，仍需指挥中心单独批准，并由平台提供 route、key 托管、费用上限、输出 sandbox 和审计日志边界。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 真实生成被流程边界阻止：本轮只允许 route/config check。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否批准 `REAL_MEDIA_MINIMAL_SAMPLE_APPROVAL_QUEUE.md` 中 3 项进入真实最小样例。
- 若批准，是否统一限制为每项最多 1 张 mock 图片、固定尺寸、固定预算上限、输出仅进 runner sandbox。

## 5. 建议下一步

- 指挥中心确认是否进入真实最小样例。
- 未获批准前，测试台不得调用 image endpoint、不得写 key、不得上传素材、不得生成图片。

## 6. 数量表

| route_config_check_status | 数量 |
| --- | ---: |
| passed | 3 |
| needs_fix | 0 |
| blocked | 0 |

## 7. 统一检查口径

| 检查项 | 要求 | 结果 |
| --- | --- | --- |
| 平台 image relay 调用配置 | 必须只表达 route/config/payload，不直连 provider | passed |
| 输入 schema | 必须包含业务目标、文案/商品/菜单信息、尺寸、风格、授权声明 | passed |
| 输出路径 schema | 必须只声明 sandbox output path，不发布、不写稳交付库 | passed |
| 成本上限字段 | 必须包含 `cost_limit` 或等价字段 | passed |
| 审计字段 | 必须包含 candidate_id、route_id、request_id、prompt 摘要、成本、审核结果 | passed |
| 内容安全字段 | 必须包含 prompt policy check 与 output review 字段 | passed |
| mock prompt | 必须提供可测试 mock prompt，不含真实客户素材 | passed |
| mock asset policy | 必须声明只使用 mock/自有/授权素材 | passed |
| 人工复核 | 必须包含 `manual_review_required` 与触发条件 | passed |
| 禁止项 | 不真实生成、不上传素材、不写 key、不发布、不客户调用 | passed |

## 8. 明细表

| candidate_id | provider_route | 输入 schema | 输出路径 schema | 成本字段 | 审计字段 | 内容安全字段 | mock prompt | mock asset policy | manual_review_required | 禁止项检查 | route_config_check_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `marketing_real_poster_banner_agent_candidate` | `image_relay.openai.mock_route` | `candidate_id`, `campaign_goal`, `target_audience`, `copy`, `visual_style`, `size`, `brand_constraints`, `asset_policy`, `cost_limit`, `content_safety_policy` | `output_mode=route_config_only`, `sandbox_output_path`, `no_publish=true`, `no_customer_callable=true` | `cost_limit={max_images:0, max_usd:0, requires_approval_for_real_sample:true}` | `audit={route_id, request_id_placeholder, prompt_summary, policy_check, reviewer, timestamp}` | `prompt_policy_check`, `trademark_check`, `claim_check`, `output_review_required` | “社区生鲜店草莓 19.9 元周末促销海报，清爽红白配色，避免全网最低等绝对化表述。” | 仅 mock 文案；不使用真实 logo、人物、门店照片；字体/商标需人工确认 | true；价格、商标、人物、医疗/金融承诺、绝对化用语触发 | 未出图、未上传、未写 key、未发布 | passed |
| `ecommerce_product_main_image_agent_candidate` | `image_relay.openai.mock_route` | `candidate_id`, `product_info`, `platform_rules`, `visual_style`, `image_ref_policy`, `asset_policy`, `cost_limit`, `content_safety_policy` | `output_mode=route_config_only`, `sandbox_output_path`, `no_shopify_write=true`, `no_customer_callable=true` | `cost_limit={max_images:0, max_usd:0, requires_approval_for_real_sample:true}` | `audit={route_id, request_id_placeholder, product_input_summary, policy_check, reviewer, timestamp}` | `product_truth_check`, `trademark_check`, `platform_compliance_check`, `output_review_required` | “316 不锈钢保温杯白底电商主图，突出杯身和容量标签，但不得虚构材质、容量或认证。” | 仅 mock 商品信息；不上传真实商品图；logo/包装/商标需授权 | true；商品参数不确定、商标包装、虚假卖点、平台规则触发 | 未出图、未上传、未写 key、未写平台 | passed |
| `store_menu_poster_generation_candidate` | `image_relay.openai.mock_route` | `candidate_id`, `menu_items`, `prices`, `promotion_rules`, `brand_style`, `size`, `font_policy`, `asset_policy`, `cost_limit`, `content_safety_policy` | `output_mode=route_config_only`, `sandbox_output_path`, `no_publish=true`, `no_customer_callable=true` | `cost_limit={max_images:0, max_usd:0, requires_approval_for_real_sample:true}` | `audit={route_id, request_id_placeholder, menu_summary, price_review_status, policy_check, reviewer, timestamp}` | `price_accuracy_check`, `food_claim_check`, `font_trademark_check`, `output_review_required` | “奶茶店夏季菜单海报，包含三款饮品与价格，清爽明亮风格，需保留价格人工复核。” | 仅 mock 菜单和价格；不使用真实门店 logo、食品照片、商标字体 | true；价格/菜单不确定、食品功效、字体商标、促销承诺触发 | 未出图、未上传、未写 key、未发布 | passed |

## 9. 最小真实样例准入建议

三项均可进入“待指挥中心批准真实最小样例”队列，但不得直接真实生成。若后续批准，建议统一限制：

- 每项最多 1 张 mock 图片。
- 仅使用 mock/自有/明确授权素材，不上传真实客户素材。
- key 只由平台 secrets manager / image relay 持有，测试台不接触明文 key。
- 输出仅进入 runner sandbox，不发布、不写客户空间、不写稳交付库。
- 默认 0 次自动重试；如需重试，必须人工批准且最多 1 次。
- 必须记录 route_id、request_id、成本、prompt 摘要、审核结果和 sandbox 输出路径。

## 10. 权限边界确认

本轮未调用真实 image endpoint，未写 key，未上传素材，未生成图片，未消耗费用，未发布，未客户调用，未写业务系统，未写稳交付库。
