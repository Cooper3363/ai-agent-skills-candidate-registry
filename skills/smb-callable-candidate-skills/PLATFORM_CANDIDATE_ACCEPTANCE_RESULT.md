# 平台候选调用验收结果

回传时间：2026-06-03

## 验收边界

本次只做“候选调用 / 受控试点验收”，不是稳交付验收。

结论不会改变当前客户可调用清单。稳交付库客户可调用数量仍为 13。

## 验收对象

| Candidate ID | 当前状态 | 候选调用验收结论 | 是否进入稳交付 |
| --- | --- | --- | --- |
| `visual_prompt_brief_candidate` | `draft_l3` | 候选调用可试点 | 否 |
| `sales_followup_draft_candidate` | `draft_l3` | 候选调用可试点 | 否 |

## visual_prompt_brief_candidate

验收结论：候选调用可试点。

已确认：

- 状态为 `draft_l3`。
- `customer_callable=false`。
- `platform_deliverable=false`。
- 有明确 adapter target：`openclow`、`openclaw`、`hermes`、`mcp`、`generic_agent`。
- 输入输出字段清楚。
- 中文最小调用样例可用于候选试点。
- 不生成图片。
- 不调用 Eachlabs API。
- 不输出图片 URL。
- 不声明素材授权、商用可用或平台审核通过。

试点限制：

- 只能作为视觉 prompt brief 生成候选。
- 涉及肖像、商标、版权不明、医疗/金融/教育宣传、价格库存不清、品牌规范冲突时必须人工复核。
- 后续 smoke 需确认不会输出 `generated_image`、`image_url`、`asset_license_claim`、`commercial_use_guarantee`。

## sales_followup_draft_candidate

验收结论：候选调用可试点。

已确认：

- 状态为 `draft_l3`。
- `customer_callable=false`。
- `platform_deliverable=false`。
- 有明确 adapter target：`openclow`、`openclaw`、`hermes`、`mcp`、`generic_agent`。
- 输入输出字段清楚。
- 中文最小调用样例可用于候选试点。
- `send_allowed=false` 固定输出。
- 不发送邮件、短信、微信。
- 不写 CRM。
- 不触发任何外部动作。

试点限制：

- 只能生成销售跟进草稿。
- 个性化依据必须来自输入，不得虚构客户事实。
- 涉及折扣、合同、投诉、个人信息、拒绝触达、触达授权不明、报价争议、付款承诺或低置信度客户事实时必须人工复核。
- 后续 smoke 需确认不会输出 `send_instruction`、`crm_write_payload` 或外部动作 payload。

## 组件项处理

以下 3 个仍为组件，不进入平台调用验收，不作为独立 L3，不客户调用：

- `sales_meeting_task_brief_candidate`
- `lead_research_brief_candidate`
- `competitor_product_snapshot_candidate`

## 总体结论

两个 draft L3 候选可以进入候选调用库做内部 mock / dry-run / 受控试点。

它们仍禁止进入稳交付库，禁止标记为“可交付平台”，客户正式可调用新增仍为 0。
