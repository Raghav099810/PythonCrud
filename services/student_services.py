from bson import ObjectId
from database import students_collection
from utils.student_utils import now
from typing import List
from pymongo import ReturnDocument

currentTime = now()


def create_student(student_data: dict):
    student_data['updated_at'] = currentTime
    student_data['created_at'] = currentTime
    result = students_collection.insert_one(student_data)
    student_data["id"] = str(result.inserted_id)
    return student_data


def get_all_students(search: str = None):
    query = {}
    if search:
        query = {
            "$or": [
                {"name": {"$regex": search, "$options": 'i'}},
                {"grade": {"$regex": search, "$options": 'i'}}
            ]
        }
    student = []
    for stu in students_collection.find(query):
        stu["_id"] = str(stu["_id"])
        student.append(stu)

    return student


def get_particular_student(student_id: str):
    student = students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        student["_id"] = str(student["_id"])

    return student


def update_student(student_id: str, update_student_data: dict):
    update_student_data['updated_at'] = currentTime
    result = students_collection.find_one_and_update(
        {"_id": ObjectId(student_id)},
        {"$set": update_student_data},
        return_document=ReturnDocument.AFTER
    )
    if result:
        result["_id"] = str(result["_id"])
    return result


def delete_student(student_id: str):
    result = students_collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0
