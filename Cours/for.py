#Utilisation de la boucle FOR(Sert à parcourir une collection ou examiner 1 à 1 les éléments)
iterable = ["Hello","Bonjour","Welcome"]

iterator = iter(iterable)#Ici, on itère la liste

objet = next(iterator)#next(iterator)=> permet de chercher l'élément suivant
print(objet)

objet = next(iterator)
print(objet)

objet = next(iterator)
print(objet)

#Les bonnes pratiques pour travailler avec la boucle FOR
factures = ['Fac.1','Fac.2','Fac.3','Fac.4']

for each in factures:
    print(each)
#utilisation itérator
factures = ['Fac.1','Fac.2','Fac.3','Fac.4']
 
for compteur, facture in enumerate(factures):
    print(compteur,facture)

#autre syntaxe
for i,facture in enumerate(factures):
    print(i,facture)