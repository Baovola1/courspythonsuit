#Utilisation de la boucle FOR(Sert à parcourir une collection ou examiner 1 à 1 les éléments)
iterable = ["Hello","Bonjour","Welcome"]

iterator = iter(iterable)#Ici, on itère la liste

objet = next(iterator)#next(iterator)=> permet de chercher l'élément suivant
print(objet)

objet = next(iterator)
print(objet)

objet = next(iterator)
print(objet)