from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.auth.roles import require_admin
from app.database.session import get_db

from app.models.user import User
from app.models.transaction import Transaction

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


# -------------------------------
# Get All Users
# -------------------------------
@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    return db.query(User).all()


# -------------------------------
# Dashboard Summary
# -------------------------------
@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    total_users = db.query(User).count()

    total_transactions = db.query(Transaction).count()

    approved_transactions = db.query(Transaction).filter(
        Transaction.status == "Approved"
    ).count()

    fraud_transactions = db.query(Transaction).filter(
        Transaction.prediction == "Fraud"
    ).count()

    fraud_percentage = 0

    if total_transactions > 0:
        fraud_percentage = round(
            (fraud_transactions / total_transactions) * 100,
            2
        )

    return {
        "total_users": total_users,
        "total_transactions": total_transactions,
        "approved_transactions": approved_transactions,
        "fraud_transactions": fraud_transactions,
        "fraud_percentage": fraud_percentage
    }


# -------------------------------
# High Risk Transactions
# -------------------------------
@router.get("/high-risk")
def high_risk_transactions(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    transactions = db.query(Transaction).filter(
        Transaction.fraud_score >= 0.60
    ).all()

    return transactions


# -------------------------------
# Merchant Fraud Report
# -------------------------------
@router.get("/fraud-report")
def fraud_report(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):

    report = (
        db.query(
            Transaction.merchant,
            func.count(Transaction.id).label("frauds")
        )
        .filter(Transaction.prediction == "Fraud")
        .group_by(Transaction.merchant)
        .all()
    )

    return report