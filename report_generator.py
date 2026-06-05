from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    risk_percent,
    health_score,
    risk_level,
    recommendations
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Diabetes Risk Analysis Report",
        styles["Title"]
    )

    content.append(title)
    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Risk Probability: {risk_percent:.2f}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Health Score: {health_score}/100",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Category: {risk_level}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    for rec in recommendations:
        content.append(
            Paragraph(
                f"• {rec}",
                styles["Normal"]
            )
        )

    doc.build(content)