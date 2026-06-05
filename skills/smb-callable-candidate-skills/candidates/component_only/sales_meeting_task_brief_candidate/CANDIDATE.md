# sales_meeting_task_brief_candidate

## 当前状态

- 状态：`component_only`
- 客户可调用：否
- 独立 L3：否
- 来源：六部门候选池正式 L2 simulated

## 业务定位

把销售会议纪要整理成任务草案和 dry-run payload，适合在销售会议、客户评审、报价沟通后整理下一步行动项。

## 调用边界

- 允许：输出会议摘要、行动项、负责人、时间、dry-run payload、权限提示和风险标签。
- 禁止：真实 OAuth、真实写入 Google Workspace、日历、任务、CRM 或文档。
- 人工复核：合同条款、价格承诺、客户隐私、行动项归属不确定。

## L2 结论

正式 L2 simulated 完成，但结论为仅组件。外部 Workspace 写入能力未测试，不作为独立客户可调用 Skill。

## 下一步

进入候选库组件池，等待销售会议组合流程复用。
