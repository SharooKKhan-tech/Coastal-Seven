from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    role: str
    salary: float

class EmployeeResponse(BaseModel):
    id: int
    name: str
    role: str