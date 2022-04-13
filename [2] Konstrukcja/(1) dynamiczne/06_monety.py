# (6) Wydawanie monet
#
# W tablicy M znajdują się dostępne monety. Mamy za zadanie wydać kwotę K. Należy:
# 1. Zwrócić najmniejszą liczbę monet aby tego dokonać
# 2. Wypisać których monet należy użyc


import math
import helpful


def f(monety, kwot, pom):
    if kwot == 0:
        return 0
    if kwot < 0:
        return math.inf
    if pom[kwot] < 0:
        mn = math.inf
        for i in range(len(monety)):
            mn = min(mn, f(monety, kwot - monety[i], pom))
        pom[kwot] = mn + 1
    return pom[kwot]


# Zadanie 1
def zad1(M, K):
    pom = [-1 for _ in range(K+1)]
    rez = f(M, K, pom)
    if rez == math.inf:
        return None
    return rez


# wypisywanie
def g(monety, kwot, counter, saver):
    if kwot == 0:
        return 0
    if kwot < 0:
        return math.inf

    n = len(monety)
    if counter[kwot] < 0:
        mn = math.inf
        mn_i = -1
        for i in range(n):
            rez = g(monety, kwot - monety[i], counter, saver)
            if rez < mn:
                mn = rez
                mn_i = i
        counter[kwot] = mn + 1
        if mn_i >= 0:
            for i in range(n):
                saver[kwot][i] = saver[kwot - monety[mn_i]][i]
            saver[kwot][mn_i] += 1
    return counter[kwot]


# Zadanie 2
def zad2(M, K):
    n = len(M)
    coun = [-1 for _ in range(K+1)]
    sav = [[0 for _ in range(n)] for _ in range(K+1)]

    g(M, K, coun, sav)
    # print(sav[K])
    print(f"Aby otrzymać {K} użyto {coun[K]} monet: ")
    for i in range(n):
        r = sav[K][i]
        if r > 0:
            print(f"Moneta ({mon[i]}):  {r} razy")
    print()


if __name__ == '__main__':
    mon = [2, 3, 4, 10, 12, 15]
    for i in range(2, 20):
        # print(i, zad1(mon, i))
        zad2(mon, i)
