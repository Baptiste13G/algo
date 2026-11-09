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
    
    def lesFeuilles(self): #dfs
        if self.estFeuille():
            return [self.__val]
        feuilles = []
        if self.aFG():
            feuilles += (self.__fg.lesFeuilles())
        if self.aFD():
            feuilles += (self.__fd.lesFeuilles())
        return feuilles
    
    def plusGrandeValeur(self):
        max_val = self.__val  
        if self.aFG():
            max_val = max(max_val, self.__fg.plusGrandeValeur()) #recherche / comparaison avec le sous-arbre gauche      
        if self.aFD():
            max_val = max(max_val, self.__fd.plusGrandeValeur()) #recherche / comparaison avec le sous-arbre droite 
        return max_val
    
    def hauteur(self):
        hg=0
        hd=0
        if self.aFG(): #On cherche dan sle sous-arbre gauche
            hg = self.__fg.hauteur() 
        if self.aFD(): #On cherche dan sle sous-arbre droite
            hd = self.__fd.hauteur()           
        return 1 + max(hg,hd) #On compare les deux 
    
    def toStrPrefixee(self):
        chaine=str(self.__val)+" ("
        if self.aFG():
            chaine+=self.__fg.toStrPrefixee()
        if self.aFD() and self.aFG():
            chaine+= ", "
        if self.aFD():
            chaine += self.__fd.toStrPrefixee()
        chaine+=")"
        return chaine
    
class ArbreBinaire:
    
    def __init__(self, racine=None):
        self.__racine = racine
        
    def est_vide(self):
        return self.__racine is None
      
    def cherche_dfs(self,val):
        """
        Retourne le premier sommet de valeur val, sinon None
        """
        if not self.est_vide():
            return self.__racine.chercher_dfs(val)
        return None
    
    def lesFeuilles(self): #dfs
        if self.est_vide() :
            return []
        return self.__racine.lesFeuilles()
    
    def plusGrandeValeur(self):
        if self.est_vide():
            return None
        return self.__racine.plusGrandeValeur()
    
    def hauteur(self):
        if self.est_vide():
            return 0
        return self.__racine.hauteur()
    
    def hauteur_bfs(self):
        if self.est_vide():
            return 0
        
        file = File()
        file.ajouter(self.__racine)
        
        nb=1
        hauteur=0
        while not file.est_vide():
            
            taille=nb
            hauteur+=1
            nb=0
            
            #On traite les sommets du niveau courant
            for i in range(taille):
                s=file.enlever()
                if s.aFG():
                    file.ajouter(s.fg())
                    nb+=1
                if s.aFD():
                    file.ajouter(s.fd())
                    nb+=1
        return hauteur
                
    
    def toStrPrefixee(self):
        if self.est_vide():
            return ""
        return self.__racine.toStrPrefixee()