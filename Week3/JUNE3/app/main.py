from fastapi import FastAPI, Depends , HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.user import User
from app.schemas.user import (
    CreateUser,
    UserResponse,
    UpdateUser
)

app = FastAPI()

@app.post(
    "/users",
    response_model=UserResponse
)
async def create_user(
    user: CreateUser,
    db: AsyncSession = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(new_user)

    await db.commit()

    await db.refresh(new_user)

    return new_user

@app.get(
    "/users",
    response_model=list[UserResponse]
)
async def get_users(
    db: AsyncSession = Depends(get_db)
):

    stmt = select(User)

    result = await db.execute(stmt)

    users = result.scalars().all()

    return users

@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):

    stmt = select(User).where(
        User.id == user_id
    )

    result = await db.execute(stmt)

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@app.patch(
    "/users/{user_id}",
    response_model=UserResponse
)
async def update_user(
    user_id: int,
    user_data: UpdateUser,
    db: AsyncSession = Depends(get_db)
):

    stmt = select(User).where(
        User.id == user_id
    )

    result = await db.execute(stmt)

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if user_data.name is not None:
        user.name = user_data.name

    if user_data.email is not None:
        user.email = user_data.email

    if user_data.age is not None:
        user.age = user_data.age

    await db.commit()

    await db.refresh(user)

    return user

@app.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):

    stmt = select(User).where(
        User.id == user_id
    )

    result = await db.execute(stmt)

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    await db.delete(user)

    await db.commit()

    return {
        "message": "User deleted successfully"
    }