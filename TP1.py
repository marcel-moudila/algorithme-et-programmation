#TP1
print("Exercice 1*************************************************")
            
x = 1
y = 3
surname = "MOUDILA "
firstname = "Marcel "
A = -2.5
B = 2.5

print(x+y)
print(surname + firstname)
print(A+B)
            

print(A*B)

print(surname*y)
            
s= 1
i= 1
print(s+i)
print(s+s)
print(s+i)
print()
print("Exercice 2*********************************************")
x = 6
y = 2
chaine1 = " x = 6"
chaine2 = " y = 2"
print(chaine1)
print(chaine2)

print()
print("Exercice 3*********************************************")
note = 10
affichage1 = " Bravo "
affichage2 = " Essaye encore "
if note > 10 : 
   print (affichage1) 
else : 
   print (affichage2)

print()
print("Exercice 4*********************************************")


def tarif(membre,entier1):
      if membre :
         if entier1 <= 16 :
            return "gratuit"
         else :
            return " 2 euros "
      else :
         if entier1 <= 3 :
            return "gratuit"
         if (entier1 >= 4) and (entier1 <= 16) :
            return " 2 euros"
         if (entier1 >= 17) and (entier1 <= 65) :
            return " 5 euros "
         if entier1 > 66 :
            return "3 euros"
                          
print(tarif(True,0))
print(tarif(True,4))
print(tarif(True,67))
print(tarif(False,3))
print(tarif(False,65))



print()
print("Exercice 5*********************************************")
            #question 1
entier_n = 100
print()
            #question 2
i = 0
for loop in range(entier_n) :
   print(i,end = " ")
   i = i + 1
print()
print()
            #question 3
i = 0
for loop in range(entier_n):
   print(2*i,end = " ")
   i = i+1
print()
print()
            #question 4
print(entier_n * (entier_n + 1))
print()
            #question 5
i = 0
somme = 0
for loop in range(entier_n):
   somme = somme + i
   i = i + 1
print(somme)
print()
            #question 6
i = 0
somme_carré = 0
for loop in range(entier_n) :
   somme_carré = somme_carré + i*i
   i = i + 1
print(somme_carré)
print()
            #question 7
i = 1
for loop in range(entier_n) :
   if entier_n % i ==  0 :
      print(i,end = " ")
   i = i + 1
print()
            #question 8
lettre = "n "
print(lettre * entier_n)
print()
print()


print("Exercice 6*********************************************")
            #question 1
nb_étoiles = 25
affiche = "* "
print(affiche * nb_étoiles)
print()
print()
            #question 2
i = 1
for loop in range(nb_étoiles) :
   print(affiche * i)
   i = i + 1
print()
print("Exercice 7*********************************************")
            #question 1
def fonction1(entier1,entier2) :
      x = entier1 + entier2
      return (entier1 + entier2)

print(fonction1(5,7))
print()
            #question 2
entier1 = 2
entier2 = 3
def echange(entier1,entier2):
      aux = entier1
      entier1 = entier2
      entier2 = aux
      return(entier1,entier2)
print(echange(5,7))
print()
#question 3
def fonction2(entier1,entier2,booléen):
      
      if booléen :
         print( "je fais la somme de",entier1,"et",entier2,"qui vaut", entier1 + entier2)
         return " "
      
print(fonction2(-11,4,True))


   
  






