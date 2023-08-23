import cv2
img_bgr= cv2.imread("1.jpg")
img_hsv=cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
img_hsv[:, :, 2]=cv2.equalizeHist(img_hsv[:, :, 2])# aplica equalização no canal V
saida=cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
concat=cv2.hconcat((img_bgr,saida))

cv2.imwrite("equalizeHist.jpg",concat)



