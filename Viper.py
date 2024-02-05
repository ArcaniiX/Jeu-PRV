from Animal import Animal
from Board import Board

board = Board()

class Viper(Animal):
    def __init__(self):
        super().__init__()
        Animal._nb_animal += 1
        self.number = Animal._nb_animal
        self.position = (board.x - 0.5, 0.5)
        self.name = "Viper"
        self.base_target = "Fox"
        self.color = "gs"
        self.color_texte = "Green"
        