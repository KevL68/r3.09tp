#Exercice 1 :

def lecture_fichier(x: str) -> str:
    with open(x, "r") as f: #Ouverture du fichier "test.txt" en lecture seule. Le bloc "with" permet la fermeture automatique du fichier
        lecture = f.read() #Affichage du contenu du fichier
    return lecture

#Exercice 2 :

if __name__ == '__main__':
    try:
        nom_fichier = input("Nom du fichier à ouvrir : ")
        contenu = lecture_fichier(nom_fichier)
        print(contenu)
    except FileNotFoundError:
        print("Le fichier",nom_fichier,"n'existe pas !")
    except IOError:
        print("Le fichier",nom_fichier,"n'existe pas et/ou vous ne pouvez pas lire/écrire dans celui-ci.")
    except FileExistsError:
        print("Le fichier ou le répertoire",nom_fichier,"existe déjà.")
    except PermissionError:
        print("Vous n'avez pas la permission de lire ou d'écrire dans ce fichier.")
    finally:
        fin = "Fin du programme"
        print(fin)
