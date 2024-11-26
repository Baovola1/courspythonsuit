#SCOPE(Portée des varibales)
#Règles:1)Je peux avoir deux variables différents avec le même nom tant qu'elles sont dans 2scopes différentes
        #2)Je peux appeler dans ma scope interne des variables définies dans la scope externe
        #A UNE CONDITION;C'est de ne jamais utiliser = sur la variable externe(ie assigné qlq chose sur la varibale externe après avoir utiliser)
        #3)Je ne peux pas appeler une varibale interne à l'externe de mon code
#UnboundLocalError:On ne peut pas assigner une valeur à une variable externe
result="DEFINIE A L'EXTERIEUR DE MA FONCTION"

#Ici: on ne peut pas faire
def addition(a,b,c=0):
    print('DEBUG:A l\'intérieur')
    #Ici,on met avant:not valable
    print(result)
    result= a+ b +c
    return result

print('\nDEBUG:à l\extérieur')
#résultat= addition(10,20,30)
#print(result)

#Ici: On peut faire
def addition(a,b,c=0):
    print('DEBUG:A l\'intérieur')
    result= a+ b +c
    #Ici on met après avoir assigné une valeur,c'est valable
    print(result)
    return result

print('\nDEBUG:à l\extérieur')
résultat= addition(10,20,30)
print(result)

#PASSAGE D'ARGUMENTS par reference
def simulation_double_pop(liste):
    liste.pop()
    liste.pop()
    return liste