"""
Practical 05: Build CRUD APIs for a Task Management App
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Practical 05 - Task Management CRUD API",
    description="Full CRUD (Create, Read, Update, Delete) operation implementation for a Task Management System.",
    version="1.0.0"
)

# Pydantic Request Model for Creation/Update
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Task title")
    description: Optional[str] = Field(None, max_length=500, description="Task details")
    completed: bool = Field(default=False, description="Task completion status")

# Pydantic Response Model
class TaskResponse(TaskCreate):
    id: int

# In-memory database
tasks_db: List[dict] = [
    {"id": 1, "title": "Complete API Practical 05", "description": "Build CRUD operations in FastAPI", "completed": True},
    {"id": 2, "title": "Prepare Data Science Notes", "description": "Review Machine Learning algorithms", "completed": False}
]
id_counter = 2

@app.get("/")
def home():
    return {"message": "Task Management CRUD API Service"}

# 1. CREATE Task
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """Create a new task in the system."""
    global id_counter
    id_counter += 1
    new_task = {
        "id": id_counter,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }
    tasks_db.append(new_task)
    return new_task

# 2. READ ALL Tasks
@app.get("/tasks", response_model=List[TaskResponse])
def get_all_tasks(completed: Optional[bool] = None):
    """Get all tasks, optionally filtering by completion status."""
    if completed is not None:
        filtered = [t for t in tasks_db if t["completed"] == completed]
        return filtered
    return tasks_db

# 3. READ SINGLE Task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id: int):
    """Retrieve a specific task by its ID."""
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")

# 4. UPDATE Task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskCreate):
    """Update an existing task by ID."""
    for task in tasks_db:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed
            return task
    raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")

# 5. DELETE Task
@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int):
    """Delete a task by ID."""
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted_task = tasks_db.pop(index)
            return {"message": "Task deleted successfully", "deleted_task": deleted_task}
    raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
