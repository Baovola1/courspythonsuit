#Récupérer une fonction dans un autre fichier
from helper import dire_bonjour

def dire_bonjour_deux_fois():
    dire_bonjour()
    dire_bonjour()

dire_bonjour_deux_fois()

##RETOURNER des valeurs avec les fonctions en Python
def ma_fonction():
    print('Hey')
    return 'VALEUR DE RETOUR'

print(ma_fonction())