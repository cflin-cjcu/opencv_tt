# OpenCV的核心操作
# 讀圖
# Import only if not previously imported
import cv2
import numpy as np
img = cv2.imread("./img/test1.jpg", 1)  # (flag = 0 or 1 or -1)
print(img.shape, img.size)
# ROI (Region of Interest)
roi1 = img[30:180, 350:850]
roi2 = img[450:600, 20:520]
print(roi1.shape)
# 浮水印
roi1gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(roi1gray, 200, 255, cv2.THRESH_BINARY)
makk_inv = cv2.bitwise_not(mask)

img_fg = cv2.bitwise_and(roi2, roi2, mask=makk_inv)
img_bg = cv2.bitwise_and(roi1, roi1, mask=mask)
roi = cv2.add(img_fg, img_bg)
# 顯示圖
# Import only if not previously imported
img[450:600, 20:520] = roi
cv2.imshow("Ex03", img)
cv2.imshow("img_fg", img_fg)
cv2.imshow("img_bg", img_bg)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
