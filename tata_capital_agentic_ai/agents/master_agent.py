from agents.sales_agent import sales_conversation
from agents.verification_agent import verify_customer
from agents.underwriting_agent import evaluate_loan
from agents.sanction_agent import generate_sanction
from services.email_service import send_email

def master_agent_flow(phone, requested_amount):
    sales = sales_conversation(requested_amount)
    customer = verify_customer(phone)

    if not customer["verified"]:
        return {"status": "rejected", "reason": "KYC Failed"}

    loan = evaluate_loan(customer, requested_amount)
    pdf = generate_sanction(customer, loan)

    send_email(customer, pdf, loan["status"])

    if loan["status"] == "approved":
        return {
            "status": "approved",
            "kyc_status": "verified",
            "credit_score": loan["credit_score"],
            "approved_amount": loan["approved_amount"],
            "interest_rate": f"{loan['interest_rate']}%",
            "apr": f"{loan['apr']}%",
            "processing_fee": loan["processing_fee"],
            "emi": loan["emi"],
            "sanction_letter_pdf": pdf
        }

    return {
        "status": "rejected",
        "credit_score": loan["credit_score"],
        "reason": loan["reason"],
        "rejection_letter_pdf": pdf
    }