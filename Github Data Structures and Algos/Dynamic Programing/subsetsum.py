def subsetsum(s, n, sm):
    DP = []
    for i in range(n + 1):
        DP.append([])
        for j in range(sm+1):
            DP[i].append(False)

    for i in range(n+1):
        DP[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sm + 1):
            if j >= s[i-1]:
                DP[i][j] = DP[i-1][j-s[i-1]] or DP[i-1][j]
            if j < s[i-1]:
                DP[i][j] = DP[i-1][j]

    for i in range(1, n + 1):
        if DP[i][1]:
            return True


print(subsetsum([1, 2, 3, 4, 5], 5, 10))
