# REAL_MEDIA_MINIMAL_SAMPLE_SMOKE_RESULT

回传对象：AI.Skills 指挥中心  
执行日期：2026-06-05  
审批文件：`REAL_MEDIA_MINIMAL_SAMPLE_APPROVAL_DECISION.md`  
执行命令：`scripts/run_image_relay_sample.ps1 -Execute -WriteReport`

## 1. 已完成事项

- 已读取 `REAL_MEDIA_MINIMAL_SAMPLE_APPROVAL_DECISION.md`。
- 已确认受控 image relay runner 入口已补齐：
  - `platform-runners/deepagents-local-runner/deepagents_local_runner/run_image_relay_sample.py`
  - `platform-runners/deepagents-local-runner/scripts/run_image_relay_sample.ps1`
- 已确认本轮批准范围仍仅限 3 个 OpenAI-compatible image relay 候选，每项最多 1 张 mock 图片，总计最多 3 张。
- 已安全检查当前进程环境变量名称；未发现本轮执行所需 route/key/approval 变量名。
- 已尝试通过 PowerShell fallback 执行受控 runner：`-Execute -WriteReport`。
- 已确认安全闸未满足，未触发真实 provider/API 调用。

## 2. 当前问题

- runner 已存在，不再是 runner 缺失。
- 当前 route/env 未就绪：测试台进程中未发现以下必需环境变量名：
  - `REAL_MEDIA_SMOKE_APPROVED`
  - `IMAGE_RELAY_BASE_URL` 或 `OPENAI_BASE_URL`
  - `IMAGE_RELAY_API_KEY` 或 `OPENAI_API_KEY`
- PowerShell runner 尝试写回报告时遇到本地文件写入拒绝，因此测试台使用受控落盘方式覆盖本结果文件。

## 3. 阻塞原因

本轮阻塞类型：`route_env_not_ready`。

硬限制要求：

- `REAL_MEDIA_SMOKE_APPROVED=1`
- 必须由环境提供 image relay base URL。
- 必须由环境提供 image relay API key。
- `key_visible_to_testbench=false`
- 不得把 key 写入 repo。
- 不得打印 key。
- 不得绕过平台 route 直连 provider。

当前测试台没有可用的 route/env，因此不能执行真实 image endpoint 调用。3 个候选均保持 `blocked`。

## 4. 需要 AI.Skills 指挥中心决策的问题

- 是否由平台/运行器窗口把所需环境变量注入测试台进程后重跑。
- 是否改由平台侧执行真实最小样例，并将 sandbox 输出路径和审计摘要回传测试台。
- 是否修复 PowerShell runner 对结果文件写入被拒绝的问题，或改为写入中间 sandbox report 再由测试台汇总。

## 5. 建议下一步

- 注入 `REAL_MEDIA_SMOKE_APPROVED=1`。
- 注入 `IMAGE_RELAY_BASE_URL` 或 `OPENAI_BASE_URL`。
- 注入 `IMAGE_RELAY_API_KEY` 或 `OPENAI_API_KEY`，但不允许测试台打印或写入 key。
- 重跑同一命令：`powershell.exe -NoProfile -ExecutionPolicy Bypass -File ...\run_image_relay_sample.ps1 -Execute -WriteReport`。

## 6. 数量表

| result_status | 数量 |
| --- | ---: |
| passed | 0 |
| needs_fix | 0 |
| blocked | 3 |
| failed | 0 |

## 7. 逐项结果

| candidate_id | provider_route | request summary | usage/cost note | output path | content safety status | manual review status | result_status | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `marketing_real_poster_banner_agent_candidate` | OpenAI-compatible image relay | Fictional stationery shop weekend sale poster, no real brand/trademark/people/assets | No request sent; no cost incurred | N/A | Preflight only; no prompt submitted | Not reached; manual review required if rerun | blocked | route/env not ready: approval/base URL/API key not visible to controlled runner |
| `ecommerce_product_main_image_agent_candidate` | OpenAI-compatible image relay | Fictional stainless steel thermos hero image with mock attributes only | No request sent; no cost incurred | N/A | Preflight only; no prompt submitted | Not reached; manual review required if rerun | blocked | route/env not ready: approval/base URL/API key not visible to controlled runner |
| `store_menu_poster_generation_candidate` | OpenAI-compatible image relay | Fictional noodle shop menu poster with mock menu items and mock prices | No request sent; no cost incurred | N/A | Preflight only; no prompt submitted | Not reached; manual review required if rerun | blocked | route/env not ready: approval/base URL/API key not visible to controlled runner |

## 8. 未执行动作确认

- 未调用真实 image endpoint。
- 未调用 provider/API。
- 未写 key。
- 未打印 key。
- 未读取 `.env` 或密钥文件。
- 未上传客户、员工、候选人、品牌、商标、版权或第三方素材。
- 未生成图片。
- 未消耗费用。
- 未发布、未外发、未客户调用。
- 未写业务系统。
- 未写稳交付库。

## 9. 最终结论

本轮真实最小样例 smoke 未能执行，3 项均为 `blocked`。阻塞原因已从上一轮的 `runtime_route_unavailable` 更新为 `route_env_not_ready`：runner 入口已补齐，但审批变量、route base URL 和 API key 未注入当前测试台运行环境。即使后续重跑并 passed，也只代表真实最小样例 smoke 通过，不代表客户正式可调用，不代表稳交付扩容。
