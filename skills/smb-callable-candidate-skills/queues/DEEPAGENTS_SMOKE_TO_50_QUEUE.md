# 测试台任务：第一阶段 DeepAgents Candidate Smoke

## 输入

等待许可证窗口输出 `LICENSE_REVIEW_TO_50_RESULT.md`。

## 任务

只对 L1/trial mode 放行项做 DeepAgents candidate smoke。

每个候选至少覆盖：

- 1 个中文 mock 输入
- 预期输出字段
- 禁止输出/禁止动作
- 人工复核触发
- Smoke 结论：`passed` / `failed` / `needs_fix` / `blocked`

## Smoke 不是正式 L2

- Smoke 通过只代表候选库可试跑。
- 正式 L2 只给 Top 15 优先候选执行，每个至少 3 个中文业务用例。
- 不安装额外业务依赖，不访问真实账号，不调用真实业务 API，不发送、不写入、不抓取、不上传、不生成真实媒体。

## 输出文件

- `DEEPAGENTS_SMOKE_TO_50_RESULT.md`
- `L2_OFFICIAL_TOP15_FROM_TO50_QUEUE.md`
