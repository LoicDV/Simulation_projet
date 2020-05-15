import matplotlib.pyplot as plt
import new_pi as pi
import randomizer

def dict_gap(a, b, list_value, pi2):
    if (a >= b) or (a < 0) or (b > 1):
        raise Exception("a, b have to be in [0, 1].")
    if pi2 and b > 0.9:
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
    dict_value = pi.occ_number(list_gap)
    return dict_value

def dict_poker(list_value, poker, k=5, d=10):
    list_poker = []
    list_test_poker = []
    for elem in list_value:
        list_test_poker.append(elem)
        if len(list_test_poker) == k:
            number = len(pi.occ_number(list_test_poker))
            list_poker.append(number)
            list_test_poker = []
    dict_value = pi.occ_number(list_poker)
    return dict_value

def histo_chi2(liste):
    titre ="Histogramme sur les décimales de pi en fonction de leur occurence."
    plt.figure()
    plt.hist(liste, bins=10)
    plt.xlabel("Valeur des digits")
    plt.ylabel("Nombre d'occurence")
    plt.title(titre)
    plt.show()

def histo_gap(dict_histo):
    titre ="Histogramme sur les décimales de pi en fonction de leur occurence dans l'intervalle [0, 0.5]"
    plt.figure()
    plt.bar(dict_histo.keys(), dict_histo.values())
    plt.xlabel("Valeur des longueurs")
    plt.ylabel("Nombre d'occurence")
    plt.title(titre)
    plt.show()

def histo_poker(dict_histo):
    titre ="Histogramme sur les décimales de pi en fonction de leur occurence dans l'intervalle [0, 0.5]"
    plt.figure()
    plt.bar(dict_histo.keys(), dict_histo.values())
    plt.xlabel("Valeur des longueurs")
    plt.ylabel("Nombre d'occurence")
    plt.title(titre)
    plt.show()

if __name__ == "__main__":
    list_pi = pi.get_decimal_pi()
    print("(1) Test de Chi2 avec deg 9 :")
    print("(2) Test de Chi2 avec deg len(dict_value)-1 :")
    print("(3) Test du Gap :")
    print("(4) Test du Poker :")
    print("(5) Exit")
    number_test = int(input("Quel test voulez-vous ?" + '\n'))
    if number_test != 1 and number_test != 2 and number_test != 3 and number_test != 4 and number_test != 5:
        raise Exception("Vous n'entrez pas un bon numéro.")
    elif number_test == 1:
        histo_chi2(list_pi)
    elif number_test == 2:
        a = 0
        b = 0.5
        for i in range(len(list_pi)):
            list_pi[i] /= 10
        dict_histo = dict_gap(a, b, list_pi, True)
        histo_gap(dict_histo)
    elif number_test == 3:
        a = 0.5
        b = 1
        for i in range(len(list_pi)):
            list_pi[i] /= 10
        dict_histo = dict_gap(a, b, list_pi, True)
        histo_gap(dict_histo)
    elif number_test == 4:
        dict_histo = dict_poker(list_pi, False)
        histo_poker(dict_histo)
    else:
        exit()