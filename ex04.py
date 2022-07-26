# OpenCV的色彩空間與應用
# Import only if not previously imported
import cv2
import numpy as np
hmin = 100
smin = 43
vmin = 46
hmax = 124
smax = 255
vmax = 255

# In VideoCapture object either Pass address of your Video file
# Or If the input is the camera, pass 0 instead of the video file
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lowerb = np.array([hmin, smin, vmin])
        upperb = np.array([hmax, smax, vmax])
        mask = cv2.inRange(hsv, lowerb, upperb)
        img = cv2.bitwise_and(frame, frame, mask=mask)
        # Display the resulting frame
        cv2.imshow('Frame', frame)
        cv2.imshow('hsv', hsv)
        cv2.imshow('img', img)
        # Press esc to exit
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
