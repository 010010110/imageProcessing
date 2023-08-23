import cv2
import numpy as np

# Leitura da imagem de entrada
img = cv2.imread('3.jpg')

# Conversão para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicação do filtro de suavização Gaussiano
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Cálculo do gradiente de intensidade da imagem usando Sobel em X e Y
grad_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

# Cálculo da magnitude e direção do gradiente
mag, ang = cv2.cartToPolar(grad_x, grad_y, angleInDegrees=True)

# Aplicação da técnica de não máxima supressão
nms_kernel_size = 3
nms_mag = np.zeros_like(mag)
for y in range(nms_kernel_size // 2, mag.shape[0] - nms_kernel_size // 2):
    for x in range(nms_kernel_size // 2, mag.shape[1] - nms_kernel_size // 2):
        mag_max = np.max(mag[y - nms_kernel_size // 2 : y + nms_kernel_size // 2 + 1,
                             x - nms_kernel_size // 2 : x + nms_kernel_size // 2 + 1])
        if mag[y, x] == mag_max:
            nms_mag[y, x] = mag[y, x]

# Aplicação da técnica de limiarização dupla
low_threshold = 50
high_threshold = 150
edges = np.zeros_like(nms_mag)
strong_edges_y, strong_edges_x = np.where(nms_mag >= high_threshold)
weak_edges_y, weak_edges_x = np.where((nms_mag >= low_threshold) & (nms_mag < high_threshold))
edges[strong_edges_y, strong_edges_x] = 255
for y, x in zip(weak_edges_y, weak_edges_x):
    if np.max(edges[y - 1 : y + 2, x - 1 : x + 2]) == 255:
        edges[y, x] = 255

# Aplicação das bordas encontradas na imagem colorida original
color_edges = np.zeros_like(img)
color_edges[:, :, 0] = edges
color_edges[:, :, 1] = edges
color_edges[:, :, 2] = edges
result = cv2.bitwise_and(img, color_edges)

# Exibição do resultado
cv2.imshow('Resultado', result)
cv2.waitKey(0)
cv2.destroyAllWindows()