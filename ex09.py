# OpenCV的影像梯度與邊緣偵測
# 讀圖
import cv2
import numpy as np
img1 = cv2.imread("./img/test2.jpg", 0)  # (flag = 0 or 1 or -1)
ret, img = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img)

# Sobel (8U)
sobel = cv2.Sobel(img, cv2.CV_8U, 0, 1)
cv2.imshow("sobel", sobel)
# Sobel (64F)
sobel64fx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobel_2x = cv2.convertScaleAbs(sobel64fx)
sobel64fy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobel_2y = cv2.convertScaleAbs(sobel64fy)
sobel_2 = cv2.addWeighted(sobel_2x, 0.5, sobel_2y, 0.5, 0)
cv2.imshow("sobel_2", sobel_2)

# Sharr (8U)

# cv2.imshow("scharr", scharr)

# Scharr (64F)
scharr64fx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr_2x = cv2.convertScaleAbs(scharr64fx)
scharr64fy = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharr_2y = cv2.convertScaleAbs(scharr64fy)
scharr_2 = cv2.addWeighted(scharr_2x, 0.5, scharr_2y, 0.5, 0)

cv2.imshow("scharr_2", scharr_2)
# cv2.imshow("sobel-scharr", sobel_2-scharr_2)
# laplacian (8U)
laplacian = cv2.Laplacian(img, cv2.CV_8U)
cv2.imshow("laplacian", laplacian)

# Canny邊緣偵測
canny1 = cv2.Canny(img1, 50, 100)
cv2.imshow("canny1", canny1)
canny2 = cv2.Canny(img1, 150, 200)
cv2.imshow("canny2", canny2)
canny3 = cv2.Canny(img1, 50, 200)
cv2.imshow("canny3", canny3)

cv2.waitKey(0)
cv2.destroyAllWindows()
