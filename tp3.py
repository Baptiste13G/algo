import math

#Exercice 1
def inverse_carre1(n):
    somme=0
    for i in range(1,n+1):
        somme=somme+(1/(i**2))
    return somme

#print(inverse_carre1(3))

def inverse_carre2(n,add=0):
    if n==1:
        return add+1
    add=add+1/(n**2)
    return inverse_carre2(n-1,add)

#print(inverse_carre2(3))

#Exercice 2

def n_premiers_termes1(n):
    tab=[]
    for i in range(n):
        if i==0:
            tab.append(1)
        else:
            tab.append(3*tab[i-1]+1)
    return tab

#print(n_premiers_termes1(3))

def n_premiers_termes2(n):
    if n==0:
        return[]
    tab = n_premiers_termes2(n - 1)
    if len(tab) == 0:
        tab.append(1) 
    else:
        tab.append(3 * tab[-1] + 1)
    
    return tab

#print(n_premiers_termes2(3))

#Exercice 3

def termes_adja(n,dic={}):
    if n in dic:
        return dic[n]
    if n==0:
        dic[0]=(4,5)
        return dic[0]
    u_prec, v_prec = termes_adja(n-1, dic)
    un = (u_prec + v_prec) / 2
    vn = math.sqrt(u_prec * v_prec)
    dic[n]=(un,vn)
    return dic[n] 

#print(termes_adja(2)) 

#Exercice 4

def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    resultat = 0
    for i in range(n):
        sous_matrice = []
        for k in range(n):
            if k != i:
                ligne = []
                for j in range(1, n):
                    ligne.append(A[k][j])
                sous_matrice.append(ligne)
        signe = (-1) ** i
        resultat += signe * A[i][0] * det(sous_matrice)
    
    return resultat

#print(det([[1, 2], [3, 4]]))
#print(det([[5]])) 

#Exercice 5

def occurence(phrase,car):
    if len(phrase)==0:
        return 0
    else:
        if phrase[0]==car:
            return 1 +occurence(phrase[1:],car)
        else:
            return 0+occurence(phrase[1:],car)
        
pi="aaaaa bricot"
#print(occurence(pi,'a'))

#Exercice 6

def anagramme(c1,c2,dic1=None,dic2=None):
    if dic1 is None: dic1 = {}
    if dic2 is None: dic2 = {}
    if len(c1)!=len(c2):
        return False
    if len(c1)==0:
        return dic1==dic2
    if c1[0] not in dic1:
        dic1[c1[0]]=1
    elif c1[0] in dic1:
        dic1[c1[0]]+=1
    if c2[0] not in dic2:
        dic2[c2[0]]=1
    elif c2[0] in dic2:
        dic2[c2[0]]+=1
    return anagramme(c1[1:],c2[1:],dic1,dic2)

#Exercice 7

def temps_de_vol(N):
    u = N
    n = 0
    while u != 1:
        if u % 2 == 0:
            u = u // 2
        else:
            u = 3 * u + 1
        n += 1
    return n

def altitude_max(N):
    u = N
    maximum = u
    while u != 1:
        if u % 2 == 0:
            u = u // 2
        else:
            u = 3 * u + 1
        if u > maximum:
            maximum = u
    return maximum

#print(temps_de_vol(6))
#print(altitude_max(6)) 

#Exercice 8

def u_naif(n):
    if n == 0 or n == 1:
        return 1
    return 2 * u_naif(n - 1) + 3 * u_naif(n - 2)

#print(u_naif(200)) ça plante...

def u_memo(n, cache=None):
    if cache is None:
        cache = {0: 1, 1: 1}
    if n in cache:
        return cache[n]
    cache[n] = 2 * u_memo(n - 1, cache) + 3 * u_memo(n - 2, cache)
    return cache[n]

#print(u_memo(200)) grâce au mémo/cache ça fonctionne 
    
#Exercice 9

def dans_la_liste(n,tab,i=0):
    if i>=len(tab):
        return False
    if tab[i]==n:
        return True
    return dans_la_liste(n,tab,i+1)

#print(dans_la_liste(3 , [1 , 2 , 5]))
#print(dans_la_liste(2 , [1 , 2 , 5]))

#Exercice 10 

def dans_la_liste_triee(n, tab, debut=0, fin=None):
    if fin is None:
        fin = len(tab) - 1
    if debut > fin:
        return False
    milieu = (debut + fin) // 2
    if tab[milieu] == n:
        return True
    if tab[milieu] < n:
        return dans_la_liste_triee(n, tab, milieu + 1, fin)
    else:
        return dans_la_liste_triee(n, tab, debut, milieu - 1)

#print(dans_la_liste_triee(3 , [1 , 2 , 5]))
#print(dans_la_liste_triee(2 , [1 , 2 , 5]))

#Exercice 11

def intersection(l1, l2, i=0, resultat=None):
    if resultat is None:
        resultat = []
    if i >= len(l1):
        return resultat
    if l1[i] in l2:
        resultat.append(l1[i])
    return intersection(l1, l2, i + 1, resultat)

#print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
#print(intersection([1, 2], [3, 4]))