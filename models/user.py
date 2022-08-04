from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str
