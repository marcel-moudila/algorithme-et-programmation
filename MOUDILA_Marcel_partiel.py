print("=========== Exercice 2 ===============")

print("======== question 1 =========")

def degre(Tp):

    ''' entree : un polynome Tp
sortie : le degre de Tp '''
    
    n = len(Tp)
    i = -1
    while Tp[i] ==0 :
        i = i - 1
    return i + n

#je teste la fonction degre
def testDegre(Tp):
    print("degre(",Tp,") = ",degre(Tp))
    return ""


print(testDegre([1,0,0,1,0,0]))
print(testDegre([3,-1,4,0,0,19]))


print("======== question 2 =========")


def remplissage(Tp,n) :

    ''' entree : un polynome Tp et un entier positf n strictement plus grand que la taille de Tp
sortie : le polynome Tp de taille n '''
    
    m = len(Tp)
    return Tp + [0]*(n-m)


def sommePoly(Tp,Tq):
    
    ''' entree: deux polynomes Tp et Tq
sortie : la somme polynomiale Tp + Tq '''
    
    n = len(Tp)
    m = len(Tq)
    if n < m :
        TpModifie = remplissage(Tp,m)
        Tnew = [TpModifie[i] + Tq[i] for i in range(m)]
        return Tnew
    if m < n :
        TqModifie = remplissage(Tq,n)
        Tnew = [TqModifie[i] + Tp[i] for i in range(n)]
        return Tnew

#je teste la fonction sommePoly
def testSommePoly(Tp,Tq):
    print("sommePoly(",Tp,",",Tq,") = ",sommePoly(Tp,Tq))
    return ""


print(testSommePoly([1,0,2,-1],[0,3,5,2,2]))
print(testSommePoly([0,0,2,-1,3,0,0,0],[0,3,5,2,2,1,1]))


print("======== question 3 =========")


def estPositif(Tp):

    ''' entree : un tableau de polynome
sortie : un booleen (True si tous les coefficients de Tp sont positifs )'''

    n = len(Tp)
    for i in range(n) :
        if Tp[i] < 0 :
            return False
    return True

#je teste la fonction estPositif
def testEstPositif(Tp):
    print("estPositif(",Tp,") : ",estPositif(Tp))
    return ""

print(testEstPositif([1,0,2,3]))
print(testEstPositif([1,0,-2,3]))
print(testEstPositif([-1,0,2,3,0]))
print(testEstPositif([1,0,2,3,0]))





print("=========== Exercice 1 ===============")

print("======== question 1 =========")

def nombreOccu(L,n):
    
    ''' entree : une liste L et un entier n
sortie : le nombre d'occurence de n dans L '''
    
    resultat = 0
    i = 0
    while i < len(L) :
        if L[i] == n :
            resultat = resultat + 1
        i = i + 1
    return resultat

def triPivotAux(T,n):

    ''' entree : un tableau T et un entier n
sortie : un tableau T1 obtenue  a partir de T selon les indications de l'exercice '''

    

    liste1 = [i for i in T if i < n ]
    liste2 = [n]*nombreOccu(T,n)
    liste3 = [i for i in T if i > n]

    return liste1 + liste2 + liste3


#je teste
def testTriPivotAux(T,n):
    print("triPivotAux(",T,",",n,") = ",triPivotAux(T,n))
    return ""

print(testTriPivotAux([1,5,2,9,3,0,-1],2))
print(testTriPivotAux([1,2,3,5,2,9,3,2,0,-1],3))


print("======== question 2 =========")

def estTrie(T):
    ''' - entree : un tableau T
        - sortie : un booleen True si T est trie en ordre croissant
    '''
    i = 0
    while (i < len(T) - 1 and T[i] <= T[i+1]):
        i = i + 1
    if i == len(T) - 1 :
        return True
    else :
        return False


def Trie(T):
    '''
        - entree : un tableau d'entiers T
        - sortie : un tableau T trie par echange
    '''
    while not estTrie(T):
        i = 0
        while i < len(T) - 1 :
            if T[i] >= T[i+1]:
                tmp = T[i]
                T[i] = T[i+1]
                T[i+1] = tmp
            i = i + 1
    return T

def trirapide(T):

    

        liste = triPivotAux(T,T[0])
        TG = [k for k in liste if k < T[0]]
        TD = [k for k in liste if k > T[0]]

        tab1 = Trie(TG)
        tab2 = Trie(TD)
        resultat = tab1 + [T[0]]*nombreOccu(T,T[0]) + tab2

        return resultat

#je teste

T = [1,5,2,9,3,0,-1]
print("T = ",T)
print("trirapide(T) = ",trirapide(T))


print("=========== Exercice 3 ===============")

print("======== question 1 =========")

def nombreOcc(M,n) :

    ''' entree : une matrice M et un entier n
sortie : le nombre d'occurence de n dans M '''

    resultat = 0 
    i = 0
    while i < len(M) :
        resultat = resultat + nombreOccu(M[i],n) #ici nombreOccu est celui defini plus haut
        i = i +1
    return resultat

#je teste la fonction nombreOcc
def testNombreOcc(M,n):
    print("nombreOcc(",M,",",n,") = ",nombreOcc(M,n))
    return ""

print(testNombreOcc([[1,2,3],[0,0,0],[3,4,5]],0))
print(testNombreOcc([[1,2,3],[0,0,0],[3,4,5]],1))
print(testNombreOcc([[1,2,3],[0,0,0],[3,4,5]],3))


print("======== question 2 =========")

def estDansPos(M,N,l,c):

    ''' entree : une matrice M, une matrice N (nombre de ligne et de colonne strictement plus petit que celui de M)
                 un entier l strictement plus que le nombre de ligne de M , un entier c strictement plus petit que le nombre de colonne de M
        sortie : un booleen (True selon les indications de l'enonce ) '''

    if M[l][c:c+2] != N[0][0]:
        return False
    

    

    


    








