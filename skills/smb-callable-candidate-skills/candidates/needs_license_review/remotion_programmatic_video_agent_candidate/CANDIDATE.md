# remotion_programmatic_video_agent_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- real_generation_target: true

## 来源与能力
- source_project: Remotion
- source_url_or_path: https://www.remotion.dev/docs/
- target_capability: 程序化视频渲染、批量模板视频、本地 mp4 输出

## 六部门场景
- 运营: 数据日报/活动复盘视频
- 销售: 个性化跟进视频
- 管理: 月报/周报短视频

## 最小真实 smoke
用 mock 数据渲染 1 个 10 秒竖版运营日报 mp4，输出 sandbox 文件和 render log。

## 权限边界
本地 sandbox 渲染；不读取客户文件；不上传、不发布；依赖需锁定。

## 下一步
许可证窗口复核 Remotion 商用许可、依赖、渲染环境和 sandbox 输出目录。
