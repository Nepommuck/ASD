#
#       3
#       |
#   2 ----- 0
#       |
#       1
#
import math
import queue


def valid(L, y0, x0):
    y = len(L)
    x = len(L[0])
    if not (0 <= x0 < x and 0 <= y0 < y):
        return False
    if L[y0][x0] == 'X':
        return False
    return True


def ystep(y, kier):
    if kier == 1:
        return y + 1
    if kier == 3:
        return y - 1
    return y


def xstep(x, kier):
    if kier == 0:
        return x + 1
    if kier == 2:
        return x - 1
    return x


def gener_array(elem, y, x, cop=False, kier=4, szyb=3):
    mat = [
        [
            [
                [
                    elem.copy() if cop else elem for _ in range(szyb)
                ] for _ in range(kier)
            ] for _ in range(x)
        ] for _ in range(y)
    ]
    return mat


def robot(L, A, B):
    rot = 45
    pace = [60, 40, 30]

    w = len(L)
    k = len(L[0])

    # mat[y][x][kier][szyb]
    mat = gener_array([], w, k, True)

    for y in range(w):
        for x in range(k):
            for kier in range(4):
                for szyb in range(3):

                    if valid(L, y, x):
                        mat[y][x][kier][szyb].append(
                            (y, x, (kier + 1) % 4, 0, rot)
                        )
                        mat[y][x][kier][szyb].append(
                            (y, x, (kier - 1) % 4, 0, rot)
                        )

                        y1 = ystep(y, kier)
                        x1 = xstep(x, kier)
                        if valid(L, y1, x1):
                            mat[y][x][kier][szyb].append(
                                (y1, x1, kier, min(2, szyb + 1), pace[szyb])
                            )
    # for y in range(w):
    #     for x in range(k):
    #         for kier in range(4):
    #             for szyb in range(3):
    #                 print("Vertex: ", y, x, kier, szyb)
    #                 print(mat[y][x][kier][szyb])

    # DIJKSTA
    x0, y0 = A
    dis = gener_array(math.inf, w, k)
    visited = gener_array(False, w, k)

    dis[y0][x0][0][0] = 0

    pq = queue.PriorityQueue()

    # (dis, y, x, kier, szyb)
    pq.put((0, y0, x0, 0, 0))
    while not pq.empty():
        d, y, x, kier, szyb = pq.get()
        # print("Przetw: ", d, y, x, kier, szyb)
        if not visited[y][x][kier][szyb]:

            # (y1, x1, kier, min(2, szyb + 1), pace[szyb])
            for (y1, x1, kier1, szyb1, edge) in mat[y][x][kier][szyb]:
                # print("found: ", y1, x1, kier1, szyb1, edge)
                # Relax
                if dis[y1][x1][kier1][szyb1] > d + edge:
                    dis[y1][x1][kier1][szyb1] = d + edge
                    pq.put(
                        (dis[y1][x1][kier1][szyb1], y1, x1, kier1, szyb1)
                    )

            visited[y][x][kier][szyb] = True

    # DEBUG
    # Printowanie najkrotszych dystansow do kazdego pola
    for row in dis:
        for item in row:
            mn = math.inf
            for i in range(4):
                for k in range(3):
                    mn = min(mn, item[i][k])
            print(mn, end=' ')
        print("")

    rez = math.inf
    x1, y1 = B
    for i in range(4):
        for k in range(3):
            rez = min(rez, dis[y1][x1][i][k])

    if math.isinf(rez):
        return None
    return rez


if __name__ == '__main__':
    labirynt1 = [
        "XXXXXXXXXXXXXX",
        "X X          X",
        "X XXX XXXX   X",
        "X            X",
        "XXXXXXXXXXXXXX"
    ]

    print(
        robot(labirynt1, (1, 1), (8, 3))
    )
