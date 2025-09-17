from fastapi import APIRouter, HTTPException, Depends


from App.dependencies.database import admins_collection
from App.dependencies.database import mods_collection
from App.schemas.moderator_schema import Moderator
from App.schemas.moderator_schema import Update_Moderator
from App.dependencies.authentication_helpers import hash_password, get_current_user

router = APIRouter(
  tags = ["moderators"],
  prefix = "/moderators"
)


@router.post("/moderators")
def add_mod(mod_request : Moderator, admin_details : dict = Depends(get_current_user)):
  if admin_details.get("role") == "admin":
    mods = mods_collection()
    is_mods = mods.find_one({"$or" : [{"username" : mod_request.username}, {"email" : mod_request.email}]})
    
    if is_mods:
      raise HTTPException(status_code = 409, detail = "Mod is already exists")

    mod_request.password = hash_password(mod_request.password)
    
    result = mods.insert_one(mod_request.model_dump())
    return(str(result.inserted_id))
  else:
    raise HTTPException(status_code = 401, detail = "required admin rights")

@router.put('/moderators')
def update_mod(update_request : Update_Moderator, admin_details : dict = Depends(get_current_user)):
  if admin_details.get("role") == "admin" or admin_details.get("role") == "mod":
    mod_data = update_request.model_dump(exclude_unset = True)
    mods = mods_collection()
    is_mods = mods.find_one({"username" : update_request.username})
    
    if not is_mods:
      raise HTTPException(status_code = 404, detail = "No mod with this username is found")
    
    mods.update_one(
      {"username" : update_request.username},
      {"$set" : mod_data}
    )
    
    return mod_data
  else:
    raise HTTPException(status_code = 401, detail = "required admin rights")