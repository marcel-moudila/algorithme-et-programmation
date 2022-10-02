import math



print("========== Exercice 1 ==============")
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
print("========== Exercice 2 ==============")
print()

print()
print ("=== question 1 ===")
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
print("=== question 2 ===")
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
print("=== question 3 ===")
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
print("=== question 4 ===")
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
print("========== Exercice 3 ==============")
print()


print()
print("=== question 1 ===")
print()

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
    else: 
        TqModifie = remplissage(Tq,n)
        Tnew = [TqModifie[i] + Tp[i] for i in range(n)]
        return Tnew

#je teste la fonction sommePoly
def testSommePoly(Tp,Tq):
    print("sommePoly(",Tp,",",Tq,") = ",sommePoly(Tp,Tq))
    return ""


print(testSommePoly([1,0,2,-1],[0,3,5,2,2]))
print(testSommePoly([0,0,2,-1,3,0,0,0],[0,3,5,2,2,1,1]))


print()
print("=== question 2 ===")
print()

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


print()
print("=== question 3 ===")
print()

def produitMonome(Tp,a,d):
    
    ''' entree: un polynome Tp quelconque  et un monome de coefficient a et de degre d
sortie : le produit polynomiale de Tp avec le monome '''

    if d == 0 :
        resultat = produitScal(Tp,a)
        return resultat
    else :
        resultat = [0]*d + [a * Tp[i - d] for i in range(d,len(Tp)+d)]
        return resultat


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



print()
print("=== question 4 ===")
print()

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


print()
print("=== question 5 ===")
print()

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
    
    
print()
print("=== question 6 ===")
print()

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

        
print()
print("========== Exercice 4 ==============")
print()

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



def AKS(n):

    
    if not estParfait(n):#etape 1
        
        
        r = 1
        while ordre(n,r) <= 4*math.log(n**2,2) :
            r = r  + 1 #etape 2

            
        for a in range (r+1):
            d = pgcd(a,n)
            if 1 < d and d < n :  
                return False #etape 3
            
        if n <= r : 
            return True #etape 4
                
        else :
            print("bonjour")
            for a in range(1,2*(euler(r)**0.5)*math.log(n,2)): 
                P = puissancePoly([a,1],n)
                Q = sommePoly([-1],puissancePoly([0,1],r))
                R = sommePoly([a],puissancePoly([0,1],n))
                if not egale(restePoly(P,Q),R):
                    return False #etape 5
            
            return True #etape 6
    else :
        return False

#je teste


print(not estParfait(3)) # =  True


def etape2_AKS(n):
    r = 1
    while ordre(n,r) <= 4*math.log(n**2,2) :
        r = r  + 1
    return r

print(etape2_AKS(3)) # = 15

def etape3_AKS(n):
    r = etape2_AKS(n)
    for a in range (r+1):
        d = pgcd(a,n)
        if 1 < d and d < n :  
            return False
    return True

print(etape3_AKS(3))

def etape4_AKS(n):
    r = etape2_AKS(n)
    if n <= r :
        return True
    
print(AKS(24))




              
  

    
    
