from pilefile import *

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
    
    def nb_sommets_dfs(self):
        """Sommet -> int
        retourne le nombre de sommets d’un arbre
        """
        if self.aFG() and self.aFD():
            return 1 + self.__fg.nb_sommets_dfs() + self.__fd.nb_sommets_dfs()
        elif self.aFG():
            return 1 + self.__fg.nb_sommets_dfs()
        elif self.aFD():
            return 1 + self.__fd.nb_sommets_dfs()
        else:
            return 1
        
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
    
