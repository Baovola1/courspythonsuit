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

#Utilisatioon argument et return
#Cas1:nbr argument compatible avec les 3 chiffres donnés
def addition(a,b,c):
    return a+b+c

result=addition(10,20,30)
print(result)

#Cas2: nbr argument différent du nbr des chiffres
def addition1(a,b,c=0):
    return a+b+c

result=addition1(10,20)
print(result)
