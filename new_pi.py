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
    p = b - a
    for i in dict_value:
        proba = math.pow(1 - p, i) * p
        dict_proba[i] = proba
    return dict_proba

def Kr(r, N, dict_value, dict_proba):
    kr = 0
    for i in dict_value:
        ni = dict_value[i]
        pi = dict_proba[i]
        kr += math.pow((ni - N*pi)/math.sqrt(N*pi), 2)
    return kr

def test_chi2(r, list_value, dict_value, dict_proba, deg):
    list_win = []
    kr = Kr(len(dict_value), len(list_value), dict_value, dict_proba)
    list_alpha = [0.001, 0.01, 0.025, 0.05, 0.1]
    for alpha in list_alpha:
        crit_value = scp.chi2.ppf(1-alpha, deg)
        if kr < crit_value:
            list_win.append((alpha, True))
        else:
            list_win.append((alpha, False))
    return list_win

def test_gap(a, b, list_value):
    if (a >= b) or (a < 0) or (b > 1):
        raise Exception("a, b have to be in [0, 1].")
    a *= 10
    b *= 10
    list_gap = []
    compt = 0
    for i in range(len(list_value)):
        if list_value[i] >= a and list_value[i] <= b:
            list_gap.append(compt)
            compt = 0
        else :
            compt += 1
    dict_value = occ_number(list_gap)
    dict_proba = proba_dict_gap(a/10, b/10, dict_value)
    deg = max(dict_value) - 1
    return test_chi2(len(dict_value), list_gap, dict_value, dict_proba, deg)

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
    list_value = get_decimal_pi()
    a = float(input("Nombres dans [0, 1[ : "))
    b = float(input("Nombres dans ]0, 1] avec le premier < celui-ci : "))
    list_final = test_gap(a, b, list_value)
    print(list_final)