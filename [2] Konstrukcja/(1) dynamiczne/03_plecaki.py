# 3) Plecaki

# Mamy do dyspozycji tablicę przedmiotów, z których każdy ma swoją wartość i wagę.
# Należy wskazać maksymalną wartość przedmiotów które można zabrać bez przekraczania 
# określonej sumarycznej wagi. Wagi są liczbami naturalnymi!

import math


# items[n][0] - waga;   items[n][1] - wartość
def f(items, i, w, pomoc):
    if w < 0:
        return -math.inf
    if i < 0 or w == 0:
        return 0
    if pomoc[i][w] == -1:
        pomoc[i][w] = max(f(items, i-1, w, pomoc), f(items, i-1, w - items[i][0], pomoc) + items[i][1])
    return pomoc[i][w]


def zad(items, w):
    n = len(items)
    p = [[-1 for _ in range(w)] for _ in range(n)]
    return f(items, n-1, w, p)
  
