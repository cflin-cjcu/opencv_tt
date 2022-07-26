# OpenCV的幾何變換
# Import only if not previously imported
import cv2
import numpy as np
img = cv2.imread("./img/test3.jpg", 1)  # (flag = 0 or 1 or -1)
pts1 = np.float32([[44, 111], [507, 17], [534, 201], [107, 357]])
pts2 = np.float32([[0, 0], [500, 0], [500, 200], [0, 200]])
M = cv2.getPerspectiveTransform(pts1, pts2)
res = cv2.warpPerspective(img, M, (500, 200))
# Import only if not previously imported
cv2.imshow("img", img)
cv2.imshow("res", res)
cv2.imwrite("./img/test4.jpg", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
