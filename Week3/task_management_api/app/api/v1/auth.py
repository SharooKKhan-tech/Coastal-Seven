from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.schemas.user import (
    UserCreate,
    UserLogin
)

from app.services.user_service import UserService
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

user_service = UserService()
auth_service = AuthService()

@router.post("/register")
async def register(
    data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    user = await user_service.create_user(
        db,
        data
    )

    return user

@router.post("/login")
async def login(
    data: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    token = await auth_service.login(
        db,
        data.email,
        data.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }