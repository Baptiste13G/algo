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