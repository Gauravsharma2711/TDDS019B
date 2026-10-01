"""
Practical 01: Create Basic FastAPI Endpoints
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Practical 01 - Basic FastAPI Endpoints",
    description="A simple API demonstrating basic GET and POST endpoints using FastAPI.",
    version="1.0.0"
)

# Pydantic schema for Student input/output
class Student(BaseModel):
    id: int
    name: str
    course: str
    age: int

# In-memory database of students
students_db = [
    Student(id=1, name="Gaurav Sharma", course="Data Science", age=20),
    Student(id=2, name="Sarthak Patel", course="Data Science", age=21)
]

@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the FastAPI Basics API!"}

@app.get("/students")
async def get_all_students():
    """Endpoint to retrieve all student records."""
    return {"status": "success", "total": len(students_db), "students": students_db}

@app.post("/students", status_code=201)
async def create_student(student: Student):
    """Endpoint to add a new student record."""
    students_db.append(student)
    return {
        "message": "Student created successfully",
        "student": student
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
