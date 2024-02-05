from Board import Board
from Chicken import Chicken
from Fox import Fox
from Viper import Viper

import random

# Initializing global variables
board = Board()
animal_list = [[Chicken()],[Fox()],[Viper()]]
animal_name = ["Chicken","Fox","Viper"]
nb_each_animal = 3
update_time = 1

### Fonctions ###
# Copy the animal_list in a list without animal_seperation
def Copy_list():
    copy_list = []
    for list in animal_list:
        for animal in list:
            copy_list.append(animal)
    return copy_list


# Returns a new animal similar to the target, and retrieves the index of the corresponding animal in "animal_list"
def New_animal(target):
    for i in range(len(animal_name)):
        if target.name == animal_name[i]:
            if i == 0:
                new_animal = Chicken()
                break
            elif i == 1:
                new_animal = Fox()
                break
            else:
                new_animal = Viper()
                break
    return new_animal, i

# Returns updated animal information
def Maj(animal):
    print(animal.number, animal.name, animal.position, animal.health, animal.food_bar)

# Returns the list sorted by animals composed of all the positions taken (only looks at the animals)
def Taken_places():
    taken_place = []
    for list in animal_list:
        taken_place_same = []
        for animal in list:
            taken_place_same.append(animal.position)
        taken_place.append(taken_place_same)
    return taken_place

# Returns the list of available positions around a target (looks at the board and the animals)
def Available_space(target):
    liste_pos, taken_place = [], []
    for list in Taken_places():
        taken_place += list
    x, y = target.position
    for dx, dy in target.movement:
        if 0.5 <= x+dx <= board.x and 0.5 <= y+dy <= board.y and (x+dx,y+dy) not in taken_place:
            liste_pos.append((x+dx, y+dy))
    return liste_pos

# Returns the list of available positions around several targets (looks at the board and the animals)
def Available_spaces(list_target):
    listes_pos = []
    for target in list_target:
        liste_pos = Available_space(target)
        listes_pos += liste_pos
    return list(set(listes_pos))

# Returns a random position relative to the list of "available_spaces(.)"
def Change_pos(list_target):
    list_pos = Available_spaces(list_target)
    end_pos = random.choice(list_pos)
    return end_pos

# # Returns the animal after mouvements
def Movement(animal):
    acted = False
    list_pos = Available_space(animal)
    if len(list_pos) > 0:
        acted = True
        end_pos = random.choice(list_pos)
        animal.position = end_pos
        print("Movement")
        Maj(animal)
        print("--------------------")
    return acted

# Returns the list sorted by subjective status of animals detected around a target
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

# Reverses the action of an attack from one animal to another
def Attack(animal_1):
    acted = False
    detection = Animal_detections(animal_1)[0]
    if len(detection) > 0:
        animal_2 = detection[0]
        if animal_1.base_target == animal_2.name:
            acted = True
            print("Attacked animal")
            Maj(animal_2)
            index = animal_name.index(animal_2.name)
            list = animal_list[index]
            list.remove(animal_2)
            animal_list[index] = list
            animal_1.attack(animal_2)
            print("Attacker animal")
            Maj(animal_1)
            print("--------------------")
        elif animal_2.base_target == animal_1.name:
            acted = True
            print("Attacked animal")
            Maj(animal_1)
            index = animal_name.index(animal_1.name)
            list = animal_list[index]
            list.remove(animal_1)
            animal_list[index] = list
            animal_2.attack(animal_1)
            print("Attacker animal")
            Maj(animal_2)
            print("--------------------")
    return acted

# Returns the action of procreation between 2 animals
def Procreation(animal_1):
    acted = False
    if animal_1.food_bar > animal_1.lost_food_per_procreation:
        detection = Animal_detections(animal_1)[1]
        if len(detection) > 0:
            animal_2 = detection[0]
            for animal_2_ in detection:
                if animal_2.food_bar < animal_2_.food_bar:
                    animal_2 = animal_2_
            if animal_2.food_bar > animal_2.lost_food_per_procreation:
                avaible_space_born = Available_spaces([animal_1,animal_2])
                if len(avaible_space_born) > 0:
                    acted = True
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
                    print("--------------------")
    return acted

# Returns the thing which goes when an animal is dead
def Death(animal):
    print("Hunger death")
    Maj(animal)
    print("--------------------")
    index = animal_name.index(animal.name)
    list = animal_list[index]
    list.remove(animal)
    animal_list[index] = list
    del animal

# Returns the animal creation set-up for the start of the game
def Start_position():
    for i in range(nb_each_animal-1):
        end_pos_poule = Change_pos(animal_list[0])
        poule = Chicken()
        poule.position = end_pos_poule
        animal_list[0].append(poule)

        end_pos_renard = Change_pos(animal_list[1])
        renard = Fox()
        renard.position = end_pos_renard
        animal_list[1].append(renard)
    
        end_pos_viper = Change_pos(animal_list[2])
        viper = Viper()
        viper.position = end_pos_viper
        animal_list[2].append(viper)