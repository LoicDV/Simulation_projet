import new_pi as pi
import datetime

list_value = pi.get_decimal_pi()

def randFloat(decimal_number):
    floating = ""
    for i in range(decimal_number):
        time = datetime.datetime.now().microsecond
        digit = (time*36170)%(2**20)
        index = digit/(2**20)
        index *= 1000000
        digit_result = list_value[int(index)]
        floating += str(digit_result)
    our_float = float('0.' + floating)
    return our_float

if __name__ == "__main__":
    """
    for __ in range(5):
        list_test = []
        for _ in range(1000000):
            number = randFloat(3)
            list_test.append(number)
        dict_test = pi.occ_number(list_test)
        maxi = dict_test[0]
        mini = dict_test[0]
        for elem in dict_test:
            if maxi < dict_test[elem]:
                maxi = dict_test[elem]
            if mini > dict_test[elem]:
                mini = dict_test[elem]
        print(maxi)
        print(mini)
        print("--------")
    """
    pass