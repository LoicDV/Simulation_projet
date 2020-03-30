import matplotlib.pyplot as plt

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
    Retourne : Met dans un dictionnaire les occurences des nombres.
    Effet : /

    Crée un dictionnaire pour chaque valeur et contient le nombre de fois
    qu'il apparait.
    """
    dictionnaire_occurence = {}
    for element in liste_nombre:
        if element not in dictionnaire_occurence:
            dictionnaire_occurence[element] = 1
        else:
            dictionnaire_occurence[element] += 1
    return dictionnaire_occurence

def afficheur_occurence(dictionnaire_occurence):
    """
    Argument : dictionnaire_occurence : un dictionnaire avec les nombres.
                                        ainsi que leur occurence.
    Retourne : /
    Effet : Affiche pour chaque nombre, leur occurence.

    Print pour chaque clé dans le dictionnaire, le nombre de fois qu'il y est.
    """
    for clé in range(len(dictionnaire_occurence)):
        print("Le nombre " + str(clé) + " est sorti " \
            + str(dictionnaire_occurence[clé]) + \
            " fois dans les décimales de pi.")

def dictionnaire_en_liste(dictionnaire_digit):
    """
    Argument : dictionnaire_digit : dictionnaire de digits des décimales de pi.
    Retourne : 2 listes avec dans l'une les clés.
                             dans l'autre les valeurs.
    Effet : /

    Transfome le dictionaire en 2 listes utilisables par la suite.
    """
    cle = []
    valeur = []
    for element in range(len(dictionnaire_digit)):
        cle.append(element)
        valeur.append(dictionnaire_digit[element])
    return cle, valeur

def histo_digits_pi(liste):
    """
    Argument : dictionnaire_digit :
    Retourne : /
    Effet : Construit un histogramme par rapport au dictionnaire fournit.

    Prend toutes les décimales de pi et construis un histogramme avec pyplot.
    """
    titre ="Histogramme sur les décimales de pi en fonction de leur occurence."
    plt.figure()
    plt.hist(liste)
    plt.xlabel("Valeur des digits")
    plt.ylabel("Nombre d'occurence")
    plt.title(titre)
    plt.show()

if __name__ == "__main__":
    liste = prendre_pi_decimale()
    dico = compteur_de_nombre(liste)
    histo_digits_pi(liste)