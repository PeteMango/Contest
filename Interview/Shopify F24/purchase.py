from collections import defaultdict


def solve(inp) -> int:
    soda: float = 2.5
    popcorn: float = 8

    d: defaultdict = defaultdict(lambda: defaultdict(int))

    for date, purchase in inp:
        d[date][purchase] += 1

    ans: float = 0
    for _, purchases in d.items():
        pop, soda = purchases["popcorn"], purchases["soda"]
        bundle = min(pop, soda)
        ans += 9 * bundle + (pop - bundle) * 8 + (soda - bundle) * 2.5

    return ans


inp = [["10212021", "popcorn"], ["10222021", "popcorn"], [
    "10212021", "soda"], ["10212021", "popcorn"], ["10212021", "soda"]]


ret = solve(inp)

print(ret)
