# File and Upload File

from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {
        "file_size": len(file),
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }

# Direct File Access: Receive the file as bytes and access its size
# UploadFile Class: Use the UploadFile class for more metadata like accessing filename and content type
