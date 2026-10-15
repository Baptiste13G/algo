#Exercice n°1:

#fonction pile : .empiler() .dépiler() .sommet() .estVide()
#fonction file : ...

def pair_impair(p):
    tab_pair=[]
    tab_impair=[]
    while not p.estVide():
        if p.sommet()%2==0:
            tab_pair.append(p.dépiler())
        else:
            tab_impair.append(p.dépiler())
    if len(tab_pair)>len(tab_impair):
        nb=len(tab_pair)-len(tab_impair)
        for x in range(0,nb):
            p.empiler(tab_pair[0])
            tab_pair.pop(0)
    else: 
        nb2=len(tab_impair)-len(tab_pair)
        for y in range(0,nb2):
            p.empiler(tab_impair[0])
            tab_impair.pop(0)
    for i in range(0, len(tab_pair)+len(tab_impair)):
        if p.sommet()%2==0:
            p.empiler(tab_impair[0])
            tab_impair.pop(0)
        else:
            p.empiler(tab_pair[0])
            tab_pair.pop(0)
    return p

"""
pileA=Pile()
pileA.empiler(12)
pileA.empiler(-46)
pileA.empiler(123)
pileA.empiler(85)
pileA.empiler(-111)
pileA.empiler(37)
pileA.empiler(6)
"""
#pair_impair(pileA)

#Exercice n°2:

import random
from math import sqrt

def approx_pi(n):
    c=0
    for i in range(1,n):
        y=random.random()
        x=random.random()
        if sqrt(y**2 + x**2) <=1 : #Points dans le cercle
            c+=1
        resultat=4*c/i
        print(f"Tir : {i} - Approximation de pi : {resultat}")

#approx_pi(15000)

#Exercice n°3:

class Sudoku:
    def __init__(self, liste):
        self.erreur=0

        self.matrice= [[0 for j in range(9)] for i  in range(9)]
        
        self._aide=  [[[] for j in range(9)] for i in range(9)]

        for lig,col,val in liste:
            self.matrice[lig][col]=val

    def afficher(self):
        print("  0 1 2 3 4 5 6 7 8")
        for ligne in range(9):
            print(f"  +-+-+-+-+-+-+-+-+-+")
            ligne_str = f"{ligne} "
            for colonne in range(9):
                valeur = self.matrice[ligne][colonne]
                if valeur == 0:
                    ligne_str += "| "
                else:
                    ligne_str += f"|{valeur}"
            ligne_str += "|"
            print(ligne_str)
        print("  +-+-+-+-+-+-+-+-+-+")

    def ligne_correcte(self,lig):
        #(col,lig,val) je récup lig et val et si val apparait + que une fois (sauf 0) pas correct donc false
        rsp=True
        for val in self.matrice[lig]:
            if val!=0:
                i = self.matrice[lig].count(val)
                if i>1:
                    rsp=False
        return rsp
    
    def colonne_correcte(self,col):
        rsp=True
        colonne = [self.matrice[ligne][col] for ligne in range(9)]
        for val in colonne:
            if val!=0:
                i = colonne.count(val)
                if i>1:
                    rsp=False
        return rsp

    def matrice_correcte(self):
        resp=True
        for i in range(9):
            if resp==False:
                break
            resp=self.ligne_correcte(i) and self.colonne_correcte(i)
        if resp==True:print("bon")
        return resp
    
    def pose_val_sans_aide(self,lig,col,val):
        x=True
        val_changee=self.matrice[lig][col]
        self.matrice[lig][col]=val
        if not self.matrice_correcte():
            self.matrice[lig][col]=val_changee
            x=False
            self.erreur+=1
        return x

    def val_manquantes_ligne(self,lig):
        val=[1,2,3,4,5,6,7,8,9]
        val_pas=[]
        for v in val:
            if v not in self.matrice[lig] :
                val_pas.append(v)
        return val_pas

    def est_dans_colonne(self,col,val):
        x=False
        colonne = [self.matrice[ligne][col] for ligne in range(9)]
        if val in colonne:
            x=True
        return x

    def val_manquantes_colonne(self,col,vals):
        colonne = [self.matrice[ligne][col] for ligne in range(9)]
        val_pas=[]
        for v in vals:
            if v not in colonne:
                val_pas.append(v)
        return val_pas

    def val_possibles(self,lig,col):
        manquantes_ligne = self.val_manquantes_ligne(lig)
        possibles = self.val_manquantes_colonne(col,manquantes_ligne)
        return possibles

    def construit_aide(self):
        for lig in range(9):
            for col in range(9):
                self._aide[lig][col] = self.val_possibles(lig,col)

    def aide(self,lig,col):
        return self._aide[lig][col]

    def pose_val_avec_aide(self,lig,col,val):
        x=True
        if val in self._aide[lig][col]:
            self.matrice[lig][col]=val
            self._aide[lig][col]=[]
            for c in range(9):
                if val in self._aide[lig][c]:
                    self._aide[lig][c].remove(val)
            for l in range(9):
                if val in self._aide[l][col]:
                    self._aide[l][col].remove(val)
        else:
            x=False
        return x
    

        
        
jeu = Sudoku([(0,0,3),(1,1,1),(2,2,5),(1,3,8),(2,3,7),(2,5,1),(0,6,2),(1,7,6),(0,8,7),
              (3,4,7),(3,7,2),(3,8,9),(4,1,7),(6,4,3),(5,1,8),(6,0,8),(6,2,9),(4,3,3),
              (4,5,2),(5,7,7),(5,8,3),(7,2,4),(7,4,8),(8,5,9),(8,6,1)])

"""jeu.afficher()
jeu.construit_aide()
print(jeu.aide(0,2))
jeu.pose_val_avec_aide(0,2,1)
jeu.afficher()"""