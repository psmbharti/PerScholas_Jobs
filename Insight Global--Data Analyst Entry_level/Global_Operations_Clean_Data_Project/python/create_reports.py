import pandas as pd
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.enums import TA_CENTER

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER

heading_style = styles["Heading2"]

body_style = styles["BodyText"]
body_style.fontSize = 8
body_style.leading = 10


def csv_to_pdf(csv_file, pdf_file, title):

    df = pd.read_csv(csv_file)

    document = SimpleDocTemplate(
        pdf_file,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    elements = []

    # -------------------------------------------------
    # Report Title
    # -------------------------------------------------

    elements.append(Paragraph(title, title_style))
    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now().strftime('%d-%b-%Y %H:%M')}",
            body_style,
        )
    )

    elements.append(
        Paragraph(
            f"<b>Total Records:</b> {len(df)}",
            body_style,
        )
    )

    elements.append(Spacer(1, 15))

    # -------------------------------------------------
    # Create Table
    # -------------------------------------------------

    table_data = []

    # Header
    table_data.append(
        [
            Paragraph(f"<b>{col}</b>", body_style)
            for col in df.columns
        ]
    )

    # Data
    for _, row in df.iterrows():

        table_data.append(

            [
                Paragraph(str(value), body_style)
                for value in row
            ]

        )

    # -------------------------------------------------
    # Column Widths
    # -------------------------------------------------

    num_cols = len(df.columns)

    page_width = 760

    col_width = page_width / num_cols

    table = Table(
        table_data,
        repeatRows=1,
        colWidths=[col_width] * num_cols
    )

    # -------------------------------------------------
    # Table Style
    # -------------------------------------------------

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.royalblue),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("FONTSIZE", (0,0), (-1,-1), 8),

            ("GRID", (0,0), (-1,-1), 0.5, colors.black),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),

            ("VALIGN", (0,0), (-1,-1), "TOP"),

            ("BOTTOMPADDING", (0,0), (-1,0), 8),

            ("TOPPADDING", (0,1), (-1,-1), 4),

        ])

    )

    elements.append(table)

    document.build(elements)

    print(f"{pdf_file} created successfully")


# -----------------------------------------
# Data Quality Report
# -----------------------------------------

csv_to_pdf(

    "data/quality/validation_report.csv",

    "reports/Data_Quality_Report.pdf",

    "Global Operations Data Quality Report"

)


# -----------------------------------------
# UAT Report
# -----------------------------------------

csv_to_pdf(

    "data/quality/uat_test_results.csv",

    "reports/UAT_Test_Report.pdf",

    "Global Operations UAT Test Report"

)


# -----------------------------------------
# Risk Report
# -----------------------------------------

csv_to_pdf(

    "data/governance/data_risk_register.csv",

    "reports/Risk_Assessment_Report.pdf",

    "Global Operations Risk Assessment Report"

)
