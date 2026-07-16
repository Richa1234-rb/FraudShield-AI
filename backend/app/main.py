from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.admin import router as admin_router
from app.database.init_db import init_db

# Create database tables
init_db()

app = FastAPI(
    title="FraudShield AI",
    version="1.0.0",
    description="AI Powered Financial Fraud Detection System"
)

# Routers
app.include_router(auth_router)
app.include_router(admin_router)


@app.get("/")
def root():
    return {
        "message": "🚀 FraudShield AI Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }