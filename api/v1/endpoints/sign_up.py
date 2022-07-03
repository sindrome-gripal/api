from fastapi import APIRouter, Request, HTTPException, status

from schemas.sign_up import UserSignUp
from settings import DefaultConfig

from services.auth.pwd_crypt_context import get_password_hash
from db.users import DataBase


router = APIRouter()
config = DefaultConfig()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def sign_up_user(request: Request, user: UserSignUp):

    db = DataBase()
    
    user_request_data = await request.json()
    user_db = db.get_user(user_request_data.get('username', None))
    
    if(user_db is not None):
        already_exists_user_exception = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This user already exists.",
        )
        return already_exists_user_exception
    
    password_hash = get_password_hash(user_request_data.get('password', None))
    user.hashed_password = password_hash
    
    success_created = db.insert_one(user)
    if success_created:
        return "User created successfully."
    
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Unable to register user. Database error."
    ) 
