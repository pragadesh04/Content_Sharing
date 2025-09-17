from pydantic import BaseModel, Field

class Login_Utensils(BaseModel):
  username : str = Field(...)
  password : str = Field(...)