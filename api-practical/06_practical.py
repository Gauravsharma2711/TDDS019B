"""
Practical 06: Add Custom Exception Handling
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Practical 06 - Custom Exception Handling",
    description="Handling custom domain exceptions gracefully with FastAPI exception handlers.",
    version="1.0.0"
)

# Sample database
students_db = {
    101: {"name": "Gaurav Sharma", "course": "Data Science", "status": "active"},
    102: {"name": "Nitish Singh", "course": "Computer Science", "status": "suspended"}
}

# 1. Custom Exception Classes
class StudentNotFoundException(Exception):
    def __init__(self, student_id: int):
        self.student_id = student_id

class StudentInactiveException(Exception):
    def __init__(self, student_id: int, student_name: str):
        self.student_id = student_id
        self.student_name = student_name

# 2. Register Custom Exception Handlers
@app.exception_handler(StudentNotFoundException)
async def student_not_found_handler(request: Request, exc: StudentNotFoundException):
    """Custom handler for student not found exception."""
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error_code": "STUDENT_NOT_FOUND",
            "message": f"Student with ID '{exc.student_id}' could not be found in records.",
            "path": str(request.url)
        }
    )

@app.exception_handler(StudentInactiveException)
async def student_inactive_handler(request: Request, exc: StudentInactiveException):
    """Custom handler for inactive/suspended student exception."""
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "error_code": "ACCOUNT_INACTIVE",
            "message": f"Student '{exc.student_name}' (ID: {exc.student_id}) account is suspended.",
            "path": str(request.url)
        }
    )

@app.get("/")
def home():
    return {"message": "Custom Exception Handling API"}

@app.get("/students/{student_id}")
def get_student_record(student_id: int):
    """API endpoint demonstrating custom exception triggering."""
    if student_id not in students_db:
        raise StudentNotFoundException(student_id=student_id)

    student = students_db[student_id]
    if student["status"] != "active":
        raise StudentInactiveException(student_id=student_id, student_name=student["name"])

    return {
        "status": "success",
        "student_id": student_id,
        "details": student
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
