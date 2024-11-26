#Ex01: Règle n°01 des scopes et des fonctions
#Result=> Error: Toute variable définie à l'intérieur d'une fonction n'existe pas à l'extérieur de cette fonction.
#def créer_une_variable():
    #nouvelle-variable='To be or not to be'

#créer_une_variable()
#print(nouvelle_variable)

#Ex02:Règle n°02 des scopes et des fonctions
#Deux variables différentes peuvent avoir le même nom si elles se situent dans deux scopes différentes.
NE_PAS_MODIFIER='Fichier Rapport confidentiel secret'

def une_fonction_rien_à_voir():
    NE_PAS_MODIFIER='La recette surpême de grand-mère du ragout de légumes.'
    print("J'adore",NE_PAS_MODIFIER)
    print('Jespère ne jamais la perdre. \n')

une_fonction_rien_à_voir()
print('Il ne faut surtout pas modifier', NE_PAS_MODIFIER)
print('Il en va de la survie du monde')
