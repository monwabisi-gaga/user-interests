from fastapi import FastAPI, UploadFile, File, BackgroundTasks
import uuid
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transcoding_service.main import transcode_video

app = FastAPI()

@app.post("/upload/")
async def create_upload_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    # Generate a unique content ID
    content_id = str(uuid.uuid4())

    # Validate file type (placeholder)
    if file.content_type not in ["video/mp4", "image/jpeg"]:
        return {"error": "Invalid file type"}

    # Save the file
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    input_path = os.path.join(upload_dir, f"{content_id}_{file.filename}")

    with open(input_path, "wb") as buffer:
        buffer.write(await file.read())

    # Define output directory for transcoded files
    output_dir = f"transcoded_files/{content_id}"

    # Add transcoding to background tasks
    background_tasks.add_task(transcode_video, input_path, output_dir)

    return {"content_id": content_id, "filename": file.filename, "message": "File upload successful, transcoding started in the background."}