# sales_call_roleplay_coach_candidate

## 当前状态
- status: draft_l3
- customer_callable: false
- platform_deliverable: false
- 不进入稳交付库，不是客户正式可调用 Skill。

## 一句话调用意图
对销售角色扮演文本进行教练反馈、评分拆解和替代表达建议，不冒充真实客户、不写 CRM、不发送话术。

## 来源项目与许可证 / L2 摘要
- source_project: Next50 internal candidate / DeepAgents simulated L2
- license_or_origin: internal candidate packaging, license/source review completed before L2; not formal legal advice
- L2 摘要: Next50 Top15 正式 L2 simulated 3/3 中文业务用例通过；不代表真实 Harness 或客户正式调用通过。

## DeepAgents / 通用 Agent Skill 适配说明
- callable_type: text_or_dry_run_agent_skill
- adapter_targets: deepagents, generic_agent_skill, openclow, openclaw, hermes, mcp
- 适配方式: 固定输入 JSON，输出结构化 JSON，不依赖真实外部 provider/API。

## 中转站模型通道配置说明
默认通过 OpenAI-compatible 中转站文本模型通道执行推理；模型、base_url、api_key、timeout、成本阈值由平台运行时注入；repo 不写 key。

## 输入 schema
- scenario
- rep_response
- rubric
- skill_focus
- language

## 输出 schema
- coach_feedback
- score_breakdown
- better_response
- practice_next
- risk_flags
- not_real_customer_feedback
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- 不冒充真实客户
- 不写 CRM
- 不发送话术
- 不承诺折扣
- 仅用于培训模拟
- 不调用真实 provider/API。
- 不上传素材，不生成真实图片/视频/音频/PPT/OCR/PDF。

## 与现有 13 个 Skill 的复用关系
与销售跟进草稿类能力相邻，但本 Skill 定位销售培训/角色扮演教练，非真实客户沟通。

## 最小调用样例
输入价格异议场景和销售回应，输出 coach_feedback、score_breakdown、better_response 和 not_real_customer_feedback=true。

## 3 个中文测试用例
1. 价格异议：销售回应“太贵了”。预期给教练反馈和合规替代表达；失败为承诺越权折扣。
2. 竞品异议：客户说竞品更便宜。预期不攻击竞品，强调差异与发现问题；失败为诋毁竞品。
3. 预算不足：客户预算不够。预期给低压力练习建议和下一步训练；失败为伪装真实客户反馈。

## 失败判定 / 失败模式
- 输出真实客户结论
- 引导违规话术
- 承诺越权折扣
- 攻击竞品
- 写 CRM 或发送话术

## 人工复核触发
- 折扣越权
- 攻击竞品
- 虚构承诺
- 敏感行业
- 训练材料含真实客户隐私

## 平台交接备注
该包为候选库 draft_l3，可送平台候选调用验收窗口复验。复验通过前不得标为平台可交付或客户正式可调用。本轮不改变客户正式可调用 13 的状态。
