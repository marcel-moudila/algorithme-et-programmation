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
    taille_TF = max(liste)+1
    TF = [0]* taille_TF
    i = 0
    while i < len(TF):
        TF[i]= nombreOccu(liste,i)
        i = i + 1
    print("TF = ",TF)
    #construction de la liste triee par ordre croissant
    Tnew = []
    j = 0
    while j < len(TF):
        if TF[j] != 0 :
            Tnew = Tnew + [j]*TF[j]
        j = j+1
    return Tnew
    
#je teste
print("triParFreq([1,4,0,2,1,4,2,4,1])) : ",triParFreq([1,4,0,2,1,4,2,4,1]))

print()

print("triParFreq([1,4,0,4,2,1,6,1,8])) : ",triParFreq([1,4,0,4,2,1,6,1,8]))

print()

print("triParFreq([1,2,3,2,1,3,2,1])) : ",triParFreq([1,2,3,2,1,3,2,1]))



