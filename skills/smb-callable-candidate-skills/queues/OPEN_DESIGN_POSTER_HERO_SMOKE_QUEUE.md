# OPEN_DESIGN_POSTER_HERO_SMOKE_QUEUE

生成日期：2026-06-05

来源：`../OPEN_DESIGN_POSTER_HERO_LICENSE_REVIEW_RESULT.md`

本队列只包含收窄后的 open-design `poster-hero` child skill L1 放行项。只允许 metadata/mock smoke，不允许真实执行 open-design。

## Hard Boundaries

- 不安装依赖。
- 不调用 API/provider。
- 不写 key。
- 不访问真实账号。
- 不上传素材。
- 不生成图片、PDF、HTML 文件、PPT、截图或下载物。
- 不写本地 artifact 或项目文件。
- 不启用 Model Router、MCP、browser automation、export/download。
- 不混用 `design-templates/image-poster` 真实图片生成路线。
- 不送正式 L2，不封装，不客户调用。

## Summary

| l1_result | 数量 |
| --- | ---: |
| `can_mock_smoke` | 1 |
| smoke queue total | 1 |

## Queue

| # | candidate_id | source_project | source_subdir | smoke_type | trial_mode | write_allowed | export_allowed | upload_allowed | real_media_generation_allowed | smoke_focus |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `quality_sprint02_open_design_poster_hero_menu_poster_child_candidate` | `nexu-io/open-design` | `skills/poster-hero` | metadata/mock | `metadata_only`, `mock_only`, `read_only`, `external_action_blocked` | false | false | false | false | mock menu/activity/brand text -> poster brief + HTML structure plan + design spec |

## Required Mock Inputs

- mock menu or price list text only.
- mock campaign or discount text only.
- mock brand tone and color preferences only.
- no real logo, QR code, product photo, store photo, customer file, private brand asset, or upload.

## Expected Mock Outputs

- poster brief.
- section structure.
- text hierarchy.
- layout notes.
- HTML structure plan as text only.
- no `index.html` file, no image/PDF export, no screenshot.

