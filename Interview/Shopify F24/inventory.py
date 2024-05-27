from sortedcontainers import SortedList
from bisect import bisect_right

J = [('Toronto', 5), ('Vancouver', 10),
     ('Montreal', 3), ('Calgary', 1), ('Halifax', 28)]

H = [('Toronto', 0), ('Vancouver', 2),
     ('Montreal', 5), ('Calgary', 18), ('Halifax', 2)]

S = [('Toronto', 0), ('Vancouver', 6),
     ('Montreal', 5), ('Calgary', 2), ('Halifax', 12)]


def solve(J, H, S) -> list[str]:
    j, h, s = 3, 2, 4
    a, b, c = SortedList(), SortedList(), SortedList()
    for key, val in J:
        a.add((val, key))

    for key, val in H:
        b.add((val, key))

    for key, val in S:
        c.add((val, key))

    def key_func(t):
        return t[0]

    idxa = bisect_right(a, j, key=key_func)
    idxb = bisect_right(b, h, key=key_func)
    idxc = bisect_right(c, s, key=key_func)

    seta = set([t[1] for t in a[idxa:]])
    setb = set([t[1] for t in b[idxb:]])
    setc = set([t[1] for t in c[idxc:]])

    print(seta)
    print(setb)
    print(setc)

    return list(seta.intersection(setb).intersection(setc))


ret = solve(J, H, S)
print(ret)
# ["van", "mon", "hali"]

inp2 = {"H": 7, "S": 1}
# ret = solve(J, H, S, inp2)
print(ret)
# ["cal"]
