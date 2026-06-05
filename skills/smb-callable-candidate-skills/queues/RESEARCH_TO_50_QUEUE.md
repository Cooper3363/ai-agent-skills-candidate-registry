# 研究窗口任务：第一阶段候选扩到 50

## 输入

- 当前候选库实际候选卡：7 个。
- 第一阶段目标：新增 43 个可试跑候选，使候选库达到 50。
- 业务包优先：客服、销售、营销、电商/门店、经营报表、行政/财务/HR。

## 任务

输出 70 个高频候选线索，并从中推荐 43 个进入可试跑候选队列。

每个候选必须包含：

- `candidate_id`
- 业务包
- 适配角色
- 中小微企业高频场景
- 来源类型：OpenClaw / Hermes / MCP / GitHub / ClawHub / internal_template / existing_skill_combo
- 来源链接或复用关系
- 是否被 13 个稳交付 Skill 覆盖
- 建议状态：`mock_callable` / `dry_run_callable` / `component_only` / `needs_license_review` / `market_lead`
- `deepagents_trial_fit`：`skill_ready` / `mock_only` / `dry_run_only` / `component_only` / `not_suitable`
- 建议 smoke 中文用例一句话

## 优先场景

- 客服：质检、投诉摘要、FAQ 扩展、知识库整理、退款/账号安全分流。
- 销售：跟进草稿、会议行动项、线索简报、报价异议、CRM 记录。
- 营销：文案、活动 brief、视觉 prompt、合规检查、社媒/广告变体。
- 电商/门店：商品文案、订单库存异常、竞品快照、评价聚类、退换货摘要。
- 经营报表：日报周报、指标异常、漏斗摘要、数据质量、老板摘要。
- 行政/财务/HR：票据、简历脱敏、合同分区、采购比价、会议纪要、SOP。

## 输出文件

- `RESEARCH_TO_50_RESULT.md`
- 70 个候选线索总表
- 43 个推荐进入许可证/trial mode 复核的候选表

## 禁止

- 不直接送 L2。
- 不直接封装。
- 不把纯线索计入 100。
