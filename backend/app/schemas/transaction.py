from pydantic import BaseModel


class TransactionCreate(BaseModel):
    amount: float
    merchant: str
    location: str


class TransactionResponse(BaseModel):
    id: int
    amount: float
    merchant: str
    location: str
    prediction: str
    fraud_score: float
    status: str

    class Config:
        from_attributes = True