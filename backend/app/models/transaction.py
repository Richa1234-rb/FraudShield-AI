from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.session import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    merchant = Column(
        String(100),
        nullable=False
    )

    location = Column(
        String(100),
        nullable=False
    )

    merchant_encoded = Column(
        Integer,
        default=0
    )

    location_encoded = Column(
        Integer,
        default=0
    )

    transaction_hour = Column(
        Integer,
        default=0
    )

    fraud_score = Column(
        Float,
        default=0.0
    )

    prediction = Column(
        String(20),
        default="Safe"
    )

    status = Column(
        String(20),
        default="Approved"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User",
        back_populates="transactions"
    )