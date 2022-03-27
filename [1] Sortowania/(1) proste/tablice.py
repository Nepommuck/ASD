def bubble_sort(tab, l):
    for i in range(l-1, -1, -1):
        for k in range(i):
            if tab[k] > tab[k+1]:
                tab[k], tab[k+1] = tab[k+1], tab[k]


def insersion_sort(tab, l):
    for i in range(1, l):
        buf = tab[i]
        k = i-1
        while tab[k] > buf and k >= 0:
            tab[k+1] = tab[k]
            k -= 1
        tab[k+1] = buf


def selection_sort(tab, l):
    for i in range(l-1):
        ind = i+1
        min = tab[ind]
        for k in range(i+2, l):
            if tab[k] < min:
                ind = k
                min = tab[k]
        tab[ind], tab[i] = tab[i], tab[ind]
