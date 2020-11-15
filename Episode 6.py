def nombreDivisibles(l, n):
    cnt=0
    for nb in l:
        if nb%n==0:
            print(str(nb)+" est divisible par " + str(n))
            cnt+=1
        else:
            print(str(nb)+"n'est pas divisible par " + str(n))
    return cnt

print("le nombre d'élément divisible est "+str(nombreDivisibles([5,16,20,25,27],5)))


def nombreOccurences(l,x):
    cnt=0
    for item in l:
        if item==x:
            cnt+=1
    return cnt

print("le nombre d'occurences de l'élément x est de "+str(nombreOccurences([5,16,20,5,25,27],5))+" fois")


def InsertEtoile(ch):
    ch1=""
    for char in ch:
        if char==ch[-1]:
            break
        else:
            ch1=ch1+char+"*"
    ch1=ch1+ch[-1]
    return ch1

print("La chaine Python devien" + InsertEtoile("Python"))


def toutEnMajuscule(l):
    l1=[]
    for mot in l:
        l1.extend([mot.upper()])
        
    return l1



print(toutEnMajuscule(["Python", "est", "un", "langage", "de", "programmation"]))


def nbminmaj(ch):
    maj=0
    min=0
    for lettre in ch:
        if lettre.isupper() and lettre != " ":
            maj+=1
        elif lettre.islower() and lettre != " ":
            min+=1
    return "Il y'a "+str(maj)+" majuscules et "+str(min)+" minuscules dans la chaine"


print(nbminmaj("Combien Y'a de Maj et de Min"))


def base10(nb):     
    l=[]
    r=0
    while nb>9:
        r=nb%10
        nb= nb//10
       
        l.extend([r])
        if nb<=9:
            l.extend([nb])  
    l.reverse()
    return l

print(str(base10(1748)))


def estcommun(l1,l2):
    l3=[]
    for mot in l1:
        for bis in l2:
            if mot==bis:
                l3.extend([mot])

    return l3

print("Les mots commun a l1 et l2 sont "+str(estcommun(["coucou","toi","salut","tomate"],["courgette","alibaba","toi","coucou","hallo"])))
