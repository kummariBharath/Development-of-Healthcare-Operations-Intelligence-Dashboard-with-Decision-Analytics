"""
MedOps Technical Documentation - ReportLab Styles & Canvas Configuration
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

# Page Dimensions (A4)
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 36.0  # 0.5 inch = 36 points
PRINTABLE_WIDTH = PAGE_WIDTH - (2 * MARGIN)  # 523.27 points

# Enterprise Color Palette
PRIMARY_NAVY = colors.HexColor('#0F172A')   # Slate 900
BRAND_TEAL = colors.HexColor('#0891B2')     # Cyan 600
BRAND_CYAN = colors.HexColor('#06B6D4')     # Cyan 500
ACCENT_BLUE = colors.HexColor('#2563EB')    # Blue 600
ACCENT_AMBER = colors.HexColor('#D97706')   # Amber 600
ACCENT_ROSE = colors.HexColor('#E11D48')    # Rose 600
ACCENT_EMERALD = colors.HexColor('#059669') # Emerald 600
BG_LIGHT_SLATE = colors.HexColor('#F8FAFC') # Slate 50
BG_CARD = colors.HexColor('#F1F5F9')        # Slate 100
BORDER_COLOR = colors.HexColor('#CBD5E1')   # Slate 300
TEXT_MAIN = colors.HexColor('#1E293B')      # Slate 800
TEXT_MUTED = colors.HexColor('#64748B')     # Slate 500


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas that accumulates pages and writes dynamic
    'Page X of Y' footers and running chapter headers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, total_pages):
        self.saveState()
        
        # Running Header
        self.setFont('Helvetica-Bold', 7.5)
        self.setFillColor(PRIMARY_NAVY)
        self.drawString(MARGIN, PAGE_HEIGHT - 26, "MEDOPS HEALTHCARE INTELLIGENCE")
        self.setFont('Helvetica', 7.5)
        self.setFillColor(TEXT_MUTED)
        self.drawString(MARGIN + 165, PAGE_HEIGHT - 26, "|   Technical Architecture & Internal Demonstration Handbook")
        
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.5)
        self.line(MARGIN, PAGE_HEIGHT - 30, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 30)

        # Running Footer
        self.line(MARGIN, 32, PAGE_WIDTH - MARGIN, 32)
        self.setFont('Helvetica-Bold', 7.5)
        self.setFillColor(ACCENT_ROSE)
        self.drawString(MARGIN, 22, "CONFIDENTIAL & PROPRIETARY")
        self.setFont('Helvetica', 7.5)
        self.setFillColor(TEXT_MUTED)
        self.drawString(MARGIN + 130, 22, " --  Internal Demo & Verification Reference Only")
        
        page_str = f"Page {self._pageNumber} of {total_pages}"
        self.setFont('Helvetica-Bold', 7.5)
        self.setFillColor(PRIMARY_NAVY)
        self.drawRightString(PAGE_WIDTH - MARGIN, 22, page_str)

        self.restoreState()


def get_custom_styles():
    """Builds a cohesive stylesheet tailored for technical handbooks."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='DocTitle',
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY_NAVY,
        alignment=TA_LEFT,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='DocSubtitle',
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=BRAND_TEAL,
        alignment=TA_LEFT,
        spaceAfter=15
    ))

    styles.add(ParagraphStyle(
        name='SecHeading1',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=PRIMARY_NAVY,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='SecHeading2',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=BRAND_TEAL,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='SecHeading3',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=TEXT_MAIN,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='BodyCustom',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_MAIN,
        spaceAfter=5
    ))

    styles.add(ParagraphStyle(
        name='BodyCustomJustify',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_MAIN,
        alignment=TA_JUSTIFY,
        spaceAfter=5
    ))

    styles.add(ParagraphStyle(
        name='BulletCustom',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.5,
        textColor=TEXT_MAIN,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        name='TableHeader',
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10,
        textColor=colors.white,
        alignment=TA_CENTER
    ))

    styles.add(ParagraphStyle(
        name='TableCell',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=TEXT_MAIN
    ))

    styles.add(ParagraphStyle(
        name='TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=PRIMARY_NAVY
    ))

    styles.add(ParagraphStyle(
        name='TableCellCode',
        fontName='Courier',
        fontSize=7.0,
        leading=8.5,
        textColor=PRIMARY_NAVY
    ))

    styles.add(ParagraphStyle(
        name='CodeInline',
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=PRIMARY_NAVY
    ))

    styles.add(ParagraphStyle(
        name='CalloutText',
        fontName='Helvetica',
        fontSize=8.0,
        leading=11.5,
        textColor=TEXT_MAIN
    ))

    styles.add(ParagraphStyle(
        name='CalloutTitle',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=PRIMARY_NAVY,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='MentorQ',
        fontName='Helvetica-Bold',
        fontSize=9.0,
        leading=12.5,
        textColor=PRIMARY_NAVY,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='MentorA',
        fontName='Helvetica',
        fontSize=8.3,
        leading=11.8,
        textColor=TEXT_MAIN,
        spaceAfter=4
    ))

    return styles


def make_callout(title, text, callout_type='note', styles=None):
    """Generates a professional callout box with a colored left border."""
    if styles is None:
        styles = get_custom_styles()

    border_colors = {
        'note': BRAND_TEAL,
        'important': ACCENT_BLUE,
        'warning': ACCENT_AMBER,
        'caution': ACCENT_ROSE,
        'success': ACCENT_EMERALD,
    }
    bg_colors = {
        'note': colors.HexColor('#F0FDFA'),
        'important': colors.HexColor('#EFF6FF'),
        'warning': colors.HexColor('#FFFBEB'),
        'caution': colors.HexColor('#FFF1F2'),
        'success': colors.HexColor('#ECFDF5'),
    }

    b_color = border_colors.get(callout_type, BRAND_TEAL)
    bg_color = bg_colors.get(callout_type, colors.HexColor('#F0FDFA'))

    content = [
        Paragraph(f"<b>{title.upper()}</b>", styles['CalloutTitle']),
        Paragraph(text, styles['CalloutText'])
    ]

    t = Table([[content]], colWidths=[PRINTABLE_WIDTH])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_color),
        ('BOX', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('LINEBEFORE', (0, 0), (0, -1), 3.5, b_color),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    return t


def make_code_block(code_text, language="Python", styles=None):
    """Generates a styled code block with dark slate header and light monospace content."""
    if styles is None:
        styles = get_custom_styles()

    header_para = Paragraph(f"<b>SOURCE CODE / LOGIC ({language})</b>", styles['TableHeader'])
    code_para = Paragraph(f"<font face='Courier' size='7'>{code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>&nbsp;&nbsp;')}</font>", styles['BodyCustom'])

    t = Table([[header_para], [code_para]], colWidths=[PRINTABLE_WIDTH])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY_NAVY),
        ('BACKGROUND', (0, 1), (-1, 1), BG_LIGHT_SLATE),
        ('BOX', (0, 0), (-1, -1), 0.8, PRIMARY_NAVY),
        ('TOPPADDING', (0, 0), (-1, 0), 3),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
        ('TOPPADDING', (0, 1), (-1, 1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 5),
        ('LEFTPADDING', (0, 1), (-1, 1), 8),
        ('RIGHTPADDING', (0, 1), (-1, 1), 8),
    ]))
    return t


def make_section_divider():
    """Returns a subtle horizontal divider between major sections."""
    return HRFlowable(width="100%", thickness=1, color=BORDER_COLOR, spaceBefore=10, spaceAfter=10)
