from Board import Board
from Chicken import Chicken
from Fox import Fox
from Viper import Viper
from Logical_functions import *

import matplotlib.pyplot as plt

# Retourne l'affiche du board et tous les animaux vivants
def Display():
    plt.clf()
    board.__str__()
    for i in range(len(animal_list)):
        for animal in animal_list[i]:
            plt.plot(animal.position[0],animal.position[1],animal.color,markersize=10)
    plt.pause(update_time)