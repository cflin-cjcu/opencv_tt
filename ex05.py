# OpenCV的幾何變換

# Import only if not previously imported
import cv2
import numpy as np
img = cv2.imread("./img/test2.jpg", 1)  # (flag = 0 or 1 or -1)
rows, cols, ch = img.shape
# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# roi = img[220:220+340, 330:330+270]
# Import only if not previously imported
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
print(M)
res = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("img", img)
cv2.imshow("res", res)

cv2.imwrite("./img/test5.jpg", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
