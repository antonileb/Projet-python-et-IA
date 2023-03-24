dict_fn = {
    5:3,
    6:2,
    7:4,
    8:5,
    9:6,
    10:7,
    11:8,
    12:10,
    13:9
}
dict_noeud = {
    6 : {5: 3, 7: 4},
    7 : {6: 2, 8: 5},
    8 : {7: 4, 9: 6},
    9 : {8: 5, 10: 7},
    10 : {9: 6, 11: 8},
    11 : {10: 7, 12: 10},
    12 : {11: 8, 13: 9},
    13 : {12: 10, 14: 7}
}

def get_key(val):
    for key, value in dict_noeud.items():
        if val == value:
            return key
    return "key doesn't exist"

nd_n = 6
while True:
    if dict_noeud[nd_n][nd_n - 1] <= dict_fn[nd_n] and dict_noeud[nd_n][nd_n + 1] <= dict_fn[nd_n]:
        nd_prime = nd_n
        break
    else:
        if dict_noeud[nd_n][nd_n - 1] > dict_noeud[nd_n][nd_n + 1]:
            nd_prime = get_key(dict_noeud[nd_n - 1])
            nd_n = nd_prime
        else:
             nd_prime = get_key(dict_noeud[nd_n + 1])
             nd_n = nd_prime
    print(nd_n)  