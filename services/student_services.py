from bson import ObjectId
from database import students_collection
from datetime import datetime
from utils.student_utils import now
from typing import List

currentTime = now()


def create_student(student_data: dict):
    student_data['updated_at'] = currentTime
    student_data['created_at'] = currentTime
    result = students_collection.insert_one(student_data)
    student_data["id"] = str(result.inserted_id)
    return student_data


def get_all_students():
    student = []
    for stu in students_collection.find():
        stu["_id"] = str(stu["_id"])
        student.append(stu)

    return student


def get_particular_student(student_id: str):
    student = students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        student["_id"] = str(student["_id"])

    return student


def update_student(student_id: str, update_student: dict):
    update_student['updated_at'] = currentTime
    result = students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": update_student}
    )
    return result.modified_count > 0


def delete_student(student_id: str):
    result = students_collection.delete_one({"_id": student_id})
    return result.deleted_count > 0


def search_student(query: str) -> List[dict]:
    result = students_collection.find({
        "$or": [
            {"name": {"$regex": query, "$options": 'i'}},
            {"grade": {"$regex": query, "$options": "i"}}
        ]
    })

    student = []
    for stu in result:
        stu["_id"] = str(stu["_id"])
        student.append(stu)

    return student
