from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city : str
    state : str
    pincode : int

class Student (BaseModel):
    name : str
    age : int
    email : str
    address : Address

@app.post("/students")
def create_student(student : Student):
    return{
        "message" : "Student Added Successfully " , 
        "student" : student
    }
