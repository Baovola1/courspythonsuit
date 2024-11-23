#Utilisation de la boucle FOR(Sert à parcourir une collection ou examiner 1 à 1 les éléments)

#Les bonnes pratiques pour travailler avec la boucle FOR
factures = ['Fac.1','Fac.2','Fac.3','Fac.4']

for each in factures:
    print(each)
#utilisation itérator=> on peut parcourir qu'une seule collection
factures = ['Fac.1','Fac.2','Fac.3','Fac.4']
 
for compteur, facture in enumerate(factures):
    print(compteur,facture)

#autre syntaxe
for i,facture in enumerate(factures):
    print(i,facture)
#UTILISATION de zip()=> sert à parcourir 2 ou plsrs collections
symboles = ['+','-','*','/']
opérations=['addition','soustraction','multiplication','division']

for objet in zip(symboles,opérations):
    print(type(objet),objet)

#autre syntaxe
template = 'Le symbole de l\'opération {op} est {sym}'
for symbole, opération in zip(symboles,opérations):
    message = template.format(op=opération, sym=symbole)
    print(message)

#Utilisation reversed()avec une liste
A=['a','b','c','d']

for each in reversed(A):
    print(each)
