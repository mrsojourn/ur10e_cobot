import cv2
import time
import rtde_receive
import rtde_control
import rtde_io
import utils.HandTrackingModule as htm

# Set the width and height of the video frame
w, h = 640, 480

# Open the video capture device
cap = cv2.VideoCapture(0)

# Create an instance of the hand detector
detector = htm.HandDetector(detectionCon=0.8)

# Enter the IP address of your UR10e robot here
ip_address = '10.0.0.117'

# Create interfaces for receiving data from and controlling the robot
rtde_r = rtde_receive.RTDEReceiveInterface(ip_address)
rtde_c = rtde_control.RTDEControlInterface(ip_address)
rt_io = rtde_io.RTDEIOInterface(ip_address)

while True:
    gesture = ' '

    # Get the current joint angles and TCP pose of the robot
    actual_q = rtde_r.getActualQ()
    actual_x = rtde_r.getActualTCPPose()

    # Read a frame from the video capture device
    success, img = cap.read()

    # Detect hands in the frame
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        if len(lmList) != 0:
            # Detect the number of fingers raised
            fingers = detector.fingersUp()

            time.sleep(0.1)

            if fingers == [1, 1, 1, 1, 1]:
                gesture = 'Open'
                print('Press T to continue...')
                if cv2.waitKey(1) & 0xFF == ord('t'):
                    print('t pressed:')
                    print('Reacting...')
                    # Move the first joint of the robot
                    actual_q[0] = actual_q[0] - 0.6
                    rtde_c.moveJ(actual_q, 0.5, 0.5)
                    time.sleep(1)
                    actual_q[0] = actual_q[0] + 0.6
                    rtde_c.moveJ(actual_q, 0.5, 0.5)
                    print('done')
                    time.sleep(1)
                    continue

            elif fingers == [0, 0, 0, 0, 0]:
                gesture = 'Close'
                print('Press Y to continue...')
                if cv2.waitKey(1) & 0xFF == ord('y'):
                    print('y pressed:')
                    print('Reacting...')
                    # Move the second joint of the robot
                    actual_q[1] = actual_q[1] - 0.2
                    rtde_c.moveJ(actual_q, 0.5, 0.5)
                    time.sleep(1)
                    actual_q[1] = actual_q[1] + 0.2
                    rtde_c.moveJ(actual_q, 0.5, 0.5)
                    print('done')
                    time.sleep(1)
                    continue

            elif fingers == [0, 1, 1, 0, 0]:
                gesture = 'Victory'
                print('Press v to continue...')
                if cv2.waitKey(1) & 0xFF == ord('v'):
                    print('v pressed:')
                    print('Reacting...')
                    # Move the TCP pose of the robot
                    actual_x[0] = actual_x[0] - 0.08
                    rtde_c.moveL(actual_x, 0.5, 0.5)
                    time.sleep(1)
                    actual_x[0] = actual_x[0] + 0.08
                    rtde_c.moveL(actual_x, 0.5, 0.5)
                    print('done')
                    time.sleep(1)
                    continue

            # Display the detected gesture on the image
            cv2.putText(img, f'{gesture}'.upper(), (50, 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # Display the image
    cv2.imshow("Image", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture device
cap.release()

# Close all windows
cv2.destroyAllWindows()
