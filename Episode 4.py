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
   
