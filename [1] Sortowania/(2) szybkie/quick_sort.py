def quick_sort(tab, p, k):
    if p < k:
        a = p
        for i in range(p, k):
            if tab[i] < tab[k]:
                swap(tab, i, a)
                a += 1
        swap(tab, k, a)
        quick_sort(tab, p, a-1)
        quick_sort(tab, a+1, k)
