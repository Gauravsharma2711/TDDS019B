from fastapi import FastAPI , BackgroundTasks
import time 

app = FastAPI()

def send_email(email:str):
    print(f"Sending email to {email}...")
    time.sleep(10)
    print("Email Sent successfully!")

@app.post("/register")
def register (email: str , background_tasks : BackgroundTasks):
    background_tasks.add_task(send_email , email)

    return {
        'message' : 'Student registered successfully'
    }