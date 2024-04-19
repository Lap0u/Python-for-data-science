import numpy as np
from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    """Open an image, zoom it and display it with matplotlib."""
    img_data = ft_load("animal.jpeg")
    assert isinstance(img_data, np.ndarray), "Image data not found"
    print("The shape of the image is :", img_data.shape)
    print(img_data)
    sliced_img = img_data[50:450, 450:850, 0:1]
    print("New shape after slicing :", sliced_img.shape)
    print(sliced_img)
    plt.imshow(sliced_img, interpolation="nearest")
    plt.show()


if __name__ == "__main__":
    main()
