import numpy as np
from matplotlib import pyplot as plt


def ft_print_image(array) -> None:
    """Print an image."""
    plt.imshow(array, interpolation="nearest")
    plt.show()


def ft_invert(array) -> np.ndarray:
    """Invert the colors of an image."""
    copy = array.copy()
    copy = 255 - copy
    ft_print_image(copy)
    return copy


def ft_red(array) -> np.ndarray:
    """Apply a red filter to an image."""
    copy = array.copy()
    for i in range(copy.shape[0]):
        for j in range(copy.shape[1]):
            copy[i, j, 1] *= 0
            copy[i, j, 2] *= 0
    ft_print_image(copy)
    return copy


def ft_green(array) -> np.ndarray:
    """Apply a green filter to an image."""
    copy = array.copy()
    for i in range(copy.shape[0]):
        for j in range(copy.shape[1]):
            copy[i, j, 0] -= copy[i, j, 0]
            copy[i, j, 2] -= copy[i, j, 2]
    ft_print_image(copy)
    return copy


def ft_blue(array) -> np.ndarray:
    """Apply a blue filter to an image."""
    copy = array.copy()
    for i in range(copy.shape[0]):
        for j in range(copy.shape[1]):
            copy[i, j, 0] = 0
            copy[i, j, 1] = 0
    ft_print_image(copy)
    return copy


# greyscale formula
# https://www.geeksforgeeks.org/matlab-rgb-image-to-grayscale-image-conversion/
def ft_grey(array) -> np.ndarray:
    """Apply a grey filter to an image."""
    copy = array.copy()
    for i in range(copy.shape[0]):
        for j in range(copy.shape[1]):
            red_scaled = copy[i, j, 0] * 0.2989
            green_scaled = copy[i, j, 1] * 0.5870
            blue_scaled = copy[i, j, 2] * 0.1140
            grey = int(red_scaled + green_scaled + blue_scaled)
            copy[i, j] = [grey, grey, grey]
    ft_print_image(copy)
    return copy
