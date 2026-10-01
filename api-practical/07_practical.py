"""
Practical 07: Add Background Task to Send Async Email
Author: Gaurav Sharma (Roll No: TDDS019B)
Course: TYBSc Data Science - API Subject
"""

import time
import asyncio
from typing import List
from fastapi import FastAPI, BackgroundTasks, status
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Practical 07 - Background Tasks (Async Email)",
    description="Executing long-running tasks asynchronously in the background using FastAPI BackgroundTasks.",
    version="1.0.0"
)

# Email request model
class EmailRequest(BaseModel):
    recipient_email: EmailStr
    subject: str
    body: str

# Log memory for sent background emails
sent_email_logs: List[dict] = []

# Synchronous/Simulated long-running function
def send_email_background_task(recipient_email: str, subject: str, body: str):
    """Simulates sending an email notification in the background."""
    print(f"--> [BACKGROUND TASK STARTED] Sending email to {recipient_email}...")
    time.sleep(3)  # Simulate network latency/SMTP transmission
    print(f"--> [BACKGROUND TASK COMPLETED] Email sent to {recipient_email}!")

    # Store log
    sent_email_logs.append({
        "recipient": recipient_email,
        "subject": subject,
        "status": "DELIVERED",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@app.get("/")
def home():
    return {"message": "Background Task Service API"}

@app.post("/send-email", status_code=status.HTTP_202_ACCEPTED)
def trigger_email_notification(
    email_data: EmailRequest,
    background_tasks: BackgroundTasks
):
    """
    Accepts email request and delegates sending operation to background task.
    Returns immediate HTTP 202 Accepted response without blocking the client.
    """
    background_tasks.add_task(
        send_email_background_task,
        email_data.recipient_email,
        email_data.subject,
        email_data.body
    )

    return {
        "status": "Accepted",
        "message": f"Email notification to '{email_data.recipient_email}' queued in background.",
        "recipient": email_data.recipient_email
    }

@app.get("/email-logs")
def get_email_logs():
    """Retrieve history of sent background emails."""
    return {
        "total_sent": len(sent_email_logs),
        "logs": sent_email_logs
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
