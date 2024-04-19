import numpy as np
from load_image import ft_load
from matplotlib import pyplot as plt


def rotate_image(image: np.ndarray):
    """Rotates a numpy array by 90 degrees counter clockwise."""
    res_img = np.zeros((image.shape[1], image.shape[0]), dtype=image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            res_img[j, i] = image[i, j]
    return res_img


def main():
    """Opens an image, cut it and rotate by 90 degrees"""
    img_data = ft_load("animal.jpeg")
    assert isinstance(img_data, np.ndarray), "Image data not found"
    sliced_img = img_data[50:450, 450:850, 0]
    print("The shape of the image is :", sliced_img.shape)
    print(sliced_img)
    rotated_img = rotate_image(sliced_img)
    print("New shape after Transpose :", rotated_img.shape)
    print(rotated_img)
    plt.imshow(rotated_img, interpolation="nearest")
    plt.show()


if __name__ == "__main__":
    main()
