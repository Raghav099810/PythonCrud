from fastapi import APIRouter, HTTPException
from services.student_services import (
    create_student,
    get_all_students,
    get_particular_student,
    update_student,
    delete_student
)
from schemas import StudentCreate, Student

router = APIRouter(prefix="/student", tags=Student)


def create(student: StudentCreate):
    new_student = create_student(student.dict())
    return Student(**new_student)


def get_all():
    students = get_all_students()
    return [Student(**stu) for stu in students]


def get_particular(student_id: str):
    student = get_particular_student(student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student detail not found")

    return Student(**student)


def update(student_id: str, student: StudentCreate):
    update = update_student(student_id=student_id,
                            update_student=student.dict())

    if not update:
        raise HTTPException(
            status_code=404, detail="Can not update the student")
    return {"message": "Student updated successfully"}


def delete(student_id: str):
    deleted = delete_student(student_id=student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
