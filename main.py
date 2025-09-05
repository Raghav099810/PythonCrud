from fastapi import FastAPI
from routes.student_routes import student_routes
from fastapi_pagination import add_pagination

app = FastAPI()

app.include_router(
    student_routes,
    prefix="/students",
    tags=["Students"]
)

add_pagination(app)
