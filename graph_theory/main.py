from operator import itemgetter

# h(n)
heuristique = {"A": 4, "B": 2, "C": 2, "D": 2, "E": 1, "F": 3, "G": 4, "H": 0}


graph = {
    "A": {"B": 3, "C": 1, "D": 1},
    "B": {"E": 1, "F": 1},
    "C": {"F": 3, "G": 2},
    "D": {"G": 1, "H": 6},
    "E": {"H": 1},
    "F": {"H": 3},
    "G": {"H": 5},
    "H": True
}


# g(n)
def cout_trajet_g(n0, n1, n2):
    if n1[0] == "E" or n1[0] == "F" or n1[0] == "G":
        cout_g = graph[n1[0]][n2] + graph[n1[2]][n1[0]] + graph[n0[0]][n1[2]]
    elif n1[0] == "B" or n1[0] == "C" or n1[0] == "D":
        cout_g = graph[n1[0]][n2] + graph[n0[0]][n1[0]]
    else: 
        cout_g = graph[n1[0]][n2]
    return cout_g

# f(n) = g(n) + h(n)
def cout_total_f(n0, n1, n2):
    cout_total = cout_trajet_g(n0, n1, n2) + heuristique[n2[0]]
    return cout_total

def recherche_dans_graphe(n0):
    open = []
    closed = []
    open.append(n0)
    print(open)
    while True:
        if len(open) == 0:
            print("aucune solution n'existe")
            break
        n1 = open[0]
        open.remove(n1)
        closed.append(n1)
        if n1[0] == "H":
            print("solution trouvé !")
            print(closed[-3][-1], closed[-2][-1], parent_n2, n1[0])
            break
        for n2 in graph[n1[0]]:
            parent_n2 = n1[0]
            cout_f = cout_total_f(n0, n1, n2)
            open.append([n2, cout_f, parent_n2])
        open = sorted(open, key=itemgetter(1))
        print("open : ", open)
        print("closed : ", closed)
            # if n2 in open[0] and cout_f < open[1]:
            #     open.remove(open[0])
            # open.append([n2, cout_f, parent_n2])
            # open = sorted(open, key=itemgetter(1))
            # print("open : ", open)
            # print("closed : ", closed)

recherche_dans_graphe(["A", heuristique["A"], None])