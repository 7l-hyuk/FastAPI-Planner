from fastapi import APIRouter, HTTPException, status
from src.models.users import User
from src.database.connection import Database

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

user_db = Database(User)


@user_router.post("/signup")
async def sign_new_user(user: User):
    user_exist = await User.find_one(User.email == user.email)
    
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already"
        )
    await user_db.save(user)
    return {
        "message": "User created successfully"
    }
