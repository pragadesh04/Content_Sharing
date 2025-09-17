from pydantic import BaseModel, Field
from typing import Optional

class Courses(BaseModel):
  title : str = Field(..., description = "Course title")
  description : Optional[str] = Field(None, description = "Provide the course description (optional)")
  tutor : str = Field(...)
    
  schedule : str = Field(..., description="Course schedule date")
  duration : float = Field(...)
  price : float = Field(...)
      
class Update_Courses(BaseModel):
  title : Optional[str] = Field(None, description = "Course title")
  description : Optional[str] = Field(None, description = "Provide the course description (optional)")
  tutor : Optional[str] = Field(None, description = "Provide the course description (optional)")

      
  schedule : Optional[str] = Field(None, description="Course schedule date")
  duration : Optional[float] = Field(None)
  price : Optional[float] = Field(None)