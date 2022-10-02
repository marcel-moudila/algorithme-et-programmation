print(" ")
print("Exercice 1 ============================================== ")
print(" ")
print("question 1 ============================================== ")
print(" ")
#Début(affiche un tableau de 5 entiers rangés par ordre croissant)
tableau = [i for i in range(5)]
#je teste
print("j'affiche un tableau  : ", end = " ")
print(tableau)
#Fin
print(" ")
print("question 2 ============================================== ")
print(" ")
#Début(donne la liste des éléments d'un tableau)
def elements_tableau(liste):
    for i in range(len(liste)):
        print (liste[i])
    return " "  
#je teste
print("elements_tableau([1,2,0,5,9] est : ")
print(elements_tableau([1,2,0,5,9]))
#Fin
print(" ")
print("question 3 ============================================== ")
print(" ")
#Début (fait la somme des éléments d'un tableau d'entiers)
def somme_element_tab(liste):
    resultat = 0
    for i in range(len(liste)):
        resultat = resultat + liste[i]
        
    return resultat        
#je teste
print("somme_element_tab([1,2,-1]) est :    ",end = " ")
print(somme_element_tab([1,2,-1]))
print("somme_element_tab([0,8,10]) est :    ",end = " ")
print(somme_element_tab([0,8,10]))
#Fin
print(" ")
print("question 4 ============================================== ")
print(" ")
#Début(crée une calculette qui fait des sommes ou produits des éléments)
def produit_element_tab(liste):
    resultat = 1
    for i in range(len(liste)):
        resultat = resultat * liste[i]
    return resultat
def calculette(liste,somme):
    
    if somme:
        print(somme_element_tab(liste))
    else :
        print(produit_element_tab(liste))

    return " "
# je teste 
print ("calculette([1,2,3,9],True) est  :  ", end = " ")
print (calculette([1,2,3,9],True))
print ("calculette([1,2,3,9],False) est  :  ", end = " ")
print (calculette([1,2,3,9],False))
#Fin
print(" ")
print("question 5 ============================================== ")
print(" ")
#Début(donne le nombre de fois un élément est repété dans un tableau)
def nombreOccurence(element,liste):
    compteur = 0
    for elt in liste:
        if elt == element :
            compteur += 1
        else :
            compteur

    return compteur
#je teste
print("nombreOccurence(0,[1,2,3,6,9,-1]) :  ", end = " ")
print(nombreOccurence(0,[1,2,3,6,9,-1]))
print("nombreOccurence(6,[1,2,3,6,9,-1]) :  ", end = " ")
print(nombreOccurence(6,[1,2,3,6,9,-1]))
#Fin
print(" ")
print("Exercice 2 ============================================== ")
print(" ")
#Début(je n'ai pas compris)
print("je n'ai pas compris cet exercice ")
def copie(A,B):
    A = B
    return A
T = [1,3,5,1,2]
S = [1,2,4,1]
T = copie(T,S)
T[2] = 4
S[1] = 2
print(S)
print(T)
#Fin
print(" ")
print("Exercice 3 ============================================== ")
print(" ")
print("question 1 ============================================== ")
print(" ")
#Début(augmente la taille d'un tableau en y ajoutant un élément indexé)
def ajout(liste,indice,element):
    if indice > (len(liste) - 1):
        return False
    if (indice > 0) and (indice < len(liste)-1) :
        liste1 = [element]
        liste2 = liste[0:indice]
        liste3 = liste[indice:len(liste)]
        return (liste2 + liste1) + liste3
    if indice == 0 :
        liste4 = [element]
        return liste4 + liste
    if indice == (len(liste)-1):
        liste5 = [element]
        return liste + liste5
#je teste    
print("ajout([1,2,3,4,5],0,banane) :      ", end = " ")
print(ajout([1,2,3,4,5],0,"banane"))
print("ajout([1,2,3,4,5],2,banane) :      ", end = " ")
print(ajout([1,2,3,4,5],2,"banane"))
print("ajout([1,2,3,4,5],7,banane) :      ", end = " ")
print(ajout([1,2,3,4,5],7,"banane"))
#Fin
print(" ")
print("question 2 ============================================== ")
print(" ")
#Début(dis si un élément figure dans un tableau)
def estDans(liste,entier):
    if entier in liste: 
        return True 
    else :
        return False        
#je teste
print ("estDans([1,2,3,4,5],5) :     ",end = " ")
print (estDans([1,2,3,4,5],5))
print ("estDans([1,2,3,4,5],10) :     ",end = " ")
print (estDans([1,2,3,4,5],10))
#Fin
print(" ")
print("question 3 ============================================== ")
print(" ")
#Début(donne un tableau sans occurence d'un de ses éléments)
def supprimerC(liste,element) :
    
    liste1 = [i for i in liste if i!= element]
    return liste1
   
#je teste
print("supprimerC([0,2,9,3,6,2,5,6,2,9,2],2) est :  ", end = " ")
print(supprimerC([0,2,9,3,6,2,5,6,2,9,2],2))
print("supprimerC([0,2,9,3,6,2,5,6,2,9,2],100) est :  ", end = " ")
print(supprimerC([0,2,9,3,6,2,5,6,2,9,2],100))















    

    
