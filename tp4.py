import random
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
