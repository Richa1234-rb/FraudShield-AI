import random


def predict_transaction(amount: float):

    if amount < 1000:
        score = random.uniform(0.01, 0.20)

    elif amount < 5000:
        score = random.uniform(0.20, 0.60)

    else:
        score = random.uniform(0.60, 0.99)

    prediction = "Fraud" if score > 0.60 else "Safe"

    status = "Rejected" if prediction == "Fraud" else "Approved"

    return {
        "prediction": prediction,
        "fraud_score": round(score, 2),
        "status": status
    }