# 首批 20 个许可证核验通过候选条目

核验日期：2026-06-02。数据来自 GitHub 官方仓库元数据。当前状态统一为 `L1 license_metadata_verified`，尚未冒充为真实部署跑通。

## 总览

| ID | 项目 | 类别 | 许可证 | Stars | 最近更新 UTC | 中小微适配方向 | 状态 |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| AGS-001 | [CrewAI](https://github.com/crewAIInc/crewAI) | 销售线索/CRM | MIT | 52666 | 2026-06-02 | 多角色销售/运营协作 Agent | L1 |
| AGS-002 | [LangGraph](https://github.com/langchain-ai/langgraph) | 知识库/RAG | MIT | 33650 | 2026-06-02 | 状态机式客服/业务流程 Agent | L1 |
| AGS-003 | [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 办公文档 | MIT | 28032 | 2026-05-29 | 企业应用内嵌 AI 编排 | L1 |
| AGS-004 | [LlamaIndex](https://github.com/run-llama/llama_index) | 知识库/RAG | MIT | 49855 | 2026-05-29 | 文档知识库、检索问答 | L1 |
| AGS-005 | [Haystack](https://github.com/deepset-ai/haystack) | 客服问答 | Apache-2.0 | 25438 | 2026-06-02 | RAG、客服检索、问答流水线 | L1 |
| AGS-006 | [LangChain](https://github.com/langchain-ai/langchain) | 电商运营 | MIT | 138321 | 2026-06-02 | 工具调用、业务自动化原型 | L1 |
| AGS-007 | [Langflow](https://github.com/langflow-ai/langflow) | 办公文档 | MIT | 149087 | 2026-06-02 | 可视化 Agent/Workflow 搭建 | L1 |
| AGS-008 | [smolagents](https://github.com/huggingface/smolagents) | 财税行政 | Apache-2.0 | 27666 | 2026-06-02 | 轻量代码执行型 Agent | L1 |
| AGS-009 | [CAMEL](https://github.com/camel-ai/camel) | 销售线索/CRM | Apache-2.0 | 17106 | 2026-06-02 | 多智能体协作与模拟 | L1 |
| AGS-010 | [OpenAI Swarm](https://github.com/openai/swarm) | 客服问答 | MIT | 21562 | 2026-04-15 | 轻量多 Agent 交接模式 | L1 |
| AGS-011 | [Rasa](https://github.com/RasaHQ/rasa) | 客服问答 | Apache-2.0 | 21190 | 2026-05-22 | 对话机器人、客服流程 | L1 |
| AGS-012 | [browser-use](https://github.com/browser-use/browser-use) | 电商运营 | MIT | 96704 | 2026-06-01 | 网页操作自动化 Agent | L1 |
| AGS-013 | [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | 知识库/RAG | MIT | 60941 | 2026-06-02 | 企业知识库与私有聊天入口 | L1 |
| AGS-014 | [llmware](https://github.com/llmware-ai/llmware) | 知识库/RAG | Apache-2.0 | 14848 | 2026-05-17 | 企业文档 RAG 与小模型流程 | L1 |
| AGS-015 | [mem0](https://github.com/mem0ai/mem0) | 客服问答 | Apache-2.0 | 57394 | 2026-06-01 | Agent 长期记忆与客户上下文 | L1 |
| AGS-016 | [Composio](https://github.com/ComposioHQ/composio) | 销售线索/CRM | MIT | 28584 | 2026-06-02 | 工具集成、认证和动作执行 | L1 |
| AGS-017 | [DSPy](https://github.com/stanfordnlp/dspy) | 营销内容 | MIT | 34789 | 2026-06-01 | Prompt/模块优化与质量提升 | L1 |
| AGS-018 | [Instructor](https://github.com/567-labs/instructor) | 办公文档 | MIT | 13078 | 2026-05-24 | 结构化输出、表单和报告生成 | L1 |
| AGS-019 | [GraphRAG](https://github.com/microsoft/graphrag) | 知识库/RAG | MIT | 33395 | 2026-05-28 | 复杂知识图谱检索问答 | L1 |
| AGS-020 | [MarkItDown](https://github.com/microsoft/markitdown) | 办公文档 | MIT | 140557 | 2026-05-26 | Office/PDF 转 Markdown 知识入库 | L1 |

## 入库卡片与运行测试

### AGS-001 CrewAI

- 推荐场景：销售线索调研、营销活动拆解、竞品分析。
- 待跑通测试：输入 10 条潜在线索生成分层跟进建议；输入竞品网站生成卖点对比；输入活动目标生成角色分工与执行清单。

### AGS-002 LangGraph

- 推荐场景：客服流程、审批流程、带状态的多轮业务 Agent。
- 待跑通测试：客户退款咨询多轮处理；销售报价审批状态流转；异常输入时回退到人工节点。

### AGS-003 Semantic Kernel

- 推荐场景：把 AI 能力嵌入现有业务系统。
- 待跑通测试：将客户资料生成跟进邮件；调用函数生成报价摘要；缺少字段时返回补全清单。

### AGS-004 LlamaIndex

- 推荐场景：企业资料问答、产品手册问答、售后知识库。
- 待跑通测试：导入 3 篇产品文档回答售后问题；输出引用依据；无法命中资料时拒绝编造。

### AGS-005 Haystack

- 推荐场景：客服知识检索、RAG 流水线、文档问答。
- 待跑通测试：中文 FAQ 检索问答；多个文档冲突时标注来源；低置信度问题转人工。

### AGS-006 LangChain

- 推荐场景：业务工具调用、订单/库存/客服原型。
- 待跑通测试：根据订单状态生成回复；调用模拟库存工具；多工具失败时返回可解释错误。

### AGS-007 Langflow

- 推荐场景：低代码搭建内部 AI 流程。
- 待跑通测试：搭建客服问答流程；搭建营销文案流程；导出可复用流程配置。

### AGS-008 smolagents

- 推荐场景：轻量数据整理、财税行政表格处理。
- 待跑通测试：读取 CSV 生成经营摘要；计算费用分类；对高风险代码执行请求拒绝。

### AGS-009 CAMEL

- 推荐场景：多角色经营决策模拟。
- 待跑通测试：销售和运营共同制定活动方案；客服和质检复盘投诉；多 Agent 输出合并为单一清单。

### AGS-010 OpenAI Swarm

- 推荐场景：轻量 Agent 交接样板。
- 待跑通测试：客服接待转售后专家；售前转报价助手；交接时保留上下文摘要。

### AGS-011 Rasa

- 推荐场景：客服机器人、规则+模型混合对话。
- 待跑通测试：订单咨询意图识别；退换货流程槽位收集；低置信度转人工。

### AGS-012 browser-use

- 推荐场景：网页后台自动化、电商运营巡检。
- 待跑通测试：登录演示后台读取订单；抓取商品页标题和价格；遇到验证码或登录失败时安全停止。

### AGS-013 AnythingLLM

- 推荐场景：内部知识库、门店 SOP 问答。
- 待跑通测试：上传门店 SOP 后问答；对敏感信息输出提醒；多工作区隔离验证。

### AGS-014 llmware

- 推荐场景：企业文档 RAG、小模型本地化流程。
- 待跑通测试：合同条款问答；发票字段摘要；无依据答案拒绝。

### AGS-015 mem0

- 推荐场景：客户偏好记忆、长期服务上下文。
- 待跑通测试：记录客户偏好；下一轮自动引用偏好；用户要求删除记忆时清除。

### AGS-016 Composio

- 推荐场景：Agent 连接 SaaS 工具和业务系统。
- 待跑通测试：模拟 CRM 新建线索；生成邮件草稿；权限不足时返回授权提示。

### AGS-017 DSPy

- 推荐场景：稳定营销文案、分类器和结构化任务。
- 待跑通测试：优化活动标题生成；分类客户反馈；比较优化前后输出一致性。

### AGS-018 Instructor

- 推荐场景：表单抽取、结构化报告、销售摘要。
- 待跑通测试：客户邮件抽取 JSON；会议纪要生成任务列表；字段缺失时返回空值和理由。

### AGS-019 GraphRAG

- 推荐场景：复杂企业知识库、产品关系问答。
- 待跑通测试：多文档生成实体关系；回答跨文档问题；输出依据链路。

### AGS-020 MarkItDown

- 推荐场景：Office/PDF 知识入库预处理。
- 待跑通测试：Word 转 Markdown；PDF 转 Markdown；表格和标题结构保留检查。

