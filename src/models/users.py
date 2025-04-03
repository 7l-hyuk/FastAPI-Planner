from pydantic import BaseModel, EmailStr

from .events import Event


# collection
class User(BaseModel):
    email: EmailStr
    password: str
    events: list[Event] | None = None


# data validation
class UsersignIn(BaseModel):
    email: EmailStr
    password: str
