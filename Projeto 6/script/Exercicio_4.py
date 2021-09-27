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

########## FILTRO IDEAL ############
filtro_pb_ideal_1 = FiltroIdeal(1.0, img.shape)
plt.subplot(152), plt.imshow(np.abs(filtro_pb_ideal_1), "gray"), plt.title("Filtro Ideal 1.0")

filtro_pb_ideal_15 = FiltroIdeal(1.5, img.shape)
plt.subplot(153), plt.imshow(np.abs(filtro_pb_ideal_1), "gray"), plt.title("Filtro Ideal 1.5")

filtro_pb_ideal_50 = FiltroIdeal(50, img.shape)
plt.subplot(154), plt.imshow(np.abs(filtro_pb_ideal_50), "gray"), plt.title("Filtro Ideal 50")

plt.show()
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

########## FILTRO BUTTERWORTH ############

filtro_pb_Butterworth10 = FiltroButterworth(1.0, img.shape, 20)
plt.subplot(151), plt.imshow(np.abs(filtro_pb_Butterworth10), "gray"), plt.title("Filtro Butterworth 1.0")

filtro_pb_Butterworth15 = FiltroButterworth(1.5, img.shape, 20)
plt.subplot(152), plt.imshow(np.abs(filtro_pb_Butterworth15), "gray"), plt.title("Filtro Butterworth 1.5")

filtro_pb_Butterworth50 = FiltroButterworth(50, img.shape, 20)
plt.subplot(153), plt.imshow(np.abs(filtro_pb_Butterworth50), "gray"), plt.title("Filtro Butterworth 50")

plt.show()
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

########## FILTRO GAUSSIANO ############

filtro_pb_Gaussiano10 = FiltroGaussiano(1.0, img.shape)
plt.subplot(151), plt.imshow(np.abs(filtro_pb_Gaussiano10), "gray"), plt.title("Filtro Gaussiano 1.0")

filtro_pb_Gaussiano15 = FiltroGaussiano(1.5, img.shape)
plt.subplot(152), plt.imshow(np.abs(filtro_pb_Gaussiano15), "gray"), plt.title("Filtro Gaussiano 1.5")

filtro_pb_Gaussiano50 = FiltroGaussiano(50, img.shape)
plt.subplot(153), plt.imshow(np.abs(filtro_pb_Gaussiano50), "gray"), plt.title("Filtro Gaussiano 50")

plt.show()

plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

############################################################################

# c) a imagem resultante após aplicação de cada filtro
########## IMAGEM FILTRO IDEAL ############

centralizada_ideal = img_fft_centralizada * filtro_pb_ideal_1
img_ideal = np.fft.ifftshift(centralizada_ideal)
processada_ideal = np.fft.ifft2(img_ideal)
plt.subplot(161), plt.imshow(np.abs(processada_ideal), "gray"), plt.title("Filtro Ideal 1.0")

centralizada_ideal = img_fft_centralizada * filtro_pb_ideal_15
img_ideal = np.fft.ifftshift(centralizada_ideal)
processada_ideal = np.fft.ifft2(img_ideal)
plt.subplot(162), plt.imshow(np.abs(processada_ideal), "gray"), plt.title("Filtro Ideal 1.5")

centralizada_ideal = img_fft_centralizada * filtro_pb_ideal_50
img_ideal = np.fft.ifftshift(centralizada_ideal)
processada_ideal = np.fft.ifft2(img_ideal)
plt.subplot(163), plt.imshow(np.abs(processada_ideal), "gray"), plt.title("Filtro Ideal 50")


plt.show()
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

########## IMAGEM FILTRO BUTTERWORTH ############

centralizada_but = img_fft_centralizada * filtro_pb_Butterworth10
img_butterworth = np.fft.ifftshift(centralizada_but)
processada_butterworth = np.fft.ifft2(img_butterworth)
plt.subplot(161), plt.imshow(np.abs(processada_butterworth), "gray"), plt.title("Filtro Butterworth 1.0")

centralizada_but = img_fft_centralizada * filtro_pb_Butterworth15
img_butterworth = np.fft.ifftshift(centralizada_but)
processada_butterworth = np.fft.ifft2(img_butterworth)
plt.subplot(162), plt.imshow(np.abs(processada_butterworth), "gray"), plt.title("Filtro Butterworth 1.5")

centralizada_but = img_fft_centralizada * filtro_pb_Butterworth50
img_butterworth = np.fft.ifftshift(centralizada_but)
processada_butterworth = np.fft.ifft2(img_butterworth)
plt.subplot(163), plt.imshow(np.abs(processada_butterworth), "gray"), plt.title("Filtro Butterworth 50")

plt.show()
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

########## IMAGEM FILTRO GAUSSIANO ############

centralizada_gaussiano = img_fft_centralizada * filtro_pb_Gaussiano10
img_gaussiano = np.fft.ifftshift(centralizada_gaussiano)
processada_gaussiano = np.fft.ifft2(img_gaussiano)
plt.subplot(161), plt.imshow(np.abs(processada_gaussiano), "gray"), plt.title("Filtro Gaussiano 1.0")

centralizada_gaussiano = img_fft_centralizada * filtro_pb_Gaussiano15
img_gaussiano = np.fft.ifftshift(centralizada_gaussiano)
processada_gaussiano = np.fft.ifft2(img_gaussiano)
plt.subplot(162), plt.imshow(np.abs(processada_gaussiano), "gray"), plt.title("Filtro Gaussiano 1.5")

centralizada_gaussiano = img_fft_centralizada * filtro_pb_Gaussiano50
img_gaussiano = np.fft.ifftshift(centralizada_gaussiano)
processada_gaussiano = np.fft.ifft2(img_gaussiano)
plt.subplot(163), plt.imshow(np.abs(processada_gaussiano), "gray"), plt.title("Filtro Gaussiano 50")

plt.show()
plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)


