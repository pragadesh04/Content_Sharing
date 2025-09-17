from typing import Optional

from pydantic import BaseModel, Field


class course_payment(BaseModel):
  username : str = Field(...)
  title : str = Field(...)
  payment_status : bool = Field(...)


class User(BaseModel):
  username : str = Field(..., min_length = 3)
  age : int = Field(..., gt = 16)
  phone : str = Field(..., min_length=10, max_length=10)
  location : str = Field(...)
  
  
class Update_User(BaseModel):
  username : Optional[str] = Field("None", min_length = 3)
  age : Optional[int] = Field(None, gt = 16)
  phone : Optional[str] = Field(None, min_length=10, max_length=10)
  location : Optional[str] = Field(None)