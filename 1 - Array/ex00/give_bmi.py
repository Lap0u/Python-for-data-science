import numpy as np


def give_bmi(height: list[float], weight: list[float]) -> list[int | float]:
    """Returns the BMI for each elements in the list.
    The formula for BMI is weight in kilograms
    divided by height in meters squared"""
    assert isinstance(height, list), "The height should be a list"
    assert isinstance(weight, list), "The weight should be a list"
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
    bmi_list = weight / (height**2)
    return bmi_list.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of boolean values where True
    indicates that the BMI is above the limit"""
    assert isinstance(bmi, list), "The BMI should be a list"
    assert isinstance(limit, int), "The limit should be an integer"
    bmi = np.array(bmi)
    assert (
        bmi.dtype == np.float64 or bmi.dtype == np.int64
    ), "The BMI array should contain only integers or floats"
    return [i > limit for i in bmi]
