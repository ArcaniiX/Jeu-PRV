from Board import Board
from Chicken import Chicken
from Fox import Fox
from Viper import Viper
from Logical_functions import *
from Display import *

from copy import deepcopy

# Initializing global variables
nb_lap = 100

# Return the game
def Main():
    # Start :
    Start_position()
    print("-----")
    print("Start")
    print("-----")
    print("\n\n")
    Display()

    # Laps :
    lap, nb_animal = 0, nb_each_animal*len(animal_list)
    while lap < nb_lap and nb_animal > 1:
        print("Lap : " + str(lap+1))
        # Setup the copy of animal_list
        copy_list = Copy_list()
        animal = random.choice(copy_list)

        acted = Attack(animal)
        if acted == False:
            acted = Procreation(animal)
            if acted == False:
                acted = Movement(animal)
                if acted == False:
                    print("Any possible action")
                    Maj(animal)
                    print("--------------------")
        animal.food_bar -= animal.lost_food_per_lap
        if animal.food_bar <= 0 and animal in animal_list[animal_name.index(animal.name)]:
            Death(animal)

        Display()
        print("\n")
        lap += 1
        nb_animal = len(copy_list)

    # Return the game
    plt.show()
    plt.close()
    print("-----")
    print("End")
    print("-----")

Main()

