import cv2
import time
from filters import apply_sepia, apply_grayscale, apply_mirror, apply_resize

def apply_filters(frame):
    # frame = apply_sepia(frame)       # Use of sepia
    # frame = apply_grayscale(frame)   # Black and white filter
    # frame = apply_mirror(frame)      # Mirror filter
    # frame = apply_resize(frame, 0.5) # Resize (scale 50%)
    return frame

def start_video_stream(video_path, output_path, duration=10):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video source {video_path}")
        return

    # Options for recording video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret or (time.time() - start_time) > duration:
            print("Video processing stopped after duration or end of file.")
            break

        processed_frame = apply_filters(frame)
        out.write(processed_frame)
        cv2.imshow("Processed Video", processed_frame)

        # Interrupt by pressing the ‘q’ key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Video stopped by user pressing 'q'.")
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {output_path}")

