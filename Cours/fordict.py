#Utilisation de la boucle FOR dans une dictionnaire ou dict
opérations = {'addition': '+',
              'soustraction': '-',
              'multiplication': '*',
              'division': '/',}

msg= 'L\'opération {o} est définie par le symbole {s}'

#items() => permet de récupérer les éléments 1 par 1 ie clés et valeurs en mm temps
#Pour parcourir les clés et valeurs=> on utilise la méthode items()
for k,v in opérations.items():
    print(k,v)

#Pour parcourir toutes les valeurs=> on utilise la méthode values()
for v in opérations.values():
    print(v)

#Pour itérer toutes les clés=> on utilise la méthode keys()
for k in opérations.keys():
    print(k)