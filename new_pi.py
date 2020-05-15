import math
import scipy.stats as scp

def get_decimal_pi():
    """
    Entrée: /
    Sortie: (list) une liste contenant les décimales de pi.
    Effet de bord: /

    Crée une liste contenant 1 000 000 d'entiers représentant les décimales de pi.
    """
    liste_totale = []
    with open("pi_decimal.txt") as file:
        for lines in file:
            for element in range(len(lines)):
                if lines[element] == '\n':
                    break
                nombre = int(lines[element])
                liste_totale.append(nombre)
    return liste_totale

def occ_number(list_value):
    """
    Entrée: (list) une liste de nombre.
    Sortie: (dict) un dictionnaire de nombre.
    Effet de bord: /

    Crée un dictionnaire calculant l'occurence de chaque nombre.
    """
    dict_occ = {}
    for element in list_value:
        if element not in dict_occ:
            dict_occ[element] = 1
        else:
            dict_occ[element] += 1
    return dict_occ

def proba_dict_chi2(r, dict_value):
    """
    Entrées: (int) r: entier pour la loi uniforme.
             (dict) dict_value: dictionnaire d'occurence de nombres.
    Sortie: (dict) un dictionnaire de probabilités.
    Effet de bord: /

    Crée un dictionnaire de probabilités associant chaque valeur possible avec la probabilité d'obtenir cette valeur.
    """
    dict_proba = {}
    proba = 1/r
    for i in dict_value:
        dict_proba[i] = proba
    return dict_proba

def proba_dict_gap(p, dict_value):
    """
    Entrées: (float) p: une probabilité.
             (dict) dict_value: un dictionnaire d'occurence de nombres.
    Sortie: (dict) un dictionnaire de probabilités.
    Effet de bord: /

    Crée un dictionnaire associant les différentes longueurs que l'on peut obtenir avec la probabilités d'obtenir cette longueur.
    """
    dict_proba = {}
    for i in dict_value:
        if i == 10:
            continue
        proba = math.pow(1-p, i) * p
        dict_proba[i] = proba
    somme = 0
    for j in dict_proba:
        somme += dict_proba[j]
    dict_proba[10] = 1 - somme
    return dict_proba

def proba_dict_poker(k, d):
    """
    Entrées: (int) k: entier pour la longueur de la main.
             (int) d: le nombre d'intervalle.
    Sortie: (dict) un dictionnaire de probabilités.
    Effet de bord: /

    Crée un dictionnaire associant le nombre d'intervalle dans lesquelles on trouve au moins une valeur
    à la probabilité d'obtenir ce nombre d'intervalle.
    """
    dict_proba = {}
    dict_stir = {}
    for i in range(1, d):
        tmp = d
        stirling = stirling_number(dict_stir, k, i)
        while tmp >= d-i+1:
            stirling *= tmp
            tmp -= 1
        stirling /= d**k
        dict_proba[i] = stirling
    return dict_proba

def stirling_number(dict_stir, k, r):
    """
    Entrées: (dict) dict_stir: dictionnaire avec certain nombre de striling.
             (int) k: entier utile pour calculer le nombre de stirling.
             (int) r: entier utile pour calculer le nombre de stirling.
    Sortie: (int) le nombre de Stirling.
    Effet de bord: Rajoute des valeurs dans dict_stir (méthode de mémoïsation).

    Retourne le nombre de Striling correspondant au k et r
    et modifie dict_stir pour rendre la fonction plus performante.
    """
    if k < r:
        dict_stir[(k, r)] = 0
    if (k, r) in dict_stir:
        return dict_stir[(k, r)]
    elif r == 1:
        dict_stir[(k, 1)] = 1
        return 1
    elif k == r:
        dict_stir[(k, r)] = 1
        return 1
    stirling = stirling_number(dict_stir, k-1, r-1) + r * stirling_number(dict_stir, k-1, r)
    dict_stir[(k, r)] = stirling
    return stirling

def Kr(N, dict_value, dict_proba):
    """
    Entrées: (int) N: nombre total d'élements.
             (dict) dict_value: dictionnaire d'occurence de nombres.
             (dict) dict_proba: dictionnaire de probabilités.
    Sortie: (int) le nombre Kr.
    Effet de bord: /

    Calcule le Kr.
    """
    kr = 0
    for i in dict_value:
        ni = dict_value[i]
        pi = dict_proba[i]
        kr += math.pow(ni - N*pi, 2)/(N*pi)
    return kr

def test_chi2(r, list_value, dict_value, dict_proba, deg):
    """
    Entrées: (int) r: le nombre de valeurs possibles.
             (list) list_value: une liste de nombre.
             (dict) dict_value: un dictionnaire d'occurence de nombre.
             (dict) dict_proba: un dictionnaire de probabilité.
             (int) deg: le degré de liberté.
    Sortie: (list) une liste de tuples avec une valeur de alpha et un booléen.
    Effet de bord: /

    Effectue le test de chi2 pour les différentes valeurs d'alpha.
    """
    list_win = []
    kr = Kr(len(list_value), dict_value, dict_proba)
    list_alpha = [0.001, 0.01, 0.025, 0.05, 0.1]
    for alpha in list_alpha:
        crit_value = scp.chi2.ppf(1-alpha, deg)
        if kr < crit_value:
            list_win.append((alpha, True))
        else:
            list_win.append((alpha, False))
    return list_win

def test_gap(a, b, list_value, pi):
    """
    Entrées: (float) a: nombre représentant le début de l'intervalle.
             (float) b: nombre représentant la fin de l'intervalle.
             (list) list_value: liste de nombres
             (bool) pi: True si c'est les décimales de pi, False sinon.
    Sortie: un appel vers le test de chi2 --> (list)
    Effet de bord: /

    Exécute le test du gap avec un certain intervalle.
    """
    if (a >= b) or (a < 0) or (b > 1):
        raise Exception("a, b have to be in [0, 1].")
    if pi and b > 0.9:
        b = 0.9
    k = 0
    while list_value[k] < a or list_value[k] > b:
        k += 1
    list_gap = []
    compt = 0
    for i in range(k+1, len(list_value)):
        if list_value[i] >= a and list_value[i] <= b:
            if compt > 10:
                compt = 10
            list_gap.append(compt)
            compt = 0
        else :
            compt += 1
    dict_value = occ_number(list_gap)
    if pi:
        proba = math.floor(10*b)/10 - math.ceil(10*a)/10 + 0.1
    else:
        proba = b - a
    dict_proba = proba_dict_gap(proba, dict_value)
    deg = len(dict_value) - 1
    return test_chi2(len(dict_value), list_gap, dict_value, dict_proba, deg)

def test_poker(list_value, poker, k=5,d=10):
    """
    Entrées: (list) list_value: liste de nombres.
             (bool) poker: False si c'est les décimales de pi, True sinon.
             (int) k: longueur de la main.
             (int) d: le nombre dintervalle.
    Sortie: un appel vers le test de chi2 --> (list)
    Effet de bord: /

    Exécute le test du poker.
    """
    if poker:
        for i in range(len(list_value)):
            list_value[i] = math.floor(list_value[i]*10)/10
    dict_proba = proba_dict_poker(k, d)
    list_poker = []
    list_test_poker = []
    for elem in list_value:
        list_test_poker.append(elem)
        if len(list_test_poker) == k:
            number = len(occ_number(list_test_poker))
            list_poker.append(number)
            list_test_poker = []
    dict_value = occ_number(list_poker)
    return test_chi2(k, list_poker, dict_value, dict_proba, k-1)

if __name__ == "__main__":
    print("(1) Test de Chi2 :")
    print("(2) Test du Gap :")
    print("(3) Test du Poker :")
    print("(4) Exit")
    number_test = int(input("Quel test voulez-vous ?" + '\n'))
    if number_test != 1 and number_test != 2 and number_test != 3 and number_test != 4:
        raise Exception("Vous n'entrez pas un bon numéro.")
    elif number_test == 1:
        """TEST DE CHI2"""
        list_value = get_decimal_pi()
        dict_value = occ_number(list_value)
        dict_proba = proba_dict_chi2(len(dict_value), dict_value)
        r = len(dict_value)
        deg = r - 1
        list_final = test_chi2(r, list_value, dict_value, dict_proba, deg)
        print(list_final)

    elif number_test == 2:
        """TEST DU GAP"""
        list_value = get_decimal_pi()
        for i in range(len(list_value)):
            list_value[i] /= 10
        a = float(input("a dans [0, 1[ : "))
        b = float(input("b dans ]0, 1] avec a < b : "))
        list_final = test_gap(a, b, list_value, True)
        print(list_final)
    elif number_test == 3:
        """TEST DU POKER"""
        list_value = get_decimal_pi()
        list_final = test_poker(list_value, False)
        print(list_final)
    else:
        exit()