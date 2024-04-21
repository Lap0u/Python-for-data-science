class calculator:
    """A class that represents a calculator.
    It has a data attribute that is a list of numbers"""

    def __init__(self, data) -> None:
        """Constructor for this class.
        Initializes the data attribute with the data parameter."""
        self.data = data

    def __add__(self, value) -> None:
        """Add number to each element and print the result."""
        self.data = [x + value for x in self.data]
        print(self.data)

    def __mul__(self, value) -> None:
        """Multiply each element by the number and print the result."""
        self.data = [x * value for x in self.data]
        print(self.data)

    def __sub__(self, value) -> None:
        """Subtract the number from each element and print the result."""
        self.data = [x - value for x in self.data]
        print(self.data)

    def __truediv__(self, value) -> None:
        """Divide each element by the number and print the result."""
        if value == 0:
            print("Can't divide by zero!")
            return
        self.data = [x / value for x in self.data]
        print(self.data)
