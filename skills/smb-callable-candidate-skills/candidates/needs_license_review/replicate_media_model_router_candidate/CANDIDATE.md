# replicate_media_model_router_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- real_generation_target: true

## 来源与能力
- source_project: Replicate API
- source_url_or_path: https://replicate.com/docs
- target_capability: 托管开源图片/视频模型，多模型媒体路由

## 六部门场景
- 创意设计: FLUX/Stable Diffusion 图片生成
- 电商: 商品图变体、upscale
- 运营: 视频/图片实验模型

## 最小真实 smoke
选择 1 个许可证清楚的模型生成 1 张图，记录模型 ID、版本、许可证和输出路径。

## 权限边界
逐模型 L1；不默认所有 Replicate 模型可商用；不上传客户素材。

## 下一步
许可证窗口逐模型复核许可证、费用、数据保留和中转站/Provider key。
