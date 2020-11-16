
from itertools import permutations
from itertools import combinations

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


def chiffreportbohneur(nb):
    
    l = base10(nb)  
    while nb >9:
        nb=0
        for nb1 in l:
            nb = nb+nb1**2      
        l = base10(nb)

    return nb

print(str(chiffreportbohneur(913)))
##################################################################################

def generateur(l,nb):
    i=0
    l1=[]
    for item in l:
        while i<nb:
            l1.extend([item])
            i+=1
        i=0    
    return l1

print(generateur(["a","b","c","d"],2))


#######################################################################################




def powerset(l):
    l1=[]
    r=len(l)

    for i in range(0,r+1,1):
        l1.extend([list(combinations(l,i))])
    return l1

l=[1,2,3]
print(powerset(l))

############################################################################################



def mon_decorateur(fonction):
    counter = 0
    def ma_fonction_decoree(*args, **kwargs):
        nonlocal counter
        counter += 1
        print("Appel N°: " + str(counter))
        return fonction(*args, **kwargs)
    return ma_fonction_decoree



@mon_decorateur
def salut():
    print("salut")


salut()
salut()
salut()
