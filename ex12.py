# OpenCV的模板匹配
# 讀圖
import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread("./img/test4.jpg", 1)  # (flag = 0 or 1 or -1)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./img/test4-1.jpg', 0)
w, h = template.shape[::-1]

# 所有匹配的方法
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)  # 去掉引號
#     # 匹配
#     res = cv2.matchTemplate(img, template, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     # 如果方法是 TM_SQDIFF 或 TM_SQDIFF_NORMED 取最小值
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     print(meth, min_val, max_val, min_loc, max_loc)
#     bottom_right = (top_left[0] + w, top_left[1] + h)

#     cv2.rectangle(img, top_left, bottom_right, 255, 2)

#     plt.subplot(121), plt.imshow(res, cmap='gray'),
#     plt.title('Matching Result'), plt.axis('off')
#     plt.subplot(122), plt.imshow(img, cmap='gray'),
#     plt.title('Detected Point'), plt.axis('off')
#     plt.suptitle(meth)

#     plt.show()


#找尋所有匹配 > threshold
res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
img = img1.copy()
loc = np.where(res >= threshold)
print(*loc[::-1])
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

plt.subplot(131), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)),
plt.title('Original')
plt.subplot(132), plt.imshow(template, cmap='gray'),
plt.title('Template')
plt.subplot(133), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)),
plt.title('Matching Result')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
