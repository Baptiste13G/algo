import random
<<<<<<< HEAD
import math
=======
>>>>>>> 5040e18 (algo)
from pilefile import *

#Exercice 1

def recherche_mini(l, ind):
    mini = ind
    for i in range(ind, len(l)):
        if l[i] < l[mini]:
            mini = i
    return mini

def tri_selection(l):
    for i in range(len(l)):
        ind_mini=recherche_mini(l,i)
        l[i], l[ind_mini]= l[ind_mini], l[i]

def tri_a_bulles(l):
    bulle = True
    i=0
    while i< len(l) and bulle:
        bulle = False
        for ind in range(len(l) - i - 1):
            if l[ind] > l[ind + 1]:
                l[ind], l[ind + 1] = l[ind + 1], l[ind]
                bulle = True
        i += 1

def tri_insertion(l):
    for i in range(1, len(l)):
        ref = l[i]
        j=i-1
        while j >= 0 and l[j] > ref:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = ref

def tab_random(n):
    tab=[]
    for _ in range(n):
        tab.append(random.randint(1,100))
    return tab

#+ rapide selection puis insertion puis a bulle.

def pile_random(n,p):
    for _ in range(n):
        p.empiler(random.randint(1,100))
    return p

def tri_pile(p):
    resultat = Pile()
    temp = Pile()

    while not p.est_vide():
        min_courant = p.depiler()
        while not p.est_vide():
            x = p.depiler()
            if x < min_courant:
                temp.empiler(min_courant)
                min_courant = x
            else:
                temp.empiler(x)

        while not temp.est_vide():
            p.empiler(temp.depiler())

        resultat.empiler(min_courant)

    return resultat

def tri_gnome(l):
    i = 0
    while i < len(l):
        if i == 0 or l[i] >= l[i - 1]:
            i += 1
        else:
            l[i], l[i - 1] = l[i - 1], l[i]
            i -= 1
    return l

#Exercice 2:

def fusionner(l, deb, milieu, fin):
    part1, part2 = l[deb:milieu], l[milieu:fin]
    i, j, k = 0, 0, deb
    while i< len(part1) and j< len(part2):
        if part1[i] < part2[j]:
            l[k] = part1[i]
            i += 1
        else:
            l[k] = part2[j]
            j += 1
        k += 1
    while i< len(part1):
        l[k] = part1[i]
        i, k = i + 1, k + 1
    while j< len(part2):
        l[k] = part2[j]

def tri_fusion(l, deb, fin):
    if fin - deb >= 2:
        milieu = (deb + fin) // 2
        tri_fusion(l, deb, milieu)
        tri_fusion(l, milieu, fin)
        fusionner(l, deb, milieu, fin)

def tri_fusion2(l, deb, fin):
    if len(l)<100:
        return tri_insertion(l)
    if fin - deb >= 2:
        milieu = (deb + fin) // 2
        tri_fusion(l, deb, milieu)
        tri_fusion(l, milieu, fin)
        fusionner(l, deb, milieu, fin)

def tri_mixte(l, k):
    taille = len(l) // k + 1
    sous = [l[i:i+taille] for i in range(0, len(l), taille)]
    for s in sous:
        tri_insertion(s)
    res = []
    while any(sous):
        mini, arg = min((s[0], j) for j, s in enumerate(sous) if s)
        res.append(sous[arg].pop(0))
    return res

#Exercice 3
<<<<<<< HEAD

def tri_chaine(s:str)->str:
    #renvoie la chaine de caractère triée par ordre alphabétique
    dic_alph={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
              "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    res=""
    for i in range(len(s)):
        dic_alph[s[i]]+=1
    for cle,valeur in dic_alph.items():
        for i in range(valeur):
            res+=cle
    return res


def tri_insertion2(l):
    for i in range(1, len(l)):
        ref = l[i]
        lo, hi = 0, i
        while lo < hi:
            mid = (lo + hi) // 2
            if l[mid] <= ref:
                lo = mid + 1
            else:
                hi = mid
        for j in range(i, lo, -1):
            l[j] = l[j - 1]
        l[lo] = ref
    return l

def partitionner(l, deb, fin):
    pivot = l[fin - 1]
    borne_inf = deb
    borne_sup = fin - 1
    while borne_inf < borne_sup:
        if l[borne_inf] < pivot:
            borne_inf += 1
        else:
            l[borne_sup] = l[borne_inf]
            l[borne_sup - 1] = l[borne_sup - 1]
            l[borne_sup - 1] = l[borne_inf]
    borne_sup -= 1
    l[borne_inf] = pivot

def tri_rapide(l, deb, fin):
    if deb < fin - 1:
        ind_pivot = partitionner(l, deb, fin)
        tri_rapide(l, deb, ind_pivot)
        tri_rapide(l, ind_pivot + 1, fin)

def partitionner2(l, deb, fin):
    pivot = l[deb]
    borne_inf = deb
    borne_sup = fin - 1
    while borne_inf < borne_sup:
        if l[borne_inf] < pivot:
            borne_inf += 1
        else:
            l[borne_sup] = l[borne_inf]
            l[borne_sup - 1] = l[borne_sup - 1]
            l[borne_sup - 1] = l[borne_inf]
    borne_sup -= 1
    l[borne_inf] = pivot

def tri_rapide2(l, deb, fin):
    if deb < fin - 1:
        ind_pivot = partitionner2(l, deb, fin)
        tri_rapide(l, deb, ind_pivot)
        tri_rapide(l, ind_pivot + 1, fin)

def partitionner_rec(l, deb, fin, k=None, borne_inf=None):
    if k is None:
        k = deb
    if borne_inf is None:
        borne_inf = deb
    pivot = l[fin - 1]
    if k == fin - 1:
        l[borne_inf], l[fin - 1] = l[fin - 1], l[borne_inf]
        return borne_inf
    if l[k] < pivot:
        l[borne_inf], l[k] = l[k], l[borne_inf]
        return partitionner_rec(l, deb, fin, k + 1, borne_inf + 1)
    else:
        return partitionner_rec(l, deb, fin, k + 1, borne_inf)

#Exercice 4:

def dist_origine(p):
    return p[0] ** 2 + p[1] ** 2

def tri_insertion(points):
    l = points[:]
    for i in range(1, len(l)):
        ref = l[i]
        d_ref = dist_origine(ref)
        j = i - 1
        while j >= 0 and dist_origine(l[j]) > d_ref:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = ref
    return l

def tri_selection(points):
    l = points[:]
    n = len(l)
    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if dist_origine(l[j]) < dist_origine(l[imin]):
                imin = j
        l[i], l[imin] = l[imin], l[i]
    return l
=======
>>>>>>> 5040e18 (algo)
