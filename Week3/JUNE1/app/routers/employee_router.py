from fastapi import APIRouter, status, HTTPException
from app.services.employee_service import employees
from app.schemas.employee_schema import Employee, EmployeeResponse

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Employee API is running"}

@router.get("/employees", response_model=list[EmployeeResponse])
def get_employees():
    return employees

@router.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

@router.get("/search")
def search_employee(name: str):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee

    return {"message": "Employee not found"}

@router.post(
    "/employees",
    status_code=status.HTTP_201_CREATED
)
def create_employee(employee: Employee):

    for emp in employees:
        if emp["id"] == employee.id:
            raise HTTPException(
                status_code=400,
                detail="Employee ID already exists"
            )

    employees.append(employee.model_dump())

    return {
        "message": "Employee created successfully",
        "employee": employee
    }