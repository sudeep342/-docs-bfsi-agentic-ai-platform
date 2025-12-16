def send_email(customer, pdf_path, status):
    print("\n📧 EMAIL SENT")
    print(f"To: {customer['name']} <registered-email>")
    print(f"Status: {status.upper()}")
    print(f"Attachment: {pdf_path}")
    print("--------------------------------------------------\n")
