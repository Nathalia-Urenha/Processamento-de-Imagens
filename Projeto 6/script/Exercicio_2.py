import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp


def distancia(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def FiltroIdeal(D0, imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            if distancia((y, x), center) < D0:
                base[y, x] = 1
    return base


def FiltroButterworth(D0, imgShape, n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            base[y, x] = 1 / (1 + (distancia((y, x), center) / D0) ** (2 * n))
    return base


def FiltroGaussiano(D0, imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            base[y, x] = exp(((-distancia((y, x), center) ** 2) / (2 * (D0 ** 2))))
    return base


plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

img = cv2.imread("../Images/lena.jpg", 0)

# a) a imagem inicial;
plt.subplot(151), plt.imshow(img, "gray"), plt.title("Imagem Original")

img_fft = np.fft.fft2(img)
img_fft_centralizada = np.fft.fftshift(img_fft)

# b) a imagem de cada filtro;
filtro_pb_ideal = FiltroIdeal(50, img.shape)
plt.subplot(152), plt.imshow(np.abs(filtro_pb_ideal), "gray"), plt.title("Filtro Ideal")

filtro_pb_Butterworth = FiltroButterworth(50, img.shape, 20)
plt.subplot(153), plt.imshow(np.abs(filtro_pb_Butterworth), "gray"), plt.title("Filtro Butterworth")

filtro_pb_Gaussiano = FiltroGaussiano(50, img.shape)
plt.subplot(154), plt.imshow(np.abs(filtro_pb_Gaussiano), "gray"), plt.title("Filtro Gaussiano")

plt.show()

plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

# c) a imagem resultante após aplicação de cada filtro
centralizada_ideal = img_fft_centralizada * filtro_pb_ideal
img_ideal = np.fft.ifftshift(centralizada_ideal)
processada_ideal = np.fft.ifft2(img_ideal)
plt.subplot(161), plt.imshow(np.abs(processada_ideal), "gray"), plt.title("Filtro Ideal")

centralizada_but = img_fft_centralizada * filtro_pb_Butterworth
img_butterworth = np.fft.ifftshift(centralizada_but)
processada_butterworth = np.fft.ifft2(img_butterworth)
plt.subplot(162), plt.imshow(np.abs(processada_butterworth), "gray"), plt.title("Filtro Butterworth")

centralizada_gaussiano = img_fft_centralizada * filtro_pb_Gaussiano
img_gaussiano = np.fft.ifftshift(centralizada_gaussiano)
processada_gaussiano = np.fft.ifft2(img_gaussiano)
plt.subplot(163), plt.imshow(np.abs(processada_gaussiano), "gray"), plt.title("Filtro Gaussiano")

plt.show()


