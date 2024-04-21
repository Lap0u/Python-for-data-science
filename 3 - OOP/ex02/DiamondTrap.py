from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, name):
        """Initializes the King class with the name of the king."""
        Lannister.__init__(self, name)
        Baratheon.__init__(self, name)

    def set_eyes(self, eyes):
        """Sets the eyes of the king."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Sets the hairs of the king."""
        self.hairs = hairs

    def get_eyes(self):
        """Returns the eyes of the king."""
        return self.eyes

    def get_hairs(self):
        """Returns the hairs of the king."""
        return self.hairs
