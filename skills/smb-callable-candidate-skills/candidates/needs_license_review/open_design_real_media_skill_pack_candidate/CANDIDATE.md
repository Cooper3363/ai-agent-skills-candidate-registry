# open_design_real_media_skill_pack_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- real_generation_target: true

## 来源与能力
- source_project: nexu-io/open-design
- source_url_or_path: https://github.com/nexu-io/open-design
- local_scan: `X:\codexwork\.tmp\open-design-api-scan-20260604135230`
- target_capability: open-design 中 imagegen、fal、venice、sora、remotion、card、poster、figma、pptx 等媒体 skill 源级包

## 六部门场景
- 创意设计: 图片生成、海报、设计评审
- 电商: 商品图、社媒卡、图生视频
- 运营: 短视频、PPT、活动素材

## 最小真实 smoke
不整仓执行。逐子 skill 复核后，选 1 个图片生成和 1 个视频生成子 skill 做 sandbox smoke。

## 权限边界
不安装整仓依赖；不执行 Figma/PPT/export/upload；不调用未批准 provider。

## 下一步
研究窗口拆子 skill Top20，许可证窗口逐项 L1/API 依赖复核，再决定哪些进入真实生成 smoke。
