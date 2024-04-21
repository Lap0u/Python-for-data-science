from abc import ABC, abstractmethod


class Character(ABC):
    """The abstract class for the characters in the series.
    It has the following attributes:
    - first_name: a string representing the first name of the character
    - is_alive: a boolean representing if the character is alive or not
    It has the following methods:
      - die: a method that sets the is_alive attribute to False"""

    def __init__(self, first_name, is_alive=True):
        """Initializes the character class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """The Stark class that inherits from Character.
    It has the following attributes:
    - first_name: a string representing the first name of the character
    - is_alive: a boolean representing if the character is alive or not
    It has the following methods:
      - die: a method that sets the is_alive attribute to False"""

    def __init__(self, first_name, is_alive=True):
        """Initializes the Stark class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Sets the is_alive attribute to False"""
        self.is_alive = False
