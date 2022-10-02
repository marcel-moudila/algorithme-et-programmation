def fusionner(T_1, T_2):
    i = 0
    j = 0
    len_T1 =len(T_1)
    len_T2 =len(T_2)
    Tnew = []
    while len_T1 > i and len_T2 > j :
        if T_1[i] < T_2[j]:
            Tnew += [T_1[i]]
            i += 1
        else:
            Tnew += [T_2[j]]
            j += 1
    while i < len_T1:
        Tnew += [T_1[i]]
        i += 1
    while j < len_T2:
        Tnew += [T_2[j]]
        j += 1
    return Tnew


def triFusion(T):
    if len(T) <= 1 :
        return T
    k = len(T)//2
    T_1 = T[:k]
    T_2 = T[k:]
    gauche = triFusion(T_1)
    droite = triFusion(T_2)
    fusionne = fusionner(gauche, droite)
    return fusionne


#je teste
print("triFusion([14, 14, 7, 7, 5, 5, 1, 1, 0]) = ",triFusion([14, 14, 7, 7, 5, 5, 1, 1, 0]))

print()

print("triFusion([14, -2, 7, 7, 5, 5, -1, 1, 2]) = ",triFusion([14, -2, 7, 7, 5, 5, -1, 1, 2]))
