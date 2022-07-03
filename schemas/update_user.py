from typing import Optional
from pydantic import BaseModel


class UserUpdate(BaseModel):
    name: Optional[str]
    full_name: Optional[str]
    email: str
    username: str
    disabled: bool = False
    hashed_password: Optional[str]
