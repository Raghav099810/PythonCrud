from fastapi import APIRouter, HTTPException
import constants.student_constants as status_code
from services.student_services import (
    create_student,
    get_all_students,
    get_particular_student,
    update_student,
    delete_student,
    search_student
)
from schemas import StudentCreate, Student, BaseResponse
from typing import List

router = APIRouter(prefix="/student", tags=Student)


def create(student: StudentCreate) -> BaseResponse[Student]:
    new_student = create_student(student.dict())
    if not new_student:
        raise HTTPException(
            status_code=status_code.HTTP_INTERNAL_SERVER_ERROR,
            detail="Failed to create a student"
        )
    return BaseResponse[Student](
        data=Student(**new_student),
        message="Student created successfully",
        statusCode=status_code.HTTP_CREATED
    )


def get_all() -> BaseResponse[List[Student]]:
    students = get_all_students()
    if not students:
        raise HTTPException(
            status_code=status_code.HTTP_NOT_FOUND,
            detail="No student data found"
        )
    return BaseResponse[List[Student]](
        data=[Student(**stu) for stu in students],
        message="Data returned successfully",
        statusCode=status_code.HTTP_OK
    )


def get_particular(student_id: str) -> BaseResponse[Student]:
    student = get_particular_student(student_id=student_id)
    if not student:
        raise HTTPException(
            status_code=status_code.HTTP_NOT_FOUND,
            detail="Student detail not found"
        )
    return BaseResponse[Student](
        data=Student(**student),
        message="Student returned successfully",
        statusCode=status_code.HTTP_OK
    )


def update(student_id: str, student: StudentCreate) -> BaseResponse[Student]:
    updated = update_student(student_id=student_id,
                             update_student=student.dict())
    if not updated:
        raise HTTPException(
            status_code=status_code.HTTP_BAD_REQUEST,
            detail="Cannot update the student"
        )
    return BaseResponse[None](
        data=Student(**updated),
        message="Student updated successfully",
        statusCode=status_code.HTTP_ACCEPTED
    )


def delete(student_id: str) -> BaseResponse[None]:
    deleted = delete_student(student_id=student_id)
    if not deleted:
        raise HTTPException(
            status_code=status_code.HTTP_NOT_FOUND,
            detail="Student not found"
        )
    return BaseResponse[None](
        data=None,
        message="Student deleted successfully",
        statusCode=status_code.HTTP_OK
    )


def search(query: str) -> BaseResponse[Student]:
    student_result = search_student(query=query)
    if not student_result:
        raise HTTPException(
            status_code=status_code.HTTP_NOT_FOUND, detail="No such student found")

    return BaseResponse[List[Student]](
        data=[Student(**stu) for stu in student_result],
        message="Search successful",
        statusCode=status_code.HTTP_OK
    )
