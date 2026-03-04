from fastapi import APIRouter
from datetime import datetime
from app.core.database import sessionLocal
from app.pydantic_models.UserModel import  UserModel
from app.core.security import hash_password
from app.models.User import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/register")
async def register_user(user: UserModel):
    email = user.email
    password = user.password
    hashed_password = hash_password(password)

    db = sessionLocal()
    new_user = User(
        email=email,
        hashed_password=hashed_password,
        created_at=datetime.now(),
    )

    db.add(new_user)
    db.commit()
    db.close()