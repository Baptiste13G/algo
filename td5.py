class Maillon:
    def __init__(self,val,suiv=None):
        self.__val=val
        self.__suiv=suiv
        
    def get(self):
        return self.__val
    
    def suivant(self):
        return self.__suiv
    
    def set_suiv(self,m): #m est un autre maillon
        self.__suiv=m
        
    def __str__(self):
        mess=str(self.__val)
        if self.__suiv is not None:
            mess += ", "
        return mess
        
class ListeChainee:
    def __init__(self):
        self.__tete=None
        
    def est_vide(self):
        pass
    
    def __str__(self):
        mess="["
        prec = self.__tete
        while prec is not None:
            mess+=prec.__str__()
            prec=prec.suivant()
        mess+="]"
        return mess
    
    def len(self):
        nb=0
        prec=self.__tete
        while prec is not None:
            prec=prec.suivant()
            nb+=1
        return nb
    
    def get(self,ind): #renvoie l'élément à l'indice ind
        assert 0 <= ind <= self.len()
        cpt=0
        m=self.__tete
        while cpt<ind :
            m=m.suivant()
            cpt+=1
        return m.get()
    
    def append(self,val):
        if self.est_vide():
            self.__tete = Maillon(val)
        else:
            prec=self.__tete #prec : maillon auquel on va raccrocher le nouveau maillon 
            while prec.suivant() is not None:
                prec=prec.suivant()
            prec.set_suiv(Maillon(val))
            
    def delete(self, ind):
        assert 0 <= ind < self.len()
        if ind==0:
            self.tete=self.__tete.suivant()
        else:
            prec=self.__tete
            for i in range(ind-1):
                prec=prec.suivant()
            prec.set_suiv(prec.suivant().suivant())
    
    def insert(self,val,ind):
        assert 0 <= ind <= self.len()
        if ind ==0:
            self.__tete=Maillon(val,self.__tete)
        else:
            prec = self.__tete
            for i in range(ind-1):
                prec=prec.suivant()
            prec.set_suiv(Maillon(val,prec.suivant()))
            
    def ajoute_maillon(self,m):
        if self.est_vide():
            self.__tete=m
        else:
            prec=self.__tete
            while prec.suivant() is not None:
                prec=prec.suivant()
            prec.set_suiv(m)
            
    def supprime_maillon(self,m):
        if self.est_vide():
            return
        if self.__tete==m:
            self.__tete=self.__tete.suivant()
            return
        prec=self.__tete
        while prec.suivant() is not None and prec.suivant() !=m:
            prec=prec.suivant()
        if prec.suivant() == m:
            prec.set_suiv(m.suivant())
            m.set_suiv(None)
        
    """def ajoute_liste(self,l): #O(n**2)
        for i in l:
            self.append(i)"""
    
    def ajoute_liste(self,l): #Compléxité O(n)
        for i in range(len(l)):
            if i == 0:
                self.__tete=Maillon(l[i])
                courant=self.__tete
            else:
                courant.set_suiv(Maillon(l[i]))
                courant=courant.suivant()
            
    def min_max(self):
        if self.est_vide():
            return (None, None)
        else:
            prec=self.__tete
            mini = prec.__val
            maxi = prec.__val
            while prec.suivant() is not None:
                prec=prec.suivant()
                if prec.__val>maxi:
                    maxi=prec.__val
                if prec.__val<mini:
                    mini=prec.__val
            return (mini, maxi)


    def supprimer_negatifs(self):
        if self.est_vide():
            return None
        else:              
            prec=self.__tete
            for i in range(self.len()):
                if prec.__val<0:
                    self.delete(i)
                prec=prec.suivant()
    
    def supprimer_doublons(self):
        tab=[]
        prec=self.__tete
        for i in range(self.len()):
            if prec.__val not in tab:
                tab.append(prec.__val)
            else:
                self.delete(i)
            prec=prec.suivant()
    
    def supprimer_n_apres_m(self,n,m): #Supprime les n premiers éléments après les m premiers
        if n==0:
            return self
        for i in range(m-1,self.len()):
            while n>0:
                self.delete(i)
                n=n-1
        
    def inverser(self):
        tab=[]
        prec=self.__tete
        for i in range(self.len()):
            tab.append(prec.__val)
            prec=prec.suivant()
        tab.reverse()
        for i in range(self.len()):
            self.delete(i)
        self.ajoute_liste(tab)
        
    def fusionner(self,lc2):
        j=0
        for i in range(self.len()):
            pass