# google_imagen_real_image_agent_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- real_generation_target: true

## 来源与能力
- source_project: Google Gemini / Imagen
- source_url_or_path: https://ai.google.dev/gemini-api/docs/image-generation
- target_capability: 真实图片生成、图片编辑、高分辨率营销图
- preferred_route: relay first; provider adapter if relay unsupported

## 六部门场景
- 创意设计: 品牌图、活动海报、社媒图
- 电商: 商品主图、店铺活动视觉
- 运营: 节日活动图、内容封面

## 最小真实 smoke
生成 1 张门店活动海报图，输出 sandbox 图片文件和 metadata。

## 权限边界
仅平台自有测试 prompt；不上传客户素材；不发布、不写店铺、不声明素材授权。

## 下一步
许可证窗口复核 Gemini/Imagen route、商用条款、输出格式和中转站兼容性。
