# OpenCV的直方圖處理
# 讀圖
import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread("./img/bg.jpg")  # (flag = 0 or 1 or -1)
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
imggray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(imggray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("img", img1)

# 單色
# hist = cv2.calcHist([imggray], [0], None, [256], [0, 256])   # 直方圖統計資料
# plt.plot(hist)                                      # 用plot()繪直方圖
# plt.show()

# 彩色RGB
# b = cv2.calcHist([img1], [0], None, [256], [0, 256])  # B 通道統計資料
# g = cv2.calcHist([img1], [1], None, [256], [0, 256])  # G 通道統計資料
# r = cv2.calcHist([img1], [2], None, [256], [0, 256])  # R 通道統計資料
# plt.plot(b, color="blue", label="Blue")    # 用plot()繪 B 通道
# plt.plot(g, color="green", label="Green")   # 用plot()繪 G 通道
# plt.plot(r, color="red", label="Red")     # 用plot()繪 R 通道
# plt.legend(loc="best")
# plt.show()

# # mask
# mask = np.zeros(imggray.shape[:2], np.uint8)
# mask[100:400, 100:400] = 255
# masked_img = cv2.bitwise_and(imggray, imggray, mask=mask)
# # Calculate histogram with mask and without mask
# # Check third argument for mask
# hist_full = cv2.calcHist([imggray], [0], None, [256], [0, 256])
# hist_mask = cv2.calcHist([imggray], [0], mask, [256], [0, 256])

# plt.subplot(221), plt.imshow(imggray, 'gray'), plt.title('Original')
# plt.subplot(222), plt.imshow(mask, 'gray'), plt.title('Mask')
# plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('Masked')
# plt.subplot(224), plt.plot(hist_full, label='original'),
# plt.plot(hist_mask, label='masked'), plt.xlim([0, 256]),
# plt.legend(loc=1), plt.title('Histogram')
# plt.show()

# # 均衡化
# img = imggray.copy()
# hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# # 計算累積分布(原圖)
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max() / cdf.max()

# plt.subplot(321), plt.imshow(img, 'gray'), plt.axis('off')
# plt.title('Original')
# plt.subplot(322), plt.plot(cdf_normalized, color='b'),
# plt.hist(img.flatten(), 256, [0, 256], color='r'),
# plt.xlim([0, 256]),
# plt.legend(('cdf', 'histogram'), loc='upper left'),
# plt.title('Histogram')

# # opencv均衡化
# img2 = cv2.equalizeHist(img)
# hist2, bins = np.histogram(img2.flatten(), 256, [0, 256])
# cdf2 = hist2.cumsum()
# cdf_m = cdf2 * hist2.max() / cdf2.max()

# plt.subplot(323), plt.imshow(img2, 'gray'), plt.axis('off')
# plt.title('Histogram Equalization')
# plt.subplot(324), plt.plot(cdf_m, color='b'),
# plt.hist(img2.flatten(), 256, [0, 256], color='r'),
# plt.xlim([0, 256]),
# plt.legend(('cdf', 'histogram'), loc='upper left'),
# plt.title('Histogram')

# # 有限對比自適性直方圖均衡化CLAHE（Contrast Limited Adaptive Histogram Equalization）
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# img3 = clahe.apply(img)
# hist3, bins = np.histogram(img3.flatten(), 256, [0, 256])
# cdf3 = hist3.cumsum()
# cdf_m = cdf3 * hist3.max() / cdf3.max()

# plt.subplot(325), plt.imshow(img3, 'gray'), plt.axis('off')
# plt.title('CLAHE')
# plt.subplot(326), plt.plot(cdf_m, color='b'),
# plt.plot(cdf_normalized, color='g'),
# plt.hist(img3.flatten(), 256, [0, 256], color='r'),
# plt.xlim([0, 256]),
# plt.legend(('cdf', 'cdf(ori)', 'histogram'), loc='upper left'),
# plt.title('Histogram')

# plt.show()

# 2D直方圖
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
