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
            m=m.suivant
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