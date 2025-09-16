from fastapi import APIRouter,HTTPException

from App.dependencies.database import courses_collection
from App.dependencies.data_manipulations import serialiser
from App.schemas import course_schema


router = APIRouter(
    tags = ["admin"],
    prefix = "/admin"
)


@router.post("/courses")
def add_courses(courses : course_schema.Courses):
    new_course = {"title" : courses.title, "description" : courses.description,
                  "price" : courses.price, "duration" : courses.duration,
                  "schedule" : courses.schedule
                  }
    
    print(new_course)
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