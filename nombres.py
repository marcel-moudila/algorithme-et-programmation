def diviseurStrict(p):
    '''
        - entree : un entier positif p
        - sortie : la liste des diviseurs strictes de p
    '''

    liste = [n for n in range(1,p) if p % n == 0]
    return liste

def nombresAmis(p):
    '''
        - entree : un entier p
        - sortie : les couples d'entiers (i,j) tel que i < p, j < p , i et j sont amis
    '''

    Tnew = []
    for j in range(1,p+1):
        i = sum(diviseurStrict(j))
        if sum(diviseurStrict(i)) == j: #alors i et j sont amis
            Tnew = Tnew + [(i,j)]
    return Tnew

p = 15000
print("p = ",p)
print("nombresAmis(p) =",nombresAmis(p))


print()
print("===========================================")
print()

def diviseur(p):
    '''
        - entree : un entier positif p
        - sortie : la liste des diviseurs de p
    '''

    liste = [n for n in range(1,p+2) if p % n == 0]
    return liste

def cribleEratostheme(p):
    '''
        - entree : un entier positif p
        - sortie : un booleen (True si p est premier, False sinon)
    '''

    if len(diviseur(p)) == 2 :
        return True
    else :
        return False

#je teste
print("cribleEratostheme(10) = ",cribleEratostheme(10))
print("cribleEratostheme(9) = ",cribleEratostheme(9))
print("cribleEratostheme(13) = ",cribleEratostheme(13))

print()
print("===========================================")
print()

print()
print("===========================================")
print()

def pgcd(a,b):
    '''
        - entree : deux entiers a et b
        - sortie : le plus grand commun diviseur de a et b
    '''

    liste1 = diviseur(a)
    liste2 = diviseur(b)
    liste3 = [d for d in liste1 if d in liste2]

    return max(liste3)

#je teste

print("pgcd(10,5) = ", pgcd(10,5))
print("pgcd(9,5) = ", pgcd(9,5))
print("pgcd(255,75) = ", pgcd(255,75))

print()
print("===========================================")
print()

def euler(n):
    '''
        - entree : un entier n
        - sortie : l'indicatrice d'Euler de n
    '''
    
    if n == 0 :
        return 1

    liste = [a for a in range(1,n) if pgcd(a,n) == 1]
    return len(liste)

#je teste

print("euler(10) = ",euler(10))
print("euler(9) = ",euler(9))
print("euler(8) = ",euler(8))

print()
print("===========================================")
print()

def estParfait(n):
    '''
        - entree : un entier n
        - sortie : un booleen (True si n est une puissance parfaite)
    '''
    
    if cribleEratostheme(n) :
        return False
    else : 
        A = diviseur(n)
        B = A[1:len(A)-1]
        i = 0
        while i < len(B) - 1 :
            if pgcd(B[i],B[i+1]) == 1:
                return False
            i = i + 1
        return True

# je teste

print("estParfait(8) = ",estParfait(8))
print("estParfait(10) = ",estParfait(10))
print("estParfait(27) = ",estParfait(27))

print()
print("===========================================")
print()

def ordre(n,r):
    '''
        - entree : deux entiers n et r non nuls
        - sortie : le plus petit entier i tel que n**i % r == 1
    '''
    
    i = 1
    while i <= r and (n**i) % r != 1  :
        i = i + 1
    return i-1
    


#je teste
def testOrdre(n,r):
    print("ordre(",n,",",r,") = ",ordre(n,r))
    return ""

print(testOrdre(1,11))
print(testOrdre(2,11))
print(testOrdre(3,11))
print(testOrdre(4,11))
print(testOrdre(5,11))
print(testOrdre(6,11))
print(testOrdre(7,11))
print(testOrdre(8,11))
print(testOrdre(9,11))
print(testOrdre(10,11))


print()
print("===========================================")
print()

def premiersJumeaux(n):
    '''
        - entree : un entier n
        - sortie : la liste des nombres premiers jumeaux < n
    '''
    # deux nombres premiers jumeaux sont deux nombres premiers distant de 2, par exemple 3 et 5

    Tnew = []
    liste = [p for p in range(2,n) if cribleEratostheme(p)]
    n = len(liste)
    resultat = [(liste[i],liste[i+1]) for i in range (n-1) if liste[i+1] - liste[i] == 2]
    return resultat

print(premiersJumeaux(100))


print()
print("===========================================")
print()

def extracteurChiffre(n):
    texte = str(n)
    tab = list(texte)
    return tab

print(extracteurChiffre(123456))


    

    
    

