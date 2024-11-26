def afficher_aide():
    message_aide="Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker."
    print(message_aide)

#TP ARGUMENT FONCTION
#Ex01:
def dire_bonjour():
    print('Bonjour')


#Ex02
def dire_qlqchose_X_fois(qlqchose,x):
    for _ in range(x):
        print(qlqchose)

#Ex05: 
def creer_une_phrase(mot1,mot2,mot3,mot4='',mot5=''):
    #Arguments :
    #mot1, mot2, mot3 : mots obligatoires pour former une phrase.
    #mot4, mot5       : mots optionnels, ajoutés si fournis.
    
    #Ici,le premier mot commence par une majuscule
    phrase=mot1.title()+' '+mot2.lower()+' '+ mot3.lower()

    #Ajout de mot4 s'il est fourni.
    if mot4:
        phrase+= ' '+ mot4.lower()
    
    #Ajout de mot5 s'il est fourni.
    if mot5:
        phrase += ' ' + mot5.lower()
    #La phrase se termine par un point    
    phrase += '.'
    return phrase
    
# Appels de la fonction avec différents arguments pour observer son fonctionnement.
#result1= creer_une_phrase('Hello','le','monde')
#print(result1)

#result2=creer_une_phrase('Mon','code','en','python')
#print(result2)

#result3=creer_une_phrase('Mon','code','en','python','vscode')
#print(result3)

#SUITE SCOPE(ARGUMENT PAR REFERENCE)
from scope import simulation_double_pop

ma_liste=[4,10,7]

result=simulation_double_pop(ma_liste)

print(result)
