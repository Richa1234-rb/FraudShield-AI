from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.session import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

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
        String(150),
        nullable=False
    )

    location = Column(
        String(100),
        nullable=False
    )

    prediction = Column(
        String(20),
        default="Unknown"
    )

    fraud_score = Column(
        Float,
        default=0.0
    )

    status = Column(
        String(30),
        default="Pending"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User",
        back_populates="transactions"
    )