#Chercher le nombre plus petit dans la liste
#1)Récupérer les arguments depuis la ligne de commande
import sys
_,*liste = sys.argv

if not liste:
    liste=['4','7','-1.1','6.2',-10]
    print('DEBUG, une lsite est forunie par défaut')
    
#2)a-Convertir les str en float
for i in range(len(liste)):
    liste[i]= float(liste[i])#liste[i] fait référence à l'élément de la liste situé à l'indice i.

print('\nAprès type-cast')
print(liste)

#2)b-Autre alternative
#for i, nombre in enumerate(liste):
#   liste[i]= float(nombre)
    
print(liste)

#3)Rechercher le minimum 
minimum = liste[0]#Ici, on initialise la variable de recherche

for nombre in liste:
    if nombre<minimum:
        minimum = nombre

#4)Afficher le result via l'utilisation du built-in min())
print('Nous avons trouvé le minimum:', minimum)
print('Le builtin min() a trouvé:', min(liste))
