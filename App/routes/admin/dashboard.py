from fastapi import APIRouter,HTTPException
from bson.objectid import ObjectId

from App.dependencies.database import courses_collection
from App.dependencies.data_manipulations import serialiser
from App.schemas import course_schema


router = APIRouter(
  tags = ["admin"],
  prefix = "/admin"
)


@router.post("/courses")
def add_courses(courses : course_schema.Courses):
  new_course = {"title" : courses.title.lower(), "description" : courses.description,
              "price" : courses.price, "tutor" : courses.tutor,
              "duration" : courses.duration, "schedule" : courses.schedule
              }
  course = courses_collection()
  result = course.insert_one(new_course)
  new_course["_id"] = str(new_course["_id"])
    
  return {"course" :new_course, "result id" : str(result.inserted_id)}


@router.get("/courses")
def list_courses():
  course = courses_collection().find({})
  courses = list(course)   
  serialised_course = []

  for c in courses:
    serialised_course.append(serialiser(c))
  if not serialised_course:
    raise HTTPException(status_code = 404, detail = "No Course at this time")

  return(serialised_course)


@router.put("/courses")
def update_courses(course_id : str, updated_request : course_schema.Update_Courses):      
  updated_request = updated_request.model_dump(exclude_unset=True)      
  course = courses_collection()
  course.update_one(
        {"_id" : ObjectId(course_id)},
        {"$set" : updated_request}
  )
      
  field, value = next(iter(updated_request.items()))
  result = course.find_one({"_id" : ObjectId(course_id)})
      
  return({"detail" : f"""Successfully Updated "{field}" to "{value}" """, "The Result" : serialiser(result)})


@router.delete("/courses")
def delete_courses(course_id : str):
  course = courses_collection()
  
  if course.find_one({"_id" : ObjectId(course_id)}):
    result = course.delete_one({"_id" : ObjectId(course_id)})
    info, status = result.deleted_count, result.acknowledged
    return{"number of deletions" : info, "Status" : status}
  else:
    return {"detail" : "No data to delete"}