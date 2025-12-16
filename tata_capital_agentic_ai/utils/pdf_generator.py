from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from datetime import date
import os

def create_approval_pdf(customer, loan):
    os.makedirs("sanctions", exist_ok=True)
    path = f"sanctions/{customer['name']}_sanction.pdf"

    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    # Brand Header
    c.setFillColor(colors.HexColor("#004B8D"))
    c.rect(0, height - 3*cm, width, 3*cm, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height - 2*cm, "Tata Capital")

    # Title
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - 4*cm, "Loan Sanction Letter")

    c.setFont("Helvetica", 10)
    c.drawRightString(width - 2*cm, height - 5*cm, f"Date: {date.today()}")

    # Customer Info
    c.drawString(2*cm, height - 6.5*cm, f"Customer Name: {customer['name']}")
    c.drawString(2*cm, height - 7.2*cm, f"City: {customer['city']}")

    # Table
    table_y = height - 9*cm
    row_height = 0.9 * cm

    data = [
        ("Loan Amount Approved", f" ₹{loan['approved_amount']}"),
        ("Interest Rate", f"{loan['interest_rate']} % p.a."),
        ("APR", f"{loan['apr']} %"),
        ("Tenure", f"{loan['tenure']} months"),
        ("Processing Fee", f"₹ {loan['processing_fee']}"),
        ("Monthly EMI", f"₹ {loan['emi']}"),
        ("Credit Score", loan["credit_score"]),
        ("KYC Status", "Verified")
    ]

    c.setFont("Helvetica", 10)
    for i, (label, value) in enumerate(data):
        y = table_y - i * row_height
        c.rect(2*cm, y, 6*cm, row_height)
        c.rect(8*cm, y, 6*cm, row_height)
        c.drawString(2.2*cm, y + 0.3*cm, label)
        c.drawString(8.2*cm, y + 0.3*cm, str(value))

    # Footer
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(
        2*cm, 3*cm,
        "This is a system-generated sanction letter and does not require a physical signature."
    )

    c.save()
    return path


def create_rejection_pdf(customer, reason):
    os.makedirs("sanctions", exist_ok=True)
    path = f"sanctions/{customer['name']}_rejection.pdf"

    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height - 3*cm, "Loan Application Update")

    c.setFont("Helvetica", 11)
    c.drawString(2*cm, height - 6*cm, f"Dear {customer['name']},")

    c.drawString(
        2*cm, height - 7.5*cm,
        f"We regret to inform you that your loan application could not be approved."
    )

    c.drawString(2*cm, height - 9*cm, f"Reason: {reason}")

    c.drawString(
        2*cm, height - 11*cm,
        "You may reapply after improving eligibility parameters."
    )

    c.save()
    return path
