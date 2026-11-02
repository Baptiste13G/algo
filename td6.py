class MaillonRec:
    def __init__(self,val,suiv=None):
            self.__val=val
            self.__suiv=suiv
        
    def append(self,val):
        if self.__suiv is None:
            self.__suiv=MaillonRec(val)
        else:
            self.__suiv.append(val)

    def get(self,ind):
        if ind==0:
            return self.__val
        else:
            return self.__suiv.get(ind-1)
            
    def set(self,ind,val):
        if ind==0:
            self.__val=val
        else:
            self.__suiv.set(ind-1,val)
            
    def delete(self,ind):
        if ind ==1:
            self.__suiv=self.__suiv.__suiv
        else:
            self.__suiv.delete(ind-1)
            
    def insert(self,ind,val):
        if ind==1:
            self.__suiv=MaillonRec(val,self.__suiv)
        else:
            self.__suiv.insert(ind-1,val)
            
    def copy(self):
        m=MaillonRec(self.__val)
        if self.__suiv is not None:
            m.__suiv=self.__suiv.copy()
        return m
    
    def maximum(self, val=None):
        if val is None or self.__val > val:
            val = self.__val
        if self.__suiv is None:
            return val
        return self.__suiv.maximum(val)
    
    def maximum2(self):
        if self.__suiv is None:
            return self.__val
        max_suiv=self.__suiv.maximum2()
        if self.__val >max_suiv:
            return self.__val
        else:
            return max_suiv
    
    def construire(self,tab):
        if len(tab)>0:
            self.__suiv=MaillonRec(tab[0])
            self.__suiv.construire(tab[1:])
        else:
            self.__suiv=fin
        
    def supprimer_negatifs(self):
        if self.__suiv is not None:
            self.__suiv=self.__suiv.supprimer_negatifs()
        if self.__val<0:
            return self.__suiv
        
    def inserer_liste(self,tab,indice):
        if not tab:
            return
        
        if indice==1:
            self.__suiv=MaillonRec(tab[0],self.__suiv)
            self.__suiv.inserer_liste(tab[1:],1)
        else:
            if self.__suiv is None:
                raise IndexError("Indice d'insertion non valide.")
            
            self.__suiv.inserer_liste(tab,indice-1)        
        

class ListeChaineeRec:
    def __init__(self):
        self.__tete=None
        
    def est_vide(self):
        return self.__tete is None
    
    def append(self,val):
        if self.est_vide():
            self.__tete=MaillonRec(val)
        else:
            self.__tete.append(val)
            
    def get(self,ind):
        assert 0<= ind < self.len()
        return self.__tete.get(ind)
    
    def set(self,ind,val):
        assert 0<= ind < self.len()
        self.__tete.set(ind,val)
        
    def delete(self,ind):
        assert 0<= ind < self.len()
        if ind==0:
            self.__tete=self.__tete.suivant()
        else:
            self.__tete.delete(ind)
            
    def insert(self,ind,val):
        assert 0<= ind <= self.len()
        if ind==0:
            self.__tete=MaillonRec(val,self.__tete)
        else:
            self.__tete.insert(val,ind)
            
    def copy(self):
        l=ListeChaineeRec()
        if not self.est_vide():
            l.__tete=self.__tete.copy()
        return l
    
    def maximum(self):
        if not self.est_vide():
            return self.__tete.maximum()
        
    def construire(self,tab):
        if not tab:
            self.__tete=None
            return
        self.__tete=MaillonRec(tab[0])
        self.__tete.construire(tab[1:])
        
    def supprimer_negatifs(self):
        if not self.est_vide():
            self.__tete.supprimer_negatifs()
            
    def inserer_liste(self, tab, indice):
        if not (0 <= indice <= self.len()):
            raise IndexError("L'indice doit être vailde.")
        if not tab:
            return
        if indice == 0:
            self.__tete=MaillonRec(tab[0],self.__tete)
            self.__tete.construire(tab[1:],1)
        else:
            if self.__tete is None:
                raise IndexError("Indice d'insertion non valide.")
            self.__tete.inserer_liste(tab,indice)