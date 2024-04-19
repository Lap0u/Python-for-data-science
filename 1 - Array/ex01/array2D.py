import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Returns a slice of the list from start to end"""
    assert isinstance(family, list), "The family should be a list"
    assert isinstance(start, int), "The start should be an integer"
    assert isinstance(end, int), "The end should be an integer"
    np_family = np.array(family)
    print("My shape is : ", np_family.shape)
    sliced_family = np_family[start:end]
    print("My new shape is : ", sliced_family.shape)
    return sliced_family.tolist()
