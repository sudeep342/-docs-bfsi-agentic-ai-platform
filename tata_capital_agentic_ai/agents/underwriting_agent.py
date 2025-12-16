from services.credit_bureau import fetch_credit_score

def evaluate_loan(customer, amount):
    score = fetch_credit_score()
    limit = customer["preapproved_limit"]

    interest_rate = 12.5
    tenure = 24
    processing_fee_rate = 0.02
    apr = 14.1
    emi = int(amount / tenure + (amount * interest_rate / 100) / 12)

    if score < 700:
        return {"status": "rejected", "reason": "Low credit score, below eligibilty threshold", "credit_score": score}

    if amount <= limit:
        processing_fee = int(amount * processing_fee_rate)
        emi  = int((amount + processing_fee) /tenure)
        return {
           "status": "approved",
            "approved_amount": amount,
            "credit_score": score,
            "interest_rate": interest_rate,
            "apr": apr,
            "tenure": tenure,
            "processing_fee": processing_fee,
            "emi": emi
        }

    return {"status": "rejected", "reason": "Amount exceeds eligibility", "credit_score": score}
