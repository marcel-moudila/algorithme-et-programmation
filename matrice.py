#teste si une liste represente une matrice 
def estMatrice(liste):
    i = 0
    while i < len(liste) - 1 and len(liste[i]) == len(liste[i+1]):
        i = i + 1
    if i == len(liste) -1 :
        return True
    else :
        return False

'''===================================================='''

# donne le nombre de ligne d'une matrice
def nbLigne(liste):
    if estMatrice(liste):
        return len(liste)
    else:
        return "n'est pas une matrice"


'''===================================================='''

#donne le nombre de colonne d'une matrice
def nbColonne(liste):
    if estMatrice(liste):
        return len(liste[0])
    else :
        return "n'est pas une matrice"

'''===================================================='''

#teste si une matrice est carre
def MatriceCarree(liste):
    if nbLigne(liste) == nbColonne(liste):
        return True
    else:
        return False

'''===================================================='''

#teste si une matrice carre est triangulaire inferieur(que des 0 au dessus de diag)
def triangulaireInf(liste):
    test = MatriceCarree(liste)
    if not test:
        return "n'est pas une matrice carree"
    else :
        i = 0
        while i < len(liste)-1:
            j = i + 1
            while j < len(liste):
                if liste[i][j] != 0:
                    return False
                j = j+1
            i = i+1
        return True


'''===================================================='''

#teste si une matrice carre est triangulaire sup(que des 0 au dessous de diag)
def triangulaireSup(liste):
    test = MatriceCarree(liste)
    if not test:
        return "n'est pas une matrice carree"
    else :
        i = 1
        while i < len(liste):
            j = 0
            while j < i :
                if liste[i][j] != 0 :
                    return False
                j = j + 1
            i = i + 1
        return True 


'''===================================================='''

#affiche joliment une matrice
def afficheMatrice(liste) : 
    test = estMatrice(liste)
    if not test:
        return "n'est pas une matrice "
    else :
        n = nbLigne(liste)
        m = nbColonne(liste)
        for i in range(0, n):
            for j in range(0, m) :
                print (liste[i][j],end= " ")
            print(" ")
        return " "


'''===================================================='''

#fait la somme de la matrice A avec la matrice B
def additionMatrice(A,B):
    test1 = estMatrice(A)
    test2 = estMatrice(B)
    if test1 and test2 :
        if (nbLigne(A) == nbLigne(B)) and (nbColonne(A) == nbColonne(B)):
            Tnew = []
            for i in range(0,nbLigne(A)):
                ligne = [A[i][j] + B[i][j] for j in range(nbColonne(A))]
                Tnew = Tnew + [ligne]
            return Tnew
        else :
            return - 1


'''===================================================='''

#fait le produit d'une matrice avec un scalaire
def MatriceProduitScalaire(liste,scalaire):
    if estMatrice(liste):
        Tnew = []
        for i in range(nbLigne(liste)):
            ligne = [scalaire * liste[i][j] for j in range(nbColonne(liste))]
            Tnew = Tnew + [ligne]
        return afficheMatrice(Tnew)



'''===================================================='''

#donne la j-eme colonne d'une matrice
def Colonne(A,j):
    n = len(A)
    colonne = [A[i][j] for i in range(n)]
    return colonne


'''===================================================='''

#donne la i-eme ligne d'une matrice 
def Ligne(A,i):
    ligne = A[i]
    return ligne

'''===================================================='''

#donne le produit termes à termes d'une ligne et d'une colonne de meme taille
def prodTableau(L, C):
    res = 0
    for i in range(len(L)):
        res += L[i]*C[i]
    return res

'''===================================================='''

#donne le produit matriciel de la matrice carre A avec la matrice carre B
def prodMatrice(A, B):
    Tnew = []
    for i in range(len(A)):
        ligne = [prodTableau(Ligne(A,i), Colonne(B,j))  for j in range(len(B))]
        Tnew = Tnew + [ligne]
    return Tnew


'''===================================================='''

    

A = [[6,3,5],[2,1,5],[-1,3,0]]

V = [[3,1,5]]

W = [[1],[3],[5]]

L = [[1,3,5],[0,1,5],[0,0,1]]

U = [[1,0,0],[2,1,0],[0,1,0]]

print(triangulaireSup(A))
print(triangulaireSup(V))
print(triangulaireSup(W))
print(triangulaireSup(L))
print(triangulaireSup(U))

    
            





        
    
