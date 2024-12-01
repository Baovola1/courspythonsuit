#Ajouter-modifier-supprimer-lecture(accès)

#1)Ajout(à la création)
dico ={'clé1':100,
       'clé2':[40,20],
       'clé3':'Hello',
       'clé5':0}


#1-a)Ajout nouvelle clé
dico['clé4']='Im a new'


#2)Lecture(accès)
print(dico['clé1'])

#3)Modifier
dico['que je veux']='SALUT :)'
dico['que je veux']='VALEUR'

print(dico)

#4)Supprimer
del dico['que je veux']
print(dico)

#5)Builtin 'in' et len()
    #5)a=> utilisation in()
dico ={'a':0, 'b':1}

print('a' in dico)
    #5)b=> utilisation len()(Ici, on compte uniquement les clés)
print(len(dico))

#6)Accès sécurisé pour les dico: get()/pop()
    #6-a-Cas utilisation get()
dico ={'c':2, 'd':4}
result=dico.get('c')
print(result)
    #Ici, clé n'existe pas sans le défault
o= dico.get('e')
print(o)#result=>none
    #Ici, clé n'existe pas avec définition valeur de retour par défaut en retour
o1= dico.get('e',-1)
print(o1)
    #6-b-Cas utilisation pop()
r= dico.pop('d')
print(r)
print(dico)
    #RQ: Avec pop, il faut utiliser une valeur par défaut pour debug du code si la clé n'existe pas
r1= dico.pop('f',-1)
print(r1)

#7-A connaitre absolument: items(), keys(), values()
    #7-a)Utilisation items()
dictio={'j':7,'k':14}
resultat = dictio.items()
#RQ:TOUJOURS CONVERTIR resultat EN Liste
print(list(resultat))
    #7-b)Utilisation keys()
resultat1 = dictio.keys()
print(list(resultat1))
    #7-c)Utilisation values()
resultat2 = dictio.values()
print(list(resultat2))
