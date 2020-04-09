import numpy as np
import matplotlib.pyplot as plt
import operator
import math
import scipy.stats as scp

def get_decimal_pi():
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
    dict_occ = {}
    for element in list_value:
        if element not in dict_occ:
            dict_occ[element] = 1
        else:
            dict_occ[element] += 1
    return dict_occ

def proba_dict_chi2(r):
    dict_proba = {}
    proba = 1/r
    for i in range(r):
        dict_proba[i] = proba
    return dict_proba

def proba_dict_gap(a, b, dict_value):
    dict_proba = {}
    p = math.floor(10*b)/10 - math.ceil(10*a)/10 + 0.1
    for i in dict_value:
        proba = math.pow(1 - p, i) * p
        dict_proba[i] = proba
    return dict_proba

def proba_dict_poker():
    pass

def stirling_number(dict_stir, k, r):
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

def poss_poker(list_value):
    dict_occ = occ_number(list_value)
    if len(dict_occ) == 1:
        return "Poker"
    elif len(dict_occ) == 2:
        if dict_occ[list_value[0]] == 3 or dict_occ[list_value[0]] == 2:
            return "Full"
        return "Carré"
    elif len(dict_occ) == 3:
        for elem in dict_occ:
            if dict_occ[elem] == 3:
                return "Brelan"
        return "Double pair"
    elif len(dict_occ) == 4:
        return "Pair"
    return "Rien"


def Kr(N, dict_value, dict_proba):
    kr = 0
    for i in dict_value:
        ni = dict_value[i]
        pi = dict_proba[i]
        kr += math.pow((ni - N*pi)/math.sqrt(N*pi), 2)
    return kr

def test_chi2(r, list_value, dict_value, dict_proba, deg):
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

def test_gap(a, b, list_value):
    if (a >= b) or (a < 0) or (b > 0.9):
        raise Exception("a, b have to be in [0, 0.9].")
    k = 0
    while list_value[k]/10 < a or list_value[k]/10 > b:
        k += 1
    list_gap = []
    compt = 0
    for i in range(k+1, len(list_value)):
        if list_value[i]/10 >= a and list_value[i]/10 <= b:
            list_gap.append(compt)
            compt = 0
        else :
            compt += 1
    dict_value = occ_number(list_gap)
    dict_proba = proba_dict_gap(a, b, dict_value)
    deg = len(dict_value) - 1
    return test_chi2(len(dict_value), list_gap, dict_value, dict_proba, deg)

    def test_poker():
        pass

if __name__ == "__main__":
    """
    TEST DE CHI2
    """
    """
    list_value = get_decimal_pi()
    dict_value = occ_number(list_value)
    dict_proba = proba_dict_chi2(len(dict_value))
    r = len(dict_value)
    deg = r - 1
    list_final = test_chi2(r, list_value, dict_value, dict_proba, deg)
    print(list_final)
    """
    """
    TEST DU GAP
    """
    """
    list_value = get_decimal_pi()
    a = float(input("a dans [0, 1[ : "))
    b = float(input("b dans ]0, 1] avec a < b : "))
    list_final = test_gap(a, b, list_value)
    print(list_final)
    """
    """
    TEST DU POKER
    """