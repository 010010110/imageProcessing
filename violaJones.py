import cv2

# Carregar o classificador pré-treinado para detecção de carros
car_cascade = cv2.CascadeClassifier('cars.xml')

# Verificar se o classificador foi carregado corretamente
if car_cascade.empty():
    print('Erro ao carregar o classificador.')
    exit()

# Ler a imagem
imagem = cv2.imread('carros.png')

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar o classificador para detectar carros
carros = car_cascade.detectMultiScale(gray, 1.1, 3)

# Desenhar retângulos ao redor dos carros detectados
for (x, y, w, h) in carros:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 3)

# Mostrar a imagem com as detecções de carros
cv2.imshow('Detecção de Carros', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
