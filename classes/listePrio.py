"""

Tas = arbre binaire parfait, tout les nieaux remplis sauf éventuellement le dernier;
Chaque sommet est tassé : chaque sommet est égal à ses deux fils. #pas sur de ça

"""

class Tas:
    def __init__(self, tas=[]):
        self.__tas = tas
        self.__nTas=len(tas)
        
    def maximum(self):
        assert len(self.__tas)>0
        return self.__tas[0]
    
    def ajouter(self, v):
        i = self.__nTas
        self.__tas.append(v)
        self.__nTas +=1
        while i > 0 and self.__tas[(i-1)/2]<=v:
            self.__tas[i]=self.__tas[(i-1)//2]
            i=(i-1)//2
        self.__tas[i]=v
        
    def suppression(self):
        self.__tas[0] = self.__tas[self.__nTas-1]
        self.__nTas = self.__nTas - 1
        del self.__tas[self.__nTas]
        v = self.__tas[0]
        i = 0
        fini = False
        while not fini and (2*i + 1 < self.__nTas):
            j = 2*i +1
            if(j+1 < self.__nTas and self.__tas[j+1] > self.__tas[]):
                j+=1
            if(v >= self.__tas[j]):
                fini = True
            else:
                self.__tas[i] = self.__tas[j]
                i=j
        self.__tas[j] = v
        
def triParTas(liste):
    n=len(liste)
    t=Tas()
    liste_triee=[]
    for i in range(n):
        v = t.maximum()
        t.supprimer()
        liste_triee.append(v)
    return liste_triee
