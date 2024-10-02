# Archeon

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

## Getting Started

1. Create a folder named fyp
2. Open folder in visual studio code
3. connect your github account to vs code
4. open terminal
5. Clone the repository:
   ```bash
   git clone https://github.com/your-username/archeon.git
   cd archeon
   ```
6. make and start virtual environment and install requirements:
   ```bash
   python -m venv archeonvenv
   set-executionpolicy -scope process -executionpolicy bypass
   ./archeovenv/Scripts/activate
   pip install -r requirements.txt
   ```
