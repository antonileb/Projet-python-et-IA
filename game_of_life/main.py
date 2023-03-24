import numpy
import time
import os

frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]])

def compute_number_alive_neighbors(paded_frame, index_line, index_column):
    number_alive_neighbors = paded_frame[index_line - 1][index_column - 1] + paded_frame[index_line - 1][index_column] + paded_frame[index_line - 1][index_column + 1] +\
                             paded_frame[index_line][index_column - 1] + paded_frame[index_line][index_column + 1] +\
                             paded_frame[index_line + 1][index_column - 1] + paded_frame[index_line + 1][index_column] + paded_frame[index_line + 1][index_column + 1]

    return number_alive_neighbors

def compute_next_frame(frame):
    # ici on créer à partir de notre frame une nouvelle frame qui va etre paded (entouré) de 0, donc on ajoute 1 ligne en haut et en bas et une column a gauche et a droite
    paded_frame = numpy.pad(frame, 1, mode="constant")
    # ici on fait un raster scan (méthode qui consiste à parcourir tous les éléments d'une matrice ou d'un tableau). Quand on fini tous les éléments de la ligne 1 on passe à la ligne en dessous. 1er for pour parcourir les lignes, 2eme for pour parcourir les column dans les lignes
    #ici on loupe sur la frame non paded
    for index_line in range(0, frame.shape[0]): # shape[0] donne le nb de ligne
        for index_column in range(0, frame.shape[1]): # shape[1] donne le nb de column
            number_alive_neighbor =  compute_number_alive_neighbors(paded_frame, index_line + 1, index_column + 1) # on fait + 1 car on a paded la frame

            if frame[index_line][index_column] == 0 and number_alive_neighbor == 3:
                frame[index_line][index_column] = 1
            elif  frame[index_line][index_column] == 1 and not (number_alive_neighbor == 2 or number_alive_neighbor == 3):
                frame[index_line][index_column] = 0

while True:
    #grace a la bibli os on peut ecrire des commande bash, ici on demande à clear notre terminal apres chaque tour de boucle
    os.system("cls")
    print(frame)
    # time.sleep c'est pour dire d'attendre un certain temps (en seconde) avant de faire autre chose, ici on attend 1 seconde avant d'afficher la frame suivante
    time.sleep(1)
    compute_next_frame(frame)