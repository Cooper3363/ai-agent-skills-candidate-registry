# 平台验收窗口任务：To100 Draft L3 候选调用复核

## 输入

请读取：

- `DRAFT_L3_PACKAGING_FROM_TO100_RESULT.md`
- `L2_OFFICIAL_TOP15_FROM_TO100_RESULT.md`
- `queues/DRAFT_L3_PACKAGING_QUEUE_FROM_TO100.md`
- `PLATFORM_ACCEPTANCE_TO_100_RESULT.md`
- `skills/smb-candidate-draft-l3-skills/skills/<candidate_id>/SKILL.md`
- `skills/smb-candidate-draft-l3-skills/skills/<candidate_id>/skill.yaml`

## 复核对象

1. `support_ticket_autotag_router_candidate`
2. `support_refund_evidence_request_candidate`
3. `support_policy_conflict_detector_candidate`
4. `support_vip_customer_handoff_candidate`
5. `pricing_terms_risk_summary_candidate`
6. `demo_script_builder_candidate`
7. `lost_deal_followup_draft_candidate`
8. `customer_reference_brief_candidate`
9. `promo_bundle_copy_matrix_candidate`
10. `influencer_brief_draft_candidate`
11. `product_attribute_gap_checker_candidate`
12. `supplier_delivery_risk_brief_candidate`
13. `gross_margin_bridge_summary_candidate`

## 任务

对 To100 13 个 draft L3 包做候选调用复核。本轮只判断是否可以继续作为候选库内部/受控试跑的 L3 草案，不做客户正式调用验收，不迁入稳交付库。

## 必查项

- 每个包是否存在 `SKILL.md` 与 `skill.yaml`。
- `status=draft_l3` 是否存在。
- `customer_callable=false` 是否存在。
- `platform_deliverable=false` 是否存在。
- 是否有稳定 Skill ID、intent、输入 schema、输出 schema。
- 是否有权限边界、禁止动作、人工复核触发。
- 是否有 3 个中文测试用例。
- 是否有最小调用样例。
- 是否写明 L1/L2 摘要。
- 是否写明本轮不新增客户正式可调用 Skill，稳交付库仍为 13。
- 3 个 dry-run 包是否保留：
  - `external_action_blocked=true`
  - `send_allowed=false`
  - `write_allowed=false`

## dry-run 重点对象

- `support_refund_evidence_request_candidate`
- `lost_deal_followup_draft_candidate`
- `influencer_brief_draft_candidate`

## 不验收对象

以下 2 个仍为组件池对象，不进入本轮 draft L3 复核：

- `support_ticket_batch_summary_candidate`
- `brand_forbidden_words_checker_candidate`

## 结论枚举

- `candidate_trial_accepted`
- `candidate_trial_needs_fix`
- `blocked`

## 输出

请落盘：

- `PLATFORM_ACCEPTANCE_DRAFT_L3_FROM_TO100_RESULT.md`

输出需要包含：

- 13 个 draft L3 复核数量。
- accepted / needs_fix / blocked 数量。
- dry-run 三断言检查结果。
- 是否发现 `customer_callable=true` 或 `platform_deliverable=true`。
- 缺字段清单，如有。
- 可继续候选调用试跑对象。
- 明确说明稳交付库客户正式可调用数量仍为 13。

## 禁止

- 不把候选调用复核通过写成客户正式可调用。
- 不迁入稳交付库。
- 不修改 13 个稳交付 Skill 原包。
