"""
Practical 04: Create Nested Input/Output Models
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from typing import List, Optional
from datetime import date
from fastapi import FastAPI, status
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="Practical 04 - Nested Pydantic Models",
    description="Building nested input and output Pydantic schemas for multi-level data representation.",
    version="1.0.0"
)

# Nested Model 1: Address
class Address(BaseModel):
    street: str = Field(..., example="123 Science Park Road")
    city: str = Field(..., example="Mumbai")
    state: str = Field(..., example="Maharashtra")
    pincode: int = Field(..., example=400001)

# Nested Model 2: Task Item
class TaskItem(BaseModel):
    item_id: int
    title: str
    is_completed: bool = False

# Complex Model using Address & TaskItem: User Profile
class UserProfile(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    address: Address
    pending_tasks: List[TaskItem] = []

# Response Model (Output Schema)
class UserProfileResponse(BaseModel):
    status: str
    user: UserProfile
    task_count: int

# In-memory storage
users_db: List[UserProfile] = []

@app.get("/")
def home():
    return {"message": "Nested Models API Service"}

@app.post("/users", response_model=UserProfileResponse, status_code=status.HTTP_201_CREATED)
def create_user_profile(user: UserProfile):
    """Create a user profile containing nested address and task details."""
    users_db.append(user)
    return UserProfileResponse(
        status="User profile created successfully",
        user=user,
        task_count=len(user.pending_tasks)
    )

@app.get("/users", response_model=List[UserProfile])
def list_users():
    """Retrieve all user profiles with nested fields."""
    return users_db

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
