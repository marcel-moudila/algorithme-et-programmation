############################
print(" ")
print("=== Exercice 1, question 1 ====")
print(" ")
############################
alphabet = "abcdefghijklmnopqrstuvwxyz"
def rechercheIndex(lettre, alphabet):
    for i in range(len(alphabet)) :
        if alphabet[i] == lettre:
            return i

print("rechercheIndex(a,alphabet): ",rechercheIndex("a",alphabet))
print("rechercheIndex(z,alphabet): ",rechercheIndex("z",alphabet))
print("rechercheIndex(q,alphabet): ",rechercheIndex("q",alphabet))
############################
def decalage(lettre, entier, alphabet):
    for i in range (len(alphabet)):
        if alphabet[i] == lettre :
            return alphabet[ (i + entier) % len(alphabet)]

print("decalage(a,1,alphabet) : ",decalage("a",1,alphabet))
print("decalage(z,2,alphabet) : ",decalage("z",2,alphabet))
print("decalage(q,17,alphabet) : ",decalage("q",17,alphabet))
############################
def decalageMot(mot, entier, alphabet):
    nouveauMot = ""
    for i in range(len(mot)):
        nouveauMot = nouveauMot + decalage(mot[i],entier,alphabet)
    return nouveauMot

print("decalageMot(bonjour, 4,alphabet) : ",decalageMot("bonjour",4,alphabet))
############################
def decalageMotVigenere(mot, tableau, alphabet):
    nouveauMot = ""
    if len(mot) <= len(tableau):
        for i in range(len(mot)):
            nouveauMot = nouveauMot + decalage(mot[i],tableau[i],alphabet)
    return nouveauMot

print("decalageMotVigenere(bonjour,[25,6,4,21,2,4,3,2,1],alphabet) : ",decalageMotVigenere("bonjour",[25,6,4,21,2,4,3,2,1],alphabet))
############################
print(" ")
print("=== Exercice 1, question 2 ====")
print(" ")
############################
print("Ces deux fonctions ne font rien de spécial ,elles renvoient les valeurs c et b quand la condition du while prend fin")
def fonct1(tableau):
	a = 0
	b = tableau[0]
	c = -1
	while a < len(tableau):
		if b < tableau[a]:
			c = a
			b = tableau[a]		
		a = a+1
	return c

def fonct2(tableau):
	a = 0
	b = tableau[0]
	c = -1
	while a < len(tableau):
		if b < tableau[a]:
			c = a
			b = tableau[a]		
		a += 1
	return b

print(fonct1([1,5,2,5,6,1,6]))
print(fonct2([1,5,2,5,6,1,6]))

############################
print(" ")
print("=========== Exercice 3 ===========")
print(" ")
############################
def moyenne(T):
	'''entrée : tableau d'entiers
	sortie : un réel
	calcule la moyenne d'un tableau'''
	i = 0
	somme = 0
	while i < len(T):
		somme = somme + T[i]
		i = i + 1
	return somme/i
def enlever(T,e):
	'''entrée : un tableau et un élément de même type que le tableau
	sortie : un tableau
	enlève toutes les occurences de e dans T'''
	i = 0
	Taux = []
	while i < len(T):
		if T[i] != e:
			Taux += [T[i]]
		i+=1
	return Taux
def triParMaxi(T):
	'''Entrée un tableau
	sortie : un tableau
	tri le tableau T'''
	Taux = []
	while len(T) > 0:
		m = max(T)
		T = enlever(T,m)
		Taux =  Taux + [m] #ici demandez au prof car c'était [m] + Taux
	return Taux
print("la moyenne de [1,1,0,1,9] est : ", moyenne([1,1,0,1,9,]))
print("le tri par maximum du tableau [1,1,0,1,9] est : ", triParMaxi([1,1,0,1,9]))
############################
print(" ")
print("=========== Exercice 2 ===========")
print(" ")
import random

def minimum(i,j):
	'''Retourne le minimum de deux entiers'''
	return min(i,j)

def maximum(T):
	'''Attend un tableau d'entier et retourne le max'''
	return max(T)

		
#--Initialisation des variables--#

T1 = [1,5,5,7,8,25]
T2 = [2,2,5,10,19,21]
Taux = [0]*(len(T1)+len(T2))
p = ""

'''#--Fusion de deux tableaux triés en un tableau trié--#
for k in range(len(Taux)):
        Taux[k] = min(min(T1),min(T2))
        p = p + Taux[k]
        T1 = [i for i in T1 if i!= Taux[k]]
        T2 = [i for i in T2 if i!= Taux[k]]
print(Taux)'''

#--Création d'un tableau de taille du plus grand entier contenu dans T1 et T2--#
#--Ce tableau sera rempli de lettres aléatoires--#
T3 = [0]*max(max(T1),max(T2))
s = ""
Talpha= "nbrvaakvvvoivgjckjsocojkhcgwhcgwkhcvgwhkjv"
for i in range(len(T3)):
	T3[i] = random.choice(Talpha)
	s = s + T3[i]
print(s)
print(len(s))
	
	



