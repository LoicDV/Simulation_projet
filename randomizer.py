import new_pi as pi
import datetime
import random
import math

list_value = pi.get_decimal_pi()

def randFloat(decimal_number):
    floating = ""
    for i in range(decimal_number):
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
        for ___ in range(1, 101):
            print("test " + str(___) + ":" )
            n = 5

            list_test_us = []
            list_test_util_us = []
            for __ in range(1000000):
                number = randFloat(n)
                list_test_us.append(number)
                number *= (10**n)
                list_test_util_us.append(int(number))
            dict_test_us = pi.occ_number(list_test_util_us)
            """
            list_test_random = []
            list_test_util_random = []
            for __ in range(1000):
                number = generator_random(n)
                list_test_random.append(number)
                number *= (10**n)
                list_test_util_random.append(int(number))
            dict_test_random = pi.occ_number(list_test_util_random)
            """
            """Test de Chi2"""
            """Notre générateur :"""
            dict_proba_chi2_us = pi.proba_dict_chi2(len(dict_test_us), dict_test_us)
            list_final_chi2_us = pi.test_chi2(len(list_test_us), list_test_us, dict_test_us, dict_proba_chi2_us, len(dict_test_us)-1)
            f.write("Test de Chi2" + '\n')
            f.write("Notre générateur :" + '\n')
            kr = pi.Kr(len(list_test_us), dict_test_us, dict_proba_chi2_us)
            f.write(str(kr) + '\n')
            string = "".join(str(elem) for elem in list_final_chi2_us)
            f.write(string + '\n')
            """-----------------------------------------------------"""
            """Random :"""
            """
            dict_proba_chi2_random = pi.proba_dict_chi2(len(dict_test_random), dict_test_random)
            list_final_chi2_random = pi.test_chi2(len(list_test_random), list_test_random, dict_test_random, dict_proba_chi2_random, len(dict_test_random)-1)
            f.write("Test de Chi2" + '\n')
            f.write("random de python :" + '\n')
            string = "".join(str(elem) for elem in list_final_chi2_random)
            f.write(string + '\n')
            """
            """-----------------------------------------------------"""
            """-----------------------------------------------------"""