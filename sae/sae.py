from classes.pilefile import *

class Labyrinthe:
    """Modélise un labyrinthe sous forme de grille 2D et permet sa résolution."""
    def __init__(self, modele):
        self.modele = modele
        self.lignes = len(modele)
        self.colonnes = len(modele[0])
        self.entree = self.trouver_entree()
        self.sortie = self.trouver_sortie()
        for ligne in modele:
            if len(ligne) != self.colonnes:
                raise ValueError("La grille doit être rectangulaire")
        if self.entree is None or self.sortie is None:
            raise ValueError("Le labyrinthe doit contenir une entrée 'S' et une sortie 'E'")

    def afficher_labyrinthe(self):
        """
        Affiche la grille du labyrinthe dans le terminal.
        """
        chaine=""
        for i in range(self.lignes):
            chaine+='\n'
            for j in range(self.colonnes):
                if self.modele[i][j]=='#':
                    chaine+=' # ' 
                if self.modele[i][j]=='S':
                    chaine+=' S '
                if self.modele[i][j]=='E':
                    chaine+=' E '
                if self.modele[i][j]=='.':
                    chaine+=' . '
        print(chaine)

    def est_valide(self, ligne, colonne):
        """
        Vérifie si la case (ligne, colonne) est dans la grille et n'est pas un mur ('#').
        """
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes and self.modele[ligne][colonne] != '#':
            return True
        return False

    def trouver_entree(self):
        """
        Recherche et renvoie les coordonnées (ligne, colonne) de l'entrée 'S'.
        """
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if self.modele[i][j] == 'S':
                    return (i,j)
        return

    def trouver_sortie(self):
        """
        Recherche et renvoie les coordonnées (ligne, colonne) de la sortie 'E'.
        """
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if self.modele[i][j] == 'E':
                    return (i,j)
        return
    
    def res_dfs(self):
        """
        Résout le labyrinthe en profondeur (DFS) et renvoie (trouvé, chemin, nb_visites).
        """
        p=Pile()
        p.empiler(self.entree)
        visit=[self.entree]
        pred = {self.entree : None}
        while not p.est_vide() :
            sommet = p.depiler()
            if sommet == self.sortie:
                break
            ligne, colonne = sommet
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dl, dc in directions:
                v_ligne = ligne + dl
                v_colonne = colonne + dc
                voisin = (v_ligne, v_colonne)
                if self.est_valide(v_ligne, v_colonne) and voisin not in visit:
                    visit.append(voisin)
                    pred[voisin] = sommet
                    p.empiler(voisin)
        if self.sortie not in pred:
            return False, [], len(visit)
        chemin = []
        courant = self.sortie
        while courant is not None:
            chemin.append(courant)
            courant = pred[courant]
        chemin.reverse()
        return True, chemin, len(visit)
    
    def res_bfs(self):
        """
        Résout le labyrinthe en largeur BFS et renvoie (trouvé, chemin, nb_visites).
        """
        f=File()
        f.ajouter(self.entree)
        visit=[self.entree]
        pred = {self.entree : None}
        while not f.est_vide() :
            sommet = f.enlever()
            if sommet == self.sortie:
                break
            ligne, colonne = sommet
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dl, dc in directions:
                v_ligne = ligne + dl
                v_colonne = colonne + dc
                voisin = (v_ligne, v_colonne)
                if self.est_valide(v_ligne, v_colonne) and voisin not in visit:
                    visit.append(voisin)
                    pred[voisin] = sommet
                    f.ajouter(voisin)
        if self.sortie not in pred:
            return False, [], len(visit)
        chemin = []
        courant = self.sortie
        while courant is not None:
            chemin.append(courant)
            courant = pred[courant]
        chemin.reverse()
        return True, chemin, len(visit)
    
    def afficher_chemin(self, chemin, symbole='*'):
        """Affiche une copie du labyrinthe avec le chemin tracé."""
        grille_copie = [ligne[:] for ligne in self.modele]
        for ligne, colonne in chemin:
            if grille_copie[ligne][colonne] != 'S' and grille_copie[ligne][colonne] != 'E':
                grille_copie[ligne][colonne] = symbole        
        for ligne in grille_copie:
            print(" ".join(ligne))
        
                
#Test

#1. Labyrinthe simple
lab1 = Labyrinthe([
    ['S', '.', '#'],
    ['#', '.', '.'],
    ['#', '#', 'E']
])
print("Test 1 : DFS :", lab1.res_dfs())
print("Test 1 : BFS :", lab1.res_bfs())

#2. Labyrinthe avec boucle (BFS doit trouver un chemin plus court que DFS)
lab2 = Labyrinthe([
    ['S', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '#', '#', '#'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E']
])
print("Test 2 : Taille DFS :", len(lab2.res_dfs()[1]))
print("Test 2 : Taille BFS :", len(lab2.res_bfs()[1]))

#3. Labyrinthe impossible (doit afficher False)
lab3 = Labyrinthe([
    ['S', '.', '#'],
    ['.', '#', '#'],
    ['#', '#', 'E']
])
print("Test 3 : DFS :", lab3.res_dfs())
print("Test 3 : BFS :", lab3.res_bfs())

#4. Labyrinthe invalide
#Labyrinthe([['.', '.', 'E']])  #Sans S
#Labyrinthe([['S', '.', '.']])  #Sans E
#Labyrinthe([['S', '.'], ['E']]) #Pas rectangulaire
