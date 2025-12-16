from utils.pdf_generator import create_approval_pdf, create_rejection_pdf

def generate_sanction(customer, loan):
    if loan["status"] == "approved":
        return create_approval_pdf(customer, loan)
    else:
        return create_rejection_pdf(customer, loan["reason"])
