# ele usou reflect pra comparar com imageJ
import numpy as np
from numpy import asarray
from PIL import Image
from scipy import ndimage



# Funções de abrir a imagem do ImageJ

def openImageJ(path_image):
    image_in = Image.open(path_image)
    image_np = np.array(image_in)
    print('Imagem filtrada no ImageJ')
    printImage(image_np)



def printImage(image):
    print(image)
    print(image.dtype)
    print(image.min(), image.max())

# Função de converter a imagem em um numpy array
def converting(image):
    img_array = np.array(image).astype(int)
    print('Imagem Original')
    printImage(img_array)
    return img_array

# Função de realizar a convolução
def convolution(img_array, k):
    im = ndimage.convolve(img_array, k, mode='reflect')
    print("Imagem após somente a convolução")
    printMinMax(im)
    im = replaceNegativeValues(im)
    return im

# Função de exibir o máx e min
def printMinMax(im):
    print()
    print(im)
    print(im.min(),im.max())

# Função de converter para int para permitir valores negativos
def replaceNegativeValues(im):
    im = np.where(im < 0, 0, im)
    print('Imagem após convolução e substituição zero')
    printMinMax(im)
    return im

# Função de converter array em imagem tipo usint uint8
def convertUint8(im):
    image_out = Image.fromarray(im.astype('uint8'))
    image_out.show()
    return image_out

# Abrir Imagem Original
image = Image.open('../Images/Filo.jpg')
image.show()


#RESPOSTA DA ALTERNATIVA A
print('-------------------Alternativa A-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-a.tif')

# Converter imagem original em array
img_array = converting(image)

# Kernel (A) -  # Convolução usando filtro no modo reflect
K_A = np.array([[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]])

# Aplicando convolução
im = convolution(img_array, K_A)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/a.jpg')

#RESPOSTA DA ALTERNATIVA B

print('-------------------Alternativa B-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-b.tif')


# Kernel (B) -  # Convolução usando filtro no modo reflect
K_B = np.array([[1, 0, -1],
                [0, 0, 0],
                [-1, 0, 1]])

# Aplicando convolução
im = convolution(img_array, K_B)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/b.jpg')

#RESPOSTA DA ALTERNATIVA C

print('-------------------Alternativa C-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-c.tif')


# Kernel (C) -  # Convolução usando filtro no modo reflect
K_C = np.array([[0, -1, 0],
                [-1, 4, -1],
                [0, -1, 0]])

# Aplicando convolução
im = convolution(img_array, K_C)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/c.jpg')

#RESPOSTA DA ALTERNATIVA C

print('-------------------Alternativa D-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-d.tif')


# Kernel (D) -  # Convolução usando filtro no modo reflect
K_D = np.array([[-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]])

# Aplicando convolução
im = convolution(img_array, K_D)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/d.jpg')

print('-------------------Alternativa E-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-e.tif')


# Kernel (E) -  # Convolução usando filtro no modo reflect
K_E = np.array([[0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]])

# Aplicando convolução
im = convolution(img_array, K_E)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/e.jpg')

print('-------------------Alternativa F-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-f.tif')


# Kernel (F) -  # Convolução usando filtro no modo reflect
K_F = np.array([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]])

# Multiplicando pela constante
result_f = K_F*(1/9)

# Aplicando convolução
im = convolution(img_array, result_f)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/f.jpg')

print('-------------------Alternativa G-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-g.tif')


# Kernel (G) -  # Convolução usando filtro no modo reflect
K_G = np.array([[1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]])

# Multiplicando pela constante
result_g = K_G*(1/16)

# Aplicando convolução
im = convolution(img_array, result_g)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/g.jpg')

print('-------------------Alternativa H-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-h.tif')


# Kernel (H) -  # Convolução usando filtro no modo reflect
K_H = np.array([[1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]])

# Multiplicando pela constante
result_h = K_H*(1/256)

# Aplicando convolução
im = convolution(img_array, result_h)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/h.jpg')

print('-------------------Alternativa I-----------------------')
# Imagem filtrada usando ImageJ para comparação
openImageJ('../Images/ImageJ/Filo-ImageJ-i.tif')


# Kernel (I) -  # Convolução usando filtro no modo reflect
K_I = np.array([[1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, -476, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]])

# Multiplicando pela constante
result_i = K_I * (-1/256)

# Aplicando convolução
im = convolution(img_array, result_i)

# Convertendo array em imagem tipo usint uint8 e salvando imagem
img_out = convertUint8(im)
img_out.save('../Images/i.jpg')

