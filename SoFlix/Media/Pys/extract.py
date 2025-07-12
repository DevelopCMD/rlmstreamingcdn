import cv2
import random
import sys
import os
import numpy as np

def is_frame_too_dark(frame, brightness_threshold=20):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg_brightness = np.mean(gray)
    return avg_brightness < brightness_threshold

def extract_random_frame(video_path, max_attempts=10):
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = f"{base_name}.jpg"

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames == 0:
        print("Error: No frames found in video.")
        return

    for attempt in range(max_attempts):
        random_frame = random.randint(0, total_frames - 1)
        cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)
        success, frame = cap.read()

        if success and not is_frame_too_dark(frame):
            cv2.imwrite(output_path, frame)
            print(f"Saved bright frame as '{output_path}' (frame {random_frame}/{total_frames})")
            cap.release()
            return

    print(f"Failed: Could not find a bright enough frame after {max_attempts} tries.")
    cap.release()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract.py [path_to_video.mp4]")
        sys.exit(1)

    video_file = sys.argv[1]
    if not os.path.isfile(video_file):
        print(f"Error: File '{video_file}' does not exist.")
        sys.exit(1)

    extract_random_frame(video_file)
