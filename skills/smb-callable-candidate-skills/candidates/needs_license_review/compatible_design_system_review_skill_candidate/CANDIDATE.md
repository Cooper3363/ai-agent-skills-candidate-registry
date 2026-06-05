# compatible_design_system_review_skill_candidate

## 当前状态
- status: needs_license_review
- customer_callable: false
- platform_deliverable: false
- not_l2_passed: true
- formal_l2_status: not_started
- deepagents_smoke_status: not_started
- count_towards_100: false
- count_towards_150_agent_skill_source: true

## Agent Skill 来源证据
- skill_source_class: agent_skill_compatible
- source_project: bergside/awesome-design-skills
- source_url_or_path: https://github.com/bergside/awesome-design-skills
- upstream_skill_md_status: reported_by_source_pending_file_verification
- upstream_skill_yaml_or_manifest_status: unknown; needs_license_window_verification
- preferred_runtime: Codex Skills / DeepAgents local runner
- OpenClaw/Hermes compatibility: adapter_pending，需研究窗口确认目录规范和 manifest 映射

## 业务包、角色、场景
- business_package: 营销视觉包
- roles: 设计协作、市场专员
- scenario: 来自 awesome-design-skills 类 SKILL.md/设计技能仓库线索，用于页面/物料设计规范审阅

## 来源与许可证 / Trial Mode
- license_or_origin: needs_l1_review_before_smoke
- l1_result: pending
- recommended_trial_mode: mock_only, read_only, external_action_blocked
- deepagents_trial_fit: mock_only

## 中文 smoke 用例
- 输入摘要: 给定落地页截图说明和品牌色，输出设计规范检查
- 预期输出字段: design_findings, brand_alignment, accessibility_notes, risk_notes, manual_review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy
- source_skill_notes

## 输出字段
- design_findings
- brand_alignment
- accessibility_notes
- risk_notes
- manual_review_required

## 权限边界
- read_only: true
- external_action_blocked: true
- send_allowed: false
- write_allowed: false
- no_real_account: true
- no_real_business_api: true
- no_customer_delivery: true
- no_real_file_upload: true
- no_real_web_crawl: true

## 禁止动作
- 不发送消息
- 不写 CRM/日历/任务/业务系统
- 不调用真实业务 API
- 不读取真实客户文件
- 不生成图片
- 不改页面
- 不声明素材授权

## 人工复核触发
- 低置信
- 客户隐私
- 对外承诺
- 权限边界不清
- 品牌规范冲突
- 可访问性

## 复用 / 重复关系
外部 Agent Skill 兼容来源，需核验具体子目录和许可证

## 下一步动作
许可证窗口先做 L1/source verification。L1 放行后才进入 DeepAgents candidate smoke；本卡不代表 L2 通过、draft L3 通过或客户正式可调用。
