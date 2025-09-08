from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

MONGO_URL = "mongodb+srv://raghav:raghav12@cluster0.ej7rq6n.mongodb.net/school_db"

try:
    client = MongoClient(MONGO_URL)
    client.admin.command("ping")
    print("Connected to MongoDB successfully")
    db = client["school_db"]
    students_collection = db["students"]


except ConnectionFailure as e:
    print("Could not connect to MongoDB:", e)
    client = None
    db = None
    students_collection = None
