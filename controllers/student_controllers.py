from fastapi import APIRouter, HTTPException, Depends
import constants.student_constants as status_code
from services.student_services import (
    create_student,
    get_all_students,
    get_particular_student,
    update_student,
    delete_student,
)
from schemas import StudentCreate, Student, BaseResponse, StudentResponse
from fastapi_pagination import Page, paginate, Params

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


def get_all(params: Params = Depends(), search: str = None) -> BaseResponse[Page[StudentResponse]]:
    students = get_all_students(search=search)
    if not students:
        raise HTTPException(
            status_code=status_code.HTTP_NOT_FOUND,
            detail="No student data found"
        )
    paginated_student_data = paginate(
        [StudentResponse(**stu) for stu in students], params=params)
    return BaseResponse[Page[StudentResponse]](
        data=paginated_student_data,
        message="Data returned successfully",
        statusCode=status_code.HTTP_OK
    )


def get_particular(student_id: str) -> BaseResponse[StudentResponse]:
    student = get_particular_student(student_id=student_id)
    if not student:
        raise HTTPException(
            status_code=status_code.HTTP_NOT_FOUND,
            detail="Student detail not found"
        )
    return BaseResponse[StudentResponse](
        data=StudentResponse(**student),
        message="Student returned successfully",
        statusCode=status_code.HTTP_OK
    )


def update(student_id: str, student: StudentCreate) -> BaseResponse[Student]:
    updated = update_student(student_id=student_id,
                             update_student_data=student.dict())
    if not updated:
        raise HTTPException(
            status_code=status_code.HTTP_BAD_REQUEST,
            detail="Cannot update the student"
        )
    return BaseResponse[Student](
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
