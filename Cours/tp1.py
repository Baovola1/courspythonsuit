#Exo1: Factorisation avec des boucles FOR
collection = ["A","B","C"]

for alphabet in collection:
    print(alphabet.lower())

#Exo2:Bien choisir ses noms de variables
nombre_pairs=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

for nombre_pair in nombre_pairs:
    carré = nombre_pair ** 2
    print(carré)