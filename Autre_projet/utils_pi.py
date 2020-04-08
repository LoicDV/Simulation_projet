#coding: utf-8

import matplotlib.pyplot as plt
import operator
import numpy as np
import scipy.stats

stirling_history = []
GAP_RANGE = range(50)

def get_decimal_pi(limit=1000000):
    """Convertit le fichier 'pi_decimal.txt' en liste de nombre

    Args:
        limit (int, optional): Représente la limite des décimales de pi à charcher. Defaults to 1000000.

    Returns:
        list: la liste des décimales de pi
    """
    k=0
    with open("pi_decimal.txt", 'r') as fi:
        res = []
        for line in fi:
            for ch in line:
                if ch != '\n':
                    if limit == k:
                        return res
                    k+=1
                    res.append(int(ch))
        return res

def kr(exp, proba_dict):
    """Calcule l'indice Kr du test du chi2

    Args:
        exp (list): La liste des mesures expérimentales
        proba_dict (dict): Le dictionnaire des probabilités de chacuns des événements

    Returns:
        float: L'indice Kr
    """
    somme = 0
    for i in range(len(proba_dict)):
        temp = 0
        ni = exp.count(i)
        try:
            Npi = len(exp) * proba_dict[i]
            temp += ((ni - Npi)/np.sqrt(Npi))**2
            somme+=temp
        except KeyError:
            print('KeyError - Surement Test du Gap')
    return somme

#inspired from: https://www.apprendre-en-ligne.net/random/corriges/ex18.py
def KS(x):
    n = len(x)
    d_alpha = 1.36/np.sqrt(n)
    x.sort()
    a = -1000
    b = -1000
    alpha_list = [0.001, 0.01, 0.02, 0.05, 0.10]
    d_alpha_list = [1.949, 1.627, 1.517, 1.358, 1.223]
    dn_list = []
    result=[]
    for i in range(n):
        if float(i)/n - x[i] > a:
            a = float(i)/n - x[i]
        if x[i] - float(i)/n > b:
            b = x[i] - float(i)/n
    d = max(a,b)
    for i in range(len(alpha_list)):
        dn_list.append(d)
        if d > d_alpha_list[i]/np.sqrt(n):
            result.append('Raté')
        else:
            result.append('Réussi')
    return alpha_list, dn_list, d_alpha_list, result


def chi_2_test(x, proba_dict, df):
    """Effectue le test du chi2 sur l'échantillon x pour plusieurs alpha pré-établis

    Args:
        x (list): liste des mesures expérimentale
        proba_dict (dict): le dictionnaire des probabilités de chaque évenéments
        df (int): le degré de liberté du test

    Returns:
        tuple: Tuple contenant:
                . alpha_list - les alphas utilisés pour le test du chi2
                . kr_list - la liste des indices Kr (tous les mêmes car dépend de x)
                . chi_2 - la liste des valeurs du chi2 dans la table (scipy)
                . result - le résultat du test ('Réussi' ou 'Raté')
    """
    D = kr(x, proba_dict)
    alpha_list = [0.001, 0.01, 0.025, 0.05, 0.10]
    kr_list = []
    chi_2 = []
    result = []
    for alpha in alpha_list:
        kr_list.append(D)
        c = scipy.stats.chi2.ppf(1.0-alpha, df)
        chi_2.append(c)
        if D < c:
            result.append('Réussi')
        else:
            result.append('Raté')
    return alpha_list, kr_list, chi_2, result

def gap_test_digit(decimal_pi, digit):
    """Effectue le test du gap sur les décimale de pi pour un digit donné selon le test du chi2

    Args:
        decimal_pi (list): les décimales de pi
        digit (int): le digit testé

    Returns:
        tuple: Tuple contenant:
                . alpha_list - les alphas utilisés pour le test du chi2
                . kr_list - la liste des indices Kr (tous les mêmes car dépend de x)
                . chi_2 - la liste des valeurs du chi2 dans la table (scipy)
                . result - le résultat du test ('Réussi' ou 'Raté')
    """
    proba_dict = proba_dict_gap(GAP_RANGE)
    gap_exp = len_gap(decimal_pi, digit)
    return chi_2_test(gap_exp, proba_dict, len(GAP_RANGE)-1)

def poker_test(decimal_pi, real=False):
    k = 5
    proba_dict = proba_dict_poker(k, 10)
    poker_exp = poker(decimal_pi, real)
    return chi_2_test(poker_exp, proba_dict, k)

def len_gap(decimal_pi, digit, count_zero = True):
    """Calcule les longueurs de gap entre chaque occurences de digit

    Args:
        decimal_pi (list): les décimales de pi
        digit (int): le digit testé
        count_zero (bool, optional): compte les longueurs de taille 0. Defaults to True.

    Returns:
        list: la liste de toutes les longueurs séparant les occurences de digit
    """
    L = 0
    len_list = []
    for i in decimal_pi:
        # if L == len(GAP_RANGE)-1:
        #     len_list.append(L)
        #     L = 0
        if i != digit:
            L += 1
        else:
            if L != 0:
                len_list.append(L)
                L = 0
            elif count_zero:
                len_list.append(L)
                L = 0
    return len_list

def proba_dict_gap(gap_range):
    """Calcule toutes les probabilités que deux digits soient séparés de toutes les longueurs données dans gap_range

    Args:
        gap_range (list): la liste des longueurs de gap possible

    Returns:
        dict: le dictionnaire des probabilités pour chaque longueur
    """
    proba_dict = {}
    for i in gap_range:
        # if i == len(gap_range)-1:
        #     proba_gap_i = ((9./10) ** (i+1))
        # else:
        proba_gap_i = 0.1
        proba_gap_i *= np.power(0.9, i)
        proba_dict[i] = round(proba_gap_i, 6)
    return proba_dict

def proba_gap(gap_range):
    """Ajoute autant de longueurs de gap qu'il est probable d'en avoir en théorie

    Args:
        gap_range (list): la liste des longueurs de gap possible

    Returns:
        list: la liste des longueurs théorique
    """
    thq_len = []
    for i in gap_range:
        temp = []
        # if i == len(gap_range)-1:
        #     proba_gap_i = ((9./10) ** (i+1))
        # else:
        proba_gap_i = 0.1
        proba_gap_i *= np.power(0.9, i)
        temp.append(i)
        thq_len += temp*(int(proba_gap_i*100000))
    return thq_len

def comptage(digits):
    '''Compte le nombre d'occurences d'un digit dans la liste digits

    Args:
        digits (list): la liste des digits

    Returns:
        int: le numéro de la main obtenue
            . poker : 0
            . carre/full : 1
            . brelan/double paire : 2
            . paire : 3
            . rien : 4
    '''
    d = {}
    for l in digits:
        if l not in d : d[l] = 1
        else: d[l] += 1
    return d

def comptage_for_0_1(digits):
    dico={}
    intervalle = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    for d in digits:
        for i in range(len(intervalle)-1):
            if d >= intervalle[i] and d < intervalle[i+1]:
                x = (intervalle[i], intervalle[i+1])
                if x not in dico:
                    dico[x] = 1
                else:
                    dico[x] += 1
    print(dico)
    return dico

def poker_hand_0_1(c):
    first_max = c.pop(max(c.iteritems(), key=operator.itemgetter(1))[0])
    if first_max == []:
        return 0
    if first_max == 4:
        return 1
    second_max = c.pop(max(c.iteritems(), key=operator.itemgetter(1))[0])
    if first_max == 3:
        if second_max == 2:
            return 1
        else:
            return 2
    if first_max == 2:
        if second_max == 2:
            return 2
        else:
            return 3
    return 4

def poker_hand(c):
    """Calcule le type de main dans c

    Args:
        c (dict): le dictionnaire des 5 digits à testé

    Returns:
        int: représente le numéro de la main
            . poker : 0
            . carre/full : 1
            . brelan/double paire : 2
            . paire : 3
            . rien : 4
    """
    first_max = c.pop(max(c.iteritems(), key=operator.itemgetter(1))[0])
    if first_max == 5:
        return 0
    if first_max == 4:
        return 1
    second_max = c.pop(max(c.iteritems(), key=operator.itemgetter(1))[0])
    if first_max == 3:
        if second_max == 2:
            return 1
        else:
            return 2
    if first_max == 2:
        if second_max == 2:
            return 2
        else:
            return 3
    return 4

def poker(decimal_pi, real=False):
    '''Récupère des séquences de 5 digit afin d'appliquer le test du poker

    Args:
        decimal_pi (list): la liste des décimales de pi
        digit ([type]): [description]

    Returns:
        list: La liste de toutes les mains obtenues pour les 200.000 séquences
        de 5 digit
            . poker : 0
            . carre/full : 1
            . brelan/double paire : 2
            . paire : 3
            . rien : 4
    '''

    len_list = []
    poker_list = []
    for i in decimal_pi:
        len_list.append(i)
        if len(len_list) == 5:
            if real:
                c = comptage_for_0_1(len_list)
            else:
                c = comptage(len_list)
            #ajoute 0,1,2,3,4 à la liste
            #plus facile pour faire l'histogramme
            poker_list.append(poker_hand(c))
            len_list = []
    return poker_list

def stirling(k, r):
    """Calcule le nombre de stirling

    Args:
        k (int): nombre dans les r paquets
        r (int): nombres de paquets

    Returns:
        int: le nombre de stirling
    """
    if r == 1 or r == k:
        return 1
    else:
        return stirling(k-1, r-1) + r*stirling(k-1, r)

def proba_dict_poker(k, d):
    """Calcule le dictionnaire des probabilités d'avoir une certaine main

    Args:
        k (int): nombre de digit dans la man
        d (int): nombre de possibilité de digit

    Returns:
        dict: dictionnaire des probabilités
    """
    proba_dict = {}
    for r in range(5):
        if r in [0, 3, 4]:
            proba = stirling(k, r+1)
        else:
            proba = stirling(k, r+1)
        d_fact_r = d
        for i in range(1,r+1): #jusque rthq-1 <=> r+1-1
            d_fact_r *= (d-i)
        d_fact_r /= float(d**k)
        proba_dict[r] = proba*d_fact_r
    return proba_dict

def proba_poker(k, d):
    """Ajoute autant de mains qu'il est probable d'en avoir en théorie

    Args:
        k (int): nombre de digit dans la man
        d (int): nombre de possibilité de digit

    Returns:
        list: la liste des mains théorique
    """
    proba = proba_dict_poker(k,d)
    thq_len = []
    for i in range(5):
        temp = [i]
        thq_len += temp*(int(proba[i]*200000))
    return thq_len
"""
def format_latex((l, x, y, result), first_title, second_title, third_title, fourth_title):
    s = '\\begin{center}\n\\begin{tabular}{|c|c|c|c|}\n\\hline\n'
    s += first_title + ' & ' + second_title + ' & ' + third_title + ' & ' + fourth_title + '\\\\\n\\hline\n\\hline\n'
    for index in range(len(x)):
        s += str(round(a[index], 3)) + ' & ' + str(round(x[index], 5)) + ' & ' + str(round(y[index], 3)) + ' & ' + str(result[index]) + '\\\\\n'
    s += '\\hline\n\\end{tabular}{}\\end{center}'
    return s
"""
if __name__ == "__main__":

    decimal_pi = get_decimal_pi()

    # plt.hist(decimal_pi, range(11), color = '#3498db', edgecolor='#2980b9', align='left', rwidth=0.8)

    digit = 3
    gap_range = GAP_RANGE
    gap_exp = len_gap(decimal_pi, digit)
    gap_thq = proba_gap(gap_range)

    poker_exp = poker(decimal_pi)
    poker_thq = proba_poker(5, 10)

    # print('\\begin{center}\n\\begin{tabular}{|c|c|c|c|}\n\\hline')
    # for i in GAP_RANGE:
    #     s = str(gap_thq.count(i)) + ' & ' + str(gap_exp.count(i)) + '\\\\'
    #     print(s)
    #     print('\\hline')
    # print('\\hline\n\\end{tabular}{}\\end{center}')

    # plt.hist([gap_exp, gap_thq], GAP_RANGE, color = ['yellow', 'green'],
    #     edgecolor='red', hatch='.', label=['Exp', 'Thq'], histtype='bar') #test du poker
    # plt.legend()
    # plt.show()
    # t = []

    # for i in range(10):
    #     temp = [i]
    #     temp*=int(0.1*1000000)
    #     t.append(temp)

    # for i in range(10):
    #plt.hist([poker_exp, poker_thq], color = ['#3498db', '#1abc9c'], edgecolor='#2c3e50', label=['Exp', 'Thq'])
    #plt.xlabel('Main r')
    #plt.ylabel('Frequence')
    #plt.title('Histogramme des mains k')
    #plt.legend()
    #plt.show()

    '''
    Test du chi2
    '''

    simple_proba_dict = {}
    for i in range(10):
        simple_proba_dict[i] = 0.1

    #print(format_latex(chi_2_test(decimal_pi, simple_proba_dict, 9), '$\\alpha$' , '$K_r$', '$\\chi_2$', '$Test$'))

    '''
    Test du gap
    '''

    # for i in range(10):
    #     print("Test du gap pour", i)
    #     print(format_latex(gap_test_digit(decimal_pi, i), '$\\alpha$' , '$K_r$', '$\\chi^2$', '$Test$'))
    #     print('\n%-----------------------------\n')

    '''
    Test du poker
    '''

    #print(format_latex(poker_test(decimal_pi), '$\\alpha$' , '$K_r$', '$\\chi^2$', '$Test$'))