# 许可证窗口复核队列

## 本轮任务

优先复核研究窗口新增的高频、低权限、可 mock、可 dry-run 候选。

## 复核输出

| 字段 | 要求 |
| --- | --- |
| `candidate_id` | 候选 ID |
| `source_project` | 来源项目 |
| `license` | LICENSE 和 SPDX |
| `commercial_use_notes` | 商用限制或不确定点 |
| `maintenance_status` | 维护状态 |
| `dependency_risks` | API、模型、云服务、OAuth、数据上传风险 |
| `trial_mode` | `mock_only`、`dry_run_only`、`BYOK_required`、`read_only`、`external_action_blocked` |
| `l1_result` | 可送 L2、需补资料、暂缓、只作线索 |

## 默认规则

- 许可证不清可以留在候选库，但不得进入正式 L2。
- 需要外部真实动作的候选，只允许 dry-run 结论。
- ClawHub 或聚合站链接必须定位到真实上游项目再复核。
- 不把平台可调用性建立在无法核验的作者授权上。
