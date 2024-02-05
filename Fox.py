from Animal import Animal
from Board import Board

board = Board()

class Fox(Animal):
    def __init__(self):
        super().__init__()
        Animal._nb_animal += 1
        self.number = Animal._nb_animal
        self.position = (0.5, 0.5)
        self.name = "Fox"
        self.base_target = "Chicken"
        self.color = "rs"
        self.color_texte = "Red"
