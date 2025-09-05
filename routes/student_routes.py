from fastapi import APIRouter, Query
from controllers import student_controllers
from schemas import Student, StudentCreate, BaseResponse

student_routes = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@student_routes.post("/", response_model=BaseResponse[Student])
def create_student_route(student: StudentCreate):
    return student_controllers.create(student=student)


@student_routes.get("/", response_model=BaseResponse[list[Student]])
def get_all_students_route():
    return student_controllers.get_all()


@student_routes.get("/{student_id}", response_model=BaseResponse[Student])
def get_student_route(student_id: str):
    return student_controllers.get_particular(student_id=student_id)


@student_routes.put("/{student_id}", response_model=BaseResponse[Student])
def update_student_route(student_id: str, student: StudentCreate):
    return student_controllers.update(student_id=student_id, student=student)


@student_routes.delete("/{student_id}", response_model=BaseResponse[None])
def delete_student_route(student_id: str):
    return student_controllers.delete(student_id=student_id)


@student_routes.get("/search", response_model=BaseResponse[list[Student]])
def search_student_route(query: str = Query(..., description="Search for student")):
    return student_controllers.search(query=query)
