# OpenCV與MediaPipe用於臉部檢測與應用
from FaceDetectionModule import FaceDetector
import cv2
import cvzone

cap = cv2.VideoCapture(0)
detector = FaceDetector()
heartimg = cv2.imread('./img/heart.png', cv2.IMREAD_UNCHANGED)


while True:
    success, img = cap.read()
    img, bboxs, pp = detector.findFaces(img)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        # cv2.circle(img, pp[0], 5, (255, 0, 255), cv2.FILLED)
        cc = pp[1]
        cc = [cc[0]-16, cc[1]-16]
        img = cvzone.overlayPNG(img, heartimg, cc)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
