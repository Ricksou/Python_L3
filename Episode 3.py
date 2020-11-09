import math
import os

i=1
while i <=10:
    print(str(i))
    i=i+1

print()
n = int(input("Entrer un nombre n pour afficher la valeur de 1+2+...+n et de 1*2*...*n "))

i=1
val=1
while i < n:

    
    val = val + i+1
   

    i=i+1

print(str(val))   

i=1
val=1
while i < n:

    
    val = val * (i+1)
   

    i=i+1

print(str(val))
print()

r = int(input("Entrer le rayon d'un cercle en cm "))

surface = math.pi*r*r
perimetre = 2* math.pi *r

print("La surface d'un cercle de rayon "+str(r)+" est de "+str(surface)+ " cm².")
print("Le périmètre d'un cercle de rayon "+str(r)+" est de "+str(perimetre)+ " cm.")

print()
d = int(input("Entrer un nombre pour lequel on affichera ses diviseurs "))
i=d
while i > 0:
    
    if d % i ==0:
        print(str(i))
    i = i-1 
  
    
   
print()
d = int(input("Entrer un nombre pour lequel on affichera sa table de multiplication "))

i=1
while i<=10:
    multi= d*i
    print(str(d) +" * "+str(i)+" = "+str(multi))
    i=i+1


i=1
j=1
print()
print("Toutes les tables de multiplication de 1 à 9")
os.system("Pause")
while i<=9:
    print("Table de "+str(i))
    while j <= 10:
        multi= j*i
        print(str(i) +" * "+str(j)+" = "+str(multi))
        j=j+1
    j=1
    print()             
    i=i+1


print()
print("Division Euclidienne (a/b)")
a = int(input("Entrer le premier nombre nommé a "))
b = int(input("Entrer le premier nombre nommé b "))    


r=a%b
q= (a-r)/b
print("Le résultat de la Division Euclidienne "+str(a) +" / "+str(b) +" = "+ str(q)+" et reste "+str(r))


print()
e = int(input("Rentrez un nombre entier pour vérifier si il est un carré parfait ou non "))

racine = math.sqrt(e)
if e%racine==0:
    print("Votre nombre est un carré parfait")
else:
    print("Votre nombre n'est pas un carré parfait")


print()
e = int(input("Rentrez un nombre entier pour vérifier si il est premier "))
i=e-1
premier = True
while i > 1:
    if e%i==0:
        premier=False
    i = i-1

if premier == True:
    print("Votre nombre est premier")
else:
    print("Votre nombre n'est pas premier")
