from math import *

#fait la somme de deux nombres complexes          
def sommeComplexe(Z1,Z2):
    resultat = [Z1[0] + Z2[0],Z1[1] + Z2[1]]
    return resultat

def testSommeComplexe(Z1,Z2):
    print("Z1 = ", Z1)
    print("Z2 = ", Z2)
    print("sommeComplexe(Z1,Z2) = ", sommeComplexe(Z1,Z2))
    return ""

print(testSommeComplexe([1,1],[1,-1]))
print(testSommeComplexe([1,1],[0,0]))
print(testSommeComplexe([1,0],[0,1]))


print("==================================================")


#fait le produit de deux nombres complexes
def produitComplexe(Z1,Z2):
    a = Z1[0]
    b = Z1[1]
    c = Z2[0]
    d = Z2[1]
    resultat = [a*c - b*d, a*d + b*c]
    return resultat


def testProduitComplexe(Z1,Z2):
    print("Z1 = ", Z1)
    print("Z2 = ", Z2)
    print("produitComplexe(Z1,Z2) = ", produitComplexe(Z1,Z2))
    return ""

print(testProduitComplexe([1,1],[1,0]))
print(testProduitComplexe([1,1],[1,-1]))
print(testProduitComplexe([1,0],[0,1]))


print("==================================================")

#fait le produit d'un nombre complexe avec un reel
def produitScalaire(Z,r):
    r = [r,0]
    return produitComplexe(Z,r)


def testProduitScalaire(Z,r):
    print("Z = ", Z)
    print("r = ", r)
    print("produitScalaire(Z,r) = ", produitScalaire(Z,r))
    return ""

print(testProduitScalaire([1,1],1))
print(testProduitScalaire([1,1],-1))
print(testProduitScalaire([1,0],0))


print("==================================================")

#evalue un polynome P en Z un nombre complexe : resultat nbr cplx
def polyComplexe(P,Z):
    resultat = [0,0]
    puissance = [1,0]
    i = 0
    while i < len(P) :
        resultat = sommeComplexe(resultat,produitScalaire(puissance,P[i]))
        puissance = produitComplexe(puissance,Z)
        i = i + 1
    return resultat

def testPolyComplexe(P,Z):
    print("P = ", P)
    print("Z = ", Z)
    print("polyComplexe(P,Z) = ", polyComplexe(P,Z))
    return ""

print(testPolyComplexe([1,2,1],[0,1]))
print(testPolyComplexe([1,2,1],[0,-1]))
print(testPolyComplexe([0,0,1],[0,1]))


print("==================================================")

#donne le module d'un nombre complexe

def moduleComplexe(Z):
    a = Z[0]
    b = Z[1]
    resultat = sqrt(a**2 + b**2)
    return resultat

def testModuleComplexe(Z):
    print("Z = ", Z)
    print("moduleComplexe(Z) = ", moduleComplexe(Z))
    return ""

print(testModuleComplexe([0,1]))
print(testModuleComplexe([1,0]))
print(testModuleComplexe([1,1]))


print("==================================================")

#donne l'argument d'un nombre complexe

def argumentComplexe(Z):

    a = Z[0]
    module = moduleComplexe(Z)
    return acos(a / module)


def testArgumentComplexe(Z):
    print("Z = ", Z)
    print("argumentComplexe(Z) = ", argumentComplexe(Z))
    return ""

print(testArgumentComplexe([0,1]))
print(testArgumentComplexe([1,0]))
print(testArgumentComplexe([1,1]))


print("==================================================")

#donne le conjugue d'un nombre complexe

def conjugueComplexe(Z):
    resultat = [Z[0],-Z[1]]
    return resultat


def testConjugueComplexe(Z):
    print("Z = ", Z)
    print("conjugueComplexe(Z) = ", conjugueComplexe(Z))
    return ""

print(testConjugueComplexe([0,1]))
print(testConjugueComplexe([1,0]))
print(testConjugueComplexe([1,1]))








