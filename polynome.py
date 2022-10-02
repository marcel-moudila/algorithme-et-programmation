from math import *
from random import *

# affiche un polynome

def affiche_Poly(Tp):

    resultat = str(Tp[0])
    for j in range (1,len(Tp)):
        if Tp[j] > 0 :
            resultat = resultat + " + " + str(Tp[j]) + "*X^" + str(j)
        if Tp[j] < 0 :
            resultat = resultat + " " + str(Tp[j]) + "*X^" + str(j)
        if Tp[j] == 0 :
            resultat = resultat
    return resultat

print(affiche_Poly([0,1,3,0,0,0,0,0,12,0,0,0,-8,0,0,0]))
        
            

print("==========================================")

def monome(a,n):

    '''
        - entree : un reel a, et un entier n
        - sortie : le monome a*X**n
    '''

    if n == 0 :
        return [a]
    if n == 1 :
        return [0,a]
    if n > 1 :
        return [0]*n + [a]


#je teste la fonction monome
def testMonome(a,n):
    print("monome(",a,",",n,") = ",monome(a,n))
    return ""

print(testMonome(1,0))
print(testMonome(1,1))
print(testMonome(1,5))


print("==========================================")

def estNul(Tp):
    '''
        - entree : un polynome Tp
        - sortie : un booleen (True si Tp est le polynome nul, Fasle sinon
    '''
    i = 0
    while i < len(Tp):
        if Tp[i] != 0 :
            return False
        i = i + 1
    return True

#je teste la fonction estNul
def testEstNul (Tp):
    print("estNul(",Tp,") = ",estNul(Tp))
    return ""

print(testEstNul([1,2,3]))
print(testEstNul([0,0,0]))
print(testEstNul([0]))


print("==========================================")



def derive(Tp):

    ''' entree : un polynome Tp
sortie : le polynome derive de Tp '''
    
    n = len(Tp)
    Tpnew = [i*Tp[i] for i in range(n)]
    return Tpnew[1:]

#je teste la fonction derivee
def testDerive(Tp):
    print("derive(",Tp,") = ",derive(Tp))
    return ""

print(testDerive([1,1,1]))
print(testDerive([1,0,1]))
print(testDerive([0,1,1]))


print("==========================================")



def evaluer(Tp,r):

    ''' entree : un polynome Tp et un reel r
sortie : le reel resultat de l'evaluation de Tp en r '''
    somme = 0
    for i in range(0,len(Tp)):
        somme = somme + (Tp[i])*(r**i)
    return somme

#je teste la fonction evaluer
def testEvaluer(Tp,r):
    print("evaluer(",Tp,",",r,") = ",evaluer(Tp,r))
    return ""

print(testEvaluer([1,1,1],2))
print(testEvaluer([1,1,1],-2))
print(testEvaluer([1,1,1],0))


print("==========================================")


def remplissage(Tp,n) :

    ''' entree : un polynome Tp et un entier positf n strictement plus grand que la taille de Tp
sortie : le polynome Tp de taille n '''
    
    m = len(Tp)
    return Tp + [0]*(n-m)

#je teste la fonction remplissage
def testRemplissage(Tp,n):
    print("remplissage(",Tp,",",n,") : ",remplissage(Tp,n))
    return ""


print(testRemplissage([1,2,3,4],7))
print(testRemplissage([1,2,0,4],5))

print("==========================================")

def sommePoly(Tp,Tq):
    
    ''' entree: deux polynomes Tp et Tq
sortie : la somme polynomiale Tp + Tq '''
    
    n = len(Tp)
    m = len(Tq)
    if n < m :
        TpModifie = remplissage(Tp,m)
        Tnew = [TpModifie[i] + Tq[i] for i in range(m)]
        return Tnew
    else :
        TqModifie = remplissage(Tq,n)
        Tnew = [TqModifie[i] + Tp[i] for i in range(n)]
        return Tnew

#je teste la fonction sommePoly
def testSommePoly(Tp,Tq):
    print("sommePoly(",Tp,",",Tq,") = ",sommePoly(Tp,Tq))
    return ""


print(testSommePoly([1,0,2,-1],[0,3,5,2,2]))
print(testSommePoly([0,0,2,-1,3,0,0,0],[0,3,5,2,2,1,1]))


print("==========================================")

def produitScal(Tp,r):
    
    ''' entree: un polynome Tp et un reel r (ou polynome constant ou scalaire)
sortie : le produit polynomiale de Tp avec un scalaire '''
    
    n = len(Tp)
    Tnew = [r*Tp[i] for i in range(n)]
    return Tnew

#je teste la fonction produitScal
def testProduitScal(Tp,r):
    print("produitScal(",Tp,",",r,") = ",produitScal(Tp,r))
    return ""

print(testProduitScal([1,0,2,-1],2))
print(testProduitScal([0,3,5,2,2,1,1],-1))


print("==========================================")

def produitMonome(Tp,a,d):
    
    ''' entree: un polynome Tp quelconque  et un monome de coefficient a et de degre d
sortie : le produit polynomiale de Tp avec le monome '''

    resultat = [0]*d + [a * Tp[i - d] for i in range(d,len(Tp)+d)]
    return resultat


#je teste la fonction produitMonome
def testProduitMonome(Tp,a,d):
    print("produitMonome(",Tp,",",a,",",d,") = ",produitMonome(Tp,a,d))
    return ""

print(testProduitMonome([1,1,1,1],1,2))
print(testProduitMonome([1,1,1,1],1,0))
print(testProduitMonome([1,1,1,1],2,1))


print("==========================================")

def produitPoly(Tp,Tq):

    ''' entree : deux polynomes Tp et Tq
sortie : le produit polynomiale de Tp avec Tq '''

    resultat = [0]
    for i in range(len(Tq)):
        resultat = sommePoly(resultat,produitMonome(Tp,Tq[i],i))
    return resultat

#je teste la fonction produitPoly
def testProduitPoly(Tp,Tq):
    print("produitPoly(",Tp,",",Tq,") = ",produitPoly(Tp,Tq))
    return ""


print(testProduitPoly([1,0,2,3],[0,2,4]))
print(testProduitPoly([1,-1],[1,1]))
print(testProduitPoly([1,1],[1,1]))


print("==========================================")

def puissancePoly(Tp,n):

    '''
        - entree : un polynome Tp et un entier n
        - sortie : le polynome Tp**n
    '''

    if n == 0:
        return [1]
    if n == 1 :
        return Tp
    if n >= 2 :
        resultat = [1]
        for i in range (n):
            resultat = produitPoly(Tp,resultat)
        return resultat

#je teste la fonction puissancePoly
def testPuissancePoly(Tp,n):
    print("Tp = ", Tp)
    print("n = ",n)
    print("puissancePoly(Tp,n) = ",puissancePoly(Tp,n))
    return ""

print(testPuissancePoly([1,1],0))
print(testPuissancePoly([1,1],1))
print(testPuissancePoly([1,1],2))
print(testPuissancePoly([1,1],3))


print("==========================================")

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


print(testDegre([1,2,0,5,0,0]))
print(testDegre([1,2,0,5]))


print("==========================================")

def primitive(Tp):

    '''
        - entree : un polynome Tp
        - sortie : la primitive de Tp qui s'annule en 0
    '''

    resultat = [0] + [Tp[i]/(i+1) for i in range(degre(Tp)+1)]

    return resultat

print(primitive([1,1]))

print("==========================================")

def egale(Tp,Tq):

    ''' entree : deux tableaux de polynomes
sortie : le booleen True si les deux tableaux representent le meme polynome, False sinon '''

    #deux polynomes sont egaux s'ils ont meme degre et les coefficients des monomes sont egaux

    if degre(Tp) == degre(Tq):
        for i in range(degre(Tp) + 1):
            if Tp[i] != Tq[i] :
                return False
        return True
    if degre(Tp) != degre(Tq):
        return False

#je teste la fonction egale
def testEgale(Tp,Tq):
    print("egale(",Tp,",",Tq,") : ",egale(Tp,Tq))
    return ""

print(testEgale([1,2,3],[1,2,3]))
print(testEgale([1,2,3],[1,2,3,0]))
print(testEgale([1,2,3],[1,2,0,3]))
print(testEgale([1,2,3,0],[1,2,3]))


print("==========================================")

def restePoly(Tp,Tq):

    '''
        - entree : un polynome quelconque Tp et un polynome non nul Tq
        - sortie : le reste de la division euclidienne de Tp par Tq
    '''

    if degre(Tp) < degre(Tq):
        reste = Tp
        return reste
    else :
        if Tp == Tq :
            reste = [0]
            return reste
        else:
            while degre(Tp) >= degre(Tq):
                d = degre(Tp) - degre(Tq)
                n = degre(Tp)
                m = degre(Tq)
                poly1 = produitMonome(Tq,-1*Tp[n]/Tq[m],d)
                reste = sommePoly(Tp,poly1)
                Tp = reste
            return reste

def divisionPoly(Tp,Tq):

    '''
        - entree : un polynome quelconque Tp et un polynome non nul Tq
        - sortie : le quotient de la division euclidienne de Tp par Tq
    '''

    if degre(Tp) < degre(Tq):
        quotient = [0]
        return quotient
    else :
        if Tp == Tq :
            quotient = [1]
            return quotient
        else:
            quotient = []
            while degre(Tp) >= degre(Tq):
                d = degre(Tp) - degre(Tq)
                n = degre(Tp)
                m = degre(Tq)
                quotient = [Tp[n]/Tq[m]] + quotient
                poly1 = produitMonome(Tq,-1*Tp[n]/Tq[m],d)
                reste = sommePoly(Tp,poly1)
                Tp = reste
    
            return quotient


def testDivision(Tp,Tq):
    print("Tp = ",Tp)
    print("Tq = ",Tq)
    print("divisionPoly(Tp,Tq) = ",divisionPoly(Tp,Tq))
    print("restePoly(Tp,Tq) = ",restePoly(Tp,Tq))
    return ""

print(testDivision([-4,3,0,2],[1,1]))
print(testDivision([1,1],[-4,3,0,2]))
print(testDivision([-4,3,0,2],[-4,3,0,2]))
print(testDivision([-4,3,0,1],[-4,3,0,2]))


def divisionTest(P,Q):

    ''' on teste si P = Q*D + R '''

    D = divisionPoly(P,Q)
    R = restePoly(P,Q)
    print(P," = ",Q," * ",D," + ",R," : ",egale(P,sommePoly(R,produitPoly(Q,D))))
    return ""


#je teste

print()
print(divisionTest([-4,3,0,2],[1,1]))
print(divisionTest([1,1],[-4,3,0,2]))
print(divisionTest([-4,3,0,2],[-4,3,0,2]))
print(divisionTest([-4,3,0,1],[-4,3,0,2]))







    
    


    
