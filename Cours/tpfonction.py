#Ex01: Importer et Appeler des fonctions
from helper import dire_bonjour

def dire_bonjour_trois_fois():
 dire_bonjour()
 dire_bonjour()
 dire_bonjour()

dire_bonjour_trois_fois()

#Ex02:Appelez des fonctions avec plusieurs paramètres
from helper import dire_qlqchose_X_fois

## Appel de la fonction pour dire "Salut", 12 fois
# Utilisation du style positionel pour passer les arguments
dire_qlqchose_X_fois("Salut",12)

# Appel de la fonction pour dire "Hey", 5 fois 
# Utilisation du style positionel pour passer le première argument, et le style keyword pour passer l'argument X
dire_qlqchose_X_fois("Hey",x=5) 
 
# Appele de la fonction pour dire "Hello World", 1 fois
# Utilisez le style keyword pour passer les deux arguments
dire_qlqchose_X_fois(qlqchose='Hello world', x=1)    