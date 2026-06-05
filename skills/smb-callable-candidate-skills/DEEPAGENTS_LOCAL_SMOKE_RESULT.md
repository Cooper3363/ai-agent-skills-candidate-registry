# DeepAgents 本地试跑结果

生成时间：2026-06-03

## 结论

- DeepAgents 本地试跑底座已接入。
- 本轮使用 OpenAI-compatible 中转站模型通道调用 5.5 模型完成 smoke。
- 稳交付库客户可正式调用数量仍为 13，未新增客户可调用 Skill。
- 本轮发现并加载 17 个 Skill：
  - 13 个稳交付基线 Skill。
  - 4 个候选 draft L3 Skill。
- 本轮共执行 25 个中文 mock smoke 用例，全部通过本地禁用动作检查。

## 接入范围

| 范围 | 数量 | 处理口径 |
| --- | ---: | --- |
| 稳交付库 | 13 | 只验证 DeepAgents 本地可发现、可调用、可输出；不重跑平台正式验收 |
| 候选 draft L3 | 4 | 验证 mock 调用、字段完整、禁止输出、人工复核边界 |

候选 draft L3 包括：

- `visual_prompt_brief_candidate`
- `sales_followup_draft_candidate`
- `complaint_escalation_summary_candidate`
- `product_listing_copy_candidate`

## 权限边界

本地 runner 不暴露任何业务外部动作工具：

- 不发送邮件、短信、微信。
- 不写 CRM、日历、任务、客服系统或电商平台。
- 不抓取网页、不调用 SEO/API、不上传商品。
- 不退款、不赔偿承诺、不改库存。
- 不生成真实图片、视频、音频、OCR 或 PDF 结果。

## 技术产物

- Runner 目录：`X:\codexwork\ai-agent-skills-registry\platform-runners\deepagents-local-runner`
- Runner 报告：`X:\codexwork\ai-agent-skills-registry\platform-runners\deepagents-local-runner\DEEPAGENTS_LOCAL_SMOKE_RESULT.md`
- 本地环境：`uv` + `.venv`
- 模型配置：通过本地 `.env` 读取，`.env` 已被 `.gitignore` 排除，不作为仓库提交内容。

## 后续动作

- 测试台窗口可基于该结果复核“DeepAgents 本地候选调用试跑通过/未通过”。
- 平台验收窗口不得把本地 smoke 通过等同于稳交付扩容。
- 后续新增候选进入 DeepAgents 前，应先标注 `deepagents_trial_fit`：
  - `skill_ready`
  - `mock_only`
  - `dry_run_only`
  - `component_only`
  - `not_suitable`
