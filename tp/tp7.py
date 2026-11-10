from classes.pilefile import *

class Sommet:
    def __init__(self, val, fg=None, fd=None):
        self.__val = val
        self.__fg = fg #fils gauche
        self.__fd = fd #fils droite
    
    def get(self):
        return self.__val
    
    def fd(self):
        return self.__fd

    def fg(self):
        return self.__fg

    def aFG(self):
        return self.__fg != None

    def aFD(self):
        return self.__fd != None

    def estFeuille(self):
        return self.__fg == None and self.__fd == None
    
    def chercher_dfs(self,val):
        """
        Retourne le premier sommet de valeur val, sinon None
        """
        if self.__val == val:
            return self
        if self.aFG():
            sommet=self.__fg.chercher_dfs(val)
            if sommet is not None:
                return sommet
        if self.aFD():
            sommet=self.__fd.chercher_dfs(val)
            if sommet is not None:
                return sommet
        return None
    
    """def nb_sommets_dfs(self):
        Sommet -> int
        retourne le nombre de sommets d’un arbre
        
        if self.aFG() and self.aFD():
            return 1 + self.__fg.nb_sommets_dfs() + self.__fd.nb_sommets_dfs()
        elif self.aFG():
            return 1 + self.__fg.nb_sommets_dfs()
        elif self.aFD():
            return 1 + self.__fd.nb_sommets_dfs()
        else:
            return 1"""
        
    def maximum(self):
        if self.estFeuille():
            return self.__val
        max1,max2 = self.get(),self.get()
        if self.aFG():
            max1 = self.__fg.maximum()
        else:
            max1 = self.__val
        if self.aFD():
            max2 = self.__fd.maximum()
        else:
            max2 = self.__val
        return max(self.__val,max1,max2)
    
    def est_dans_arbre_dfs(self, val):
        if self.__val == val:
            return True
        if self.aFG() and self.__fg.est_dans_arbre_dfs(val):
            return True
        if self.aFD() and self.__fd.est_dans_arbre_dfs(val):
            return True
        return False
    
    def nb_sommets_dfs(self):
        if self.aFD() and self.aFG():
            return 1 + self.__fd.nb_sommets_dfs() + self.__fg.nb_sommets_dfs
        if self.aFG():
            return 1 + self.__fg.nb_sommets_dfs()
        if self.aFD():
            return 1 + self.__fd.nb_sommets_dfs()
        return 1
    
    def lister_valeurs(self):
            """Retourne la liste de toutes les valeurs de l'arbre en DFS."""
            tab = [self.__val]
            if self.aFG():
                tab.extend(self.__fg.lister_valeurs())
            if self.aFD():
                tab.extend(self.__fd.lister_valeurs())
            return tab

    def deuxieme_plus_grand_dfs(self):
        valeurs_uniques = sorted(set(self.lister_valeurs())) #enleve les doublons et tri
        if len(valeurs_uniques) < 2:
            return None
        return valeurs_uniques[-2]
    
    def un_fils_dfs(self,tab=None):
        if tab is None:
            tab = []
        if self.aFG() ^ self.aFD():
            tab.append(self.__val)
        if self.aFG():
            self.__fg.un_fils_dfs(tab)
        if self.aFD():
            self.__fd.un_fils_dfs(tab)
        return tab
    
    def internes_dfs(self, tab=None):
        if tab is None:
            tab=[]
        if self.aFG() or self.aFD():
            tab.append(self.__val)
        if self.aFG():
            self.__fg.internes_dfs(tab)
        if self.aFD():
            self.__fd.internes_dfs(tab)
        return tab
    
    def feuilles_negatives_dfs(self, tab=None):
        if tab is None:
            tab=[]
        if self.estFeuille() and self.__val<0:
            tab.append(self.__val)
        if self.aFG():
            self.__fg.feuilles_negatives_dfs(tab)
        if self.aFD():
            self.__fd.feuilles_negatives_dfs(tab)
        return tab
    
    def sommets_profondeur_sup_k_dfs(self, k, profondeur=0, tab=None):
        if tab is None:
            tab = []
        if profondeur > k:
            tab.append(self.__val)
        if self.aFG():
            self.__fg.sommets_profondeur_sup_k_dfs(k, profondeur + 1, tab)
        if self.aFD():
            self.__fd.sommets_profondeur_sup_k_dfs(k, profondeur + 1, tab)
        return tab

class ArbreBinaire:
    
    def __init__(self, racine=None):
        self.__racine = racine
        
    def est_vide(self):      
        return self.__racine is None
    
    def maximum_BFS(self):
        """ArbreBinaire -> float
        retourne la valeur maximum dans un arbre binaire"""
        assert self.__racine is not None
        f = File()
        f.ajouter(self.__racine)
        maxi = self.__racine.get()
        while not f.est_vide():
            sommet = f.enlever()
            if sommet.get() > maxi:
                maxi = sommet.get()
            if sommet.aFG():
                f.ajouter(sommet.fg())
            if sommet.aFD():
                f.ajouter(sommet.fd())
        return maxi
    
    def cherche_dfs(self,val):
        if not self.est_vide():
            return self.__racine.chercher_dfs(val)
        return None
    
    def cherche_bfs(self, valeur):
        """Retourne le noeud de valeur valeur, sinon None"""
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.enlever()
                if sommet.get() == valeur:
                    return sommet
                if sommet.fg() != None:
                    f.ajouter(sommet.fg())
                if sommet.fd() != None:
                    f.ajouter(sommet.fd())
        return None
    
    def nb_sommets_bfs(self) :
        """ArbreBinaire -> int
        retourne le nombre de sommets d’un arbre
        """
        cpt = 0
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.enlever()
                cpt += 1
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
        return cpt
    
    
    def nb_sommets_dfs(self):
        """ArbreBinaire -> int
        retourne le nombre de sommets d’un arbre
        """
        if self.__racine != None:
            return self.__racine.nb_sommets_dfs()
        return 0
    
    def est_dans_arbre_dfs(self, val):
        if self.est_vide():
            return False
        return self.__racine.est_dans_arbre_dfs(val)
    
    def est_dans_arbre_bfs(self, val):
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.enlever()
                if sommet.get() == val:
                    return True
                if sommet.fg() != None:
                    f.ajouter(sommet.fg())
                if sommet.fd() != None:
                    f.ajouter(sommet.fd())
        return False
    
    def nb_sommets_dfs(self):
        if self.est_vide():
            return 0
        return self.__racine.nb_sommets_dfs()
    
    def nb_sommets_bfs(self):
        cpt = 0
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.enlever()
                cpt += 1
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
        return cpt
    
    def deuxieme_plus_grand_dfs(self):
        if self.est_vide():
            return None
        return self.__racine.deuxieme_plus_grand_dfs()
                
    def deuxieme_plus_grand_bfs(self):
        assert self.__racine is not None
        f = File()
        f.ajouter(self.__racine)
        maxi = self.__racine.get()
        maxi2=maxi
        while not f.est_vide():
            sommet = f.enlever()
            if sommet.get() > maxi:
                maxi2=maxi
                maxi = sommet.get()
            if sommet.aFG():
                f.ajouter(sommet.fg())
            if sommet.aFD():
                f.ajouter(sommet.fd())
        return maxi2

    def un_fils_bfs(self):
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            tab=[]
            while not f.est_vide():
                sommet=f.enlever()
                if sommet.aFD() ^ sommet.aFG():
                    tab.append(sommet)
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
        return tab
    
    def un_fils_dfs(self):
        if self.est_vide():
            return []
        return self.__racine.un_fils_dfs()
                
    def internes_bfs(self):
        tab=[]
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet=f.enlever()
                if sommet.aFD() or sommet.aFG():
                    tab.append(sommet)
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
        return tab
    
    def internes_dfs(self):
        if self.est_vide():
            return []
        return self.__racine.internes_dfs()
               
    def feuilles_negatives_bfs(self):
        tab=[]
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet=f.enlever()
                if sommet.estFeuille() and sommet.get()<0:
                    tab.append(sommet)
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
            return tab
        
    def feuilles_negatives_dfs(self):
        if self.est_vide():
            return []
        return self.__racine.feuilles_negatives_dfs()
    
    def sommets_profondeur_sup_k_bfs(self, k):
            tab = []
            if self.__racine is not None:
                f = File()
                f.ajouter((self.__racine, 0))
                while not f.est_vide():
                    sommet, profondeur = f.enlever()
                    if profondeur > k:
                        tab.append(sommet.get())
                    if sommet.aFG():
                        f.ajouter((sommet.fg(), profondeur + 1))
                    if sommet.aFD():
                        f.ajouter((sommet.fd(), profondeur + 1))       
            return tab
        
    def sommets_profondeur_sup_k_dfs(self,k):
        if self.est_vide():
            return []
        return self.__racine.sommets_profondeur_sup_k_dfs(k)