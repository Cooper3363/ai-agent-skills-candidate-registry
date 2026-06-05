# Draft L3 Packaging Queue From To100

来源：`L2_OFFICIAL_TOP15_FROM_TO100_RESULT.md`  
状态：draft L3 packaging candidates only  
说明：进入本队列不代表客户正式可调用，不改变稳交付库 13 个 Skill 状态。

## 1. 统一封装边界

- 不安装额外业务依赖。
- 不访问真实账号。
- 不读取真实客户文件。
- 不调用真实业务 API。
- 不发送邮件、短信或微信。
- 不写 CRM、日历、任务、客服系统、电商平台、采购系统、财务系统或其他业务系统。
- 不真实抓取网页。
- 不上传文件。
- 不退款、不赔偿、不改库存、不改价、不下采购单。
- 不生成真实图片、视频、音频、OCR 或 PDF 结果。
- 不改稳交付 13 个包。
- 所有输出必须包含人工复核触发和风险提示。

## 2. 封装候选

| candidate_id | 业务包 | L2 结论 | 必须保留的权限边界 | 必须保留的人工复核触发 | draft L3 重点 |
| --- | --- | --- | --- | --- | --- |
| `support_ticket_autotag_router_candidate` | 客服知识库助手包 | L2 通过可封装 | 只读工单文本；不写客服系统；不自动派单 | 投诉、退款、账号安全、VIP、低置信 | 工单标签、优先级、路由建议 |
| `support_refund_evidence_request_candidate` | 客服知识库助手包 | L2 通过可封装 | dry-run；`external_action_blocked=true`; `send_allowed=false`; `write_allowed=false`; 不退款 | 赔偿、监管威胁、敏感证据、未成年人 | 退款证据最小化请求草稿 |
| `support_policy_conflict_detector_candidate` | 客服知识库助手包 | L2 通过可封装 | 只读政策片段；不改知识库；不发布政策 | 客户权益、退款/保修/配送冲突 | 政策冲突定位和修订问题 |
| `support_vip_customer_handoff_candidate` | 客服知识库助手包 | L2 通过可封装 | 只读客户上下文；不联系客户；不承诺补偿 | VIP 投诉、合同客户、舆情、赔偿 | VIP 高风险转人工简报 |
| `pricing_terms_risk_summary_candidate` | 销售跟进助手包 | L2 通过可封装 | 只读报价条款；不审批折扣；不改报价 | 高折扣、长账期、验收后付款、违约责任 | 价格/付款条款风险摘要 |
| `demo_script_builder_candidate` | 销售跟进助手包 | L2 通过可封装 | 只输出演示脚本；不承诺产品能力或交付结果 | 未验证能力、定制需求、敏感行业 | 售前演示流程和话术 |
| `lost_deal_followup_draft_candidate` | 销售跟进助手包 | L2 通过可封装 | dry-run；`external_action_blocked=true`; `send_allowed=false`; `write_allowed=false`; 不写 CRM | 退订、竞品敏感、折扣越权、明确拒绝 | 丢单复联草稿 |
| `customer_reference_brief_candidate` | 销售跟进助手包 | L2 通过可封装 | 只用授权案例；不外发未授权信息；不伪造案例 | 案例授权、效果夸大、行业敏感 | 授权客户案例匹配简报 |
| `promo_bundle_copy_matrix_candidate` | 营销内容生产包 | L2 通过可封装 | 只产出文案矩阵；不发布；不投放；不改价格 | 价格库存、绝对化承诺、平台规则 | 促销套装多渠道文案矩阵 |
| `influencer_brief_draft_candidate` | 营销内容生产包 | L2 通过可封装 | dry-run；`external_action_blocked=true`; `send_allowed=false`; `write_allowed=false`; 不联系达人、不付款 | 广告披露、授权、效果承诺、肖像/素材 | 达人合作 brief 草稿 |
| `product_attribute_gap_checker_candidate` | 营销内容生产包 | L2 通过可封装 | 只检查商品信息；不写平台；不改商品 | 食品/3C/服饰关键属性、平台规则 | 商品属性缺口检查 |
| `supplier_delivery_risk_brief_candidate` | 经营报表分析包 | L2 通过可封装 | 只读供应商记录；不下采购单；不处罚供应商 | 合同履约、缺货涨价、质量退货 | 供应商交付风险简报 |
| `gross_margin_bridge_summary_candidate` | 经营报表分析包 | L2 通过可封装 | 只读财务指标；不做审计/税务/经营决策 | 财务口径、成本异常、折扣异常、缺失数据 | 毛利变化桥接摘要 |

## 3. 不进入封装的组件项

| candidate_id | 处理 |
| --- | --- |
| `support_ticket_batch_summary_candidate` | 进入客服运营组件池，不单独 draft L3 |
| `brand_forbidden_words_checker_candidate` | 进入营销合规/品牌词库组件池，不单独 draft L3 |

## 4. 下一步

封装窗口可基于本队列生成 draft L3 资料包，但不得把 draft L3 状态写成客户正式可调用。正式可调用仍需平台调用验收和指挥中心确认。
