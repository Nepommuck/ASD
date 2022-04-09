# 2) Impreza 

# Impreza jest dopuszczalna jeśli dla żadnego zaproszonego pracownika, jego szef nie został zaproszony. 
# Wartością imprezy jest suma współczynników 'fun' zaproszonych.
# Należy znaleźć wartość najlepszej legalnej imprezy.


class Employee:
    def __init__(self, fun):
        self.fun = fun
        # podwładni
        self.emp = []


def best_party(boss):
    return f(boss)


# zwraca najlepszą możliwą imprezę z prac i podwładnych
def f(prac):
    if len(prac.emp) == 0:
        return prac.fun
    a = 0
    for p in prac.emp:
        a += f(p)
    return max(a, g(prac))


# zwraca najlepszą możliwą imprezę z podwładnych prac
def g(prac):
    if len(prac.emp) == 0:
        return 0
    a = 0
    for p in prac.emp:
        a += f(p)
    return a
