# 1) Najdluższy rosnący podciąg

# Znaleźć najdłuższy (niespójny) podciąg rosnący w tablicy. 
# Wypisać jego 1) dlugość, 2) elementy


# rozwiązanie na poziomie WDI - złożoność O(2^n)
def lis_wdi(tab, i=0, akt=-float('inf'), ile=0):
    if i >= len(tab):
        return ile
    a = lis_wdi(tab, i+1, akt, ile)
    if akt >= tab[i]:
        return a
    return max(a, lis_wdi(tab, i+1, tab[i], ile+1))


# 1)
def lis(tab):
    n = len(tab)
    # dlugosci dla danego elementu
    L = [1 for i in range(n)]
    for i in range(1,n):
        for k in range(i):
            if tab[k] < tab[i]:
                L[i] = max(L[i], L[k]+1)
    mx = L[0]
    for i in range(1, n):
        mx = max(mx, L[i])
    return mx


# 2) wersja z wypisywaniem
def p_lis(tab):
    n = len(tab)
    # dlugosci dla danego elementu
    L = [1 for i in range(n)]
    prev = [-1 for i in range(n)]
    for i in range(1, n):
        for k in range(i):
            if tab[k] < tab[i] and L[k]+1 > L[i]:
                L[i] = L[k]+1
                prev[i] = k
    mxind = 0
    for i in range(1, n):
        if L[mxind] < L[i]:
            mxind = i
    print(f'Podciąg ma {L[mxind]} elemen.: \n({tab[mxind]}', end='')
    print_lis(tab, prev, prev[mxind])
    print(')')


def print_lis(tab, prev, i):
    if i >= 0:
        print_lis(tab, prev, prev[i])
        print(',', tab[i], end= '')
