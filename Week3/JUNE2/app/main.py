from pydantic import BaseModel,Field,EmailStr,field_validator,model_validator
from typing import List,Optional
class Address(BaseModel):
    city : str
    state : str
    pincode : str
class User(BaseModel):

    username : str
    @field_validator("username")
    def validate_username(cls,value):
        if " " in value:
            raise ValueError(
                "Username cannot contain spaces"
            )

        return value
    name: str 
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        if not value[0].isupper():
            raise ValueError(
                "Name must start with a capital letter"
            )

        return value
    age : int | None = None  
    email : EmailStr
    number : str = Field(
        pattern=r"^[0-9]{10}$"
    )

    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_password_match(self):

        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )

        return self
    address : List[Address]

user = User(
    username = "sharook_khan",
    name="Sharook",
    age="22",
    email="sharook@vvit.com",
    number="8919687218",
    password="sharook123",
    confirm_password="sharook123",
    address=[
        {
        "city": "Vijayawada",
        "state": "Andhra Pradesh",
        "pincode": "520001"
        },
        {
            "city": "HYD",
            "state": "TS",
            "pincode": "520027"
        }
    ]
)

print(user.model_dump())