"""
MedOps Technical Documentation - Sections 15 to 18 Content Generator
Covers:
  Section 15: Internal Demonstration Script (5-7 min Full + 2 min Lightning)
  Section 16: Comprehensive Mentor Question Bank (40 Categorized + 10 Senior Grill Questions)
  Section 17: Last-Minute Revision Cheat Sheet
  Section 18: Healthcare & Cloud Engineering Glossary
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib import colors
from docs.styles import (
    PRINTABLE_WIDTH, PRIMARY_NAVY, BRAND_TEAL, BRAND_CYAN, ACCENT_BLUE,
    ACCENT_AMBER, ACCENT_ROSE, ACCENT_EMERALD, BG_CARD, BORDER_COLOR,
    TEXT_MAIN, make_callout, make_code_block, make_section_divider
)

def build_section_15(styles):
    """Section 15: Internal Demo Scripts."""
    story = []
    story.append(Paragraph("15. INTERNAL DEMONSTRATION SCRIPTS & WALKTHROUGHS", styles['SecHeading1']))
    story.append(Paragraph(
        "A successful technical demonstration requires fluid transitions, crisp verbal delivery, and disciplined boundaries. "
        "Below are the verified step-by-step demonstration scripts tailored for evaluator reviews:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("15.1 Full 5-7 Minute Master Demonstration Script", styles['SecHeading2']))
    
    demo_steps = [
        ("Step 1: Introduction & Problem Context (0:00 - 0:45)",
         "Open browser to MedOps application shell (Header visible).",
         "\"Good morning. MedOps is a unified healthcare operations intelligence command system built for regional hospital networks. "
         "Modern hospital leaders struggle with fragmented departmental data -- emergency queues, inpatient beds, billing clearinghouses, and pharmacy supplies "
         "run on disconnected systems, leaving executives reliant on delayed spreadsheets. MedOps centralizes 41 operational datasets across 5 facilities into an AWS serverless data lake.\"",
         "Highlight Vercel edge deployment and Amazon Cognito Managed Login authentication with PKCE.",
         "Do not claim that this is an Electronic Health Record (EHR). It is an operational decision intelligence layer."),

        ("Step 2: Architecture & Data Pipeline (0:45 - 1:30)",
         "Navigate to 'AWS Cloud Services Hub' or open the Architecture Blueprint.",
         "\"Our architecture follows a clean three-tier model: A React 19 and TypeScript frontend, a FastAPI analytical backend, and an AWS serverless data lake. "
         "In production on Vercel, the backend uses Vercel OIDC tokens to assume a temporary IAM role via AWS STS -- zero static keys in the cloud. "
         "Data in Amazon S3 (Mumbai) is cataloged by AWS Glue (Hyderabad) and queried via Amazon Athena using distributed Presto SQL, backed by a 300-second in-memory cache.\"",
         "Explain the multi-region topology: S3 in ap-south-1, Glue/Athena in ap-south-2, and Bedrock/Cognito in us-east-1.",
         "Do not claim dedicated EC2/ECS servers; emphasize serverless query execution."),

        ("Step 3: Executive Command Center & Census (1:30 - 2:30)",
         "Select 'Executive Command Center', filter by 'All Facilities' and 'Monthly'.",
         "\"Here in the Executive Command Center, leadership gains instantaneous macro visibility across our 5 facilities. "
         "Notice our Active Inpatient Admissions and our Bed Occupancy Rate at 84.2%. Crucially, this occupancy calculation is based on active admissions "
         "overlapping the reference date against licensed bed capacity, rather than blindly counting historical cumulative admissions. "
         "At the top, our AI Operational Briefing dynamically synthesizes capacity thresholds and financial risks without exposing any patient PHI.\"",
         "Point to the 'Data Source: Amazon Athena (Verified)' badge in the header.",
         "Do not claim that the AI generates clinical diagnoses; it synthesizes administrative operational metrics."),

        ("Step 4: Revenue Cycle & Financial Intelligence (2:30 - 3:45)",
         "Click 'Financial Intelligence (P&L)', then 'Insurance & Claims Automation'.",
         "\"Turning to revenue cycle management: In Financial Intelligence, we present an executive 9-line Statement of Profit & Loss showing our Operating Margin "
         "and EBITDA proxy. Notice that our Revenue Budget Variance is favorable by 2.5%. During our technical audit, we verified that Days Cash on Hand lacked balance-sheet "
         "cash reserve data, so we completely removed the card to maintain strict product truthfulness. In Claims Automation, we monitor our 8.4% denial rate and top denial codes like CO-16.\"",
         "Show the expense categories breakdown and monthly revenue vs cost area chart.",
         "Do not pretend Days Cash on Hand is calculated; explain why it was deliberately removed."),

        ("Step 5: Clinical Quality, Pharmacy & Vendors (3:45 - 4:45)",
         "Open 'Quality & Compliance', then 'Pharmacy & Inventory', then 'Supply Chain'.",
         "\"In Quality & Compliance, we track our Data Privacy Compliance Score of 94.2% and our Infection Incident Rate of 1.25%, calculated against an active admissions denominator. "
         "In Pharmacy, our dynamic 90-day rolling expiration algorithm flags 18 batches requiring proactive stock rotation. "
         "And in Supply Chain, we replaced the unsupported defect rate with an authentic Average Vendor Quality Score of 91.4% derived from actual supplier audits.\"",
         "Point to the rolling 90-day expiration risk table and verified vendor scorecard.",
         "Do not call infection rate 'Hospital-Acquired' unless the dataset proves nosocomial origin."),

        ("Step 6: AI Copilot & Real-Time Query (4:45 - 5:45)",
         "Click 'AI Copilot' in the header to expand the slide-over drawer; send prompt: 'Summarize ICU capacity and emergency wait times'.",
         "\"Our Medical Operations AI Copilot bridges cloud inference with empirical healthcare telemetry. The backend passes structured aggregate metrics into the context prompt. "
         "Notice how the response highlights our high-acuity ESI cases and recommends nurse reallocation. If public APIs experience rate limits, the system seamlessly activates Deterministic Analytics Mode.\"",
         "Explain prompt serialization and zero-PHI compliance.",
         "Do not claim the model has access to private medical records."),

        ("Step 7: Verification, Limitations & Closing (5:45 - 6:30)",
         "Open the System Health status or test summary.",
         "\"In summary, MedOps delivers verified healthcare decision analytics backed by 26 automated unit and regression tests. "
         "Our next architectural milestones include converting S3 CSVs to Snappy-Parquet and activating native Bedrock Nova-Lite models once AWS account entitlements clear. "
         "Thank you, and I look forward to your questions.\"",
         "Highlight the 100% passing test suite exit codes.",
         "Do not claim live streaming HL7; acknowledge current batch/Athena query cadence.")
    ]

    t_script_data = [[
        Paragraph("Demonstration Phase", styles['TableHeader']),
        Paragraph("Action on Screen", styles['TableHeader']),
        Paragraph("Verbatim Spoken Narration", styles['TableHeader']),
        Paragraph("Technical Focus Point", styles['TableHeader']),
        Paragraph("Boundary / Do NOT Claim", styles['TableHeader'])
    ]]
    for phase, action, script, tech, bound in demo_steps:
        t_script_data.append([
            Paragraph(f"<b>{phase}</b>", styles['TableCellBold']),
            Paragraph(action, styles['TableCell']),
            Paragraph(script, styles['TableCell']),
            Paragraph(f"<font color='#0284C7'>{tech}</font>", styles['TableCell']),
            Paragraph(f"<font color='#E11D48'><b>{bound}</b></font>", styles['TableCell'])
        ])

    t_script = Table(t_script_data, colWidths=[85, 95, 175, 85, PRINTABLE_WIDTH - 440])
    t_script.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_NAVY),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_script)
    story.append(Spacer(1, 8))

    story.append(Paragraph("15.2 Rapid 2-Minute Lightning Demonstration Script", styles['SecHeading2']))
    fast_script = (
        "\"Good morning. MedOps is a cloud-native healthcare operations intelligence dashboard. It centralizes 41 relational datasets across 5 regional "
        "hospitals into an Amazon S3 data lake in Mumbai, cataloged by AWS Glue and queried via Amazon Athena in Hyderabad using Presto SQL.<br/><br/>"
        "Here on the Executive Command Center, leadership monitors enterprise census, active admissions, and net revenue in real time. "
        "Our bed occupancy is 84.2%, accurately calculated using active admission date-interval overlap rather than cumulative historical records. "
        "In our Financial Intelligence module, we track operating margins and EBITDA proxy with audited Athena SQL queries. "
        "Notice our Quality and Pharmacy modules: we calculate infection incident rates per admission, track dynamic 90-day medication expirations, "
        "and maintain authentic vendor audit scores. Finally, our AI Executive Copilot synthesizes operational briefings using Google Gemini and Amazon Bedrock "
        "with zero patient PHI exposure. With 26 automated regression tests passing, MedOps provides reliable, defensible healthcare operational intelligence.\""
    )
    story.append(make_callout("2-MINUTE LIGHTNING SCRIPT", fast_script, callout_type="note", styles=styles))
    story.append(Spacer(1, 10))
    return story


def build_section_16(styles):
    """Section 16: Comprehensive Mentor Question Bank (40 + 10 Questions)."""
    story = []
    story.append(Paragraph("16. MENTOR QUESTION BANK & TECHNICAL DEFENSE GUIDE", styles['SecHeading1']))
    story.append(Paragraph(
        "Technical mentors and evaluators probe architecture, data integrity, security, and edge-case handling. "
        "Below are 50 comprehensive questions and bulletproof answers divided across 8 technical domains plus a senior evaluator grill section:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    qa_list = [
        # Domain 1: Project Fundamentals
        ("1. What specific business problem does MedOps solve that existing EHRs cannot?",
         "EHRs are optimized for transactional clinical documentation, not multi-facility executive operations. MedOps unifies 41 datasets across 5 facilities to deliver cross-functional decision intelligence.",
         "Clinical EHRs (Epic, Cerner) store patient charts in relational silos. They lack unified cross-departmental aggregation for financial P&L, supply chain lead-times, and workforce scheduling. MedOps acts as an analytical overlay using serverless data lake technology.",
         "README.md (Sections 1-2)",
         "Do not claim MedOps replaces the hospital EHR. It sits on top of EHRs as an operational intelligence platform."),

        ("2. Who are the primary target users and how does each persona benefit?",
         "Hospital C-suite (COO, CMO, CFO) and clinical department heads who need real-time throughput and revenue visibility.",
         "COOs monitor bed capacity and emergency boarding; CMOs track infection rates and physician workloads; CFOs analyze claims denial trends and monthly operating margins; Pharmacy directors monitor 90-day expiring batches.",
         "src/components/layout/Sidebar.tsx",
         "Do not state it is built for patient self-service; it is strictly an administrative and clinical leadership platform."),

        ("3. Why did you choose a serverless data lake rather than a traditional relational database (e.g., PostgreSQL)?",
         "To handle large-scale, high-cardinality analytical queries across 41 tables without paying for idle database compute.",
         "A relational database requires dedicated instance sizing, maintenance windows, and read-replica management. S3 + Glue + Athena provides serverless elasticity, scanning CSV/Parquet data on-demand where costs scale strictly with query volume.",
         "backend/app/aws/athena.py",
         "Do not say Athena is faster than Postgres for single-row lookups; Athena is optimized for distributed columnar scans and aggregations."),

        ("4. What makes your data pipeline resilient to network drops or AWS throttling?",
         "A multi-tier fallback architecture: In-Memory Cache (300s TTL) -> Athena SQL -> S3 Direct Read -> Local CSV Fallback -> Safe Empty States.",
         "In backend/app/services/dashboard_service.py, _load_table() wraps Athena queries in try/except blocks. If Athena fails, it streams the CSV from S3. If S3 fails, it resolves local CSVs, ensuring the dashboard never throws 500 errors.",
         "backend/app/services/dashboard_service.py (_load_table)",
         "Do not say the system always hits Athena live; acknowledge the 300s cache and fallback tiers."),

        # Domain 2: Architecture
        ("5. Can you walk me through the end-to-end request-response flow when a user changes a filter?",
         "React state triggers useEffect -> apiService.ts sends HTTPS request with Cognito Bearer token -> FastAPI router validates parameters -> dashboard_service checks cache or queries Athena -> Pandas aggregates metrics -> JSON returned to UI.",
         "When facility_id='FAC001' is selected, React triggers fetchFinancialIntelligence. FastAPI passes this to get_financial_intelligence(). It checks _TABLE_CACHE. On miss, it executes Athena Presto SQL. Rows are sanitized via _clean_df_types(), aggregated, and returned as HTTP 200.",
         "src/services/apiService.ts, backend/app/routes/dashboard.py",
         "Do not forget to mention the Bearer token injection and defensive numeric cleaning."),

        ("6. Why did you separate the frontend (React/Vite) from the backend (FastAPI)?",
         "To maintain clean separation of concerns, enable independent scaling, and isolate cloud credentials from the browser.",
         "The React SPA handles UI rendering and interactive SVG charts via Recharts. The FastAPI backend handles heavy analytical computation, Pandas data frame aggregations, and secure Boto3 cloud SDK invocations. The client never touches AWS credentials.",
         "package.json, backend/app/main.py",
         "Do not say they are bundled together; they are decoupled services connected over REST."),

        ("7. How does Vercel Workload Identity work without static AWS access keys?",
         "Vercel generates an OIDC JWT token which the backend presents to AWS STS via AssumeRoleWithWebIdentity for 1-hour scoped credentials.",
         "In cloud deployment, storing AWS_ACCESS_KEY_ID in environment variables poses security leakage risks. MedOps uses VERCEL_OIDC_TOKEN exchanged dynamically with AWS STS, obtaining temporary credentials scoped to the vercel-medical-operations IAM role.",
         "backend/app/aws/session.py",
         "Do not claim keys are hardcoded in the frontend; all cloud interaction is strictly server-side."),

        ("8. What is the role of the 300-second in-memory cache in the backend?",
         "It prevents duplicate Athena query execution, reducing cloud query costs and delivering sub-10ms response times.",
         "_TABLE_CACHE stores DataFrame snapshots indexed by table name. If multiple users query admissions for the same facility within 5 minutes, Athena is not re-queried, dramatically reducing S3 scan costs.",
         "backend/app/services/dashboard_service.py (_TABLE_CACHE)",
         "Do not claim it is a distributed Redis cluster; it is a thread-safe in-memory cache with planned Redis migration."),

        ("9. Why is the AWS infrastructure split across multiple regions (ap-south-1, ap-south-2, us-east-1)?",
         "Storage, query compute, and AI services were provisioned where their specific resources and model entitlements reside.",
         "S3 raw data lake is in ap-south-1 (Mumbai) for durability; AWS Glue Catalog and Athena workgroups are in ap-south-2 (Hyderabad); Amazon Bedrock Nova-Lite and Amazon Cognito are in us-east-1 (N. Virginia) where enterprise AI models are available.",
         "backend/app/config.py (Settings)",
         "Do not claim all services run in a single region; explain the intentional multi-region cloud topology."),

        # Domain 3: AWS & Data Engineering
        ("10. What is the difference between AWS Glue Data Catalog and Amazon Athena?",
         "Glue is the metadata catalog (schema and file locations); Athena is the serverless SQL query execution engine.",
         "Glue does not store or process data; it stores table definitions (column names, types, S3 location prefixes). Athena uses Presto/Trino distributed compute to parse Glue schemas and execute SQL queries directly against raw S3 CSV/Parquet files.",
         "backend/app/aws/glue.py, backend/app/aws/athena.py",
         "Do not confuse Glue crawlers with database servers; Glue is strictly a schema catalog."),

        ("11. How does Amazon Athena execute SQL queries directly against S3 CSV files?",
         "Athena reads the Glue schema, discovers CSV files in the S3 bucket prefix, splits them into chunks, and executes distributed Presto SQL.",
         "When SELECT * FROM admissions is dispatched, Athena resolves the S3 prefix from Glue (s3://medical-operations-bharath-2026/raw/admissions/), executes parallel worker scans across files, and streams results to an output CSV in s3://medical-operations-athena-results-bharath-2026/.",
         "scripts/query_live_athena.py",
         "Do not claim Athena loads data into a relational table; it queries files in-place on S3."),

        ("12. What happens if AWS Glue encounters generic 'col0..colN' headers?",
         "Our backend detects 'col0' in row 0, extracts the real column headers from the first data row, and resets the DataFrame columns dynamically.",
         "In certain Glue CSV crawlers where headers are not automatically promoted, the catalog registers columns as col0, col1, etc. Lines 260-270 of dashboard_service.py inspect the header; if col0 is present, row 0 is promoted to column names and secondary headers are stripped.",
         "backend/app/services/dashboard_service.py (Lines 260-272)",
         "Do not say the system crashes; show how our code dynamically detects and repairs generic Glue headers."),

        ("13. How do your synthetic data generator scripts prevent primary key collisions?",
         "By applying unique synthetic prefixes (e.g., SYN-ADM-*, SYN-BIL-*, SYN-CLM-*) and checking pre-existing keys.",
         "scripts/generate_hospital_data.py uses distinct alphanumeric prefixes and executes a head_object preflight check in S3 with conditional IfNoneMatch='*' to prevent overwriting existing files.",
         "scripts/generate_hospital_data.py, scripts/README.md",
         "Do not claim the synthetic generator runs automatically in background; it is a manually invoked developer utility."),

        ("14. How is data freshness handled in the platform?",
         "Through manual batch ingestion scripts and Athena on-demand query execution, supplemented by cache TTL eviction.",
         "New CSV files uploaded to S3 table prefixes are instantly discoverable by subsequent Athena queries. The 300s in-memory cache expires automatically, ensuring fresh data is pulled without requiring database restarts.",
         "backend/app/services/dashboard_service.py",
         "Do not claim real-time streaming HL7 ingestion exists currently; state that current freshness is batch-driven."),

        # Domain 4: Database & SQL
        ("15. What are the core entities in your healthcare relational schema?",
         "Facilities, Departments, Beds, Patients, Admissions, Emergency Visits, Billing, Claims, and Clinical Staff.",
         "The schema links facilities to departments, beds, and admissions. Admissions link patients to billing records, and billing records link to insurance claims, establishing a full clinical-to-financial audit trail.",
         "docs/assets/er_diagram.png",
         "Do not say all 41 tables are independent; they share relational keys like facility_id, patient_id, and bill_id."),

        ("16. How do you prevent SQL injection when querying Athena?",
         "By parameterizing queries and validating facility_id and timeframe inputs against strict alphanumeric whitelists.",
         "In dashboard_service.py, input strings are sanitized, and date ranges are computed via Python datetime objects rather than accepting raw SQL fragments from user input.",
         "backend/app/services/dashboard_service.py",
         "Do not claim raw user strings are concatenated into SQL WHERE clauses."),

        ("17. How does the system handle date-range filtering for monthly vs quarterly vs YTD?",
         "The _get_timeframe_range() function computes exact start and end timestamps based on a verified reference date.",
         "For monthly, it calculates the first and last day of the current operational month (e.g., 2026-09-01 to 2026-09-30). For quarterly, it computes the 3-month boundary (2026-07-01 to 2026-09-30). For YTD, it spans 2026-01-01 to ref_date.",
         "backend/app/services/dashboard_service.py (_get_timeframe_range)",
         "Do not assume end-of-month is always the 31st; verify that exact calendar date arithmetic is used."),

        # Domain 5: Metrics & Clinical Formulations
        ("18. How exactly is Bed Occupancy Rate calculated?",
         "Active Admissions as of reference date divided by Total Licensed Beds, multiplied by 100.",
         "Occupancy = (Active Admissions / Total Licensed Beds) * 100. An admission is active if admission_date <= ref_date AND (discharge_date IS NULL OR discharge_date > ref_date). This prevents counting historically discharged patients.",
         "backend/app/services/dashboard_service.py (Lines 370-430)",
         "Do not calculate occupancy by dividing total cumulative admissions by beds."),

        ("19. Why was Days Cash on Hand removed from Financial Intelligence?",
         "Because the source dataset lacked balance-sheet cash reserves, short-term investments, and non-cash depreciation.",
         "Days Cash on Hand = (Cash + Short-Term Investments) / ((OpEx - Depreciation) / 365). Our data lake records monthly operating revenues and expenses, but lacks balance-sheet liquidity reserves. To preserve strict product truthfulness, the card was removed.",
         "src/components/modules/FinancialIntelligence.tsx",
         "Do not fabricate an imaginary cash number; proudly cite product truthfulness as the engineering rationale."),

        ("20. Why was Physical Defect Rate replaced with Average Vendor Quality Score?",
         "The dataset lacked damaged shipment inspection records, but contained authentic vendor audit quality scores.",
         "vendor_performance.csv contains quality_score evaluated during supplier audits. Rather than showing an unverified defect percentage, we surfaced the authentic Vendor Quality Score (91.4%).",
         "src/components/modules/SupplyChainVendor.tsx",
         "Do not claim you calculate carton damage rates; explain the defensible replacement."),

        ("21. How is the Infection Incident Rate calculated, and why is it not called HAI Rate?",
         "Infection incidents divided by total period admissions times 100. It is not labeled HAI because datasets lack hospital-acquired clinical evidence.",
         "Formula: (Infection Incidents / Total Admissions) * 100. To classify an infection as Hospital-Acquired (HAI), CDC guidelines require evidence that the infection was not present or incubating upon admission (typically > 48 hours post-admission). Because our records lack positive pre-admission swab telemetry, we truthfully label it 'Infection Incident Rate'.",
         "backend/app/services/dashboard_service.py (Lines 1880-1910)",
         "Never claim regulatory HAI classification without clinical onset telemetry."),

        ("22. How are Medication Errors reported across 'Today' versus the reporting period?",
         "Today tracks incidents matching the current reference date; total reports incidents across the entire selected timeframe.",
         "In QualityCompliance.tsx, Card 4 displays Total Medication Errors in the period with an embedded badge showing errors registered specifically on the reference evaluation day.",
         "src/components/modules/QualityCompliance.tsx",
         "Do not confuse single-day error counts with multi-month period totals."),

        ("23. How do you calculate Operating Profit (EBITDA Proxy)?",
         "Net Operating Revenue minus Total Operating Expenses (OpEx).",
         "Operating Profit = Revenue - Operating Cost. Operating Margin % = (Operating Profit / Revenue) * 100. Revenue Variance = Actual Revenue - Budget Revenue.",
         "backend/app/services/dashboard_service.py (_build_financial_response)",
         "Do not claim it is an audited GAAP net income figure; clearly label it an operational EBITDA proxy."),

        # Domain 6: Frontend & UI State
        ("24. How does the frontend handle empty data states when a facility has no admissions?",
         "It renders a graceful 'No Data Available' state without throwing JavaScript undefined errors.",
         "In PatientOperations.tsx, lines 75-85 check if data is null or empty. If true, it returns an icon with informative guidance instead of attempting to access data.admissions and triggering a React crash.",
         "src/components/modules/PatientOperations.tsx",
         "Do not claim the dashboard displays blank cards; explain the explicit empty-state guard."),

        ("25. How do Recharts components handle responsive resizing on mobile or small screens?",
         "By wrapping chart elements in ResponsiveContainer width='100%' height={300}.",
         "Recharts dynamically measures parent DOM container widths and recalculates SVG coordinate paths upon window resize events, preventing horizontal scrolling or clipped labels.",
         "src/components/modules/FinancialIntelligence.tsx",
         "Do not use fixed pixel widths on chart containers."),

        ("26. How are Cognito access tokens passed from React to FastAPI?",
         "apiService.ts wraps standard fetch() in apiFetch(), injecting Authorization: Bearer <id_token> into HTTP headers.",
         "Tokens are retrieved from browser sessionStorage via getIdToken(). If present, the header is set automatically on all REST calls to /api/*.",
         "src/services/apiService.ts (apiFetch)",
         "Do not store authentication tokens in unencrypted localStorage."),

        # Domain 7: AI, Copilot & Predictions
        ("27. How do you prevent patient PHI leakage to Google Gemini or Amazon Bedrock?",
         "Prompts contain strictly aggregate mathematical metrics; zero patient identifiers are ever serialized into LLM prompts.",
         "The prompt context assembler serializes only total admissions, occupancy %, average length of stay, revenue collections, and denial rates. Zero names, IDs, dates of birth, or clinical notes are sent.",
         "backend/app/services/copilot_service.py",
         "Never state that the LLM reads raw patient medical charts."),

        ("28. What happens if Google Gemini returns a 429 Rate Limit or 503 Service Unavailable?",
         "The system cascades to alternative models and automatically activates Deterministic Analytics Mode.",
         "The Gemini provider cascades: gemini-3.5-flash -> gemini-3.8-flash -> gemini-flash-latest. If all fail, it catches the exception and generates a deterministic rule-based executive brief from raw telemetry numbers.",
         "backend/app/services/ai_service.py",
         "Do not allow the dashboard to crash when external AI APIs timeout."),

        ("29. How is the 7-day predictive inpatient inflow forecast calculated?",
         "Using a statistical 14-day exponential moving average combined with day-of-week seasonality weighting factors.",
         "It is a deterministic statistical time-series model that weights recent admissions against historical Monday-through-Sunday admission velocity, generating 95% confidence prediction bands.",
         "src/components/modules/AIPredictiveIntelligence.tsx",
         "Do not call a statistical moving average a 'deep neural network'."),

        # Domain 8: Testing, Security & Deployment
        ("30. What automated test suites exist and what did the latest test execution prove?",
         "Two comprehensive pytest suites: test_audit_remediation_fixes.py (9/9 passed) and test_data_expansion_and_filters.py (17/17 passed).",
         "They prove that monthly date SQL filters include end-of-month dates, active bed occupancy correctly isolates overlapping stays, dynamic 90-day expiry triggers accurately, and date filters slice DataFrames correctly.",
         "backend/tests/",
         "Do not claim you ran 500 tests; cite the exact 26 passing regression tests."),

        ("31. What does a successful 'npx tsc --noEmit' and 'npm run build' prove?",
         "It proves zero TypeScript compilation errors, valid JSX syntax, resolved imports, and production asset bundle generation.",
         "tsc validates that all interface properties match API contracts across 21 modules. Vite bundles CSS and JavaScript into dist/index.html and dist/assets/ in 1.12s without runtime syntax errors.",
         "package.json (build script)",
         "Do not claim a build proves live cloud database connectivity; it validates code and asset integrity."),

        ("32. How is the application deployed to production on Vercel?",
         "Vercel builds the React frontend with Vite and routes /api/* requests to the FastAPI Python serverless runtime via vercel.json.",
         "vercel.json defines builds and rewrites, uniting the static frontend and Python serverless function under a single unified domain without requiring complex CORS configurations.",
         "vercel.json",
         "Do not claim you are running Kubernetes or Docker containers in production."),

        ("33. What are the 5 Amazon Cognito user groups configured in the user pool?",
         "ADMIN, HOSPITAL_ADMIN, DOCTOR, ANALYST, and VIEWER.",
         "These groups correspond to healthcare roles. When a user authenticates, their ID token contains cognito:groups claims, which the React AuthContext maps to user permissions.",
         "src/context/AuthContext.tsx",
         "Do not claim fine-grained endpoint route RBAC is fully active; explain that role claims are mapped on the frontend profile."),

        ("34. How are database credentials and secrets kept out of source code?",
         "All credentials use environment variables loaded via python-dotenv, strictly excluded from Git in .gitignore.",
         "backend/.env is listed in .gitignore. In production on Vercel, workload identity uses OIDC to obtain credentials dynamically without storing static secret keys.",
         "backend/app/config.py, .gitignore",
         "Never commit .env files to GitHub."),

        ("35. What is the difference between client-side and server-side filtering in MedOps?",
         "Server-side filters slice data in SQL or Pandas before returning JSON; client-side filters re-sort or re-slice loaded tables in memory.",
         "Facility and timeframe parameters are passed to FastAPI and applied server-side in Athena SQL or Pandas DataFrame queries, minimizing network payload sizes.",
         "backend/app/routes/dashboard.py",
         "Do not claim the browser downloads all 100k rows and filters them locally."),

        ("36. How do you handle division by zero in healthcare ratio calculations?",
         "Using safe divisor checks: if denominator == 0, return 0.0 or None, serialized as 'N/A'.",
         "In occupancy, denial rates, and ALOS calculations, denominators are verified (> 0). In Python, if total_beds == 0: occupancy = 0.0. In React, null displays as 'N/A' rather than NaN% or Infinity.",
         "backend/app/services/dashboard_service.py",
         "Never allow NaN or Infinity to appear on dashboard KPI cards."),

        ("37. What is Case Mix Index (CMI) in Medical Coding?",
         "A relative value score measuring the clinical complexity and financial resource requirements of treated patients.",
         "A higher CMI indicates that a hospital treats more severely ill patients requiring intensive clinical interventions, directly influencing Medicare and private insurance reimbursement rates.",
         "src/components/modules/MedicalCodingDocumentation.tsx",
         "Do not confuse CMI with simple patient headcounts."),

        ("38. What is the Left Without Being Seen (LWBS) rate in emergency medicine?",
         "The percentage of patients who register in the ED but depart before receiving a medical examination from a physician.",
         "LWBS is a premier operational benchmark of emergency department overcrowding and triage bottlenecks. High LWBS indicates dangerously extended wait times.",
         "src/components/modules/EmergencyCriticalOperations.tsx",
         "Do not claim walkout patients were fully treated."),

        ("39. What is a clean claim rate and why do CFOs monitor it closely?",
         "The percentage of claims adjudicated and approved by insurance payers on initial submission without manual correction.",
         "A clean claim rate above 85% prevents cash flow delays and eliminates expensive billing re-submissions, which cost between $25 and $118 per reworked claim.",
         "src/components/modules/InsuranceClaimsAutomation.tsx",
         "Do not confuse clean claim rate with overall collection rate."),

        ("40. What is the difference between gross revenue, net revenue, and collected revenue?",
         "Gross is total chargemaster list price; Net is expected reimbursement after contractual discounts; Collected is actual cash received.",
         "Gross = $14.2M; Discounts = $2.8M; Net Billed = $11.4M; Collected = $9.8M; Outstanding A/R = $1.6M. MedOps tracks all four distinctly in billing and P&L tables.",
         "src/components/modules/FinancialIntelligence.tsx",
         "Do not use gross and net revenue interchangeably; hospitals rarely collect gross charges.")
    ]

    # Render Q&A in compact structured blocks
    for q, short, deep, loc, mist in qa_list:
        q_story = []
        q_story.append(Paragraph(f"<b>{q}</b>", styles['MentorQ']))
        q_story.append(Paragraph(f"<b>Direct Answer:</b> {short}", styles['MentorA']))
        q_story.append(Paragraph(f"<b>Technical Deep-Dive:</b> {deep}", styles['TableCell']))
        q_story.append(Paragraph(f"<b>Source Location:</b> <code>{loc}</code> &nbsp;|&nbsp; <b>Common Trap:</b> <font color='#E11D48'>{mist}</font>", styles['TableCellCode']))
        q_story.append(Spacer(1, 4))
        story.append(KeepTogether(q_story))

    # 10 Senior Mentor Trap Questions
    story.append(Spacer(1, 6))
    story.append(Paragraph("16.2 Top 10 Senior Mentor Grill / Trap Questions & Bulletproof Defenses", styles['SecHeading2']))
    
    grill_questions = [
        ("Trap 1: 'Your dashboard looks nice, but is it querying Athena right now or just showing hardcoded mock numbers?'",
         "\"It queries through our four-tier fallback hierarchy. If an active Athena session is live, it executes Presto SQL and displays the 'Data Source: Amazon Athena (Verified)' badge. "
         "If running offline without AWS credentials, our backend falls back to local CSVs in dataset/medical_operations_core_v9_100k/. The numbers are never hardcoded mock constants; "
         "they are computed dynamically by Pandas from 100k+ underlying records.\""),

        ("Trap 2: 'Why does your Bed Occupancy calculation not match total admissions divided by beds?'",
         "\"Because dividing total admissions by beds is an arithmetic error that counts every historically discharged patient as still occupying a bed. "
         "Our formula evaluates active admissions overlapping the reference evaluation timestamp against licensed facility bed capacity, representing true point-in-time census.\""),

        ("Trap 3: 'Why did you remove Days Cash on Hand? Did you fail to calculate it?'",
         "\"We deliberately removed it to uphold engineering integrity. Calculating Days Cash on Hand requires balance-sheet cash reserves, short-term investments, and depreciation. "
         "Our data lake houses operational revenues and expenses, but lacks balance-sheet liquidity accounts. Rather than inventing an unverified cash balance or presenting a false metric, "
         "we removed the card and re-balanced the UI.\""),

        ("Trap 4: 'How can you claim this dashboard is HIPAA compliant?'",
         "\"We do not claim full HIPAA regulatory certification. MedOps is an operational decision intelligence tool, not an EHR or medical device. "
         "What we do enforce is strict architectural data protection: Zero PHI is transmitted to LLM prompts, credentials are isolated from the client, "
         "and Cognito sessions are tab-isolated via sessionStorage.\""),

        ("Trap 5: 'Why are you using CSV files in S3 instead of Parquet?'",
         "\"CSV was chosen during Phase 1 for maximum human readability and rapid schema auditing across Glue crawlers. "
         "Our production roadmap includes automated AWS Glue ETL jobs to convert these datasets into Snappy-compressed Apache Parquet, which will reduce Athena query scan costs by up to 80%.\""),

        ("Trap 6: 'What happens if Google Gemini goes down or experiences a 429 quota exhaustion during your demo?'",
         "\"The system will not crash. Our provider-independent AI service implements automatic model cascading across three Gemini versions, "
         "and if all fail, it instantly activates Deterministic Analytics Mode, generating rule-based executive insights directly from verified telemetry.\""),

        ("Trap 7: 'How do you handle patient data privacy if a doctor opens the dashboard on a shared workstation?'",
         "\"First, Cognito tokens are stored in sessionStorage, meaning closing the tab terminates the session. Second, all metrics in the dashboard are aggregated "
         "at the facility or department level -- zero patient names or personal health records appear on general dashboard cards.\""),

        ("Trap 8: 'Why use FastAPI instead of Node.js / Express for the backend?'",
         "\"Because healthcare operations intelligence requires heavy numerical data transformation, date-interval arithmetic, and statistical aggregations. "
         "Python's Pandas ecosystem is vastly superior to JavaScript for high-cardinality DataFrame operations, while FastAPI provides high-throughput async REST endpoints.\""),

        ("Trap 9: 'What happens if a user submits a SQL injection attempt in the interactive Athena console?'",
         "\"The AWSCloudServicesHub console is restricted to developers and executes queries via scoped IAM policies with read-only permissions on the medical_operations_db database. "
         "Athena cannot execute DROP, ALTER, or destructive write operations against immutable S3 data lake storage.\""),

        ("Trap 10: 'What was the single most difficult technical challenge you solved during the recent audit remediation?'",
         "\"Resolving the financial monthly Athena SQL date filtering. The monthly table stores records indexed by YYYY-MM-01. "
         "Standard string comparisons or incorrect end-of-month assumptions were omitting the final month of the range. "
         "We implemented precise inclusive date-interval logic and verified it across single-month, quarterly, and YTD filters backed by automated pytest suites.\"")
    ]

    for trap_title, trap_ans in grill_questions:
        t_box = []
        t_box.append(Paragraph(f"<b>{trap_title}</b>", styles['MentorQ']))
        t_box.append(Paragraph(trap_ans, styles['MentorA']))
        story.append(KeepTogether(t_box))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 10))
    return story


def build_section_17(styles):
    """Section 17: Last-Minute Revision Cheat Sheet."""
    story = []
    story.append(Paragraph("17. LAST-MINUTE REVISION CHEAT SHEET (10-MINUTE CRAM GUIDE)", styles['SecHeading1']))
    story.append(Paragraph(
        "Review this compact cheat sheet 10 minutes prior to entering the demonstration room:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    cram_blocks = (
        "<b>PROJECT IN 60 SECONDS:</b> MedOps is a cloud-native healthcare operations intelligence dashboard. It centralizes 41 relational datasets "
        "across 5 regional hospitals into an Amazon S3 data lake in Mumbai, cataloged by AWS Glue and queried via Amazon Athena in Hyderabad using Presto SQL. "
        "A FastAPI backend processes metrics defensibly through a 300s cache, powering 21 React modules and an AI executive briefing engine with zero PHI exposure.<br/><br/>"
        "<b>ARCHITECTURE IN ONE SENTENCE:</b> React 19 SPA (Vercel) + FastAPI analytical REST service + Amazon S3/Glue/Athena serverless data lake + Cognito PKCE auth + Vercel OIDC workload identity.<br/><br/>"
        "<b>TOP 5 FORMULAS TO REMEMBER:</b><br/>"
        "1. <b>Bed Occupancy Rate:</b> (Active Inpatient Admissions overlapping ref_date / Total Licensed Beds) * 100.<br/>"
        "2. <b>Operating Profit (EBITDA Proxy):</b> Net Operating Revenue - Total Operating Expenses (OpEx).<br/>"
        "3. <b>Claims Denial Rate:</b> (Denied Claims Count / Total Submitted Claims) * 100.<br/>"
        "4. <b>Infection Incident Rate:</b> (Total Infection Incidents / Total Period Admissions) * 100.<br/>"
        "5. <b>Clean Claim Rate:</b> (Claims Paid on Initial Submission / Total Claims) * 100.<br/><br/>"
        "<b>THREE CRITICAL REMOVALS & HONESTIES:</b><br/>"
        "• <b>Days Cash on Hand:</b> Removed from UI because datasets lack balance-sheet cash reserves.<br/>"
        "• <b>Physical Defect Rate:</b> Replaced with authentic Average Vendor Quality Score from supplier audits.<br/>"
        "• <b>Infection Rate:</b> Labeled 'Infection Incident Rate' per admission, NOT 'Hospital-Acquired' without clinical onset evidence.<br/><br/>"
        "<b>FIVE GOLDEN DEMO RULES:</b><br/>"
        "1. Never claim MedOps is an EHR; it is an operational decision intelligence platform.<br/>"
        "2. Never claim real patient records are transmitted to Google Gemini or Bedrock.<br/>"
        "3. Proudly cite the 300s in-memory cache and 5-tier fallback when asked about offline resilience.<br/>"
        "4. State exact test metrics: 26 backend regression tests passed, zero TypeScript compilation errors.<br/>"
        "5. If asked about a missing feature, acknowledge it honestly and point to the Parquet/HL7 production roadmap."
    )
    story.append(make_callout("PRE-DEMO RAPID REVISION SUMMARY", cram_blocks, callout_type="important", styles=styles))
    story.append(Spacer(1, 10))
    return story


def build_section_18(styles):
    """Section 18: Glossary of Technical & Healthcare Terms."""
    story = []
    story.append(Paragraph("18. GLOSSARY OF HEALTHCARE & CLOUD ENGINEERING TERMS", styles['SecHeading1']))
    story.append(Paragraph(
        "Standardized definitions of healthcare operational metrics, regulatory acronyms, and cloud data engineering technologies:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    glossary_items = [
        ("ALOS (Average Length of Stay)", "The average number of days an admitted inpatient occupies a hospital bed between admission and discharge."),
        ("Amazon Athena", "An interactive, serverless query service that enables distributed ANSI SQL analysis directly over data stored in Amazon S3."),
        ("Amazon Cognito", "An enterprise identity service providing user authentication, federation, and single sign-on via OAuth 2.0 and PKCE."),
        ("AWS Glue Data Catalog", "A centralized metadata repository that stores table definitions, column types, and schema mappings for data lake files."),
        ("CAPA (Corrective Action)", "Corrective and Preventive Actions instituted following clinical quality incidents to prevent recurrence."),
        ("CMI (Case Mix Index)", "A relative clinical score reflecting the medical complexity, severity, and resource consumption of hospitalized patients."),
        ("CSAT (Customer Satisfaction)", "A transactional metric measuring patient satisfaction following a specific outpatient or inpatient care encounter."),
        ("Door-to-Doctor Time", "The elapsed time in minutes from a patient's arrival at emergency triage to initial evaluation by a licensed physician."),
        ("EBITDA Proxy", "Earnings Before Interest, Taxes, Depreciation, and Amortization; measured as hospital operating revenue minus operating expenses."),
        ("ESI (Emergency Severity Index)", "A 5-level emergency triage algorithm stratifying patients from Level 1 (immediate resuscitation) to Level 5 (non-urgent)."),
        ("In-Memory Cache (TTL)", "Thread-safe RAM storage caching DataFrame queries for 300 seconds to minimize Athena scan latency and cost."),
        ("LWBS (Left Without Being Seen)", "The percentage of emergency department patients who register but depart prior to medical examination due to delays."),
        ("NPS (Net Promoter Score)", "A loyalty metric calculated as the percentage of patient promoters (ratings 9-10) minus detractors (ratings 1-6)."),
        ("OIDC (OpenID Connect)", "An identity layer on top of OAuth 2.0 enabling Vercel serverless functions to acquire temporary AWS STS IAM credentials."),
        ("Presto / Trino", "The high-performance distributed SQL query engine that powers Amazon Athena's serverless data lake scans."),
        ("Recharts", "A declarative, responsive React charting library built with SVG elements and Tailwind styling for interactive analytics.")
    ]

    t_gloss_data = [[Paragraph("Term / Acronym", styles['TableHeader']), Paragraph("Technical Definition & Healthcare Operational Context", styles['TableHeader'])]]
    for term, defn in glossary_items:
        t_gloss_data.append([
            Paragraph(f"<b>{term}</b>", styles['TableCellBold']),
            Paragraph(defn, styles['TableCell'])
        ])

    t_gloss = Table(t_gloss_data, colWidths=[130, PRINTABLE_WIDTH - 130])
    t_gloss.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_NAVY),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_gloss)
    story.append(Spacer(1, 10))
    return story
