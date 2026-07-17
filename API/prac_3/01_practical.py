from fastapi import FastAPI
from pydantic import BaseModel , Field ,EmailStr

app = FastAPI()

class Student(BaseModel):
    
    name : str = Field(
        min_length=2 , 
        max_length= 30
    )

    id : int = Field(
        gt=18 ,
        lt=60
    )

    email : EmailStr

    course : str = Field(
        min_length=6 , 
        max_length=30
    )

    fees : float

@app.post('/students')

def create_student (student : Student):
    return {
        "message" : "Student registered succesfully" , 
        "student" : Student
    }