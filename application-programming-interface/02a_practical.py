from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Gaurav", "course": "Data Science", "city": "Mumbai"},
    2: {"name": "Tanmay", "course": "Financial Markets", "city": "Banglore"},
    3: {"name": "Rohan", "course": "Psychology", "city": "Pune"},
    4: {"name": "Vidit", "course": "Commerce", "city": "Gujrat"},
    5: {"name": "Rahul", "course": "AI", "city": "Delhi"}
}

# for student in students.values() :
#     print (student['name'])

@app.get("/")
def home():
    return {"message": f"Welcome Gaurav to Student API"}

@app.get("/students")
def get_students():
    print (f"Information of : {students}")

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id, "Student Not Found")

@app.get("/search")
def search_students(course: str = None, city: str = None):
    return {
        "course": course,
        "city": city
    }

@app.get("/student/{student_id}/details")
def student_details(student_id: int, semester: int, section: str):
    return {
        "student_id": student_id,
        "semester": semester,
        "section": section
    }