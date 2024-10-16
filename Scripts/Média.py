import cv2
import numpy as np
import matplotlib.pylab as plt

escolha = int(input("Escolha o numero e uma imagem ira passar nos filtros: \n (1) Cachorro com Ruídos \n (2) Placa de Carro desfocada \n"))

if escolha == 1:
    imagem = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)
elif escolha == 2:
    imagem = cv2.imread('placa.jpg', cv2.IMREAD_GRAYSCALE)

#Aplicando o filtro de média com tamanho 3x3
filtro_3x3 = cv2.blur(imagem, (3, 3))

#Aplicando o filtro de média com tamanho 5x5
filtro_5x5 = cv2.blur(imagem, (5, 5))

#Aplicando o filtro de média com tamanho 10x10
filtro_10x10 = cv2.blur(imagem, (10, 10))

#Mostrar Imagens
plt.figure(figsize=(15,10))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(filtro_3x3, cmap='gray')
plt.title('Filtro de Média (Blur) - 3x3')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(filtro_5x5, cmap='gray')
plt.title('Filtro de Media (Blur) - 5x5')
plt.axis('off')


plt.subplot(2, 2, 4)
plt.imshow(filtro_10x10, cmap='gray')
plt.title('Filtro de Média (Blur) - 10x10')
plt.axis('off')

plt.show()