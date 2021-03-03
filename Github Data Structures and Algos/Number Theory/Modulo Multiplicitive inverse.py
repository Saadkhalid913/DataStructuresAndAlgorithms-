def ModMulcInverse(n, m):
    for i in range(1, m):
        if n * i % m == 1:
            return i

    return 1
