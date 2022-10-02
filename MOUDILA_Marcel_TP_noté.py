print()
print("=================== exercice 1 =======================================")
print()


A = [[6,3,5],[2,1,5],[-1,3,0]]

V = [[3,1,5]]

W = [[1],[3],[5]]

L = [[1,3,5],[0,1,5],[0,0,1]]

U = [[1,0,0],[2,1,0],[0,1,0]]

#je teste

print("A = ",A)
print("V = ",V)
print("W = ",W)
print("L = ",L)
print("U = ",U)

print()
print("=================== question 1 de l'exo 2 ============================")
print()


def estMatrice(liste):

    '''
        entree : une liste dont les elements sont eux-memes des listes d'entiers
        sortie : un booleen (True si l'entree est une matrice, False sinon)
    '''
    
    i = 0
    while i < len(liste) - 1:
        if len(liste[i]) != len(liste[i+1]): #liste est une matrice si chaque liste[i] a meme taille
            return False
        i = i + 1
    return True

#je teste

B = [[1,2],[3]]

print("B = ",B)
print("A = ",A)
print("V = ",V)
print("W = ",W)
print("L = ",L)
print("U = ",U)

print()

print("estMatrice(B) = ",estMatrice(B))
print("estMatrice(A) = ",estMatrice(A))
print("estMatrice(V) = ",estMatrice(V))
print("estMatrice(W) = ",estMatrice(W))
print("estMatrice(L) = ",estMatrice(L))
print("estMatrice(U) = ",estMatrice(U))




print()
print("=================== question 2 de l'exo 2 ============================")
print()


def nbLigne(liste):

    '''
        entree : une matrice
        sortie : son nombre de ligne
    '''
    return len(liste) 
    
def nbColonne(liste):

    '''
        entree : une matrice
        sortie : son nombre de colonne 
    '''
    return len(liste[0]) #ou len(liste[i]) avec i quelqonque entre (0) et (taille de liste - 1)
    

# je teste

def testNbLigne(liste):
    print("nbLigne(",liste,") = ",nbLigne(liste))
    return ""

print(testNbLigne(A))
print(testNbLigne(V))
print(testNbLigne(W))
print(testNbLigne(L))
print(testNbLigne(U))


print()
print("================")
print()

def testNbColonne(liste):
    print("nbColonne(",liste,") = ",nbColonne(liste))
    return ""

print(testNbColonne(A))
print(testNbColonne(V))
print(testNbColonne(W))
print(testNbColonne(L))
print(testNbColonne(U))

print()
print("=================== question 3 de l'exo 2 ============================")
print()

def triangulaireInf(liste):

    '''
        entree : une matrice carree
        sortie : un booleen (True cette matrice est triangulaire inferieure, False sinon)
    '''
    
    i = 0
    while i < len(liste)-1:
        j = i + 1
        while j < len(liste):
            if liste[i][j] != 0:
                return False
            j = j+1
        i = i+1
    return True


def triangulaireSup(liste):

    '''
        entree : une matrice carre
        sortie : un booleen (True cette matrice est triangulaire superieure, False sinon)
    '''
    i = 1
    while i < len(liste):
        j = 0
        while j < i :
            if liste[i][j] != 0 :
                return False
            j = j + 1
        i = i + 1
    return True

#je teste

print("A = ",A)
print("L = ",L)
print("U = ",U)

print()

print("triangulaireInf(A) = ",triangulaireInf(A))
print("triangulaireInf(L) = ",triangulaireInf(L))
print("triangulaireInf(U) = ",triangulaireInf(U))


print()
print("=================")
print()

print("triangulaireSup(A) = ",triangulaireSup(A))
print("triangulaireSup(L) = ",triangulaireSup(L))
print("triangulaireSup(U) = ",triangulaireSup(U))




print()
print("=================== question 4 de l'exo 2 ============================")
print()

def afficheMatrice(liste) :

    '''
        entree : une matrice 
        sortie : la matrice affichee joliment
    '''
    n = nbLigne(liste)
    m = nbColonne(liste)
    for i in range(n):
        for j in range(m) :
            print (liste[i][j],end= " ")
        print(" ")
    return " "

#je teste

def testAfficheMatrice(liste):
    print("afficheMatrice(",liste,") est :")
    print(afficheMatrice(liste))
    return ""

print(testAfficheMatrice(A))
print(testAfficheMatrice(V))
print(testAfficheMatrice(W))
print(testAfficheMatrice(L))
print(testAfficheMatrice(U))




print()
print("=================== question 1 de l'exo 3 ============================")
print()


def additionMatrice(A,B):

    '''
        entree : deux matrices A et B 
        sortie : leur somme A+B, ou -1 si la somme n'est pas possible
    '''
    
    if nbLigne(A) == nbLigne(B) and nbColonne(A) == nbColonne(B):
        Tnew = []
        for i in range(nbLigne(A)):
            ligne = [A[i][j] + B[i][j] for j in range(nbColonne(A))]
            Tnew = Tnew + [ligne]
        return Tnew
    else :
        return - 1

#je teste

print("A = ",A)
print("V = ",V)
print("W = ",W)
print("L = ",L)
print("U = ",U)

print()

print("additionMatrice(A,V) = ",  additionMatrice(A,V))
print("additionMatrice(A,W) = ",  additionMatrice(A,W))
print("additionMatrice(A,L) = ",  additionMatrice(A,L))
print("additionMatrice(A,U) = ",  additionMatrice(A,U))



print()
print("=================== question 2 de l'exo 3 ============================")
print()

def MatriceProduitScalaire(matrice,scalaire):

    '''
        entree : une matrice et un scalaire reel
        sortie : leur produit
    '''
    
    Tnew = []
    for i in range(nbLigne(matrice)):
        ligne = [scalaire * matrice[i][j] for j in range(nbColonne(matrice))]
        Tnew = Tnew + [ligne]
    return Tnew

print("A = ",A)
print("V = ",V)
print("W = ",W)
print("L = ",L)
print("U = ",U)

print()

print("MatriceProduitScalaire(A,3) = ", MatriceProduitScalaire(A,3))
print("MatriceProduitScalaire(V,3) = ", MatriceProduitScalaire(V,3))
print("MatriceProduitScalaire(W,3) = ", MatriceProduitScalaire(W,3))
print("MatriceProduitScalaire(L,3) = ", MatriceProduitScalaire(L,3))



print()
print("=================== question 3 de l'exo 3 ============================")
print()


def sommeElementTableau(liste): #fonction auxilliaire : entree (une liste d'entiers), sortie (la somme des elements)
    somme = 0
    for i in range(len(liste)):
        somme = somme + liste[i]
    return somme



def MatriceProduitVecteur(vecteur,matrice):#vecteur est vecteur ligne

    '''
        entree : une matrice de taille n*m et un vecteur de taille 1*n
        sortie : le produit de l'un et l'autre, ou - 1 si c'est pas possible
    '''
    if nbColonne(vecteur) != nbLigne(matrice):
        return -1
    Tnew = []
    for j in range(nbColonne(matrice)):
        tableau = [vecteur[0][k] * matrice[k][j] for k in range(nbLigne(matrice))] # tableau des produits terme a terme du vecteur avec la j-eme colonne de la matrice
        Tnew = Tnew + [sommeElementTableau(tableau)] #obtention des Tnew[0][j] et leur concatenation donne Tnew[0]
    return [Tnew]
        
                                       
#je teste

print("A = ",A)
print("V = ",V)
print("W = ",W)

print()

print("MatriceProduitVecteur(V,A) = ",  MatriceProduitVecteur(V,A))
print("MatriceProduitVecteur(V,W) = ",  MatriceProduitVecteur(V,W))
print("MatriceProduitVecteur(V,V) = ",  MatriceProduitVecteur(V,V))



print()
print("=================== question 4 de l'exo 3 ============================")
print()


def ProduitMatrice(A,B):

    '''
        entree : une matrice  A de taille n*m et une matrice B de taille m*k
        sortie : le produit de l'un et l'autre, ou -1 si c'est pas possible 
    '''
    
    if nbColonne(A) != nbLigne(B):
        return -1
    if nbColonne(A) == nbLigne(B):
        Tnew = []
        for i in range(nbLigne(A)):
            Tnew = Tnew + MatriceProduitVecteur([A[i]],B) # produit des vecteurs lignes i de A avec la matrice B, puis la concatenation donne le resultat
        return Tnew
            
#je teste
    
print("A = ",A)
print("V = ",V)
print("W = ",W)
print("L = ",L)

print()

print("ProduitMatrice(A,V) = ", ProduitMatrice(A,V))
print("ProduitMatrice(A,W) = ", ProduitMatrice(A,W))
print("ProduitMatrice(A,L) = ", ProduitMatrice(A,L))
print("ProduitMatrice(V,W) = ", ProduitMatrice(V,W))



print()
print("=================== question 5 de l'exo 3 ============================")
print()

def transposeeVecteur(vecteur):

    '''
        entree : un vecteur (colonne ou ligne)
        sortie : la transposee de ce vecteur
    '''
    if len(vecteur) == 1 : #vecteur ligne
        transposee = [[k] for k in vecteur[0]] #creons une liste de  [vecteur[0][k]] et la transposee est cree
        return transposee
    if nbColonne(vecteur) == 1 : #vecteur colonne
        Tnew = []
        for i in range(len(vecteur)):
            Tnew = Tnew + vecteur[i]
            tableau = [Tnew] #n'oublions pas de mettre Tnew dans un tableau
        transposee = tableau # la transposee est cree
        return transposee

#je teste

print("V = ",V)
print("W = ",W)

print()

print("transposeeVecteur(V) = ",transposeeVecteur(V))
print("transposeeVecteur(W) = ",transposeeVecteur(W))



print()
print("=================== question 1 de l'exo 4 ============================")
print()


def determinantM2x2(matrice):

    '''
        entree : une matrice de taille 2*2
        sortie : son determinant
    '''
    return matrice[0][0]*matrice[1][1] - matrice[0][1]*matrice[1][0]


#je teste

I = [[1,0],[0,1]]
P = [[1,2],[3,4]]
O = [[0,0],[0,0]]

print("I = ",I)
print("P = ",P)
print("O = ",O)

print()

print("determinantM2x2(I) = ", determinantM2x2(I))
print("determinantM2x2(P) = ", determinantM2x2(P))
print("determinantM2x2(O) = ", determinantM2x2(O))


print()
print("=================== question 2 de l'exo 4 ============================")
print()

def sousMatrice(matrice, i,j):

    '''
        entree : une matrice nxm, un entier i < n, un entier j < m
        sortie : une matrice (n-1)x(m-1) sans la ligne i et sans la colonne j 
    '''
    Tnew = []

    #je recupere toutes les lignes de matrice sauf la ligne d'index i
    if i == 0:
        M = matrice[1:] 
    else :
        M = matrice[0:i] + matrice[i+1:] #je recupere toutes les lignes de matrice sauf la ligne d'index i

    #apres supression de la ligne d'index i, je supprime la colonne d'index j de ma nouvelle matrice    
    if j == 0 :
        Tnew = [ M[s][1:] for s in range(len(M))]
    else:
        Tnew = [ M[s][0:j] + M[s][j+1:] for s in range(len(M)) ]        
    return Tnew
    
        
#je teste

print("A = ",A)

print()

print("sousMatrice(A,0,0) = ",sousMatrice(A,0,0))
print("sousMatrice(A,0,1) = ",sousMatrice(A,0,1))
print("sousMatrice(A,1,0) = ",sousMatrice(A,1,0))
print("sousMatrice(A,2,2) = ",sousMatrice(A,2,2))


print()
print("=================== question 3 de l'exo 4 ============================")
print()


def determinant(matrice):
    
    '''
        entree : une matrice carre
        sortie : le determinant de cette matrice carre
    '''
    if nbLigne(matrice) == 2 and nbColonne(matrice) == 2:
        
        return determinantM2x2(matrice)
    
    #developpons suivant la ligne d'index 0 (c'est un choix)
    
    resultat = 0
    M = [sousMatrice(matrice, 0,k) for k in range(nbColonne(matrice))] #tableau des sous-matrices

    j = 0
    while j < nbColonne(matrice):
        resultat = resultat + (-1)**(j)* matrice[0][j] * determinant(M[j])
        j = j + 1
    return resultat

    
#je teste

print("A = ",A)
print("L = ",L)
print("U = ",U)

print()

print("determinant(A) = ",determinant(A))
print("determinant(L) = ",determinant(L))
print("determinant(U) = ",determinant(U))
            
            
            
                           
                           
                           

    
    




        

