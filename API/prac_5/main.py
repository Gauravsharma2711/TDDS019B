from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title : str
    description : str
    completed : bool

tasks = []

@app.get("/")
def home ():
    return ("message" : "Task Management API")

@app.post("/tasks")