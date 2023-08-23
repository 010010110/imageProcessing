import cv2

# carrega a imagem
img = cv2.imread('9.png')

b, g, r = cv2.split(img)

# aplica o detector de bordas em cada canal
edges_b = cv2.medianBlur(b, 5)
edges_g = cv2.medianBlur(g, 5)
edges_r = cv2.medianBlur(r, 5)

# soma as bordas encontradas em cada canal
edges = edges_b + edges_g + edges_r

# # aplica o detector de bordas
# edges = cv2.medianBlur(img, 5)

# aplica a transformada de Hough para detecção de círculos
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 15, param1=50, param2=40, minRadius=0, maxRadius=0)

# desenha os círculos encontrados na imagem original
if circles is not None:
    circles = circles[0]
    for x, y, r in circles:
        cv2.circle(img, (int(x), int(y)), int(r), (0, 255, 0), 2)

# exibe a imagem com os círculos detectados
cv2.imshow('circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()