import os
import pypdf
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_ats_resume(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.45 * inch,
        rightMargin=0.45 * inch,
        topMargin=0.32 * inch,
        bottomMargin=0.32 * inch
    )

    # ATS Optimized Color Palette
    primary_color = colors.HexColor('#0f172a')   # Deep Slate
    accent_color = colors.HexColor('#0284c7')    # Professional Blue
    text_color = colors.HexColor('#1e293b')      # Charcoal Text
    sub_color = colors.HexColor('#475569')       # Muted Slate

    # Typography / Paragraph Styles
    name_style = ParagraphStyle(
        'NameStyle',
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=19,
        alignment=TA_CENTER,
        textColor=primary_color
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=sub_color
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=accent_color,
        spaceBefore=4,
        spaceAfter=1,
        keepWithNext=True
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=primary_color
    )

    body_regular = ParagraphStyle(
        'BodyRegular',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        alignment=TA_LEFT,
        textColor=text_color
    )

    body_italic = ParagraphStyle(
        'BodyItalic',
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10.5,
        textColor=sub_color
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        leftIndent=10,
        textColor=text_color
    )

    story = []

    # 1. Header
    story.append(Paragraph("YADAM GOPIKRISHNA", name_style))
    story.append(Spacer(1, 1.5))
    
    contact_text = (
        "<b>Andhra Pradesh, India</b> | "
        "<b>Phone:</b> +91 6281415416 | "
        "<b>Email:</b> <a href='mailto:gopikrishnayadam53@gmail.com' color='#0284c7'>gopikrishnayadam53@gmail.com</a> | "
        "<b>GitHub:</b> <a href='https://github.com/yadamgopikrishna' color='#0284c7'>github.com/yadamgopikrishna</a>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(HRFlowable(width="100%", thickness=1, color=accent_color, spaceBefore=3, spaceAfter=3))

    # 2. Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_text = (
        "<b>Computer Science Engineering student (2024–2028)</b> with strong foundations in Python, "
        "Data Structures & Algorithms, Machine Learning, and Full-Stack Web Development (React, Node, Express, MongoDB, Flask). "
        "Demonstrated experience engineering multimodal AI assistants, citizen welfare recommendation portals, and agricultural marketplaces. "
        "Dedicated to architecting efficient, high-impact software solutions."
    )
    story.append(Paragraph(summary_text, body_regular))
    story.append(Spacer(1, 2))

    # 3. Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    skills_data = [
        [Paragraph("<b>Programming Languages:</b>", body_bold), Paragraph("Python (Advanced, Data Science, OOP), JavaScript (ES6+), Dart, SQL", body_regular)],
        [Paragraph("<b>AI & Machine Learning:</b>", body_bold), Paragraph("Scikit-learn, Google GenAI SDK, Prompt Engineering, NLP, NumPy, Pandas, Vector Search", body_regular)],
        [Paragraph("<b>Full-Stack Development:</b>", body_bold), Paragraph("React.js, Node.js, Express.js, Flask, HTML5, CSS3, REST APIs, JSON Architecture", body_regular)],
        [Paragraph("<b>Databases & Tools:</b>", body_bold), Paragraph("MongoDB Atlas, Relational SQL, Git, GitHub, VS Code, Google Colab, Jupyter Notebook", body_regular)],
        [Paragraph("<b>Core CS Fundamentals:</b>", body_bold), Paragraph("Data Structures & Algorithms (DSA), OOP, Database Management Systems (DBMS), OS", body_regular)]
    ]
    t_skills = Table(skills_data, colWidths=[1.6 * inch, 5.9 * inch])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.8),
        ('TOPPADDING', (0,0), (-1,-1), 0.8),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 2))

    # 4. Education
    story.append(Paragraph("EDUCATION", section_heading))
    
    edu_table_data = [
        [
            Paragraph("<b>Bachelor of Technology (B.Tech) — Computer Science & Engineering</b>", body_bold),
            Paragraph("<b>2024 – 2028 (Currently Pursuing)</b>", ParagraphStyle('Right1', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("DVR & HS MIC College of Technology | Kanchikacherla, Andhra Pradesh", body_italic),
            Paragraph("<b>CGPA: 7.5 / 10.0</b>", ParagraphStyle('RightScore1', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ],
        [
            Paragraph("<b>Intermediate (Class XII / Higher Secondary — MPC)</b>", body_bold),
            Paragraph("<b>2022 – 2024</b>", ParagraphStyle('Right2', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("Maruthi Junior College | Koduru, Andhra Pradesh", body_italic),
            Paragraph("<b>Score: 80.0%</b>", ParagraphStyle('RightScore2', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ],
        [
            Paragraph("<b>Secondary School Certificate (Class X / SSC)</b>", body_bold),
            Paragraph("<b>2021 – 2022</b>", ParagraphStyle('Right3', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("Andhra Pradesh Residential School (APRS) | Puligadda, Andhra Pradesh", body_italic),
            Paragraph("<b>Score: 85.0%</b>", ParagraphStyle('RightScore3', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ]
    ]
    t_edu = Table(edu_table_data, colWidths=[5.4 * inch, 2.1 * inch])
    t_edu.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.6),
        ('TOPPADDING', (0,0), (-1,-1), 0.6),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_edu)
    story.append(Spacer(1, 2))

    # 5. Featured Projects
    story.append(Paragraph("FEATURED PROJECTS", section_heading))

    # Project 1: OG AI
    p1_head = [
        [Paragraph("<b>OG AI — Multimodal Conversational Assistant</b> | <i>Python, Google GenAI SDK, NLP, FastAPI</i>", body_bold),
         Paragraph("<a href='https://github.com/yadamgopikrishna/chatbot' color='#0284c7'><b>[GitHub]</b></a>", ParagraphStyle('PR1', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p1_head, colWidths=[6.5 * inch, 1.0 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5), ('TOPPADDING', (0,0), (-1,-1), 0.5)]))
    story.append(Paragraph("• Architected multimodal AI system utilizing Google GenAI API for contextual reasoning, document QA, and image analysis.", bullet_style))
    story.append(Paragraph("• Built token management, conversation memory caching, and structured JSON parsing for rapid frontend responses.", bullet_style))
    story.append(Spacer(1, 1.5))

    # Project 2: Sarkari Scheme Finder
    p2_head = [
        [Paragraph("<b>Sarkari Scheme Finder — Citizen Welfare Portal</b> | <i>MERN (React, Node, Express, MongoDB)</i>", body_bold),
         Paragraph("<a href='https://github.com/yadamgopikrishna/sarkari-scheme-finder' color='#0284c7'><b>[GitHub]</b></a>", ParagraphStyle('PR2', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p2_head, colWidths=[6.5 * inch, 1.0 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5), ('TOPPADDING', (0,0), (-1,-1), 0.5)]))
    story.append(Paragraph("• Developed full-stack web application matching citizens with central/state schemes based on demographic & financial eligibility.", bullet_style))
    story.append(Paragraph("• Built dynamic search indexing, modular REST API endpoints, and clean responsive UI with instant filtering.", bullet_style))
    story.append(Spacer(1, 1.5))

    # Project 3: AgriSeed Marketplace
    p3_head = [
        [Paragraph("<b>AgriSeed — Agricultural Marketplace Platform</b> | <i>Python, Flask, MongoDB Atlas, JavaScript</i>", body_bold),
         Paragraph("<a href='https://github.com/yadamgopikrishna/AgriSeed-Marketplace' color='#0284c7'><b>[GitHub]</b></a>", ParagraphStyle('PR3', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p3_head, colWidths=[6.5 * inch, 1.0 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5), ('TOPPADDING', (0,0), (-1,-1), 0.5)]))
    story.append(Paragraph("• Built direct farmer-to-supplier e-commerce platform connecting agricultural growers with certified seed producers.", bullet_style))
    story.append(Paragraph("• Implemented secure vendor authentication, product catalog filters, real-time inventory updates, and order workflows.", bullet_style))
    story.append(Spacer(1, 1.5))

    # Project 4: Student Performance Prediction
    p4_head = [
        [Paragraph("<b>Student Academic Performance Predictor</b> | <i>Python, Scikit-learn, Pandas, NumPy, Matplotlib</i>", body_bold),
         Paragraph("<b>[ML Model]</b>", ParagraphStyle('PR4', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p4_head, colWidths=[6.5 * inch, 1.0 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0.5), ('TOPPADDING', (0,0), (-1,-1), 0.5)]))
    story.append(Paragraph("• Engineered supervised regression model achieving 88%+ accuracy in predicting student examination performance.", bullet_style))
    story.append(Paragraph("• Conducted exploratory data analysis (EDA), feature scaling, model cross-validation, and metric evaluation.", bullet_style))
    story.append(Spacer(1, 2))

    # 6. Certifications
    story.append(Paragraph("PROFESSIONAL CERTIFICATIONS", section_heading))
    certs_data = [
        [Paragraph("• <b>Mastering ReactJS</b> & <b>Learning Express Web App Development</b> — Infosys Springboard (Oct 2026)", bullet_style)],
        [Paragraph("• <b>Building AI Agents with MongoDB</b> & <b>MongoDB Vector Search</b> — MongoDB / Credly (Verified, 2026)", bullet_style)],
        [Paragraph("• <b>Python 101 for Data Science</b> — IBM / Cognitive Class & Developer Skills Network", bullet_style)],
        [Paragraph("• <b>JavaScript Essentials 1, CSS Essentials & HTML Essentials</b> — Cisco Networking Academy", bullet_style)]
    ]
    t_certs = Table(certs_data, colWidths=[7.5 * inch])
    t_certs.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0.6),
        ('TOPPADDING', (0,0), (-1,-1), 0.6),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_certs)

    doc.build(story)
    
    # Verification
    reader = pypdf.PdfReader(output_path)
    page_count = len(reader.pages)
    print(f"Generated ATS Resume at: {output_path} | Page Count: {page_count}")
    assert page_count == 1, f"ERROR: Resume is {page_count} pages, expected 1 page!"

if __name__ == '__main__':
    build_ats_resume('assets/Resume.pdf')
    build_ats_resume('Resume.pdf')
