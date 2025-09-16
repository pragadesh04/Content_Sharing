from pymongo import MongoClient

from dotenv import load_dotenv
import os

load_dotenv()

mongo_url = os.environ.get("mongo_url")

client = MongoClient(mongo_url)
db = client["database"]

users = db.users
admin = db.admin
courses = db.courses

if admin.find_one({}) is None:
    admin.insert_one({"username" : "admin", "password" : "123asd"})
    print({"detail" : "the Admin account is not present and added"})

else:
    print({"detail" : "the Admin account is present"})

def user_collection():
    return users
def admin_collection():
    return admin
def courses_collection():
    return courses