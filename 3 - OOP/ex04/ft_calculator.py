class calculator:
    """A class that represents a calculator of vectors."""

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """Calculates the dot product of two vectors."""
        res = 0
        for i in range(len(v1)):
            res += v1[i] * v2[i]
        print(f"Dot product is {res}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Adds two vectors together."""
        res = []
        for i in range(len(v1)):
            res.append(v1[i] + v2[i])
        print(f"Add vector is {res}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Subtracts two vectors."""
        res = []
        for i in range(len(v1)):
            res.append(v1[i] - v2[i])
        print(f"Add vector is {res}")
