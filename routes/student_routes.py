from fastapi import APIRouter
from controllers import student_controllers
from schemas import Student, StudentCreate

student_routes = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@student_routes.post("/", response_model=Student)
def create_student_route(student: StudentCreate):
    return student_controllers.create(student)


@student_routes.get("/", response_model=list[Student])
def get_all_students_route():
    return student_controllers.get_all()


@student_routes.get("/{student_id}", response_model=Student)
def get_student_route(student_id: str):
    return student_controllers.get_particular(student_id)


@student_routes.put("/{student_id}")
def update_student_route(student_id: str, student: StudentCreate):
    return student_controllers.update(student_id, student)


@student_routes.delete("/{student_id}")
def delete_student_route(student_id: str):
    return student_controllers.delete(student_id)
