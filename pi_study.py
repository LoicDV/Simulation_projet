"""
Pour la partie codage, mettre juste après la définition :
    Argument :
    Retourne :
    Effet :

et expliquer en 1-2 lignes ce que fait le code.
"""

def prendre_pi_decimale():
    """
    Argument : /
    Retourne : une liste comprenant toutes les décimales de pi (max 1 million).
    Effet : /

    Va parcourir les décimales de pi et va les ajouter dans une liste.
    """
    liste_totale = []
    with open("Décimales de pi.txt") as fichier:
        for ligne in fichier:
            for element in range(len(ligne)):
                if (ligne[element] == '\n'):
                    break
                nombre = int(ligne[element])
                liste_totale.append(nombre)
    return liste_totale

def compteur_de_nombre(liste_nombre):
    """
    Argument : liste_nombre : une liste d'entier.
    Retourne : Met dans un dictionnaire les occurences des nombres triés.
    Effet : /


    """
    dictionnaire_occurence = {}
    for element in liste_nombre:
        if element not in dictionnaire_occurence:
            dictionnaire_occurence[element] = 1
        else:
            dictionnaire_occurence[element] += 1
    return dictionnaire_occurence

liste = prendre_pi_decimale()
test = compteur_de_nombre(liste)
print(test)

def afficheur_d_occurence(dictionnaire_occurence):
    """
    Argument : dictionnaire_occurence : un dictionnaire avec les nombres
                                        ainsi que leur occurence.
    Retourne : /
    Effet : Affiche pour chaque nombre, leur occurence.


    """