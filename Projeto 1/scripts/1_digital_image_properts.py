
import numpy as np
from PIL import Image
from numpy import asarray

# converting image to grayscale
image = Image.open('../Images/Filo.jpg').convert('L')
image.show()

def main():
    # Open image

    print(image.format)
    print(image.size)
    print(image.mode)
    #print(image.bits)
    print(image.getextrema())
    # convert image to numpy array
    npImage = np.array(image)
    print(type(npImage))
    # summarize shape
    print(npImage.shape)

    # value of pixel 0 0
    print(npImage[0][0])
    print(npImage[10][10])

    # values os a windows 5 X 5
    print(npImage[0:5, 0:5])

    # divide by 2 pixels
    npImage = (npImage / 2).astype(int)

    # values os a windows 5 X 5
    print(npImage[0:5, 0:5])

    # 1° Inversão de Pixels Usando For
    print("Inverting the pixels...")
    x, y = npImage.shape
    for i in range(x):
        for j in range(y):
            npImage[i,j] = abs(npImage[i,j] - 255)

    #Convert ndarray image to Pillow image
    image2 = Image.fromarray(npImage)
    image2.show()


    # create the histogram
    histogram, bin_edges = np.histogram(npImage, bins=256, range=(0, 255))
    print(histogram.shape)


if __name__ == "__main__":
    main()
