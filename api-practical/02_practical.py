"""
Practical 02: Handle Query and Path Parameters
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI(
    title="Practical 02 - Path and Query Parameters",
    description="Demonstrating Path and Query parameters with type validation in FastAPI.",
    version="1.0.0"
)

# Sample database
students_db = {
    1: {"name": "Gaurav Sharma", "course": "Data Science", "city": "Mumbai", "semester": 5},
    2: {"name": "Tanmay Varma", "course": "Financial Markets", "city": "Bangalore", "semester": 5},
    3: {"name": "Rohan Mehta", "course": "Data Science", "city": "Pune", "semester": 3},
    4: {"name": "Vidit Shah", "course": "Commerce", "city": "Ahmedabad", "semester": 1},
    5: {"name": "Rahul Kumar", "course": "AI & ML", "city": "Delhi", "semester": 5}
}

@app.get("/")
def home():
    return {"message": "Welcome to Student Directory API"}

# Path parameter with validation
@app.get("/students/{student_id}")
def get_student_by_id(
    student_id: int = Path(..., title="The ID of the student to fetch", ge=1, le=100)
):
    """Fetch student details using path parameter student_id."""
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student_id, "data": student}

# Query parameters for searching & filtering
@app.get("/search")
def search_students(
    course: Optional[str] = Query(None, min_length=2, max_length=50, description="Filter by course name"),
    city: Optional[str] = Query(None, description="Filter by city"),
    limit: int = Query(10, ge=1, le=50, description="Limit result count")
):
    """Search students based on query parameters course, city, and limit."""
    results = {}
    for sid, info in students_db.items():
        match_course = (course is None) or (course.lower() in info["course"].lower())
        match_city = (city is None) or (city.lower() == info["city"].lower())

        if match_course and match_city:
            results[sid] = info
            if len(results) >= limit:
                break

    return {
        "filters": {"course": course, "city": city, "limit": limit},
        "count": len(results),
        "results": results
    }

# Combining Path and Query parameters
@app.get("/students/{student_id}/details")
def get_student_details(
    student_id: int = Path(..., ge=1),
    semester: int = Query(..., ge=1, le=8, description="Semester number"),
    section: str = Query("A", max_length=2, description="Class section")
):
    """Combine Path parameter (student_id) and Query parameters (semester, section)."""
    student = students_db.get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return {
        "student_id": student_id,
        "name": student["name"],
        "course": student["course"],
        "academic_details": {
            "semester": semester,
            "section": section
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
