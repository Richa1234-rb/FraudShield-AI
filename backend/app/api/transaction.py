from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db

from app.models.transaction import Transaction
from app.models.user import User

from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse
)

from app.ml.predictor import predict_transaction

from app.utils.encoder import (
    encode_merchant,
    encode_location,
    current_hour
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post(
    "/",
    response_model=TransactionResponse
)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    merchant_code = encode_merchant(
        transaction.merchant
    )

    location_code = encode_location(
        transaction.location
    )

    hour = current_hour()

    result = predict_transaction(
        transaction.amount
    )

    new_transaction = Transaction(
        user_id=current_user.id,

        amount=transaction.amount,

        merchant=transaction.merchant,

        location=transaction.location,

        merchant_encoded=merchant_code,

        location_encoded=location_code,

        transaction_hour=hour,

        prediction=result["prediction"],

        fraud_score=result["fraud_score"],

        status=result["status"]
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


@router.get(
    "/my",
    response_model=list[TransactionResponse]
)
def my_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    ).all()