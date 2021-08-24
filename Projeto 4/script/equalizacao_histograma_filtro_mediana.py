import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def main():
    # Open image
    image_in = '../Images/enhance-me.gif'
    save_equalization = '../Images/equalization.jpg'

    # Load the Image
    image = Image.open(image_in)

    # Convert image to numpy array
    img_array = np.array(image)

    # Show original histogram
    plt.hist(img_array.flatten(),256,[0,256])
    plt.show()

    # Flattens the image array and calculates the histogram through binning
    histogram_array = np.bincount(img_array.flatten(), minlength=256)

    # Normalize
    num_pixels = np.sum(histogram_array)
    histogram_array = histogram_array / num_pixels

    # Normalized cumulative histogram
    chistogram_array = np.cumsum(histogram_array)

    # Pixel mapping lookup table
    transform_map = np.floor(255 * chistogram_array).astype(np.uint8)

    # Transformation

    # Flatten image array into 1D list
    img_list = list(img_array.flatten())

    # Transform pixel values to equalize
    eq_img_list = [transform_map[p] for p in img_list]

    # Reshape and write back into img_array
    eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)

    # Convert NumPy array to pillow Image and write to file
    eq_img = Image.fromarray(eq_img_array)
    eq_img.save(save_equalization)
    
    # Show equalized histogram
    equalized_img = Image.open('../Images/equalization.jpg')
    equalized_array = np.asarray(equalized_img)
    plt.hist(equalized_array.flatten(),256,[0,256])
    plt.show()
    

    # Applying Median Filter to equalized image

    img_equalized = '../Images/equalization.jpg'

    # Open Image
    image = Image.open(img_equalized)

    # Convert image to numpy array
    npImage = np.array(image)

    # Median filter
    m = npImage.shape[0]  # qtd linhas
    n = npImage.shape[1]  # qtd colunas

    for x in range(1, m - 2):
        for y in range(1, n - 2):
            w = npImage[x - 1:x + 2, y - 1:y + 2]
            npImage[x, y] = np.median(w).astype(int)
    
    # Show median filter image histogram
    plt.hist(npImage.flatten(),256,[0,256])
    plt.show()

    # Convert numpy array to pillow Image and write to file
    image_filtered = Image.fromarray(npImage)
    image_filtered.show()
    image_filtered.save('../Images/enhace-me-filtered.jpg')


if __name__ == "__main__":
    main()
