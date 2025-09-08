from datetime import datetime
from bson import ObjectId


def now():
    return datetime.now()


def validateName(name: str) -> str:
    if (len(name.strip()) < 3):
        raise ValueError("Name must be atlest 3 characters long")
    if (name.startswith(" ")):
        raise ValueError("Name cannot have space before")
    if (len(name.strip()) > 20):
        raise ValueError("Name is too much lengthy")

    if (len(name) == 0):
        raise ValueError("Name cannot be empty")

    if not name.isalpha:
        raise ValueError("Cannot enter number or special expressions")

    return name


def validateAge(age: int):
    if (age < 3 or age > 25):
        raise ValueError("Enter valid age")
    return age


def validateDob(dob: datetime):
    if (dob > datetime.now()):
        raise ValueError("Enter valid dob")
    return dob


def validate_id(student_id: str):
    return ObjectId.is_valid(student_id)
