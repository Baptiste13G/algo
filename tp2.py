import math  
#Exercice 1

def somme_factorielles(n): #Compléxité linéaire car une boucle
    res=0
    for i in range(n+1):
        fac=math.factorial(i)
        res=res+fac
    print(res)

#somme_factorielles(6)

#Exercice 2

def premiere_repetition(tab): #Compléxité linéaire car une boucle ? (Je ne sais pas si le in tab2 change qqc)
    tab2=[]
    for i in tab:
        if i not in tab2:
            tab2.append(i)
        else:
            print(i)
            break

l = [1 , 2 , 3 , 5 , 7 , 5 , 2 , 12 , 1]
#premiere_repetition (l)

#Exercice 3

def affichage_diagonales(mat): #Compléxité de ...
    long=len(mat[0])
    for k in range(2*long-1):
        chaine=""
        for i in range(long): #Ou (max(0,k+1-long)),(min(k,long-1))
            for j in range(long):
                if i+j==k:
                    chaine+=str(mat[j][i])+' '
        print(chaine)


matr = [[1 , 2 , 3 , 4] ,[5 ,6 ,7 , 8] ,[9 ,10 ,11 ,12] ,[13 ,14 ,15 ,16]]
#affichage_diagonales(matr)

#Exercice 4

def intrus(tab): #complexité linéaire car 2 boucles mais pas imbriqués
    dic={}
    for i in tab:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for cle,valeur in dic.items():
        if valeur==1:
            print(cle)
            break

l2 = [1 , 2 , 3 , 5 , 7 , 5 , 2 , 1 , 3]
#intrus(l2)

#Exercice 5

def intervalles_est_dans_liste(tab,borne1,borne2): #Compléxité constante ?
    resp=True
    tab2=[]
    for i in tab:
        if i not in tab2 and borne1<i<borne2:
            tab2.append(i)
    test=borne2-borne1
    #print(test, len(tab2))
    if len(tab2)+1!=test:
        resp=False
    print(resp)

l3 = [4 , 1 , 2 , 3 , 5 , 7 , 5 , 2 , 1 , 3 , 6 , 9]

#intervalles_est_dans_liste(l3,1,12)
#intervalles_est_dans_liste(l3,2,5)

#Exercice 6

def triplet_avec_ordre(tab): #renvoie les positions des élt du triplet
    triplet=(-1,-1,-1)
    mini=min(tab)
    index=tab.index(mini)
    if index == len(tab):
        print(triplet)
    for i in range(index+1,len(tab)):
        for j in range(index+2,len(tab)):
            if tab[j]>tab[i]:
                triplet=(index,i,j)
                break
        if triplet!=(-1,-1,-1):
            break
    print(triplet)
 

l4 = [4 , 0 , 7 , 3 , 5 , 7 , 5 , 2 , 1 , 3 , 6 , 9]
#triplet_avec_ordre(l4)
l5 = [14 , 12 , 7 , 5 , 5 , 3 , 0]
#triplet_avec_ordre(l5)

#Exercice 7

def somme_maximale(tab): 
    meilleure_somme=tab[0]
    somme_courante=tab[0]
    for i in range(1,len(tab)):
        if somme_courante<0:
            somme_courante=tab[i]
        else:
            somme_courante=somme_courante+tab[i]
        if somme_courante>meilleure_somme:
            meilleure_somme=somme_courante
    print(meilleure_somme)

l6 = [-2 , 1 , -3 , 4 , -1 , 2 , 1 , -5 , 4]
#somme_maximale(l6) # 6

def affiche_spirale(mat): 
    haut=0
    bas=len(mat)-1
    gauche=0
    droite=len(mat[0])-1
    res=""
    while haut<=bas and gauche<=droite:
        for i in range(gauche,droite+1): #ligne du haut, vers la droite
            res=res+str(mat[haut][i])+' '
        haut=haut+1
        for i in range(haut,bas+1): #colonne de droite, vers le bas
            res=res+str(mat[i][droite])+' '
        droite=droite-1
        if haut<=bas:
            for i in range(droite,gauche-1,-1): #ligne du bas, vers la gauche
                res=res+str(mat[bas][i])+' '
            bas=bas-1
        if gauche<=droite:
            for i in range(bas,haut-1,-1): #colonne de gauche, vers le haut
                res=res+str(mat[i][gauche])+' '
            gauche=gauche+1
    print(res)

M = [[1 , 2 , 3 , 4] ,
     [5 , 6 , 7 , 8] ,
     [9 , 10 , 11 , 12]]
#affiche_spirale(M) # 1 2 3 4 8 12 11 10 9 5 6 7

def deplacer_zeros(tab): 
    j=0
    for i in range(len(tab)):
        if tab[i]!=0:
            tab[j],tab[i]=tab[i],tab[j] #échange en place
            j=j+1

l7 = [0 , 1 , 0 , 3 , 12]
#deplacer_zeros(l7)
#print(l7) # [1, 3, 12, 0, 0]