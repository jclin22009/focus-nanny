import cv2
import time
from PIL import Image
import numpy as np
import os

def resize(frame):
    '''
    Takes an image, resizes it, and returns the resized opencv image
    '''
     # Convert the frame to a PIL image
    pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Resize the image
    max_size = 250
    ratio = max_size / max(pil_img.size)
    new_size = tuple([int(x*ratio) for x in pil_img.size])
    resized_img = pil_img.resize(new_size, Image.LANCZOS)

    # Convert the PIL image back to an OpenCV image
    frame = cv2.cvtColor(np.array(resized_img), cv2.COLOR_RGB2BGR)
    return frame

# Folder
folder = "frames"

# Create the frames folder if it doesn't exist
frames_dir = os.path.join(os.getcwd(), folder)
os.makedirs(frames_dir, exist_ok=True)

while True:
    # Capture screenshot
    os.system(f"screencapture {folder}/screen.png")

    # Read the screenshot
    frame = cv2.imread(f"{folder}/screen.png")

    # if frame == previous_frame:
    #     print("Duplicate frame, skipping")
    #     continue
    
    # frame = resize(frame)

    # Save the frame as an image file
    print("📸 Say cheese! Saving frame.")
    path = f"{folder}/frame.jpg"
    cv2.imwrite(path, frame)
   

    # Wait for 2 seconds
    time.sleep(2)

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

