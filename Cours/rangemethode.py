#Utilisation de la fonction range() avec une boucle FOR

borne_fin = 3
#Ici, on compte de 0 à 2, le 3 sera exclu
for i in range(borne_fin):
    print(i)

for i in range(4):
    print(i)

for i in range(1,3):
    print(i)

#IMPORTANT: Comment changer un objet de type range() en liste?
objet = range(10)

liste = list(objet)

print(liste)

#Autre méthode:
liste_de_nombres = list(range(0,100))
print(liste_de_nombres)

#Utilisation liste décroissante(mettre dans l'ordre décroissante)
for i in reversed(range(2,10+1)):
    print(i)
#Comment sauter des nombres(Ici on veut tous les brs paires=> via l'utilisation de 2 à la fin)
for i in range (0,10,2):
    print(i)

#Utilisation de "continue()" => Permet de passer à l'itération suivante
#toujours utilisé avec une condition
for i in range(0,100):
    if i % 2 != 0:
        continue
    print(i)
    
