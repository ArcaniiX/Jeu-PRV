from Board import Board
from Poule import Poule
from Renard import Renard
from Viper import Viper

import matplotlib.pyplot as plt
import random

# Initialisation variables globales
board = Board()
animal_list = [[Poule()],[Renard()],[Viper()]]
animal_name = ["Poule","Renard","Viper"]
nb_each_animal = 5
update_time = 1

### Fonctions ###
# Retourne un nouvel animal semblable à la cible, et récupère l'indice de l'animal correspondant dans "animal_list"
def New_animal(target):
    for i in range(len(animal_name)):
        if target.name == animal_name[i]:
            if i == 0:
                new_animal = Poule()
                break
            elif i == 1:
                new_animal = Renard()
                break
            else:
                new_animal = Viper()
                break
    return new_animal, i

# Retourne les infos MAJ de l'animal
def Maj(animal):
    print(animal.number, animal.name, animal.position, animal.health, animal.food_bar)

# Retourne la liste triée par animaux composée de toutes les positions prises (ne regarde que les animaux)
def Taken_places():
    taken_place = []
    for list in animal_list:
        taken_place_same = []
        for animal in list:
            taken_place_same.append(animal.position)
        taken_place.append(taken_place_same)
    return taken_place

# Retourne la liste des positions disponibles autour d'une cible (regarde le board et les animaux)
def Available_space(target):
    liste_pos, taken_place = [], []
    for list in Taken_places():
        taken_place += list
    x, y = target.position
    for dx, dy in target.movement:
        if 0.5 <= x+dx <= board.x and 0.5 <= y+dy <= board.y and (x+dx,y+dy) not in taken_place:
            liste_pos.append((x+dx, y+dy))
    return liste_pos

# Retourne la liste des positions disponibles autour de plusieurs cibles (regarde le board et les animaux)
def Available_spaces(list_target):
    listes_pos = []
    for target in list_target:
        liste_pos = Available_space(target)
        listes_pos += liste_pos
    return list(set(listes_pos))

# Retourne une position aléatoire par rapport à la liste des "available_spaces(.)"
def Change_pos(list_target):
    list_pos = Available_spaces(list_target)
    end_pos = random.choice(list_pos)
    return end_pos

# Retourne la liste triée par statut subjectif des animaux détectés autour d'une cible
def Animal_detections(animal_1):
    detection = [[],[],[]]                          # [[attack],[procreation],[]]
    x1, y1 = animal_1.position
    for dx1, dy1 in animal_1.movement:
        for list in animal_list:
            for animal_2 in list:
                x2, y2 = animal_2.position
                if x1+dx1 == x2 and y1+dy1 == y2:
                    if animal_1.base_target == animal_2.name or animal_2.base_target == animal_1.name:
                        detection[0].append(animal_2)
                    elif animal_1.name == animal_2.name and animal_1.food_bar >= animal_1.min_food_procreation and animal_2.food_bar >= animal_2.min_food_procreation:
                        detection[1].append(animal_2)
                    else:
                        detection[2].append(animal_2)
    return detection

# Retourne l'action d'une attaque d'un animal sur un autre
def Attack(animal_1):
    detection = Animal_detections(animal_1)[0]
    if len(detection) > 0:
        animal_2 = detection[0]
        if animal_1.base_target == animal_2.name:
            print("Attacked animal")
            Maj(animal_2)
            list = animal_list[animal_name.index(animal_2.name)]
            list.remove(animal_2)
            animal_1.attack(animal_2)
            print("Attacker animal")
            Maj(animal_1)
        elif animal_2.base_target == animal_1.name:
            print("Attacked animal")
            Maj(animal_1)
            list = animal_list[animal_name.index(animal_1.name)]
            list.remove(animal_1)
            animal_2.attack(animal_1)
            print("Attacker animal")
            Maj(animal_2)

# Retourne l'action de procréation entre 2 animaux 
def Procreation(animal_1):
    detection = Animal_detections(animal_1)[1]
    if len(detection) > 0:
        animal_2 = detection[0]
        for animal_2_ in detection:
            if animal_2.food_bar < animal_2_.food_bar:
                animal_2 = animal_2_
        avaible_space_born = Available_spaces([animal_1,animal_2])
        if len(avaible_space_born) > 0:
            end_pos = random.choice(avaible_space_born)

            animal_3, index = New_animal(animal_1)
            animal_3.position = end_pos
            animal_list[index].append(animal_3)

            animal_1.food_bar -= animal_1.lost_food_per_procreation
            animal_2.food_bar -= animal_2.lost_food_per_procreation
            print("Procreated animal")
            Maj(animal_3)
            print("Parent animal")
            Maj(animal_1)
            Maj(animal_2)

# Retourne le set-up de création d'animaux pour le début de game
def Start_position():
    for i in range(nb_each_animal-1):
        end_pos_poule = Change_pos(animal_list[0])
        poule = Poule()
        poule.position = end_pos_poule
        animal_list[0].append(poule)

        end_pos_renard = Change_pos(animal_list[1])
        renard = Renard()
        renard.position = end_pos_renard
        animal_list[1].append(renard)
    
        end_pos_viper = Change_pos(animal_list[2])
        viper = Viper()
        viper.position = end_pos_viper
        animal_list[2].append(viper)

# Retourne l'affiche du board et tous les animaux vivants
def Affichage():
    global graph
    for i in range(len(animal_list)):
        for animal in animal_list[i]:
            graph = plt.plot(animal.position[0],animal.position[1],animal.color,markersize=10)
            plt.show()
            plt.pause(update_time)
            graph.remove()
    

# Retourne le jeu
def Main():
    pass

# Fonctions d'essais
Start_position()
print("Start")
board.__str__()
Affichage()
print("\nProcréation :")
print("---------------------------")
Procreation(animal_list[0][-1])
print("\n")
Procreation(animal_list[1][-1])
print("\n")
Procreation(animal_list[2][-1])
print("---------------------------")
print("\nAttaques :")
print("---------------------------")
Attack(animal_list[0][-1])
print("\n")
Attack(animal_list[1][-1])
print("\n")
Attack(animal_list[2][-1])
print("---------------------------")
