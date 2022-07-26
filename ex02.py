# 匯入 cv2
import cv2

# 匯入 matplotlib
from matplotlib import pyplot as plt
# (flag = 0 or 1 or -1)
# 讀圖
img = cv2.imread("./img/test1.jpg", cv2.IMREAD_GRAYSCALE)

# 顯示圖
# 用 matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()

# 用 cv2
# cv2.imshow("Test", img)
# cv2.imwrite("./img/out.png", img)
# 暫停視窗
# cv2.waitKey(0)
# cv2.destroyAllWindows()
