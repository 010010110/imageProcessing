import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread('1.png')

# Aplica a detecção de bordas
edges = cv2.Canny(img, 150, 200, None, 3)

# Aplica a transformada de Hough
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# Desenha as linhas encontradas na imagem original
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a*rho, b*rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv2.line(img, pt1, pt2, (0, 0, 255), 3)

# Exibe a imagem com as retas detectadas
cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()