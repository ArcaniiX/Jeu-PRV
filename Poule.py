from Animal import Animal
from Board import Board

board = Board()

class Poule(Animal):
    def __init__(self):
        super().__init__()
        Animal._nb_animal += 1
        self.number = Animal._nb_animal
        self.position = (board.x//2 + 0.5, board.y - 0.5)
        self.name = "Poule"
        self.base_target = "Viper"
        self.color = "bs"
        self.color_texte = "Blue"