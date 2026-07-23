from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    completed: bool

tasks = []

# Home
@app.get("/")
def home():
    return {"message": "Task Management API"}

# Create Task
@app.post("/tasks")
def create_task(task: Task):

    task_data = task.model_dump()

    task_data["id"] = len(tasks) + 1

    tasks.append(task_data)

    return {
        "message": "Task Created",
        "task": task_data
    }

# Read All Tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# Read Single Task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task Not Found"
    )

# Update Task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for task in tasks:

        if task["id"] == task_id:

            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed

            return {
                "message": "Task Updated",
                "task": task
            }

    raise HTTPException(
        status_code=404,
        detail="Task Not Found"
    )

# Delete Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return {
                "message": "Task Deleted Successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task Not Found"
    )