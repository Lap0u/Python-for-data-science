def square(x: int | float) -> int | float:
    """Returns the square of the given number."""
    return x**2


def pow(x: int | float) -> int | float:
    """Returns the square of the given number."""
    return x**x


def outer(x: int | float, function) -> object:
    """returns an object that when called returns the result of the arguments
    calculation"""
    count = x

    def inner() -> float:
        """returns the result of the arguments calculation"""
        nonlocal count
        count = function(count)
        return count

    return inner
