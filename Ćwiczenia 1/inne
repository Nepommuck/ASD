# Funckcja która znajduje minimalny i maksymalny element tablicy wykonując jedynie (3/2)n porównań
def find_min_max(tab):
    n = len(tab)
    if n == 0:
        return None, None
    if n == 1:
        return tab[0], tab[0]
    
    for i in range(0, n-1, 2):
        if tab[i] > tab[i+1]:
            tab[i], tab[i+1] = tab[i+1], tab[i]
    mn = tab[0]
    mx = tab[1]
    
    for i in range(2, n, 2):
        if tab[i] < mn:
            mn = tab[i]
    for i in range(3, n, 2):
        if tab[i] > mx:
            mx = tab[i]
    return mn, mx


# Tablica wypełniona jest naturalnymi (bez 0), a jej elementy się nie powtarzają.
# Znajdź najmniejszą liczbę naturalną której nie ma w tablicy. [czas: log(n)]
# np. (1, 2, 3, 4, 6, 12, 90) -> 5
def zad2(tab):
    n = len(tab)
    if n == 0 or tab[0] > 1:
        return 1
    if n == 1:
        return 2
    if tab[n-1] == n:
        return n+1
    
    a = 0
    b = n-1
    while a+1 < b:
        s = (a+b) // 2
        if tab[s] == s+1:
            a = s
        else:
            b = s
    return a+2
