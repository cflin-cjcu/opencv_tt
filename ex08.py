# OpenCV的形態學轉換
# 讀圖
# Import only if not previously imported
import cv2
import numpy as np
img1 = cv2.imread("./img/test2.jpg", 0)  # (flag = 0 or 1 or -1)
ret, img = cv2.threshold(img1, 50, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img)

# 設定捲積核
kernel = np.ones((3, 3), np.uint8)

# 侵蝕erode
erode = cv2.erode(img, kernel)
cv2.imshow("erode", erode)
# 擴張dilate
dilate = cv2.dilate(img, kernel)
cv2.imshow("dilate", dilate)
# 開運算 erode->dilate
open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("open", open)
# 閉運算 dilate->erode
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("close", close)
# 梯度運算 erode 跟 dialte 的差值
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("gradient", gradient)
# 禮帽 原圖和開運算的差值
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("tophat", tophat)
# 黑帽 原圖和閉運算的差值
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("bloack", blackhat)
# 顯示
cv2.waitKey(0)
cv2.destroyAllWindows()
