from app.models.nerf_model import nerf_model


def generate_3d_model(video_path: str):
    # Call the NeRF model to generate a 3D model from the video
    return nerf_model.generate(video_path)
