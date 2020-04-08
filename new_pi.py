import numpy as np
import matplotlib.pyplot as plt
import operator
import math
import scipy.stats as scp

def get_decimal():
    liste_totale = []
    with open("pi_decimal.txt") as file:
        for lines in file:
            for element in lines:
                if lines[element] is '\n':
                    break
                nombre = int(lines[element])
                liste_totale.append(nombre)
    return liste_totale

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



if __name__ == "__main__":
    pass