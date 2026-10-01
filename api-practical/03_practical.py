"""
Practical 03: Validate Data with Pydantic Models
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from typing import Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr, field_validator

app = FastAPI(
    title="Practical 03 - Pydantic Model Validation",
    description="Validating request bodies using Pydantic fields, field constraints, and custom validators.",
    version="1.0.0"
)

# Pydantic schema with comprehensive validation constraints
class StudentRegistration(BaseModel):
    student_id: int = Field(
        ...,
        gt=0,
        lt=10000,
        description="Unique student identifier between 1 and 9999"
    )
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Full name of the student"
    )
    email: EmailStr = Field(
        ...,
        description="Valid student email address"
    )
    course: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Enrolled degree or course"
    )
    age: int = Field(
        ...,
        ge=17,
        le=60,
        description="Student age must be between 17 and 60"
    )
    fees_paid: float = Field(
        ...,
        ge=0.0,
        description="Tuition fee amount paid"
    )

    # Custom validator for student name format
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not all(x.isalpha() or x.isspace() for x in value):
            raise ValueError("Name must contain only alphabetic characters and spaces")
        return value.title()

# In-memory storage
registered_students = []

@app.get("/")
def home():
    return {"message": "Pydantic Validation API standard endpoint"}

@app.post("/students", status_code=status.HTTP_201_CREATED)
def register_student(student: StudentRegistration):
    """Register a new student with full Pydantic validation."""
    # Check for duplicate student_id
    for existing in registered_students:
        if existing.student_id == student.student_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Student with ID {student.student_id} is already registered."
            )

    registered_students.append(student)
    return {
        "message": "Student registered successfully",
        "data": student
    }

@app.get("/students")
def get_all_registered_students():
    """List all validated registered students."""
    return {
        "total_count": len(registered_students),
        "students": registered_students
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
