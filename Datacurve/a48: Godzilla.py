def godzilla_path(city: list[list[int]]) -> int:
    def printdp(dp):
        for row in dp:
            print(row)
    printdp(city)
    if not city:
        raise ValueError('city must be a 2d list of building heights')

    n, m = len(city), len(city[0])
    dp = city.copy()

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            to_add = 10**9
            if i > 0:
                to_add = min(to_add, dp[i-1][j])

            if j > 0:
                to_add = min(to_add, dp[i][j-1])

            dp[i][j] += to_add

    print()
    printdp(dp)
    return dp[-1][-1]


# assert godzilla_path([[0]]) == 0, "Test case 1 failed"

# assert godzilla_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#                      ) == 21, "Test case 3 failed"

assert godzilla_path([[3, 2, 1], [0, 1, 0], [0, 2, 3]]
                     ) == 3, "Test case 4 failed"
