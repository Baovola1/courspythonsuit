#Création liste des multiples de 3 contenus entre 10 et 100
nbr = 10

liste = []
while nbr <= 100:
   if nbr % 3 == 0:
    liste.append(nbr) 
   nbr=nbr+1

print(liste)
