def tri_shaker(l):
    debut = 0
    fin = len(l) - 1
    echange = True
    while echange:
        echange = False
        for i in range(debut, fin):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                echange = True
        fin -= 1
        for i in range(fin, debut, -1):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
                echange = True
        debut += 1
        


def tri_peigne(l,k):
    n = len(l)
    est_triee = False
    while not est_triee:
        if k<=1:
            k=1
            est_triee=True
        else:
            est_triee=False
        i=0
        while i+k<n:
            if l[i]>l[i+k]:
                l[i],l[i+k]=l[i+k],l[i]
                est_triee=False
            i+=1
        k-=1

def fusionner_r(a,b,c=None):
    if c==None:
        c=[]
    if len(a)==0:
        c.extend(b)
        return c
    if len(b)==0:
        c.extend(a)
        return c
    if a[0]<=b[0]:
        c.append(a.pop(0))
        return fusionner_r(a,b,c)
    else:
        c.append(b.pop(0))
        return fusionner_r(a,b,c)
    
def fusion_r2(a,b):
    if a==[]:
        return b
    if b==[]:
        return a
    if a[0]<=b[0]:
        return [a[0]]+fusion_r2(a[1:],b)
    else:
        return [b[0]]+fusion_r2(a,b[1:])

def tri_a_bulles_r(l,n=None):
    if n is None:
        n=len(l)
    if n<=1:
        return l
    echange = False
    for i in range(n-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            echange = True
        if not echange:
            return l
        return tri_a_bulles_r(l,n-1)

tab=[5,7,2,3,1,1,10]


def sous_liste(l): #On cherche une sous liste d'elt contigu dont le res = 0
    for i in range(len(l)-1):
        if l[i]==0:
            return True
        else:
            res=0
            for j in range(i,len(l)-1):
                res+=l[j]
                if res==0:
                    return True
    return False #Compléxité n**2
            
def sous_liste2(l): #Compléxité n
    dic={}
    somme=0
    for i in range(len(l)):
        somme+=l[i]
        if somme not in dic.keys():
            dic[somme]=1
        else:
            dic[somme]+=1  
    for valeur in dic.values():
        if valeur >1:
            return True
    return False

print(sous_liste2(tab))
        
        
        
    
    
def tri_radix(l):
    pass