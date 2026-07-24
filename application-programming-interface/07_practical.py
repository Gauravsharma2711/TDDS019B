from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload File
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File Uploaded Successfully",
        "filename": file.filename
    }

# List Files
@app.get("/files")
def show_files():

    return {
        "files": os.listdir(UPLOAD_FOLDER)
    }

# Download File
@app.get("/download/{filename}")
def download_file(filename: str):

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        return {"message": "File Not Found"}

    return FileResponse(
        path=file_path,
        filename=filename
    )