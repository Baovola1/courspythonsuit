#Règle de syntaxe sur la fonction en python
def nom_de_variable():
    print('Hello world')

nom_de_variable()

#Ici, on importe la fonction qui est dans le fichier helper.py
from helper import afficher_aide
import sys

_,*arguments = sys.argv

if len(arguments)<1: 
    print('Erreur: pas d\'argument fournis:\n')
    afficher_aide()
    exit()

