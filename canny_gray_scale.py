import cv2
import numpy as np

img = cv2.imread('4.jpg')
# imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img, 100, 200)

# Gradiente em x e y
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3)

# Aplicação do Laplaciano
laplacian = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Sobel', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()