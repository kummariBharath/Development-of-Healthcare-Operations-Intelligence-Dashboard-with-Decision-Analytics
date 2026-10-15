"""
MedOps Technical Documentation - Section 5: Complete Dashboard Module Guide
Documents all 21 modules verified from the source code across 14 standardized criteria.
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib import colors
from docs.styles import (
    PRINTABLE_WIDTH, PRIMARY_NAVY, BRAND_TEAL, BRAND_CYAN, ACCENT_BLUE,
    ACCENT_AMBER, ACCENT_ROSE, ACCENT_EMERALD, BG_CARD, BORDER_COLOR,
    TEXT_MAIN, make_callout, make_section_divider
)

# 21 Modules Data Definition
MODULES_DATA = [
    {
        "num": "5.1",
        "name": "Executive Command Center",
        "purpose": "Provides macro-level operational, financial, and clinical throughput visibility across all 5 regional facilities.",
        "problem": "Hospital C-suite leaders lack a single pane of glass to monitor hospital-wide census, revenue run-rate, and emergency load.",
        "kpis": "Active Admissions (Total Inpatients), Bed Occupancy Rate (%), Total Net Revenue ($), Claims Denial Rate (%), Avg Emergency Wait Time (mins), Average Length of Stay (ALOS days).",
        "features": "AI Executive Synthesis Brief, Multi-facility comparison matrix, Departmental admissions breakdown bar chart, Timeframe filters (Realtime, Today, Weekly, Monthly, Quarterly, YTD), Drilldown modal trigger.",
        "file": "src/components/modules/ExecutiveCommandCenter.tsx",
        "endpoint": "GET /api/dashboard/summary",
        "service": "get_executive_summary()",
        "sources": "admissions, facilities, billing, claims, emergency_visits, beds",
        "calc": "Occupancy = (Active Admissions / Total Licensed Beds) * 100; Denial Rate = (Denied Claims / Total Claims) * 100; Net Revenue = sum(net_amount).",
        "rules": "Active admissions count records where admission_date <= ref_date AND (discharge_date IS NULL OR discharge_date > ref_date).",
        "unavail": "Displays '0' or 'N/A' safely; shows 'Data Source: Amazon Athena (Verified)' badge when live.",
        "demo": "Select facility 'All' and timeframe 'Monthly' to demonstrate macro-level enterprise census of 5 facilities.",
        "qa": "Q: Why does the Occupancy rate not match total historical admissions? A: Because it strictly filters for active admissions overlapping the reference date against licensed beds, rather than cumulative admissions."
    },
    {
        "num": "5.2",
        "name": "Patient Operations & Flow",
        "purpose": "Tracks inpatient flow, bed occupancy by ward, room assignments, admission types, and discharge barriers.",
        "problem": "Patient boarding in emergency departments and delayed bed turnover slow down admissions and increase diversion hours.",
        "kpis": "Total Admissions, Active Inpatients, Bed Occupancy %, Average Length of Stay (ALOS), Discharges Today, Discharge Delays.",
        "features": "Bed occupancy by department bar chart, Admission type distribution (Emergency vs Elective vs Urgent), Inpatient census table with bed numbers.",
        "file": "src/components/modules/PatientOperations.tsx",
        "endpoint": "GET /api/dashboard/patient-ops",
        "service": "get_patient_ops_intelligence()",
        "sources": "admissions, beds, departments, facilities, discharge_records",
        "calc": "ALOS = sum(length_of_stay_days) / total_discharges; Occupancy per department = (Active Inpatients in Dept / Total Beds in Dept) * 100.",
        "rules": "NULL discharge_date is treated as an active inpatient. Filters apply consistently to both admission and discharge records.",
        "unavail": "If no admissions match, renders 'No Data Available' state without throwing JavaScript undefined errors.",
        "demo": "Filter by 'General Ward' to highlight high bed turnover compared to the ICU.",
        "qa": "Q: How do you handle patients discharged on the same day? A: Length of stay is treated as 1 day minimum or calculated in decimal hours if arrival/departure timestamps exist."
    },
    {
        "num": "5.3",
        "name": "Doctor & Staff Intelligence",
        "purpose": "Monitors clinical workforce allocation, physician workload, nursing ratios, and overtime expenditure.",
        "problem": "Imbalanced physician assignments and unmonitored nursing overtime lead to clinical burnout and staffing budget overruns.",
        "kpis": "Total Clinical Staff, Active On-Duty Physicians, Avg Workload Score, Total Overtime Hours, Patient-to-Nurse Ratio.",
        "features": "Physician workload distribution chart, Departmental staffing allocation table, Overtime trend analysis, Shift attendance tracking.",
        "file": "src/components/modules/DoctorStaffIntelligence.tsx",
        "endpoint": "GET /api/dashboard/doctor-staff",
        "service": "get_doctor_staff_intelligence()",
        "sources": "staff, doctors, staff_attendance, doctor_workload, nurse_shifts",
        "calc": "Overtime Rate = (Total Overtime Hours / Total Scheduled Hours) * 100; Workload Score = weighted average of patient encounters and surgeries.",
        "rules": "Protected IDs (doctor_id, staff_id) are never converted to numbers during Pandas aggregation.",
        "unavail": "Falls back to departmental baseline ratios if live timesheet data is unavailable.",
        "demo": "Point out the Cardiology department's elevated workload score during emergency surges.",
        "qa": "Q: How is workload score defined? A: It is an indexed clinical activity score combining outpatient appointments, inpatient rounds, and surgical procedures against standard shift hours."
    },
    {
        "num": "5.4",
        "name": "Emergency & Critical Operations",
        "purpose": "Provides high-frequency telemetry on Emergency Department (ED) triage, boarding, and ICU capacity.",
        "problem": "Emergency overcrowding causes extended door-to-doctor times, patient walkouts, and compromised critical care outcomes.",
        "kpis": "Total ED Visits, Avg Door-to-Doctor Wait Time (mins), ICU Bed Utilization %, High-Acuity Cases (ESI 1 & 2), Left Without Being Seen (LWBS).",
        "features": "Emergency triage level breakdown (ESI 1-5), Hourly arrival trend line chart, ICU ventilator utilization progress bars, Emergency disposition table.",
        "file": "src/components/modules/EmergencyCriticalOperations.tsx",
        "endpoint": "GET /api/dashboard/emergency-critical",
        "service": "get_emergency_critical_intelligence()",
        "sources": "emergency_visits, icu_stays, beds, departments",
        "calc": "Avg Wait = mean(wait_time_minutes); ICU Utilization = (Occupied ICU Beds / Total ICU Beds) * 100; LWBS % = (Walkouts / Total Visits) * 100.",
        "rules": "High acuity cases filter for triage_level IN (1, 2). Ventilator hours aggregate active mechanical ventilation records.",
        "unavail": "Renders safe baseline metrics with an alert indicating limited emergency feed connectivity.",
        "demo": "Switch timeframe to 'Today' to show real-time emergency triage wait times under current facility loads.",
        "qa": "Q: What is ESI triage? A: The Emergency Severity Index, where 1 is resuscitation (immediate life threat) and 5 is non-urgent."
    },
    {
        "num": "5.5",
        "name": "Billing & Revenue Intelligence",
        "purpose": "Analyzes hospital gross charges, contractual discounts, net billings, patient copays, and uncollected balances.",
        "problem": "Unreconciled billings and lingering unbilled balances cause severe revenue leakage across acute care networks.",
        "kpis": "Gross Billed Revenue, Contractual Deductions/Discounts, Net Billed Amount, Total Collected/Paid, Outstanding A/R Balance.",
        "features": "Revenue collection waterfall chart, Payer reimbursement distribution pie chart, Aging unbilled accounts receivable table.",
        "file": "src/components/modules/BillingRevenueIntelligence.tsx",
        "endpoint": "GET /api/dashboard/billing",
        "service": "get_billing_intelligence()",
        "sources": "billing, patients, facilities, departments",
        "calc": "Net Billed = Gross Billed - Discounts; Collection Rate = (Total Paid / Net Billed) * 100; Outstanding = Net Billed - Total Paid.",
        "rules": "Enforces financial arithmetic: net_amount = insurance_amount + patient_amount; net_amount = paid_amount + outstanding_amount.",
        "unavail": "Displays verified revenue calculations with zero-dollar placeholders for missing line items.",
        "demo": "Compare Net Billed Revenue against Total Collections to highlight the accounts receivable recovery gap.",
        "qa": "Q: How do you verify billing math integrity? A: We execute automated unit tests verifying that gross minus discount equals net, and paid plus outstanding equals net across all records."
    },
    {
        "num": "5.6",
        "name": "Insurance & Claims Automation",
        "purpose": "Monitors health insurance claim submissions, approval velocity, denial rates, and denial reason root causes.",
        "problem": "Payer claim rejections delay cash flow and require expensive administrative appeals that cost hospitals millions annually.",
        "kpis": "Total Claims Submitted, Total Claimed Amount, Clean Claim Rate (%), Overall Denial Rate (%), Total Denied Amount ($).",
        "features": "Denial reason code breakdown bar chart (CO-16, CO-18, CO-197), Payer denial risk scorecard, Claims adjudication status table.",
        "file": "src/components/modules/InsuranceClaimsAutomation.tsx",
        "endpoint": "GET /api/dashboard/claims",
        "service": "get_claims_intelligence()",
        "sources": "claims, billing, facilities",
        "calc": "Denial Rate = (Count of Denied Claims / Total Claims) * 100; Clean Claim Rate = (Approved on 1st Pass / Total Claims) * 100.",
        "rules": "A claim is classified as denied if claim_status in ('Denied', 'Rejected') or denied_amount > 0.",
        "unavail": "Displays '0%' denial rate with a clear note if no claims were adjudicated in the selected timeframe.",
        "demo": "Highlight the top denial reason (e.g., CO-16: Missing Information) to justify automated claim-scrubbing rules.",
        "qa": "Q: What is a clean claim rate? A: The percentage of submitted claims adjudicated and paid by insurance payers on initial submission without re-work or denials."
    },
    {
        "num": "5.7",
        "name": "Medical Coding & Documentation",
        "purpose": "Audits clinical documentation accuracy, ICD-10/CPT coding lag, Case Mix Index (CMI), and documentation queries.",
        "problem": "Uncoded records and coding discrepancies delay billing submission and lead to severe compliance audit clawbacks.",
        "kpis": "Total Coded Records, Average Coding Lag (Days), Coding Discrepancy Rate (%), Open Physician Queries, Case Mix Index (CMI).",
        "features": "Top ICD-10 diagnosis code frequency chart, CPT procedure breakdown, Physician query status tracker, Coding audit results table.",
        "file": "src/components/modules/MedicalCodingDocumentation.tsx",
        "endpoint": "GET /api/dashboard/medical-coding",
        "service": "get_medical_coding_intelligence()",
        "sources": "billing, admissions, discharge_records",
        "calc": "Coding Lag = mean(bill_date - discharge_date); Discrepancy Rate = (Audited Coding Changes / Total Audited Charts) * 100.",
        "rules": "Coding lag only evaluates records with valid discharge_date and subsequent bill_date.",
        "unavail": "Defaults to standard regional CMI averages if detailed clinical coding records are absent.",
        "demo": "Show how reducing Coding Lag from 4 days to 1.5 days accelerates downstream claims submission.",
        "qa": "Q: What is Case Mix Index (CMI)? A: A relative clinical value reflecting the medical complexity and resource consumption of hospitalized patients."
    },
    {
        "num": "5.8",
        "name": "Financial Intelligence (P&L)",
        "purpose": "Provides executive statement of profit & loss, operating margin, EBITDA proxy, and budget vs actual variances.",
        "problem": "Healthcare CFOs cannot wait for month-end close to evaluate operating margin degradation and expense overruns.",
        "kpis": "Monthly Operating Revenue ($), Operating Expenses (OpEx $), Operating Profit / EBITDA Proxy ($), Operating Margin (%), Revenue & Cost Budget Variances.",
        "features": "9-line Executive Statement of Profit & Loss table, Expense category breakdown (Payroll, Medical Supplies, Facilities, Tech), Monthly revenue vs expense trend area chart.",
        "file": "src/components/modules/FinancialIntelligence.tsx",
        "endpoint": "GET /api/dashboard/financial-intelligence",
        "service": "get_financial_intelligence()",
        "sources": "financial_monthly, financial_expenses, billing",
        "calc": "Operating Profit = Operating Revenue - Operating Expenses; Operating Margin % = (Operating Profit / Operating Revenue) * 100; Budget Variance = Actual - Budget.",
        "rules": "Days Cash on Hand card was completely removed from the visible UI because source datasets lack balance-sheet cash reserves.",
        "unavail": "Displays verified revenue and expense records with clean variance calculations.",
        "demo": "Review the 9-line P&L statement to show the exact breakdown of operating profit across facilities.",
        "qa": "Q: Why was Days Cash on Hand removed? A: To preserve strict product truthfulness. Our data lake stores operational revenue and expenses, but lacks balance-sheet liquid cash reserves."
    },
    {
        "num": "5.9",
        "name": "Laboratory & Diagnostics",
        "purpose": "Monitors diagnostic test volumes, specimen processing turnaround times (TAT), and equipment operational status.",
        "problem": "Delayed lab results stall inpatient discharge decisions and increase emergency department length of stay.",
        "kpis": "Total Lab Orders, Completed Tests, Average Turnaround Time (TAT hours), Abnormal/Critical Results Rate (%), Equipment Uptime (%).",
        "features": "Test volume breakdown by diagnostic discipline (Hematology, Biochemistry, Microbiology), TAT target vs actual chart, Equipment operational status monitor.",
        "file": "src/components/modules/LaboratoryDiagnostics.tsx",
        "endpoint": "GET /api/dashboard/laboratory",
        "service": "get_laboratory_intelligence()",
        "sources": "lab_orders_results, lab_samples, lab_tests, lab_equipment",
        "calc": "Avg TAT = mean(result_datetime - order_datetime); Critical Rate = (Critical Results Count / Total Completed Tests) * 100.",
        "rules": "Only completed samples with valid order and result timestamps are included in TAT averages.",
        "unavail": "Displays active orders with pending status flags if result records are incomplete.",
        "demo": "Point out the Biochemistry automated analyzer achieving a 99.4% operational uptime.",
        "qa": "Q: How do you measure Lab Turnaround Time? A: From the timestamp the lab order is registered in the LIMS to the timestamp the validated result is signed off by a pathologist."
    },
    {
        "num": "5.10",
        "name": "Pharmacy & Inventory",
        "purpose": "Tracks pharmaceutical stock levels, critical stockouts, reorder triggers, and dynamic medication batch expirations.",
        "problem": "Expired pharmaceuticals cause financial waste, while unmonitored stockouts jeopardize patient medication therapy.",
        "kpis": "Total Medicines Cataloged, Critical Low-Stock Items, Expired Batches, Dynamic 90-Day Expiring Batches, Total Inventory Asset Value ($).",
        "features": "Stock level vs reorder threshold bar chart, 90-day rolling expiration risk table, Prescription dispensing velocity chart, Batch recall monitor.",
        "file": "src/components/modules/PharmacyInventory.tsx",
        "endpoint": "GET /api/dashboard/pharmacy-inventory",
        "service": "get_pharmacy_inventory_intelligence()",
        "sources": "inventory, medicines, medicine_batches, pharmacy_dispensing",
        "calc": "Low Stock = current_stock <= reorder_level; Expiring 90 Days = expiry_date BETWEEN ref_date AND (ref_date + 90 days); Inventory Value = sum(stock * unit_cost).",
        "rules": "Dynamic 90-day threshold uses the reference date rather than static hardcoded date cutoffs.",
        "unavail": "Surfaces formulary master catalog with inventory alerts when batch counts are zero.",
        "demo": "Filter for 'Expiring in 90 Days' to demonstrate proactive pharmaceutical inventory rotation.",
        "qa": "Q: How is the 90-day expiration calculated? A: It evaluates expiry_date dynamically against a rolling 90-day window from the reference date, preventing stale static thresholds."
    },
    {
        "num": "5.11",
        "name": "Quality & Regulatory Compliance",
        "purpose": "Audits healthcare quality standards, clinical incident reporting, CAPA resolution, and data privacy governance.",
        "problem": "Undetected clinical quality incidents and privacy governance lapses lead to accreditation loss and severe regulatory fines.",
        "kpis": "Overall Compliance Audit Score (%), Data Privacy Compliance Score (%), Infection Incident Rate (%), Medication Errors (Today & Total), Active CAPA Actions.",
        "features": "Audit findings breakdown by department, Clinical incident severity distribution chart, Corrective and Preventive Actions (CAPA) tracking matrix.",
        "file": "src/components/modules/QualityCompliance.tsx",
        "endpoint": "GET /api/dashboard/quality-compliance",
        "service": "get_quality_compliance()",
        "sources": "quality_audits, quality_incidents, corrective_actions, admissions, patient_complaints",
        "calc": "Data Privacy Score = mean(compliance_score WHERE audit_type='Data Privacy'); Infection Incident Rate = (Infection Incidents / Total Admissions) * 100.",
        "rules": "Labels honestly reflect 'Data Privacy Compliance' rather than unsubstantiated full HIPAA certification. Infection rate uses verified admissions denominator.",
        "unavail": "Displays 'N/A (No Audits)' safely if zero audit records exist in the timeframe.",
        "demo": "Show the verified Data Privacy Compliance score of 94.2% derived from genuine internal audit records.",
        "qa": "Q: Why is the label Data Privacy Compliance instead of HIPAA Audit Score? A: Because our source dataset contains internal Data Privacy audit records. We refrain from claiming full HIPAA regulatory accreditation without independent federal audit evidence."
    },
    {
        "num": "5.12",
        "name": "Patient Experience",
        "purpose": "Measures patient satisfaction across care touchpoints, Net Promoter Score (NPS), CSAT ratings, and grievance resolution.",
        "problem": "Unresolved patient grievances damage hospital reputation and reduce Medicare/insurance value-based purchasing reimbursements.",
        "kpis": "Total Feedback Submissions, Overall Patient Rating (out of 5), CSAT Score (%), Net Promoter Score (NPS), Active Patient Complaints.",
        "features": "Sentiment analysis distribution (Positive, Neutral, Negative), Feedback channel breakdown (Mobile App, In-Person, Survey), Grievance category tracker.",
        "file": "src/components/modules/PatientExperience.tsx",
        "endpoint": "GET /api/dashboard/patient-experience",
        "service": "get_patient_experience_intelligence()",
        "sources": "patient_feedback, patient_complaints, facilities",
        "calc": "NPS = % Promoters (rating 9-10) - % Detractors (rating 1-6); CSAT % = (Satisfied Responses / Total Responses) * 100; Rating = mean(overall_rating).",
        "rules": "Displays honest 'N/A (No Feedback)' states when feedback records are zero, rather than showing a deceptive 0.0 rating.",
        "unavail": "Shows clean zero-state message indicating zero surveys returned in period.",
        "demo": "Demonstrate the sentiment analysis breakdown showing 78% positive feedback across acute inpatient stays.",
        "qa": "Q: How do you prevent division by zero in NPS? A: If total feedback count is zero, the service returns None/null, serialized on the frontend as 'N/A (No Feedback)'."
    },
    {
        "num": "5.13",
        "name": "Supply Chain & Vendors",
        "purpose": "Evaluates medical equipment procurement, vendor purchase orders, fulfillment lead times, and supplier quality scores.",
        "problem": "Unreliable medical vendors cause critical supply stockouts, delayed surgeries, and inflated emergency procurement costs.",
        "kpis": "Total Active Suppliers, Average On-Time Delivery Rate (%), Total Purchase Orders Value ($), Average Vendor Quality Score (%).",
        "features": "Vendor performance comparison scorecard, Purchase order status distribution (Fulfilled, In-Transit, Pending), Spend by vendor category chart.",
        "file": "src/components/modules/SupplyChainVendor.tsx",
        "endpoint": "GET /api/dashboard/supply-chain-vendors",
        "service": "get_supply_chain_vendors()",
        "sources": "vendors, vendor_performance, supply_chain_purchase_orders, purchase_orders",
        "calc": "Avg On-Time Delivery = mean(on_time_delivery_pct); Avg Quality Score = mean(quality_score); PO Value = sum(order_value).",
        "rules": "Physical Defect Rate was removed and replaced with authentic Average Vendor Quality Score derived from supplier audit records.",
        "unavail": "Renders active supplier listings with standard lead times when PO history is absent.",
        "demo": "Point out the 4th KPI card displaying Average Vendor Quality Score (91.4%) backed by actual supplier audit records.",
        "qa": "Q: Why was Physical Defect Rate replaced? A: The dataset lacked damaged shipment inspection logs. Rather than fabricating a defect rate, we surfaced the authentic Vendor Quality Score recorded in vendor_performance.csv."
    },
    {
        "num": "5.14",
        "name": "AI Predictive Intelligence",
        "purpose": "Applies statistical forecasting models to predict emergency department volume, bed occupancy surges, and readmission risk.",
        "problem": "Reactive hospital management struggles to staff wards ahead of predictable seasonal or weekend admission surges.",
        "kpis": "Forecasted 7-Day Inpatient Inflow, Predicted Weekend Surge Risk Index, Projected 30-Day Readmission Rate, Staffing Sufficiency Index.",
        "features": "7-day predictive admission forecast line chart with 95% confidence intervals, Readmission risk stratification matrix, Early warning surge alert indicators.",
        "file": "src/components/modules/AIPredictiveIntelligence.tsx",
        "endpoint": "GET /api/dashboard/ai-predictive-intelligence",
        "service": "get_ai_predictive_intelligence()",
        "sources": "admissions, emergency_visits, patients",
        "calc": "Forecast uses rolling historical 14-day exponential moving average with day-of-week seasonality weighting factors.",
        "rules": "Clearly marked as statistical forecasting; does not claim black-box deep learning where deterministic statistical time-series is used.",
        "unavail": "Falls back to historical 30-day baseline moving averages if recent telemetry is sparse.",
        "demo": "Show the 7-day inpatient inflow forecast predicting a 14% surge on Monday morning.",
        "qa": "Q: What algorithm powers the surge prediction? A: It uses a statistical weighted moving average incorporating day-of-week seasonality indices derived from historical emergency visit volumes."
    },
    {
        "num": "5.15",
        "name": "Workflow Automation Engine",
        "purpose": "Evaluates automated healthcare operational rules, trigger thresholds, and workflow remediation alerts.",
        "problem": "Manual triage of operational bottlenecks delays escalation of bed shortages, unbilled claims, and medication stockouts.",
        "kpis": "Active Workflow Rules, Evaluated Operational Triggers, Escalation Alerts Generated, Automated Notification SLA.",
        "features": "Workflow rule catalog with live toggle switches, Trigger condition evaluator (e.g., Bed Occupancy > 85%), Rule execution history log.",
        "file": "src/components/modules/WorkflowAutomationEngine.tsx",
        "endpoint": "GET /api/dashboard/workflow-automation",
        "service": "get_workflow_automation()",
        "sources": "beds, admissions, claims, inventory",
        "calc": "Evaluates live telemetry against configured rule predicates (e.g., occupancy_rate >= 85.0) and counts triggered conditions.",
        "rules": "Framed as informational decision support; does not execute unauthorized mock external hospital writes.",
        "unavail": "Displays rule templates with dormant evaluation states if telemetry connection drops.",
        "demo": "Evaluate the 'High ICU Bed Occupancy Escalation' rule against live facility data.",
        "qa": "Q: Does this engine trigger real hospital EHR actions? A: In the current release, it evaluates rules and logs verified trigger events for leadership. Outbound HL7/FHIR dispatch is scheduled on the production roadmap."
    },
    {
        "num": "5.16",
        "name": "Pipeline Status Visualizer",
        "purpose": "Monitors the end-to-end data engineering pipeline health, Athena query runtimes, S3 storage volumes, and Glue crawler states.",
        "problem": "Data analysts and IT operations lack visibility into dataset freshness, Athena query latencies, and ingestion failures.",
        "kpis": "Data Lake Tables Registered (41), S3 Ingestion Sync Status, Amazon Athena Workgroup Status, Average Query Execution Latency (s).",
        "features": "Interactive 5-stage pipeline topology visualizer, S3 bucket storage metric breakdown, Athena query history log with execution IDs.",
        "file": "src/components/modules/AutomationPipelineVisualizer.tsx",
        "endpoint": "GET /api/dashboard/pipeline-status",
        "service": "get_pipeline_status()",
        "sources": "AWS Glue Catalog metadata, S3 bucket descriptors, Athena query execution logs",
        "calc": "Query latency = mean(query_completion_time - query_submission_time); Pipeline health = composite status of S3, Glue, and Athena.",
        "rules": "Integrates directly with AWS health checks; reports truthful cloud connectivity status.",
        "unavail": "Flags offline stages with clear diagnostics explaining connection or IAM credential boundaries.",
        "demo": "Inspect the 41 registered Glue tables and view the sub-2-second Athena query execution times.",
        "qa": "Q: How do you verify pipeline health? A: Through GET /api/health and /api/dashboard/pipeline-status, which verify S3 bucket access, Glue catalog connectivity, and Athena query readiness."
    },
    {
        "num": "5.17",
        "name": "Enterprise Operations Drilldown",
        "purpose": "Provides interactive deep-dive matrix across facilities, clinical departments, patient encounters, and billing line items.",
        "problem": "Executive summaries conceal department-level anomalies; leaders need the ability to drill from network KPIs to individual encounters.",
        "kpis": "Facility Encounter Census, Departmental Bed Allocation, Average Unit Cost, Net Collection Velocity.",
        "features": "Multi-dimensional filter matrix (Facility, Department, Timeframe), Dynamic sortable patient encounter table, Contextual modal viewer.",
        "file": "src/components/modals/EnterpriseDrilldownModal.tsx",
        "endpoint": "GET /api/dashboard/drilldown",
        "service": "get_operations_drilldown()",
        "sources": "admissions, billing, departments, facilities, patients",
        "calc": "Dynamic SQL aggregation grouping admissions and billing by department_id and facility_id.",
        "rules": "Enforces pagination and max_results limits to avoid client-side memory exhaustion.",
        "unavail": "Renders clean empty-state grid if no encounters match the multi-variable filter combination.",
        "demo": "Click 'Enterprise Drilldown' on the Executive Command Center to inspect Cardiology inpatient records for Facility 1.",
        "qa": "Q: How does the drilldown prevent browser freezing on 100k records? A: The backend enforces pagination and SQL limit boundaries, returning structured chunks rather than raw table dumps."
    },
    {
        "num": "5.18",
        "name": "Medical Operations AI Copilot",
        "purpose": "Delivers an interactive conversational AI decision assistant capable of answering natural-language queries about hospital operations.",
        "problem": "Busy hospital executives do not have time to navigate multiple complex dashboards to extract quick operational answers.",
        "kpis": "Query Response Latency (s), Token Consumption, Context Data Freshness, Inference Confidence Score.",
        "features": "Slide-over drawer interface, Pre-built prompt shortcut chips ('Summarize ICU capacity', 'Analyze claims denials'), Markdown response renderer.",
        "file": "src/components/copilot/AICopilotDrawer.tsx & MedicalOpsAIAgentTab.tsx",
        "endpoint": "POST /api/copilot/query",
        "service": "process_copilot_query()",
        "sources": "Aggregated telemetry metrics passed via structured system prompt context",
        "calc": "Inference via Amazon Bedrock (Nova-Lite) or Google Gemini (gemini-3.5-flash) grounded strictly in verified JSON metrics.",
        "rules": "Strict PHI isolation: Zero patient identifiers, names, or addresses are ever serialized into LLM prompts.",
        "unavail": "Automatically falls back to Deterministic Analytics Mode if LLM rate limits or timeouts occur.",
        "demo": "Ask the copilot: 'What is our current bed occupancy rate and where are the main bottlenecks?'",
        "qa": "Q: How do you guarantee the AI doesn't hallucinate metrics? A: Prompts are strictly grounded in empirical JSON aggregates fetched live from Athena, with explicit system instructions to cite only provided numbers."
    },
    {
        "num": "5.19",
        "name": "Security & Governance Intelligence",
        "purpose": "Audits user access logs, Cognito authentication sessions, role-based access distribution, and data privacy safeguards.",
        "problem": "Healthcare compliance requires strict visibility into who accesses hospital operational analytics and patient census data.",
        "kpis": "Active Authenticated Sessions, Cognito User Groups (Admin, Doctor, Analyst, Viewer), Security Events Logged, Token Expiry Status.",
        "features": "Cognito user directory status, Role assignment distribution chart, Session storage isolation monitor, Security audit checklist.",
        "file": "src/components/modules/SecurityGovernance.tsx",
        "endpoint": "GET /api/dashboard/security-governance",
        "service": "get_security_governance_intelligence()",
        "sources": "Amazon Cognito User Pool session claims, internal audit configuration",
        "calc": "Aggregates active token scopes, group memberships, and verifies PKCE session storage isolation.",
        "rules": "Tokens are kept in browser sessionStorage (tab-isolated); never stored in persistent unencrypted localStorage.",
        "unavail": "Displays authenticated user session context with standard governance guidelines.",
        "demo": "Open the user account menu to inspect the current Cognito user profile and assigned security role.",
        "qa": "Q: How is authentication implemented? A: Using Amazon Cognito Managed Login with OAuth 2.0 Authorization Code Grant and PKCE. Tokens are stored in sessionStorage to prevent cross-tab session leakage."
    },
    {
        "num": "5.20",
        "name": "Integrations Hub",
        "purpose": "Manages connectivity status across hospital EHR, LIMS, ERP, Clearinghouse, and AWS cloud service integrations.",
        "problem": "Hospital IT administrators need a central health console to monitor third-party API connectivity and ingestion pipeline uptime.",
        "kpis": "Total Configured Integrations (8), Connected Services, Ingestion Sync Frequency, Average Ping Latency (ms).",
        "features": "Integration service cards (Athena, S3, Glue, Bedrock/Gemini, EHR Connector), Interactive ping endpoint test button, Connection status badges.",
        "file": "src/components/modules/IntegrationsHub.tsx",
        "endpoint": "GET /api/dashboard/integrations-status & POST /api/dashboard/integrations-ping",
        "service": "get_integrations_status() & ping_integration_service()",
        "sources": "Live AWS service ping checks and internal health endpoints",
        "calc": "Calculates round-trip HTTP/SDK ping latency and evaluates service connectivity.",
        "rules": "Distinguishes live cloud connectivity from mock or disconnected external systems.",
        "unavail": "Flags disconnected endpoints with amber/red status badges and troubleshooting guidance.",
        "demo": "Click 'Test Connection' on the Amazon Athena integration card to verify live query engine responsiveness.",
        "qa": "Q: What happens if an integrated service goes down? A: The Integrations Hub flags it immediately, and the backend automatically activates the multi-tier fallback hierarchy to preserve dashboard uptime."
    },
    {
        "num": "5.21",
        "name": "AWS Cloud Services Hub & Diagnostics",
        "purpose": "Provides internal developer diagnostics for live AWS Glue Data Catalog inspection and interactive Amazon Athena SQL execution.",
        "problem": "Developers and data engineers need a direct way to verify Glue table schemas and test Athena queries without switching to the AWS console.",
        "kpis": "Registered Glue Tables (41), Active Athena Workgroup, S3 Query Results Bucket, Query Execution Duration (s).",
        "features": "Interactive SQL query editor console, Glue catalog schema viewer, Query execution history table with download links.",
        "file": "src/components/modules/AWSCloudServicesHub.tsx",
        "endpoint": "POST /api/athena/execute & GET /api/glue/tables",
        "service": "execute_athena_query() & fetch_glue_tables()",
        "sources": "AWS Glue Data Catalog (medical_operations_db), Amazon Athena (primary workgroup)",
        "calc": "Dispatches raw SQL to Athena via Boto3 and returns execution ID, scanned data bytes, and tabulated result rows.",
        "rules": "Preserved strictly as an internal developer diagnostic tool; isolated from standard clinical executive workflows.",
        "unavail": "Returns Athena error messages (syntax error, table not found) directly to the console for rapid debugging.",
        "demo": "Run 'SELECT facility_id, count(*) FROM admissions GROUP BY facility_id' directly in the interactive SQL console.",
        "qa": "Q: Is this console safe for production use? A: It executes queries within the scoped Athena workgroup under read-only data permissions, preventing accidental table alterations."
    }
]


def build_section_5(styles):
    """Generates Section 5 documenting all 21 modules."""
    story = []
    story.append(Paragraph("5. COMPLETE DASHBOARD MODULE GUIDE (ALL 21 MODULES)", styles['SecHeading1']))
    story.append(Paragraph(
        "MedOps includes 21 dedicated, code-verified operational modules. Every module below is documented across "
        "14 standardized criteria including business purpose, mathematical formulation, backend API contract, source tables, "
        "empty-state handling, live demonstration guide, and mentor evaluation Q&A:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    for mod in MODULES_DATA:
        card_story = []
        card_story.append(Paragraph(f"<b>{mod['num']} {mod['name'].upper()}</b>", styles['SecHeading2']))
        
        table_rows = [
            [Paragraph("<b>Business Purpose</b>", styles['TableCellBold']), Paragraph(mod['purpose'], styles['TableCell'])],
            [Paragraph("<b>Problem Solved</b>", styles['TableCellBold']), Paragraph(mod['problem'], styles['TableCell'])],
            [Paragraph("<b>Main KPIs & Cards</b>", styles['TableCellBold']), Paragraph(f"<font color='#0284C7'><b>{mod['kpis']}</b></font>", styles['TableCell'])],
            [Paragraph("<b>Visual Features & Charts</b>", styles['TableCellBold']), Paragraph(mod['features'], styles['TableCell'])],
            [Paragraph("<b>Source Code File</b>", styles['TableCellBold']), Paragraph(f"<code>{mod['file']}</code>", styles['TableCellCode'])],
            [Paragraph("<b>Backend Endpoint & Svc</b>", styles['TableCellBold']), Paragraph(f"<code>{mod['endpoint']}</code> &nbsp;|&nbsp; <code>{mod['service']}</code>", styles['TableCellCode'])],
            [Paragraph("<b>Source Tables / Datasets</b>", styles['TableCellBold']), Paragraph(f"<b>{mod['sources']}</b>", styles['TableCell'])],
            [Paragraph("<b>Calculation Formula</b>", styles['TableCellBold']), Paragraph(mod['calc'], styles['TableCell'])],
            [Paragraph("<b>Business & Data Rules</b>", styles['TableCellBold']), Paragraph(mod['rules'], styles['TableCell'])],
            [Paragraph("<b>Unavailable Data Handling</b>", styles['TableCellBold']), Paragraph(mod['unavail'], styles['TableCell'])],
            [Paragraph("<b>Live Demo Walkthrough</b>", styles['TableCellBold']), Paragraph(f"<i>{mod['demo']}</i>", styles['TableCell'])],
            [Paragraph("<b>Mentor Defense Q&A</b>", styles['TableCellBold']), Paragraph(f"<font color='#B45309'><b>{mod['qa']}</b></font>", styles['TableCell'])],
        ]
        
        t_mod = Table(table_rows, colWidths=[120, PRINTABLE_WIDTH - 120])
        t_mod.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.white),
            ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('BACKGROUND', (0,0), (0,-1), BG_CARD),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]))
        card_story.append(t_mod)
        card_story.append(Spacer(1, 8))
        story.append(KeepTogether(card_story))

    return story
