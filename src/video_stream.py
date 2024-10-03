import cv2
from filters import apply_sepia, apply_grayscale, apply_mirror, apply_resize

def apply_filters(frame):
    frame = apply_sepia(frame)       # Use of sepia
    frame = apply_grayscale(frame)   # Black and white filter
    frame = apply_mirror(frame)      # Mirror filter
    frame = apply_resize(frame, 0.5) # Resize (scale 50%)
    return frame

def start_video_stream(video_path, output_path, duration=10):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video source {video_path}")
        return

    # Settings for recording video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 20.0

    # Options for recording video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            # write the flipped frame
            processed_frame = apply_grayscale(frame)
            processed_frame = cv2.resize(processed_frame, (frame_width, frame_height))
            out.write(processed_frame)
            cv2.imshow("Processed Video", processed_frame)

            # Interrupt by pressing the ‘q’ key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {output_path}")

