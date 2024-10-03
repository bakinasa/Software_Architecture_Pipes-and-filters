import os
from video_stream import start_video_stream

if __name__ == "__main__":
    # video_path = "inputs/input-1.mp4"  # Path to the input video file
    video_path = 0  # Using the camera
    
    output_path = "outputs/processed_output.mp4"  # Path to save the output video

    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
    else:
        start_video_stream(video_path, output_path)
