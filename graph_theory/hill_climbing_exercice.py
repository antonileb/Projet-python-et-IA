import numpy as np

matrice = np.array([
    [4,4,2,1,1,0],
    [4,5,7,3,2,1],
    [3,10,8,4,2,6],
    [2,6,4,0,8,10],
    [1,0,2,6,15,12],
    [0,0,3,4,9,7]
])

paded_matrice = np.pad(matrice, 1, mode="constant")

print(paded_matrice)



def question1():
    i = 2 + 1
    j = 5 + 1
    etat_init = paded_matrice[i, j]
    chemin = [etat_init]
    while True:
        if etat_init >= paded_matrice[i + 1, j] and etat_init >= paded_matrice[i - 1, j] and etat_init >= paded_matrice[i, j + 1] and etat_init >= paded_matrice[i, j - 1]:
            etat_init = etat_init
            print("aucun voisin plus grand")
            break
        else:
            if paded_matrice[i + 1, j] > paded_matrice[i - 1, j] and paded_matrice[i + 1, j] > paded_matrice[i, j + 1] and paded_matrice[i + 1, j] > paded_matrice[i, j - 1]:
                etat_init =  paded_matrice[i + 1, j]
                i += 1
            elif paded_matrice[i - 1, j] > paded_matrice[i + 1, j] and paded_matrice[i - 1, j] > paded_matrice[i, j + 1] and paded_matrice[i - 1, j] > paded_matrice[i, j - 1]:
                etat_init = paded_matrice[i - 1, j]
                i -= 1
            elif paded_matrice[i, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i, j + 1] > paded_matrice[i, j - 1]:
                etat_init = paded_matrice[i, j + 1]
                j += 1
            else:
                etat_init = paded_matrice[i, j - 1]
                j -= 1
        chemin.append(etat_init)
    print(chemin)

question1()



def question2():
    i = 2 + 1
    j = 5 + 1
    etat_init = paded_matrice[i, j]
    print(etat_init)
    while True:
        if etat_init >= paded_matrice[i + 1, j] and etat_init >= paded_matrice[i - 1, j] and etat_init >= paded_matrice[i, j + 1] and etat_init >= paded_matrice[i,j-1] and etat_init >= paded_matrice[i + 1, j + 1] and etat_init >= paded_matrice[i - 1, j + 1] and etat_init >= paded_matrice[i + 1, j - 1] and etat_init >= paded_matrice[i - 1, j - 1]:
            etat_init = etat_init
            print("aucun voisin plus grand")
            break
        else:
            if paded_matrice[i + 1, j] > paded_matrice[i - 1, j] and paded_matrice[i + 1, j] > paded_matrice[i, j + 1] and paded_matrice[i + 1, j] > paded_matrice[i, j - 1] and paded_matrice[i + 1, j] > paded_matrice[i + 1, j + 1] and paded_matrice[i + 1, j] > paded_matrice[i - 1, j + 1] and paded_matrice[i + 1, j] > paded_matrice[i + 1, j - 1] and paded_matrice[i + 1, j] > paded_matrice[i - 1, j - 1]:
                etat_init =  paded_matrice[i + 1, j]
                i += 1
            elif paded_matrice[i - 1, j] > paded_matrice[i + 1, j] and paded_matrice[i - 1, j] > paded_matrice[i, j + 1] and paded_matrice[i - 1, j] > paded_matrice[i, j - 1] and paded_matrice[i - 1, j] > paded_matrice[i + 1, j + 1] and paded_matrice[i - 1, j] > paded_matrice[i - 1, j + 1] and paded_matrice[i - 1, j] > paded_matrice[i + 1, j - 1] and paded_matrice[i - 1, j] > paded_matrice[i - 1, j - 1]:
                etat_init = paded_matrice[i - 1, j]
                i -= 1
            elif paded_matrice[i, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i, j + 1] > paded_matrice[i, j - 1] and paded_matrice[i, j + 1] >= paded_matrice[i + 1, j + 1] and paded_matrice[i, j + 1] >= paded_matrice[i - 1, j + 1] and paded_matrice[i, j + 1] >= paded_matrice[i + 1, j - 1] and paded_matrice[i, j + 1] >= paded_matrice[i - 1, j - 1]:
                etat_init = paded_matrice[i, j + 1]
                j += 1
            elif paded_matrice[i, j - 1] > paded_matrice[i + 1, j] and paded_matrice[i, j - 1] > paded_matrice[i + 1, j] and paded_matrice[i, j - 1] > paded_matrice[i, j + 1] and paded_matrice[i, j - 1] >= paded_matrice[i + 1, j + 1] and paded_matrice[i, j - 1] >= paded_matrice[i - 1, j + 1] and paded_matrice[i, j - 1] >= paded_matrice[i + 1, j - 1] and paded_matrice[i, j - 1] >= paded_matrice[i - 1, j - 1]:
                etat_init = paded_matrice[i, j - 1]
                j -= 1
            elif paded_matrice[i + 1, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i + 1, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i + 1, j + 1] > paded_matrice[i, j + 1] and paded_matrice[i + 1, j + 1] >= paded_matrice[i, j - 1] and paded_matrice[i + 1, j + 1] >= paded_matrice[i - 1, j + 1] and paded_matrice[i + 1, j + 1] >= paded_matrice[i + 1, j - 1] and paded_matrice[i + 1, j + 1] >= paded_matrice[i - 1, j - 1]:
                etat_init = paded_matrice[i + 1, j + 1]
                i += 1
                j += 1
            elif paded_matrice[i - 1, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i - 1, j + 1] > paded_matrice[i + 1, j] and paded_matrice[i - 1, j + 1] > paded_matrice[i, j + 1] and paded_matrice[i - 1, j + 1] >= paded_matrice[i, j - 1] and paded_matrice[i - 1, j + 1] >= paded_matrice[i + 1, j + 1] and paded_matrice[i - 1, j + 1] >= paded_matrice[i + 1, j - 1] and paded_matrice[i - 1, j + 1] >= paded_matrice[i - 1, j - 1]:
                etat_init = paded_matrice[i - 1, j + 1]
                i -= 1
                j += 1
            elif paded_matrice[i + 1, j - 1] > paded_matrice[i + 1, j] and paded_matrice[i + 1, j - 1] > paded_matrice[i + 1, j] and paded_matrice[i + 1, j - 1] > paded_matrice[i, j + 1] and paded_matrice[i + 1, j - 1] >= paded_matrice[i, j - 1] and paded_matrice[i + 1, j - 1] >= paded_matrice[i + 1, j + 1] and paded_matrice[i + 1, j - 1] >= paded_matrice[i - 1, j + 1] and paded_matrice[i + 1, j - 1] >= paded_matrice[i - 1, j - 1]:
                etat_init = paded_matrice[i + 1, j - 1]
                i += 1
                j -= 1
            else:
                etat_init = paded_matrice[i - 1, j - 1]
                i -= 1
                j -= 1
        print(etat_init)

