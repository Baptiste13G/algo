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
        return self.__tete is None
    
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
            self.__tete=self.__tete.suivant()
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
            
    def contient(self,val):
        if self.est_vide():
            return False
        prec=self.__tete
        while prec is not None:
            if prec.__val==val:
                return True
            prec=prec.suivant()
        return False
    
    def moyenne(self):
        if self.est_vide():
            return 0
        prec=self.__tete
        moy=0
        n=0
        while prec is not None:
            moy+=prec.__val
            n+=1
            prec=prec.suivant()
        return moy / n
    
    def indice_minimum(self):
        if self.est_vide():
            return []
        prec=self.__tete
        mini=prec.__val
        ind=0
        n=[]
        while prec is not None:
            if prec.__val<mini:
                mini=prec.__val
                n=[ind]
            elif prec.__val==mini:
                n.append(ind)
            prec=prec.suivant()
            ind+=1
        return n
    
    def kieme_depuis_fin(self,ind):
        n=self.len()
        if ind >= n or ind<0:
            return None
        if self.est_vide():
            return None
        cpt=0
        for i in range(n-1,-1,-1):
            if cpt==ind:
                return self.get(i)
            cpt+=1
        
    def permute_tete_queue(self):
        if self.est_vide() or self.__tete.suivant() is None:
            return 
        prec=self.__tete
        tete=prec.__val
        while prec.suivant() is not None:
            prec=prec.suivant()
        queue=prec.__val
        prec.__val=tete
        self.__tete.__val=queue
        
    def premiere_repetition(self):
        if self.est_vide() or self.__tete.suivant() is None:
            return None
        prec=self.__tete
        tab=[]
        while prec is not None:
            if prec.__val not in tab:
                tab.append(prec.__val)
            else:
                return prec.__val
        return None
    
    def permute_pairs(self):
        prec = self.__tete
        while prec is not None and prec.suivant() is not None:
            suiv = prec.suivant()
            v = prec.__val
            prec.__val = suiv.__val
            suiv.__val = v
            prec = suiv.suivant()
        return None
            
    def diviser(self):
        lc1 = ListeChainee()
        lc2 = ListeChainee()
        prec = self.__tete
        i = 0
        while prec is not None:
            if i % 2 == 0:
                lc1.append(prec.__val)
            else:
                lc2.append(prec.__val)
            prec = prec.suivant()
            i += 1
        return lc1, lc2
    
    def diviser2(self):
        a=ListeChainee()
        prec=self.__tete
        
        