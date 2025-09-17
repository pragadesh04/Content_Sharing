from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt
import os

load_dotenv()

oauth2 = OAuth2PasswordBearer(tokenUrl = "/login")

psw = CryptContext(schemes = ["bcrypt"])

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")

def create_access_token(data : dict):
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + timedelta(minutes = 30)
  
  to_encode.update({"exp" : expire})
  
  encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded

def get_current_user(token : str = Depends(oauth2)):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    role = payload.get("role")
    return {"username" : username, "role" : role}
  except Exception as e:
    raise HTTPException(status_code = 400, detail = "Invalid token or Expired Token")
  
def hash_password(password):
  return psw.hash(password)

def dehash_password(password, hashed_password):
  return psw.verify(password, hashed_password)