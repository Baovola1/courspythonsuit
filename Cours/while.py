#Création liste des multiples de 3 contenus entre 10 et 100
nbr = 10

liste = []
while nbr <= 100:
   if nbr % 3 == 0:
    liste.append(nbr) 
   nbr=nbr+1

print(liste)

#IndexError et boucles while
liste=['A','B','C','D','E','F','G']

index = 0
while index < len(liste):
    print(liste[index])
    index = index + 1
    
#Indexing Négatif et boucle While   
liste=['A','B','C','D','E','F','G']

index = -1
while index > -(len(liste)+1):
    print(liste[index])
    index = index -1