# QUALITY_SOURCE_SPRINT_09_RESULT

Updated: 2026-06-09

## Scope

- Goal: select 30 high-quality Skill / Agent / tool candidates for SMB six-department scenarios.
- Department coverage: creative design, operations, sales, ecommerce, support, management / HR / finance.
- Selection rule: candidates can enter the candidate registry if they fit the platform base, can use the OpenAI-compatible relay/model gateway where model inference is needed, and can serve SMB six-department workflows.
- This file is source research only. It does not mean L1 passed, L2 passed, draft L3 packaged, stable promoted, or customer-callable.
- No dependencies installed, no repository code executed, no real account access, no API/provider calls, no generated images/videos/audio/files, no customer data access, no key read/write/print, no business-system writes.

## Current Registry Baseline

- Stable registry current count: 71 formal Skills.
- Candidate repository tracked file count before this Sprint09 source write: 776.
- Deduplication baseline: avoid direct repeats from Quality Sprints 01-08 and existing stable 71. Known repeats intentionally excluded include ComfyUI, FFmpeg, n8n, Grafana, PrestaShop, Magento API snapshot, Shopify, BigCommerce, WooCommerce, Medusa, Saleor, Sylius, Superset, Redash, Metabase, PostHog, Intercom, Zendesk, Freshdesk, Help Scout, Front, HubSpot, Zoho, Pipedrive, Stripe, Xero, QuickBooks, BambooHR, and prior media provider route candidates.

## Selection Summary

| Category | Count |
| --- | ---: |
| Total selected candidates | 30 |
| Creative design | 5 |
| Operations | 5 |
| Sales / marketing ops | 5 |
| Ecommerce | 5 |
| Support / customer success | 5 |
| Management / HR / finance | 5 |
| Open-source repo / tool candidates | 30 |
| Media / local runtime route candidates | 3 |
| License-review-sensitive candidates | 16 |
| Default L1 state | 30 needs_license_review |

## Top 30 Candidate Table

| # | candidate_id | department | source / URL | source_type | license_signal | proposed_skill | trial_mode | score | why selected | hard boundary |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | `quality_sprint09_invokeai_product_scene_workflow_candidate` | Creative design | InvokeAI, https://github.com/invoke-ai/InvokeAI | open-source media workflow | Apache-2.0 signal; model/license dependency review required | product scene workflow payload planner | route_config_mock | 86 | mature creative AI image workflow with canvas and node workflows; good fit for marketing/ecommerce visuals | no local server, no model run, no GPU job, no generated image, no upload |
| 2 | `quality_sprint09_sdwebui_ad_asset_workflow_candidate` | Creative design | AUTOMATIC1111 stable-diffusion-webui, https://github.com/AUTOMATIC1111/stable-diffusion-webui | open-source media runtime | license and extension/model terms need review | ad asset prompt and workflow spec | route_config_mock | 78 | widely used image generation UI; useful as workflow spec only | no webui launch, no extension install, no model run, no generated media |
| 3 | `quality_sprint09_blender_product_scene_brief_candidate` | Creative design | Blender, https://github.com/blender/blender | open-source 3D creation suite | GPL signal; output and add-on boundary review required | product 3D scene / shot list brief | metadata_mock | 80 | strong product scene and training visualization tool; useful before any render pipeline | no Blender launch, no render, no file output, no asset upload |
| 4 | `quality_sprint09_penpot_design_system_gap_candidate` | Creative design | Penpot, https://github.com/penpot/penpot | open-source design platform | MPL-2.0 signal; API/plugin boundary review required | design system gap read-only brief | read_only_mock | 83 | open-source design platform with API/MCP direction; fits design-to-code and brand ops | no workspace login, no design export, no file write, no plugin execution |
| 5 | `quality_sprint09_excalidraw_process_diagram_candidate` | Creative design | Excalidraw, https://github.com/excalidraw/excalidraw | open-source whiteboard/diagram | MIT signal; export boundary review required | process diagram structure and handoff brief | mock_json_only | 79 | useful for operations process diagrams, support flow maps, onboarding sketches | no canvas render, no export, no browser automation, no file output |
| 6 | `quality_sprint09_temporal_sla_workflow_exception_candidate` | Operations | Temporal, https://github.com/temporalio/temporal | open-source workflow engine | MIT signal; service/cloud terms review required | SLA workflow exception digest | metadata_mock | 86 | high-quality workflow engine for operational exception modeling | no workflow execution, no worker run, no namespace/API connection |
| 7 | `quality_sprint09_kestra_ops_flow_failure_digest_candidate` | Operations | Kestra, https://github.com/kestra-io/kestra | open-source orchestration/scheduling | Apache-2.0 signal; plugin/cloud terms review required | ops flow failure and retry digest | metadata_mock | 84 | strong event-driven orchestration candidate for ops automations | no flow run, no scheduler write, no plugin execution |
| 8 | `quality_sprint09_prometheus_alert_runbook_digest_candidate` | Operations | Prometheus, https://github.com/prometheus/prometheus | open-source monitoring | Apache-2.0 signal; data/privacy review required | alert-to-runbook digest | read_only_mock | 82 | common SMB/self-host monitoring stack; good operations health adapter | no scrape, no alertmanager write, no production metric read |
| 9 | `quality_sprint09_signoz_service_health_candidate` | Operations | SigNoz, https://github.com/SigNoz/signoz | open-source observability | license/edition review required | service health and customer-impact digest | read_only_mock | 81 | OpenTelemetry-native observability platform with logs/traces/metrics | no real telemetry read, no alert write, no retention/export action |
| 10 | `quality_sprint09_jaeger_trace_incident_timeline_candidate` | Operations | Jaeger, https://github.com/jaegertracing/jaeger | open-source tracing | Apache-2.0 signal; trace data privacy review required | incident trace timeline brief | read_only_mock | 79 | useful for support/ops incident explanation from trace summaries | no trace backend connection, no query execution, no data export |
| 11 | `quality_sprint09_espocrm_lead_source_health_candidate` | Sales / marketing ops | EspoCRM, https://github.com/espocrm/espocrm | open-source CRM | AGPL-3.0 signal; commercial use review required | lead source health read-only report | read_only_mock | 80 | mature CRM with lead/contact/opportunity support | no CRM write, no task create, no email send |
| 12 | `quality_sprint09_suitecrm_opportunity_stale_stage_candidate` | Sales / marketing ops | SuiteCRM, https://github.com/salesagility/SuiteCRM | open-source CRM | GPL/AGPL-family review required | stale opportunity stage read-only brief | read_only_mock | 77 | widely recognized open-source CRM; fills non-HubSpot coverage | no CRM write, no task/email/campaign action |
| 13 | `quality_sprint09_mautic_campaign_lead_nurture_candidate` | Sales / marketing ops | Mautic, https://github.com/mautic/mautic | open-source marketing automation | GPL-family signal; email/commercial terms review required | campaign nurture health read-only brief | read_only_mock | 80 | well-known marketing automation platform for SMB lifecycle campaigns | no email send, no segment write, no campaign publish |
| 14 | `quality_sprint09_frappe_crm_pipeline_gap_candidate` | Sales / marketing ops | Frappe CRM, https://github.com/frappe/crm | open-source CRM | license review required | pipeline gap and handoff quality brief | read_only_mock | 79 | modern open-source CRM aligned with ERPNext/Frappe ecosystem | no CRM write, no assignment, no notification send |
| 15 | `quality_sprint09_listmonk_newsletter_segment_health_candidate` | Sales / marketing ops | listmonk, https://github.com/knadh/listmonk | open-source newsletter manager | AGPL-3.0 signal; email/send boundary review required | newsletter segment health report | read_only_mock | 78 | self-hosted mailing list manager with strong SMB relevance | no campaign send, no subscriber import/export, no segment write |
| 16 | `quality_sprint09_opencart_catalog_stock_qc_candidate` | Ecommerce | OpenCart, https://github.com/opencart/opencart | open-source ecommerce | license file present; terms review required | catalog and stock QC read-only brief | read_only_mock | 82 | common open-source ecommerce platform not yet covered in stable | no product/order/inventory write, no checkout action |
| 17 | `quality_sprint09_nopcommerce_order_margin_candidate` | Ecommerce | nopCommerce, https://github.com/nopSolutions/nopCommerce | open-source ecommerce | license review required | order margin and anomaly digest | read_only_mock | 80 | ASP.NET ecommerce platform; useful for non-PHP/.NET shops | no order/status/product/inventory write |
| 18 | `quality_sprint09_spree_return_exchange_risk_candidate` | Ecommerce | Spree Commerce, https://github.com/spree/spree | open-source headless ecommerce | license review required | return and exchange risk read-only brief | read_only_mock | 81 | headless commerce platform with REST API and marketplace use cases | no return/refund/order/catalog write |
| 19 | `quality_sprint09_shopware_promo_catalog_gap_candidate` | Ecommerce | Shopware, https://github.com/shopware/shopware | open-source commerce platform | MIT signal plus commercial/extension review required | promo and catalog gap read-only report | read_only_mock | 80 | recognized commerce platform with strong EU/SMB footprint | no product/promotion/order/customer write |
| 20 | `quality_sprint09_solidus_order_exception_candidate` | Ecommerce | Solidus, https://github.com/solidusio/solidus | open-source ecommerce framework | license review required | order exception and fulfillment gap brief | read_only_mock | 78 | mature commerce framework for customizable stores | no order write, no fulfillment update, no inventory change |
| 21 | `quality_sprint09_zammad_ticket_sla_macro_gap_candidate` | Support / customer success | Zammad, https://github.com/zammad/zammad | open-source helpdesk | AGPL-3.0 signal; commercial use review required | ticket SLA and macro gap read-only report | read_only_mock | 82 | web-based open-source support desk; fills support stack coverage | no reply send, no assignment/tag/status write |
| 22 | `quality_sprint09_osticket_queue_triage_candidate` | Support / customer success | osTicket, https://github.com/osTicket/osTicket | open-source ticketing | GPL-2.0 signal; extension terms review required | ticket queue triage read-only brief | read_only_mock | 80 | widely used ticketing system for small teams | no ticket update, no reply send, no assignment write |
| 23 | `quality_sprint09_uvdesk_article_macro_gap_candidate` | Support / customer success | UVdesk, https://github.com/uvdesk/community-skeleton | open-source helpdesk | license review required | help article and macro gap brief | read_only_mock | 77 | support ticket system with knowledge workflow fit | no ticket reply, no article publish, no assignment/tag write |
| 24 | `quality_sprint09_freescout_mailbox_handoff_candidate` | Support / customer success | FreeScout, https://github.com/freescout-help-desk/freescout | open-source shared mailbox/helpdesk | license review required | shared mailbox handoff digest | read_only_mock | 79 | lightweight Help Scout alternative for SMB shared inboxes | no reply send, no mailbox write, no assignment/tag write |
| 25 | `quality_sprint09_glitchtip_customer_impact_issue_digest_candidate` | Support / customer success | GlitchTip, https://gitlab.com/glitchtip/glitchtip | open-source error tracking | license review required | customer-impact issue digest | read_only_mock | 76 | Sentry-compatible error tracking can support customer impact triage | no issue resolve, no alert write, no source map upload |
| 26 | `quality_sprint09_erpnext_purchase_approval_aging_candidate` | Management / HR / finance | ERPNext, https://github.com/frappe/erpnext | open-source ERP | GPL-3.0 signal; accounting/ERP terms review required | purchase approval aging read-only brief | read_only_mock | 84 | broad SMB ERP coverage across purchasing, accounting, inventory, projects | no PO/invoice/payment/accounting/inventory write |
| 27 | `quality_sprint09_dolibarr_invoice_payment_exception_candidate` | Management / HR / finance | Dolibarr, https://github.com/Dolibarr/dolibarr | open-source ERP/CRM | GPL signal; accounting boundary review required | invoice and payment exception brief | read_only_mock | 80 | SMB-friendly ERP/CRM with invoices, orders, stocks, agenda | no invoice/payment/customer/accounting write |
| 28 | `quality_sprint09_kimai_timesheet_anomaly_candidate` | Management / HR / finance | Kimai, https://github.com/kimai/kimai | open-source time tracking | license review required | timesheet anomaly and billing risk brief | read_only_mock | 79 | practical HR/finance bridge for timesheets, invoices, reports | no timesheet edit, no invoice generation, no payroll decision |
| 29 | `quality_sprint09_orangehrm_leave_coverage_candidate` | Management / HR / finance | OrangeHRM, https://github.com/orangehrm/orangehrm | open-source HRM | GPL signal; HR decision boundary review required | leave coverage and staffing risk brief | read_only_mock | 78 | recognized HRM with leave and employee lifecycle coverage | no leave approval/rejection, no employee record write, no HR decision |
| 30 | `quality_sprint09_openproject_project_risk_digest_candidate` | Management / HR / finance | OpenProject, https://github.com/opf/openproject | open-source project management | GPL signal; project data boundary review required | project risk and handoff digest | read_only_mock | 81 | strong project/task management coverage for admin and delivery teams | no task creation/update, no notification, no file sharing |

## P0 Priority Subset

These 12 should be prioritized for L1 review because their source quality, business value, and testability are strongest:

1. `quality_sprint09_invokeai_product_scene_workflow_candidate`
2. `quality_sprint09_penpot_design_system_gap_candidate`
3. `quality_sprint09_temporal_sla_workflow_exception_candidate`
4. `quality_sprint09_kestra_ops_flow_failure_digest_candidate`
5. `quality_sprint09_prometheus_alert_runbook_digest_candidate`
6. `quality_sprint09_espocrm_lead_source_health_candidate`
7. `quality_sprint09_mautic_campaign_lead_nurture_candidate`
8. `quality_sprint09_opencart_catalog_stock_qc_candidate`
9. `quality_sprint09_spree_return_exchange_risk_candidate`
10. `quality_sprint09_zammad_ticket_sla_macro_gap_candidate`
11. `quality_sprint09_erpnext_purchase_approval_aging_candidate`
12. `quality_sprint09_openproject_project_risk_digest_candidate`

## L1 Review Guidance

- Open-source tools with permissive licenses can move to `allow_smoke` if the license and dependency chain are clean.
- GPL/AGPL/MPL/custom or unclear license candidates may still remain in candidate evidence, but should not enter stable without legal/commercial confirmation.
- Media/local runtime candidates must stay `route_config_mock` or `metadata_mock`; no real generation before separate provider/runtime approval.
- CRM/ERP/helpdesk/ecommerce candidates must stay `read_only_mock`; no real account/OAuth/API access, no writes, no sends, no exports.
- HR/finance candidates must keep human review and advisory-only boundaries; no HR decisions, payroll, accounting, payment, tax, or ledger writes.
- Observability/workflow candidates must not connect to production metrics/traces/logs, execute workflows, or write schedules/alerts.

## Recommended Next Step

- Send `queues/LICENSE_REVIEW_QUALITY_SPRINT_09_QUEUE.md` to the license window.
- If L1 passes, testbench should generate `DEEPAGENTS_SMOKE_QUALITY_SPRINT_09_RESULT.md` and a Top10 or Top12 L2 queue.
- Stable registry remains at 71 until explicit platform acceptance and promotion.
