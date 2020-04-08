import numpy as np
import matplotlib.pyplot as plt
import operator
import math

def get_decimal():
    liste_totale = []
    with open("pi_decimal.txt") as file:
        for lines in file:
            for element in lines:
                if ligne[element] is '\n':
                    break
                nombre = int(ligne[element])
                liste_totale.append(nombre)
    return liste_totale

def Kr(r, N, dict_value, dict_proba):
    kr = 0
    for i in dict_value:
        ni = dict_value[i]
        pi = dict_proba[i]
        kr += math.pow((ni - N*pi)/math.sqrt(N*pi), 2)
    return kr

def test_chi2(r, Kr, list_value):
    pass