from fastapi import APIRouter, HTTPException

from App.schemas.user_schema import User, Update_User, course_payment
from App.dependencies.database import courses_collection
from App.dependencies.database import users_collection
from App.dependencies.data_manipulations import serialiser

router = APIRouter(
  tags = ["approvals"],
  prefix = "/admin/approvals"
)


@router.post("/user-approvals")
def add_user(user_request : User):
  users = users_collection()

  is_user = users.find_one({"username" : user_request.username})
  
  try:
    phone = int(user_request.phone)
  except:
    raise HTTPException(status_code = 422, detail = "enter the valid mobile number")
  
  if not is_user:
    result = users.insert_one({
      "username" : user_request.username, "age" : user_request.age,
      "phone" : phone ,"location" : user_request.location
    })
    return (str(result.inserted_id))
  else:
    raise HTTPException(status_code = 409, detail = "User already exists - update to add courses")
  

@router.put("/user-approval")
def update_users_courses(courses_opted : course_payment = None):
  users = users_collection()
  courses = courses_collection()
  
  
  is_user = users.find_one({"username" : courses_opted.username})
  is_course_in_user = users.find_one({"username" : courses_opted.username, "courses.title" : courses_opted.title})
  is_courses = courses.find_one({"title" : courses_opted.title.lower()})
  
  if not is_user:
    raise HTTPException(status_code = 404, detail = "no user found")
  if not is_courses:
    raise HTTPException(status_code = 404, detail = "No course with that name is found")
  if is_course_in_user:
    users.update_one(
      {
        "username" : courses_opted.username,
        "courses.title" : courses_opted.title
      },
      {"$set" : {"courses.$.payment_status" : courses_opted.payment_status}}
    )
    return courses_opted
  if courses_opted:
    users.update_one(
      {"username" : courses_opted.username},
      {"$addToSet" : {"courses" : {"title" : courses_opted.title, "payment_status" : courses_opted.payment_status}}}
    )
  
  return courses_opted


@router.put("/user-update")
def users_detail_update(updated_request : Update_User):
  users = users_collection()
  
  try:
    phone = int(updated_request.phone)
    updated_request.phone = phone
  except Exception as e:
    raise HTTPException(status_code = 422, detail = f"enter the valid mobile number")
  
  updated_requests = updated_request.model_dump(exclude_unset = True)
  
  is_user = users.find_one({"username" : updated_request.username})
  
  if is_user:
    users.update_one(
      {"username" : updated_request.username},
      {"$set" : updated_requests}
    )
  return updated_request