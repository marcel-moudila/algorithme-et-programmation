print(" ============= (tri par insertion) ====================== ")

# Inserre un elt à l'index voulu                                
def insererListe(liste,entier,index):
    if index > len(liste):
        return " pas possible "
    
    else: 
        liste1 = liste[0:index]
        liste2 = liste[index:]
        liste3 = liste1 + [entier] + liste2
        return liste3

# Inserre un elt dans une liste triée en croissant              
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

# Donne l'index de la premiere occurrence d'un elt              
def premiereOccu(liste,entier):
    if entier not in liste :
        return "n'est pas dans la liste"
    else:
        i = 0
        while liste[i] != entier:
            i = i +1
        return i

    
# Supprime la premiere occurence d'un elt                       
def supprimerPremiereOccu(liste,entier):
    n = premiereOccu(liste,entier)
    if n == 0:
        return liste[1:]
    else :
        return liste[0:n] + liste[n+1:]

    
def triParInsertion(liste):
    Tnew = []
    i = 0
    while len(liste) > 0:
        entier = liste[i]
        Tnew = insererDansListeTrie(Tnew,entier) #inserre et trie par ordre croissant
        liste = supprimerPremiereOccu(liste,entier)  
        i = 0
    return Tnew
    
# je teste
T1 = [7, 8, 3, 1, 9, 2, 4, 15, 11,1,3]
T2 = [-1,0,-2,4,8,2,-10,9]
T3 = [0,5,-6,2,-3,-6,10]
print("T1 =",T1)
print("triParInsertion(T1) = ",triParInsertion(T1))

print()

print("T2 =",T2)
print("triParInsertion(T2) = ",triParInsertion(T2))

print ()

print("T3 =",T3)
print("triParInsertion(T3) = ",triParInsertion(T3))

