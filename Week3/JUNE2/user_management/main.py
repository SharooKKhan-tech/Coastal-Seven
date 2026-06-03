from fastapi import FastAPI
from schemas.user import (
    CreateUser,
    UpdateUser,
    UserResponse
)

app = FastAPI()

# Dummy Database

users = []


@app.post(
    "/users",
    response_model=UserResponse
)
def create_user(user: CreateUser):

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "address": user.address
    }

    users.append(new_user)

    return new_user


@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int):

    return users[user_id - 1]


@app.patch("/users/{user_id}")
def update_user(
    user_id: int,
    user: UpdateUser
):

    stored_user = users[user_id - 1]

    if user.name is not None:
        stored_user["name"] = user.name

    if user.age is not None:
        stored_user["age"] = user.age

    if user.email is not None:
        stored_user["email"] = user.email

    return {
        "message": "User Updated",
        "user": stored_user
    }