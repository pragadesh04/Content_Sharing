from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Moderator(BaseModel):
  username : str = Field(...)
  email : EmailStr = Field(...)
  password : str = Field(..., min_length = 6)
  
class Update_Moderator(BaseModel):
  username : Optional[str] = Field(None)
  email : Optional[EmailStr] = Field(None)
  password : Optional[str] = Field(None, min_length = 6)