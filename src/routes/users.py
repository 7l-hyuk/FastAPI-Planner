from fastapi import APIRouter, HTTPException, status
from src.models.users import User, UsersignIn

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users: dict[str, User] = {}


@user_router.post("/signup")
async def sign_new_user(user: User):
    """
    Sign up a new user

    Args:
        user (`User`)
    """
    if user.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )
    users[user.email] = user
    return {"meassage": "User created successfully"}


@user_router.post("/signin")
async def sign_user_in(credentials: UsersignIn):
    """
    Sign in a user

    Args:
        credentials (`UserSignIn`)
    """
    if credentials.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    stored_user = users[credentials.email]

    if credentials.password != stored_user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid password"
        )
    return {"message": "User signed in successfully"}
