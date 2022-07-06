from zad2testy import runtests


class Node:
    def __init__(self):
        self.counter = 0
        self.left = None
        self.right = None

    def add_to_tree(self, nap):
        self.counter += 1
        p = self
        for let in nap:
            if let == '0':
                if p.left is None:
                    p.left = Node()
                p = p.left
            else:
                if p.right is None:
                    p.right = Node()
                p = p.right
            p.counter += 1


def get_rez(nod, akt, rez):
    l = 0 if nod.left is None else nod.left.counter
    r = 0 if nod.right is None else nod.right.counter

    if l < 2 and r < 2 and nod.counter >= 2:
        rez.append(akt)
    if l >= 2:
        get_rez(nod.left, akt+'0', rez)
    if r >= 2:
        get_rez(nod.right, akt+'1', rez)


def debug_tree(nod, akt):
    if nod is not None:
        print(f'{akt}:  {nod.counter}')

        debug_tree(nod.left, akt + '0')
        debug_tree(nod.right, akt + '1')


def double_prefix(L):
    tree = Node()
    for nap in L:
        tree.add_to_tree(nap)

    # debug_tree(tree, '')

    odp = []
    get_rez(tree, '', odp)
    return odp


runtests( double_prefix )
