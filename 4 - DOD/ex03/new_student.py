import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15 characters long string."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class using dataclass"""

    name: str
    surname: str
    login: str = field(init=False)
    id: str = field(init=False)
    active: bool = True

    def __post_init__(self):
        """Generates login from name and surname after __init__."""
        self.login = self.name[0] + self.surname.lower()
        self.id = generate_id()
