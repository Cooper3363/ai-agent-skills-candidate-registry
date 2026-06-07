# OPEN_DESIGN_POSTER_HERO_LICENSE_REVIEW_RESULT

回传日期：2026-06-05

## 1. 已完成事项

- 已读取研究窗口补资料文件：`OPEN_DESIGN_MENU_POSTER_CHILD_FOLLOWUP.md`。
- 已只读核验本地 open-design 扫描副本中的根目录 `LICENSE`、`README.md` 与 `skills/poster-hero/SKILL.md`。
- 已确认收窄后候选 ID：`quality_sprint02_open_design_poster_hero_menu_poster_child_candidate`。
- 已生成 smoke 队列：`queues/OPEN_DESIGN_POSTER_HERO_SMOKE_QUEUE.md`。
- 本轮未安装依赖、未调用 API/provider、未生成图片/PDF/HTML 文件、未写 key、未访问真实账号、未上传素材、未修改稳交付库。

## 2. 当前问题

- `poster-hero` 是通用营销竖版海报 / 朋友圈分享图 child skill，不是菜单海报专用 skill；菜单/价目表场景需要由平台输入模板约束。
- `poster-hero` 只有 `SKILL.md`，未发现独立 `skill.yaml` 或 manifest；L1 可接受 `SKILL.md` frontmatter 作为临时元数据来源，但正式封装前仍需补 manifest 或候选卡字段。
- `SKILL.md` 标注 upstream 为 `nexu-io/html-anything`；本轮只记录上游引用，不引入 upstream 执行、不安装、不调用。
- open-design 整仓包含图片、视频、PDF、PPT、export、Model Router、MCP 等更重能力；本候选只能按 `skills/poster-hero` 子目录收窄复核，不得整仓放行。

## 3. 阻塞原因

- 无权限阻塞。
- 无 `blocked` 项。
- 仍需补资料项不影响 L1 mock smoke，但影响正式 L2 / 封装：upstream `html-anything` 许可证/归属、模板资产清单、正式 manifest。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否接受候选正式改名为 `quality_sprint02_open_design_poster_hero_menu_poster_child_candidate`。
- 是否接受 `SKILL.md` frontmatter 在 L1 阶段临时代替 manifest；正式封装前再补 manifest / candidate schema。
- 是否将 `design-templates/image-poster` 或真实图片生成路线另开媒体 provider 候选；本候选不混入真实图片生成。

## 5. 建议下一步

- 测试台可读取 `queues/OPEN_DESIGN_POSTER_HERO_SMOKE_QUEUE.md`，仅执行 metadata/mock smoke。
- smoke 输入使用 mock 菜单、价目表、活动和品牌文字；输出仅为 poster brief / HTML structure plan / design spec。
- 强制设置 `write_allowed=false`、`export_allowed=false`、`upload_allowed=false`、`real_media_generation_allowed=false`。
- 正式 L2 前补齐：`html-anything` upstream 许可证/归属、poster-hero 模板资产清单、正式 manifest、是否允许生成本地 HTML artifact 的平台策略。

## 6. L1 结论

| 字段 | 结论 |
| --- | --- |
| candidate_id | `quality_sprint02_open_design_poster_hero_menu_poster_child_candidate` |
| source_project | `nexu-io/open-design` |
| source_url | https://github.com/nexu-io/open-design |
| source_subdir | `skills/poster-hero` |
| source_skill_file | `skills/poster-hero/SKILL.md` |
| license_status | 根目录 `LICENSE` 为 Apache-2.0；未发现 `poster-hero` 子目录独立许可证冲突，L1 可按 Apache-2.0 继承处理 |
| commercial_use_notes | Apache-2.0 产品筛选阶段可接受；但 bundled templates / upstream / example assets 仍需正式封装前补清单 |
| upstream_boundary | `SKILL.md` 标注 upstream `nexu-io/html-anything`；本轮仅作为来源引用，不安装、不执行、不调用 |
| manifest_status | 无独立 manifest；L1 可用 `SKILL.md` frontmatter 作 metadata 替代，正式封装前需补 manifest |
| dependency_api_model_risk | open-design 整仓能力重；本候选限定为 metadata/mock，不启用 Model Router、MCP、provider、export、PDF/PPT/image/video |
| asset_license_risk | `poster-hero` 子目录本地仅见 `SKILL.md`、`example.md`、`example.html`；未见独立素材许可证，但正式封装前需补模板资产清单 |
| trial_mode | `metadata_only`, `mock_only`, `read_only`, `external_action_blocked` |
| l1_result | `can_mock_smoke` |
| smoke_allowed | yes |
| formal_l2_allowed | no |
| customer_callable | no |

## 7. 禁止动作

- 不安装 open-design 或 html-anything 依赖。
- 不调用 Model Router、MCP、OpenAI、fal、Figma、browser automation 或任何 provider/API。
- 不生成真实图片、PDF、HTML 文件、PPT、截图或下载物。
- 不写 `index.html`、artifact、project 文件或本地导出文件。
- 不上传菜单、商品图、品牌素材、二维码、商标或客户文件。
- 不混用 `design-templates/image-poster` 真实图片生成路线。
- 不把本候选声明为客户正式可调用 Skill。

## 8. 复核表

| candidate_id | LICENSE / 条款 | 商用限制 | 维护状态或来源可信度 | 依赖/API/provider/模型风险 | BYOK / route 要求 | trial_mode | 是否可送 smoke | 仍需补资料 | l1_result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `quality_sprint02_open_design_poster_hero_menu_poster_child_candidate` | 根目录 Apache-2.0；`poster-hero` 未见独立许可证冲突 | 可做产品筛选阶段 metadata/mock；正式封装前需补 upstream 与模板资产清单 | GitHub 项目本地扫描可定位；`skills/poster-hero/SKILL.md` 已验证 | 整仓有重型 provider/export 能力；本候选限定为 HTML/prototype metadata，不执行、不写文件 | metadata/mock 阶段不需要 BYOK；如未来真实执行再单独复核 route/key | `metadata_only`, `mock_only`, `read_only`, `external_action_blocked` | yes | `html-anything` 许可证/归属、模板资产清单、正式 manifest、HTML artifact 写入策略 | `can_mock_smoke` |

