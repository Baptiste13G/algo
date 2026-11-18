from classes.pilefile import *
import tkinter as tk

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
            return False, [], len(visit), visit
        chemin = []
        courant = self.sortie
        while courant is not None:
            chemin.append(courant)
            courant = pred[courant]
        chemin.reverse()
        return True, chemin, len(visit), visit
    
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
            return False, [], len(visit), visit
        chemin = []
        courant = self.sortie
        while courant is not None:
            chemin.append(courant)
            courant = pred[courant]
        chemin.reverse()
        return True, chemin, len(visit), visit
    
    def afficher_chemin(self, chemin, symbole='*'):
        """Affiche une copie du labyrinthe avec le chemin tracé."""
        grille_copie = [ligne[:] for ligne in self.modele]
        for ligne, colonne in chemin:
            if grille_copie[ligne][colonne] != 'S' and grille_copie[ligne][colonne] != 'E':
                grille_copie[ligne][colonne] = symbole        
        for ligne in grille_copie:
            print(" ".join(ligne))
        
        
class Interface:
    def __init__(self, fenetre, labyrinthes):
        self.fenetre = fenetre
        self.fenetre.title("SAE Labyrinthe")
        self.labyrinthe = labyrinthes
        self.index_lab = 0
        
        cadre_boutons = tk.Frame(self.fenetre)
        cadre_boutons.pack(pady=10)
        
        tk.Button(cadre_boutons, text="Nouveau labyrinthe", command=self.nouveau_labyrinthe).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_boutons, text="Résoudre DFS", command=self.resoudre_dfs).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_boutons, text="Résoudre BFS", command=self.resoudre_bfs).pack(side=tk.LEFT, padx=5)
        tk.Button(cadre_boutons, text="Effacer", command=self.effacer).pack(side=tk.LEFT, padx=5)

        self.label_info = tk.Label(self.fenetre, text="Prêt.")
        self.label_info.pack(pady=5)

        self.canvas = tk.Canvas(self.fenetre, width=350, height=350, bg="white")
        self.canvas.pack(padx=10, pady=10)
        
        self.taille_case = 30
        self.lab = self.labyrinthe[self.index_lab]
        self.dessiner_grille()
        
    def dessiner_grille(self, visites=None, chemin=None):
        self.canvas.delete("all")
        largeur = self.lab.colonnes * self.taille_case
        hauteur = self.lab.lignes * self.taille_case
        self.canvas.config(width=largeur, height=hauteur)

        for i in range(self.lab.lignes):
            for j in range(self.lab.colonnes):
                case = self.lab.modele[i][j]
                if case == '#':
                    couleur = "#1C232A"
                elif case == 'S':
                    couleur = "#00FF0D"
                elif case == 'E':
                    couleur = "#FF0000"
                elif chemin is not None and (i, j) in chemin:
                    couleur = "yellow" #chemin
                elif visites is not None and (i, j) in visites:
                    couleur = "#76B2EF" #exploré
                else:
                    couleur = "white"

                x1 = j * self.taille_case
                y1 = i * self.taille_case
                x2 = x1 + self.taille_case
                y2 = y1 + self.taille_case

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="gray") 
        
    def effacer(self):
        self.dessiner_grille()
        self.label_info.config(text="Affichage effacé.")
        
    def nouveau_labyrinthe(self):
        self.index_lab = (self.index_lab + 1) % len(self.labyrinthe)
        self.lab = self.labyrinthe[self.index_lab]
        self.dessiner_grille()
        self.label_info.config(text=f"Labyrinthe {self.index_lab + 1} affiché.")
        
    def resoudre_bfs(self):
        trouve, chemin, nb_visites, visites = self.lab.res_bfs()
        if trouve:
            self.dessiner_grille(visites=visites, chemin=chemin)
            self.label_info.config(text=f"BFS : Solution trouvée ! Chemin : {len(chemin)} cases | Explorées : {nb_visites}")
        else:
            self.dessiner_grille(visites=visites)
            self.label_info.config(text=f"BFS : Aucune solution. Cases explorées : {nb_visites}")
            
    def resoudre_dfs(self):
        trouve, chemin, nb_visites, visites = self.lab.res_dfs()
        if trouve:
            self.dessiner_grille(visites=visites, chemin=chemin)
            self.label_info.config(text=f"DFS : Solution trouvée ! Chemin : {len(chemin)} cases | Explorées : {nb_visites}")
        else:
            self.dessiner_grille(visites=visites)
            self.label_info.config(text=f"DFS : Aucune solution... Cases explorées : {nb_visites}")
    
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

# 4. Grand labyrinthe ouvert 12x15 (montre très bien la différence entre DFS qui serpente et BFS qui s'étale)
lab4 = Labyrinthe([
    ['S', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', 'E']
])

# 5. Labyrinthe 10x10 avec de nombreux culs-de-sac
lab5 = Labyrinthe([
    ['S', '.', '#', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '#', '.', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '#', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '.', '#', '#', '#', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '#', '#', '#', '.', '.', 'E']
])

# 6. Grand labyrinthe impossible (chemin bloqué juste avant la sortie)
lab6 = Labyrinthe([
    ['S', '.', '.', '#', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '#', '#', 'E']
])

#4. Labyrinthe invalide
#Labyrinthe([['.', '.', 'E']])  #Sans S
#Labyrinthe([['S', '.', '.']])  #Sans E
#Labyrinthe([['S', '.'], ['E']]) #Pas rectangulaire

racine = tk.Tk()
app = Interface(racine, [lab1, lab2, lab3, lab4, lab5, lab6])
racine.mainloop()