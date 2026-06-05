# native_seo_audit_skill_candidate

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
- skill_source_class: native_agent_skill
- source_project: local_codex_user_skill
- source_url_or_path: C:/Users/Administrator/.codex/skills/seo-audit/SKILL.md
- upstream_skill_md_status: verified_local_skill_md
- upstream_skill_yaml_or_manifest_status: source_skill_yaml_not_found; registry_candidate_yaml_generated
- preferred_runtime: Codex Skills / DeepAgents local runner
- OpenClaw/Hermes compatibility: adapter_pending，需研究窗口确认目录规范和 manifest 映射

## 业务包、角色、场景
- business_package: 营销与搜索包
- roles: 市场负责人、网站运营
- scenario: 用已有 SKILL.md 在已提供页面信息基础上做 SEO 问题检查

## 来源与许可证 / Trial Mode
- license_or_origin: needs_l1_review_before_smoke
- l1_result: pending
- recommended_trial_mode: mock_only, read_only, external_action_blocked
- deepagents_trial_fit: mock_only

## 中文 smoke 用例
- 输入摘要: 给定网页标题、正文、URL 和描述，做 SEO 审计
- 预期输出字段: seo_findings, priority_fixes, evidence_notes, risk_notes, manual_review_required

## 输入字段
- mock_input
- business_context
- constraints_or_policy
- source_skill_notes

## 输出字段
- seo_findings
- priority_fixes
- evidence_notes
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
- 不抓取网页
- 不改网站

## 人工复核触发
- 低置信
- 客户隐私
- 对外承诺
- 权限边界不清
- 外部排名事实
- 技术改站

## 复用 / 重复关系
与现有候选能力相邻，作为原生 SKILL.md 来源候选复核

## 下一步动作
许可证窗口先做 L1/source verification。L1 放行后才进入 DeepAgents candidate smoke；本卡不代表 L2 通过、draft L3 通过或客户正式可调用。
