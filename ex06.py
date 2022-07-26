# OpenCV的影像閥值

# Import only if not previously imported

import cv2

img = cv2.imread("./img/test2.jpg", 0)  # (flag = 0 or 1 or -1)

ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

ret3, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)


th5 = cv2.adaptiveThreshold(

    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

ret6, th6 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)

cv2.imshow("res", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", cv2.adaptiveThreshold(

    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2))
cv2.imshow("th5", th5)
cv2.imshow("th6", th6)

cv2.waitKey(0)

cv2.destroyAllWindows()
