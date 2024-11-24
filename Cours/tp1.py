#Exo1: Factorisation avec des boucles FOR
collection = ["A","B","C"]

for alphabet in collection:
    print(alphabet.lower())

#Exo2:Bien choisir ses noms de variables
nombre_pairs=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

for nombre_pair in nombre_pairs:
    carré = nombre_pair ** 2
    print(carré)

#Exo3:Utilisation de la fonction built-in enumerate()plutôt que de créer des compteurs
multiples_de_trois=list(range(0,100,3))


for i,each in enumerate(multiples_de_trois):
    # Ci-dessous, {i + 1} car i commence à zéro et on veut compter à partir de 1
    print(f'Le multiple de trois n°{i+1} est {each}')

#Autre solution de l'exo3 
multiples_de_trois=list(range(0,100,3))


for each in enumerate(multiples_de_trois):
    print(each)

#Ex04: Utilisation de zip() pour itérer en parallèle sur deux listes distinctes.
nombres= list(range(1,20))
racines_carrées = []
# Cette boucle nous permet de créer une liste des racines carrés des nombre de 1 à 19
for nombre in nombres:
    racine = nombre ** 0.5
    racines_carrées.append(racine)
#Ici on remplace la deuxième boucle par une plus succinte en utilisant zip(...)
for nombre,racine in zip(nombres,racines_carrées,):
    
    print(f'La racine carrée du nombre {nombre} est {racine}')

#Exo5:Utilisation de reversed() pour inerser l'ordre de lecture d'une liste
# Ici on Affiche les nombres de 1 à 30 en ordre décroissant (commencer par 30)
un_à_trente=list(range(0,30+1))

#Cas d'utilisation pour obtenir les ndrs positifs inversés
for i in reversed(un_à_trente):
    print(i)
#Cas d'utilisation pour obtenir un nbr négatif
for nombre in reversed(un_à_trente):
    negatif=-nombre# Conversion en nbr négatif
    print(negatif)

#Exo6:Utilisation .items() pour itérer sur les éléments d'un dict
menu={'Poisson':100,
      'Végé':40,
      'Pizza':70}

for plat,prix in menu.items():
    print(f'Le cout du {plat} est {prix}$')

#Exo7:Utilisation de "continue" pour ignorer des cas dans une boucle
# Ici on cherche tous les fichiers .mp3
mes_fichiers= ['musique_rock.mp3',
               'fast_and_furious_18.MP4',
                'twilight_4_le_retour.MP4', 
                'game_of_thrones_S1E1.mp4',
                'musique_zumba.MP3', 
                'musique_techno.mp3',
                'avengers_5.mp4', 
                'podcast_cool.MP3']

for fichier in mes_fichiers:
    #Explication: Le [-1] permet de récupérer le dernier élément de la liste créée par split('.').
    #Dans le contexte des noms de fichiers, le dernier élément correspond généralement à l'extension du fichier (comme mp3 ou MP4).
    
    ext = fichier.split('.')[-1]#Ici, on sépare par un point et on récupère le dernier elt
    if ext.lower() == 'mp3':  # Ici, on vérifie et faire une Comparaison sans le point
        print(fichier)  # Affiche uniquement les fichiers .mp3

#Exo8: TP table de multiplication avec utilisation boucle for
#Affichage de la  de multiplications de 11 à 20 plutôt que celles de 1 à 10.
for i in range(11, 20+1):
    print(f'Table de multiplication de {i}')
    for j in range(10+1):
        print(f'{i} x {j} = {i * j}')
    print('\n')

#Affichage des tables plus grandes qui vont de 0 à 19 plutôt que de 0 à 10.
for i in range(1, 10+1):
    print(f'Table de multiplication de {i}')
    for j in range(19+1):
        print(f'{i} x {j} = {i * j}')
    print('\n')

## Question 3: Changez l'ordre d'affichage
for i in range(1, 10+1):
    print(f'Table de multiplication de {i}')
    for j in range(10+1):
        print(f'{j} x {i} = {i * j}')
    print('\n')
    
for i in range(0,19+1):
    print(f'Table de multiplication de {i}')
    for j in reversed(range (19+1)):
        print(f'{i}x{j} = {i*j}')
        print('\n')