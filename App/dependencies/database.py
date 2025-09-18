from pymongo import MongoClient
from dotenv import load_dotenv
import os

from App.dependencies.authentication_helpers import hash_password
load_dotenv()

telegram_api_token = os.environ.get("telegram_bot_token")
print(telegram_api_token)

mongo_url = os.environ.get("mongo_url")
password = os.environ.get("admin_pass")

client = MongoClient(mongo_url)
db = client["database"]

users = db.users
admin = db.admin
mods = db.mods
courses = db.courses

users.create_index("username", unique = True)
admin.create_index("username", unique = True)
courses.create_index("title", unique = True)
mods.create_index("username", unique = True)
if admin.find_one({}) is None:
  admin.insert_one({"username" : "admin", "password" : f"{hash_password(password)}"})
  print({"detail" : "the Admin account is not present and added"})

else:
  print({"detail" : "the Admin account is present"})

def users_collection():
  return users
def admins_collection():
  return admin
def courses_collection():
  return courses
def mods_collection():
  return mods