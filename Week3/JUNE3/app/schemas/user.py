from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age : int

    model_config = {
        "from_attributes": True
    }


class UpdateUser(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age : int | None = None