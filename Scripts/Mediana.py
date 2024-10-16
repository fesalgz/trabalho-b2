import cv2
import numpy as np
import matplotlib.pylab as plt

escolha = int(input("Escolha o numero e uma imagem ira passar nos filtros: \n (1) Cachorro com Ruídos \n (2) Placa de Carro desfocada \n"))

if escolha == 1:
    imagem = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)
elif escolha == 2:
    imagem = cv2.imread('placa.jpg', cv2.IMREAD_GRAYSCALE)

#Aplicar o filtro Gaussiano (mediana) com tamanho de kernel 3x3
filtro_gaussiano_3x3 = cv2.GaussianBlur(imagem, (3, 3), 0)

#Aplicar o filtro Gaussiano (mediana) com tamanho de kernel 5x5
filtro_gaussiano_5x5 = cv2.GaussianBlur(imagem, (5, 5), 0)

#Aplicar o filtro Gaussiano (mediana) com tamanho de kernel 7x7
filtro_gaussiano_7x7 = cv2.GaussianBlur(imagem, (7, 7), 0)

#Mostrar Imagens
plt.figure(figsize=(15,10))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(filtro_gaussiano_3x3, cmap='gray')
plt.title('Filtro Gaussiano (Mediana) - 3x3')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(filtro_gaussiano_5x5, cmap='gray')
plt.title('Filtro Gaussiano (Mediana) - 5x5')
plt.axis('off')


plt.subplot(2, 2, 4)
plt.imshow(filtro_gaussiano_7x7, cmap='gray')
plt.title('Filtro Gaussiano (Mediana) - 7x7')
plt.axis('off')

plt.show()