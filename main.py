from fastapi import FastAPI
from routes.student_routes import student_routes

app = FastAPI()

app.include_router(
    student_routes,
    prefix="/students",
    tags=["Students"]
)
