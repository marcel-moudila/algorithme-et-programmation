print(" ======= test de mes fonctions annexes ====== ")
# Des fonctions intermédiaires

# Donne le nbre d'occurence d'un elt                             #fonction 1
def nombreOccu(liste,entier):
    resultat = len(liste) - len(supprimerElement(liste,entier))  
    return resultat


# Supprime un elt et ses occurences                              #fonction 2
def supprimerElement(liste,entier):
    liste1 =[i for i in liste if i!= entier]                                          
    return liste1

# Donne l'index de la premiere occurrence d'un elt              #fonction 3
def premiereOccu(liste,entier):
    if entier not in liste :
        return "n'est pas dans la liste"
    else:
        i = 0
        while liste[i] != entier:
            i = i +1
        return i

# Inserre un elt à l'index voulu                                #fonction 4
def insererListe(liste,entier,index):
    if index > len(liste):
        return " pas possible "
    
    else: 
        liste1 = liste[0:index]
        liste2 = liste[index:]
        liste3 = liste1 + [entier] + liste2
        return liste3

# Supprime la premiere occurence d'un elt                       #fonction 5
def supprimerPremiereOccu(liste,entier):
    n = premiereOccu(liste,entier)
    if n == 0:
        return liste[1:]
    else :
        return liste[0:n] + liste[n+1:]

# Inserre un elt dans une liste triée en croissant              #fonction 6
def insererDansListeTrie(liste,entier):
    if len(liste)== 0:
        Tnew = [entier]
        return Tnew
    elif entier > max(liste):
        Tnew = liste + [entier]
        return Tnew
    else :
        i = 0
        while (liste[i] <= entier) and entier <= max(liste):
            i = i +1
        Tnew = insererListe(liste,entier,i)
        return Tnew


#je teste
print(nombreOccu([1,2,6,1,1,8,1],1))
print(supprimerElement([1,2,3],3))
print(premiereOccu([1,2,3,1],1))
print(insererListe([1,2,3],0,3))
print(supprimerPremiereOccu([1,2,3,3,1],3))
print(insererDansListeTrie([6,8,10,12],9))

print(" ============= Exercice 2 (tri par insertion) ====================== ")
def triParInsertion(liste):
    Tnew = []
    i = 0
    while len(liste) > 0:
        entier = liste[i]
        Tnew = insererDansListeTrie(Tnew,entier)
        liste = supprimerPremiereOccu(liste,entier)  
        i = 0
    return Tnew
    
# je teste
print(triParInsertion([7, 8, 3, 1, 9, 2, 4, 15, 11,1,3]))

print(" ======= Exercice 3 (Tri par Selection) ============== ")
def triParSelection(liste):
    Tnew = []
    while len(liste) > 0:
        valeurMax = max(liste)
        Tnew = [valeurMax]*nombreOccu(liste,valeurMax) + Tnew
        liste = supprimerElement(liste,valeurMax)
    return  Tnew

#je teste
print(triParSelection([6,5,3,5,4,2,3,3,5,6,1,10,6,1]))
                                      
print(" ====== Exercice 4 (tri par Fréquence ) ============== ")
def triParFreq(liste):
    taille = max(liste)+1
    TF = [0]* taille
    for i in range(taille):
        TF[i]= nombreOccu(liste,i)
    return TF

#je teste
print(triParFreq([1,4,0,2,1,4,2,4,1]))

print(" ==== Exercice 5 (tri fusion) ======= ")

def fusion(T):
    if len(T) <= 1 :
        return T
    k = len(T)//2
    T_1 = T[:k]
    T_2 = T[k:]
    gauche = fusion(T_1)
    droite = fusion(T_2)
    fusionne = fusionner(gauche, droite)
    return fusionne

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

# je teste
T = [14, 14, 7, 7, 5, 5, 1, 1, 0]
print(fusion(T))    
    





        
    
            

