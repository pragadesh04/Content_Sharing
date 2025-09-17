from App.dependencies import authentication_helpers
from App.schemas.login_schemas import Login_Utensils
from App.dependencies.database import admins_collection, mods_collection

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags = ["logins"])

@router.post("/login")
def login(login_request : OAuth2PasswordRequestForm = Depends()):
  admins = admins_collection()
  mods = mods_collection()
  
  in_admins = admins.find_one({"username" : login_request.username})
  in_mods = mods.find_one({"username" : login_request.username})
  
  if in_admins:
    admin_pass = admins.find_one({"username" : login_request.username}).get("password")
    if authentication_helpers.dehash_password(login_request.password, admin_pass):
      access_token = authentication_helpers.create_access_token({"sub" : login_request.username, "role" : "admin"})
      print({"sub" : login_request.username, "role" : "admin"})
      return {"access_token" : access_token, "token_type" : "Bearer"}
    else:
      raise HTTPException(status_code = 400, detail = "Incorrect Password")
    
    
  elif in_mods:
    mods_pass = mods.find_one({"username" : login_request.username}).get("password")
    if authentication_helpers.dehash_password(login_request.password, mods_pass):
      access_token = authentication_helpers.create_access_token({"sub" : login_request.username, "role" : "mod"})
      return {"access_token" : access_token, "token_type" : "Bearer"}
    else:
      raise HTTPException(status_code = 400, detail = "Incorrect Password")
    
  else:
    raise HTTPException(status_code = 404, detail = "user not found")