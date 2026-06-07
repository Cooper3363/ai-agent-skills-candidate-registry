# open-design menu poster child 补资料

更新日期: 2026-06-05

## 1. 已完成事项

- 已读取 `QUALITY_SOURCE_SPRINT_02_RESULT.md` 与 `LICENSE_REVIEW_QUALITY_SPRINT_02_RESULT.md`。
- 已复核本地只读扫描目录：`X:\codexwork\.tmp\open-design-api-scan-20260604135230\src\open-design-main`。
- 已定位 `quality_sprint02_open_design_menu_poster_child_candidate` 可对应的具体 open-design child skill。
- 未安装依赖，未调用 API，未生成图片/PDF，未写 key，未访问真实账号，未上传素材，未改稳交付库。

## 2. 当前问题

- 已找到可定位 child skill，但它不是“菜单海报”专名 skill，而是更通用的营销海报 child skill。
- `poster-hero` 只有 `SKILL.md`，未发现独立 `skill.yaml` 或 manifest。
- 如果改用 `image-poster` 路线，会进入真实图片生成与本地文件写入边界，不建议本候选当前直接采用。

## 3. 阻塞原因

无权限阻塞。

候选此前阻塞原因已缩小为：

- 需要把泛称 `open-design menu poster child` 落到具体 child skill 路径。
- 需要区分低风险 HTML/prototype 海报 skill 与高风险真实图片生成 skill。
- 需要明确文件写入、导出、Provider、BYOK 边界。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否接受将该候选改名/收窄为：`open_design_poster_hero_menu_poster_candidate`。
- 是否允许重新送许可证 L1，trial mode 限定为 `metadata_only` 或 `mock_only`，暂不进入真实图片生成或文件导出。
- 是否把 `image-poster` 另开为单独媒体候选，走真实媒体 Provider / route 预检链路，而不是混入本候选。

## 5. 建议下一步

- 建议重新送许可证 L1。
- 推荐 L1 名称：`quality_sprint02_open_design_poster_hero_menu_poster_child_candidate`。
- 推荐 trial mode：`metadata_only` 首选，`mock_only` 次选。
- 不建议当前进入 smoke；先由许可证窗口确认 `poster-hero` 子目录和 Apache-2.0 边界后，再送 DeepAgents mock。

## 6. 候选补资料表

| 字段 | 结论 |
| --- | --- |
| candidate_id | `quality_sprint02_open_design_menu_poster_child_candidate` |
| 建议收窄后 ID | `quality_sprint02_open_design_poster_hero_menu_poster_child_candidate` |
| source repo | `nexu-io/open-design` |
| source_url | https://github.com/nexu-io/open-design |
| local_scan_path | `X:\codexwork\.tmp\open-design-api-scan-20260604135230\src\open-design-main` |
| 主 child skill 路径 | `skills/poster-hero/SKILL.md` |
| 主 child skill 名称 | `poster-hero` |
| 中文定位 | 营销海报 / 竖版海报 / 朋友圈分享图 |
| 备选 template 路径 | `design-templates/image-poster/SKILL.md`, `design-templates/magazine-poster/SKILL.md`, `design-templates/html-ppt-zhangzara-bold-poster/SKILL.md` |
| 是否有 SKILL.md | 是，`skills/poster-hero/SKILL.md` 已本地只读验证 |
| 是否有 skill.yaml | 未发现 |
| 是否有 manifest | 未发现独立 manifest；`SKILL.md` frontmatter 可作为元数据来源 |
| LICENSE / 商用条款 | 根目录 `LICENSE` 为 Apache-2.0；README badge 与许可证复核结果均指向 Apache-2.0 |
| 商用可用性 | 仓库主许可证宽松；仍需 L1 确认模板资产、示例内容、上游 `html-anything` 引用边界 |
| 是否依赖外部 API/provider | `poster-hero` 的 `SKILL.md` 本身未要求直接调用外部 API；open-design 整体支持 Model Router / BYOK / MCP，但本候选应限制为不调用 |
| 是否会生成/导出图片 | `poster-hero` 是 prototype/web/html 预览语义；真实执行可能生成 HTML artifact，不应在本轮生成或导出图片 |
| 是否会生成 PDF | `poster-hero` 未显示 PDF 生成要求；open-design 整体有 PDF/export 能力，当前候选必须禁用 |
| 是否会生成设计文件 | 不建议生成；只输出菜单海报 brief / HTML 结构 / design spec |
| 是否会写本地文件 | 完整 open-design 执行可能写 `index.html` 或项目文件；本候选 trial 必须 `write_allowed=false` |
| 是否需要 BYOK | `metadata_only/mock_only` 不需要；若进入真实 open-design/Model Router 执行则可能需要 |
| DeepAgents/通用 Agent Skill 适配 | 可适配为轻量 callable Skill：输入菜单/活动/品牌信息，输出 poster spec / HTML draft plan |
| OpenAI-compatible 中转站适配 | 文本生成阶段可用；当前 trial 不调用真实模型 route 以外工具 |
| 六部门业务包 | 电商/门店、营销 |
| 六部门角色 | 门店店长、门店运营、美工/设计、市场运营 |
| 中小微业务场景 | 奶茶店/烘焙店/餐饮小店菜单海报、价目表、活动公告、朋友圈竖版分享图 |
| 建议 trial mode | `metadata_only` 首选；`mock_only` 可作为下一步；不建议 `dry_run_payload_only`，除非拆到 `image-poster` 媒体生成路线 |
| 是否可重新送许可证 L1 | 是，建议重新送 L1 |
| 是否建议进入 smoke | 当前不直接进入；L1 通过后进入 DeepAgents mock，不做真实导出 |

## 7. 主 child skill 证据摘要

`skills/poster-hero/SKILL.md` frontmatter 显示：

- `name: poster-hero`
- `category: poster`
- `scenario: marketing`
- `aspect_hint: 1080x1920 vertical`
- `od.mode: prototype`
- `od.surface: web`
- `od.preview.type: html`
- `od.preview.entry: index.html`
- `od.design_system.requires: false`
- `upstream: https://github.com/nexu-io/html-anything`

本地目录文件：

| 文件 | 说明 |
| --- | --- |
| `skills/poster-hero/SKILL.md` | skill 元数据和海报生成说明 |
| `skills/poster-hero/example.md` | 示例输入/说明 |
| `skills/poster-hero/example.html` | 示例 HTML 预览 |

## 8. 风险边界

| 风险项 | 结论 | 建议控制 |
| --- | --- | --- |
| 整仓功能过重 | open-design 整体包含 MCP、Model Router、图片/视频/PDF/PPT/export 等能力 | 只按 child skill 复核，不整仓入库 |
| 文件写入 | `poster-hero` 预览入口为 HTML，完整执行可能写项目文件 | L1/Smoke 均设置 `write_allowed=false` |
| 导出/下载 | open-design 整体支持导出 | 禁止 export/download/screenshot |
| 外部 Provider | open-design 整体支持 BYOK 和多 Provider | 本候选只做 metadata/mock，不调用 provider |
| 上游引用 | `poster-hero` 标注 upstream `nexu-io/html-anything` | L1 需确认 upstream 许可/归属说明 |
| 菜单海报适配 | `poster-hero` 是通用营销海报，不是菜单专用 | 平台封装时用菜单/价目表输入模板约束输出 |

## 9. 不建议混用的备选路径

| 路径 | 原因 | 建议 |
| --- | --- | --- |
| `design-templates/image-poster/SKILL.md` | 明确描述单图生成，会通过 media dispatcher 生成 PNG/JPEG 并保存文件 | 另开媒体生成候选，走 provider route / BYOK / 文件写入预检 |
| `design-templates/magazine-poster/SKILL.md` | 更偏杂志页面/版式，不是门店菜单海报主路径 | 可作为后续模板线索 |
| `design-templates/html-ppt-zhangzara-bold-poster/SKILL.md` | 更偏 HTML/PPT 风格海报，可能涉及文件/页面产物 | 后续单独复核 |
| `skills/card-xiaohongshu/SKILL.md` | 社媒卡片，适合小红书/分享图，不是菜单海报主路径 | 可作为营销社媒卡候选 |

## 10. 推荐 L1 复核入口

```yaml
candidate_id: quality_sprint02_open_design_poster_hero_menu_poster_child_candidate
source_project: nexu-io/open-design
source_url: https://github.com/nexu-io/open-design
source_subdir: skills/poster-hero
source_skill_file: skills/poster-hero/SKILL.md
has_skill_md: true
has_skill_yaml: false
has_manifest: false
license_hint: Apache-2.0
business_package: 电商/门店
target_roles:
  - 门店店长
  - 门店运营
  - 美工/设计
  - 市场运营
job_to_be_done: 将菜单、价目表、促销活动和品牌信息整理成竖版海报 brief / HTML 结构草案
trial_mode_recommended: metadata_only
deepagents_fit: skill_adapter_possible
openai_compatible_route_fit: text_generation_only_possible
external_provider_dependency: false_for_metadata_mock
BYOK_required: false_for_metadata_mock
write_allowed: false
export_allowed: false
upload_allowed: false
real_media_generation_allowed: false
customer_callable: false
l1_requeue_recommended: true
```

## 11. 最终结论

- 是否找到可定位 child skill：是。
- 推荐主路径：`nexu-io/open-design/skills/poster-hero/SKILL.md`。
- 是否建议重新送 L1：是。
- 是否建议直接 smoke：否，先重新 L1；通过后只做 DeepAgents mock。
- 缺口清单：需许可证窗口补核 `poster-hero` 子目录许可证继承、`html-anything` upstream 引用边界、是否存在模板资产许可限制、以及是否接受 `SKILL.md frontmatter` 作为 manifest 替代。
