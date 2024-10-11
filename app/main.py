from fastapi import FastAPI, UploadFile, File
from app.services.nerf_generation_service import generate_3d_model
from app.render.renderer import render_3d_model

app = FastAPI()

@app.post("/upload_video/")
async def upload_video(file: UploadFile = File(...)):
    # Process the video file and pass it to the NeRF model
    video_path = f"static/videos/{file.filename}"
    with open(video_path, "wb") as buffer:
        buffer.write(await file.read())
    jj
    # Call the service to generate 3D model
    model_output = generate_3d_model(video_path)
    
    # Render the 3D model in the app
    render_output = render_3d_model(model_output)
    
    return {"message": "3D model generated", "render_output": render_output}
