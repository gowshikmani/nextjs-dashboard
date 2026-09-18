import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
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
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 762, "ECONOMICS QUARTERLY EXAM EXPECTED QUESTIONS")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, 754, 576, 754)

        # Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 42, 576, 42)
        
        self.setFont("Helvetica", 8)
        self.drawString(36, 28, "2026 - 2027 Academic Session")
        self.drawRightString(576, 28, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def create_pdf(filename="Economics_Quarterly_Exam_Expected_Questions.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#2563EB"),
        spaceAfter=15
    )

    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=0,
        spaceAfter=0
    )

    cell_no = ParagraphStyle(
        'CellNo',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        alignment=1, # Center
        textColor=colors.HexColor("#334155")
    )

    cell_question = ParagraphStyle(
        'CellQuestion',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#1E293B")
    )

    cell_chapter = ParagraphStyle(
        'CellChapter',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        alignment=1, # Center
        textColor=colors.HexColor("#1E40AF")
    )

    # Question Data
    data_2mark = [
        ("1", "Define/Meaning of Macro Economics", "Ch 1"),
        ("2", "What is Mixed Economy?", "Ch 1"),
        ("3", "What are Stock and Flow variables? (give example)", "Ch 1"),
        ("4", "What is Circular Flow of Income?", "Ch 1"),
        ("5", "Define National Income (any one definition)", "Ch 2"),
        ("6", "What is Per Capita Income?", "Ch 2"),
        ("7", "What is GDP?", "Ch 2"),
        ("8", "What is Full Employment?", "Ch 3"),
        ("9", "State Say's Law of Market", "Ch 3"),
        ("10", "What is Effective Demand?", "Ch 3"),
        ("11", "What is Consumption Function?", "Ch 4"),
        ("12", "Define Multiplier", "Ch 4"),
        ("13", "What is Accelerator Principle?", "Ch 4"),
        ("14", "Give the meaning of Money", "Ch 5"),
        ("15", "Define Inflation", "Ch 5"),
        ("16", "What is Trade Cycle?", "Ch 5"),
        ("17", "What is a Commercial Bank?", "Ch 6"),
        ("18", "What is Demonetisation?", "Ch 6"),
        ("19", "What is NABARD?", "Ch 6"),
        ("20", "Define Balance of Trade", "Ch 7"),
    ]

    data_3mark = [
        ("1", "Distinguish between Capitalism and Socialism", "Ch 1"),
        ("2", "State the features of Mixed Economy", "Ch 1"),
        ("3", "Distinguish between Stock and Flow variables (with examples)", "Ch 1"),
        ("4", "State the methods of measuring National Income", "Ch 2"),
        ("5", "Difficulties in measuring National Income (any three)", "Ch 2"),
        ("6", "Distinguish between GDP and GNP", "Ch 2"),
        ("7", "Explain the types of Unemployment (any three)", "Ch 3"),
        ("8", "Distinguish between Classicism and Keynesianism", "Ch 3"),
        ("9", "Distinguish between Consumption Function and Investment Function", "Ch 4"),
        ("10", "Factors influencing Investment", "Ch 4"),
        ("11", "Explain Super Multiplier", "Ch 4"),
        ("12", "Explain the types of Inflation", "Ch 5"),
        ("13", "State the measures to control Inflation", "Ch 5"),
        ("14", "Distinguish between Deflation and Disinflation", "Ch 5"),
        ("15", "State the functions of Commercial Banks (any three)", "Ch 6"),
        ("16", "Explain credit creation by commercial banks (brief)", "Ch 6"),
        ("17", "Methods of credit control by Central Bank (any three)", "Ch 6"),
        ("18", "Distinguish between Balance of Trade and Balance of Payments", "Ch 7"),
        ("19", "State the gains from International Trade", "Ch 7"),
        ("20", "State the objectives of SAARC", "Ch 8"),
    ]

    data_5mark = [
        ("1", "Explain the features, merits and demerits of Capitalism", "Ch 1"),
        ("2", "Explain the features, merits and demerits of Socialism", "Ch 1"),
        ("3", "Explain the features, merits and demerits of Mixed Economy", "Ch 1"),
        ("4", "Explain the methods of measuring National Income in detail", "Ch 2"),
        ("5", "Explain the importance of National Income Analysis", "Ch 2"),
        ("6", "Explain the difficulties in measuring National Income", "Ch 2"),
        ("7", "Explain Keynes' Theory of Employment and Income", "Ch 3"),
        ("8", "Compare Classical and Keynesian theories of employment", "Ch 3"),
        ("9", "Explain the Consumption Function (with diagram)", "Ch 4"),
        ("10", "Explain the concept of Multiplier (with diagram)", "Ch 4"),
        ("11", "Explain the Accelerator Principle in detail", "Ch 4"),
        ("12", "Explain the causes, effects of Inflation and measures to control it", "Ch 5"),
        ("13", "Explain the Quantity Theory of Money", "Ch 5"),
        ("14", "Explain the Trade Cycle and its phases", "Ch 5"),
        ("15", "Explain the functions of Commercial Banks in detail", "Ch 6"),
        ("16", "Explain the functions of Central Bank (RBI)", "Ch 6"),
        ("17", "Explain the role of NABARD in agricultural credit", "Ch 6"),
        ("18", "Explain the theories of International Trade", "Ch 7"),
        ("19", "Explain the factors determining Exchange Rate / role of FDI", "Ch 7"),
        ("20", "Explain the functions of IMF and World Bank", "Ch 8"),
    ]

    story = []

    # Title Block
    story.append(Paragraph("ECONOMICS EXPECTED QUESTIONS", title_style))
    story.append(Paragraph("QUARTERLY EXAM • 2026 TO 2027", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0F172A"), spaceAfter=15))

    def build_table(header_title, badge_color, questions_data):
        # Section Header Banner
        header_p = Paragraph(f"<b>{header_title}</b>", section_style)
        header_table = Table([[header_p]], colWidths=[540])
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F1F5F9")),
            ('PADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LINELEFT', (0, 0), (0, -1), 4, badge_color),
        ]))
        
        # Table Content
        table_rows = [
            [
                Paragraph("<b>#</b>", cell_no),
                Paragraph("<b>Question Description</b>", cell_question),
                Paragraph("<b>Chapter</b>", cell_chapter)
            ]
        ]
        
        for no, q, ch in questions_data:
            table_rows.append([
                Paragraph(no, cell_no),
                Paragraph(q, cell_question),
                Paragraph(ch, cell_chapter)
            ])

        content_table = Table(table_rows, colWidths=[35, 435, 70])
        
        t_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F8FAFC")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#334155")),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('ALIGN', (0, 0), (0, -1), 'CENTER'),
            ('ALIGN', (2, 0), (2, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor("#CBD5E1")),
            ('LINEBELOW', (0, 1), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ]
        
        # Row striping
        for i in range(1, len(table_rows)):
            if i % 2 == 0:
                t_style.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor("#F8FAFC")))
                
        content_table.setStyle(TableStyle(t_style))
        
        return [header_table, Spacer(1, 4), content_table, Spacer(1, 14)]

    # Add 2-Mark Section
    story.extend(build_table("TOP 20 EXPECTED 2-MARK QUESTIONS", colors.HexColor("#16A34A"), data_2mark))
    
    # Add 3-Mark Section
    story.extend(build_table("TOP 20 EXPECTED 3-MARK QUESTIONS", colors.HexColor("#2563EB"), data_3mark))
    
    # Add 5-Mark Section
    story.extend(build_table("TOP 20 EXPECTED 5-MARK QUESTIONS", colors.HexColor("#D97706"), data_5mark))

    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == "__main__":
    create_pdf()