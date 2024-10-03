import os
import time
import hashlib
from video_stream import start_video_stream

def generate_unique_filename(base_name="processed_output"):
    current_time = time.time()
    hash_object = hashlib.md5(str(current_time).encode()) 
    unique_hash = hash_object.hexdigest()
    return f"{base_name}_{unique_hash}.mp4"

if __name__ == "__main__":
    # video_path = "inputs/input-1.mp4"  # Path to the input video file
    video_path = 0  # Using the camera
    
    output_path = os.path.join("outputs", generate_unique_filename())  # Path to save the output video
    os.makedirs(os.path.dirname(output_path), exist_ok=True) # create folder if not exists

    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
    else:
        start_video_stream(video_path, output_path)
