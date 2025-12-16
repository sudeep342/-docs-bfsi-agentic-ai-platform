import json

def verify_customer(phone):
    with open('data/crm_data.json', 'r') as f:
        crm = json.load(f)


    if phone in crm:
        return {**crm[phone], "verified": True}
    return {"verified": False}