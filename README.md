# NeRF Video-to-3D Model Generation App

This project converts videos into 3D models using Neural Radiance Fields (NeRF). The service is exposed via a FastAPI app, and the generated 3D models can be rendered in-app.

## Features

- Upload videos via a FastAPI endpoint
- Extract frames from video for NeRF processing
- Generate 3D models using NeRF
- Render generated 3D models in the app
- Model weights versioning for NeRF fine-tuning

## Directory Structure

- `app/`: The main FastAPI app code and services.
- `models/weights/`: Stores the NeRF model weights.
- `docs/`: Documentation, including model specs and architecture diagrams.
- `notebooks/`: Jupyter notebooks for development and fine-tuning.
- `static/3d_models/`: Generated 3D models are stored here.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nerf-video-to-3d-app.git
   cd nerf-video-to-3d-app
   ```
