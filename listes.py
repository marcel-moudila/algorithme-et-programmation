from math import *


# Donne la somme des elements d'une liste d'entiers

def sommeElement(L):
    resultat = 0
    for d in L :
        resultat = resultat + d
    return resultat

# Donne le maximum d'une liste d'entiers

def maximumListe(L):

    resultat = L[0]
    i = 0
    while i < len(L):
        if L[i] >= resultat :
            resultat = L[i]
        i = i + 1
    return resultat



# Recherche un element x dans une liste

def estDansListe(liste,x):

    i = 0
    while i < len(liste):
        if liste[i] == x:
            return True
        i = i + 1
    return False


# Recherche une sous-liste l  dans une liste L

def sousListe(L,l):
    n = len(L)
    m = len(l)
    for i in range(n-m+1) :
        if l[:m] == L[i:i+m]:
            print(i) #affiche l'indice du debut de la sous-liste
            return True
    return False


    



# Supprime un elt et ses occurences                              
def supprimerElement(liste,entier):
    liste1 =[i for i in liste if i!= entier]                                          
    return liste1


# Donne le nbre d'occurence d'un elt                             
def nombreOccu(liste,entier):
    #faisons par une methode sophistiquee
    resultat = len(liste) - len(supprimerElement(liste,entier)) 
    return resultat




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

# Inverse l'ordre des elements

def inverseElement(L):

    Tnew = []
    i = - 1
    while i >= -len(L) :
        Tnew = Tnew + [L[i]]
        i = i - 1
    return Tnew



    
