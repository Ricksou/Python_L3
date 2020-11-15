

chaine = "Python"

for lettre in chaine:
    print(lettre)


print()
chaine = str(input("Ecrire un mot afin de compter les occurence de chaque lettre dans ce mot "))
i=0
cnt=0

while i <= len(chaine)-1 :
    compteur = chaine.count(chaine[i])
    
    i+=1
    index=i
    i-=1
    while i>=0:
        if chaine[index-1] == chaine[i]:
            cnt+=1
        i-=1        
        
    if cnt ==1:
        print("La lettre "+chaine[index-1]+ " est affiché "+str(compteur)+ " fois")
                
        
    cnt=0
    i =index
   


chaine = str(input("Ecrire un mot "))
char = str(input("Saisissez la lettre a rechercher dans le mot "))


for i in range(0,len(chaine),1):
    if char == chaine[i]:
        print("La lettre "+char+" se trouve à la position "+str(i+1))



l = ["laptop", "iphon", "tablet"]
for item in l:
    print(item + " possède " + str(len(item))+ " caractères")


chaine = str(input("Ecrire un mot "))
char=chaine[-1]
char1= chaine[0]
chaine2=""
for i in range(0,len(chaine),1):
    if i==0:
        chaine2=chaine[-1]
    elif i==len(chaine)-1:
        chaine2=chaine2+chaine[0] 
    else:
        chaine2= chaine2+chaine[i] 
 
print(chaine2)


chaine = str(input("Ecrire un mot "))
cnt=0
for lettre in chaine:
    if lettre in "aeiouy":
        cnt +=1

print("Il y'a "+str(cnt)+" voyelles dans ce mot")


chaine = str(input("Ecrire une phrase "))
i=0
first=""
while chaine[i] != " " :
    first = first+chaine[i]
    i+=1
print(first)


chaine = str(input("Ecrire le nom d'un fichier "))
ext=""
for i in range(0,len(chaine),1):
    if chaine[i]==".":
        for i in range(i,len(chaine),1):
            ext= ext+chaine[i]
print("L'extension du fichier est "+ext)


chaine = str(input("Ecrire un mot "))
mirroir=""
l=len(chaine)
for i in range(0,l,1):
    mirroir=mirroir+chaine[l-1-i]

if mirroir==chaine:
    print("C'est bien un palindrome")
else:
    print("Ce n'est pas un palindrome")


chaine = str(input("Ecrire un mot "))
mirroir=""
l=len(chaine)
for i in range(0,l,1):
    mirroir=mirroir+chaine[l-1-i]

print(mirroir)


chaine = str(input("Ecrire un texte "))
char = str(input("Saisissez la lettre a rechercher dans le texte "))
l=len(chaine)
mot=""
i=0
if chaine[0]==char:
    while chaine[i]!=" ":
            mot=mot+chaine[i]
            i+=1
    print(mot)

for i in range(0,l,1):
    if chaine[i]==char and chaine[i-1]==" ":
        mot=""
        while chaine[i]!=" " and i < l-1:
            mot=mot+chaine[i]
            if i==l-2:
                mot=mot+chaine[i+1]
            i+=1
        print(mot)


chaine = input("Ecrire un texte ").split(" ")
char = input("Saisissez la lettre a rechercher dans le texte ")

for item in chaine:
    if item[0]==char:
        print(item)

