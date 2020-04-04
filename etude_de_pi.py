import matplotlib.pyplot as plt
import math

"""
Pour la partie codage, mettre juste après la définition :
    Argument :
    Retourne :
    Effet :

et expliquer en 1-2 lignes ce que fait le code.
"""

def get_pi_decimal():
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

def occ_number(liste_nombre):
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

def display_occ(dictionnaire_occurence):
    """
    Argument : dictionnaire_occurence : un dictionnaire avec les nombres.
                                        ainsi que leur occurence.
    Retourne : /
    Effet : Affiche pour chaque nombre, leur occurence.

    Print pour chaque clé dans le dictionnaire, le nombre de fois qu'il y est.
    """
    for cle in range(len(dictionnaire_occurence)):
        print("Le nombre " + str(cle) + " est sorti " \
            + str(dictionnaire_occurence[cle]) + \
            " fois dans les décimales de pi.")

def dict_to_list(dictionnaire_digit):
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

def test_chi2(liste):
    """
    Argument : liste : liste d'entiers.
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
    plt.grid()
    plt.show()

liste = get_pi_decimal() #liste des décimales de pi.
dico = occ_number(liste) #dictionnaire avec les occurences de pi.

def Kr(r, N, proba):
    """
    Argument : r : nombres d'intervalles.
               N : nombre total d'élément.
           proba : probabilité d'avoir le digit en question.
    Retourne : Le résultat du Kr.
    Effet : /

    Calcule, selon la slide 38 du cours, le Kr.
    """
    sol = 0
    for i in range(r):
        n_i = dico[i]
        sol += math.pow((n_i - N * proba) / math.sqrt(N * proba), 2)
    return sol

def testeur():
    import random
    import math

    def moins_chelou():
        return random.randint(0, 10000000000) / 100000000

    dictt = {}
    for i in range(0, 10001):
        dictt[(i, i+1)] = 0

    for i in range(10000000):
        k = moins_chelou()
        dictt[(math.floor(k), math.floor(k)+1)] += 1

    for i in range(0, 100):
        print(str((i, i+1)) + ' ----> ' + str(dictt[(i, i+1)]))

def test_gap(a0, b0):
    if (a0 >= b0) or (a0 < 0) or (b0 > 1):
        raise Exception("a, b have to be in [0, 1].")
    a = a0 * 10
    b = b0 * 10
    liste_gap = [] #liste de n éléments de compteurs.
    compteur = 0
    for i in range(len(liste)):
        if liste[i] >= a and liste[i] <= b:
            liste_gap.append(compteur)
            compteur = 0
        else :
            compteur += 1
    dictionnaire_occurence = occ_number(liste_gap)
    display_occ(dictionnaire_occurence)
    test_chi2(liste_gap)

if __name__ == "__main__":
    test_gap(0, 0.5)