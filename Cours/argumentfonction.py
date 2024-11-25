#Utilisation simple argument
def dire_quelquechose(qqch):
    print(qqch)

dire_quelquechose('Hey you')

#Définir un argument par défaut
#Cas1:il affiche le msg par défaut
def ma_fonction(mot='Message par défaut'):
    print(mot)

ma_fonction()
#Cas2:le msg 'Hey you' s'affiche dans ce cas
def ma_fonction1(msg='Message par défaut'):
    print(msg)

ma_fonction1('Hey You')
