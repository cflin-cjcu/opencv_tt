# OpenCV的影像模糊方法
# 讀圖
# Import only if not previously imported
import cv2
import numpy as np
img1 = cv2.imread("./img/test2.jpg", 0)  # (flag = 0 or 1 or -1)
ret1, img = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("IMG", img)
# 2D捲積濾波
# 5x5的平均濾波和
kernel = np.ones((5, 5), np.float32) / 25
det = cv2.filter2D(img, -1, kernel)
cv2.imshow("2D", det)
# 平均模糊
blur = cv2.blur(img, (11, 11))
cv2.imshow("blur", blur)
# 高斯濾波
gauss = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("gauss", gauss)

# 中值濾波
median = cv2.medianBlur(img, 11)
cv2.imshow("median", median)
# 雙邊濾波
bila = cv2.bilateralFilter(img, 10, 200, 200)
cv2.imshow("bila", bila)
# 顯示
# Import only if not previously imported


cv2.waitKey(0)
cv2.destroyAllWindows()
