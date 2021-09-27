import cv2
import matplotlib.pyplot as plt
import imutils
import numpy as np
from numpy import asarray
from PIL import Image
from scipy import ndimage



# a) crie e visualize uma imagem simples – quadrado branco sobre fundo preto;
widthImage, heightImage = 512, 512
filePath = '../Images/quadrado.png'
fileName = (filePath, "PNG")

ObjPillow = Image.new("RGB", (widthImage, heightImage))
setPillow = ObjPillow.load()

for row in range(heightImage):
    for col in range(widthImage):
        color = (000)
        rev_col, rev_row = widthImage - col - 1, heightImage - row - 1
        setPillow[col, row] = color
        setPillow[rev_col, row] = color
        setPillow[col, rev_row] = color
        setPillow[rev_col, rev_row] = color

for row in range(206, 306):
    for col in range(206, 306):
        color = (255, 255, 255)
        setPillow[col, row] = color

ObjPillow.save(*fileName)
rgbToGrey = Image.open(filePath).convert('L')
rgbToGrey.save(filePath)
rgbToGrey.show()

img = cv2.imread('../Images/quadrado.png', 0)
plt.subplot(151), plt.imshow(img, "gray"), plt.title("Imagem Original")

# b) calcular e visualizar seu espectro de Fourier (amplitudes);
img_fft_amplitude = np.fft.fft2(img)
plt.subplot(152), plt.imshow(np.log(1+np.abs(img_fft_amplitude)), "gray"), plt.title("Espectro Amplitude")

# c) calcular e visualizar seu espectro de Fourier (fases);
img_fft_fase = np.angle(img_fft_amplitude)
plt.subplot(153), plt.imshow(img_fft_fase, "gray"), plt.title("Espectro Fase")

# d) obter e visualizar seu espectro de Fourier centralizado;
img_centralizado = np.fft.fftshift(img_fft_amplitude)
plt.subplot(154), plt.imshow(np.log(1+np.abs(img_centralizado)), "gray"), plt.title("Espectro Centralizado")

plt.show()

# e) Aplique uma rotação de 40º no quadrado e repita os passo b-d;

imagem = cv2.imread('../Images/quadrado.png')
altura, largura = imagem.shape[:2]
cv2.waitKey(0)

#rotacao
ponto = (largura / 2, altura / 2) #ponto no centro da figura
rotacao = cv2.getRotationMatrix2D(ponto, 40, 1.0)
rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
cv2.imshow("Rotacionado 40 graus", rotacionado)
cv2.waitKey(0)

cv2.imwrite('../Images/quadrado_40.png', rotacionado)

plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

img_rotacionada40 = cv2.imread('../Images/quadrado_40.png', 0)
plt.subplot(151), plt.imshow(img_rotacionada40, "gray"), plt.title("Imagem Rotacionada")

img_fft_amplitude = np.fft.fft2(img_rotacionada40)
plt.subplot(152), plt.imshow(np.log(1+np.abs(img_fft_amplitude)), "gray"), plt.title("Espectro Amplitude")

img_fft_fase = np.angle(img_fft_amplitude)
plt.subplot(153), plt.imshow(img_fft_fase, "gray"), plt.title("Espectro Fase")

img_centralizado = np.fft.fftshift(img_fft_amplitude)
plt.subplot(154), plt.imshow(np.log(1+np.abs(img_centralizado)), "gray"), plt.title("Espectro Centralizado")

plt.show()

# f) Aplique uma translação nos eixos x e y no quadrado e repita os passo b-d;

# translacao (deslocamento)
deslocamento = np.float32([[1, 0, -50], [0, 1, -90]])
deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
cv2.imshow("Cima e esquerda", deslocado)
cv2.waitKey(0)

cv2.imwrite('../Images/quadrado_transladada.png', deslocado)

plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

img_deslocada = cv2.imread('../Images/quadrado_transladado.png', 0)
plt.subplot(151), plt.imshow(img_deslocada, "gray"), plt.title("Imagem Transladada")

img_fft_amplitude = np.fft.fft2(img_deslocada)
plt.subplot(152), plt.imshow(np.log(1+np.abs(img_fft_amplitude)), "gray"), plt.title("Espectro Amplitude")

img_fft_fase = np.angle(img_fft_amplitude)
plt.subplot(153), plt.imshow(img_fft_fase, "gray"), plt.title("Espectro Fase")

img_centralizado = np.fft.fftshift(img_fft_amplitude)
plt.subplot(154), plt.imshow(np.log(1+np.abs(img_centralizado)), "gray"), plt.title("Espectro Centralizado")

plt.show()

