from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    field_validator,
    model_validator,
    ConfigDict
)

# -------------------
# Nested Model
# -------------------

class Address(BaseModel):
    city: str
    state: str

    pincode: str = Field(
        pattern=r"^[0-9]{6}$"
    )


# -------------------
# Create User
# -------------------

class CreateUser(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=50
    )

    age: int = Field(
        ge=18,
        le=60
    )

    email: EmailStr

    password: str = Field(
        min_length=8
    )

    confirm_password: str

    address: Address

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Sharook Khan",
                "age": 22,
                "email": "sharook@gmail.com",
                "password": "password123",
                "confirm_password": "password123",
                "address": {
                    "city": "Vijayawada",
                    "state": "Andhra Pradesh",
                    "pincode": "520001"
                }
            }
        }
    )

    # field_validator

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        if not value[0].isupper():
            raise ValueError(
                "Name must start with capital letter"
            )

        return value

    # model_validator

    @model_validator(mode="after")
    def validate_passwords(self):

        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )

        return self


# -------------------
# Update User
# -------------------

class UpdateUser(BaseModel):

    name: str | None = None
    age: int | None = None
    email: EmailStr | None = None


# -------------------
# Response Schema
# -------------------

class UserResponse(BaseModel):

    id: int
    name: str
    age: int
    email: EmailStr
    address: Address