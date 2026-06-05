# openai_gpt_image_real_generation_agent_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- real_generation_target: true

## 来源与能力
- source_project: OpenAI API
- source_url_or_path: https://platform.openai.com/docs/guides/image-generation
- skill_source_class: real_generation_provider_agent
- target_capability: 真实图片生成、图片编辑、多轮图片修改
- preferred_route: OpenAI-compatible relay first

## 六部门场景
- 创意设计: 商品海报、活动主视觉、品牌图
- 电商: 商品主图、详情页配图
- 运营: 社媒配图、活动图

## 最小真实 smoke
- 生成 1 张茶饮店新品海报图，比例 4:5。
- 输出图片文件和 metadata JSON。
- metadata 记录 provider、model、job id、尺寸、费用/用量、输出路径。

## 权限边界
- route check 前不生成真实图片。
- route check 通过后仅允许 sandbox 输出。
- 不上传、不发布、不写素材库、不声明版权/商标/肖像授权。

## 下一步
许可证窗口复核中转站是否支持 GPT Image endpoint、组织验证要求、内容政策、计费和输出格式。L1 放行后测试台做 1 张图真实生成 smoke。
