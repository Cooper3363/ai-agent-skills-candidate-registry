# 研究窗口候选收集队列

## 本轮任务

围绕六大中小微业务包继续收集 OpenClaw、Hermes、MCP、GitHub 等来源候选。不要按来源堆列表，要按业务包输出。

## 每个候选必须包含

| 字段 | 要求 |
| --- | --- |
| `candidate_id` | 保留下划线命名 |
| `business_package` | 客服、销售、营销、电商/门店、经营报表、行政/财务/HR |
| `target_role` | 中小微企业里的实际使用人 |
| `job_to_be_done` | 具体工作内容 |
| `source_type` | OpenClaw、Hermes、MCP、GitHub、文档来源等 |
| `source_url` | 可复核链接 |
| `covered_by_stable_13` | 是否已被 13 个稳交付 Skill 覆盖 |
| `suggested_status` | `market_lead` 或 `needs_license_review` |
| `risk_hint` | 权限、外部动作、合规或依赖风险 |

## 优先收集

- 高频、低权限、可 mock、可 dry-run。
- 能产出结构化输入输出。
- 能服务中小微企业老板、运营、客服、销售、财务、HR。

## 暂不优先

- 通用开发工具。
- 大型 WebUI 产品。
- 研究 demo。
- 必须真实 OAuth、发送、写入、抓取或生成商业素材的项目。
- 没有明确中小微业务场景的通用 Agent。
