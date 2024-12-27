# BouchraHadrouk_Task1
# Eye Blink Detection

## Overview
This project uses Python, MediaPipe, and OpenCV to detect eye blinks through webcam input. The system processes face landmarks to calculate the distance between the upper and lower eyelids and detects when the eyes blink based on this distance.

## Setup and Running the Script

## Requirements
Before running the script, make sure you have the following installed:
- Python 3.6 or higher
- OpenCV
- MediaPipe
- SciPy
  
## Usage
- The script works by tracking facial landmarks in real-time.
- It calculates the distance between the upper and lower eyelids to detect blinks.
- If the average distance between the eyelids is below the **`BLINK_THRESHOLD`** (default 7.0), the script counts a blink.
- The blink count and elapsed time are displayed in the output window.
- The script only detects one face at a time, and works best when the face is clearly visible and centered in the camera view.
  
### To Close the Camera:
To stop the camera and close the window, press **`q`** on your keyboard. This will terminate the script and close the webcam feed.


