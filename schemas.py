from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Generic, TypeVar, Optional
from utils.student_utils import validateAge, validateName
from fastapi_pagination import Page


class StudentInfoClass(BaseModel):
    name: str = Field(..., description="Enter name")
    age: int = Field(..., description="Enter age")
    grade: str = Field(..., min_length=2, max_length=3,
                       description="Enter valid grade")
    dob: datetime

    @field_validator("name")
    def validate_name(cls, v):
        return validateName(v)

    @field_validator("age")
    def validate_age(cls, v):
        return validateAge(v)


class StudentCreate(StudentInfoClass):
    pass


class Student(StudentInfoClass):
    created_at: datetime | None = None
    updated_at: datetime | None = None


# Base Response Model
T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    data: Optional[T] = None
    message: str
    statusCode: int
