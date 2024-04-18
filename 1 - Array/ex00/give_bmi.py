import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Returns the BMI for each elements in the list.
    The formula for BMI is weight in kilograms divided by height in meters squared"""
    height = np.array(height)
    weight = np.array(weight)
    assert (
        height.shape == weight.shape
    ), "The shape of the two arrays should be the same"
    assert (
        height.dtype == np.float64 or height.dtype == np.int64
    ), "The height array should contain only integers or floats"
    assert (
        weight.dtype == np.float64 or weight.dtype == np.int64
    ), "The weight array should contain only integers or floats"
    bmi_list = weight / (height / 100) ** 2
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of boolean values where True indicates that the BMI is above the limit"""
    bmi = np.array(bmi)
    print(bmi.dtype, bmi)
    assert (
        bmi.dtype == np.float64 or bmi.dtype == np.int64
    ), "The BMI array should contain only integers or floats"
    return bmi > limit
