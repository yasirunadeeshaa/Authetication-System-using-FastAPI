from fastapi import APIRouter, HTTPException
from models import User

router = APIRouter()

# In-memory fake DB
users = []

@router.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@router.get("/users", response_model=list[User])
def get_users():
    return users

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
