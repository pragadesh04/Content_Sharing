from pydantic import BaseModel, Field

class Courses(BaseModel):
    title : str = Field(..., description = "Course title")
    description : str = Field(description = "Provide the course description (optional)")
    
    schedule : str = Field(..., description="Course schedule date")
    duration : float = Field(...)
    price : float = Field(...)