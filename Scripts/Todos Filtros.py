import cv2
import numpy as np
import matplotlib.pylab as plt

escolha = int(input("Escolha o numero e uma imagem ira passar nos filtros: \n (1) Cachorro com Ruídos \n (2) Placa de Carro desfocada \n"))

if escolha == 1:
    imagem = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)
elif escolha == 2:
    imagem = cv2.imread('placa.jpg', cv2.IMREAD_GRAYSCALE)

#Aplicar o filtro Gaussiano (mediana) com tamanho de kernel 5x5
filtro_gaussiano = cv2.GaussianBlur(imagem, (5, 5), 0)

#Aplicando o filtro de média com tamanho 5x5
filtro_5x5 = cv2.blur(imagem, (5, 5))

#Aplicar o Filtro de Sobel na direção X (encontrar bordas verticais)
sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)

#Aplicar o Filtro de Sobel na direção Y (encontrar bordas horizontais)
sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)

#Converter os resultados para um formato mais facil de visualizar
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

#Combinar as bordas encontradas nas direções X e Y
sobel_combinado = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

#Mostrar Imagens
plt.figure(figsize=(15,10))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(filtro_gaussiano, cmap='gray')
plt.title('Filtro Gaussiano (Mediana) - 5x5')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(filtro_5x5, cmap='gray')
plt.title('Filtro de Media (Blur) - 5x5')
plt.axis('off')


plt.subplot(2, 2, 4)
plt.imshow(sobel_combinado, cmap='gray')
plt.title('Filtro de Sobel Combinado')
plt.axis('off')

plt.show()