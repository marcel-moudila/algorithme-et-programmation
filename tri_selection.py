# Supprime un elt et ses occurences                              
def supprimerElement(liste,entier):
    liste1 =[i for i in liste if i!= entier]                                          
    return liste1


# Donne le nbre d'occurence d'un elt                             
def nombreOccu(liste,entier):
    #faisons par une methode sophistiquee
    resultat = len(liste) - len(supprimerElement(liste,entier)) 
    return resultat


def triParSelection(liste):
    Tnew = []
    while len(liste) > 0:
        valeurMax = max(liste)
        Tnew = [valeurMax]*nombreOccu(liste,valeurMax) + Tnew
        liste = supprimerElement(liste,valeurMax)
    return  Tnew

#je teste
T1 = [7, 8, 3, 1, 15,9, 2, 4, 15, 11,1,3]
T2 = [-1,0,2,4,8,2,-10,9]
T3 = [0,5,-6,2,-3,-6,10]
print("T1 =",T1)
print("triParSelection(T1) = ",triParSelection(T1))

print()

print("T2 =",T2)
print("triParSelection(T2) = ",triParSelection(T2))

print ()

print("T3 =",T3)
print("triParSelection(T3) = ",triParSelection(T3))
