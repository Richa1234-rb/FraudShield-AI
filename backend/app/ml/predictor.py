import joblib
import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "fraud_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

# -----------------------------
# Load model and scaler once
# -----------------------------
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


def predict_transaction(amount: float):
    """
    Predict fraud using trained ML model.
    """

    # Dummy feature vector
    # Dataset has 30 input features.
    features = [0] * 30

    # Time
    features[0] = 0

    # Amount
    features[29] = amount

    # Scale
    scaled = scaler.transform([features])

    prediction = model.predict(scaled)[0]

    probability = model.predict_proba(scaled)[0][1]

    result = "Fraud" if prediction == 1 else "Safe"

    status = "Rejected" if prediction == 1 else "Approved"

    return {
    "prediction": result,
    "fraud_score": round(float(probability), 4),
    "status": status
}