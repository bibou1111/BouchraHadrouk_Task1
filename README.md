# BouchraHadrouk_Task1
# Eye Blink Detection

## Overview
This project uses Python, MediaPipe, and OpenCV to detect eye blinks through webcam input. 

## Setup and Running the Script

## Requirements
Before running the script, make sure you have the following installed:
- **Python 3.6 or higher**
- **OpenCV** - `pip install opencv-python`
- **MediaPipe** - `pip install mediapipe`
- **SciPy** - `pip install scipy`
  
## Usage
- The script works by tracking facial landmarks in real-time.
- It calculates the distance between the upper and lower eyelids to detect blinks.
- If the average distance between the eyelids is below the **`BLINK_THRESHOLD`** (default 7.0), the script counts a blink.
- The total number of detected blinks is displayed on the screen, along with the elapsed time since the script started.
  
### To Close the Camera:
To stop the camera and close the window, press **`q`** on your keyboard. 

