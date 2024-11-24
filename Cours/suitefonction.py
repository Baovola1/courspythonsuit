#Récupérer une fonction dans un autre fichier
from helper import dire_bonjour

def dire_bonjour_deux_fois():
    dire_bonjour()
    dire_bonjour()

dire_bonjour_deux_fois()

##RETOURNER des valeurs avec les fonctions en Python
def ma_fonction():
    print('Hey')
    return 'ON EST DANS LE RETURN'

print(ma_fonction())

#Plus d'explication sur le return
def ma_fonction_avec():
    print('Hey avec')
    return 'AVEC VALEUR DE RETOUR'

def ma_fonction_sans():
    print('Hey sans')#Ici sans valeur retourné, on a un result 'None'

avec = ma_fonction_avec()
sans = ma_fonction_sans()

print(avec)
print(sans)

#Les valeurs qu'on peut retourner:nbr,chaine de caractère,fonction,tuples, listes
def fonction():
    return 1

print(fonction())

def fonction1():
    def function_interne():
        print('Hello from the inside')
    
    return function_interne

nom_externe = fonction1()

nom_externe()