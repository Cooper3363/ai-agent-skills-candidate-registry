# 六部门 5 个候选正式 L2 simulated 结果

回传来源：测试台窗口  
回传时间：2026-06-03  
状态：正式 L2 simulated 完成，不代表真实 Harness 或生产运行通过

## 总体结论

本轮测试台已对 5 个 L1 放行候选完成正式 L2 simulated 中文业务用例测试。每个候选 3 个中文业务用例，共 15 个用例。

本轮全程 mock/dry-run：

- 未安装依赖
- 未访问外网
- 未读取真实客户文件
- 未调用真实 API
- 未做真实 OAuth
- 未写 CRM、日历、邮件、任务或网页系统
- 未生成真实图片/视频
- 未做真实抓取

| 结果分类 | 候选 |
| --- | --- |
| L2 通过可封装 | `visual_prompt_brief_candidate`, `sales_followup_draft_candidate` |
| 仅组件 | `sales_meeting_task_brief_candidate`, `lead_research_brief_candidate`, `competitor_product_snapshot_candidate` |
| 新增客户可调用 Skill | 0 |

## 总表

| 候选 | 3 个中文用例是否完成 | 输出结构稳定性 | 中文可用性 | 权限边界 | 人工复核触发 | L2 结论 | 建议下一步 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `visual_prompt_brief_candidate` | 完成 | 高 | 高 | 只输出视觉提示词 brief，不生成图片，不调 Eachlabs API | 肖像/商标/版权不明，医疗/金融/教育宣传，品牌规范冲突 | L2 通过可封装 | 送封装；定位为视觉 brief 生成，不接图片生成 |
| `sales_followup_draft_candidate` | 完成 | 高 | 高 | 只输出跟进草稿，`send_allowed=false`，不发邮件/短信，不写 CRM | 折扣、合同、投诉、个人信息、客户拒绝触达 | L2 通过可封装 | 送封装；与 `crm_note_structurer` 组合使用 |
| `sales_meeting_task_brief_candidate` | 完成 | 高 | 高 | 只输出会议任务草案和 dry-run payload，不 OAuth，不写 Workspace | 合同条款、价格承诺、客户隐私、行动项归属不确定 | 仅组件 | 入组件池；不作为 Workspace 写入 Skill |
| `lead_research_brief_candidate` | 完成 | 中高 | 高 | 只用 mock 页面文本，不调 Tavily API，不搜索，不 crawl | 页面过期、低置信、对外沟通前、来源不足 | 仅组件 | 入组件池；真实搜索/网页读取另审 |
| `competitor_product_snapshot_candidate` | 完成 | 中高 | 中高 | 只用 mock HTML/快照文本，不真实抓取，不代理，不绕 robots/ToS | ToS/robots 不清、页面过期、价格证据不足、动态内容 | 仅组件 | 入组件池；真实抓取/监控另审 |

## 用例摘要

### 1. `visual_prompt_brief_candidate`

建议 schema：`prompt_brief`, `asset_requirements`, `style_constraints`, `negative_prompts`, `channel_specs`, `risk_notes`, `manual_review_required`。

| 用例 | 输入摘要 | 预期输出 | 失败点 | 风险提示 |
| --- | --- | --- | --- | --- |
| 生鲜海报视觉 brief | 社区生鲜店、草莓 19.9 元、品牌色绿色、朋友圈、禁用“全网最低” | 主视觉提示词、商品呈现要求、字体/色彩建议、negative_prompts、risk_notes | 承诺直接生成图片或虚构“已授权素材” | 价格、库存、版权需人工确认 |
| 瑜伽馆小红书封面 brief | 肩颈放松体验课、温柔风、上班族女性、禁用医疗疗效 | 避免“治疗颈椎病”，包含画面主体、风格、构图、文字层级 | 医疗化承诺或过度身体羞辱 | 健康宣传人工复核 |
| 电商主图 brief | 保温杯参数、白底图、平台要求、品牌规范 | 标注产品角度、留白、禁止元素，符合平台规范 | 忽略平台规范或商标边界 | 平台规则/商标审核 |

结论：L2 通过可封装。与现有 13 个 Skill 不重复；相邻于 `marketing_copy_pack`，但输出视觉 brief 而非营销正文。

### 2. `sales_followup_draft_candidate`

建议 schema：`message_draft`, `subject_options`, `talking_points`, `personalization_basis`, `risk_notes`, `send_allowed=false`, `missing_info`, `manual_review_required`。

| 用例 | 输入摘要 | 预期输出 | 失败点 | 风险提示 |
| --- | --- | --- | --- | --- |
| 试用后微信跟进 | 客户试用 3 天、使用排课提醒、目标预约演示 | 简短微信草稿、个性化依据、下一步建议，`send_allowed=false` | 虚构客户行为或语气压迫 | 销售发送前人工确认 |
| 报价后价格异议邮件 | 客户说价格贵、最多 9 折但优先延长服务期 | 强调价值，不直接越权打折，风险提示折扣权限 | 承诺超权限折扣 | 价格/合同复核 |
| 沉睡线索唤醒短信 | 30 天未回复、新功能上线、客户未明确授权短信 | 低打扰草稿、停止触达提示、`send_allowed=false` | 生成骚扰式短信或假定授权 | 触达合规 |

结论：L2 通过可封装。与 `crm_note_structurer` / `marketing_copy_pack` 部分重叠，但可作为“销售跟进草稿”独立轻量 Skill。

### 3. `sales_meeting_task_brief_candidate`

建议 schema：`summary`, `action_items`, `owners`, `due_dates`, `dry_run_payload`, `permission_notes`, `risk_flags`, `manual_review_required`。

| 用例 | 输入摘要 | 预期输出 | 失败点 | 风险提示 |
| --- | --- | --- | --- | --- |
| 销售会议纪要转任务 | mock 会议记录“下周二演示、销售A准备报价” | action_items 明确 owner/due_date，dry_run_payload 不执行 | 真实写日历/任务或缺 owner | 销售确认后再写入 |
| 多人会议行动项归属 | 客户老板提价格、财务提付款周期、销售承诺回去确认 | 行动项归属销售，不把客户话当任务 | 归属错 | 合同/付款条款人工复核 |
| 敏感承诺记录 | 客户问“上线失败能否退款” | `risk_flags=[refund_or_contract_sensitive]`，只生成“内部确认”任务 | 生成承诺性任务或外发 payload | 退款/合同需人工 |

结论：仅组件。与 `crm_note_structurer` 部分重叠，增量是 dry-run task payload；不作为 Google Workspace 写入 Skill。

### 4. `lead_research_brief_candidate`

建议 schema：`company_summary`, `business_signals`, `likely_needs`, `follow_up_angle`, `source_notes`, `confidence`, `risk_notes`, `manual_review_required`。

| 用例 | 输入摘要 | 预期输出 | 失败点 | 风险提示 |
| --- | --- | --- | --- | --- |
| mock 公司主页文本 | 教培机构官网介绍课程、校区、学员管理难点 | 公司摘要、业务信号、跟进角度 | 把 mock 文本当尽调事实 | source_notes 必须写清 |
| mock 产品页文本 | 五金批发商网站写库存、批发、赊账 | likely_needs 包含库存/应收账款，confidence 中等 | 过度推断采购意图 | 对外沟通前人工确认 |
| mock 新闻页/公告文本 | 公司新开门店公告 | sales_trigger 标“扩张/门店管理可能需求”，risk_notes 标页面时效 | 旧公告当新信号 | 页面过期 |

结论：仅组件。真实 Tavily/search/crawl 未测；当前只可作为“已提供页面文本”简报组件。

### 5. `competitor_product_snapshot_candidate`

建议 schema：`product_name`, `old_snapshot`, `new_snapshot`, `price_change`, `availability`, `evidence_snippets`, `comparison_notes`, `risk_notes`, `manual_review_required`。

| 用例 | 输入摘要 | 预期输出 | 失败点 | 风险提示 |
| --- | --- | --- | --- | --- |
| 标准价格下降 | mock_old_html 价格 199，mock_new_html 价格 159 | `price_change=-40`，evidence_snippets 引用两段价格 | 无证据片段或算错差额 | 价格需人工确认 |
| 划线价/会员价混合 | 原价 299、划线价 199、会员价 179 | 标注 `price_type_unclear`，`manual_review_required=true` | 把划线价当现价 | 误判竞价策略 |
| 缺货/下架页面 | new_snapshot 含“已下架/暂时无货” | `availability=out_of_stock`，标注价格不可比 | 仍输出降价结论 | 页面状态变更 |

结论：仅组件。真实 Apify/抓取/代理/robots/ToS 均未测，不能作为完整监控 Skill。

## 指挥中心判定

- `visual_prompt_brief_candidate`、`sales_followup_draft_candidate`：送封装队列，状态应为 `draft_l3`，不得标为可交付平台。
- `sales_meeting_task_brief_candidate`、`lead_research_brief_candidate`、`competitor_product_snapshot_candidate`：仅进入六部门组件池，不独立 L3，不平台调用验收。
- 六部门候选池新增客户可调用 Skill 仍为 0。
