import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file and display it as an array of pixels"""
    assert isinstance(path, str), "The path should be a string"
    assert path != "", "The path should not be empty"
    try:
        img = Image.open(path)
        img.load()
        data = np.asarray(img, dtype="int32")
        return data
    except FileNotFoundError:
        print("The file does not exist")
        return []
    except PermissionError:
        print("You do not have the permission to read the file")
        return []
    except OSError:
        print("The file is not a valid image")
        return []
