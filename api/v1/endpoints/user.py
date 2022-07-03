from fastapi import APIRouter, Depends

from schemas.auth import User
from settings import DefaultConfig

from services.auth.user_validation import get_current_active_user



router = APIRouter()
config = DefaultConfig()



@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

