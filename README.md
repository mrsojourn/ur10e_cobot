# Hand Gesture Control || Ur10e_cobot || Computer Vision
_Universal Robot - Cobots Basic Programming_

## Basic Movement control for Universal Robots using Hand Gestures and Web Camera

## Demo Video: <a href="https://youtu.be/oojnQzC8snI?si=TZHDBj-BuyuO2op3"> >>> Click Here: YouTube link <<<</a>

### Packages USED!
1. OpenCV - Webcamera
2. Hand Gesture - Mediapipe
3. Ur10e control - ur-rtde

### Follow the following steps:
  1. Step 1
     Download/Clone my repo on your terminal
     ```python
     git clone https://github.com/mrsojourn/ur10e_cobot.git
     ```
     OR

     Simply DOWNLOAD it and locate your folder in your FAVOURITE IDE
     
  3. Step 1
     ```python
     pip install -r requirements.txt
     ```

     OR
     ```python
     pip install opencv-python mediapipe ur-rtde
     ```
     
  5. Step 2
     ```python
     ip_address = '10.0.0.117' #replace with your robot IP address here
     ```
  6. Step 3
     Run **ur10e_hand_gesture_control.py**
     ```python
     python ur10e_hand_gesture_control.py
     ```

### Instruction
1. Hand Open pose: Robot rotates slightly wrt its base (Joint movement)
2. Fist pose: Robot rotates slightly wrt its shoulder (Joint movement)
3. Victory pose: Simple TCP movement
