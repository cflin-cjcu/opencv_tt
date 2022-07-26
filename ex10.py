# OpenCV的輪廓處理
# 讀圖
import cv2
import numpy as np
img1 = cv2.imread("./img/test4.jpg", 1)  # (flag = 0 or 1 or -1)
imggray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(imggray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("threshold", img)
# 找輪廓
contours, hierarchy = cv2.findContours(img,
                                       cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

color1 = (255, 255, 0)
# 繪製圖形輪廓
fin = img1.copy()
dst = cv2.drawContours(fin, contours, 17, color1, -1)
# 顯示結果影像
cv2.imshow("contours", dst)

# 列印影像矩
# for i in range(len(contours)):
#     M = cv2.moments(contours[i])
#     print("列印影像矩 %d %s" % (i, M))
# print("%d length= %s area=%s" %
#       (i, cv2.arcLength(contours[i], True), cv2.contourArea(contours[i])))

# 設定感興趣的contour
contour = contours[17]

# 繪製中心點
fin = img1.copy()
M = cv2.moments(contour)                        # 影像矩
Cx = int(M["m10"] / M["m00"])                   # 質心 x 座標
Cy = int(M["m01"] / M["m00"])                   # 質心 y 座標
dst0 = cv2.circle(fin, (Cx, Cy), 3, color1, -1)
# dst0 = cv2.drawContours(fin, [contour], 0, color1, 2)
cv2.imshow("center", dst0)

# 建構矩形
fin = img1.copy()
x, y, w, h = cv2.boundingRect(contour)
dst1 = cv2.rectangle(fin, (x, y), (x+w, y+h), color1, 2)
cv2.imshow("boundingRect", dst1)

# 建構最小矩形 (中心點(x，y) (w, h))，旋轉角度)
fin = img1.copy()
box = cv2.minAreaRect(contour)
print("轉換前 ", box)
points = cv2.boxPoints(box)
points = np.int0(points)
print("轉換後 ", points)
dst2 = cv2.drawContours(fin, [points], 0, color1, 2)
cv2.imshow("minAreaRect", dst2)

# 取得圓中心座標和圓半徑
fin = img1.copy()
(x, y), radius = cv2.minEnclosingCircle(contour)
center = (int(x), int(y))                           # 圓中心座標取整數
radius = int(radius)                                # 圓半徑取整數
dst3 = cv2.circle(fin, center, radius, color1, 2)   # 繪圓
cv2.imshow("minEnclosingCircle", dst3)

# 取得最優擬合橢圓數據
fin = img1.copy()
ellipse = cv2.fitEllipse(contour)
print("最優擬合橢圓 ", ellipse)
dst4 = cv2.ellipse(fin, ellipse, color1, 2)          # 繪橢圓
cv2.imshow("fitEllipse", dst4)

# 取得三角形面積與頂點座標
fin = img1.copy()
area, triangle = cv2.minEnclosingTriangle(contour)
print("三角形面積 ", area)
print("三角頂點座標 ", triangle)
triangle = np.int0(triangle)                        # 轉整數
dst5 = cv2.line(fin, tuple(triangle[0][0]),
                tuple(triangle[1][0]), color1, 2)
dst5 = cv2.line(fin, tuple(triangle[1][0]),
                tuple(triangle[2][0]), color1, 2)
dst5 = cv2.line(fin, tuple(triangle[0][0]),
                tuple(triangle[2][0]), color1, 2)
cv2.imshow("Triangle", dst5)

# 近似多邊形包圍
fin = img1.copy()
approx1 = cv2.approxPolyDP(contour, 1, True)         # epsilon=3
print("近似多邊形", len(approx1), approx1)
print(cv2.arcLength(contour, True) - cv2.arcLength(approx1, True))
dst6 = cv2.polylines(fin, [approx1], True, color1, 2)
cv2.imshow("DP1", dst6)

fin = img1.copy()
approx2 = cv2.approxPolyDP(contour, 10, True)        # epsilon=15
dst7 = cv2.polylines(fin, [approx2], True, color1, 2)
cv2.imshow("DP2", dst7)

# 擬合線
fin = img1.copy()
rows, cols = fin.shape[:2]                          # 輪廓大小
print("擬合線 ", cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01))
vx, vy, x, y = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)                     # 左邊點的 y 座標
righty = int(((cols - x) * vy / vx) + y)            # 右邊點的 y 座標
dst10 = cv2.line(fin, (0, lefty), (cols-1, righty), color1, 2)   # 左到右繪線
cv2.imshow("fitLine", dst10)


# 凸包
fin = img1.copy()
hull = cv2.convexHull(contour)
print("凸包", len(hull), hull)               # 獲得凸包頂點座標
dst8 = cv2.polylines(fin, [hull], True, color1, 2)  # 將凸包連線
cv2.imshow("convexHull", dst8)

# 極點座標
fin = img1.copy()
cnt = contour
left = tuple(cnt[cnt[:, :, 0].argmin()][0])
right = tuple(cnt[cnt[:, :, 0].argmax()][0])
top = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])
print("最左點 ", left)
print("最右點 ", right)
print("最上點 ", top)
print("最下點 ", bottom)
dst11 = cv2.circle(fin, left, 5, [0, 255, 0], -1)
dst11 = cv2.circle(fin, right, 5, [0, 255, 0], -1)
dst11 = cv2.circle(fin, top, 5, [0, 255, 255], -1)
dst11 = cv2.circle(fin, bottom, 5, [0, 255, 255], -1)
cv2.imshow("most", dst11)

cv2.waitKey(0)
cv2.destroyAllWindows()
