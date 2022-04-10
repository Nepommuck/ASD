# (4) Podciąg o zadanej sumie

# Ciąg składa się z nieujemnych liczb całkowitych zapisanych w tablicy T.
# Czy istnieje podciąg o sumie N?


def f(tab, i, summ, pomoc):
    if summ == 0:
        return True
    if i < 0 or summ < 0:
        return False
    if pomoc[i][summ] is None:
        pomoc[i][summ] = f(tab, i-1, summ, pomoc) or f(tab, i-1, summ - tab[i], pomoc)
    return pomoc[i][summ]


def zad(T, N):
    l = len(T)
    pom = [[None for _ in range(N+1)] for _ in range(l)]
    return f(T, l-1, N, pom)
