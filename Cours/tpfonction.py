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

#Ex03:Ordre des KeyWords Arguments
#Result= Les amies salut
def créer_une_phrase(mot1,mot2,mot3):
 phrase= mot1.title() + ' '+ mot2.lower()+' '+mot3.lower()+'.'
 return(phrase)

phrase= créer_une_phrase(mot3='SaLuT',mot1='LES',mot2='Ami.e.s')
print(phrase)

#Ex04:Ordre d'exécution des instructions en Python
#Result= 5/10
print('Dehors de la fonction -1')

def casse_tête_suite(nombre2,nombre1):
 print('Inside the function - casse_tête2')
 print(nombre2)#10
 print(nombre1)#5

def casse_tête(nombre1,nombre2):
 print('Inside the function - casse_tête')
 casse_tête_suite(nombre1,nombre2)#5,10

print('Dehors de la fonction - 2')
casse_tête(nombre2=10,nombre1=5)

print('Dehors de la fonction - 3')

#Ex05: Se familiariser avec les erreurs de passsage d'arguments
#Tous les arguments nommés doivent venir après les arguments positionnels.
#2solutions possibles: 
                    #Soit tout passer comme arguments positionnels 
                    #Soit tout passer comme arguments nommés :

from helper import creer_une_phrase

#Erreur=creer_une_phrase(mot1="Hey", 'tout', 'le', 'monde')#Correction:Les arguments positionnels doivent être fournis avant les arguments nommés.

#Solution
result=creer_une_phrase("Hey","tout",'le','monde',)#Stocker dans une variable pour voir le print
print(result)

#Ex06: Erreurs de passage d'arguments
        #Explicaton: Les arguments positionnels doivent être fournis avant les arguments nommés.
                    #Chaque argument doit être fourni une seule fois.

#Erreur fournie
#SyntaxError: positional argument follows keyword argument
#creer_une_phrase('Hey','tout',mot3='le','monde')

#Correction ou solution
#Utilisation arguments positionnels uniquements ou nommés pour le tout
result1=creer_une_phrase('Hey','tout','le','monde') # ou creer_une_phrase(mot1="Hey", mot2="tout", mot3="le", mot4="monde")
print(result1)


#Ex07:Erreurs de passage d'arguments
#Missing 1 required positional argument: 'mot3'
#creer_une_phrase(mot1="Hello", mot2="World")

#Solution: Ajout d'un autre argument mot3
result2=creer_une_phrase(mot1="Hello", mot2="World",mot3='Bao')
print(result2)

#Ex08:Erreurs de passage d'arguments
#Missing 1 required positional argument: 'mot3'
creer_une_phrase(mot1="I", mot2="LOVE",mot4='PYTHON')


#Solution: insertion du mot3 en argument
result3=creer_une_phrase(mot1="I", mot2="LOVE",mot3='SOLUTION',mot4='PYTHON')
print(result3)