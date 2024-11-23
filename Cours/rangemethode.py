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