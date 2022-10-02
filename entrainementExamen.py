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


def listePremier(n):

    resultat = [i for i in range(n) if cribleEratostheme(i)]

    return resultat

print(listePremier(100))
