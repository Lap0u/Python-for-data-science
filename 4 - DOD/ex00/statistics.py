def ft_mean(data: list) -> None:
    """Prints the mean of the given numbers.
    The function can take any number of arguments and keyword arguments."""
    total = 0
    for value in data:
        total += value
    print(f"mean : {total / len(data)}")


def ft_median(data: list) -> None:
    """Prints the median of the given numbers.
    The function can take any number of arguments and keyword arguments."""
    if len(data) % 2 == 0:
        median = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
    else:
        median = data[len(data) // 2]
    print(f"median : {median}")


def ft_quartile(data: list) -> None:
    """Prints the quartile of the given numbers.
    The function can take any number of arguments and keyword arguments."""
    quartile_1 = data[len(data) // 4]
    quartile_3 = data[len(data) // 4 * 3]
    print(f"quartile : [{quartile_1}, {quartile_3}]")


def ft_variance(data: list) -> None:
    """Prints the variance of the given numbers.
    The function can take any number of arguments and keyword arguments."""
    pass


def ft_standard_deviation(data: list) -> None:
    """Prints the standard deviation of the given numbers.
    The function can take any number of arguments and keyword arguments."""
    total = 0
    for value in data:
        total += value
    mean = total / len(data)
    variance = 0
    for value in data:
        variance += (value - mean) ** 2
    variance /= len(data)
    standard_deviation = variance**0.5
    print(f"standard deviation : {standard_deviation}")


def call_stat_method(data, value):
    if value == "mean":
        ft_mean(data)
    elif value == "median":
        ft_median(data)
    elif value == "quartile":
        ft_quartile(data)
    elif value == "var":
        ft_variance(data)
    elif value == "std":
        ft_standard_deviation(data)


def ft_statistics(*args: float | int, **kwargs: float | int) -> None:
    """Prints the statistics of the given numbers.
    The function can take any number of arguments and keyword arguments."""
    if len(args) == 0 or len(kwargs) == 0:
        print("ERROR")
        return
    for value in args:
        if not isinstance(value, (int, float)):
            print("ERROR")
            return
    data = list(args)
    data.sort()
    for value in kwargs.values():
        call_stat_method(data, value)


# your code here
