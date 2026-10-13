import os
import pypdf
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_ats_resume(output_path):
    # Physical Paper Standard: Letter format with universal 0.42" printer margins
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.42 * inch,
        rightMargin=0.42 * inch,
        topMargin=0.32 * inch,
        bottomMargin=0.32 * inch
    )

    # Physical Print High-Contrast Executive Palette (Optimized for Laser/Inkjet Printing & ATS Parsers)
    primary_color = colors.HexColor('#000000')    # Pure crisp black for paper contrast
    heading_color = colors.HexColor('#0f2942')    # Deep Executive Navy
    text_color = colors.HexColor('#111827')       # Solid readable body text
    meta_color = colors.HexColor('#374151')       # Dark neutral for metadata
    rule_color = colors.HexColor('#0f2942')       # Crisp divider lines
    link_color = colors.HexColor('#0369a1')       # Professional readable blue (prints sharp dark gray/black)

    # Typography optimized for physical paper readability & ATS extraction
    name_style = ParagraphStyle(
        'PaperName',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        alignment=TA_CENTER,
        textColor=primary_color
    )

    contact_style = ParagraphStyle(
        'PaperContact',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_CENTER,
        textColor=meta_color
    )

    section_heading = ParagraphStyle(
        'PaperSection',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=heading_color,
        spaceBefore=4,
        spaceAfter=1,
        keepWithNext=True
    )

    body_bold = ParagraphStyle(
        'PaperBold',
        fontName='Helvetica-Bold',
        fontSize=8.3,
        leading=10.8,
        textColor=primary_color
    )

    body_regular = ParagraphStyle(
        'PaperRegular',
        fontName='Helvetica',
        fontSize=8.3,
        leading=10.8,
        alignment=TA_LEFT,
        textColor=text_color
    )

    body_italic = ParagraphStyle(
        'PaperItalic',
        fontName='Helvetica-Oblique',
        fontSize=7.8,
        leading=10,
        textColor=meta_color
    )

    bullet_style = ParagraphStyle(
        'PaperBullet',
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.2,
        leftIndent=9,
        textColor=text_color
    )

    story = []

    # 1. Header (Physical Paper Standard: Direct contact info & human-readable URLs)
    story.append(Paragraph("YADAM GOPIKRISHNA", name_style))
    story.append(Spacer(1, 1.5))
    
    contact_line1 = (
        "Andhra Pradesh, India &nbsp;|&nbsp; "
        "Phone: <b>+91 6281415416</b> &nbsp;|&nbsp; "
        "Email: <a href='mailto:gopikrishnayadam53@gmail.com' color='#0369a1'><b>gopikrishnayadam53@gmail.com</b></a>"
    )
    contact_line2 = (
        "GitHub: <a href='https://github.com/yadamgopikrishna' color='#0369a1'><b>github.com/yadamgopikrishna</b></a> &nbsp;|&nbsp; "
        "Portfolio: <a href='https://yadamgopikrishna.github.io/Portfolio/' color='#0369a1'><b>yadamgopikrishna.github.io/Portfolio</b></a>"
    )
    story.append(Paragraph(contact_line1, contact_style))
    story.append(Paragraph(contact_line2, contact_style))
    story.append(HRFlowable(width="100%", thickness=1.2, color=rule_color, spaceBefore=3, spaceAfter=3))

    # 2. Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_text = (
        "<b>Computer Science & Engineering student (2024–2028)</b> specializing in Artificial Intelligence, Machine Learning, and "
        "Full-Stack Web Development. Proven track record engineering production-grade multimodal AI assistants, machine learning predictive pipelines, "
        "citizen welfare recommendation portals, and agricultural marketplaces. Proficient in Python, Scikit-learn, React, Node.js, Express, "
        "MongoDB Atlas, and Streamlit, with a rigorous foundation in algorithms and software engineering."
    )
    story.append(Paragraph(summary_text, body_regular))
    story.append(Spacer(1, 1.5))

    # 3. Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    skills_data = [
        [Paragraph("<b>Programming Languages:</b>", body_bold), Paragraph("Python (Advanced, Data Science, OOP), JavaScript (ES6+), Dart, SQL", body_regular)],
        [Paragraph("<b>AI & Machine Learning:</b>", body_bold), Paragraph("Scikit-learn, Google GenAI SDK, Streamlit, Prompt Engineering, NLP, NumPy, Pandas, Vector Search", body_regular)],
        [Paragraph("<b>Web & Mobile Stack:</b>", body_bold), Paragraph("React.js, Node.js, Express.js, Flask, Flutter, HTML5, CSS3, REST APIs, JSON Architecture", body_regular)],
        [Paragraph("<b>Databases & Cloud Tools:</b>", body_bold), Paragraph("MongoDB Atlas, Relational SQL, Git, GitHub Actions, VS Code, Google Colab, Joblib", body_regular)],
        [Paragraph("<b>Core CS Fundamentals:</b>", body_bold), Paragraph("Data Structures & Algorithms (DSA), OOP, Database Management Systems (DBMS), Operating Systems", body_regular)]
    ]
    t_skills = Table(skills_data, colWidths=[1.55 * inch, 6.1 * inch])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.4),
        ('TOPPADDING', (0,0), (-1,-1), 0.4),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 1.5))

    # 4. Education
    story.append(Paragraph("EDUCATION", section_heading))
    edu_table_data = [
        [
            Paragraph("<b>Bachelor of Technology (B.Tech) — Computer Science & Engineering</b>", body_bold),
            Paragraph("<b>2024 – 2028 (Currently Pursuing)</b>", ParagraphStyle('R1', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("DVR & HS MIC College of Technology | Kanchikacherla, Andhra Pradesh", body_italic),
            Paragraph("<b>CGPA: 7.5 / 10.0</b>", ParagraphStyle('RS1', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ],
        [
            Paragraph("<b>Intermediate (Class XII / Higher Secondary — MPC)</b>", body_bold),
            Paragraph("<b>2022 – 2024</b>", ParagraphStyle('R2', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("Maruthi Junior College | Koduru, Andhra Pradesh", body_italic),
            Paragraph("<b>Board Score: 80.0%</b>", ParagraphStyle('RS2', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ],
        [
            Paragraph("<b>Secondary School Certificate (Class X / SSC)</b>", body_bold),
            Paragraph("<b>2021 – 2022</b>", ParagraphStyle('R3', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("Andhra Pradesh Residential School (APRS) | Puligadda, Andhra Pradesh", body_italic),
            Paragraph("<b>Board Score: 85.0%</b>", ParagraphStyle('RS3', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ]
    ]
    t_edu = Table(edu_table_data, colWidths=[5.45 * inch, 2.2 * inch])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.4),
        ('TOPPADDING', (0,0), (-1,-1), 0.4),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 1.5))

    # 5. Projects (Human-Readable URLs for Paper, Clickable Links for Digital/Online)
    story.append(Paragraph("PROJECTS", section_heading))

    # Project 1: OG AI
    p1_head = [
        [
            Paragraph("<b>OG AI — Multimodal Conversational Assistant</b> | <i>Python, Google GenAI SDK, FastAPI</i>", body_bold),
            Paragraph("<a href='https://github.com/yadamgopikrishna/chatbot' color='#0369a1'>github.com/yadamgopikrishna/chatbot</a>", ParagraphStyle('PURL1', parent=body_italic, alignment=TA_RIGHT, fontSize=7.2))
        ]
    ]
    story.append(Table(p1_head, colWidths=[5.0 * inch, 2.65 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.3), ('TOPPADDING', (0,0), (-1,-1), 0.3)]))
    story.append(Paragraph("• Architected multimodal AI assistant using Google GenAI SDK for contextual reasoning, document QA, and image forensics.", bullet_style))
    story.append(Paragraph("• Implemented real-time SSE streaming, prompt optimization pipelines, and session memory with structured JSON outputs.", bullet_style))
    story.append(Spacer(1, 1.0))

    # Project 2: Student Academic Performance Predictor
    p2_head = [
        [
            Paragraph("<b>AI Student Performance Predictor & Study Planner</b> | <i>Python, Scikit-learn, Streamlit</i>", body_bold),
            Paragraph("<a href='https://github.com/yadamgopikrishna/student-performance-predictor' color='#0369a1'>github.com/yadamgopikrishna/student-performance-predictor</a>", ParagraphStyle('PURL2', parent=body_italic, alignment=TA_RIGHT, fontSize=6.9))
        ]
    ]
    story.append(Table(p2_head, colWidths=[5.0 * inch, 2.65 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.3), ('TOPPADDING', (0,0), (-1,-1), 0.3)]))
    story.append(Paragraph("• Engineered supervised ML regression pipeline (88%+ accuracy) with zero-leakage preprocessing, Joblib serialization, and diagnostics.", bullet_style))
    story.append(Paragraph("• Built dynamic subject intake, automated weakness detection, and interactive 7-day study timetable generator in Streamlit.", bullet_style))
    story.append(Spacer(1, 1.0))

    # Project 3: Sarkari Scheme Finder
    p3_head = [
        [
            Paragraph("<b>Sarkari Scheme Finder — Government Scheme Portal</b> | <i>MERN (React, Node, Express, MongoDB)</i>", body_bold),
            Paragraph("<a href='https://github.com/yadamgopikrishna/sarkari-scheme-finder' color='#0369a1'>github.com/yadamgopikrishna/sarkari-scheme-finder</a>", ParagraphStyle('PURL3', parent=body_italic, alignment=TA_RIGHT, fontSize=7.0))
        ]
    ]
    story.append(Table(p3_head, colWidths=[5.0 * inch, 2.65 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.3), ('TOPPADDING', (0,0), (-1,-1), 0.3)]))
    story.append(Paragraph("• Developed full-stack citizen portal matching Indian citizens with Central & State schemes based on demographic & financial criteria.", bullet_style))
    story.append(Paragraph("• Engineered dynamic eligibility calculation engine, multi-attribute indexing, modular REST APIs, and responsive citizen UI.", bullet_style))
    story.append(Spacer(1, 1.0))

    # Project 4: AgriSeed Marketplace
    p4_head = [
        [
            Paragraph("<b>AgriSeed — Online Agricultural Marketplace</b> | <i>Python, Flask, MongoDB Atlas, JavaScript</i>", body_bold),
            Paragraph("<a href='https://github.com/yadamgopikrishna/AgriSeed-Marketplace' color='#0369a1'>github.com/yadamgopikrishna/AgriSeed-Marketplace</a>", ParagraphStyle('PURL4', parent=body_italic, alignment=TA_RIGHT, fontSize=7.0))
        ]
    ]
    story.append(Table(p4_head, colWidths=[5.0 * inch, 2.65 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.3), ('TOPPADDING', (0,0), (-1,-1), 0.3)]))
    story.append(Paragraph("• Built direct farmer-to-supplier e-commerce platform eliminating intermediary costs by connecting growers with certified producers.", bullet_style))
    story.append(Paragraph("• Implemented secure vendor authentication, product catalog filters, real-time inventory management, and order tracking.", bullet_style))
    story.append(Spacer(1, 1.0))

    # Project 5: TastyHub Mobile App
    p5_head = [
        [
            Paragraph("<b>TastyHub — Mobile Food Discovery & Delivery App</b> | <i>Flutter, Dart, Mobile UI, REST APIs</i>", body_bold),
            Paragraph("<a href='https://github.com/yadamgopikrishna/TastyHub' color='#0369a1'>github.com/yadamgopikrishna/TastyHub</a>", ParagraphStyle('PURL5', parent=body_italic, alignment=TA_RIGHT, fontSize=7.2))
        ]
    ]
    story.append(Table(p5_head, colWidths=[5.0 * inch, 2.65 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.3), ('TOPPADDING', (0,0), (-1,-1), 0.3)]))
    story.append(Paragraph("• Developed cross-platform mobile application with reactive state management for live cart calculations and menu category filtering.", bullet_style))
    story.append(Spacer(1, 1.5))

    # 6. Certifications
    story.append(Paragraph("PROFESSIONAL CERTIFICATIONS", section_heading))
    certs_data = [
        [Paragraph("• <b>Mastering ReactJS</b> & <b>Learning Express Web Application Development</b> — Infosys Springboard (Verified, Oct 2026)", bullet_style)],
        [Paragraph("• <b>Building AI Agents with MongoDB</b> & <b>MongoDB Vector Search</b> — MongoDB / Credly (Verified, 2026)", bullet_style)],
        [Paragraph("• <b>Python 101 for Data Science</b> — IBM / Cognitive Class & Developer Skills Network", bullet_style)],
        [Paragraph("• <b>JavaScript Essentials 1, CSS Essentials & HTML Essentials</b> — Cisco Networking Academy", bullet_style)]
    ]
    t_certs = Table(certs_data, colWidths=[7.65 * inch])
    t_certs.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.4),
        ('TOPPADDING', (0,0), (-1,-1), 0.4),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_certs)

    doc.build(story)
    
    # Strict Verification for Physical 1-Page Printing
    reader = pypdf.PdfReader(output_path)
    page_count = len(reader.pages)
    print(f"Generated Physical Paper ATS Resume at: {output_path} | Page Count: {page_count}")
    assert page_count == 1, f"ERROR: Resume is {page_count} pages, expected strictly 1 physical page!"

if __name__ == '__main__':
    build_ats_resume('assets/Resume.pdf')
    build_ats_resume('Resume.pdf')
