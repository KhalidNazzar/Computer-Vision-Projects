Hand Tracking Virtual Painter
GestureCanvas is an innovative hand tracking virtual painting application, utilizing cutting-edge Computer Vision technologies. It leverages OpenCV for image processing and MediaPipe for hand tracking, enabling users to paint on a virtual canvas using intuitive hand gestures.

Features
Real-Time Hand Tracking: Powered by MediaPipe for accurate hand movement detection.
Virtual Painting: Use your hand as a brush to draw on the screen.
Dynamic Color Selection: Switch between colors by interacting with a virtual palette.
Adjustable Brush Size: Change the brush thickness with hand gestures.
Gesture-Controlled Canvas Clearing: Clear your drawing with a simple hand gesture.
Getting Started
Prerequisites
Python 3.x
A webcam or similar video capturing device
Installation
Clone the repository:
sh
Copy code
git clone https://github.com/yourusername/GestureCanvas.git
Navigate to the project directory:
sh
Copy code
cd GestureCanvas
Install the required dependencies:
sh
Copy code
pip install opencv-python mediapipe numpy
Running the Application
Execute the script to start the application:

sh
Copy code
python virtual_painter.py
Usage
Drawing: Point your index finger to draw.
Changing Color: Move your index finger to different color options displayed on the screen.
Adjusting Brush Size: Bring your thumb and index finger together and move them apart or close to change the brush size.
Clearing Canvas: Show a specific gesture (e.g., thumb and pinky up) to clear the canvas.
