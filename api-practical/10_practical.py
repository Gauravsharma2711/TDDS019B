"""
Practical 10: Create Async DB APIs with Tortoise ORM
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from tortoise import fields, models
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

app = FastAPI(
    title="Practical 10 - Async DB APIs with Tortoise ORM",
    description="Asynchronous Database CRUD APIs backed by SQLite and Tortoise ORM.",
    version="1.0.0"
)

# 1. Tortoise ORM Model
class StudentModel(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    course = fields.CharField(max_length=100)
    gpa = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "students"

    def __str__(self):
        return f"{self.name} ({self.course})"

# 2. Pydantic Schemas for API Requests & Responses
class StudentCreate(BaseModel):
    name: str
    course: str
    gpa: float

class StudentResponse(StudentCreate):
    id: int

# 3. Async API Endpoints
@app.get("/")
async def home():
    return {"message": "Async Tortoise ORM API Service"}

@app.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate):
    """Create a new student record in database asynchronously."""
    student_obj = await StudentModel.create(**student.model_dump())
    return student_obj

@app.get("/students", response_model=List[StudentResponse])
async def get_all_students():
    """Retrieve all student records asynchronously using Tortoise ORM."""
    return await StudentModel.all()

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student_by_id(student_id: int):
    """Get a single student by ID asynchronously."""
    try:
        return await StudentModel.get(id=student_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")

@app.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, updated_data: StudentCreate):
    """Update student record asynchronously."""
    try:
        student_obj = await StudentModel.get(id=student_id)
        student_obj.name = updated_data.name
        student_obj.course = updated_data.course
        student_obj.gpa = updated_data.gpa
        await student_obj.save()
        return student_obj
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")

@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student(student_id: int):
    """Delete student record asynchronously."""
    try:
        student_obj = await StudentModel.get(id=student_id)
        await student_obj.delete()
        return {"message": f"Student ID {student_id} deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")

# 4. Register Tortoise ORM with FastAPI
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["__main__"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
