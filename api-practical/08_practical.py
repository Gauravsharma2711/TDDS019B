"""
Practical 08: Secure Routes with User Roles
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from datetime import datetime, timedelta, timezone
from typing import Optional, List
import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI(
    title="Practical 08 - Secure Routes with Role-Based Access Control (RBAC)",
    description="Securing API routes using OAuth2 Bearer JWT authentication and Role checking.",
    version="1.0.0"
)

# Configuration constants
SECRET_KEY = "super-secret-key-for-data-science-practical"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock User Database (Passwords stored in plain text for simple practical demonstration)
USERS_DB = {
    "gaurav": {"username": "gaurav", "password": "password123", "role": "admin", "name": "Gaurav Sharma"},
    "sarthak": {"username": "sarthak", "password": "student123", "role": "student", "name": "Sarthak Patel"}
}

# Models
class Token(BaseModel):
    access_token: str
    token_type: str

class UserProfile(BaseModel):
    username: str
    name: str
    role: str

# JWT Token Helper Functions
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = USERS_DB.get(username)
    if user is None:
        raise credentials_exception
    return user

# Role enforcement dependency factory
class RoleChecker:
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: dict = Depends(get_current_user)):
        if current_user["role"] not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Allowed roles: {self.allowed_roles}"
            )
        return current_user

# Endpoints
@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Authenticate user credentials and return JWT access token."""
    user = USERS_DB.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"], "role": user["role"]},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile", response_model=UserProfile)
def read_user_profile(current_user: dict = Depends(get_current_user)):
    """Protected endpoint accessible by any authenticated user."""
    return current_user

@app.get("/student/dashboard")
def student_dashboard(current_user: dict = Depends(RoleChecker(["student", "admin"]))):
    """Protected route accessible by student and admin roles."""
    return {
        "message": f"Welcome to Student Portal, {current_user['name']}!",
        "role": current_user["role"]
    }

@app.get("/admin/dashboard")
def admin_dashboard(current_user: dict = Depends(RoleChecker(["admin"]))):
    """Protected admin-only route."""
    return {
        "message": f"Welcome Admin {current_user['name']}! You have full system privileges.",
        "users_count": len(USERS_DB)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
