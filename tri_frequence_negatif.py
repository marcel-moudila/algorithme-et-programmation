def valeurAbsolue(X):
    
    ''' entree: un reel X
sortie : la valeur absolue de X'''

    if X < 0 :
        return - X
    else :
        return X

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


print(" ====== Exercice 4 (tri par Fréquence ) ============== ")
def triParFreq(liste):
    
    ''' entree : une liste des entiers positifs
sortie : une liste triee par ordre croissant '''

    #contruction de TF
    taille_TF = valeurAbsolue(max(liste)) + valeurAbsolue(min(liste))+1
    TF = [0]* taille_TF
    i = min(liste)
    while i < max(liste) + 1 :
        TF[i]= nombreOccu(liste,i)
        i = i + 1
    print("TF = ",TF)
    #construction de la liste triee par ordre croissant
    Tnew = []
    j = min(liste)
    while j < max(liste) + 1:
        if TF[j] != 0 :
            Tnew = Tnew + [j]*TF[j]
        j = j+1
    return Tnew
    
#je teste
def testTriParFreq(liste):
    print("triParFreq(",liste,") :",triParFreq(liste))
    return ""

print(testTriParFreq([3,1,5,3,-2,-2]))

print()

print(testTriParFreq([3,1,4,0,2,3,-2,-2]))

print()

print(testTriParFreq([-1,4,0,2,-1,-4,2,5]))

print()

print(testTriParFreq([-6,-9,-5,0,9,0,1,-9,-8,-9]))



