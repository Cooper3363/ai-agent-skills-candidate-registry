# 六部门组件池新增项

生成时间：2026-06-03

本文件只记录六部门候选池中通过正式 L2 simulated、但不适合独立封装为客户可调用 Skill 的组件候选。

## 组件池边界

- 不计入 13 个已验收 Skill。
- 不作为独立 L3 Skill。
- 不进入平台调用验收。
- 不客户可调用。
- 后续只能挂靠到明确的正式 Skill、组合包或受控流程中。

## 新增组件

| 组件 ID | 来源候选 | 当前状态 | 使用方式 | 不独立封装原因 |
| --- | --- | --- | --- | --- |
| `sales_meeting_task_brief_candidate` | Google Workspace / `sales_meeting_task_brief_candidate` | 正式 L2 simulated 完成，仅组件 | 承接 mock 会议纪要，生成任务草案和 dry-run payload，供销售跟进流程人工确认 | 真实 OAuth、Workspace 写入、日历/任务创建均未测试，且与 `crm_note_structurer` 部分重叠 |
| `lead_research_brief_candidate` | Tavily / `lead_research_brief_candidate` | 正式 L2 simulated 完成，仅组件 | 承接已提供页面文本，生成潜客简报、业务信号和跟进角度 | 真实 Tavily API、搜索、网页读取、crawl 均未测试；只可处理 mock/已提供文本 |
| `competitor_product_snapshot_candidate` | Apify / `competitor_product_snapshot_candidate` | 正式 L2 simulated 完成，仅组件 | 承接 mock HTML 或已授权快照文本，解析商品名称、价格变化、可售状态和证据片段 | 真实抓取、代理、robots/ToS、动态页面和监控能力均未测试 |

## 使用规则

- `sales_meeting_task_brief_candidate` 只能输出 dry-run payload，不得真实写入 Google Workspace、日历、任务或 CRM。
- `lead_research_brief_candidate` 只能基于输入方提供的页面文本，不得主动搜索、读取网页或调用 Tavily API。
- `competitor_product_snapshot_candidate` 只能基于 mock HTML 或已授权快照文本，不得真实抓取、代理访问或绕过 robots/ToS。
- 如未来要升级为独立 Skill，必须重新走 L1 许可证/依赖复核、L2 真实边界测试、L3 封装和平台验收。

## 当前结论

这 3 个对象只进入六部门组件池，不新增客户可调用 Skill。
