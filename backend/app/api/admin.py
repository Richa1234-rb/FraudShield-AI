from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.roles import require_admin
from app.database.session import get_db
from app.models.user import User

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin)
):
    users = db.query(User).all()

    return users