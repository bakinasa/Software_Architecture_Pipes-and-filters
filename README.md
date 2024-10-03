# Pipes-and-Filters Video Processing Application

This project demonstrates the use of the Pipes-and-Filters architectural pattern for real-time video processing. The application captures video frames from a webcam or video file, applies a series of filters, and displays the processed video in real-time.

## Features

- Captures video from a webcam or video file.
- Applies a sequence of four filters:
  - Black and white conversion
  - Mirror effect
  - Resize frame
  - Sepia filter
- Processes and visualizes the video stream in real-time.

## Architecture

This application follows the Pipes-and-Filters pattern:
- Each filter is implemented as a separate function (filter), which transforms the input frame.
- Frames are passed sequentially through each filter (pipe) before being visualized.

## Requirements

- Python 3.x
- OpenCV (install using `pip install opencv-python numpy pillow`)

## Usage


1. Clone the repository:
   ```bash
   git clone https://github.com/bakinasa/Software_Architecture_Pipes-and-filters.git
2. Install required dependencies:

    ```bash
    pip install opencv-python numpy pillow
3. Add your input video to the inputs/ directory (e.g., input-1.mp4).

4. Run the script:

    ```bash
    python src/main.py