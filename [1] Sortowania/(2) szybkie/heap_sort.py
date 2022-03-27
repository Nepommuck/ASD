def swap(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i-1) // 2


def heapify(T, n, i):
    mx = i
    l = left(i)
    r = right(i)
    if l < n and T[l] > T[mx]:
        mx = l
    if r < n and T[r] > T[mx]:
        mx = r
    if mx > i:
        swap(T, i, mx)
        heapify(T, n, mx)


def build_heap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)


def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n-1, 0, -1):
        swap(T, 0, i)
        heapify(T, i, 0)
