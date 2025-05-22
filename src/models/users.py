from pydantic import BaseModel, EmailStr
from beanie import Document

from .events import Event


# collection -> Document
class User(Document):
    email: EmailStr
    password: str
    events: list[Event] | None = None

    class Settings:
        name = "users"  # collection name


# data validation -> BaseModel
class UsersignIn(BaseModel):
    email: EmailStr
    password: str
