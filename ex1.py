#Création de la fonction "divEntier" avec les variables "x" et "y" qui seront des entiers.
def divEntier(x: int, y: int) -> int:

#Si x est inférieur à y la valeur retournée sera 0
 if x < y:
     return 0
 else:
    x = x - y
    return divEntier(x, y) + 1

#Ecercice 1 :
if __name__ == '__main__':
    try:
        resultat = divEntier(int(input("x = ")), int(input("y = ")))
        print(resultat)
#Exercice 2 :
    #ValueError doit être géré afin de préciser qu'il faut que saisir des entier.
    except ValueError:
        print("La valeur saisie n'est pas un entier.")

    except RecursionError:
        print("Vous ne pouvez pas diviser par 0.")

