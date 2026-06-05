# competitor_product_snapshot_candidate

## 当前状态

- 状态：`component_only`
- 客户可调用：否
- 独立 L3：否
- 来源：六部门候选池正式 L2 simulated

## 业务定位

解析 mock 或已授权的竞品商品快照，识别价格变化、可售状态和证据片段，服务电商或门店运营的竞品观察。

## 调用边界

- 允许：处理 mock HTML、old/new snapshot 文本、已授权快照。
- 禁止：真实网页抓取、代理、登录、绕 robots/ToS、自动监控。
- 人工复核：ToS/robots 不清、页面过期、价格证据不足、动态内容、缺货/下架不可比。

## L2 结论

正式 L2 simulated 完成，但结论为仅组件。真实抓取、代理、robots/ToS 审批均未完成，不作为独立客户可调用 Skill。

## 下一步

进入候选库组件池，等待竞品观察组合流程复用。
