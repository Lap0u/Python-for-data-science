from S1E9 import Character


class Baratheon(Character):
    """The Baratheon class that inherits from Character."""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        return f"{self.first_name} {self.family_name} {self.eyes} {self.hairs}"

    def __repr__(self) -> str:
        return f"{self.first_name} {self.family_name} {self.eyes} {self.hairs}"

    def die(self):
        """Sets the is_alive attribute to False"""
        self.is_alive = False

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)


class Lannister(Character):
    """The Lannister class that inherits from Character."""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Sets the is_alive attribute to False"""
        self.is_alive = False

    def __str__(self) -> str:
        return f"{self.first_name} {self.family_name} {self.eyes} {self.hairs}"

    def __repr__(self) -> str:
        return f"{self.first_name} {self.family_name} {self.eyes} {self.hairs}"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
