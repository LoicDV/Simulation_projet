import new_pi as pi
import datetime
import random
import math

list_value = pi.get_decimal_pi()

def randFloat(decimal_number):
    floating = ""
    for __ in range(decimal_number):
        time = datetime.datetime.now().microsecond
        digit = (time*36170)%(2**32)
        index = digit/(2**32)
        index *= 1000000
        digit_result = list_value[int(index)]
        floating += str(digit_result)
    our_float = float('0.' + floating)
    return our_float

def generator_random(decimal_number):
    number = random.random()
    number = math.floor(number*(10**decimal_number))/(10**decimal_number)
    return number

if __name__ == "__main__":
    with open ('test.txt', 'w') as f:
        for ___ in range(1, 11):
            k = 300000
            n = 3

            title = "test " + str(___) + ":"
            print(title)
            f.write(title + " avec " + str(k) + " nombres générés et " + str(n) + " décimales." + '\n')

            """Notre générateur :"""
            list_test_us = []
            list_test_util_us = []
            for __ in range(k):
                number = randFloat(n)
                list_test_us.append(number)
                number *= (10**n)
                list_test_util_us.append(int(number))
            dict_test_us = pi.occ_number(list_test_util_us)
            dict_test_9_us = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
            for i in range(len(list_test_us)):
                tmp = list_test_us[i] * 10
                if 0 <= tmp and tmp < 1:
                    dict_test_9_us[0] += 1
                elif 1 <= tmp and tmp < 2:
                    dict_test_9_us[1] += 1
                elif 2 <= tmp and tmp < 3:
                    dict_test_9_us[2] += 1
                elif 3 <= tmp and tmp < 4:
                    dict_test_9_us[3] += 1
                elif 4 <= tmp and tmp < 5:
                    dict_test_9_us[4] += 1
                elif 5 <= tmp and tmp < 6:
                    dict_test_9_us[5] += 1
                elif 6 <= tmp and tmp < 7:
                    dict_test_9_us[6] += 1
                elif 7 <= tmp and tmp < 8:
                    dict_test_9_us[7] += 1
                elif 8 <= tmp and tmp < 9:
                    dict_test_9_us[8] += 1
                elif 9 <= tmp and tmp < 10:
                    dict_test_9_us[9] += 1

            """Random :"""
            list_test_random = []
            list_test_util_random = []
            for __ in range(k):
                number = generator_random(n)
                list_test_random.append(number)
                number *= (10**n)
                list_test_util_random.append(int(number))
            dict_test_random = pi.occ_number(list_test_util_random)
            dict_test_9_random = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
            for i in range(len(list_test_us)):
                tmp = list_test_us[i] * 10
                if 0 <= tmp and tmp < 1:
                    dict_test_9_random[0] += 1
                elif 1 <= tmp and tmp < 2:
                    dict_test_9_random[1] += 1
                elif 2 <= tmp and tmp < 3:
                    dict_test_9_random[2] += 1
                elif 3 <= tmp and tmp < 4:
                    dict_test_9_random[3] += 1
                elif 4 <= tmp and tmp < 5:
                    dict_test_9_random[4] += 1
                elif 5 <= tmp and tmp < 6:
                    dict_test_9_random[5] += 1
                elif 6 <= tmp and tmp < 7:
                    dict_test_9_random[6] += 1
                elif 7 <= tmp and tmp < 8:
                    dict_test_9_random[7] += 1
                elif 8 <= tmp and tmp < 9:
                    dict_test_9_random[8] += 1
                elif 9 <= tmp and tmp < 10:
                    dict_test_9_random[9] += 1

            """Test de Chi2 avec degré = 9"""
            """Notre générateur :"""
            dict_proba_chi2_9_us = pi.proba_dict_chi2(len(dict_test_9_us), dict_test_9_us)
            list_final_chi2_9_us = pi.test_chi2(len(list_test_us), list_test_us, dict_test_9_us, dict_proba_chi2_9_us, len(dict_test_9_us)-1)
            f.write("Test de Chi2 avec degré = 9" + '\n')
            f.write("Notre générateur :" + '\n')
            string = "".join(str(elem) for elem in list_final_chi2_9_us)
            f.write(string + '\n')
            """-----------------------------------------------------"""
            """Random :"""
            dict_proba_chi2_9_random = pi.proba_dict_chi2(len(dict_test_9_random), dict_test_9_random)
            list_final_chi2_9_random = pi.test_chi2(len(list_test_random), list_test_random, dict_test_9_random, dict_proba_chi2_9_random, len(dict_test_9_random)-1)
            f.write("random de python :" + '\n')
            string = "".join(str(elem) for elem in list_final_chi2_9_random)
            f.write(string + '\n')
            """-----------------------------------------------------"""
            """-----------------------------------------------------"""
            """Test de Chi2 avec degré = len(dict_test_us) - 1"""
            """Notre générateur :"""
            """
            dict_proba_chi2_us = pi.proba_dict_chi2(len(dict_test_us), dict_test_us)
            list_final_chi2_us = pi.test_chi2(len(list_test_us), list_test_us, dict_test_us, dict_proba_chi2_us, len(dict_test_us)-1)
            f.write("Test de Chi2" + '\n')
            f.write("Notre générateur :" + '\n')
            string = "".join(str(elem) for elem in list_final_chi2_us)
            f.write(string + '\n')
            """
            """-----------------------------------------------------"""
            """Random :"""
            """
            dict_proba_chi2_random = pi.proba_dict_chi2(len(dict_test_random), dict_test_random)
            list_final_chi2_random = pi.test_chi2(len(list_test_random), list_test_random, dict_test_random, dict_proba_chi2_random, len(dict_test_random)-1)
            f.write("random de python :" + '\n')
            string = "".join(str(elem) for elem in list_final_chi2_random)
            f.write(string + '\n')
            """
            """-----------------------------------------------------"""
            """-----------------------------------------------------"""
            """ Test du Gap """
            """ Notre générateur :"""
            """
            a = 0   #float(input("a dans [0, 1[ : "))
            b = 0.5   #float(input("b dans ]0, 1] avec a < b : "))
            list_final_gap_us = pi.test_gap(a, b, list_test_us)
            string = "".join(str(elem) for elem in list_final_gap_us)
            f.write("Test du gap" + '\n')
            f.write("Notre générateur :" + '\n')
            f.write(string + '\n')
            """
            """ Random :"""
            """
            list_final_gap_random = pi.test_gap(a, b, list_test_random)
            string = "".join(str(elem) for elem in list_final_gap_random)
            f.write("random de python :" + '\n')
            f.write(string + '\n')
            """
            """-----------------------------------------------------"""
            """-----------------------------------------------------"""
            """ Test du Poker """
            """ Notre générateur :"""
            """
            list_final_poker_us = pi.test_poker(list_test_util_us)
            string = "".join(str(elem) for elem in list_final_poker_us)
            f.write("Test du poker" + '\n')
            f.write("Notre générateur :" + '\n')
            f.write(string + '\n')
            """
            """ Random :"""
            """
            list_final_poker_random = pi.test_poker(list_test_util_random)
            string = "".join(str(elem) for elem in list_final_poker_random)
            f.write("random de python :" + '\n')
            f.write(string + '\n')
            """