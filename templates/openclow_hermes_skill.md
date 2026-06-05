# SKILL.md Template

---
id: skill-id
name: Skill 中文名称
version: 0.1.0
adapter_targets:
  - openclow
  - openclaw
  - hermes
  - generic_agent
license_status: source_refs_verified
runtime: prompt_plus_tools
permissions:
  - read_input_files
  - call_llm
---

## Intent

当用户需要完成某个明确业务任务时调用本 Skill。

## Inputs

```json
{
  "business_context": "企业背景、行业、产品、客户",
  "task": "用户要完成的具体任务",
  "source_data": "可选，文档、表格、网页或对话文本"
}
```

## Outputs

```json
{
  "result": "可直接给业务人员使用的结果",
  "evidence": "引用、来源、判断依据",
  "risk_notes": "风险、缺失信息、转人工建议"
}
```

## Source Refs

- `repo`: https://github.com/example/example
- `license`: MIT
- `role`: prompt reference / parser / browser action / OCR / RAG

## Execution Steps

1. 校验输入是否足够。
2. 读取必要文档、网页或表格。
3. 调用对应轻量工具或提示词流程。
4. 生成结构化结果。
5. 输出风险提示和下一步动作。

## Tests

- 中文真实业务输入。
- 缺少必要字段时能返回补充项。
- 输出可复现，并保留引用或依据。

