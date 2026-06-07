# REAL_MEDIA_MINIMAL_SAMPLE_APPROVAL_QUEUE

来源：`REAL_MEDIA_ROUTE_CONFIG_CHECK_RESULT.md`  
生成日期：2026-06-05  
状态：pending_command_center_approval  
说明：本队列仅表示 route/config check 已通过，可等待指挥中心审批真实最小样例。不得直接真实生成。

## 1. 统一边界

- 当前不允许真实出图。
- 不调用真实 image endpoint。
- 不写 key，不让测试台持有明文 key。
- 不上传客户素材。
- 不发布、不外发、不客户调用。
- 不写业务系统，不写稳交付库。
- 若后续批准真实最小样例，输出只能进入 runner sandbox。

## 2. 待审批队列

| priority | candidate_id | provider_route | approved_current_stage | requested_next_stage | max_real_sample_if_approved | required_before_real_sample | manual_review_trigger | status |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `marketing_real_poster_banner_agent_candidate` | OpenAI-compatible image relay | route/config check passed | minimal_real_image_sample | 1 张 mock 活动海报 | 平台 key 托管、固定预算、内容安全、版权/商标/素材授权、输出 sandbox | 品牌/商标、人物、价格促销、版权或政策命中 | pending_command_center_approval |
| 2 | `ecommerce_product_main_image_agent_candidate` | OpenAI-compatible image relay | route/config check passed | minimal_real_image_sample | 1 张 mock 商品主图 | 平台 key 托管、固定预算、商品真实性、平台规则、商标/包装/素材授权、输出 sandbox | 商品失真、商标/包装风险、虚假卖点、规格不确定 | pending_command_center_approval |
| 3 | `store_menu_poster_generation_candidate` | OpenAI-compatible image relay | route/config check passed | minimal_real_image_sample | 1 张 mock 菜单海报 | 平台 key 托管、固定预算、菜单/价格人工确认、字体/商标/食品图授权、输出 sandbox | 价格/菜单不确定、食品功效、字体商标、促销承诺 | pending_command_center_approval |

## 3. 审批后仍需保留

若指挥中心后续批准真实最小样例，仍必须保留：

- `no_publish=true`
- `no_customer_callable=true`
- `sandbox_output_only=true`
- `manual_review_required=true`
- `max_images=1`
- `max_auto_retries=0`
- `key_visible_to_testbench=false`

## 4. 当前结论

3 个候选均已通过 route/config check，但真实生成仍未批准。等待 AI.Skills 指挥中心下一步决策。
