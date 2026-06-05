# comfyui_self_host_media_engine_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- real_generation_target: true

## 来源与能力
- source_project: ComfyUI
- source_url_or_path: https://github.com/comfyanonymous/ComfyUI
- target_capability: 自托管图片/视频工作流、节点式生成和编辑

## 六部门场景
- 创意设计: 可控图片工作流
- 电商: 商品图批量变体
- 运营: 长期低成本素材流水线

## 最小真实 smoke
不直接接客户；先在本地/专用 GPU sandbox 跑 1 个最小 workflow 生成测试图。

## 权限边界
需要基础设施审批；逐模型许可证复核；不读取客户文件、不开放任意节点。

## 下一步
许可证窗口复核开源许可、模型许可、依赖安装和安全隔离；平台决定是否建设自托管路线。
