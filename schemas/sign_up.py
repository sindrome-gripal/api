from typing import Optional
from pydantic import BaseModel


class UserSignUp(BaseModel):
    name: str
    full_name: str
    email: str
    username: str
    disabled: bool = False
    hashed_password: Optional[str]
