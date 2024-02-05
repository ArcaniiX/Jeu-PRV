class Animal():
    _nb_animal = -1

    def __init__(self):
        self.max_health = 1
        self.health = self.max_health
        self.max_food = 10
        self.food_bar = self.max_food
        self.lost_food_per_lap = 1
        self.food_intake = self.max_food          # Apport en nourriture = Manger
        self.min_food_procreation = 6
        self.lost_food_per_procreation = 4
        self.right = (1,0)
        self.left = (-1,0)
        self.up = (0,1)
        self.down = (0,-1)
        self.movement = [self.down, self.up, self.left, self.right]
    
    def attack(self,target):
        target.health -= 1
        del target
        # Manger augmente la barre de nourriture : Soit au max, soit la nourriture possédée + la nourriture aquise
        self.food_bar = min(self.food_bar + self.food_intake, self.max_food)
        
    