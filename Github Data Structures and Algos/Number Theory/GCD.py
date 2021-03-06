def GCD(m, n):
    if m == 0:
        return n
    return GCD(n % m, m)


print(GCD(21, 14))
