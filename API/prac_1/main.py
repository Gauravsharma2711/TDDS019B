from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name : str
    age : int
    id : int 

students = [
    Student(name="Gaurav" , age = 19 , id = 1 ),
    Student(name="Sarthak" , age = 20 , id = 2 )
]

@app.get("/")
async def root ():
    return ("This is root")

@app.post("/students")
async def create_student (student : Student) :
    students.append(student)
    return {"message":"Student Created successfully" , "student" : student}

@app.get("/students")
async def get_all_students():
    return {"students" : students}
