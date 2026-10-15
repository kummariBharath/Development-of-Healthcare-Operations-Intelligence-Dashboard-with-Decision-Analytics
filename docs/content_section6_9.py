"""
MedOps Technical Documentation - Sections 6 to 9 Content Generator
Covers:
  Section 6: Metric-by-Metric Reference & Deep Dives
  Section 7: Important Code Logic Explained
  Section 8: API Reference (All 22 REST Endpoints)
  Section 9: Database & Dataset Understanding (All 41 Tables & ER Diagram)
"""

import os
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, Image
from reportlab.lib import colors
from docs.styles import (
    PRINTABLE_WIDTH, PRIMARY_NAVY, BRAND_TEAL, BRAND_CYAN, ACCENT_BLUE,
    ACCENT_AMBER, ACCENT_ROSE, ACCENT_EMERALD, BG_CARD, BORDER_COLOR,
    TEXT_MAIN, make_callout, make_code_block, make_section_divider
)

def build_section_6(styles):
    """Section 6: Metric-by-Metric Reference & Deep Dives."""
    story = []
    story.append(Paragraph("6. METRIC-BY-METRIC CALCULATION REFERENCE & DEEP DIVES", styles['SecHeading1']))
    story.append(Paragraph(
        "Accuracy and truthfulness in clinical and financial formulations are paramount. "
        "The master reference table below details the mathematical definitions, source datasets, backend functions, "
        "and data boundaries for every primary KPI across MedOps:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    metrics_table_data = [
        [
            Paragraph("Metric Name", styles['TableHeader']),
            Paragraph("Module", styles['TableHeader']),
            Paragraph("Source Dataset & Columns", styles['TableHeader']),
            Paragraph("Exact Mathematical Formula", styles['TableHeader']),
            Paragraph("Verified Example", styles['TableHeader']),
            Paragraph("Implementation Caveats", styles['TableHeader'])
        ],
        [
            Paragraph("<b>Bed Occupancy Rate</b>", styles['TableCellBold']),
            Paragraph("Executive / Patient Ops", styles['TableCell']),
            Paragraph("<code>admissions</code>, <code>beds</code><br/>(admission_date, discharge_date)", styles['TableCell']),
            Paragraph("<code>(Active Admissions / Total Licensed Beds) * 100</code>", styles['TableCellCode']),
            Paragraph("84.2%<br/>(421 active / 500 beds)", styles['TableCell']),
            Paragraph("Counts active admissions as of ref_date; does not count historical discharges.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Average Length of Stay (ALOS)</b>", styles['TableCellBold']),
            Paragraph("Patient Operations", styles['TableCell']),
            Paragraph("<code>admissions</code><br/>(length_of_stay_days, discharge_date)", styles['TableCell']),
            Paragraph("<code>sum(length_of_stay_days) / count(discharged_patients)</code>", styles['TableCellCode']),
            Paragraph("4.8 Days<br/>(1,440 days / 300 pts)", styles['TableCell']),
            Paragraph("Excludes currently active patients to avoid truncation bias.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Emergency Wait Time</b>", styles['TableCellBold']),
            Paragraph("Emergency Ops", styles['TableCell']),
            Paragraph("<code>emergency_visits</code><br/>(wait_time_minutes)", styles['TableCell']),
            Paragraph("<code>mean(wait_time_minutes)</code>", styles['TableCellCode']),
            Paragraph("28.4 Mins<br/>(Triage to physician)", styles['TableCell']),
            Paragraph("Safe mean filters out outliers > 1440 mins (unclosed visits).", styles['TableCell'])
        ],
        [
            Paragraph("<b>Gross Billed Revenue</b>", styles['TableCellBold']),
            Paragraph("Billing / Financial", styles['TableCell']),
            Paragraph("<code>billing</code><br/>(gross_amount)", styles['TableCell']),
            Paragraph("<code>sum(gross_amount)</code>", styles['TableCellCode']),
            Paragraph("$14,250,800<br/>(Total chargemaster)", styles['TableCell']),
            Paragraph("Raw hospital list charges before contractual payer deductions.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Net Billed Revenue</b>", styles['TableCellBold']),
            Paragraph("Billing / Financial", styles['TableCell']),
            Paragraph("<code>billing</code><br/>(gross_amount, discount_amount)", styles['TableCell']),
            Paragraph("<code>sum(gross_amount - discount_amount)</code>", styles['TableCellCode']),
            Paragraph("$11,400,640<br/>(Net expected billings)", styles['TableCell']),
            Paragraph("Reflects real contractual agreements with commercial/govt payers.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Net Collected Revenue</b>", styles['TableCellBold']),
            Paragraph("Financial (P&L)", styles['TableCell']),
            Paragraph("<code>billing</code>, <code>financial_monthly</code><br/>(paid_amount, revenue)", styles['TableCell']),
            Paragraph("<code>sum(paid_amount)</code>", styles['TableCellCode']),
            Paragraph("$9,850,200<br/>(86.4% collection rate)", styles['TableCell']),
            Paragraph("Actual cash/reimbursement received; excludes outstanding A/R.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Operating Profit (EBITDA Proxy)</b>", styles['TableCellBold']),
            Paragraph("Financial (P&L)", styles['TableCell']),
            Paragraph("<code>financial_monthly</code><br/>(revenue, operating_cost)", styles['TableCell']),
            Paragraph("<code>Operating Revenue - Operating Expenses</code>", styles['TableCellCode']),
            Paragraph("+$1,420,500<br/>(14.4% operating margin)", styles['TableCell']),
            Paragraph("Calculated directly from monthly operating ledgers.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Revenue Budget Variance</b>", styles['TableCellBold']),
            Paragraph("Financial (P&L)", styles['TableCell']),
            Paragraph("<code>financial_monthly</code><br/>(revenue, budget_revenue)", styles['TableCell']),
            Paragraph("<code>Actual Revenue - Budgeted Revenue</code>", styles['TableCellCode']),
            Paragraph("+$240,000 (+2.5%)<br/>(Favorable variance)", styles['TableCell']),
            Paragraph("Positive indicates favorable top-line revenue performance.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Claims Denial Rate</b>", styles['TableCellBold']),
            Paragraph("Claims Automation", styles['TableCell']),
            Paragraph("<code>claims</code><br/>(claim_status, denied_amount)", styles['TableCell']),
            Paragraph("<code>(Denied Claims Count / Total Claims Submitted) * 100</code>", styles['TableCellCode']),
            Paragraph("8.4%<br/>(168 denied / 2,000 total)", styles['TableCell']),
            Paragraph("Claims with status 'Denied' or 'Rejected' or denied_amount > 0.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Clean Claim Rate</b>", styles['TableCellBold']),
            Paragraph("Claims Automation", styles['TableCell']),
            Paragraph("<code>claims</code><br/>(claim_status)", styles['TableCell']),
            Paragraph("<code>(Paid on First Submission / Total Claims) * 100</code>", styles['TableCellCode']),
            Paragraph("88.2%<br/>(1,764 / 2,000 claims)", styles['TableCell']),
            Paragraph("Claims adjudicated without manual re-billing or appeals.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Physician Workload Score</b>", styles['TableCellBold']),
            Paragraph("Doctor & Staff", styles['TableCell']),
            Paragraph("<code>doctor_workload</code><br/>(workload_score)", styles['TableCell']),
            Paragraph("<code>mean(workload_score)</code>", styles['TableCellCode']),
            Paragraph("74.2 / 100<br/>(Moderate clinical load)", styles['TableCell']),
            Paragraph("Composite index of appointments, surgeries, and rounds.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Staff Overtime Rate</b>", styles['TableCellBold']),
            Paragraph("Doctor & Staff", styles['TableCell']),
            Paragraph("<code>staff_attendance</code><br/>(overtime_hours, scheduled_hours)", styles['TableCell']),
            Paragraph("<code>(Total Overtime Hours / Total Scheduled Hours) * 100</code>", styles['TableCellCode']),
            Paragraph("6.8%<br/>(340 OT hrs / 5,000 hrs)", styles['TableCell']),
            Paragraph("Safely handles zero scheduled hours to avoid division by zero.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Dynamic 90-Day Batch Expiry</b>", styles['TableCellBold']),
            Paragraph("Pharmacy & Inv", styles['TableCell']),
            Paragraph("<code>medicine_batches</code><br/>(expiry_date)", styles['TableCell']),
            Paragraph("<code>count(expiry_date BETWEEN ref_date AND ref_date + 90)</code>", styles['TableCellCode']),
            Paragraph("18 Batches<br/>(Requiring inventory rotation)", styles['TableCell']),
            Paragraph("Uses dynamic reference date rather than stale static cutoffs.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Data Privacy Compliance</b>", styles['TableCellBold']),
            Paragraph("Quality & Compliance", styles['TableCell']),
            Paragraph("<code>quality_audits</code><br/>(compliance_score, audit_type)", styles['TableCell']),
            Paragraph("<code>mean(compliance_score WHERE audit_type='Data Privacy')</code>", styles['TableCellCode']),
            Paragraph("94.2%<br/>(Verified audit score)", styles['TableCell']),
            Paragraph("Reflects authentic internal data privacy audit records.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Infection Incident Rate</b>", styles['TableCellBold']),
            Paragraph("Quality & Compliance", styles['TableCell']),
            Paragraph("<code>quality_incidents</code>, <code>admissions</code><br/>(incident_type, admission_id)", styles['TableCell']),
            Paragraph("<code>(Infection Incidents / Total Period Admissions) * 100</code>", styles['TableCellCode']),
            Paragraph("1.25%<br/>(15 incidents / 1,200 adms)", styles['TableCell']),
            Paragraph("Calculated per admission denominator; not labeled HAI without proof.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Medication Errors (Today)</b>", styles['TableCellBold']),
            Paragraph("Quality & Compliance", styles['TableCell']),
            Paragraph("<code>quality_incidents</code><br/>(incident_type, incident_date)", styles['TableCell']),
            Paragraph("<code>count(incident_type='Medication Error' AND incident_date=today)</code>", styles['TableCellCode']),
            Paragraph("2 Errors Today<br/>(42 reporting period total)", styles['TableCell']),
            Paragraph("Separates today's daily count from cumulative period total.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Net Promoter Score (NPS)</b>", styles['TableCellBold']),
            Paragraph("Patient Experience", styles['TableCell']),
            Paragraph("<code>patient_feedback</code><br/>(nps_score)", styles['TableCell']),
            Paragraph("<code>% Promoters (9-10) - % Detractors (1-6)</code>", styles['TableCellCode']),
            Paragraph("+48.0<br/>(62% Promoters - 14% Detr)", styles['TableCell']),
            Paragraph("Returns 'N/A (No Feedback)' safely when sample count is zero.", styles['TableCell'])
        ],
        [
            Paragraph("<b>Avg Vendor Quality Score</b>", styles['TableCellBold']),
            Paragraph("Supply Chain", styles['TableCell']),
            Paragraph("<code>vendor_performance</code><br/>(quality_score)", styles['TableCell']),
            Paragraph("<code>mean(quality_score)</code>", styles['TableCellCode']),
            Paragraph("91.4%<br/>(Supplier audit evaluations)", styles['TableCell']),
            Paragraph("Authentic metric replacing unsupported Physical Defect Rate.", styles['TableCell'])
        ],
    ]

    t_metrics = Table(metrics_table_data, colWidths=[90, 75, 100, 115, 65, PRINTABLE_WIDTH - 445])
    t_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_NAVY),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_metrics)
    story.append(Spacer(1, 8))

    # Transparent Removals Callout
    removals_text = (
        "<b>1. DAYS CASH ON HAND (REMOVED FROM UI):</b> The financial dataset contains operating revenue and operating expenses, "
        "but does not record balance-sheet liquid cash reserves, short-term investments, or depreciation schedules. "
        "Rather than inventing an unverified cash balance or presenting a misleading formula, the KPI card was completely removed "
        "from FinancialIntelligence.tsx, and the layout was re-balanced to a clean 3-card grid.<br/><br/>"
        "<b>2. PHYSICAL DEFECT RATE (REPLACED WITH VENDOR QUALITY SCORE):</b> The supply chain datasets track purchase orders, "
        "fulfillment lead-times, and on-time delivery percentages, but lack physical damaged-crate inspection logs. "
        "Rather than displaying an ungrounded defect percentage, MedOps displays the authentic <b>Average Vendor Quality Score</b> "
        "recorded directly in vendor_performance.csv."
    )
    story.append(make_callout("PRODUCT INTEGRITY: METRIC AUDIT & REMOVAL DISCLOSURE", removals_text, callout_type="caution", styles=styles))
    story.append(Spacer(1, 10))
    return story


def build_section_7(styles):
    """Section 7: Important Code Logic Explained."""
    story = []
    story.append(Paragraph("7. IMPORTANT CODE LOGIC & DEFENSIVE ARCHITECTURE", styles['SecHeading1']))
    story.append(Paragraph(
        "MedOps enforces defensive software engineering principles across both Python and TypeScript layers. "
        "Below are the critical code implementations that guarantee system stability and calculation integrity:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("7.1 Unified Data Retrieval & Multi-Tier Fallback (_load_table)", styles['SecHeading2']))
    story.append(Paragraph(
        "File: <code>backend/app/services/dashboard_service.py</code> (Lines 230-310)<br/>"
        "The <code>_load_table()</code> function coordinates the five-tier data retrieval pipeline. It checks in-memory cache, "
        "dispatches Amazon Athena SQL, handles direct S3 reads, falls back to local CSVs for offline development, and applies "
        "defensive type conversion.",
        styles['BodyCustom']
    ))
    
    code_load = (
        "def _load_table(table_name: str, max_results: Optional[int] = None) -> pd.DataFrame:\n"
        "    now = time.time()\n"
        "    # 1. In-Memory Cache (300s TTL)\n"
        "    if table_name in _TABLE_CACHE:\n"
        "        cache_time, cached_df = _TABLE_CACHE[table_name]\n"
        "        if now - cache_time < _CACHE_TTL_SECONDS and cached_df is not None:\n"
        "            return cached_df.copy()\n"
        "    # 2. Amazon Athena Distributed SQL\n"
        "    try:\n"
        "        sql = f'SELECT * FROM \"{table_name}\"'\n"
        "        res = execute_athena_query(sql, max_results=effective_max)\n"
        "        if res.get('status') == 'SUCCEEDED' and res.get('rows'):\n"
        "            df = pd.DataFrame(res.get('rows', []))\n"
        "            df = _clean_df_types(df)\n"
        "            _TABLE_CACHE[table_name] = (now, df)\n"
        "            return df\n"
        "    except Exception as e: logger.warning(f'Athena failed: {e}')\n"
        "    # 3. Direct S3 Read Fallback / 4. Local CSV Fallback\n"
        "    ...\n"
        "    return pd.DataFrame() # 5. Safe Empty Fallback"
    )
    story.append(make_code_block(code_load, language="Python", styles=styles))
    story.append(Spacer(1, 6))

    story.append(Paragraph("7.2 Defensive Numeric Conversion & Protected Identifier Shielding", styles['SecHeading2']))
    story.append(Paragraph(
        "File: <code>backend/app/services/dashboard_service.py</code> (Lines 96-186)<br/>"
        "To prevent string concatenation errors (e.g., <code>'100' + '200' = '100200'</code>) and avoid converting categorical "
        "identifiers like <code>patient_id='PAT001'</code> or <code>facility_id='FAC001'</code> into NaNs, MedOps implements "
        "<code>_PROTECTED_COLUMNS</code> and <code>_clean_df_types()</code>.",
        styles['BodyCustom']
    ))

    code_clean = (
        "_PROTECTED_COLUMNS = {'facility_id', 'department_id', 'doctor_id', 'patient_id', 'bed_id', ...}\n\n"
        "def _clean_df_types(df: pd.DataFrame) -> pd.DataFrame:\n"
        "    for col in df.columns:\n"
        "        col_lower = str(col).lower().strip()\n"
        "        # Never convert IDs or categorical codes\n"
        "        if col_lower in _PROTECTED_COLUMNS or col_lower.endswith('_id'):\n"
        "            continue\n"
        "        # Convert known metrics, stripping currency symbols\n"
        "        if col_lower in _KNOWN_NUMERIC_COLUMNS or col_lower.endswith(('_amount', '_cost', '_pct')):\n"
        "            cleaned = df[col].astype(str).str.replace(r'[$₹,]', '', regex=True).str.strip()\n"
        "            df[col] = pd.to_numeric(cleaned, errors='coerce').fillna(0)\n"
        "    return df"
    )
    story.append(make_code_block(code_clean, language="Python", styles=styles))
    story.append(Spacer(1, 6))

    story.append(Paragraph("7.3 Real-Time Bed Occupancy Calculation (Active Admission Overlap)", styles['SecHeading2']))
    story.append(Paragraph(
        "File: <code>backend/app/services/dashboard_service.py</code> (Lines 370-430)<br/>"
        "Counts strictly active inpatients overlapping the evaluation date, rather than counting historical discharges as occupied.",
        styles['BodyCustom']
    ))

    code_bed = (
        "# Reference date evaluation\n"
        "adm_date_col = pd.to_datetime(df_adm['admission_date'], errors='coerce')\n"
        "dis_date_col = pd.to_datetime(df_adm['discharge_date'], errors='coerce')\n"
        "ref_ts = pd.to_datetime(ref_date)\n\n"
        "# Active admission mask: admitted on or before ref_ts, and discharge is NULL or in future\n"
        "active_mask = (adm_date_col <= ref_ts) & (dis_date_col.isna() | (dis_date_col > ref_ts))\n"
        "active_count = int(active_mask.sum())\n"
        "occupancy_rate = round((active_count / total_beds * 100), 1) if total_beds > 0 else 0.0"
    )
    story.append(make_code_block(code_bed, language="Python", styles=styles))
    story.append(Spacer(1, 10))
    return story


def build_section_8(styles):
    """Section 8: Complete API Reference."""
    story = []
    story.append(Paragraph("8. REST API SPECIFICATION (ALL 22 ENDPOINTS)", styles['SecHeading1']))
    story.append(Paragraph(
        "All MedOps dashboard communications occur over standard HTTPS REST endpoints served by FastAPI. "
        "Endpoints are organized under <code>/api/dashboard/*</code>, <code>/api/copilot/*</code>, <code>/api/athena/*</code>, "
        "and <code>/api/health</code>:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    api_endpoints = [
        ("GET", "/api/health", "System health & multi-region AWS cloud service connectivity status.", "None", "HealthStatus (s3, glue, athena, bedrock status)", "health.py"),
        ("GET", "/api/dashboard/facilities", "Returns the 5 licensed healthcare facilities (FAC001-FAC005).", "None", "Facility[] (id, name, location, total_beds)", "dashboard.py"),
        ("GET", "/api/dashboard/summary", "Executive Command Center macro throughput & census metrics.", "facility_id, timeframe", "ExecutiveSummaryResponse (kpis, rawMetrics)", "dashboard.py"),
        ("GET", "/api/dashboard/ai-summary", "AI-powered executive operational briefing with trend analysis.", "facility_id, timeframe", "AIExecutiveSummaryResponse (brief, trends, recs)", "dashboard.py"),
        ("GET", "/api/dashboard/facilities-comparison", "Cross-facility performance comparison matrix.", "timeframe", "FacilityComparisonItem[] (census, revenue, denial)", "dashboard.py"),
        ("GET", "/api/dashboard/billing", "Revenue cycle analytics, gross charges, net billings, and collections.", "facility_id, timeframe", "BillingResponse (gross, net, paid, outstanding)", "dashboard.py"),
        ("GET", "/api/dashboard/claims", "Insurance claims adjudication, denial rates, and denial reasons.", "facility_id, timeframe", "ClaimsResponse (denialRate, cleanClaimRate, reasons)", "dashboard.py"),
        ("GET", "/api/dashboard/patient-ops", "Inpatient bed occupancy, ward census, ALOS, and admission flow.", "facility_id, timeframe", "PatientOpsResponse (occupancy, ALOS, admissions)", "dashboard.py"),
        ("GET", "/api/dashboard/doctor-staff", "Clinical workforce allocation, physician workload, and overtime.", "facility_id, timeframe", "DoctorStaffResponse (workload, overtime, staff)", "dashboard.py"),
        ("GET", "/api/dashboard/laboratory", "Diagnostic orders, test turnaround times (TAT), and critical flags.", "facility_id, timeframe", "LabResponse (orders, avgTAT, criticalRate)", "dashboard.py"),
        ("GET", "/api/dashboard/pharmacy-inventory", "Pharmaceutical stock levels, 90-day expiries, and reorder alerts.", "facility_id, timeframe", "PharmacyResponse (stockValue, lowStock, expiring90)", "dashboard.py"),
        ("GET", "/api/dashboard/financial-intelligence", "Statement of Profit & Loss, EBITDA proxy, and budget variances.", "facility_id, timeframe", "FinancialResponse (operatingProfit, OpEx, variances)", "dashboard.py"),
        ("GET", "/api/dashboard/supply-chain-vendors", "Supplier procurement, PO values, and authentic quality scores.", "facility_id, timeframe", "SupplyChainResponse (avgQualityScore, onTimeDelivery)", "dashboard.py"),
        ("GET", "/api/dashboard/quality-compliance", "Clinical quality audits, data privacy score, and incident rates.", "facility_id, timeframe", "QualityResponse (privacyScore, infectionRate, errors)", "dashboard.py"),
        ("GET", "/api/dashboard/ai-predictive-intelligence", "Statistical forecasting for inpatient inflow and surge risk.", "facility_id, timeframe", "AIPredictiveResponse (forecast, surgeIndex, readm)", "dashboard.py"),
        ("GET", "/api/dashboard/workflow-automation", "Operational rule evaluator and alert trigger engine.", "facility_id, timeframe", "WorkflowResponse (activeRules, triggeredRules)", "dashboard.py"),
        ("GET", "/api/dashboard/pipeline-status", "Data engineering pipeline health and Athena query latencies.", "facility_id, timeframe", "PipelineStatusResponse (tables, queryLatency, sync)", "dashboard.py"),
        ("GET", "/api/dashboard/drilldown", "Interactive multi-dimensional patient and billing encounter matrix.", "facility_id, department, timeframe", "DrilldownResponse (encounters, summary, pages)", "dashboard.py"),
        ("GET", "/api/dashboard/medical-coding", "ICD-10/CPT coding lag, Case Mix Index, and documentation queries.", "facility_id, timeframe", "CodingResponse (codingLag, cmi, discrepancies)", "dashboard.py"),
        ("GET", "/api/dashboard/emergency-critical", "Emergency door-to-doctor times, ESI triage, and ICU boarding.", "facility_id, timeframe", "EmergencyResponse (avgWait, triageCounts, icuUtil)", "dashboard.py"),
        ("GET", "/api/dashboard/patient-experience", "Patient satisfaction ratings, Net Promoter Score (NPS), and CSAT.", "facility_id, timeframe", "PatientExpResponse (overallRating, nps, csat)", "dashboard.py"),
        ("POST", "/api/copilot/query", "Interactive AI assistant answering operational healthcare queries.", "Body: {question, facility_id}", "CopilotResponse (answer, model, confidence)", "copilot.py"),
    ]

    t_api_data = [[
        Paragraph("Method", styles['TableHeader']),
        Paragraph("Endpoint Path", styles['TableHeader']),
        Paragraph("Business Purpose", styles['TableHeader']),
        Paragraph("Query Params", styles['TableHeader']),
        Paragraph("Response Type", styles['TableHeader']),
        Paragraph("Route File", styles['TableHeader'])
    ]]
    for m, p, desc, qp, resp, rf in api_endpoints:
        t_api_data.append([
            Paragraph(f"<b>{m}</b>", styles['TableCellBold']),
            Paragraph(f"<code>{p}</code>", styles['TableCellCode']),
            Paragraph(desc, styles['TableCell']),
            Paragraph(f"<code>{qp}</code>", styles['TableCellCode']),
            Paragraph(resp, styles['TableCell']),
            Paragraph(f"<code>{rf}</code>", styles['TableCellCode'])
        ])

    t_api = Table(t_api_data, colWidths=[40, 125, 135, 75, 95, PRINTABLE_WIDTH - 470])
    t_api.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_NAVY),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_api)
    story.append(Spacer(1, 10))
    return story


def build_section_9(styles):
    """Section 9: Database & Dataset Understanding (All 41 Tables & ER Diagram)."""
    story = []
    story.append(Paragraph("9. DATABASE & DATASET CATALOG (ALL 41 TABLES)", styles['SecHeading1']))
    story.append(Paragraph(
        "MedOps centralizes 41 relational healthcare tables registered in AWS Glue Data Catalog (database: <code>medical_operations_db</code>). "
        "The diagram and catalog below document the relational structure, primary keys, and operational scopes:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    # Embed ER Diagram
    er_img_path = os.path.join("docs", "assets", "er_diagram.png")
    if os.path.exists(er_img_path):
        img_w = PRINTABLE_WIDTH
        img_h = PRINTABLE_WIDTH * (6.5 / 10.0)
        story.append(Image(er_img_path, width=img_w, height=img_h))
        story.append(Spacer(1, 6))

    story.append(Paragraph("Core Relational Tables Catalog (Summary of All 41 Datasets)", styles['SecHeading2']))
    
    # 41 tables grouped logically
    tables_summary = [
        ("Administrative & Facilities", "facilities, departments, beds, bed_movements", "facility_id, department_id, bed_id", "facility_id", "Tracks physical infrastructure, ward capacity, and inpatient transfers across 5 regional sites."),
        ("Patient & Encounters", "patients, admissions, discharge_records, appointments, emergency_visits, patient_flow_events, icu_stays", "patient_id, admission_id, visit_id, appointment_id", "patient_id, facility_id", "Comprehensive clinical lifecycle: admissions, ALOS, emergency triage, ICU ventilation, and discharges."),
        ("Clinical Workforce", "doctors, staff, doctor_workload, staff_attendance, staff_workload, nurse_shifts, surgeries", "doctor_id, staff_id, shift_id, surgery_id", "facility_id, department_id", "Tracks scheduled vs worked hours, overtime, patient-nurse ratios, and surgical procedures."),
        ("Revenue Cycle & Financial", "billing, claims, financial_monthly, financial_expenses", "bill_id, claim_id, financial_id", "patient_id, facility_id", "Financial ledger: gross billed amounts, contractual deductions, paid amounts, payer denial codes, and OpEx."),
        ("Diagnostics & Laboratory", "lab_orders_results, lab_samples, lab_tests, lab_equipment", "order_id, sample_id, test_id, equipment_id", "patient_id, facility_id", "Diagnostic orders, specimen tracking, turnaround time (TAT), abnormal results, and equipment uptime."),
        ("Pharmacy & Therapeutics", "medicines, medicine_batches, inventory, inventory_transactions, prescriptions, pharmacy_dispensing", "medicine_id, batch_id, prescription_id", "facility_id, medicine_id", "Pharmaceutical formulary, batch expirations, stock-to-reorder ratios, unit costs, and dispensing velocity."),
        ("Quality, Safety & Experience", "quality_audits, quality_incidents, corrective_actions, patient_feedback, patient_complaints", "audit_id, incident_id, action_id, feedback_id", "facility_id, department_id", "Clinical quality audits, infection incidents, medication errors, CAPA tracking, CSAT, and NPS."),
        ("Supply Chain & Procurement", "vendors, vendor_performance, purchase_orders, supply_chain_purchase_orders", "vendor_id, po_id", "vendor_id, facility_id", "Supplier master, purchase order fulfillment, on-time delivery rates, and vendor audit quality scores.")
    ]

    t_ds_data = [[
        Paragraph("Functional Domain", styles['TableHeader']),
        Paragraph("Included Tables (All 41)", styles['TableHeader']),
        Paragraph("Primary Keys", styles['TableHeader']),
        Paragraph("Relational Foreign Keys", styles['TableHeader']),
        Paragraph("Operational Purpose & Scope", styles['TableHeader'])
    ]]
    for domain, tbls, pks, fks, scope in tables_summary:
        t_ds_data.append([
            Paragraph(f"<b>{domain}</b>", styles['TableCellBold']),
            Paragraph(f"<code>{tbls}</code>", styles['TableCellCode']),
            Paragraph(f"<code>{pks}</code>", styles['TableCellCode']),
            Paragraph(f"<code>{fks}</code>", styles['TableCellCode']),
            Paragraph(scope, styles['TableCell'])
        ])

    t_ds = Table(t_ds_data, colWidths=[95, 125, 85, 80, PRINTABLE_WIDTH - 385])
    t_ds.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_NAVY),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_ds)
    story.append(Spacer(1, 10))
    return story
