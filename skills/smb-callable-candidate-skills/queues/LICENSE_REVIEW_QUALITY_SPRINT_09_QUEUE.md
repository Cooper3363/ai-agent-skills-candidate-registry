# LICENSE_REVIEW_QUALITY_SPRINT_09_QUEUE

Generated: 2026-06-09
Source: `../QUALITY_SOURCE_SPRINT_09_RESULT.md`

## Queue Scope

- Review exactly 30 selected candidates for six-department SMB coverage.
- This is L1 / trial-mode review only.
- Do not run code, install dependencies, call APIs/providers, generate media, read customer files, read `.env`, print/write keys, or modify stable.
- Output requested from license window:
  - `../LICENSE_REVIEW_QUALITY_SPRINT_09_RESULT.md`
  - `DEEPAGENTS_SMOKE_QUALITY_SPRINT_09_QUEUE.md` for L1/trial-mode allow items only.

## Summary

| Department | Count |
| --- | ---: |
| Creative design | 5 |
| Operations | 5 |
| Sales / marketing ops | 5 |
| Ecommerce | 5 |
| Support / customer success | 5 |
| Management / HR / finance | 5 |
| Total | 30 |

## Review Queue

| # | priority | candidate_id | department | source_url | source_type | license_review_focus | proposed_trial_mode | smoke_focus_if_allowed | exclusion_condition |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | P0 | `quality_sprint09_invokeai_product_scene_workflow_candidate` | Creative design | https://github.com/invoke-ai/InvokeAI | open-source media workflow | Confirm Apache-2.0, model licenses, hosted/local runtime boundaries, generated media rights | `route_config_mock` | product brief -> InvokeAI workflow payload plan | block local server, GPU/model run, generated media, upload |
| 2 | P1 | `quality_sprint09_sdwebui_ad_asset_workflow_candidate` | Creative design | https://github.com/AUTOMATIC1111/stable-diffusion-webui | open-source media runtime | Confirm repo license, extension/model terms, AGPL/GPL risk if applicable | `route_config_mock` | campaign brief -> SD WebUI workflow spec | block webui launch, extension install, model run, generated media |
| 3 | P1 | `quality_sprint09_blender_product_scene_brief_candidate` | Creative design | https://github.com/blender/blender | open-source 3D suite | Confirm GPL/output/add-on boundary and commercial use implications | `metadata_mock` | product metadata -> shot list and scene brief | block Blender launch, render, file output, asset upload |
| 4 | P0 | `quality_sprint09_penpot_design_system_gap_candidate` | Creative design | https://github.com/penpot/penpot | open-source design platform | Confirm MPL-2.0, API/plugin/MCP terms, design data privacy | `read_only_mock` | mock tokens/screens -> design system gap brief | block workspace login, export, plugin execution, file write |
| 5 | P1 | `quality_sprint09_excalidraw_process_diagram_candidate` | Creative design | https://github.com/excalidraw/excalidraw | open-source diagram tool | Confirm MIT, export/library terms, diagram data privacy | `mock_json_only` | mock process nodes -> diagram structure brief | block render, browser automation, export, file output |
| 6 | P0 | `quality_sprint09_temporal_sla_workflow_exception_candidate` | Operations | https://github.com/temporalio/temporal | open-source workflow engine | Confirm MIT, cloud/service terms, namespace/API boundary | `metadata_mock` | mock workflow states -> SLA exception digest | block workflow execution, worker run, API connection |
| 7 | P0 | `quality_sprint09_kestra_ops_flow_failure_digest_candidate` | Operations | https://github.com/kestra-io/kestra | open-source orchestration | Confirm Apache-2.0, plugin/cloud terms, scheduler write risks | `metadata_mock` | mock flow statuses -> failure and retry digest | block flow run, scheduler write, plugin execution |
| 8 | P0 | `quality_sprint09_prometheus_alert_runbook_digest_candidate` | Operations | https://github.com/prometheus/prometheus | open-source monitoring | Confirm Apache-2.0, metric privacy, Alertmanager boundary | `read_only_mock` | mock alerts -> runbook digest | block scrape, production metric read, alert write |
| 9 | P1 | `quality_sprint09_signoz_service_health_candidate` | Operations | https://github.com/SigNoz/signoz | observability platform | Confirm license/edition, telemetry privacy, export/write boundary | `read_only_mock` | mock telemetry rows -> service health digest | block real telemetry read, alert write, export |
| 10 | P1 | `quality_sprint09_jaeger_trace_incident_timeline_candidate` | Operations | https://github.com/jaegertracing/jaeger | distributed tracing | Confirm Apache-2.0, trace privacy, query/export boundary | `read_only_mock` | mock spans -> incident timeline | block backend connection, query execution, data export |
| 11 | P0 | `quality_sprint09_espocrm_lead_source_health_candidate` | Sales / marketing ops | https://github.com/espocrm/espocrm | open-source CRM | Confirm AGPL-3.0/commercial implications and CRM data privacy | `read_only_mock` | mock leads/opportunities -> lead source health | block CRM write, task create, email send |
| 12 | P1 | `quality_sprint09_suitecrm_opportunity_stale_stage_candidate` | Sales / marketing ops | https://github.com/salesagility/SuiteCRM | open-source CRM | Confirm GPL/AGPL-family terms and extension/commercial risks | `read_only_mock` | mock opportunities -> stale stage report | block CRM write, campaign/email/task actions |
| 13 | P0 | `quality_sprint09_mautic_campaign_lead_nurture_candidate` | Sales / marketing ops | https://github.com/mautic/mautic | marketing automation | Confirm GPL-family terms, email/send and tracking data boundaries | `read_only_mock` | mock campaigns -> nurture health brief | block email send, segment write, campaign publish |
| 14 | P1 | `quality_sprint09_frappe_crm_pipeline_gap_candidate` | Sales / marketing ops | https://github.com/frappe/crm | open-source CRM | Confirm license and Frappe ecosystem/API terms | `read_only_mock` | mock pipeline rows -> handoff quality brief | block CRM write, assignment, notification send |
| 15 | P1 | `quality_sprint09_listmonk_newsletter_segment_health_candidate` | Sales / marketing ops | https://github.com/knadh/listmonk | newsletter manager | Confirm AGPL-3.0/commercial implications and email/send boundary | `read_only_mock` | mock lists/campaign metrics -> segment health | block campaign send, subscriber import/export, segment write |
| 16 | P0 | `quality_sprint09_opencart_catalog_stock_qc_candidate` | Ecommerce | https://github.com/opencart/opencart | open-source ecommerce | Confirm license, API terms, store data privacy | `read_only_mock` | mock products/stock -> catalog QC | block product/order/inventory/checkout write |
| 17 | P1 | `quality_sprint09_nopcommerce_order_margin_candidate` | Ecommerce | https://github.com/nopSolutions/nopCommerce | open-source ecommerce | Confirm license/commercial terms and order data privacy | `read_only_mock` | mock orders -> margin and anomaly digest | block order/status/product/inventory write |
| 18 | P0 | `quality_sprint09_spree_return_exchange_risk_candidate` | Ecommerce | https://github.com/spree/spree | headless ecommerce | Confirm license and API/read-only boundary | `read_only_mock` | mock returns/orders -> risk brief | block return/refund/order/catalog write |
| 19 | P1 | `quality_sprint09_shopware_promo_catalog_gap_candidate` | Ecommerce | https://github.com/shopware/shopware | open-source commerce | Confirm MIT/commercial extension terms and store API boundary | `read_only_mock` | mock promos/products -> catalog gap report | block product/promo/order/customer write |
| 20 | P1 | `quality_sprint09_solidus_order_exception_candidate` | Ecommerce | https://github.com/solidusio/solidus | ecommerce framework | Confirm license and fulfillment/inventory boundary | `read_only_mock` | mock orders -> exception brief | block order write, fulfillment update, inventory change |
| 21 | P0 | `quality_sprint09_zammad_ticket_sla_macro_gap_candidate` | Support / customer success | https://github.com/zammad/zammad | open-source helpdesk | Confirm AGPL-3.0/commercial implications and support data privacy | `read_only_mock` | mock tickets/macros -> SLA and macro gap | block reply send, assignment/tag/status write |
| 22 | P0 | `quality_sprint09_osticket_queue_triage_candidate` | Support / customer success | https://github.com/osTicket/osTicket | ticketing system | Confirm GPL-2.0 and plugin/extension terms | `read_only_mock` | mock tickets -> queue triage brief | block ticket update, reply send, assignment write |
| 23 | P1 | `quality_sprint09_uvdesk_article_macro_gap_candidate` | Support / customer success | https://github.com/uvdesk/community-skeleton | helpdesk | Confirm license and knowledge base/ticket API boundary | `read_only_mock` | mock tickets/articles -> article and macro gap | block ticket reply, article publish, assignment/tag write |
| 24 | P1 | `quality_sprint09_freescout_mailbox_handoff_candidate` | Support / customer success | https://github.com/freescout-help-desk/freescout | shared mailbox/helpdesk | Confirm license/commercial terms and mailbox data privacy | `read_only_mock` | mock conversations -> shift handoff digest | block reply send, mailbox write, assignment/tag write |
| 25 | P2 | `quality_sprint09_glitchtip_customer_impact_issue_digest_candidate` | Support / customer success | https://gitlab.com/glitchtip/glitchtip | error tracking | Confirm license, Sentry compatibility terms, telemetry privacy | `read_only_mock` | mock issues -> customer impact digest | block issue resolve, alert write, source map upload |
| 26 | P0 | `quality_sprint09_erpnext_purchase_approval_aging_candidate` | Management / HR / finance | https://github.com/frappe/erpnext | open-source ERP | Confirm GPL-3.0, ERP/accounting data privacy, API scope | `read_only_mock` | mock purchase approvals -> aging brief | block PO/invoice/payment/accounting/inventory write |
| 27 | P1 | `quality_sprint09_dolibarr_invoice_payment_exception_candidate` | Management / HR / finance | https://github.com/Dolibarr/dolibarr | ERP/CRM | Confirm GPL terms and accounting/payment boundary | `read_only_mock` | mock invoices/payments -> exception brief | block invoice/payment/customer/accounting write |
| 28 | P1 | `quality_sprint09_kimai_timesheet_anomaly_candidate` | Management / HR / finance | https://github.com/kimai/kimai | time tracking | Confirm license and timesheet/payroll/billing boundary | `read_only_mock` | mock timesheets -> anomaly report | block timesheet edit, invoice generation, payroll decision |
| 29 | P1 | `quality_sprint09_orangehrm_leave_coverage_candidate` | Management / HR / finance | https://github.com/orangehrm/orangehrm | HRM | Confirm GPL terms, HR data privacy, decision boundary | `read_only_mock` | mock leave records -> coverage risk brief | block leave approval/rejection, employee write, HR decision |
| 30 | P0 | `quality_sprint09_openproject_project_risk_digest_candidate` | Management / HR / finance | https://github.com/opf/openproject | project management | Confirm GPL terms, project data privacy, API scope | `read_only_mock` | mock work packages -> project risk digest | block task update, notification, file sharing |

## Hard Boundary For All Items

- No dependency install.
- No repository code execution.
- No real account/OAuth/API/provider access.
- No key, token, `.env`, credential, customer file, real business document, production metric, trace, log, ledger, HR record, ticket, order, invoice, or design file read/write/print.
- No message send, file upload, business-system write, refund, compensation, payment capture, inventory update, subscription update, ledger write, tax filing, task creation, file sharing, browser automation, real crawl, render, export, or media generation.
- No stable registry modification during L1.

