import os
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
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch
    )

    styles = getSampleStyleSheet()

    # Custom Clean ATS Styles
    primary_color = colors.HexColor('#0f172a')
    accent_color = colors.HexColor('#0284c7')
    text_color = colors.HexColor('#1e293b')
    sub_color = colors.HexColor('#475569')

    name_style = ParagraphStyle(
        'NameStyle',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=23,
        alignment=TA_CENTER,
        textColor=primary_color
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        alignment=TA_CENTER,
        textColor=sub_color
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=accent_color,
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=primary_color
    )

    body_regular = ParagraphStyle(
        'BodyRegular',
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        alignment=TA_LEFT,
        textColor=text_color
    )

    body_italic = ParagraphStyle(
        'BodyItalic',
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11.5,
        textColor=sub_color
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        leftIndent=12,
        textColor=text_color
    )

    story = []

    # 1. Header
    story.append(Paragraph("YADAM GOPIKRISHNA", name_style))
    story.append(Spacer(1, 2))
    
    contact_text = (
        "<b>Andhra Pradesh, India</b> | "
        "<b>Phone:</b> +91 6281415416 | "
        "<b>Email:</b> <a href='mailto:gopikrishnayadam53@gmail.com' color='#0284c7'>gopikrishnayadam53@gmail.com</a> | "
        "<b>GitHub:</b> <a href='https://github.com/yadamgopikrishna' color='#0284c7'>github.com/yadamgopikrishna</a>"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.2, color=accent_color, spaceBefore=2, spaceAfter=5))

    # 2. Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_text = (
        "<b>Computer Science Engineering student (2024–2028)</b> with strong foundations in Python development, "
        "Data Structures & Algorithms, Machine Learning, and Full-Stack Web Development (MERN, Flask, REST APIs). "
        "Proven experience engineering production-grade multimodal AI conversational agents, personalized government welfare recommendation portals, "
        "and agricultural marketplace platforms. Skilled in data modeling with MongoDB Atlas and SQL. Committed to building practical, "
        "high-impact software and intelligent systems."
    )
    story.append(Paragraph(summary_text, body_regular))
    story.append(Spacer(1, 4))

    # 3. Education
    story.append(Paragraph("EDUCATION", section_heading))
    
    # B.Tech
    btech_table_data = [
        [
            Paragraph("<b>Bachelor of Technology (B.Tech) — Computer Science & Engineering</b>", body_bold),
            Paragraph("<b>2024 – 2028 (Currently Pursuing)</b>", ParagraphStyle('Right', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("DVR & HS MIC College of Technology | Kanchikacherla, Andhra Pradesh", body_italic),
            Paragraph("<b>CGPA: 7.5 / 10.0</b>", ParagraphStyle('RightScore', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ]
    ]
    t1 = Table(btech_table_data, colWidths=[5.3 * inch, 2.2 * inch])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t1)
    story.append(Spacer(1, 3))

    # Intermediate
    inter_table_data = [
        [
            Paragraph("<b>Intermediate (Class XII / Higher Secondary — MPC)</b>", body_bold),
            Paragraph("<b>2022 – 2024</b>", ParagraphStyle('Right', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("Maruthi Junior College | Koduru, Andhra Pradesh", body_italic),
            Paragraph("<b>Score: 80.0%</b>", ParagraphStyle('RightScore', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ]
    ]
    t2 = Table(inter_table_data, colWidths=[5.3 * inch, 2.2 * inch])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t2)
    story.append(Spacer(1, 3))

    # Schooling
    school_table_data = [
        [
            Paragraph("<b>Secondary School Certificate (Class X / SSC)</b>", body_bold),
            Paragraph("<b>2021 – 2022</b>", ParagraphStyle('Right', parent=body_bold, alignment=TA_RIGHT))
        ],
        [
            Paragraph("Andhra Pradesh Residential School (APRS) | Puligadda, Andhra Pradesh", body_italic),
            Paragraph("<b>Score: 85.0%</b>", ParagraphStyle('RightScore', parent=body_regular, alignment=TA_RIGHT, fontName='Helvetica-Bold'))
        ]
    ]
    t3 = Table(school_table_data, colWidths=[5.3 * inch, 2.2 * inch])
    t3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t3)
    story.append(Spacer(1, 4))

    # 4. Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    skills_data = [
        [Paragraph("<b>Programming:</b>", body_bold), Paragraph("Python (Advanced, Data Science, OOP), JavaScript (ES6+), Dart, SQL", body_regular)],
        [Paragraph("<b>AI & Machine Learning:</b>", body_bold), Paragraph("Scikit-learn, Google GenAI SDK, NLP, Prompt Engineering, Predictive Modeling, NumPy, Pandas, Vector Search", body_regular)],
        [Paragraph("<b>Web & Full-Stack:</b>", body_bold), Paragraph("React.js, Node.js, Express.js, Flask, HTML5, CSS3, REST APIs, Responsive Web Architecture", body_regular)],
        [Paragraph("<b>Databases & Tools:</b>", body_bold), Paragraph("MongoDB Atlas, Relational SQL, Git, GitHub, VS Code, Google Colab, Jupyter Notebook", body_regular)],
        [Paragraph("<b>CS Fundamentals:</b>", body_bold), Paragraph("Data Structures & Algorithms (DSA), Object-Oriented Programming (OOP), DBMS, Operating Systems", body_regular)]
    ]
    t_skills = Table(skills_data, colWidths=[1.7 * inch, 5.8 * inch])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 4))

    # 5. Featured Projects
    story.append(Paragraph("FEATURED PROJECTS", section_heading))

    # Project 1: OG AI
    p1_head = [
        [Paragraph("<b>OG AI — Production Multimodal AI Assistant</b> | <i>Python 3.12, Google GenAI SDK, NLP, Flask/FastAPI</i>", body_bold),
         Paragraph("<a href='https://github.com/yadamgopikrishna/chatbot' color='#0284c7'><b>[GitHub Repo]</b></a>", ParagraphStyle('PR1', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p1_head, colWidths=[6.2 * inch, 1.3 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
    story.append(Paragraph("• Architected a multimodal AI system integrating Google GenAI API for text reasoning, document intelligence, and image forensics.", bullet_style))
    story.append(Paragraph("• Implemented conversational memory persistence, prompt engineering templates, and structured JSON outputs for developer tools.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 2: Sarkari Scheme Finder
    p2_head = [
        [Paragraph("<b>Sarkari Scheme Finder — Government Scheme Recommendation Portal</b> | <i>MERN Stack (React, Node, Express, MongoDB)</i>", body_bold),
         Paragraph("<a href='https://github.com/yadamgopikrishna/sarkari-scheme-finder' color='#0284c7'><b>[GitHub Repo]</b></a>", ParagraphStyle('PR2', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p2_head, colWidths=[6.2 * inch, 1.3 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
    story.append(Paragraph("• Developed full-stack portal matching Indian citizens with Central & State government schemes tailored to their demographic and financial profile.", bullet_style))
    story.append(Paragraph("• Engineered dynamic eligibility calculation engine with category filtering, state query indexes, and responsive UI components.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 3: AgriSeed Marketplace
    p3_head = [
        [Paragraph("<b>AgriSeed — Online Agricultural Marketplace</b> | <i>Python, Flask, MongoDB Atlas, JavaScript, HTML5/CSS3</i>", body_bold),
         Paragraph("<a href='https://github.com/yadamgopikrishna/AgriSeed-Marketplace' color='#0284c7'><b>[GitHub Repo]</b></a>", ParagraphStyle('PR3', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p3_head, colWidths=[6.2 * inch, 1.3 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
    story.append(Paragraph("• Built an agricultural direct-to-farmer e-commerce platform eliminating intermediary costs by connecting growers with certified seed producers.", bullet_style))
    story.append(Paragraph("• Integrated secure vendor authentication, real-time inventory management, category search filters, and responsive checkout interface.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 4: Student Performance Prediction
    p4_head = [
        [Paragraph("<b>Student Academic Performance Predictive System</b> | <i>Python, Scikit-learn, Pandas, NumPy, Matplotlib</i>", body_bold),
         Paragraph("<b>[Machine Learning]</b>", ParagraphStyle('PR4', parent=body_regular, alignment=TA_RIGHT))]
    ]
    story.append(Table(p4_head, colWidths=[6.2 * inch, 1.3 * inch], style=[('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 1), ('TOPPADDING', (0,0), (-1,-1), 1)]))
    story.append(Paragraph("• Developed supervised machine learning regression and classification pipeline achieving 88%+ accuracy on academic outcome forecasting.", bullet_style))
    story.append(Paragraph("• Conducted exploratory data analysis (EDA), feature engineering, cross-validation, hyperparameter tuning, and metric visualization.", bullet_style))
    story.append(Spacer(1, 4))

    # 6. Certifications
    story.append(Paragraph("PROFESSIONAL CERTIFICATIONS", section_heading))
    certs_data = [
        [Paragraph("• <b>Mastering ReactJS</b> — Infosys Springboard / Wingspan (Verified Credential, Oct 2026)", bullet_style)],
        [Paragraph("• <b>Learning Express Web Application Development</b> — Infosys Springboard / Wingspan (Oct 2026)", bullet_style)],
        [Paragraph("• <b>Online MongoDB Training Course & Building AI Agents with MongoDB</b> — MongoDB / Credly (Verified, 2026)", bullet_style)],
        [Paragraph("• <b>Building AI-Powered Search with MongoDB Vector Search</b> — MongoDB / Credly (Verified, 2026)", bullet_style)],
        [Paragraph("• <b>Python 101 for Data Science</b> — IBM / Cognitive Class & IBM Developer Skills Network", bullet_style)],
        [Paragraph("• <b>JavaScript Essentials 1, CSS Essentials & HTML Essentials</b> — Cisco Networking Academy", bullet_style)]
    ]
    t_certs = Table(certs_data, colWidths=[7.5 * inch])
    t_certs.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_certs)

    doc.build(story)
    print(f"Generated ATS Resume at: {output_path}")

if __name__ == '__main__':
    build_ats_resume('assets/Resume.pdf')
    build_ats_resume('Resume.pdf')
