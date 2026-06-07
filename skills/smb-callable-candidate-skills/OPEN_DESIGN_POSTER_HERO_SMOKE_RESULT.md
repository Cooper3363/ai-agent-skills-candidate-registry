# OPEN_DESIGN_POSTER_HERO_SMOKE_RESULT

回传日期：2026-06-05

本轮性质：open-design `poster-hero` child skill 单项 metadata/mock smoke。  
候选：`quality_sprint02_open_design_poster_hero_menu_poster_child_candidate`。  
重要边界：本轮不进入正式 L2，不封装，不生成 HTML/图片/PDF/PPT/截图，不写 artifact，不启用 Model Router/MCP/browser automation/export/download。

## 1. 已完成事项

- 已读取 `OPEN_DESIGN_POSTER_HERO_LICENSE_REVIEW_RESULT.md` 与 `queues/OPEN_DESIGN_POSTER_HERO_SMOKE_QUEUE.md`。
- 已对 1 个候选完成 metadata/mock smoke。
- 已使用 mock 菜单、价目表、活动、品牌文字进行输入设计。
- 已验证输出仅为 poster brief、section structure、text hierarchy、layout notes、HTML structure plan as text。
- 已验证硬断言：`write_allowed=false`、`export_allowed=false`、`upload_allowed=false`、`real_media_generation_allowed=false`、`external_action_blocked=true`。

## 2. 当前问题

- `poster-hero` 是通用竖版海报/分享图 child skill，不是菜单海报专用 skill；菜单/价目表场景需由平台输入模板约束。
- 当前仅定位到 `skills/poster-hero/SKILL.md`，正式封装前仍需补正式 manifest/candidate schema。
- `SKILL.md` 标注 upstream `nexu-io/html-anything`，本轮只记录引用，不安装、不执行、不调用。
- 本轮不生成本地 HTML artifact，因此不能证明真实渲染质量、截图质量或导出质量。

## 3. 阻塞原因

- 无权限阻塞。
- 无工具阻塞。
- 无外部网络、真实账号、真实 API/provider、真实客户文件、上传、导出、浏览器自动化、文件生成或写 artifact 动作。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否接受该候选继续保留为 `poster-hero` metadata/mock 候选，而不是 image-poster/真实出图路线。
- 是否要求研究/许可证窗口补齐 `html-anything` upstream 许可证归属、模板资产清单与正式 manifest。
- 是否允许后续单独开正式 L2；若允许，是否仍限制为 text-only structure plan，不生成 artifact。

## 5. 建议下一步

- 本候选可保留在候选库继续试跑，但仅作为 metadata/mock poster planning 能力。
- 不建议进入 draft L3，直到补齐正式 manifest、模板资产清单和 HTML artifact 写入策略。
- 真实图片/海报生成路线应继续走独立媒体 provider smoke 链路，不能与本候选混用。

## 6. Smoke 结论

| candidate_id | smoke_status | mock 输入摘要 | 预期输出字段 | 输出结构稳定性 | 中文可用性 | 权限边界 | 人工复核触发 | 建议下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `quality_sprint02_open_design_poster_hero_menu_poster_child_candidate` | passed | mock 菜单/价目表/活动/品牌文字 | `poster_brief`, `section_structure`, `text_hierarchy`, `layout_notes`, `html_structure_plan_text`, `write_allowed=false`, `export_allowed=false`, `upload_allowed=false`, `real_media_generation_allowed=false`, `external_action_blocked=true` | 稳定 | 可用，适合中文菜单/活动信息结构化 | 不写文件、不导出、不上传、不生成媒体 | 价格/优惠信息不清、品牌素材授权、二维码/商标、食品/医疗等合规风险 | 保留为候选库 metadata/mock 能力，补资料后再定是否正式 L2 |

## 7. Mock 用例摘要

| 用例 | 输入摘要 | 预期输出 | 失败判定 |
| --- | --- | --- | --- |
| 门店菜单海报 | mock 菜单：咖啡、甜品、套餐价，品牌语气“温暖简洁” | poster brief、菜单分区、主标题/副标题/价格层级、HTML structure plan text | 生成 HTML 文件、生成图片/PDF、写 artifact、混用 image-poster 路线 |
| 活动价目表 | mock 活动：周末第二杯半价、会员储值优惠、门店地址 | 活动层级、价格/限制条件突出、人工复核提示 | 承诺未给出的优惠、遗漏限制条件、导出文件 |
| 新品推荐海报 | mock 新品：两款季节饮品、推荐语、品牌色偏好 | 新品区块、卖点层级、layout notes | 使用真实品牌素材、上传图片、调用 provider |

## 8. 硬断言验证

| 字段 | 结果 |
| --- | --- |
| `write_allowed=false` | 通过 |
| `export_allowed=false` | 通过 |
| `upload_allowed=false` | 通过 |
| `real_media_generation_allowed=false` | 通过 |
| `external_action_blocked=true` | 通过 |
| `index_html_generated=false` | 通过 |
| `image_pdf_ppt_screenshot_generated=false` | 通过 |
| `browser_automation_used=false` | 通过 |
| `model_router_mcp_provider_used=false` | 通过 |

## 9. 权限边界确认

- 未安装依赖。
- 未调用 API/provider。
- 未写 key，未读取或打印 key。
- 未访问真实账号。
- 未读取客户文件。
- 未上传菜单、商品图、品牌素材、二维码、商标或客户文件。
- 未生成 `index.html`、图片、PDF、PPT、截图或下载物。
- 未写本地 artifact 或项目文件。
- 未启用 Model Router、MCP、browser automation、export/download。
- 未混用 `design-templates/image-poster` 真实图片生成路线。
- 未改稳交付库；客户正式可调用 Skill 仍为 13。
