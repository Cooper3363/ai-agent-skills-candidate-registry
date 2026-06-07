# Packaging Quality Source Sprint 01 Preplan

回传时间: 2026-06-05
回传窗口: AI.Skills 封装专员窗口
任务: QUALITY_SOURCE_SPRINT_01 优质适配候选封装预案

## 1. 已完成事项

- 已确认当前候选库路径：
  - `X:\codexwork\ai-agent-skills-candidate-registry`
- 已检查当前 `queues/` 目录，尚未发现：
  - `L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_QUEUE.md`
  - QUALITY_SOURCE_SPRINT_01 正式 L2 结果文件
- 已按新口径准备封装预案。
- 本轮未生成实际 L3 包。
- 本轮未生成任何新的 `SKILL.md` / `skill.yaml`。
- 本轮未改动稳交付库。

## 2. 当前问题

- QUALITY_SOURCE_SPRINT_01 的 L2 Top10 队列和测试结果尚未落盘。
- 不能提前判断哪些候选进入 `draft_l3`。
- 不能把 smoke、role smoke、API 连通性检查或来源适配检查写成正式 L2 通过。
- 图片/视频/数字人真实生成类候选需要更严格的 provider、费用、路由、版权、肖像、商标和素材授权边界。

## 3. 阻塞原因

- 正常流程门禁：等待测试台输出 `L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_QUEUE.md` 和正式 L2 测试结果。
- 无权限阻塞。
- 无文件写入阻塞。
- 当前不应抢跑封装。

## 4. 需要 AI.Skills 指挥中心决策的问题

- QUALITY_SOURCE_SPRINT_01 的候选是否按来源类型分为四类队列：
  - Agent Skill / SKILL.md 来源
  - MCP/API 来源
  - 图片/视频/数字人真实生成来源
  - 角色库来源
- 图片/视频/数字人候选是否必须先完成 provider/API、费用、BYOK、中转路由、版权/肖像/商标/素材授权专项复核，再进入 L2。
- 角色库候选是否统一只进入 role component 或 role candidate，不作为独立客户可调用 L3。
- MCP/API 候选是否必须先完成 dry-run payload 与 OAuth/BYOK 权限复核，再进入 L2。

## 5. 建议下一步

- 等测试台落盘 `L2_OFFICIAL_TOP10_FROM_QUALITY_SPRINT_01_QUEUE.md` 与测试结果后，封装窗口只处理 L2 通过项。
- L2 通过但属于组件或角色库的对象，进入 component/role candidate，不生成独立客户可调用 Skill。
- L2 通过且适合独立 callable 的对象，生成候选库 `draft_l3` 包。
- 所有实际包仍需平台候选调用验收窗口复验；复验前不得进入稳交付库。

## 6. 总体封装门禁

| 阶段 | 可做 | 禁止 |
| --- | --- | --- |
| 来源入库 | 生成候选卡、保留来源证据、记录许可证状态 | 写成 L2 通过或客户可调用 |
| L1 / source review | 记录许可证、商用风险、依赖风险 | 替代正式法务意见 |
| smoke / role smoke | 验证基本适配和输出稳定性 | 写成正式 L2 通过 |
| 正式 L2 | 通过中文业务用例后进入 draft L3 队列 | 组件项封独立客户可调用 Skill |
| draft L3 | 生成 `SKILL.md` / `skill.yaml` / schema / tests / 风险边界 | 直接进入稳交付库 |
| 平台验收 | 验收调用、日志、权限、失败模式 | 未验收即客户正式调用 |

## 7. Agent Skill / SKILL.md 来源封装预案

### 候选卡要求

`CANDIDATE.md` 必须包含：

- candidate_id
- source_type: `agent_skill` 或 `native_skill_md`
- skill_source_class
- upstream_project
- upstream_skill_md_path 或 source_url_or_path
- upstream_skill_md_status
- 是否存在上游 manifest / yaml
- 原始 SKILL.md 摘要
- 适配 DeepAgents / 通用 Agent Skill 底座的方式
- OpenAI-compatible 中转站模型通道需求
- trial_mode_recommended
- 权限边界
- 禁止动作
- 中文 smoke 用例
- 人工复核触发
- `customer_callable=false`
- `platform_deliverable=false`
- `not_l2_passed=true`

### candidate.yaml 映射要求

必须保留上游来源证据，不得冒充自研：

```yaml
candidate_id: example_agent_skill_candidate
source_type: agent_skill
skill_source_class: upstream_skill_md
source_url_or_path: "..."
upstream_skill_md_status: verified_or_pending
source_attribution_required: true
customer_callable: false
platform_deliverable: false
not_l2_passed: true
trial_mode_recommended:
  - mock_only
  - read_only
  - external_action_blocked
```

### draft L3 要求

只有正式 L2 通过且适合独立 callable 时，才生成：

- `SKILL.md`
- `skill.yaml`
- 输入/输出 schema
- 权限边界
- 3 个中文测试用例
- 最小调用样例
- 失败模式
- 人工复核触发
- 来源项目与许可证
- 上游 SKILL.md 证据和适配说明

## 8. MCP/API 来源封装预案

### 候选卡要求

`CANDIDATE.md` 必须写明：

- provider/API 名称
- MCP server / API endpoint 来源
- BYOK 是否必需
- OAuth 是否必需
- read 权限范围
- write 权限范围
- 是否支持 dry-run
- dry-run payload 样例
- 外部 action 是否默认阻断
- 日志、成本、速率限制、失败重试风险
- 禁止动作
- 人工复核触发

### 必填边界

```yaml
permissions:
  read_only: true
  write_allowed: false
  send_allowed: false
  external_action_blocked: true
  byok_required: true_or_false
  oauth_required: true_or_false
dry_run:
  supported: true_or_false
  payload_required: true
```

### 禁止动作示例

- 不直接发送邮件、短信、微信、站内信
- 不写 CRM、工单、订单、库存、财务、采购或广告平台
- 不创建真实任务、会议、投放、付款或退款
- 不绕过 OAuth/BYOK 权限边界
- 不把 API 连通性检查写成 L2 通过

## 9. 图片/视频/数字人真实生成来源封装预案

### 候选卡与 draft L3 共同必填

必须写清：

- provider/API
- 是否 BYOK
- 是否走 OpenAI-compatible 中转站模型路由
- route 名称或模型路由策略
- 生成费用与计费单位
- 预算上限和失败成本处理
- 是否真实生成图片/视频/数字人
- 输入素材来源要求
- 版权风险
- 肖像权风险
- 商标风险
- 字体/音乐/配音/素材授权风险
- 人工审核触发
- 真实生成验收要求

### 明确禁止

- 不得把 key 写入 repo
- 不得声明素材天然授权
- 不得默认用户上传素材可商用
- 不得默认生成结果可商用
- 不得绕过肖像/商标/版权人工复核
- 未经验收不得真实发布、投放或交付客户

### 真实生成验收要求

进入平台验收前至少需要记录：

- provider 调用是否 dry-run 或真实生成
- 实际模型/route
- 生成成本估算
- 输出文件格式和尺寸
- 是否带水印
- 是否含第三方商标、人物肖像、可识别地点或受保护素材
- 人工审核结论
- 失败时是否有安全降级输出

## 10. 角色库来源封装预案

### 处理原则

- 只封 role component 或 role candidate。
- 不直接封独立客户可调用 L3。
- 不把 role smoke 写成正式 L2。
- 不把角色库源级候选当成单个 Skill。

### 候选卡要求

必须包含：

- source_type: `agent_role_library`
- skill_source_class: `agent_role_compatible`
- role_library_source
- upstream_role_file
- department_mapping
- role_smoke_status
- formal_l2_status: `not_applicable_yet` 或 `not_l2_passed`
- 权限边界
- 禁止 install/convert 脚本
- 人工复核触发

### 后续封装方向

- role component：供组合包选择角色提示词、职责边界、人工复核策略。
- role candidate：用于平台内部角色库试运行。
- combination pack：多个 role component 与 callable Skill 编排。

## 11. draft L3 最小包结构

正式 L2 通过后，每个独立 callable draft L3 至少落盘：

```text
skills/smb-candidate-draft-l3-skills/skills/<candidate_id>/SKILL.md
skills/smb-candidate-draft-l3-skills/skills/<candidate_id>/skill.yaml
```

`SKILL.md` 必须包含：

- 当前状态：`draft_l3`
- `customer_callable=false`
- `platform_deliverable=false`
- 一句话调用意图
- 来源项目与许可证 / trial mode
- 输入 schema
- 输出 schema
- 权限边界
- 最小调用样例
- 3 个中文测试用例
- 失败模式
- 人工复核触发
- 平台交接备注

`skill.yaml` 必须包含：

- id
- status
- customer_callable
- platform_deliverable
- source_projects
- license
- trial_mode
- l1_summary
- l2_status
- adapter_targets
- input_schema
- output_schema
- permissions
- forbidden_actions
- human_review_triggers
- failure_modes
- evaluation.test_cases
- platform_handoff_notes

## 12. PACKAGING 结果文件模板

等 L2 队列/结果落盘后，实际封装结果文件建议命名：

```text
PACKAGING_QUALITY_SPRINT_01_RESULT.md
```

建议包含：

- 已完成事项
- 当前问题
- 阻塞原因
- 需要 AI.Skills 指挥中心决策的问题
- 建议下一步
- 封装数量
- draft_l3 数量
- role/component 数量
- 退回测试台的问题
- 退回许可证的问题
- 图片/视频/数字人专项风险清单
- 平台候选调用验收对象清单

## 13. 当前结论

本轮仅完成 QUALITY_SOURCE_SPRINT_01 封装预案。

未生成实际 L3 包，未生成 `SKILL.md` / `skill.yaml`，未修改稳交付库，未把任何候选写成 L2 通过。

