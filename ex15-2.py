from PoseModule import PoseDetector
import cv2
import pafy
import time
import numpy as np

url = "https://www.youtube.com/watch?v=-Lw8Ri6BGzA"
videoPafy = pafy.new(url)
best = videoPafy.getbest()
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(best.url)

detector = PoseDetector()
pTime = 0
while True:
    success, img = cap.read()
    img1 = np.zeros([360, 640, 3], np.uint8)
    img1 = detector.findPose(img)
    # lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    # if bboxInfo:
    #     center = bboxInfo["center"]
    #     cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)

    cv2.imshow("Image", img)
    cv2.imshow("Image1", img1)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
