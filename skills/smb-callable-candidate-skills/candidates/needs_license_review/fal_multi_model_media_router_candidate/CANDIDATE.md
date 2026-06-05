# fal_multi_model_media_router_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- real_generation_target: true

## 来源与能力
- source_project: fal.ai Model APIs
- source_url_or_path: https://docs.fal.ai/model-apis
- target_capability: 多模型图片、视频、音频、3D 生成路由
- notes: fal 官方文档说明其 Model APIs 提供大量生产可用模型，覆盖 image/video/audio/multimodal。

## 六部门场景
- 创意设计: 海报、图片编辑、upscale
- 电商: 商品图、图生视频、试穿
- 运营: 短视频、社媒素材

## 最小真实 smoke
先测 1 张图或 1 段短视频，记录具体 fal model id、费用、输出 URL 与落盘路径。

## 权限边界
中转站若不代理 fal，则标 BYOK/provider_key_required；不上传客户素材，不发布。

## 下一步
许可证窗口复核 fal 条款、模型级许可证、数据保留、计费和中转站代理能力。
