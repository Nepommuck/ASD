from kolutesty import runtests
import collections
import math


def add_file(file, disk, ob, this_turn, next_turn):
    this_turn.append(file) if disk[file] == ob else next_turn.append(file)


def swaps(disk, depends):
    n = len(disk)

    rez = math.inf
    for ob in ['A', 'B']:
        needs = [
            [
                False for _ in range(n)
            ] for _ in range(n)
        ]
        needs_counter = [
            0 for _ in range(n)
        ]
        for i in range(n):
            needs_counter[i] = len(depends[i])
        allows = [
            [] for _ in depends
        ]
        for i in range(n):
            for k in depends[i]:
                allows[k].append(i)
                needs[i][k] = True

        this_turn = collections.deque()
        next_turn = collections.deque()

        for i in range(n):
            if not depends[i]:
                add_file(i, disk, ob, this_turn, next_turn)

        counter = -1
        while this_turn or next_turn:
            while this_turn:
                plik = this_turn.pop()
                for neib in allows[plik]:
                    needs[neib][plik] = False
                    needs_counter[neib] -= 1
                    if needs_counter[neib] <= 0:
                        add_file(neib, disk, ob, this_turn, next_turn)
            # A <-> B
            ob = chr(((ord(ob)-ord('A')+1) % 2) + ord('A'))
            this_turn = next_turn
            next_turn = collections.deque()
            counter += 1
        rez = min(rez, counter)

    return rez


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True )
