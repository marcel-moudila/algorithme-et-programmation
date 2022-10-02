
print("=====( test de liste triee par ordre croissant ======")

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

#je teste
T = [1,2,2,3,4]
print("")
print("T =",T)
print("")
print("estTrie(T) = ",estTrie(T))
print("")


print("=============== (tri par echange (ou tri bulle) ) =======================")

def Trie(T):
    '''
        - entree : un tableau d'entiers T
        - sortie : un tableau T trie selon les indications de l'enonce
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

# je teste
T = [5,2,8,1,2]
print("")
print("T = ", T)
print("")
print("Trie(T) = ", Trie(T))
print("")

'''
print("=============== (tri bulle ) =======================")

def triBulle(Tab):
    
    Tnew = Tab[:]
    n = len(Tnew)
    j = 1
    while j < n-1:
        i = 0
        while i < n-j:
            if Tnew[i] >= Tnew[i+1]:
                tmp = Tnew[i]
                Tnew[i] = Tnew[i+1]
                Tnew[i+1] = tmp
            i = i + 1
        j += 1
    return Tnew '''
