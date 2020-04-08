import datetime
import utils_pi as ppi

class Random(object):

    xn = 0
    pi = []
    counter = 0

    def __init__(self):
        self.xn = datetime.datetime.now().microsecond
        self.pi = ppi.get_decimal_pi()

    def nextRand(self, acc = 5):
        """Retourne un nombre aléatoire compris entre O et 1 (non compris)

        Args:
            acc (int, optional): la précision du nombre aléatoire. Defaults to 5.

        Returns:
            float: un nombre appartenant à [0,1[
        """
        ret = ''
        for _ in range(acc):
            self.xn =  16807*(self.xn)%((2**31)-1)
            index = self.xn/float((2**31)-1)
            index *= 1000000
            decimal = self.pi[int(index)]
            ret += str(decimal)
        ret = '0.' + ret
        return float(ret)

    def nextInt(self, acc = 5):
        """Retourne un nombre aléatoire compris entre O et le nombre maximum à acc digit (non compris)


        Args:
            acc (int, optional): la précision du nombre aléatoire. Defaults to 5.

        Returns:
            int: un nombre appartenant à [0,nombre max à acc digit[
        """
        ret = ''
        for _ in range(acc):
            self.xn =  16807*(self.xn)%((2**31)-1)
            index = self.xn/float((2**31)-1)
            index *= 1000000
            decimal = self.pi[int(index)]
            ret += str(decimal)
        return int(ret)

    def prob(self, l=10):
        ret = {}
        for i in range(l):
            ret[i] = 1./l
        return ret

    def probInt(self, acc=5):
        s = ''
        ret = {}
        for _ in range(acc):
            s+='9'
        limit = int(s)+1
        for i in range(limit):
            ret[i] = 1./limit
        print(limit)
        return ret

if __name__ == "__main__":
    rand = Random()

    import matplotlib.pyplot as plt
    import random as truc

    x = []

    ra = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    t = []

    X = []
    Y = []
    random = []

    print('Generating theorical...')
    for i in range(10):
        temp = [i]
        temp*=int(0.1*10000)
        t.append(temp)

    print('Finished theorical.')
    print('Generating random numbers...')
    stopX, stopY = False, False
    for i in range(1000000):
        if i == 10000:
            stopX = True
        if i == 100000:
            stopY = True
        n = rand.nextRand()
        if not stopX:
            X.append(n)
        if not stopY:
            Y.append(n)
        random.append(n)
        for index in range(len(ra)-1):
            if n >= ra[index] and n < ra[index+1]:
                x.append(index)

    print('Finished random generators')

    # print(x)
    print('Calculating kolmogorv-smirnov')
    # Y.sort()
    # plt.plot(Y)
    # plt.plot(np.arange(0, 1, 1./len(Y)))
    # plt.show()

    # print('For 10.000...')
    # print(format_latex(KS(X), '$\\alpha$', '$D_n$', '$D_\\alpha$', '$Test$'))
    # print('For 100.000...')
    # print(format_latex(KS(Y), '$\\alpha$', '$D_n$', '$D_\\alpha$', '$Test$'))
    # print('For 1.000.000...')
    # print(format_latex(KS(random), '$\\alpha$', '$D_n$', '$D_\\alpha$', '$Test$'))
    print('Finish kolmogorv-smirnov')

    # plt.hist([x, t], rwidth=0.9)
    # plt.show()

    # for i in range(100):
    #     print(datetime.datetime.now().microsecond)


    r = truc.Random()
    z = []
    for _ in range(10000):
        z.append(r.uniform(0, 1))

    print(format_latex(poker_test(z, True), '$\\alpha$' , '$K_r$', '$\\chi^2$', '$Test$'))

    # print(format_latex(chi_2_test(x, rand.prob(), 9), '\\alpha' , 'Kr', '$\\chi^2$', 'Test'))

