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
            self.__suiv.get(ind-1)
            
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
    
    def contient(self, val):
        if self.__val==val:
            return True
        if self.__suiv is None:
            return False
        self.__suiv.contient(val)
        
    def indice_premiere_occcurence(self,val,n=0):
        if self.__val==val:
            return n
        if self.__suiv is None:
            return None
        return self.__suiv.indice_premiere_occcurence(val,n+1)
    
    def indices_occurences(self,val,tab=None,n=0):
        if tab is None:
            tab=[]
        if self.__val==val:
            tab.append(n)
        if self.__suiv is None:
            return tab
        return self.__suiv.indices_occurences(val,tab,n+1)
    
    def supprimer_occurences_valeur(self, val):
        if self.__suiv is None:
            return
        if self.__suiv.__val == val:
            self.__suiv = self.__suiv.__suiv
            self.supprimer_occurences_valeur(val)
        else:
            self.__suiv.supprimer_occurences_valeur(val)
            
    def est_triee(self):
        if self.__suiv is None:
            return True
        if self.__val>self.__suiv.__val:
            return False
        return self.__suiv.est_triee()
    
    def moyenne(self, n=1, cpt=0):
        cpt += self.__val
        if self.__suiv is None:
            return cpt/n
        return self.__suiv.moyenne(n+1, cpt)
    
    def indices_minimum(self,tab=None,n=0,val=None):
        if tab is None:
            tab=[n]
        if val is None:
            val=self.__val
        if self.__val<val:
            val=self.__val
            tab=[n]
        if self.__val == val:
            if n not in tab:
                tab.append(n)
        if self.__suiv is None:
            return tab
        return self.__suiv.indices_minimum(tab,n+1,val)
    
    def premiere_repetition(self,tab=None):
        if tab is None:
            tab=[]
        if self.__val not in tab:
            tab.append(self.__val)
        else:
            return self.__val
        if self.__suiv is None:
            return None
        return self.__suiv.premiere_repetition(tab)
        

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
    
    def contient(self, val):
        if self.est_vide():
            return False
        return self.__tete.contient(val)
    
    def indice_premiere_occurence(self,val):
        if self.est_vide():
            return None
        return self.__tete.indice_premiere_occurence(val)
    
    def indices_occurences(self,val):
        if self.est_vide():
            return []
        return self.__tete.indices_occurences(val)
    
    def supprimer_occurences_valeur(self, val):
        if self.est_vide():
            return 
        if self.__tete.__val==val:
            self.__tete=self.__tete.__suiv
            return self.supprimer_occurences_valeur(val)
        return self.__tete.supprimer_occurences_valeur(val)
    
    def est_triee(self):
        if self.est_vide():
            return True
        return self.__tete.est_triee()
    
    def moyenne(self):
        if self.est_vide():
            return None
        return self.__tete.moyenne()
    
    def indices_minimum(self):
        if self.est_vide():
            return []
        return self.__tete.indices_minimum()
    
    def premiere_repetition(self):
        if self.est_vide():
            return None
        return self.__tete.premiere_repetition()
    
        