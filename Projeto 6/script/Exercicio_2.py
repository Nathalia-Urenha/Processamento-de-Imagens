import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp


def distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def idealFilterLP(D0, imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            if distance((y, x), center) < D0:
                base[y, x] = 1
    return base


def butterworthLP(D0, imgShape, n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            base[y, x] = 1 / (1 + (distance((y, x), center) / D0) ** (2 * n))
    return base


def gaussianLP(D0, imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows / 2, cols / 2)
    for x in range(cols):
        for y in range(rows):
            base[y, x] = exp(((-distance((y, x), center) ** 2) / (2 * (D0 ** 2))))
    return base


plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

img = cv2.imread("../Images/lena.jpg", 0)

# A
plt.subplot(151), plt.imshow(img, "gray"), plt.title("Imagem Original")

img_fft = np.fft.fft2(img)
img_fft_centralizada = np.fft.fftshift(img_fft)

#B
passaBaixaIdeal = idealFilterLP(50, img.shape)
plt.subplot(152), plt.imshow(np.abs(passaBaixaIdeal), "gray"), plt.title("Filtro Ideal")

passaBaixaButterworth = butterworthLP(50, img.shape, 20)
plt.subplot(153), plt.imshow(np.abs(passaBaixaButterworth), "gray"), plt.title("Filtro Butterworth")

passaBaixaGaussiano = gaussianLP(50, img.shape)
plt.subplot(154), plt.imshow(np.abs(passaBaixaGaussiano), "gray"), plt.title("Filtro Gaussiano")

plt.show()

plt.figure(figsize=(6.4 * 5, 4.8 * 5), constrained_layout=False)

#C
img_centralizada_ideal = img_fft_centralizada * passaBaixaIdeal
img_ideal = np.fft.ifftshift(img_centralizada_ideal)
img_processada_ideal = np.fft.ifft2(img_ideal)
plt.subplot(161), plt.imshow(np.abs(img_processada_ideal), "gray"), plt.title("Filtro Ideal")

img_centralizada_butterworth = img_fft_centralizada * passaBaixaButterworth
img_butterworth = np.fft.ifftshift(img_centralizada_butterworth)
img_processada_butterworth = np.fft.ifft2(img_butterworth)
plt.subplot(162), plt.imshow(np.abs(img_processada_butterworth), "gray"), plt.title("Filtro Butterworth")

img_centralizada_gaussiano = img_fft_centralizada * passaBaixaGaussiano
img_gaussiano = np.fft.ifftshift(img_centralizada_gaussiano)
img_processada_gaussiano = np.fft.ifft2(img_gaussiano)
plt.subplot(163), plt.imshow(np.abs(img_processada_gaussiano), "gray"), plt.title("Filtro Gaussiano")

plt.show()


