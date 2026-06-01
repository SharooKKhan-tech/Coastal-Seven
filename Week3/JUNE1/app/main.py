from fastapi import FastAPI
from app.routers.employee_router import router

app = FastAPI()

app.include_router(router)