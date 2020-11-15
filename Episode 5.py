from itertools import permutations

chaine = input("Ecrire un texte ").split(" ")
nb_max = len(chaine[0])
mot_max=chaine[0]

for mot in chaine:
    if len(mot) > nb_max:
        nb_max = len(mot)
        mot_max=mot
    
print("Le mot le plus long est "+mot_max+" avec "+str(nb_max)+" caractères")


l=[]
ch=""

if not l:
    print("la liste est vide")

if not ch:
    print("la chaine est vide")



l=[1,2,3,4,2,3,1,5]
print("la liste l :"+str(l)+" sans les doublons devient :")
for item in l:
    if l.count(item)>1:
        l.remove(item)
print(l)


l=[1,2,3,4,2,3,1,5]
l1=[1,7,8,9,5]
val=[]
i=0
for item in l:
    for bis in l1:
        if item==bis:            
            val.extend([item])
            i+=1

for item in val:
    if val.count(item)>1:
        val.remove(item)
print("Pour les listes \n"+str(l)+"\n et \n"+(str(l1)))
print("La/les valeur(s) commune(s) aux deux listes est/sont "+str(val))


l=[1,2,3,4,5]
li=[]
lp=[]

for item in l:
    if item%2==0:
        lp.extend([item])
    else:
        li.extend([item])

print("Pour la liste l : "+str(l)+"\n Les nombre pairs sont : "+str(lp)+"\n Les nombre impairs sont : "+str(li))


l=[1,2,3]
print("Permutation de la liste l : "+str(l))
print(list(permutations(l)))

chaine=input("Saisir une chaine où l'on affichera seulment les caractères avec un indice pair \n")
chainep=""
for i, char in enumerate(chaine):
    if i%2==0:
        chainep= chainep+char
print (chainep)


notes = [12 , 4 , 14 , 11 , 18 , 13 , 7, 10 , 5 , 9 , 15 , 8 , 14 , 16]
notessup=[]
for note in notes:
    if note>=10:
        notessup.extend([note])

print("Pour les notes : "+str(notes)+"\n les notes supérieur ou égale à la moyennes sont :\n"+str(notessup))


chaine = input("Ecrire une chaine afin de compter les occurence d'un mot dans cette chaine \n").split(" ")
char=input("Ecrire le mot pour lequel on veut compter les occurence \n")

dicochaine={}
for mot in chaine:
    dicochaine[mot]=chaine.count(mot)

for val,nb in dicochaine.items():
    if val == char:
        print("Le mot "+val+" apparait "+str(nb)+ " fois")

ch="Cette string   possèdes     des espaces multiple"
print(ch)
ch=ch.split(" ")
ch1=""
for i,char in enumerate(ch):
    while char=="" and ch[i-1]=="":               
        ch.remove(ch[i-1])        

for char in ch:
    ch1=ch1+char+" "      
print(ch1) 


s1 = set(["cou", 6, "nu"])
s2 = set([1, "nu", 6])
print(s1.intersection(s2))


s ="Pyhon est un langage de programmation"
s=s.split(" ")
s2=""
for i in range(0,len(s),1):
    if i==0:
        s2=s[-1]+ " "
    elif i==len(s)-1:
        s2=s2+s[0] + " "
    else:
        s2= s2+s[i] +" "

print(s2)


s ="Pyhon est un langage de programmation"
s=s.split(" ")

nb=len(s)
print("La chaine possède "+str(nb)+" mots")