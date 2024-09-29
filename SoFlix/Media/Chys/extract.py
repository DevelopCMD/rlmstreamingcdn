import sys
import cv2
import random
from pathlib import Path
try:
    droppedFile = sys.argv[1] 
except IndexError:
    print("No file dropped")

file_path = Path(droppedFile)
file_no_ext = file_path.stem
vidcap = cv2.VideoCapture(droppedFile)
# get total number of frames
totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
randomFrameNumber=random.randint(0, totalFrames)
# set frame position
vidcap.set(cv2.CAP_PROP_POS_FRAMES,randomFrameNumber)
success, image = vidcap.read()
if success:
    cv2.imwrite(f"{file_no_ext}.jpg", image)
    print(f"Written file {file_no_ext}.jpg")