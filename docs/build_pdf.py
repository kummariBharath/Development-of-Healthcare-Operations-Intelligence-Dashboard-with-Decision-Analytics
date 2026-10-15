"""
MedOps Technical Documentation - Master PDF Builder
Compiles all 18 sections into a professional A4 PDF guide with NumberedCanvas.
Output: docs/MedOps_Internal_Demo_Technical_Guide.pdf
"""

import os
import sys
import time
from pathlib import Path

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, PageBreak, Spacer, Paragraph, Table, TableStyle
from reportlab.lib import colors

from docs.styles import (
    NumberedCanvas, get_custom_styles, MARGIN, PRINTABLE_WIDTH,
    PRIMARY_NAVY, BRAND_TEAL, BORDER_COLOR, BG_CARD, make_section_divider
)

from docs.content_section1_4 import (
    build_cover_page, build_section_1, build_section_2, build_section_3, build_section_4
)
from docs.content_section5 import build_section_5
from docs.content_section6_9 import (
    build_section_6, build_section_7, build_section_8, build_section_9
)
from docs.content_section10_14 import (
    build_section_10, build_section_11, build_section_12, build_section_13, build_section_14
)
from docs.content_section15_18 import (
    build_section_15, build_section_16, build_section_17, build_section_18
)


def build_table_of_contents(styles):
    """Builds a structured Table of Contents block."""
    story = []
    story.append(Paragraph("TABLE OF CONTENTS & DOCUMENT BLUEPRINT", styles['SecHeading1']))
    story.append(Paragraph(
        "This master documentation is organized into 18 exhaustive technical sections designed for rapid reference during demonstration defense:",
        styles['BodyCustomJustify']
    ))
    story.append(Spacer(1, 4))

    toc_items = [
        ("Section 1", "Executive Project Overview (Elevator Pitches: 60-Second & 2-Minute)", "Overview"),
        ("Section 2", "Healthcare Operational Challenges vs. MedOps Architectural Solutions", "Problem & Solution"),
        ("Section 3", "Complete System Architecture & 10-Step Request-Response Data Flow", "Architecture"),
        ("Section 4", "AWS Cloud Data Pipeline & Multi-Region Storage / Catalog Strategy", "Data Engineering"),
        ("Section 5", "Complete Dashboard Module Guide (All 21 Verified Modules Across 14 Criteria)", "Module Reference"),
        ("Section 6", "Metric-by-Metric Calculation Reference & Clinical Deep Dives", "Formulations"),
        ("Section 7", "Important Code Logic Explained (_load_table, Defensive Typing, Bed Overlap)", "Code Logic"),
        ("Section 8", "REST API Specification (All 22 Backend Endpoints & Parameter Schemas)", "API Reference"),
        ("Section 9", "Database & Dataset Catalog (All 41 Relational Tables & ER Diagram)", "Data Schema"),
        ("Section 10", "AI & Predictive Intelligence Architecture (Bedrock, Gemini Cascade, Zero-PHI)", "AI Intelligence"),
        ("Section 11", "Complete Technology Stack & Architectural Roles Matrix", "Tech Stack"),
        ("Section 12", "Security Perimeter, Cognito PKCE Auth & Vercel OIDC Workload Identity", "Security & IAM"),
        ("Section 13", "Testing, Audit Remediation & Validation Results (26 Passing Regression Tests)", "Verification"),
        ("Section 14", "System Limitations & Future Engineering Roadmap (Transparent Gaps)", "Roadmap"),
        ("Section 15", "Internal Demonstration Scripts (5-7 Minute Master Walkthrough & 2-Min Lightning)", "Demo Scripts"),
        ("Section 16", "Mentor Question Bank (40 Categorized Questions + 10 Senior Grill Defenses)", "Mentor Defense"),
        ("Section 17", "Last-Minute Revision Cheat Sheet (10-Minute Pre-Demo Cram Guide)", "Cheat Sheet"),
        ("Section 18", "Glossary of Healthcare Operational & Cloud Engineering Terminology", "Glossary"),
    ]

    t_toc_data = [[
        Paragraph("Section", styles['TableHeader']),
        Paragraph("Chapter Title & Coverage Scope", styles['TableHeader']),
        Paragraph("Domain", styles['TableHeader'])
    ]]
    for sec, title, domain in toc_items:
        t_toc_data.append([
            Paragraph(f"<b>{sec}</b>", styles['TableCellBold']),
            Paragraph(title, styles['TableCell']),
            Paragraph(f"<font color='#0891B2'><b>{domain}</b></font>", styles['TableCell'])
        ])

    t_toc = Table(t_toc_data, colWidths=[65, PRINTABLE_WIDTH - 150, 85])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY_NAVY),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_toc)
    story.append(Spacer(1, 10))
    story.append(make_section_divider())
    return story


def generate_pdf():
    """Compiles the master PDF story and writes the document."""
    output_pdf_path = os.path.join(str(PROJECT_ROOT), "docs", "MedOps_Internal_Demo_Technical_Guide.pdf")
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

    print(f"[*] Initializing ReportLab document template at: {output_pdf_path}")
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=MARGIN
    )

    styles = get_custom_styles()
    story = []

    # 1. Cover Page
    print("[*] Generating Cover Page...")
    story.extend(build_cover_page(styles))

    # 2. Table of Contents
    print("[*] Generating Table of Contents...")
    story.extend(build_table_of_contents(styles))
    story.append(PageBreak())

    # 3. Sections 1 to 4
    print("[*] Generating Sections 1 to 4...")
    story.extend(build_section_1(styles))
    story.append(PageBreak())
    story.extend(build_section_2(styles))
    story.append(PageBreak())
    story.extend(build_section_3(styles))
    story.append(PageBreak())
    story.extend(build_section_4(styles))
    story.append(PageBreak())

    # 4. Section 5: All 21 Modules
    print("[*] Generating Section 5 (All 21 Modules)...")
    story.extend(build_section_5(styles))
    story.append(PageBreak())

    # 5. Sections 6 to 9
    print("[*] Generating Sections 6 to 9...")
    story.extend(build_section_6(styles))
    story.append(PageBreak())
    story.extend(build_section_7(styles))
    story.append(PageBreak())
    story.extend(build_section_8(styles))
    story.append(PageBreak())
    story.extend(build_section_9(styles))
    story.append(PageBreak())

    # 6. Sections 10 to 14
    print("[*] Generating Sections 10 to 14...")
    story.extend(build_section_10(styles))
    story.append(PageBreak())
    story.extend(build_section_11(styles))
    story.append(PageBreak())
    story.extend(build_section_12(styles))
    story.append(PageBreak())
    story.extend(build_section_13(styles))
    story.append(PageBreak())
    story.extend(build_section_14(styles))
    story.append(PageBreak())

    # 7. Sections 15 to 18
    print("[*] Generating Sections 15 to 18...")
    story.extend(build_section_15(styles))
    story.append(PageBreak())
    story.extend(build_section_16(styles))
    story.append(PageBreak())
    story.extend(build_section_17(styles))
    story.append(PageBreak())
    story.extend(build_section_18(styles))

    # Build the document using NumberedCanvas
    print(f"[*] Building PDF story with NumberedCanvas (Total Flowables: {len(story)})...")
    start_time = time.time()
    doc.build(story, canvasmaker=NumberedCanvas)
    duration = time.time() - start_time
    print(f"[+] Master PDF built successfully in {duration:.2f} seconds!")

    # Validate output with pypdf
    import pypdf
    reader = pypdf.PdfReader(output_pdf_path)
    total_pages = len(reader.pages)
    file_size_kb = os.path.getsize(output_pdf_path) / 1024.0

    print(f"[OK] Verification Results:")
    print(f"    - Target Path: {output_pdf_path}")
    print(f"    - Total Pages: {total_pages}")
    print(f"    - File Size: {file_size_kb:.1f} KB")

    return output_pdf_path, total_pages, file_size_kb


if __name__ == "__main__":
    generate_pdf()
