from pydantic import BaseModel
from datetime import datetime


class StudentInfoClass(BaseModel):
    name: str
    age: int
    grade: str
    dob: datetime


class StudentCreate(StudentInfoClass):
    pass


class Student(StudentInfoClass):
    pass
